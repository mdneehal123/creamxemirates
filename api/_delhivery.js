// Delhivery: pincode check and automatic booking for Cash on Delivery orders (prepaid orders ship on our own label).
// Same account as GlutaNex. Vercel env: DELHIVERY_TOKEN, DELHIVERY_PICKUP (pickup name exactly as in Delhivery; several
// may be separated by "|"), optional DELHIVERY_ENV=staging, DELHIVERY_MODE (Surface|Express, default Surface).
const base = () => (process.env.DELHIVERY_ENV === 'staging' ? 'https://staging-express.delhivery.com' : 'https://track.delhivery.com');
const token = () => (process.env.DELHIVERY_TOKEN || '').trim();
const delhiveryOn = () => Boolean(token() && (process.env.DELHIVERY_PICKUP || '').trim());
function pickupNames() {
  const out = [], add = (n) => { if (n && !out.includes(n)) out.push(n); };
  (process.env.DELHIVERY_PICKUP || '').split('|').map((x) => x.trim()).filter(Boolean)
    .forEach((n) => { add(n); add(n.toUpperCase()); add(n.toLowerCase()); add(n.replace(/\b\w/g, (ch) => ch.toUpperCase())); add(n + ' '); });
  return out.slice(0, 12);
}
const RETURN = { name: 'Beauty Mart', add: 'Azad Nagar 4th Cross, Bhatkal', city: 'Bhatkal', state: 'Karnataka', pin: '581320', phone: '9980881230' };
const head = () => ({ Authorization: 'Token ' + token(), Accept: 'application/json' });
const STATE_BY_PREFIX = {
  11: 'Delhi', 12: 'Haryana', 13: 'Haryana', 14: 'Punjab', 15: 'Punjab', 16: 'Punjab', 17: 'Himachal Pradesh',
  18: 'Jammu and Kashmir', 19: 'Jammu and Kashmir', 20: 'Uttar Pradesh', 21: 'Uttar Pradesh', 22: 'Uttar Pradesh',
  23: 'Uttar Pradesh', 24: 'Uttar Pradesh', 25: 'Uttar Pradesh', 26: 'Uttarakhand', 27: 'Uttar Pradesh', 28: 'Uttar Pradesh',
  30: 'Rajasthan', 31: 'Rajasthan', 32: 'Rajasthan', 33: 'Rajasthan', 34: 'Rajasthan', 36: 'Gujarat', 37: 'Gujarat',
  38: 'Gujarat', 39: 'Gujarat', 40: 'Maharashtra', 41: 'Maharashtra', 42: 'Maharashtra', 43: 'Maharashtra', 44: 'Maharashtra',
  45: 'Madhya Pradesh', 46: 'Madhya Pradesh', 47: 'Madhya Pradesh', 48: 'Madhya Pradesh', 49: 'Chhattisgarh',
  50: 'Telangana', 51: 'Andhra Pradesh', 52: 'Andhra Pradesh', 53: 'Andhra Pradesh', 56: 'Karnataka', 57: 'Karnataka',
  58: 'Karnataka', 59: 'Karnataka', 60: 'Tamil Nadu', 61: 'Tamil Nadu', 62: 'Tamil Nadu', 63: 'Tamil Nadu', 64: 'Tamil Nadu',
  65: 'Tamil Nadu', 66: 'Tamil Nadu', 67: 'Kerala', 68: 'Kerala', 69: 'Kerala', 70: 'West Bengal', 71: 'West Bengal',
  72: 'West Bengal', 73: 'West Bengal', 74: 'West Bengal', 75: 'Odisha', 76: 'Odisha', 77: 'Odisha', 78: 'Assam',
  79: 'Assam', 80: 'Bihar', 81: 'Bihar', 82: 'Jharkhand', 83: 'Jharkhand', 84: 'Bihar', 85: 'Bihar'
};
function stateFor(pin) { return STATE_BY_PREFIX[Number(String(pin || '').slice(0, 2))] || ''; }

// { known, cod, city, state }: known=false when Delhivery does not deliver there at all
async function serviceable(pin) {
  const r = await fetch(base() + '/c/api/pin-codes/json/?filter_codes=' + encodeURIComponent(pin), { headers: head(), signal: AbortSignal.timeout(8000) });
  if (!r.ok) throw new Error('delhivery_http_' + r.status);
  const j = await r.json().catch(() => ({}));
  const pc = j && j.delivery_codes && j.delivery_codes[0] && j.delivery_codes[0].postal_code;
  if (!pc) return { known: false, cod: false, city: '', state: '' };
  const embargo = /embargo/i.test(String(pc.remarks || ''));
  return { known: true, cod: !embargo && String(pc.cod).toUpperCase() === 'Y', city: pc.city || '', state: pc.state_code || '' };
}

// Books one COD shipment for a pack. Returns { ok, awb } or { ok:false, error }.
async function bookCod({ ref, c, pack, product }) {
  const jars = pack.jars;
  const shipment = {
    name: c.name, add: c.address, pin: c.pin, city: c.city, state: c.state || stateFor(c.pin), country: 'India', phone: c.phone, order: ref,
    payment_mode: 'COD', cod_amount: String(pack.price), total_amount: String(pack.price),
    products_desc: (product + (jars > 1 ? ' x' + jars : '')).slice(0, 200), quantity: String(jars),
    order_date: new Date().toISOString().slice(0, 19).replace('T', ' '), weight: String(Math.round((0.13 * jars + 0.05) * 1000)),
    shipment_length: String(jars > 1 ? 15 : 10), shipment_width: String(jars > 1 ? 12 : 10), shipment_height: '8',
    seller_name: 'Beauty Mart', seller_add: RETURN.add, return_name: RETURN.name, return_add: RETURN.add, return_city: RETURN.city, return_state: RETURN.state,
    return_pin: RETURN.pin, return_country: 'India', return_phone: RETURN.phone, shipping_mode: process.env.DELHIVERY_MODE || 'Surface', address_type: 'home', waybill: ''
  };
  let last = '';
  for (const name of pickupNames()) {
    try {
      const r = await fetch(base() + '/api/cmu/create.json', { method: 'POST', headers: Object.assign(head(), { 'Content-Type': 'application/x-www-form-urlencoded' }),
        body: 'format=json&data=' + encodeURIComponent(JSON.stringify({ shipments: [shipment], pickup_location: { name } })), signal: AbortSignal.timeout(15000) });
      const j = await r.json().catch(() => ({}));
      const pkg = j && Array.isArray(j.packages) && j.packages[0];
      if (r.ok && pkg && pkg.waybill && String(pkg.status).toLowerCase() === 'success') return { ok: true, awb: String(pkg.waybill) };
      last = String((pkg && (Array.isArray(pkg.remarks) ? pkg.remarks.join('; ') : pkg.remarks)) || j.rmk || j.error || ('HTTP ' + r.status));
      if (!/ClientWarehouse|warehouse|pickup/i.test(last)) break;
    } catch (e) { last = String((e && e.message) || e); break; }
  }
  return { ok: false, error: last.slice(0, 300) };
}

module.exports = { delhiveryOn, serviceable, bookCod, stateFor };
