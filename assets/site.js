(function(){
var C=window.STORE||{};var $=function(s){return document.querySelector(s)};
function pack(){var r=document.querySelector('input[name=pack]:checked');return C.packs.filter(function(p){return p.id===(r?r.value:'p1')})[0]}
function rs(n){return '₹'+n.toLocaleString('en-IN')}
function sync(){var p=pack();if(!p)return;var mrp=C.mrp*p.jars;document.querySelectorAll('[data-price]').forEach(function(e){e.textContent=rs(p.price)});
document.querySelectorAll('[data-mrp]').forEach(function(e){e.textContent=rs(mrp)});document.querySelectorAll('[data-save]').forEach(function(e){e.textContent='Save '+rs(mrp-p.price)});document.querySelectorAll('[data-online]').forEach(function(e){e.textContent=rs(p.price-C.off)});document.querySelectorAll('[data-codprice]').forEach(function(e){e.textContent=rs(p.price+C.cod)});payLabel();
var o=$('#oPack');if(o)o.value=p.id;var t=document.querySelectorAll('.gal-thumbs button');var k=p.jars===2?3:0;if(t[k]&&sync.ready){t[k].click()}sync.ready=true}
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
})();