// POST /api/order: Cash on Delivery order. Price from the server pack list; saved to the Order Desk.
const D = require('./_desk');

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'method_not_allowed' });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  if (b.website) return res.status(200).json({ ok: true, ref: 'CX' }); // hidden field: bots fill it, people don't
  const pack = D.packById(b.pack), c = D.customer(b);
  if (!pack || !c) return res.status(400).json({ ok: false, error: 'invalid_details' });
  const ref = D.newRef(b.ref);
  const r = await D.push({ ref, c, pack, total: pack.price, paid: false, note: 'Cash on Delivery · ' + pack.label });
  if (r.ok) return res.status(200).json({ ok: true, ref, total: pack.price });
  // Not saved: never tell the customer it worked. The page then sends the full order on WhatsApp instead.
  console.error('COD ORDER NOT SAVED', ref, r.error, JSON.stringify({ name: c.name, phone: c.phone, pin: c.pin, pack: pack.id }));
  return res.status(502).json({ ok: false, error: 'not_saved', ref });
};
