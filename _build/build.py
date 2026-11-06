# Static site builder for an independent Cream X Emirates seller store (run: python3 _build/build.py).
# Edit CONFIG below, rebuild, push. Pages are written into the repo root.
import os, json, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------- CONFIG: change these ----------------
SITE = 'https://trycreamxemirates.in'    # the live domain
STORE = 'Beauty Mart'                    # the seller's store name shown on the site
OWNER = 'Beauty Mart Pvt Ltd'
ADDR = 'Azad Nagar 4th Cross, near Anfa Park, Bhatkal, Uttara Kannada, Karnataka 581320, India'
WA = '919980881230'                      # TODO: confirm the WhatsApp order number
WA_SHOW = '+91 99808 81230'
EMAIL = ''                               # optional support email
PRODUCT = 'Cream X Emirates Glow Restoring Face Crème'
SIZE = '30 ml'
COD_FEE = 100                            # extra charge for Cash on Delivery; 0 turns it off
PREPAID_OFF = 50                         # extra discount for paying online (Razorpay); 0 turns it off
MRP = 2200  # MRP of one new pink jar (crossed-out price)
#                               # TODO: confirm
PACKS = [  # (id, label, jars, price): the options on the page, in order
    ('p1', '1 new pink jar', 1, 1100),
    ('p2', '2 new pink jars', 2, 1850),
    ('o1', '1 old white jar', 1, 749),
]
PACK_INFO = {  # line under each option, badge, photo shown when chosen (index in the gallery), compare-at price (crossed out; None = none)
    'p1': {'sub': 'New CXE pink pack · MRP ₹2,200', 'tag': '50% off', 'img': 1, 'cmp': 2200},
    'p2': {'sub': '₹925 per jar · MRP ₹4,400', 'tag': 'Best value', 'img': 3, 'cmp': 4400},
    'o1': {'sub': 'Old white pack · same formula · MRP ₹999', 'tag': 'Clearance', 'img': 2, 'cmp': 999},
}
# ------------------------------------------------------

def rs(n): return '₹' + format(n, ',')
SLUG = 'cream-x-emirates-face-cream-30g'
PURL = '/product/%s/' % SLUG
TODAY = datetime.date.today().isoformat()

JAR = '''<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Illustration of a 30 g face cream jar"><defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fbe9ef"/><stop offset="1" stop-color="#f3d6e0"/></linearGradient>
<linearGradient id="lid" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b8456f"/><stop offset="1" stop-color="#8a2d52"/></linearGradient>
<linearGradient id="jar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff"/><stop offset=".55" stop-color="#fbf4f6"/><stop offset="1" stop-color="#ead9df"/></linearGradient></defs>
<rect width="400" height="400" fill="#fbe9ef"/><ellipse cx="200" cy="318" rx="118" ry="16" fill="#d9b3c2" opacity=".55"/>
<rect x="92" y="190" width="216" height="124" rx="26" fill="url(#jar)" stroke="#e2c6d1" stroke-width="2"/>
<rect x="84" y="128" width="232" height="74" rx="20" fill="url(#lid)"/><rect x="84" y="182" width="232" height="10" fill="#7a2748" opacity=".35"/>
<path d="M104 146h192" stroke="#fff" stroke-opacity=".25" stroke-width="6" stroke-linecap="round"/>
<text x="200" y="250" text-anchor="middle" font-family="Georgia,serif" font-size="25" fill="#5a2140" letter-spacing="1">FACE CREAM</text>
<text x="200" y="282" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#9a6a7e" letter-spacing="3">30 g</text></svg>'''

