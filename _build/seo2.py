# SEO round 2 (6 Nov 2026): pages for the new name (CXE), the packaging change, and more Malayalam and Tamil pages.
# guides2() returns extra English guides; locals2() extra regional pages (each with 'en' = its English twin).

def guides2(rs, PACKS, OFF, CODF, WA, WA_SHOW):
    p1, p2, po = PACKS[0][3], PACKS[1][3], PACKS[2][3]
    return [
        dict(slug='cxe-glow-restoring-face-creme', short='CXE crème',
             title='CXE Glow Restoring Face Crème (Crème X): The New Name of Cream X Emirates',
             seo='CXE Glow Restoring Face Crème (Cream X Emirates) 30 ml: Price, Use',
             desc='CXE Glow Restoring Face Crème is the new pink-jar pack of Cream X Emirates. What CXE means, what changed, price (%s), how to use it, and who should not use it.' % rs(p1),
             answer='<b>CXE</b> is short for <b>Cream X Emirates</b>. The <b>CXE Glow Restoring Face Crème</b> is the brand\'s new pink 30 ml jar, which replaced the old white jar; the brand says the <b>formula is the same</b>. Here it is <b>%s</b> (MRP ₹2,200), %s for two.' % (rs(p1), rs(p2)),
             body='''<h2>CXE, Cream X Emirates, Crème X: one product</h2><p>You may see the same cream called <b>Cream X Emirates</b>, <b>CXE</b>, <b>CXE crème</b>, <b>Crème X</b> or <b>Creme X</b>. The new pack says "cxe Glow Restoring Face Crème" on the lid and "crème X" on the side, 30 ml / 1.05 fl oz.</p>
<h2>What the brand says it does</h2><ul><li>Brightens skin</li><li>Deep hydration</li><li>Improves skin texture</li><li>Nourishes and repairs</li></ul><p>Like any face cream, it works gradually: softer skin in a few weeks, a more even look over 8 to 12 weeks with daily sunscreen. Results vary.</p>
<h2>How to use</h2><p>At night: cleanse, massage in a small amount, wait about 10 minutes, apply a thin second layer as an overnight mask, and rinse with cold water in the morning. Full steps: <a href="/how-to-use-cream-x-emirates/">how to use Cream X Emirates</a>.</p>
<h2>Price</h2><div class="tbl"><table class="spec"><tbody><tr><td>1 new pink jar</td><td><s>₹2,200</s> <b>%s</b></td></tr><tr><td>2 new pink jars</td><td><s>₹4,400</s> <b>%s</b></td></tr><tr><td>1 old white jar (clearance)</td><td><s>₹999</s> <b>%s</b></td></tr></tbody></table></div><p>Pay online for %s off; Cash on Delivery adds %s. Delivery is free across India.</p>
<h2>Who should not use it</h2><p>The brand does not recommend it for children under 14, pregnant women or elderly people. Patch test first and stop if you get burning, swelling or a rash.</p>''' % (rs(p1), rs(p2), rs(po), rs(OFF), rs(CODF)),
             faq=[('What is CXE cream?', 'CXE is Cream X Emirates. CXE Glow Restoring Face Crème is its new pink 30 ml pack, with the same formula as the old white jar according to the brand.'),
                  ('Is CXE the same as Cream X Emirates?', 'Yes. CXE is the short name used on the new pink pack.'),
                  ('What is the price of CXE Glow Restoring Face Crème?', '%s for one 30 ml jar (MRP ₹2,200), %s for two.' % (rs(p1), rs(p2)))]),

        dict(slug='cream-x-emirates-new-packing', short='New packing',
             title='Cream X Emirates New Packing: Old White Jar vs New Pink CXE Jar',
             seo='Cream X Emirates New Packing: Old vs New Jar Explained',
             desc='Cream X Emirates has a new packing: the white jar is now a pink CXE Glow Restoring Face Crème jar. How to tell them apart, whether the formula changed, and which to buy.',
             answer='Cream X Emirates changed its packing from a <b>white jar</b> to a <b>pink "CXE Glow Restoring Face Crème" jar</b> (30 ml). The brand says the <b>formula is the same</b>. Both are genuine while old stock sells out: the new jar is %s and the old white jar is %s here.' % (rs(p1), rs(po)),
             body='''<figure><img src="/assets/img/cxe-old-vs-new.jpg" alt="Old white Cream X Emirates jar and new pink CXE jar" width="900" height="1125" loading="lazy" style="width:100%%;max-width:520px;height:auto;border-radius:14px"><figcaption class="meta">Old (white) and new (pink) packs. Image from the brand.</figcaption></figure>
<h2>How to tell them apart</h2><div class="tbl"><table class="spec"><thead><tr><th></th><th>Old jar</th><th>New jar</th></tr></thead><tbody>
<tr><td>Colour</td><td>White jar and lid</td><td>Pink jar and lid</td></tr><tr><td>Name on pack</td><td>"cream X emirates"</td><td>"cxe Glow Restoring Face Crème", "crème X"</td></tr>
<tr><td>Size</td><td>30</td><td>30 ml / 1.05 fl oz</td></tr><tr><td>MRP</td><td>₹999</td><td>₹2,200</td></tr><tr><td>Our price</td><td>%s</td><td>%s</td></tr></tbody></table></div>
<h2>Which one should I buy?</h2><ul><li><b>Old white jar:</b> lowest price while stock lasts. Check the expiry date when it arrives.</li><li><b>New pink jar:</b> the current pack, with the longest shelf life.</li></ul>
<h2>Is a white jar fake now?</h2><p>No. A sealed white jar with printed batch and expiry details can be genuine old stock. What matters is the seal, the printed details and a sensible price. See <a href="/original-cream-x-emirates/">how to spot a fake pack</a>.</p>''' % (rs(po), rs(p1)),
             faq=[('Did the Cream X Emirates formula change?', 'The brand says no: only the packaging changed, from a white jar to a pink CXE jar.'),
                  ('Is the old white jar still genuine?', 'Yes, sealed old stock with printed batch and expiry details is genuine. Check the expiry date.'),
                  ('Why is the old jar cheaper?', 'We are clearing the remaining old-pack stock at %s.' % rs(po))]),
    ]


