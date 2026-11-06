// POST /api/verify: called by the page after Razorpay checkout succeeds. Checks the signature, then saves the paid order.
const crypto = require('crypto');
const { savePaid } = require('./_paid');

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  const secret = process.env.RAZORPAY_KEY_SECRET;
  if (!secret || !process.env.RAZORPAY_KEY_ID) return res.status(503).json({ ok: false });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  const orderId = String(b.razorpay_order_id || ''), paymentId = String(b.razorpay_payment_id || ''), sig = String(b.razorpay_signature || '');
  if (!orderId || !paymentId || !sig) return res.status(400).json({ ok: false });
  const want = Buffer.from(crypto.createHmac('sha256', secret).update(orderId + '|' + paymentId).digest('hex')), got = Buffer.from(sig);
  if (!(want.length === got.length && crypto.timingSafeEqual(want, got))) return res.status(400).json({ ok: false });
  const r = await savePaid(orderId, paymentId, 'checkout');
  // The customer has paid (signed by Razorpay): never show an error, even if saving to the desk failed (it is logged).
  return res.status(r.ok ? 200 : 400).json({ ok: r.ok, ref: r.ref || '' });
};