CSS = r''':root{--ink:#2b1a22;--muted:#6f5a64;--rose:#b8456f;--rose-d:#8a2d52;--blush:#fbeef2;--cream:#fffaf7;--line:#efdde4;--ok:#1f7a4d}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--cream)}
a{color:var(--rose-d)}img,svg{max-width:100%;display:block}h1,h2,h3{font-family:Georgia,"Iowan Old Style",serif;line-height:1.2;margin:0 0 .5em}
h1{font-size:clamp(1.6rem,4.5vw,2.3rem)}h2{font-size:clamp(1.3rem,3.6vw,1.8rem)}
.wrap{max-width:1080px;margin:0 auto;padding:0 18px}.muted{color:var(--muted)}
.top{background:var(--rose-d);color:#fff;text-align:center;font-size:.85rem;padding:7px 10px}
header.site{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:20}
header.site .wrap{display:flex;align-items:center;justify-content:space-between;height:60px;gap:12px}
.logo{font-family:Georgia,serif;font-size:1.3rem;color:var(--ink);text-decoration:none}.logo small{display:block;font:500 .68rem system-ui;color:var(--muted);letter-spacing:.08em;text-transform:uppercase}
nav a{color:var(--ink);text-decoration:none;font-size:.92rem;margin-left:16px}nav .hide-m{display:inline}@media(max-width:700px){nav .hide-m{display:none}}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:var(--rose);color:#fff;border:0;border-radius:999px;padding:14px 22px;font:600 1rem system-ui;text-decoration:none;cursor:pointer}
.btn:hover{background:var(--rose-d)}.btn.wa{background:#1f8f55}.btn.wa:hover{background:#18744a}.btn.ghost{background:#fff;color:var(--rose-d);border:1.5px solid var(--rose)}.btn.block{width:100%}
.pdp{display:grid;grid-template-columns:1.05fr 1fr;gap:34px;padding:26px 0 10px}@media(max-width:860px){.pdp{grid-template-columns:1fr;gap:18px;padding-top:14px}}
.gal-main{border-radius:22px;overflow:hidden;background:#fbe9ef;border:1px solid var(--line)}.gal-thumbs{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:10px}.gal-main img,.gal-thumbs img{width:100%;height:100%;object-fit:cover;display:block}
.gal-thumbs button{border:1.5px solid var(--line);border-radius:14px;padding:0;background:#fff;overflow:hidden;cursor:pointer;aspect-ratio:1}.gal-thumbs button[aria-current=true]{border-color:var(--rose)}
.tile{display:flex;align-items:center;justify-content:center;text-align:center;height:100%;padding:10px;font-size:.8rem;color:var(--rose-d);background:var(--blush)}
.crumb{font-size:.82rem;color:var(--muted);margin:14px 0 0}.crumb a{color:var(--muted)}
.seller{display:inline-block;font-size:.78rem;background:var(--blush);color:var(--rose-d);border-radius:999px;padding:4px 12px;margin-bottom:10px}
.price{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin:6px 0 2px}.price b{font-size:1.9rem}.price s{color:var(--muted)}.save{background:#e7f6ee;color:var(--ok);font-weight:600;font-size:.85rem;border-radius:6px;padding:2px 8px}
.tax{font-size:.82rem;color:var(--muted);margin:0 0 16px}
.packs{display:grid;gap:10px;margin:14px 0}.pack{display:flex;align-items:center;gap:12px;border:1.5px solid var(--line);border-radius:14px;padding:12px 14px;background:#fff;cursor:pointer}
.pack input{accent-color:var(--rose);width:18px;height:18px}.pack .l{flex:1}.pack .l b{display:block}.pack .l span{font-size:.84rem;color:var(--muted)}.pack .r{text-align:right}.pack .r b{display:block}.pack .r s{font-size:.82rem;color:var(--muted)}
.pack:has(input:checked){border-color:var(--rose);background:#fff6f9}.tag{font-size:.7rem;font-weight:700;color:#fff;background:var(--rose);border-radius:6px;padding:1px 6px;margin-left:6px;vertical-align:middle}
.ctas{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:16px 0}@media(max-width:420px){.ctas{grid-template-columns:1fr}}
.trust{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin:14px 0;padding:0;list-style:none;font-size:.88rem}.trust li{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 12px}
.eta{font-size:.9rem;background:#fff;border:1px dashed var(--line);border-radius:12px;padding:10px 12px}
section.band{padding:38px 0;border-top:1px solid var(--line)}section.band.alt{background:#fff}
.steps{counter-reset:s;display:grid;gap:12px;padding:0;list-style:none}.steps li{counter-increment:s;background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 14px 14px 56px;position:relative}
.steps li:before{content:counter(s);position:absolute;left:14px;top:14px;width:30px;height:30px;border-radius:50%;background:var(--rose);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:18px}@media(max-width:760px){.grid2{grid-template-columns:1fr}}
.card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px}
.note{background:var(--blush);border-radius:14px;padding:14px 16px;font-size:.92rem}
details{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:8px 0}summary{font-weight:600;cursor:pointer}details p{margin:.6em 0 .2em}
form.order{display:grid;gap:12px}form.order label{display:grid;gap:4px;font-size:.9rem;font-weight:600}
form.order input,form.order select,form.order textarea{font:inherit;padding:12px;border:1.5px solid var(--line);border-radius:10px;background:#fff;width:100%}
form.order input:focus,form.order select:focus,form.order textarea:focus{outline:2px solid var(--rose);border-color:transparent}.two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.err{color:#b3261e;font-size:.85rem;min-height:1.2em}
footer{background:#2b1a22;color:#f3e6eb;padding:34px 0 90px;font-size:.9rem}footer a{color:#f3e6eb}footer .cols{display:grid;grid-template-columns:2fr 1fr 1fr;gap:24px}@media(max-width:760px){footer .cols{grid-template-columns:1fr}}
footer .disc{border-top:1px solid #4a3340;margin-top:22px;padding-top:16px;font-size:.8rem;color:#cdb8c2}
.sticky{position:fixed;left:0;right:0;bottom:0;background:#fff;border-top:1px solid var(--line);padding:10px 14px;display:none;align-items:center;gap:12px;z-index:30;box-shadow:0 -6px 20px rgba(0,0,0,.06)}
.sticky .p{flex:1;line-height:1.2}.sticky .p b{display:block;font-size:1.1rem}.sticky .p s{font-size:.8rem;color:var(--muted)}@media(max-width:860px){.sticky.show{display:flex}}
.prose{max-width:760px}.prose ul{padding-left:1.2em}
.pack .l .tag{color:#fff}[hidden]{display:none!important}
.wa-float{position:fixed;right:16px;bottom:20px;z-index:40;display:flex;align-items:center;gap:8px;background:#25d366;color:#fff;text-decoration:none;border-radius:999px;padding:12px;box-shadow:0 6px 18px rgba(0,0,0,.18);font:600 .9rem system-ui;animation:waring 2.4s ease-out infinite}
.wa-float span{max-width:0;overflow:hidden;white-space:nowrap;transition:max-width .3s}.wa-float:hover span,.wa-float:focus span{max-width:140px;padding-right:4px}
@keyframes waring{0%{box-shadow:0 6px 18px rgba(0,0,0,.18),0 0 0 0 rgba(37,211,102,.5)}70%{box-shadow:0 6px 18px rgba(0,0,0,.18),0 0 0 14px rgba(37,211,102,0)}100%{box-shadow:0 6px 18px rgba(0,0,0,.18),0 0 0 0 rgba(37,211,102,0)}}
@media(max-width:860px){.wa-float{bottom:84px;right:6px;padding:9px}.wa-float svg{width:24px;height:24px}.pack .r{padding-right:10px}}
/* attention animations: gentle, and off for people who ask for less motion */
@keyframes shine{0%{transform:translateX(-120%) skewX(-20deg)}55%,100%{transform:translateX(260%) skewX(-20deg)}}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.07)}}
@keyframes glow{0%,100%{box-shadow:0 0 0 0 rgba(31,122,77,0)}50%{box-shadow:0 0 0 6px rgba(31,122,77,.14)}}
@keyframes ring{0%{box-shadow:0 0 0 0 rgba(184,69,111,.55)}70%{box-shadow:0 0 0 14px rgba(184,69,111,0)}100%{box-shadow:0 0 0 0 rgba(184,69,111,0)}}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes topshim{0%{background-position:-200% 0}100%{background-position:200% 0}}
@keyframes blinkdot{0%,100%{opacity:1}50%{opacity:.25}}
.btn.shine{position:relative;overflow:hidden}.btn.shine:after{content:'';position:absolute;top:0;left:0;width:40%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.45),transparent);animation:shine 3.2s ease-in-out infinite}
.online{animation:glow 2.6s ease-in-out infinite}.online b{color:var(--ok)}
.pay .tag,.save,.pack .tag{display:inline-block;animation:pulse 1.8s ease-in-out infinite}
.top{background:linear-gradient(90deg,var(--rose-d) 0%,#c2557f 25%,var(--rose-d) 50%,#c2557f 75%,var(--rose-d) 100%);background-size:200% 100%;animation:topshim 6s linear infinite}
.top:before{content:'●';color:#ffd36b;margin-right:6px;animation:blinkdot 1.4s ease-in-out infinite;display:inline-block}
.gal-main>picture img{animation:floaty 5s ease-in-out infinite}
.sticky .btn{animation:ring 2s ease-out infinite}
@media (prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important}}
.online{background:#eef8f2;border:1px solid #cfe9da;border-radius:12px;padding:10px 12px;margin:0 0 6px;font-size:.95rem}.online span{color:var(--ok);font-size:.85rem;display:block}
.linkbtn{background:none;border:0;color:var(--rose-d);text-decoration:underline;font:inherit;cursor:pointer;padding:0}
.paysel{border:0;padding:0;margin:0;display:grid;gap:8px}.paysel legend{font-weight:600;font-size:.9rem;margin-bottom:4px}.pay{display:flex!important;grid-template-columns:none!important;align-items:center;gap:12px;border:1.5px solid var(--line);border-radius:12px;padding:12px;background:#fff;cursor:pointer}.pay input{width:18px!important;height:18px;accent-color:var(--rose)}.pay span{flex:1;font-weight:400}.pay small{display:block;color:var(--muted);font-size:.8rem}.pay:has(input:checked){border-color:var(--rose);background:#fff6f9}.pay .tag{color:#fff}
.sticky .p small{display:block;font-size:.72rem;color:var(--ok)}.glist{list-style:none;padding:0;margin:0}.glist li{border-bottom:1px solid var(--line)}.glist a{display:block;padding:12px 0;text-decoration:none;font-weight:600}.glist a:after{content:' ›';color:var(--rose)}
.answer{background:#fff;border:1px solid var(--line);border-left:5px solid var(--rose);border-radius:12px;padding:14px 16px;font-size:1.05rem}.answer:before{content:'Quick answer';display:block;font:700 .72rem system-ui;letter-spacing:.08em;text-transform:uppercase;color:var(--rose-d);margin-bottom:4px}
.pcard{display:flex;gap:14px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:16px;padding:12px;margin:22px 0}.pcard svg,.pcard img{width:84px;height:84px;border-radius:12px;flex:none;object-fit:cover}.pcard .t{flex:1}.pcard b{display:block}.pcard .btn{padding:10px 16px;font-size:.92rem}
.tbl{overflow-x:auto}.spec th{text-align:left;font-size:.85rem;color:var(--muted);padding:6px 0;border-bottom:1px solid var(--line)}.meta{font-size:.82rem;color:var(--muted)}.feat{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}@media(max-width:860px){.feat{grid-template-columns:1fr 1fr}}@media(max-width:480px){.feat{grid-template-columns:1fr}}.feat p{margin:.4em 0 0;font-size:.92rem;color:var(--muted)}
.tl{list-style:none;padding:0;margin:0;border-left:3px solid var(--rose)}.tl li{padding:0 0 16px 18px;position:relative}.tl li:before{content:'';position:absolute;left:-8px;top:6px;width:13px;height:13px;border-radius:50%;background:var(--rose)}.tl b{display:block}.tl span{color:var(--muted);font-size:.93rem}
.spec{width:100%;border-collapse:collapse;font-size:.92rem}.spec td{padding:8px 0;border-bottom:1px solid var(--line);vertical-align:top}.spec td:first-child{color:var(--muted);width:40%}.gal-thumbs .tile span{display:none}.gal-thumbs .tile b{font-size:1rem!important}
@media(max-width:860px){.gal-main{aspect-ratio:1;display:flex;justify-content:center;align-items:center}.gal-main>.tile{width:100%}.gal-thumbs{grid-template-columns:repeat(4,1fr)}}
'''