def locals2(rs, PACKS):
    p1, p2, po = PACKS[0][3], PACKS[1][3], PACKS[2][3]
    return [
        dict(lang='ml', code='ml-IN', path='/ml/cream-x-emirates-side-effects/', en='/cream-x-emirates-side-effects/',
             title='Cream X Emirates പാർശ്വഫലങ്ങൾ: എന്താണ് സാധാരണം, എപ്പോൾ നിർത്തണം',
             desc='Cream X Emirates side effects in Malayalam: പുതിയ ക്രീം ഉപയോഗിക്കുമ്പോൾ ഉണ്ടാകാവുന്ന ചെറിയ പ്രശ്നങ്ങൾ, എപ്പോൾ നിർത്തണം, ആർ ഉപയോഗിക്കരുത്.',
             h1='Cream X Emirates പാർശ്വഫലങ്ങൾ',
             body='''<p class="answer">മിക്കവർക്കും <b>പ്രശ്നമൊന്നുമില്ല, അല്ലെങ്കിൽ ആദ്യ ദിവസങ്ങളിൽ ചെറിയ വരൾച്ചയോ ചൊറിച്ചിലോ</b> മാത്രം. <b>പൊള്ളൽ, വീക്കം, ചൊറിച്ചിലുള്ള തടിപ്പ്</b> ഉണ്ടായാൽ നിർത്തി ഡോക്ടറെ കാണുക. ആദ്യം <b>പാച്ച് ടെസ്റ്റ്</b> ചെയ്യുക.</p>
<h2>സാധാരണ ചെറിയ പ്രശ്നങ്ങൾ</h2><ul><li>കുറച്ച് മിനിറ്റ് നേരിയ ചൂട് അല്ലെങ്കിൽ തരിപ്പ്</li><li>ചെറിയ വരൾച്ച</li><li>എണ്ണമയമുള്ള ചർമ്മത്തിൽ ആദ്യ ആഴ്ച ചെറിയ കുരുക്കൾ</li></ul><p>ഇവ സാധാരണയായി 1–2 ആഴ്ചയിൽ കുറയും. ആദ്യം ഒന്നിടവിട്ട രാത്രികളിൽ ഉപയോഗിക്കുക.</p>
<h2>ഉടൻ നിർത്തേണ്ടത്</h2><ul><li>മാറാത്ത പൊള്ളൽ, ചുവപ്പ്, വീക്കം</li><li>ചൊറിച്ചിലുള്ള തടിപ്പ്</li><li>പുതിയ കറുത്ത പാടുകൾ</li><li>ചുണ്ടോ കണ്ണോ വീങ്ങുക, ശ്വാസതടസ്സം: ഉടൻ ചികിത്സ തേടുക</li></ul>
<h2>ആർ ഉപയോഗിക്കരുത്</h2><p>14 വയസ്സിൽ താഴെയുള്ള കുട്ടികൾ, ഗർഭിണികൾ, പ്രായമായവർ എന്നിവർക്ക് ബ്രാൻഡ് ശുപാർശ ചെയ്യുന്നില്ല.</p>
<h2>പാച്ച് ടെസ്റ്റ്</h2><ol><li>ചെവിക്ക് പിന്നിൽ കുറച്ച് പുരട്ടുക.</li><li>24 മണിക്കൂർ കാത്തിരിക്കുക.</li><li>ചുവപ്പോ ചൊറിച്ചിലോ ഇല്ലെങ്കിൽ മുഖത്ത് ഉപയോഗിക്കാം.</li></ol>''',
             faq=[('Cream X Emirates സുരക്ഷിതമാണോ?', 'മിക്ക മുതിർന്നവർക്കും പ്രശ്നമില്ല. ആദ്യം പാച്ച് ടെസ്റ്റ് ചെയ്യുക, പ്രശ്നമുണ്ടായാൽ നിർത്തുക.'),
                  ('ഗർഭിണികൾക്ക് ഉപയോഗിക്കാമോ?', 'ഇല്ല. ഗർഭകാലത്ത് ബ്രാൻഡ് ശുപാർശ ചെയ്യുന്നില്ല.'),
                  ('കുരുക്കൾ വരുമോ?', 'ആദ്യ ആഴ്ച ചിലർക്ക് ചെറിയ കുരുക്കൾ വരാം. 2 ആഴ്ച കഴിഞ്ഞും കൂടുന്നുവെങ്കിൽ നിർത്തി ഡോക്ടറെ കാണുക.')]),
        dict(lang='ml', code='ml-IN', path='/ml/cream-x-emirates-result/', en='/cream-x-emirates-results/',
             title='Cream X Emirates റിസൾട്ട്: എത്ര ദിവസം കൊണ്ട് ഫലം കാണും',
             desc='Cream X Emirates results in Malayalam: ആഴ്ച തോറും എന്ത് പ്രതീക്ഷിക്കാം, ഫലം വേഗത്തിലാക്കാൻ എന്ത് ചെയ്യണം.',
             h1='Cream X Emirates: എത്ര ദിവസം കൊണ്ട് ഫലം?',
             body='''<p class="answer"><b>2–4 ആഴ്ചയിൽ ചർമ്മം മൃദുവാകും</b>. <b>8–12 ആഴ്ചയിൽ</b>, ദിവസവും <b>സൺസ്ക്രീനോടൊപ്പം</b>, മുഖം കൂടുതൽ തിളക്കമുള്ളതും നിറം ഒരേപോലെയുമായി തോന്നും. "7 ദിവസം കൊണ്ട്" എന്ന വാഗ്ദാനം ഒരു ക്രീമിനും യാഥാർത്ഥ്യമല്ല.</p>
<h2>ആഴ്ച തോറും</h2><ul><li><b>1–2 ആഴ്ച:</b> ചർമ്മം ശീലിക്കുന്നു, മൃദുവായി തോന്നും.</li><li><b>3–4 ആഴ്ച:</b> രാവിലെ മിനുസവും പുതുമയും.</li><li><b>5–8 ആഴ്ച:</b> മങ്ങൽ കുറയുന്നു, നേരിയ ടാൻ കുറഞ്ഞതായി തോന്നും.</li><li><b>8–12 ആഴ്ച:</b> ടാനും അസമമായ പാടുകളും കൂടുതൽ ഒരേപോലെ.</li></ul>
<h2>ഫലം വേഗത്തിലാക്കാൻ</h2><ul><li>എല്ലാ ദിവസവും രാവിലെ SPF 30+ സൺസ്ക്രീൻ</li><li>എല്ലാ രാത്രിയും മുടങ്ങാതെ ഉപയോഗിക്കുക</li><li>നാരങ്ങ, ബ്ലീച്ച് പോലുള്ളവ ഒഴിവാക്കുക</li></ul>
<p>ഫലം ഓരോരുത്തർക്കും വ്യത്യസ്തമാണ്. ഒരു ക്രീമും സ്വാഭാവിക നിറം മാറ്റില്ല.</p>
<p><a class="btn" href="/#order">ഇപ്പോൾ ഓർഡർ ചെയ്യുക</a></p>''',
             faq=[('7 ദിവസം കൊണ്ട് ഫലം കിട്ടുമോ?', 'ചർമ്മം പെട്ടെന്ന് മൃദുവാകാം, പക്ഷേ ടാനിൽ മാറ്റം കാണാൻ 8–12 ആഴ്ച വേണം.'),
                  ('ഒരു ജാർ എത്ര നാൾ വരും?', 'ഏകദേശം 4–6 ആഴ്ച. ഫലം ശരിയായി അറിയാൻ 2 ജാർ നല്ലതാണ്.'),
                  ('നിർത്തിയാൽ എന്ത് സംഭവിക്കും?', 'ദോഷമൊന്നുമില്ല. സൺസ്ക്രീൻ ഇല്ലെങ്കിൽ ടാൻ തിരികെ വരാം.')]),
        dict(lang='ta', code='ta-IN', path='/ta/cream-x-emirates/', en='/',
             title='Cream X Emirates விலை, பயன்படுத்தும் முறை | COD',
             desc='Cream X Emirates 30 ml ஃபேஸ் கிரீம்: விலை %s, பயன்படுத்தும் முறை, யார் பயன்படுத்தக் கூடாது, இலவச டெலிவரி.' % rs(p1),
             h1='Cream X Emirates ஃபேஸ் கிரீம், 30 ml',
             body='''<p class="answer">ஒரு புதிய 30 ml ஜாடி <b>%s</b> (MRP <s>₹2,200</s>), இரண்டு ஜாடிகள் <b>%s</b>, பழைய வெள்ளை ஜாடி <b>%s</b>. இந்தியா முழுவதும் <b>இலவச டெலிவரி</b>.</p>
<h2>எப்படிப் பயன்படுத்துவது</h2><ol><li>முதலில் காதுக்குப் பின்னால் 24 மணி நேரம் பேட்ச் டெஸ்ட் செய்யுங்கள்.</li><li>இரவில் முகத்தைக் கழுவி உலர்த்துங்கள்.</li><li>சிறிது கிரீம் எடுத்து முகத்தில் மசாஜ் செய்யுங்கள். கண், உதடு அருகே வேண்டாம்.</li><li>10 நிமிடம் கழித்து மெல்லிய இரண்டாவது அடுக்கை மாஸ்க் போல இரவு முழுவதும் வைத்திருங்கள்.</li><li>காலையில் குளிர்ந்த நீரில் கழுவி சன்ஸ்கிரீன் தடவுங்கள்.</li></ol>
<h2>பலன் எப்போது</h2><p>2–4 வாரங்களில் சருமம் மென்மையாகும். 8–12 வாரங்களில், தினமும் சன்ஸ்கிரீனுடன், டான் மற்றும் சீரற்ற நிறம் குறைந்ததாகத் தெரியும். பலன் நபருக்கு நபர் மாறுபடும்.</p>
<h2>யார் பயன்படுத்தக் கூடாது</h2><p>14 வயதுக்குட்பட்ட குழந்தைகள், கர்ப்பிணிகள், முதியவர்களுக்கு பிராண்ட் பரிந்துரைக்கவில்லை. எரிச்சல், வீக்கம், அரிப்பு ஏற்பட்டால் நிறுத்தி மருத்துவரைப் பாருங்கள்.</p>
<p><a class="btn" href="/#order">இப்போதே ஆர்டர் செய்யுங்கள்</a></p>''' % (rs(p1), rs(p2), rs(po)),
             faq=[('Cream X Emirates விலை என்ன?', 'ஒரு புதிய 30 ml ஜாடி %s, இலவச டெலிவரியுடன்.' % rs(p1)),
                  ('கேஷ் ஆன் டெலிவரி உண்டா?', 'ஆம், ₹100 கூடுதல் கட்டணத்துடன். ஆன்லைனில் செலுத்தினால் ₹50 தள்ளுபடி.'),
                  ('எத்தனை நாளில் பலன்?', '8–12 வாரங்கள், தினமும் சன்ஸ்கிரீனுடன்.')]),
    ]

