// POST /api/create-order: creates a Razorpay order for the chosen pack at the online price
// (pack price minus the prepaid discount, both from the server pack list). Customer details ride along in the
// Razorpay order notes, so the payment can still be matched to an order if the customer closes the page.
// Needs RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET.
const D = require('./_desk');

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });
  const id = process.env.RAZORPAY_KEY_ID, secret = process.env.RAZORPAY_KEY_SECRET;
  if (!id || !secret) return res.status(503).json({ error: 'not_configured' });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  if (b.website) return res.status(400).json({ error: 'invalid_details' });
  const pack = D.packById(b.pack), c = D.customer(b);
  if (!pack || !c) return res.status(400).json({ error: 'invalid_details' });
  const ref = D.newRef(b.ref), amount = D.onlinePrice(pack);
  try {
    const r = await fetch('https://api.razorpay.com/v1/orders', {
      method: 'POST', headers: { Authorization: 'Basic ' + Buffer.from(id + ':' + secret).toString('base64'), 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount: amount * 100, currency: 'INR', receipt: ref,
        notes: { brand: 'Cream X Emirates', ref, pack: pack.id, product: D.CFG.product + ' ' + D.CFG.size + ' · ' + pack.label, name: c.name, phone: c.phone, address: c.address, city: c.city, pincode: c.pin } })
    });
    const o = await r.json();
    if (!r.ok || !o.id) return res.status(502).json({ error: 'gateway_error' });
    return res.status(200).json({ order_id: o.id, amount: o.amount, currency: 'INR', key_id: id, total: amount, ref });
  } catch (e) { return res.status(502).json({ error: 'gateway_unreachable' }); }
};