JS = r'''(function(){
var C=window.STORE||{};var $=function(s){return document.querySelector(s)};
function pack(){var r=document.querySelector('input[name=pack]:checked');return C.packs.filter(function(p){return p.id===(r?r.value:'p1')})[0]}
function rs(n){return '₹'+n.toLocaleString('en-IN')}
function sync(){var p=pack();if(!p)return;var mrp=p.cmp||0;document.querySelectorAll('[data-price]').forEach(function(e){e.textContent=rs(p.price)});
document.querySelectorAll('[data-mrp]').forEach(function(e){e.textContent=mrp>p.price?rs(mrp):''});document.querySelectorAll('[data-save]').forEach(function(e){e.textContent=mrp>p.price?'Save '+rs(mrp-p.price):'';e.hidden=!(mrp>p.price)});document.querySelectorAll('[data-online]').forEach(function(e){e.textContent=rs(p.price-C.off)});document.querySelectorAll('[data-codprice]').forEach(function(e){e.textContent=rs(p.price+C.cod)});payLabel();
var o=$('#oPack');if(o)o.value=p.id;var t=document.querySelectorAll('.gal-thumbs button');var k=p.img||0;if(t[k]&&sync.ready){t[k].click()}sync.ready=true}
document.querySelectorAll('input[name=pack]').forEach(function(i){i.addEventListener('change',sync)});
var op=$('#oPack');if(op)op.addEventListener('change',function(){var r=document.querySelector('input[name=pack][value='+op.value+']');if(r){r.checked=true;sync()}});
sync();
// gallery
document.querySelectorAll('.gal-thumbs button').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('.gal-thumbs button').forEach(function(x){x.setAttribute('aria-current','false')});b.setAttribute('aria-current','true');$('.gal-main').innerHTML=b.innerHTML})});
// delivery estimate: dispatch in 1-2 business days, delivery 3-7 business days
function addBiz(d,n){d=new Date(d);while(n>0){d.setDate(d.getDate()+1);if(d.getDay()!==0)n--}return d}
var eta=$('#eta');if(eta){var f={weekday:'short',day:'numeric',month:'short'};eta.textContent=addBiz(new Date(),3).toLocaleDateString('en-IN',f)+' to '+addBiz(new Date(),7).toLocaleDateString('en-IN',f)}
// WhatsApp quick order
function wa(t){var a=document.createElement('a');a.href='https://wa.me/'+C.wa+'?text='+encodeURIComponent(t);a.target='_blank';a.rel='noopener';document.body.appendChild(a);a.click();a.remove()}
document.querySelectorAll('[data-wa-order]').forEach(function(b){b.addEventListener('click',function(){var p=pack();wa('Hi, I want to order '+C.product+' ('+C.size+'): '+p.label+' for '+rs(p.price)+', Cash on Delivery.')})});
// payment choice: online (Razorpay) first, COD second
function paym(){var r=document.querySelector('input[name=paym]:checked');return r?r.value:'online'}
function payLabel(){var b=$('#oGo'),p=pack();if(!b||!p||b.disabled)return;b.textContent=paym()==='online'?'Pay '+rs(p.price-C.off)+' securely':'Place order · Cash on Delivery '+rs(p.price+C.cod)}
document.querySelectorAll('input[name=paym]').forEach(function(i){i.addEventListener('change',payLabel)});
document.querySelectorAll('[data-pay-go]').forEach(function(a){a.addEventListener('click',function(){var r=document.querySelector('input[name=paym][value='+a.getAttribute('data-pay-go')+']');if(r){r.checked=true;payLabel()}})});
function loadRzp(){return new Promise(function(ok,no){if(window.Razorpay)return ok();var s=document.createElement('script');s.src='https://checkout.razorpay.com/v1/checkout.js';s.onload=ok;s.onerror=no;document.head.appendChild(s)})}
function post(u,d){return fetch(u,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)}).then(function(r){return r.json().catch(function(){return{}}).then(function(j){j._ok=r.ok;j._s=r.status;return j})})}
var f=$('#orderForm');if(f){f.addEventListener('submit',function(e){e.preventDefault();var g=function(i){return((f.elements[i]&&f.elements[i].value)||'').trim()};var err=$('#oErr');
var ph=g('phone').replace(/\D/g,'').replace(/^91(?=\d{10}$)/,'');if(g('name').length<2){err.textContent='Please enter your name.';return}
if(!/^[6-9]\d{9}$/.test(ph)){err.textContent='Please enter a 10-digit mobile number.';return}if(!/^\d{6}$/.test(g('pin'))){err.textContent='Please enter a 6-digit pincode.';return}
if(g('address').length<10){err.textContent='Please enter your full address.';return}err.textContent='';
var p=C.packs.filter(function(x){return x.id===g('pack')})[0],how=paym();
var data={ref:f.dataset.ref,pack:p.id,name:g('name'),phone:ph,address:g('address'),city:g('city'),pin:g('pin'),website:g('website')};
var msg=function(ref,paidNote){return 'New order'+(ref?' '+ref:'')+'\nProduct: '+C.product+' ('+C.size+')\nPack: '+p.label+'\nTotal: '+rs(how==='online'?p.price-C.off:p.price+C.cod)+(how==='online'?' (free delivery)':' (incl. '+rs(C.cod)+' COD charge)')+'\nPayment: '+(paidNote||'Cash on Delivery')+'\n\nName: '+g('name')+'\nMobile: '+ph+'\nAddress: '+g('address')+'\nCity: '+g('city')+'\nPincode: '+g('pin')};
var go=$('#oGo');go.disabled=true;go.textContent=how==='online'?'Opening secure payment…':'Placing your order…';
if(!f.dataset.ref)f.dataset.ref='CX'+Date.now().toString(36).toUpperCase()+Math.random().toString(36).slice(2,5).toUpperCase();data.ref=f.dataset.ref;
var reset=function(){go.disabled=false;payLabel()};
var show=function(html){var d=$('#oDone');d.innerHTML=html;d.hidden=false;d.scrollIntoView({behavior:'smooth',block:'center'})};
var waBtn=function(t,label){return '<a class="btn wa block" target="_blank" rel="noopener" href="https://wa.me/'+C.wa+'?text='+encodeURIComponent(t)+'">'+label+'</a>'};
var placed=function(ref,paid){f.hidden=true;show('<h3>'+(paid?'Payment received ✅':'Order placed ✅')+'</h3><p>Order number <b>'+ref+'</b><br>'+p.label+' · '+rs(paid?p.price-C.off:p.price+C.cod)+' · '+(paid?'Paid online':'Cash on Delivery (incl. '+rs(C.cod)+' COD charge)')+'</p><p class="muted">'+(paid?'Prepaid orders are packed first. ':'')+'We will confirm on WhatsApp and share tracking when it ships.</p>'+waBtn('Hi, I just placed order '+ref+' on your website. Please confirm.','Get updates on WhatsApp'))};
if(how==='cod'){post('/api/order',data).then(function(j){if(j._ok&&j.ok)placed(j.ref||data.ref,false);else if(j.error==='cod_unavailable'){var on=document.querySelector('input[name=paym][value=online]');if(on)on.checked=true;reset();show('<h3>Cash on Delivery is not available for pincode '+g('pin')+'</h3><p>Please pay online instead. You also get <b>'+rs(C.off)+' off</b>. Tap <b>Pay</b> below.</p>')}else{reset();show('<h3>One more step</h3><p>We could not save your order automatically. Tap below to send it on WhatsApp; it is ready to send.</p>'+waBtn(msg(data.ref),'Send order on WhatsApp'))}}).catch(function(){reset();show('<h3>One more step</h3><p>No connection. Tap below to send your order on WhatsApp.</p>'+waBtn(msg(data.ref),'Send order on WhatsApp'))});return}
// online
Promise.all([post('/api/create-order',data),loadRzp()]).then(function(x){var o=x[0];
if(!o._ok||!o.order_id){reset();show('<h3>Online payment is not available right now</h3><p>Please choose <b>Cash on Delivery</b> above, or order on WhatsApp.</p>'+waBtn(msg(data.ref),'Order on WhatsApp'));return}
var rz=new Razorpay({key:o.key_id,order_id:o.order_id,amount:o.amount,currency:'INR',name:'Cream X Emirates',description:p.label+' · '+C.size,prefill:{name:g('name'),contact:'+91'+ph},notes:{ref:o.ref},theme:{color:'#b8456f'},
handler:function(r){go.textContent='Confirming payment…';post('/api/verify',r).then(function(v){placed(v.ref||o.ref,true)}).catch(function(){placed(o.ref,true)})},
modal:{ondismiss:function(){reset();show('<h3>Payment not completed</h3><p>No money was taken. Tap <b>Pay</b> to try again, or choose <b>Cash on Delivery</b>.</p>')}}});
rz.on('payment.failed',function(){reset()});$('#oDone').hidden=true;rz.open()}).catch(function(){reset();show('<h3>Could not open payment</h3><p>Check your connection and try again, or choose <b>Cash on Delivery</b>.</p>')})})}
// sticky bar after scrolling past the buy buttons
var s=$('.sticky'),c=$('.ctas');if(s&&c&&'IntersectionObserver' in window){new IntersectionObserver(function(e){s.classList.toggle('show',!e[0].isIntersecting&&e[0].boundingClientRect.top<0)}).observe(c)}
// review form
var rv=$('#rvGo');if(rv)rv.addEventListener('click',function(){var g=function(i){return($('#'+i).value||'').trim()};if(g('rvX').length<10){$('#rvX').focus();return}
wa('Review: '+C.product+'\nRating: '+g('rvR')+'\nUsed for: '+g('rvT')+'\nReview: '+g('rvX')+'\nName and city: '+(g('rvN')||'-')+'\nOK to show on website: '+($('#rvOk').checked?'Yes':'No'))});
})();'''

