// POST /api/razorpay-webhook: Razorpay calls this when a payment is captured, so a paid order reaches the
// Order Desk even if the customer closed the page before it finished. The desk de-duplicates by order number.
// In Razorpay Dashboard > Webhooks: URL https://<domain>/api/razorpay-webhook, event payment.captured,
// and the same secret as RAZORPAY_WEBHOOK_SECRET here.
const crypto = require('crypto');
const { savePaid } = require('./_paid');

// Read the exact bytes Razorpay sent (the signature is over the raw body), without touching req.body.
async function raw(req) {
  const chunks = []; for await (const c of req) chunks.push(typeof c === 'string' ? Buffer.from(c) : c); return Buffer.concat(chunks).toString('utf8');
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).end();
  const secret = process.env.RAZORPAY_WEBHOOK_SECRET;
  if (!secret) return res.status(503).end();
  const body = await raw(req);
  const want = Buffer.from(crypto.createHmac('sha256', secret).update(body).digest('hex')), got = Buffer.from(String(req.headers['x-razorpay-signature'] || ''));
  if (!(want.length === got.length && crypto.timingSafeEqual(want, got))) return res.status(400).end();
  let ev = {}; try { ev = JSON.parse(body); } catch (e) { return res.status(400).end(); }
  const pay = ev.payload && ev.payload.payment && ev.payload.payment.entity;
  if (ev.event === 'payment.captured' && pay && pay.order_id) await savePaid(pay.order_id, pay.id, 'webhook');
  return res.status(200).json({ ok: true });
};
