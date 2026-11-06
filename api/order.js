// POST /api/order: Cash on Delivery order from the website form.
// The price is taken from the server-side pack list (not from the browser), and the order is sent to the
// Order Desk inbox (skinday.shop) under the brand "cx" (Cream X Emirates). Order Desk keeps one entry per
// order number, so a double tap or a retry never makes a duplicate.
// Needs the Vercel environment variable WEB_ORDER_KEY (same key the Order Desk accepts).
const CFG = require('./_packs.json');

const clean = (v, n) => String(v == null ? '' : v).replace(/[\u0000-\u001f\u007f]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, n);
const deskUrl = () => (process.env.ORDERDESK_URL || 'https://www.skinday.shop').replace(/\/+$/, '');

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'method_not_allowed' });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  if (b.website) return res.status(200).json({ ok: true, ref: 'CX' }); // hidden field: bots fill it, people don't

  const pack = CFG.packs.find((p) => p.id === b.pack);
  const name = clean(b.name, 80);
  const phone = String(b.phone || '').replace(/\D/g, '').replace(/^91(?=\d{10}$)/, '').slice(-10);
  const pin = String(b.pin || '').replace(/\D/g, '');
  const address = clean(b.address, 220);
  const city = clean(b.city, 60);
  const upi = /upi/i.test(String(b.pay || ''));
  if (!pack || name.length < 2 || !/^[6-9]\d{9}$/.test(phone) || !/^[1-9]\d{5}$/.test(pin) || address.length < 10) {
    return res.status(400).json({ ok: false, error: 'invalid_details' });
  }
  const key = (process.env.WEB_ORDER_KEY || '').trim();
  if (!key) return res.status(503).json({ ok: false, error: 'not_configured' });

  // order number: from the page (so a retry keeps the same number) or a new one
  let ref = clean(b.ref, 20).replace(/[^A-Z0-9]/gi, '').toUpperCase();
  if (!/^CX[A-Z0-9]{6,16}$/.test(ref)) ref = 'CX' + Date.now().toString(36).toUpperCase() + Math.random().toString(36).slice(2, 5).toUpperCase();

  const body = {
    ref, src: 'web', site: CFG.site, brand: 'cx', pay: 'cod', paid: false, payId: '',
    total: pack.price, sub: pack.price, disc: 0, coupon: '', courier: '', awb: '',
    note: (upi ? 'Customer asked to pay by UPI: send a payment link on WhatsApp. ' : 'Cash on Delivery. ') + 'Pack: ' + pack.label,
    name, phone, email: '', house: address, area: city, landmark: '', pin, city, state: '',
    items: [[pack.desk, CFG.product + ' ' + CFG.size + (pack.jars > 1 ? ' x ' + pack.jars : ''), 1, pack.price]]
  };
  try {
    const r = await fetch(deskUrl() + '/api/web-order', { method: 'POST', headers: { 'Content-Type': 'application/json', 'x-web-order-key': key }, body: JSON.stringify(body) });
    const j = await r.json().catch(() => ({}));
    if (r.ok && j.ok) return res.status(200).json({ ok: true, ref, total: pack.price });
    console.error('order desk refused', ref, r.status, j.error);
  } catch (e) {
    console.error('order desk unreachable', ref, String((e && e.message) || e));
  }
  // Not saved: never tell the customer it worked. The page then sends the full order on WhatsApp instead.
  console.error('ORDER NOT SAVED', JSON.stringify({ ref, name, phone, pin, city, pack: pack.id, total: pack.price }));
  return res.status(502).json({ ok: false, error: 'not_saved', ref });
};
