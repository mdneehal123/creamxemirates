// POST /api/order: Cash on Delivery order.
// 1) price from the server pack list, 2) Delhivery checks the pincode accepts COD (if not, the page offers online payment),
// 3) the parcel is booked with Delhivery, 4) the order is saved in the Order Desk with the Delhivery tracking number (AWB).
// If Delhivery is not set up or the booking fails, the order is still saved, flagged "book in Delhivery manually".
const D = require('./_desk');
const { delhiveryOn, serviceable, bookCod } = require('./_delhivery');

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'method_not_allowed' });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  if (b.website) return res.status(200).json({ ok: true, ref: 'CX' }); // hidden field: bots fill it, people don't
  const pack = D.packById(b.pack), c = D.customer(b);
  if (!pack || !c) return res.status(400).json({ ok: false, error: 'invalid_details' });
  const ref = D.newRef(b.ref);
  const total = pack.price + (D.CFG.codFee || 0); // pack price + COD charge

  let booked = null, warn = '';
  if (delhiveryOn()) {
    let s = null;
    try { s = await serviceable(c.pin); } catch (e) { s = null; }
    if (s && (!s.known || !s.cod)) {
      return res.status(409).json({ ok: false, error: 'cod_unavailable', message: 'Cash on Delivery is not available for this pincode. Please pay online.' });
    }
    if (!s) warn = '⚠ Delhivery pincode check did not answer. ';
    if (s && s.state && !c.state) c.state = s.state;
    booked = await bookCod({ ref, c, pack, total, product: D.CFG.product + ' ' + D.CFG.size + ' · ' + pack.label });
    if (!booked.ok) warn += '⚠ Delhivery booking failed (' + booked.error + '): book it in Delhivery manually. ';
  } else {
    warn = '⚠ Delhivery not connected on the website: book this COD order in Delhivery manually. ';
  }
  const ok = booked && booked.ok;
  const r = await D.push({ ref, c, pack, total, paid: false, courier: ok ? 'Delhivery' : '', awb: ok ? booked.awb : '',
    note: (ok ? 'COD booked with Delhivery · AWB ' + booked.awb + ' · print the label from the Delhivery panel. ' : '') + warn + 'Collect ₹' + total + (D.CFG.codFee ? ' (incl. ₹' + D.CFG.codFee + ' COD charge)' : '') + ' · ' + pack.label });
  if (r.ok) return res.status(200).json({ ok: true, ref, total, awb: ok ? booked.awb : '' });
  // Not saved in the desk. If Delhivery booked it, the parcel exists (AWB): tell the customer it is placed, and log loudly.
  console.error('COD ORDER NOT SAVED TO DESK', ref, r.error, JSON.stringify({ name: c.name, phone: c.phone, address: c.address, pin: c.pin, pack: pack.id, awb: ok ? booked.awb : '' }));
  if (ok) return res.status(200).json({ ok: true, ref, total, awb: booked.awb });
  return res.status(502).json({ ok: false, error: 'not_saved', ref });
};
