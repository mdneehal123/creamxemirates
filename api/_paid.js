// Shared by verify.js and razorpay-webhook.js: confirms a Razorpay payment for a Razorpay order and saves it to the Order Desk as PAID.
const D = require('./_desk');
const auth = () => ({ Authorization: 'Basic ' + Buffer.from(process.env.RAZORPAY_KEY_ID + ':' + process.env.RAZORPAY_KEY_SECRET).toString('base64') });
async function rp(path) { try { const r = await fetch('https://api.razorpay.com/v1' + path, { headers: auth() }); return r.ok ? await r.json() : null; } catch (e) { return null; } }

async function savePaid(orderId, paymentId, via) {
  const [p, o] = await Promise.all([rp('/payments/' + encodeURIComponent(paymentId)), rp('/orders/' + encodeURIComponent(orderId))]);
  if (p && (p.order_id !== orderId || !(p.status === 'captured' || p.status === 'authorized'))) return { ok: false, error: 'not_paid' };
  const n = (o && o.notes) || {};
  const pack = D.packById(n.pack), c = D.customer(n);
  if (!o || !pack || !c) { console.error('PAID ORDER: details unreadable, check Razorpay', orderId, paymentId); return { ok: true, saved: false, ref: n.ref || '' }; }
  const confirmed = !!p, charged = confirmed ? p.amount / 100 : D.onlinePrice(pack), expected = D.onlinePrice(pack);
  const warn = [];
  if (!confirmed) warn.push('⚠ payment not confirmed with Razorpay: check the dashboard before shipping');
  if (confirmed && charged !== expected) warn.push('⚠ paid ₹' + charged + ', price is ₹' + expected);
  const ref = D.newRef(n.ref);
  const r = await D.push({ ref, c, pack, total: charged, paid: confirmed, payId: paymentId,
    note: [pack.test ? '🧪 TEST ORDER ₹1: DO NOT SHIP (delete after checking)' : 'PREPAID · OWN LABEL: print the label from Order Desk and ship it yourself (not booked with Delhivery)', 'Razorpay' + (p && p.method ? ' (' + p.method + ')' : '') + ' · ' + paymentId + ' · ' + orderId + ' · ' + pack.label + ' · saved by ' + via].concat(warn).join(' · ') });
  if (!r.ok) console.error('PAID ORDER NOT SAVED TO DESK', ref, orderId, paymentId, r.error);
  return { ok: true, saved: r.ok, ref };
}
module.exports = { savePaid };