FAQ = [
    ('Is this the official Cream X Emirates website?', 'No. This is an independent online store selling sealed packs. We handle your order, delivery and returns ourselves; seller details are in the footer.'),
    ('How do I use Cream X Emirates?', 'At night, cleanse and dry your face, massage in a small amount until absorbed, wait about 10 minutes, then apply a second thin layer as an overnight mask. Rinse with cold water in the morning and use sunscreen.'),
    ('How soon will I see results?', 'Skin often feels softer within a few weeks. Any change in tan or uneven tone is gradual, usually over 8 to 12 weeks, and depends on daily sunscreen. Results vary from person to person.'),
    ('Who should not use it?', 'The brand does not recommend it for children under 14, pregnant women or elderly people. Ask a doctor first if you are breastfeeding or have a skin condition, and never apply it on broken or irritated skin.'),
    ('How can I pay?', 'Pay online through Razorpay (UPI, cards, net banking or wallets) and get %s off, or choose Cash on Delivery (%s COD charge) and pay when the parcel arrives.' % (rs(PREPAID_OFF), rs(COD_FEE))),
    ('Is paying online safe?', 'Yes. Payments are processed by Razorpay, a licensed Indian payment gateway; we never see your card details or UPI PIN.'),
    ('Is Cash on Delivery available?', 'Yes, on most pincodes, with a %s COD charge. You pay in cash when the parcel arrives. Paying online is cheaper: %s off instead.' % (rs(COD_FEE), rs(PREPAID_OFF))),
    ('How long does delivery take?', 'Orders are packed in 1 to 2 business days and usually delivered in 3 to 7 business days. You get tracking on WhatsApp.'),
    ('Can I return it?', 'Sealed, unused packs can be returned within 7 days of delivery. If your parcel arrives damaged, send us a photo on WhatsApp within 48 hours.'),
    ('Do I need a patch test?', 'Yes, for any new face cream. Apply a little behind the ear or on the jawline for 24 hours before using it on the whole face.'),
]

