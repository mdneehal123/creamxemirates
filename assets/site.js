(function(){
var C=window.STORE||{};var $=function(s){return document.querySelector(s)};
function pack(){var r=document.querySelector('input[name=pack]:checked');return C.packs.filter(function(p){return p.id===(r?r.value:'p1')})[0]}
function rs(n){return '₹'+n.toLocaleString('en-IN')}
function sync(){var p=pack();if(!p)return;var mrp=C.mrp*p.jars;document.querySelectorAll('[data-price]').forEach(function(e){e.textContent=rs(p.price)});
document.querySelectorAll('[data-mrp]').forEach(function(e){e.textContent=rs(mrp)});document.querySelectorAll('[data-save]').forEach(function(e){e.textContent='Save '+rs(mrp-p.price)});
var o=$('#oPack');if(o)o.value=p.id}
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
// order form -> WhatsApp
var f=$('#orderForm');if(f){f.addEventListener('submit',function(e){e.preventDefault();var g=function(i){return(f.elements[i].value||'').trim()};var err=$('#oErr');
var ph=g('phone').replace(/\D/g,'').replace(/^91(?=\d{10}$)/,'');if(g('name').length<2){err.textContent='Please enter your name.';return}
if(!/^[6-9]\d{9}$/.test(ph)){err.textContent='Please enter a 10-digit mobile number.';return}if(!/^\d{6}$/.test(g('pin'))){err.textContent='Please enter a 6-digit pincode.';return}
if(g('address').length<10){err.textContent='Please enter your full address.';return}err.textContent='';
var p=C.packs.filter(function(x){return x.id===g('pack')})[0];
wa('New order\nProduct: '+C.product+' ('+C.size+')\nPack: '+p.label+'\nTotal: '+rs(p.price)+' (free delivery)\nPayment: '+g('pay')+'\n\nName: '+g('name')+'\nMobile: '+ph+'\nAddress: '+g('address')+'\nCity: '+g('city')+'\nPincode: '+g('pin'))})}
// sticky bar after scrolling past the buy buttons
var s=$('.sticky'),c=$('.ctas');if(s&&c&&'IntersectionObserver' in window){new IntersectionObserver(function(e){s.classList.toggle('show',!e[0].isIntersecting&&e[0].boundingClientRect.top<0)}).observe(c)}
// review form
var rv=$('#rvGo');if(rv)rv.addEventListener('click',function(){var g=function(i){return($('#'+i).value||'').trim()};if(g('rvX').length<10){$('#rvX').focus();return}
wa('Review: '+C.product+'\nRating: '+g('rvR')+'\nUsed for: '+g('rvT')+'\nReview: '+g('rvX')+'\nName and city: '+(g('rvN')||'-')+'\nOK to show on website: '+($('#rvOk').checked?'Yes':'No'))});
})();