def guides3(rs, PACKS, OFF, CODF, WA, WA_SHOW):
    p1, p2, po = PACKS[0][3], PACKS[1][3], PACKS[2][3]
    return [
        dict(slug='is-cream-x-emirates-a-whitening-cream', short='Whitening cream?',
             title='Is Cream X Emirates a Whitening Cream? What It Can and Cannot Do',
             seo='Is Cream X Emirates a Whitening Cream? Honest Answer',
             desc='Cream X Emirates is often sold as a "whitening cream". What a face cream like this can realistically do for tan, dullness and dark spots, what it cannot do, and how to get the best results safely.',
             answer='Cream X Emirates is often <b>advertised as a whitening cream</b>, but no face cream changes your natural skin colour. What it can do, used nightly with <b>daily sunscreen</b>, is make skin look <b>brighter, more even and softer</b>, with tan and dark spots looking lighter over <b>8 to 12 weeks</b>.',
             body='''<h2>What it can do</h2><ul><li>Help skin look brighter and less dull</li><li>Help tan and uneven patches look lighter over weeks</li><li>Keep skin hydrated and softer overnight</li></ul>
<h2>What no cream can do</h2><ul><li>Change your natural, genetic skin colour</li><li>Remove deep pigmentation or melasma on its own</li><li>Work in 7 days. Claims like "fair in a week" are not realistic</li></ul>
<h2>Why "whitening" claims need care</h2><p>Some unbranded "fast whitening" creams have been found to contain steroids or mercury, which can damage skin. Buy only sealed packs with a printed ingredient list, batch number and expiry date. Read <a href="/original-cream-x-emirates/">how to check an original pack</a>.</p>
<h2>How to get the best result</h2><ol><li>Use it every night, following the <a href="/how-to-use-cream-x-emirates/">brand's routine</a>.</li><li>Wear SPF 30+ sunscreen every morning: it matters more than any cream for tan.</li><li>Give it 8 to 12 weeks before judging.</li></ol>
<p>New pink jar: <b>%s</b> (MRP ₹2,200) · 2 jars: <b>%s</b> · old white jar: <b>%s</b>. %s off when you pay online.</p>''' % (rs(p1), rs(p2), rs(po), rs(OFF)),
             faq=[('Does Cream X Emirates make skin fair?', 'It can make skin look brighter and more even over weeks with sunscreen, but it does not change your natural skin colour.'),
                  ('How fast does Cream X Emirates work?', 'Skin often feels softer in 2 to 4 weeks; tan and dark spots look lighter over 8 to 12 weeks with daily sunscreen.'),
                  ('Is it safe to use every day?', 'Most adults can use it nightly. Patch test first; the brand does not recommend it for children under 14, pregnant women or elderly people.')]),

        dict(slug='where-to-buy-cream-x-emirates', short='Where to buy',
             title='Where to Buy Original Cream X Emirates in India (With COD)',
             seo='Where to Buy Original Cream X Emirates Online in India',
             desc='Where to buy original Cream X Emirates online in India: what to check before you pay, why very low prices are risky, and how to order sealed packs with Cash on Delivery.',
             answer='Buy Cream X Emirates from a seller that ships <b>sealed packs</b>, shows a <b>full address and phone number</b>, offers <b>returns</b>, and sells at a sensible price. Here you get sealed stock with <b>free delivery</b>, <b>online payment (%s off)</b> or <b>Cash on Delivery</b>, and a <b>7-day return</b> on sealed packs.' % rs(OFF),
             body='''<h2>Checklist before you buy anywhere</h2><ul><li><b>Seller details:</b> a real business name, address and phone or WhatsApp number.</li><li><b>Sealed pack:</b> the jar should arrive sealed, with printed batch and expiry details.</li><li><b>Fair price:</b> a price far below others usually means old, refilled or fake stock.</li><li><b>Returns:</b> a clear return policy for damaged or wrong items.</li><li><b>Payment:</b> secure online payment or Cash on Delivery, never a request to pay a personal account first.</li></ul>
<h2>Buying here</h2><div class="tbl"><table class="spec"><tbody><tr><td>1 new pink jar</td><td><s>₹2,200</s> <b>%s</b></td></tr><tr><td>2 new pink jars</td><td><s>₹4,400</s> <b>%s</b></td></tr><tr><td>1 old white jar (clearance)</td><td><s>₹999</s> <b>%s</b></td></tr><tr><td>Delivery</td><td>Free across India, 3 to 7 business days</td></tr><tr><td>Payment</td><td>Online (%s off) or Cash on Delivery (+%s)</td></tr><tr><td>Returns</td><td>7 days on sealed packs</td></tr></tbody></table></div>
<p>We are an independent seller, not the brand. Questions before you order? WhatsApp <a href="https://wa.me/%s">%s</a>.</p>
<p><a class="btn" href="/#order">Order now</a></p>''' % (rs(p1), rs(p2), rs(po), rs(OFF), rs(CODF), WA, WA_SHOW),
             faq=[('Is Cream X Emirates available with Cash on Delivery?', 'Yes, here with a %s COD charge, or pay online and save %s.' % (rs(CODF), rs(OFF))),
                  ('How do I know I am getting an original pack?', 'Check that it arrives sealed with printed batch and expiry details. Send us a photo on WhatsApp if anything looks wrong within 48 hours.'),
                  ('Do you deliver all over India?', 'Yes, to most pincodes, with free delivery and tracking.')]),
    ]
