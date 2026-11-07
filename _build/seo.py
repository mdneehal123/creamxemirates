# SEO / AEO / GEO pages for the store. Imported by build.py after its helpers are defined.
# Each guide: answer-first box (for featured snippets and AI answers), short sections, FAQ with FAQPage schema,
# Article + BreadcrumbList schema, a product card with a buy button, and links to related guides.
import html

UPDATED = '2026-11-06'

def guides(P, rs, MRP, PACKS, PRODUCT, SIZE, WA, WA_SHOW, OFF=50, CODF=100, B_CMP={}):
    p1, p2, po = PACKS[0][3], PACKS[1][3], PACKS[2][3]
    G = []

    G.append(dict(slug='cream-x-emirates-price', short='Price',
        title='Cream X Emirates Price in India (30 ml): New Jar, Pack of 2 and Old Jar Offer',
        seo='Cream X Emirates Price in India: 30 ml Jar, Pack of 2, COD',
        desc='Cream X Emirates price in India: %s for one new 30 ml jar, %s for two, and %s for the old white jar while stock lasts. %s off when you pay online; free delivery.' % (rs(p1), rs(p2), rs(po), rs(OFF)),
        answer='One new 30 ml jar of Cream X Emirates (CXE Glow Restoring Face Crème) is <b>%s</b> (MRP ₹2,200), two jars are <b>%s</b>, and the <b>old white jar is %s</b> while stock lasts. Pay online and get <b>%s off</b>; Cash on Delivery has a %s charge. Delivery is free across India.' % (rs(p1), rs(p2), rs(po), rs(OFF), rs(CODF)),
        body='''<h2>Prices</h2><div class="tbl"><table class="spec"><thead><tr><th>Option</th><th>MRP</th><th>Price</th><th>Pay online</th><th>Cash on Delivery</th></tr></thead><tbody>%s</tbody></table></div>
<h2>Old white jar or new pink jar?</h2><p>The brand changed its packaging from a white jar to a pink CXE jar and says the formula is the same. We still have some old white jars, sold at a lower clearance price until they run out. Check the expiry date printed on either pack. Read <a href="/original-cream-x-emirates/">old vs new packaging</a>.</p>
<h2>What is included</h2><ul><li>Sealed 30 ml jar(s), new stock</li><li>Free delivery anywhere we ship in India</li><li>Pay online (UPI, cards, net banking) or Cash on Delivery</li><li>7-day return on sealed, unused packs</li></ul>
<h2>Why prices differ between sellers</h2><p>The MRP printed on the pack is the maximum anyone can charge, and sellers may sell below it. A price far below others is a warning sign: very cheap jars may be expired, refilled or fake. Read <a href="/original-cream-x-emirates/">how to check an original pack</a>.</p>
<h2>How long one jar lasts</h2><p>With the brand's night routine (a small amount, then a thin overnight layer), one 30 ml jar usually lasts around 4 to 6 weeks of nightly use. Visible change takes 8 to 12 weeks, so the pack of 2 is better value if you plan to continue.</p>''' % ''.join('<tr><td>%s</td><td>%s</td><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (l, '<s>%s</s>' % rs(B_CMP.get(i) or 0), rs(p), rs(p - OFF), rs(p + CODF)) for i, l, j, p in PACKS),
        faq=[('What is the price of Cream X Emirates 30 ml?', 'The MRP is ₹2,200. Here it is %s for one new jar, %s for two, or %s for the old white jar while stock lasts.' % (rs(p1), rs(p2), rs(po))),
             ('Is Cash on Delivery available?', 'Yes, with a %s COD charge. Paying online is cheaper: %s off.' % (rs(CODF), rs(OFF))),
             ('Is the old jar the same cream?', 'The brand says the formula is the same; only the packaging changed. Check the expiry date on the pack.')]))

    G.append(dict(slug='how-to-use-cream-x-emirates', short='How to use',
        title='How to Use Cream X Emirates: Night Routine, Step by Step',
        seo='How to Use Cream X Emirates: Step-by-Step Night Routine',
        desc='How to use Cream X Emirates face cream: the brand\'s night routine step by step, how much to apply, patch test, sunscreen, and mistakes to avoid.',
        answer='Use it <b>at night</b>: cleanse and dry your face, <b>massage in a small amount</b> until absorbed, wait <b>about 10 minutes</b>, apply a <b>second thin layer</b> as an overnight mask, and <b>rinse with cold water</b> in the morning. Wear sunscreen every day.',
        body='''<h2>Step by step</h2><ol class="steps"><li><b>Patch test.</b> Apply a little behind the ear or on the jawline and wait 24 hours before the first full use.</li>
<li><b>Cleanse.</b> Wash with a gentle face wash and pat dry. Cream absorbs better on clean, dry skin.</li>
<li><b>First layer.</b> Take a small amount, dot it on the forehead, cheeks, nose and chin, and massage until absorbed. Avoid eyes and lips.</li>
<li><b>Wait 10 minutes.</b> Let the first layer settle.</li>
<li><b>Overnight layer.</b> Spread a second thin layer like a mask and sleep with it.</li>
<li><b>Morning.</b> Rinse with cold water, moisturise if needed, and apply SPF 30+ sunscreen.</li></ol>
<h2>How much to use</h2><p>A small amount, about the size of a pea for each layer, is enough for the face. Using more does not work faster and can feel heavy.</p>
<h2>Mistakes to avoid</h2><ul><li>Skipping sunscreen: new tan keeps forming and hides progress.</li><li>Applying on broken, sunburnt or freshly waxed skin.</li><li>Mixing with other strong creams, peels or bleach on the same night.</li><li>Stopping and starting: results need regular use for 8 to 12 weeks.</li></ul>
<h2>Who should not use it</h2><p>The brand does not recommend it for children under 14, pregnant women or elderly people. Ask a doctor first if you are breastfeeding or have a skin condition.</p>''',
        faq=[('Can I use Cream X Emirates in the daytime?', 'The brand\'s routine is for night use. In the day, wear sunscreen.'),
             ('Should I wash it off in the morning?', 'Yes. Rinse with cold water in the morning, then apply sunscreen.'),
             ('Can I use it every day?', 'The brand recommends daily use. If your skin feels dry or tingly, use it every other night at first.')]))

    G.append(dict(slug='cream-x-emirates-side-effects', short='Side effects',
        title='Cream X Emirates Side Effects: What Is Normal and When to Stop',
        seo='Cream X Emirates Side Effects: Normal Reactions and When to Stop',
        desc='Cream X Emirates side effects: mild reactions some people get with any new face cream, warning signs that mean you should stop, who should not use it, and how to patch test.',
        answer='Most people have <b>no problem or only mild dryness or tingling</b> in the first days, like with any new face cream. <b>Stop and see a doctor</b> if you get burning, swelling, an itchy rash or new dark patches. Always <b>patch test</b> first.',
        body='''<h2>Mild reactions that can happen with any new cream</h2><ul><li>Slight tingling or warmth for a few minutes</li><li>Mild dryness or tightness</li><li>A few small pimples in the first week on oily skin</li></ul><p>These usually settle within 1 to 2 weeks. Use it every other night and add a plain moisturiser if needed.</p>
<h2>Stop using it if you notice</h2><ul><li>Burning that does not fade, redness or swelling</li><li>An itchy rash, hives or small blisters</li><li>New dark or light patches</li><li>Swelling of the lips or eyes, or trouble breathing: get medical help at once</li></ul>
<h2>Who should not use it</h2><p>The brand does not recommend it for <b>children under 14, pregnant women or elderly people</b>. Ask a doctor first if you are breastfeeding, have eczema, rosacea or very sensitive skin, or use prescription skin creams.</p>
<h2>A note on any "whitening" cream</h2><p>Some unbranded fairness creams sold in India and the Gulf have been found to contain steroids or mercury, which can harm the skin with long use. Buy only sealed packs with a full ingredient list, batch number and manufacturer details printed on them. See <a href="/original-cream-x-emirates/">how to check an original pack</a>.</p>
<h2>How to patch test</h2><ol><li>Apply a small amount behind the ear or on the jawline.</li><li>Leave it for 24 hours.</li><li>No redness, itching or swelling? You can start using it on the face.</li></ol>''',
        faq=[('Is Cream X Emirates safe?', 'Most adults can use a face cream like this without problems. Patch test first, follow the directions, and stop if you get burning, swelling or a rash.'),
             ('Can it cause pimples?', 'A few small pimples can appear in the first week on oily skin. If they keep increasing after 2 weeks, stop and see a dermatologist.'),
             ('Can pregnant women use it?', 'No. The brand does not recommend it during pregnancy.')]))

    G.append(dict(slug='cream-x-emirates-review', short='Honest review',
        title='Cream X Emirates Review: What to Know Before You Buy',
        seo='Cream X Emirates Review: Honest Pros, Cons and Results',
        desc='An honest Cream X Emirates review guide: what the cream is for, realistic results and timeline, pros and cons, who it suits, and what to check before buying.',
        answer='Cream X Emirates is a <b>30 ml night face cream</b> for dull skin, tan and uneven tone. Expect <b>softer skin in a few weeks</b> and a <b>more even look over 8 to 12 weeks</b> with daily sunscreen. It does not change your natural skin colour, and results vary.',
        body='''<h2>Quick verdict</h2><div class="grid2"><div class="card"><h3>Good for</h3><ul><li>A simple night routine</li><li>Dull, tired-looking skin</li><li>Tan and uneven patches on the face, with sunscreen</li><li>People who want Cash on Delivery</li></ul></div>
<div class="card"><h3>Think twice if</h3><ul><li>You want instant or overnight results</li><li>You are under 14, pregnant or elderly</li><li>You have very sensitive skin or a skin condition</li><li>You will not wear sunscreen daily</li></ul></div></div>
<h2>Realistic results timeline</h2><ul><li><b>Week 1 to 2:</b> skin feels softer; mild tingling is possible.</li><li><b>Week 3 to 4:</b> fresher, smoother look in the morning.</li><li><b>Week 8 to 12:</b> tan and uneven patches look lighter with daily sunscreen.</li></ul>
<h2>What we check as a seller</h2><p>We sell sealed packs only and check the seal and printed details before dispatch. The full ingredient list, batch number and expiry are printed on the pack; read them before use.</p>
<h2>Customer reviews</h2><p>We publish real reviews from our customers only, with their permission. <a href="/review/">Bought from us? Share your review.</a></p>''',
        faq=[('Does Cream X Emirates really work?', 'It can help skin look brighter and more even over 8 to 12 weeks, especially with daily sunscreen. It will not change your natural skin colour, and results vary from person to person.'),
             ('How many days for results?', 'Softer skin often within 2 to 4 weeks; a more even look over 8 to 12 weeks.'),
             ('Is it good for men?', 'Yes, adults of any gender can use it. Apply at night, not on freshly shaved or nicked skin.')]))

    G.append(dict(slug='original-cream-x-emirates', short='Original vs fake',
        title='Original Cream X Emirates: How to Spot a Fake Pack',
        seo='Original vs Fake Cream X Emirates: How to Check Your Pack',
        desc='How to check if your Cream X Emirates is original: seal, printed batch and expiry, ingredient list, MRP and manufacturer details, texture and smell, and prices that are too low.',
        answer='An original pack is <b>sealed</b>, has a <b>printed batch number, manufacturing and expiry dates, MRP, ingredient list and manufacturer details</b>, and is sold at a sensible price. <b>Do not use</b> a jar that is unsealed, unlabelled or far cheaper than elsewhere.',
        body='''<h2>Old and new packaging</h2><p>The brand has changed the look: the old <b>white jar</b> was replaced by a <b>pink CXE "Glow Restoring Face Crème" jar</b>, 30 ml. The brand says the formula is the same. Both can be genuine while old stock sells out; check the expiry date on either. We sell our remaining old white jars at a lower clearance price.</p><figure><img src="/assets/img/cxe-old-vs-new.jpg" alt="Old white Cream X Emirates jar and new pink CXE jar" width="900" height="1125" loading="lazy" style="width:100%%;height:auto;border-radius:14px"><figcaption class="meta">Old (white) and new (pink) packs. Image from the brand.</figcaption></figure>
<h2>Checklist when your parcel arrives</h2><ol><li><b>Seal:</b> the jar or box should be sealed and untouched.</li><li><b>Printing:</b> batch number, manufacturing date and expiry date are printed clearly, not handwritten or stickered over.</li>
<li><b>Label details:</b> MRP, net quantity (30 ml), full ingredient list and the manufacturer or marketer name and address. Indian rules require these on cosmetics.</li>
<li><b>Price:</b> a price far below other sellers is the most common sign of a fake or old stock.</li><li><b>Texture and smell:</b> if it looks watery, gritty, separated or smells unusual, do not use it.</li></ol>
<h2>Why it matters</h2><p>Fake face creams can contain banned ingredients such as mercury or strong steroids, which can damage the skin. Saving a little money is not worth the risk.</p>
<h2>Our promise</h2><ul><li>Sealed, new stock only</li><li>Unboxing video or photo within 48 hours if anything looks wrong, and we replace or refund</li><li>7-day return on sealed packs</li></ul>
<p>Not sure about a pack? Send a photo on WhatsApp to <a href="https://wa.me/%s">%s</a>.</p>''' % (WA, WA_SHOW),
        faq=[('How do I know my Cream X Emirates is original?', 'Check the seal, printed batch and expiry dates, MRP, ingredient list and manufacturer details, and avoid prices far below other sellers.'),
             ('What should I do if I get a fake?', 'Do not use it. Keep the parcel and contact the seller with photos; report it to the platform or consumer helpline if needed.'),
             ('Do you sell sealed packs?', 'Yes, we sell sealed, new stock only.')]))

    G.append(dict(slug='cream-x-emirates-results', short='Results',
        title='Cream X Emirates Results: How Many Days, and What to Expect',
        seo='Cream X Emirates Results: How Many Days to See a Difference',
        desc='How long Cream X Emirates takes to show results, week by week, what helps results (sunscreen, consistency) and what slows them down.',
        answer='Most people notice <b>softer skin within 2 to 4 weeks</b>, and a <b>brighter, more even look after 8 to 12 weeks</b> of nightly use <b>with daily sunscreen</b>. Faster "7-day" promises are not realistic for any cream.',
        body='''<h2>Week by week</h2><div class="tbl"><table class="spec"><tbody><tr><td>Week 1 to 2</td><td>Skin adjusts; feels softer. Mild tingling possible.</td></tr><tr><td>Week 3 to 4</td><td>Smoother texture, fresher look in the morning.</td></tr><tr><td>Week 5 to 8</td><td>Dullness improves; light tan starts to look lighter.</td></tr><tr><td>Week 8 to 12</td><td>A more even look on tan and uneven patches.</td></tr></tbody></table></div>
<h2>What speeds things up</h2><ul><li>Sunscreen SPF 30+ every morning, reapplied outdoors</li><li>Using it every night, not on and off</li><li>A gentle face wash, not harsh scrubs</li></ul>
<h2>What slows things down</h2><ul><li>Daily sun without protection</li><li>Lemon, bleach or harsh home remedies</li><li>Picking pimples, which leaves marks</li></ul>
<p>Results vary with skin type, the depth of tan and daily sun exposure. A face cream does not change your natural skin colour.</p>''',
        faq=[('Can Cream X Emirates give results in 7 days?', 'Skin can feel softer quickly, but visible change in tan or uneven tone takes 8 to 12 weeks with sunscreen.'),
             ('What happens if I stop using it?', 'Nothing harmful. Without sunscreen, tan can come back over time.'),
             ('Do I need to finish the whole jar?', 'One jar lasts about 4 to 6 weeks; most people need 2 to 3 jars to judge results properly.')]))
    return G


def local_pages(rs, PACKS, MRP):
    p1 = PACKS[0][3]
    return [
        dict(lang='ml', code='ml-IN', path='/ml/cream-x-emirates/', en='/',
             title='Cream X Emirates വില, ഉപയോഗിക്കേണ്ട വിധം | COD',
             desc='Cream X Emirates 30 ml ഫേസ് ക്രീം: വില %s, ഉപയോഗിക്കേണ്ട വിധം, ആർക്ക് ഉപയോഗിക്കരുത്, സൗജന്യ ഡെലിവറി, ക്യാഷ് ഓൺ ഡെലിവറി.' % rs(p1),
             h1='Cream X Emirates ഫേസ് ക്രീം, 30 ml',
             body='''<p class="answer">ഒരു 30 ml ജാറിന് <b>%s</b> . ഇന്ത്യയിലെവിടെയും <b>സൗജന്യ ഡെലിവറി</b>, <b>ക്യാഷ് ഓൺ ഡെലിവറി</b> ലഭ്യമാണ്.</p>
<h2>എങ്ങനെ ഉപയോഗിക്കാം</h2><ol><li>ആദ്യം ചെവിക്ക് പിന്നിൽ 24 മണിക്കൂർ പാച്ച് ടെസ്റ്റ് ചെയ്യുക.</li><li>രാത്രി മുഖം കഴുകി ഉണക്കുക.</li><li>കുറച്ച് ക്രീം എടുത്ത് മുഖത്ത് മസാജ് ചെയ്ത് പിടിക്കുന്നതുവരെ തേക്കുക. കണ്ണിനും ചുണ്ടിനും ചുറ്റും വേണ്ട.</li><li>10 മിനിറ്റിന് ശേഷം ഒരു നേർത്ത പാളി കൂടി മാസ്ക് പോലെ പുരട്ടി രാത്രി മുഴുവൻ വയ്ക്കുക.</li><li>രാവിലെ തണുത്ത വെള്ളത്തിൽ കഴുകി സൺസ്ക്രീൻ പുരട്ടുക.</li></ol>
<h2>ഫലം എപ്പോൾ</h2><p>2–4 ആഴ്ചയിൽ ചർമ്മം മൃദുവാകും. 8–12 ആഴ്ചയിൽ, ദിവസവും സൺസ്ക്രീനോടൊപ്പം, ടാനും അസമമായ നിറവും കുറഞ്ഞതായി തോന്നും. ഫലം ഓരോരുത്തർക്കും വ്യത്യസ്തമാണ്.</p>
<h2>ആർ ഉപയോഗിക്കരുത്</h2><p>14 വയസ്സിൽ താഴെയുള്ള കുട്ടികൾ, ഗർഭിണികൾ, പ്രായമായവർ എന്നിവർക്ക് ബ്രാൻഡ് ശുപാർശ ചെയ്യുന്നില്ല. പൊള്ളൽ, വീക്കം, ചൊറിച്ചിൽ ഉണ്ടായാൽ നിർത്തി ഡോക്ടറെ കാണുക.</p>
<p><a class="btn" href="/#order">ഇപ്പോൾ ഓർഡർ ചെയ്യുക · COD</a></p>''' % rs(p1),
             faq=[('Cream X Emirates വില എത്ര?', 'ഒരു 30 ml ജാറിന് %s, സൗജന്യ ഡെലിവറിയോടെ.' % rs(p1)), ('ക്യാഷ് ഓൺ ഡെലിവറി ഉണ്ടോ?', 'ഉണ്ട്. പാർസൽ കിട്ടുമ്പോൾ പണം നൽകാം.'), ('എത്ര ദിവസത്തിൽ ഫലം കാണും?', '8–12 ആഴ്ച, ദിവസവും സൺസ്ക്രീനോടൊപ്പം.')]),
        dict(lang='hi', code='hi-IN', path='/hi/cream-x-emirates/', en='/',
             title='Cream X Emirates की कीमत, इस्तेमाल का तरीका | COD',
             desc='Cream X Emirates 30 ml फेस क्रीम: कीमत %s, इस्तेमाल का तरीका, किसे नहीं लगानी चाहिए, फ्री डिलीवरी और कैश ऑन डिलीवरी।' % rs(p1),
             h1='Cream X Emirates फेस क्रीम, 30 ml',
             body='''<p class="answer">एक 30 ml जार की कीमत <b>%s</b> । पूरे भारत में <b>फ्री डिलीवरी</b> और <b>कैश ऑन डिलीवरी</b>।</p>
<h2>कैसे इस्तेमाल करें</h2><ol><li>पहले कान के पीछे 24 घंटे पैच टेस्ट करें।</li><li>रात को चेहरा धोकर सुखा लें।</li><li>थोड़ी क्रीम लेकर चेहरे पर मसाज करें जब तक वह समा न जाए। आंखों और होंठों के पास न लगाएं।</li><li>10 मिनट बाद एक पतली परत मास्क की तरह लगाकर रात भर छोड़ दें।</li><li>सुबह ठंडे पानी से धोएं और सनस्क्रीन लगाएं।</li></ol>
<h2>रिज़ल्ट कब दिखेगा</h2><p>2–4 हफ्तों में त्वचा मुलायम लगती है। 8–12 हफ्तों में, रोज़ सनस्क्रीन के साथ, टैन और असमान रंगत हल्की दिखती है। रिज़ल्ट हर व्यक्ति में अलग होता है।</p>
<h2>किसे नहीं लगानी चाहिए</h2><p>ब्रांड 14 साल से कम उम्र के बच्चों, गर्भवती महिलाओं और बुज़ुर्गों के लिए इसकी सलाह नहीं देता। जलन, सूजन या खुजली हो तो बंद करें और डॉक्टर को दिखाएं।</p>
<p><a class="btn" href="/#order">अभी ऑर्डर करें · COD</a></p>''' % rs(p1),
             faq=[('Cream X Emirates की कीमत कितनी है?', 'एक 30 ml जार %s, फ्री डिलीवरी के साथ।' % rs(p1)), ('क्या कैश ऑन डिलीवरी है?', 'हां। पार्सल मिलने पर नकद भुगतान करें।'), ('कितने दिन में रिज़ल्ट दिखेगा?', '8–12 हफ्ते, रोज़ सनस्क्रीन के साथ।')]),
    ]


def build_all(B, sch, title, desc):
    """Write home (with guides + hreflang), guides, local pages, hub, llms.txt, feed, 404. B = build module globals."""
    rs, MRP, PACKS, PRODUCT, SIZE, WA, WA_SHOW, SITE, OWNER, ADDR, JAR = (B[k] for k in ('rs', 'MRP', 'PACKS', 'PRODUCT', 'SIZE', 'WA', 'WA_SHOW', 'SITE', 'OWNER', 'ADDR', 'JAR'))
    layout, write, faq_html, faq_ld, simple, product_body, ROOT, os = (B[k] for k in ('layout', 'write', 'faq_html', 'faq_ld', 'simple', 'product_body', 'ROOT', 'os'))
    G = guides(None, rs, MRP, PACKS, PRODUCT, SIZE, WA, WA_SHOW, B['PREPAID_OFF'], B['COD_FEE'], {k: v['cmp'] for k, v in B['PACK_INFO'].items()})
    L = local_pages(rs, PACKS, MRP)
    import seo2
    G = G + seo2.guides2(rs, PACKS, B['PREPAID_OFF'], B['COD_FEE'], WA, WA_SHOW) + seo2.guides3(rs, PACKS, B['PREPAID_OFF'], B['COD_FEE'], WA, WA_SHOW)
    L = L + seo2.locals2(rs, PACKS)
    p1 = PACKS[0][3]
    short = lambda g: g['title'].split(':')[0]
    glinks = ''.join('<li><a href="/%s/">%s</a></li>' % (g['slug'], html.escape(short(g))) for g in G)
    def cluster(en):
        return ''.join('<link rel="alternate" hreflang="%s" href="%s%s">' % (l['code'], SITE, l['path']) for l in L if l.get('en', '/') == en) + '<link rel="alternate" hreflang="en-IN" href="%s%s"><link rel="alternate" hreflang="x-default" href="%s%s">' % (SITE, en, SITE, en)
    hre = cluster('/')
    sch = sch + [{'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Cream X Emirates online store (independent seller)', 'url': SITE + '/', 'inLanguage': 'en-IN'}]
    write('/', layout('/', title, desc, product_body('h1').replace('@@GUIDES@@', glinks), sch, extra=hre))
    card = '<div class="pcard"><img src="/assets/img/cxe-new-pack.jpg" alt="CXE Glow Restoring Face Crème" width="84" height="84" loading="lazy"><div class="t"><b>%s, %s</b><span class="muted">%s · free delivery · COD</span></div><a class="btn shine" href="/#order">Buy now</a></div>' % (html.escape(PRODUCT), SIZE, rs(p1))
    sticky = '<div class="sticky show"><div class="p"><b>%s</b><small>paying online</small></div><a class="btn" href="/#order">Buy now</a></div>' % rs(p1 - B['PREPAID_OFF'])
    for g in G:
        path = '/%s/' % g['slug']
        rel = ''.join('<li><a href="/%s/">%s</a></li>' % (o['slug'], html.escape(short(o))) for o in G if o is not g)
        body = ('<section class="band" style="border:0"><div class="wrap prose"><p class="crumb"><a href="/">Home</a> › <a href="/guides/">Guides</a> › %s</p><h1>%s</h1>'
                '<p class="meta">Updated %s · General cosmetic guidance, not medical advice.</p><p class="answer">%s</p>%s%s<h2>Questions</h2>%s<h2>More guides</h2><ul class="glist">%s</ul></div></section>%s') % (
            html.escape(g['short']), html.escape(g['title']), UPDATED, g['answer'], card, g['body'], faq_html(g['faq']), rel, sticky)
        sc = [faq_ld(g['faq']),
              {'@context': 'https://schema.org', '@type': 'Article', 'headline': g['title'], 'description': g['desc'], 'datePublished': UPDATED, 'dateModified': UPDATED, 'inLanguage': 'en-IN',
               'mainEntityOfPage': SITE + path, 'about': {'@type': 'Product', 'name': '%s %s' % (PRODUCT, SIZE)}, 'author': {'@type': 'Organization', 'name': OWNER}, 'publisher': {'@type': 'Organization', 'name': OWNER}},
              {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                  {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}, {'@type': 'ListItem', 'position': 2, 'name': 'Guides', 'item': SITE + '/guides/'},
                  {'@type': 'ListItem', 'position': 3, 'name': g['short'], 'item': SITE + path}]}]
        write(path, layout(path, g['seo'], g['desc'], body, sc, extra=cluster(path) if any(l.get('en') == path for l in L) else ''))
    for l in L:
        body = '<section class="band" style="border:0"><div class="wrap prose"><p class="crumb"><a href="/">Home</a> › %s</p><h1>%s</h1>%s%s<h2>FAQ</h2>%s<p class="meta"><a href="%s" lang="en">Read in English</a></p></div></section>%s' % (
            l['lang'].upper(), html.escape(l['h1']), card, l['body'], faq_html(l['faq']), l.get('en', '/'), sticky)
        write(l['path'], layout(l['path'], l['title'], l['desc'], body, [faq_ld(l['faq'])], lang=l['code'], extra=cluster(l.get('en', '/'))))
    simple('/guides/', 'Cream X Emirates Guides: Price, How to Use, Side Effects, Results',
           'All Cream X Emirates guides: price, how to use, side effects, honest review, results timeline and how to spot a fake pack.', 'Guides',
           ('<ul class="glist">%s</ul>' % ''.join('<li><a href="/%s/">%s</a></li>' % (g['slug'], html.escape(g['title'])) for g in G)) + '<h2>Other languages</h2><ul class="glist">' + ''.join('<li><a href="%s" lang="%s">%s</a></li>' % (l['path'], l['lang'], html.escape(l['h1'])) for l in L) + '</ul>')
    more = '; '.join('%s %s' % (lb, rs(p)) for i, lb, j, p in PACKS[1:])
    pages = '\n'.join('- %s: %s/%s/' % (short(g), SITE, g['slug']) for g in G)
    open(os.path.join(ROOT, 'llms.txt'), 'w').write('\n'.join([
        '# Cream X Emirates online store (independent seller)', '',
        '> Independent Indian online store selling sealed Cream X Emirates Glow Restoring Face Crème (30 ml). Run by %s, %s. Not the official brand website.' % (OWNER, ADDR), '',
        '## Product facts',
        '- Product: Cream X Emirates (CXE) Glow Restoring Face Crème, 30 ml jar',
        '- Price: %s for 1 new jar; %s; %s off when paying online; Cash on Delivery has a %s charge' % (rs(p1), more, rs(B['PREPAID_OFF']), rs(B['COD_FEE'])),
        '- Delivery: free across India; Cash on Delivery; packed in 1-2 business days, delivered in 3-7',
        '- Returns: sealed, unused packs within 7 days of delivery',
        '- How to use: at night on a clean face; massage in a small amount; after 10 minutes apply a thin overnight layer; rinse with cold water in the morning; sunscreen daily',
        '- Results: softer skin in 2-4 weeks; more even-looking tone in 8-12 weeks with sunscreen; results vary; does not change natural skin colour',
        '- Not recommended for: children under 14, pregnant women, elderly people (brand guidance)',
        '- Order: WhatsApp %s, or the order form on the home page' % WA_SHOW, '',
        '## Pages', '- Home and order: %s/' % SITE, pages, '- FAQ: %s/faq/' % SITE,
        '- Malayalam: %s/ml/cream-x-emirates/' % SITE, '- Hindi: %s/hi/cream-x-emirates/' % SITE, '']))
    items = ''.join(
        '<item><g:id>CXE-30ML-%s</g:id><title>%s %s, %s</title><description>%s, %s. Night face cream. Free delivery in India, Cash on Delivery.</description><link>%s/</link>'
        '<g:image_link>%s/assets/img/cxe-jars.jpg</g:image_link><g:availability>in_stock</g:availability><g:price>%d.00 INR</g:price>%s'
        '<g:brand>Cream X Emirates</g:brand><g:condition>new</g:condition><g:identifier_exists>no</g:identifier_exists><g:google_product_category>2740</g:google_product_category>'
        '<g:shipping><g:country>IN</g:country><g:price>0 INR</g:price></g:shipping>%s</item>' % (
            i, html.escape(PRODUCT), SIZE, lb, html.escape(PRODUCT), SIZE, SITE, SITE, (B['PACK_INFO'][i]['cmp'] or p), ('<g:sale_price>%d.00 INR</g:sale_price>' % p) if B['PACK_INFO'][i]['cmp'] else '', ('<g:multipack>%d</g:multipack>' % j) if j > 1 else '')
        for i, lb, j, p in PACKS)
    os.makedirs(os.path.join(ROOT, 'feeds'), exist_ok=True)
    open(os.path.join(ROOT, 'feeds/products.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0"><channel><title>Cream X Emirates store</title><link>%s/</link><description>Products</description>%s</channel></rss>\n' % (SITE, items))
    open(os.path.join(ROOT, '404.html'), 'w').write(layout('/404/', 'Page not found', 'This page does not exist.',
        '<section class="band" style="border:0"><div class="wrap prose"><h1>Page not found</h1><p><a href="/">Go to the Cream X Emirates page</a> or <a href="/guides/">read the guides</a>.</p></div></section>', robots='noindex'))
    return ['/guides/'] + ['/%s/' % g['slug'] for g in G] + [l['path'] for l in L]