def layout(path, title, desc, body, schema=None, robots='index,follow', lang='en-IN', extra=''):
    can = SITE + path
    ld = ''.join('<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False) for x in (schema or []))
    cfg = json.dumps({'wa': WA, 'off': PREPAID_OFF, 'cod': COD_FEE, 'product': PRODUCT, 'size': SIZE, 'packs': [{'id': i, 'label': l, 'jars': j, 'price': p, 'cmp': PACK_INFO[i]['cmp'], 'img': PACK_INFO[i]['img']} for i, l, j, p in PACKS]}, ensure_ascii=False)
    return ('''<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title><meta name="description" content="%s"><link rel="canonical" href="%s"><meta name="robots" content="%s">
<meta property="og:type" content="website"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s"><meta property="og:image" content="%s/assets/og.png">
<meta name="theme-color" content="#8a2d52"><meta property="og:locale" content="en_IN"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css">%s%s</head><body>
<div class="top">@@TOPBAR@@</div>
<header class="site"><div class="wrap"><a class="logo" href="/">Cream X Emirates<small>30 ml · Free delivery in India</small></a>
<nav><a class="hide-m" href="/#how-to-use">How to use</a><a class="hide-m" href="/guides/">Guides</a><a class="hide-m" href="/faq/">FAQ</a><a class="hide-m" href="/review/">Reviews</a><a href="https://wa.me/%s" rel="noopener">WhatsApp</a></nav></div></header>
<main>%s</main>
<footer><div class="wrap"><div class="cols"><div><b>%s</b><p>%s<br>%s</p><p>WhatsApp: <a href="https://wa.me/%s">%s</a>%s</p></div>
<div><b>Shop</b><p><a href="/%s">%s</a><br><a href="/#order">Order on COD</a><br><a href="/review/">Write a review</a></p></div>
<div><b>Help</b><p><a href="/guides/">Guides</a><br><a href="/faq/">FAQ</a><br><a href="/shipping-policy/">Shipping</a><br><a href="/refund-policy/">Returns and refunds</a><br><a href="/privacy-policy/">Privacy</a><br><a href="/terms/">Terms</a><br><a href="/contact/">Contact</a></p></div></div>
<p class="disc">Cream X Emirates is a trademark of its owner. This website is run by %s, an independent seller, and is not the official brand website. Product information is general cosmetic guidance, not medical advice; results vary from person to person.<br>© %d %s</p></div></footer>
<a class="wa-float" href="https://wa.me/%s?text=%s" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true"><path fill="#fff" d="M16 3C9 3 3.3 8.6 3.3 15.6c0 2.5.7 4.8 1.9 6.8L3 29l6.8-2.1c1.9 1 4 1.6 6.2 1.6 7 0 12.7-5.6 12.7-12.6S23 3 16 3zm0 23.1c-2 0-3.9-.6-5.6-1.6l-.4-.2-4 1.2 1.3-3.9-.3-.4c-1.1-1.7-1.7-3.6-1.7-5.6C5.3 9.9 10.1 5.2 16 5.2s10.7 4.7 10.7 10.5S21.9 26.1 16 26.1zm5.9-7.8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.4c.2.2 2.4 3.7 5.8 5.1.8.4 1.4.6 1.9.7.8.3 1.6.2 2.2.1.7-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg><span>Chat with us</span></a>
<script>window.STORE=%s</script><script src="/assets/site.js" defer></script></body></html>''' % (
        lang, html.escape(title), html.escape(desc), can, robots, html.escape(title), html.escape(desc), can, SITE, ld, extra,
        WA, body, html.escape(OWNER), html.escape(STORE), html.escape(ADDR), WA, WA_SHOW,
        (' · <a href="mailto:%s">%s</a>' % (EMAIL, EMAIL)) if EMAIL else '', '', html.escape(PRODUCT), html.escape(OWNER), datetime.date.today().year, html.escape(OWNER), WA, __import__('urllib.parse').parse.quote('Hi, I have a question about %s (%s).' % (PRODUCT, SIZE)), cfg)).replace('@@TOPBAR@@', ('Extra %s off when you pay online · Free delivery across India' % rs(PREPAID_OFF)) if PREPAID_OFF else 'Free delivery across India · Pay online or Cash on Delivery')

def write(path, doc):
    d = os.path.join(ROOT, path.strip('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(doc)

def faq_html(items):
    return ''.join('<details><summary>%s</summary><p>%s</p></details>' % (html.escape(q), html.escape(a)) for q, a in items)

def faq_ld(items):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in items]}

def product_ld():
    p1 = PACKS[0]
    return {'@context': 'https://schema.org', '@type': 'Product', 'name': '%s %s' % (PRODUCT, SIZE), 'brand': {'@type': 'Brand', 'name': 'Cream X Emirates'},
            'description': 'Cream X Emirates (CXE) Glow Restoring Face Crème, %s: brightens, deeply hydrates, improves skin texture, nourishes and repairs. Sold by %s, an independent seller in India.' % (SIZE, OWNER), 'image': [SITE + '/assets/img/cxe-jars.jpg', SITE + '/assets/img/cxe-new-pack.jpg', SITE + '/assets/og.png'], 'url': SITE + '/', 'sku': 'CXE-30ML',
            'offers': {'@type': 'Offer', 'price': str(p1[3]), 'priceCurrency': 'INR', 'availability': 'https://schema.org/InStock', 'itemCondition': 'https://schema.org/NewCondition', 'url': SITE + '/',
                       'seller': {'@type': 'Organization', 'name': OWNER},
                       'shippingDetails': {'@type': 'OfferShippingDetails', 'shippingRate': {'@type': 'MonetaryAmount', 'value': '0', 'currency': 'INR'}, 'shippingDestination': {'@type': 'DefinedRegion', 'addressCountry': 'IN'},
                                           'deliveryTime': {'@type': 'ShippingDeliveryTime', 'handlingTime': {'@type': 'QuantitativeValue', 'minValue': 1, 'maxValue': 2, 'unitCode': 'DAY'}, 'transitTime': {'@type': 'QuantitativeValue', 'minValue': 2, 'maxValue': 5, 'unitCode': 'DAY'}}},
                       'hasMerchantReturnPolicy': {'@type': 'MerchantReturnPolicy', 'applicableCountry': 'IN', 'returnPolicyCategory': 'https://schema.org/MerchantReturnFiniteReturnWindow', 'merchantReturnDays': 7, 'returnMethod': 'https://schema.org/ReturnByMail', 'returnFees': 'https://schema.org/FreeReturn'}}}

def pic(name, alt, eager=False):
    return '<picture><source srcset="/assets/img/%s.webp" type="image/webp"><img src="/assets/img/%s.jpg" alt="%s" width="900" height="900" %s></picture>' % (name, name, alt, 'fetchpriority="high"' if eager else 'loading="lazy"')

def product_body(h1_tag='h1'):
    packs = ''.join('''<label class="pack"><input type="radio" name="pack" value="%s"%s><span class="l"><b>%s%s</b><span>%s</span></span><span class="r"><b>%s</b>%s</span></label>''' % (
        i, ' checked' if n == 0 else '', l, (' <span class="tag">%s</span>' % PACK_INFO[i]['tag']) if PACK_INFO[i]['tag'] else '', PACK_INFO[i]['sub'],
        rs(p), ('<s>%s</s>' % rs(PACK_INFO[i]['cmp'])) if PACK_INFO[i]['cmp'] else '') for n, (i, l, j, p) in enumerate(PACKS))
    opts = ''.join('<option value="%s">%s · %s</option>' % (i, l, rs(p)) for i, l, j, p in PACKS)
    p1 = PACKS[0]
    tiles = [pic('cxe-jars', 'Cream X Emirates CXE Glow Restoring Face Crème 30 ml jars', True), pic('cxe-new-pack', 'New pink CXE Glow Restoring Face Crème pack'), pic('cxe-old-pack', 'Old white Cream X Emirates pack'), pic('cxe-pack-2', 'Two new pink CXE Glow Restoring Face Crème jars, pack of 2'), ]
    thumbs = ''.join('<button type="button" aria-label="Image %d" aria-current="%s">%s</button>' % (n + 1, 'true' if n == 0 else 'false', t) for n, t in enumerate(tiles))
    return ('''<div class="wrap"><p class="crumb"><a href="/">Home</a> › Face cream</p>
<div class="pdp"><div><div class="gal-main">%s</div><div class="gal-thumbs">%s</div></div>
<div><span class="seller">New pack · same formula · 30 ml</span><%s>%s, %s</%s>
<p class="muted" style="margin:0">For a brighter, more even-looking, softer face, with a simple night routine</p>
<div class="price"><b data-price>%s</b><s data-mrp>@@MRPS@@</s><span class="save" data-save>@@SAVE@@</span></div><p class="tax">MRP inclusive of all taxes · free delivery</p><p class="online" id="onl">💳 Pay online: <b data-online>@@ONL@@</b> <span>extra @@OFF@@ off · UPI, cards, net banking</span></p>
<div class="packs" role="radiogroup" aria-label="Choose a pack">%s</div>
<div class="ctas"><a class="btn shine" href="#order" data-pay-go="online">Buy now · Pay online</a><a class="btn ghost" href="#order" data-pay-go="cod">Cash on Delivery <small data-codfee>(+@@CODFEE@@)</small></a></div>
<ul class="trust"><li>💳 Secure payment by Razorpay</li><li>💵 COD available (+@@CODFEE@@)</li><li>🚚 Free delivery in India</li><li>↩️ 7-day return on sealed packs</li></ul>
<p class="eta" style="margin-bottom:6px">📦 Order today, expected delivery <b id="eta">in 3 to 7 business days</b></p><p class="muted" style="font-size:.78rem;margin:0">Sealed, new stock from an independent seller; this is not the brand's official website.</p></div></div></div>
<section class="band alt" id="details"><div class="wrap"><h2>What it does</h2><p class="muted">The four benefits the brand states for the Glow Restoring Face Crème.</p><div class="feat">
<div class="card"><b>✨ Brightens skin</b><p>For dull, tired-looking skin; with regular night use and sunscreen, the face looks fresher and more radiant.</p></div>
<div class="card"><b>💧 Deep hydration</b><p>A rich crème that keeps skin moisturised overnight, so it feels soft and comfortable by morning.</p></div>
<div class="card"><b>〰️ Improves skin texture</b><p>With regular use, skin feels smoother and looks more even, including tan and uneven patches over 8 to 12 weeks.</p></div>
<div class="card"><b>🌿 Nourishes and repairs</b><p>Made to nourish the skin while you sleep, as part of a simple night routine.</p></div></div></section>
<section class="band"><div class="wrap grid2"><div><h2>What to expect</h2><ol class="tl"><li><b>Week 1 to 2</b><span>Skin adjusts and feels softer. If it feels dry or tingly, use every other night at first.</span></li>
<li><b>Week 3 to 4</b><span>Smoother feel and a fresher look in the morning.</span></li><li><b>Week 8 to 12</b><span>Tan and uneven patches look lighter, if you wear sunscreen every day.</span></li></ol>
<p class="muted" style="font-size:.85rem">Results vary from person to person. A face cream does not change your natural skin colour.</p></div>
<div class="card"><h3>Product details</h3><table class="spec"><tbody>
<tr><td>Product</td><td>%s</td></tr><tr><td>Also called</td><td>CXE crème, Cream X Emirates cream</td></tr><tr><td>Net quantity</td><td>%s</td></tr><tr><td>Type</td><td>Face crème, overnight</td></tr><tr><td>When to use</td><td>Night</td></tr>
<tr><td>Where</td><td>Face and neck; avoid eyes and lips</td></tr><tr><td>Skin type</td><td>Most adult skin; patch test first</td></tr><tr><td>Not for</td><td>Under 14, pregnancy, breastfeeding or elderly users without a doctor's advice</td></tr>
<tr><td>Ingredients</td><td>Full list printed on the pack</td></tr><tr><td>Packaging</td><td>New pink jar (replaces the old white jar); same formula</td></tr><tr><td>Delivery</td><td>Free across India, COD available</td></tr></tbody></table></div></div></section>
<section class="band" id="how-to-use"><div class="wrap"><h2>How to use</h2><p class="muted">Following the brand's directions, with a patch test first and sunscreen in the morning.</p><ol class="steps">
<li><b>Patch test first.</b> Apply a little behind the ear or on the jawline and wait 24 hours.</li>
<li><b>Cleanse.</b> Wash your face well and pat it dry.</li>
<li><b>Massage in.</b> Take a small amount and massage it into the face until it absorbs. Avoid the eyes and lips.</li>
<li><b>Wait, then layer.</b> After about 10 minutes, apply a second thin layer like a night mask and leave it on overnight.</li>
<li><b>Rinse in the morning.</b> Wash off with cold water, then apply SPF 30+ sunscreen. Use nightly.</li></ol>
<p class="note"><b>Not recommended</b> for children under 14, during pregnancy or breastfeeding, or for elderly users, unless a doctor approves. Do not apply on broken, sunburnt or irritated skin. Stop if you get burning, swelling or a rash, and see a doctor.</p></div></section>
<section class="band alt" id="order"><div class="wrap grid2"><div><h2>Place your order</h2><p>Pay online to get <b>@@OFF@@ off</b> and faster dispatch: prepaid orders are packed first. Payment is handled securely by Razorpay (UPI, cards, net banking, wallets).</p>
<p class="muted">Prefer to pay at the door? Cash on Delivery is available with a @@CODFEE@@ COD charge.</p></div>
<form class="order" id="orderForm" novalidate><label>Pack<select name="pack" id="oPack">%s</select></label>
<label>Full name<input name="name" autocomplete="name" required></label><label>Mobile number<input name="phone" type="tel" inputmode="numeric" autocomplete="tel" required placeholder="10-digit number"></label>
<label>Full address<textarea name="address" rows="3" autocomplete="street-address" required placeholder="House no., street, area, landmark"></textarea></label>
<div class="two"><label>City<input name="city" autocomplete="address-level2"></label><label>Pincode<input name="pin" inputmode="numeric" maxlength="6" autocomplete="postal-code" required></label></div>
<fieldset class="paysel"><legend>Payment</legend><label class="pay"><input type="radio" name="paym" value="online" checked><span><b>Pay online <span class="tag">Save @@OFF@@</span></b><small>UPI, cards, net banking, wallets · Razorpay</small></span><b data-online>@@ONL@@</b></label><label class="pay"><input type="radio" name="paym" value="cod"><span><b>Cash on Delivery</b><small>+@@CODFEE@@ COD charge · pay in cash at the door</small></span><b data-codprice>@@CODP@@</b></label></fieldset>
<input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;height:0;width:0;opacity:0"><p class="err" id="oErr" role="alert"></p><button class="btn block shine" type="submit" id="oGo">Pay @@ONL@@ securely</button><p class="muted" style="font-size:.78rem;text-align:center;margin:0">🔒 Secured by Razorpay. We never see your card or UPI PIN.</p></form><div id="oDone" class="card" hidden></div></div></section>
<section class="band"><div class="wrap"><h2>Reviews</h2><p>No reviews yet. Bought from us? <a href="/review/">Share an honest review</a>; we publish real reviews only, with the customer's permission.</p></div></section>
<section class="band"><div class="wrap grid2"><div><h2>Quick facts</h2><table class="spec"><tbody><tr><td>Product</td><td>CXE Glow Restoring Face Crème</td></tr><tr><td>Size</td><td>30 ml jar</td></tr><tr><td>MRP</td><td>₹2,200 (new jar) · ₹999 (old jar)</td></tr><tr><td>Price</td><td>New jar @@P1@@ · 2 jars @@P2@@ · old jar @@PO@@</td></tr><tr><td>Use</td><td>Night, on the face; rinse in the morning</td></tr><tr><td>Results</td><td>Softer in 2 to 4 weeks; more even in 8 to 12 weeks with sunscreen</td></tr><tr><td>Not for</td><td>Under 14, pregnancy, elderly users</td></tr><tr><td>Delivery</td><td>Free, all India, Cash on Delivery</td></tr><tr><td>Returns</td><td>7 days on sealed packs</td></tr></tbody></table></div><div><h2>Guides</h2><ul class="glist">@@GUIDES@@</ul></div></div></section>
<section class="band alt"><div class="wrap prose"><h2>Questions</h2>%s<p><a href="/faq/">All questions</a></p></div></section>
<div class="sticky"><div class="p"><b data-online>@@ONL@@</b><small>paying online</small></div><a class="btn" href="#order" data-pay-go="online">Buy now</a></div>''' % (
        tiles[0], thumbs, h1_tag, html.escape(PRODUCT), SIZE, h1_tag, rs(p1[3]), packs,
        html.escape(PRODUCT), SIZE, opts, faq_html(FAQ[:5]))).replace('@@MRPS@@', rs(PACK_INFO[p1[0]]['cmp']) if PACK_INFO[p1[0]]['cmp'] else '').replace('@@SAVE@@', ('Save ' + rs(PACK_INFO[p1[0]]['cmp'] - p1[3])) if PACK_INFO[p1[0]]['cmp'] else '').replace('@@P1@@', rs(p1[3])).replace('@@P2@@', rs(PACKS[1][3])).replace('@@PO@@', rs(PACKS[2][3])).replace('@@ONL@@', rs(p1[3] - PREPAID_OFF)).replace('@@OFF@@', rs(PREPAID_OFF)).replace('@@CODFEE@@', rs(COD_FEE)).replace('@@CODP@@', rs(p1[3] + COD_FEE))

def simple(path, title, desc, h1, inner, schema=None):
    write(path, layout(path, title, desc, '<section class="band" style="border:0"><div class="wrap prose"><p class="crumb"><a href="/">Home</a> › %s</p><h1>%s</h1>%s</div></section>' % (html.escape(h1), html.escape(h1), inner), schema))

def build():
    os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
    os.makedirs(os.path.join(ROOT, 'api'), exist_ok=True)
    open(os.path.join(ROOT, 'api/_packs.json'), 'w').write(json.dumps({'site': SITE.split('//')[-1], 'prepaidOff': PREPAID_OFF, 'codFee': COD_FEE, 'product': PRODUCT, 'size': SIZE, 'packs': [{'id': i, 'label': l, 'jars': j, 'price': p, 'desk': 'cx%d' % (n + 1)} for n, (i, l, j, p) in enumerate(PACKS)]}, ensure_ascii=False, indent=1))
    open(os.path.join(ROOT, 'assets/site.css'), 'w').write(CSS)
    open(os.path.join(ROOT, 'assets/site.js'), 'w').write(JS)
    open(os.path.join(ROOT, 'assets/jar.svg'), 'w').write(JAR)
    open(os.path.join(ROOT, 'favicon.svg'), 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#fbe9ef"/><rect x="12" y="18" width="40" height="12" rx="4" fill="#8a2d52"/><rect x="15" y="29" width="34" height="20" rx="5" fill="#fff" stroke="#e2c6d1"/></svg>')
    title = '%s %s: Price, Benefits, How to Use | COD India' % (PRODUCT, SIZE)
    desc = 'Buy %s (%s) online for %s: benefits, how to use, what to expect week by week, free delivery across India and Cash on Delivery.' % (PRODUCT, SIZE, rs(PACKS[0][3]))
    sch = [product_ld(), faq_ld(FAQ[:5]), {'@context': 'https://schema.org', '@type': 'Organization', 'name': OWNER, 'url': SITE, 'address': ADDR, 'contactPoint': {'@type': 'ContactPoint', 'telephone': '+' + WA, 'contactType': 'customer service', 'areaServed': 'IN'}}]
    import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import seo
    extra_urls = seo.build_all(globals(), sch, title, desc)
    # /product/... redirects to the home page (vercel.json), so there is one product page and no duplicate
    open(os.path.join(ROOT, 'vercel.json'), 'w').write(json.dumps({'cleanUrls': False, 'trailingSlash': True, 'redirects': [{'source': PURL.rstrip('/'), 'destination': '/', 'permanent': True}, {'source': PURL, 'destination': '/', 'permanent': True}]}, indent=2))
    simple('/faq/', 'Cream X Emirates FAQ: How to Use, Delivery, COD and Returns', 'Answers about using %s, who should avoid it, delivery times, Cash on Delivery and returns.' % PRODUCT, 'Questions and answers', faq_html(FAQ), [faq_ld(FAQ)])
    simple('/shipping-policy/', 'Shipping Policy | Cream X Emirates', 'Free delivery across India. Orders packed in 1 to 2 business days and delivered in 3 to 7 business days.', 'Shipping policy',
           '<ul><li>Free delivery on all orders across India.</li><li>Orders are packed in 1 to 2 business days and usually delivered in 3 to 7 business days.</li><li>Cash on Delivery is available on most pincodes our courier serves, with a ' + rs(COD_FEE) + ' COD charge. Online payment has no extra charge and gets ' + rs(PREPAID_OFF) + ' off.</li><li>Tracking is shared on WhatsApp once the parcel ships.</li><li>Remote areas can take a few extra days.</li></ul>')
    simple('/refund-policy/', 'Returns and Refunds | Cream X Emirates', 'Sealed, unused packs can be returned within 7 days of delivery. Damaged parcels: send a photo within 48 hours.', 'Returns and refunds',
           '<ul><li>Sealed, unused packs can be returned within 7 days of delivery.</li><li>For hygiene reasons, opened products cannot be returned unless they arrived damaged or wrong.</li><li>Damaged or wrong item: send a photo or unboxing video on WhatsApp within 48 hours of delivery and we will replace it or refund you.</li><li>Refunds are made to your UPI or bank account within 5 to 7 business days after we receive the return.</li></ul><p>WhatsApp: <a href="https://wa.me/%s">%s</a></p>' % (WA, WA_SHOW))
    simple('/privacy-policy/', 'Privacy Policy | Cream X Emirates', 'How %s uses the name, phone number and address you share to deliver your order.' % STORE, 'Privacy policy',
           '<p>We collect only what we need to deliver your order: your name, mobile number and address, which you send us on WhatsApp. We share it only with our courier partner for delivery. We do not sell your data. To have your details deleted, message us on WhatsApp at %s.</p>' % WA_SHOW)
    simple('/terms/', 'Terms of Sale | Cream X Emirates', 'Terms for orders placed with %s.' % OWNER, 'Terms of sale',
           '<p>Orders on this website are sold and shipped by %s, %s. %s is an independent seller and is not the brand owner of Cream X Emirates. Prices include all taxes. We may cancel an order if a product is out of stock or a pincode is not serviceable, and will tell you on WhatsApp. Product information is general cosmetic guidance, not medical advice.</p>' % (html.escape(OWNER), html.escape(ADDR), html.escape(STORE)))
    simple('/contact/', 'Contact | Cream X Emirates', 'Contact %s on WhatsApp for orders, tracking and returns.' % STORE, 'Contact us',
           '<p><b>%s</b><br>%s</p><p>WhatsApp: <a href="https://wa.me/%s">%s</a><br>Monday to Saturday, 10 am to 7 pm</p>' % (html.escape(OWNER), html.escape(ADDR), WA, WA_SHOW))
    simple('/review/', 'Review Your Order | Cream X Emirates', 'Bought %s from %s? Share an honest review on WhatsApp.' % (PRODUCT, STORE), 'Share your review',
           '''<p>Tell us honestly how the cream worked for you. With your permission we may show your review on this website with your first name and city only.</p>
<form class="order" onsubmit="return false"><label>Rating<select id="rvR"><option>5 - Excellent</option><option>4 - Good</option><option>3 - Okay</option><option>2 - Not great</option><option>1 - Poor</option></select></label>
<label>How long have you used it?<select id="rvT"><option>Less than 2 weeks</option><option>2 to 4 weeks</option><option>1 to 2 months</option><option>More than 2 months</option></select></label>
<label>Your review<textarea id="rvX" rows="5" placeholder="What did you like? What could be better? Your skin type helps too."></textarea></label>
<label>First name and city<input id="rvN" placeholder="e.g. Priya, Mangaluru"></label>
<label style="display:flex;gap:8px;align-items:flex-start;font-weight:400"><input type="checkbox" id="rvOk" style="width:auto;margin-top:5px"> You may show my review on the website with my first name and city.</label>
<button class="btn" id="rvGo" type="button">Send review on WhatsApp</button></form>
<h2 style="margin-top:28px">Review policy</h2><ul><li>Real customers only, shown with permission.</li><li>No paid reviews, no discounts for good ratings.</li><li>We show mixed reviews too.</li></ul>''')
    urls = ['/'] + extra_urls + ['/faq/', '/review/', '/shipping-policy/', '/refund-policy/', '/privacy-policy/', '/terms/', '/contact/']
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % ''.join('<url><loc>%s%s</loc><lastmod>%s</lastmod></url>' % (SITE, u, TODAY) for u in urls))
    open(os.path.join(ROOT, 'robots.txt'), 'w').write(''.join('User-agent: %s\nAllow: /\n\n' % b for b in ['*', 'Googlebot', 'Bingbot', 'GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot', 'ClaudeBot', 'Claude-SearchBot', 'Google-Extended', 'Applebot-Extended']) + 'Sitemap: %s/sitemap.xml\n' % SITE)
    print('built', len(urls), 'pages')

if __name__ == '__main__':
    build()
