// Sends an order to the Order Desk inbox (skinday.shop), brand "cx". One entry per order number: retries never duplicate.
const CFG = require('./_packs.json');
const { stateFor } = require('./_delhivery');
const deskUrl = () => (process.env.ORDERDESK_URL || 'https://www.skinday.shop').replace(/\/+$/, '');
const clean = (v, n) => String(v == null ? '' : v).replace(/[\u0000-\u001f\u007f]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, n);

// Reads and checks the customer's details from a request body (or Razorpay order notes)
function customer(b) {
  const c = {
    name: clean(b.name, 80), phone: String(b.phone || '').replace(/\D/g, '').replace(/^91(?=\d{10}$)/, '').slice(-10),
    address: clean(b.address, 220), city: clean(b.city, 60), pin: String(b.pin || b.pincode || '').replace(/\D/g, '')
  };
  c.state = stateFor(c.pin);
  return c.name.length >= 2 && /^[6-9]\d{9}$/.test(c.phone) && /^[1-9]\d{5}$/.test(c.pin) && c.address.length >= 10 ? c : null;
}
const packById = (id) => CFG.packs.find((p) => p.id === id) || null;
// Online price = pack price minus the prepaid discount
const onlinePrice = (pack) => Math.max(1, pack.price - (CFG.prepaidOff || 0));
function newRef(given) {
  const r = clean(given, 20).replace(/[^A-Z0-9]/gi, '').toUpperCase();
  return /^CX[A-Z0-9]{6,16}$/.test(r) ? r : 'CX' + Date.now().toString(36).toUpperCase() + Math.random().toString(36).slice(2, 5).toUpperCase();
}

async function push({ ref, c, pack, total, paid, payId, note, courier, awb }) {
  const key = (process.env.WEB_ORDER_KEY || '').trim();
  if (!key) return { ok: false, error: 'WEB_ORDER_KEY not set' };
  const body = {
    ref, src: 'web', site: CFG.site, brand: 'cx', pay: paid ? 'upi' : 'cod', paid: Boolean(paid), payId: payId || '',
    total, sub: pack.price, disc: Math.max(0, pack.price - total), coupon: '', courier: courier || '', awb: awb || '', note: note || '',
    name: c.name, phone: c.phone, email: '', house: c.address, area: c.city, landmark: '', pin: c.pin, city: c.city, state: c.state || '',
    items: [[pack.desk, CFG.product + ' ' + CFG.size + ' · ' + pack.label, 1, pack.price]]
  };
  try {
    const r = await fetch(deskUrl() + '/api/web-order', { method: 'POST', headers: { 'Content-Type': 'application/json', 'x-web-order-key': key }, body: JSON.stringify(body) });
    const j = await r.json().catch(() => ({}));
    return r.ok && j.ok ? { ok: true, id: j.id } : { ok: false, error: j.error || 'HTTP ' + r.status };
  } catch (e) { return { ok: false, error: String((e && e.message) || e) }; }
}

module.exports = { CFG, clean, customer, packById, onlinePrice, newRef, push };
