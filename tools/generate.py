#!/usr/bin/env python3
"""Regenerate the site's HTML pages from the content below.

Optional convenience only: the committed .html files are what Cloudflare Pages
serves, and they can be edited by hand. If you edit content here instead, run
`python3 tools/generate.py` from the repository root to rewrite the pages.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MAP_QUERY = "Panj+Peer+Mazar+Mashhad-e-Hind+Samana+Punjab"
MAP_EMBED = f"https://maps.google.com/maps?q={MAP_QUERY}&output=embed"
MAP_LINK = f"https://www.google.com/maps/search/?api=1&query={MAP_QUERY}"

# Address the site is served from. Change this when a custom domain is set up.
SITE_URL = "https://mashhad-e-hind-website.pages.dev"
WAQF_URL = "https://waqf.punjab.gov.in/"

PAGES = ["index", "history", "timings", "events", "committee", "contact", "location"]

LANGS = {
    "en": {
        "dir": "ltr", "prefix": "", "label": "English",
        "fonts": "Noto+Serif:wght@400;700",
        "site": "Dargah-e-Aliya Mashhad-e-Hind, Samana",
        "ph": "To be confirmed by the committee",
        "nav": ["Home", "History", "Timings", "Events", "Committee", "Contact", "Location"],
        "authority": "An undertaking of the Punjab Waqf Board",
        "skip": "Skip to content",
        "footer": "Mashhad-e-Hind · Samana, Patiala district, Punjab, India. "
                  "Text marked in yellow is awaiting confirmation by the shrine committee.",
    },
    "hi": {
        "dir": "ltr", "prefix": "hi/", "label": "हिन्दी",
        "fonts": "Noto+Sans+Devanagari:wght@400;700",
        "site": "दरगाह-ए-आलिया मशहद-ए-हिंद, समाना",
        "ph": "कमेटी द्वारा पुष्टि बाकी है",
        "nav": ["मुख्य पृष्ठ", "इतिहास", "समय", "कार्यक्रम", "कमेटी", "संपर्क", "स्थान"],
        "authority": "पंजाब वक़्फ़ बोर्ड के अधीन",
        "skip": "सामग्री पर जाएँ",
        "footer": "मशहद-ए-हिंद · समाना, ज़िला पटियाला, पंजाब, भारत। "
                  "पीले रंग में दिखाए गए लेख की पुष्टि रौज़े की कमेटी द्वारा अभी बाकी है।",
    },
    "pa": {
        "dir": "ltr", "prefix": "pa/", "label": "ਪੰਜਾਬੀ",
        "fonts": "Noto+Sans+Gurmukhi:wght@400;700",
        "site": "ਦਰਗਾਹ-ਏ-ਆਲੀਆ ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ",
        "ph": "ਕਮੇਟੀ ਵੱਲੋਂ ਪੁਸ਼ਟੀ ਬਾਕੀ ਹੈ",
        "nav": ["ਮੁੱਖ ਪੰਨਾ", "ਇਤਿਹਾਸ", "ਸਮਾਂ", "ਸਮਾਗਮ", "ਕਮੇਟੀ", "ਸੰਪਰਕ", "ਟਿਕਾਣਾ"],
        "authority": "ਪੰਜਾਬ ਵਕਫ਼ ਬੋਰਡ ਦੇ ਅਧੀਨ",
        "skip": "ਸਮੱਗਰੀ ਵੱਲ ਜਾਓ",
        "footer": "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ · ਸਮਾਣਾ, ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ, ਭਾਰਤ। "
                  "ਪੀਲੇ ਰੰਗ ਵਿੱਚ ਦਰਸਾਈ ਲਿਖਤ ਦੀ ਪੁਸ਼ਟੀ ਰੌਜ਼ੇ ਦੀ ਕਮੇਟੀ ਵੱਲੋਂ ਹਾਲੇ ਬਾਕੀ ਹੈ।",
    },
    "ur": {
        "dir": "rtl", "prefix": "ur/", "label": "اردو",
        "fonts": "Noto+Nastaliq+Urdu:wght@400;700",
        "site": "درگاہِ عالیہ مشہدِ ہند، سمانہ",
        "ph": "کمیٹی سے تصدیق باقی ہے",
        "nav": ["سرورق", "تاریخ", "اوقات", "تقریبات", "کمیٹی", "رابطہ", "مقام"],
        "authority": "پنجاب وقف بورڈ کے زیرِ انتظام",
        "skip": "مواد پر جائیں",
        "footer": "مشہدِ ہند · سمانہ، ضلع پٹیالہ، پنجاب، بھارت۔ "
                  "پیلے رنگ میں نشان زد عبارت کی تصدیق روضے کی کمیٹی سے ابھی باقی ہے۔",
    },
}


def ph(lang, what):
    """A visible placeholder the committee must replace."""
    return f'<span class="placeholder" title="{LANGS[lang]["ph"]}">[{what}]</span>'


# ---------------------------------------------------------------------------
# Content. Each entry: (page title, meta description, body HTML)
# ---------------------------------------------------------------------------

def content(lang):
    P = lambda w: ph(lang, w)
    if lang == "en":
        return {
            "index": ("Dargah-e-Aliya Mashhad-e-Hind, Samana: official website",
                      "Official website of Mashhad-e-Hind (Mashhad e Hind, Panj Peer Mazar), the shrine of Imamzada Syed Mashhad Ali in Samana, Patiala district, Punjab. History, timings, events, contact and directions.",
                      f"""
<section class="hero">
  <img class="arch" src="assets/arch.svg" alt="">
  <p class="eyebrow">Samana · Patiala district · Punjab</p>
  <h1>Mashhad-e-Hind</h1>
  <p class="lede">The shrine of Imamzada Syed Mashhad Ali, revered as a descendant of Imam Ali al-Rida (peace be upon him).</p>
</section>
<section>
  <h2>Welcome</h2>
  <p>Mashhad-e-Hind (also written Mashhad e Hind or Mashad-e-Hind), known for generations as the Panj Peer Mazar, stands in the old town of Samana in Punjab. It is revered as the resting place of Imamzada Syed Mashhad Ali, of the family of the Holy Prophet Muhammad (peace be upon him and his family). Visitors of many faiths come here to offer their respects and prayers.</p>
  <p>A Persian inscription found at the shrine records that the building was raised in the month of Ramadan, 967 AH, in the fourth year of the reign of Emperor Akbar.</p>
  <p class="notice"><strong>Visiting today:</strong> {P("opening hours")} · <a href="timings.html">See all timings</a></p>
</section>
<section class="cards" aria-label="Sections">
  <a class="card" href="history.html"><h3>History</h3><p>The town of Samana, the shrine and its inscription.</p></a>
  <a class="card" href="timings.html"><h3>Timings</h3><p>When the shrine is open, and prayer times.</p></a>
  <a class="card" href="events.html"><h3>Events</h3><p>Majalis and observances through the year.</p></a>
  <a class="card" href="contact.html"><h3>Contact</h3><p>Reach the shrine committee.</p></a>
  <a class="card" href="location.html"><h3>Location</h3><p>Map and directions to Samana.</p></a>
</section>
"""),
            "history": ("History",
                        "The history of Samana and of Mashhad-e-Hind, the shrine of Imamzada Syed Mashhad Ali.",
                        f"""
<p class="uncertain">This history was compiled from published accounts and local tradition. Where sources disagree, both views are given. The shrine committee is reviewing the wording.</p>

<h2>The town of Samana</h2>
<p>Samana is an old town and municipal council in Patiala district, Punjab, on State Highway 10 between Patiala and Patran. The area is mentioned in accounts of the time of Raja Jaipal, and after the conquests of Muhammad of Ghor it was placed under Qutb ud-Din Aibak in 1192. In the reign of Emperor Akbar, the <em>Ain-i-Akbari</em> lists Samana as a <em>pargana</em> (district) of the Sirhind <em>sarkar</em>.</p>
<p>For centuries Samana was known as a town of saints and scholars, and it was home to many Sayyid families and Shia scholars until 1947. Local tradition holds that the town takes its name from a pious lady named Samana, connected with the family of the Imams; this is a tradition and is not recorded in early sources.</p>

<h2>Imamzada Syed Mashhad Ali</h2>
<p>The shrine is revered as the resting place of Imamzada Syed Mashhad Ali. According to tradition, he came to this region from Mashhad in Khorasan during a time of hardship for the family of the Imams under the Abbasid caliph al-Ma'mun.</p>
<p class="uncertain">Accounts differ on his exact lineage. Some describe him as a son of Imam Ali al-Rida (peace be upon him), some as a later descendant of the Imam, and some as a son of Imam Muhammad al-Taqi (peace be upon him).</p>

<h2>The shrine and its inscription</h2>
<p>For a long time the tomb was known simply as the Panj Peer Mazar. When the shrine complex was being cleaned, at the suggestion of Justice Shabbar Rizvi of the Lahore High Court, whose family had lived in Samana before Partition, a Persian inscription came to light.</p>
<p>As it has been reported, the inscription names the tomb as that of Imam Mashhad Ali and records that the building was raised by Ajruddin Khan Mughal, son of Bakhsh Allah Khan, in the month of Ramadan, 967 AH, in the fourth year of the reign of Emperor Akbar. This corresponds to about 1560 CE; some accounts give 1559.</p>
<p class="uncertain">The reading of the inscription is reported to have been examined by religious scholars, historians and visiting officials. A published scholarly reading has not yet been found.</p>

<h2>Since 1947</h2>
<p>At Partition in 1947 many Sayyid families of Samana left for Pakistan. The shrine remained, and in recent years it has again become a place of visitation for Shia and Sunni Muslims and for Sikh devotees. An annual majlis is held at Mashhad-e-Hind.</p>

<h2>Sources</h2>
<ul class="sources">
  <li>Wikipedia, "Samana, India" (history section, including the Ain-i-Akbari listing).</li>
  <li>mashadehind.in, "About Samana".</li>
  <li>V. S. Gill, "Imami Shrine at Samana: Most Noteworthy and Neglected", Heritage Guru blog, 2014.</li>
  <li>Oral tradition of the Samana community.</li>
</ul>
"""),
            "timings": ("Timings",
                        "Opening hours and prayer times at Mashhad-e-Hind, Samana.",
                        f"""
<p>All times are local (IST). Please check with the committee before travelling for special occasions.</p>
<div class="table-scroll"><table>
  <thead><tr><th>Day</th><th>Opening hours</th></tr></thead>
  <tbody>
    <tr><td>Daily</td><td>6:00 AM – 9:00 PM</td></tr>
    <tr><td>Friday</td><td>Friday prayer at the time of Zuhr</td></tr>
  </tbody>
</table></div>

<h2>Daily prayers</h2>
<p>As per the local Shia prayer timings for Patiala.</p>

<h2>During Muharram and special occasions</h2>
<p>The committee will announce any programme that is scheduled.</p>

<h2>When visiting</h2>
<ul>
  <li>Please dress modestly and cover your head.</li>
  <li>Remove your shoes before entering the shrine.</li>
  <li>Kindly keep silence near the grave and respect those at prayer.</li>
</ul>
"""),
            "events": ("Events",
                       "Majalis and observances at Mashhad-e-Hind, Samana.",
                       f"""
<p>Islamic dates follow the lunar calendar, so the Gregorian dates change every year. The committee will announce exact dates.</p>
<div class="table-scroll"><table>
  <thead><tr><th>Occasion</th><th>Islamic date</th><th>This year</th></tr></thead>
  <tbody>
    <tr><td>Annual majlis (Salana Majlis) at Mashhad-e-Hind</td><td>11–12 Jumada al-Thani 1448 AH</td><td>21–22 November 2026</td></tr>
  </tbody>
</table></div>
<p>Programmes of past majalis may be found on the shrine's social media pages.</p>
"""),
            "contact": ("Contact",
                        "Contact the committee of Mashhad-e-Hind, Samana.",
                        f"""
<p>For visits, events and enquiries, please contact the shrine committee.</p>
<div class="table-scroll"><table>
  <tbody>
    <tr><th>Committee</th><td>{P("name of the managing committee")}</td></tr>
    <tr><th>Phone</th><td>{P("phone number")}</td></tr>
    <tr><th>Email</th><td>–</td></tr>
    <tr><th>Address</th><td>Samana, Patiala district, Punjab 147101, India</td></tr>
  </tbody>
</table></div>
<p>For directions, see the <a href="location.html">location</a> page.</p>
"""),
            "location": ("Location",
                         "How to reach Mashhad-e-Hind in Samana, Patiala district, Punjab.",
                         f"""
<p>Mashhad-e-Hind is in the town of Samana, Patiala district, Punjab. Samana lies on State Highway 10 between Patiala and Patran.</p>
<iframe class="map" src="{MAP_EMBED}" title="Map of Samana" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
<p><a href="{MAP_LINK}" target="_blank" rel="noopener">Open in Google Maps</a> · {P("committee to confirm the exact map pin")}</p>

<h2>Getting here</h2>
<ul>
  <li><strong>By road:</strong> from Patiala, about 27 km south-west on State Highway 10 (approximate).</li>
  <li><strong>By rail:</strong> the nearest major railway station is Patiala.</li>
  <li><strong>By air:</strong> the nearest airport is Chandigarh, about 95 km away (approximate).</li>
  <li>{P("Directions within Samana, landmarks and parking")}</li>
</ul>
"""),
        }

    if lang == "ur":
        return {
            "index": ("درگاہِ عالیہ مشہدِ ہند، سمانہ: سرکاری ویب سائٹ",
                      "مشہدِ ہند (پنج پیر مزار)، امام زادہ سید مشہد علی کا روضہ، سمانہ، ضلع پٹیالہ، پنجاب کی سرکاری ویب سائٹ۔",
                      f"""
<section class="hero">
  <img class="arch" src="../assets/arch.svg" alt="">
  <p class="eyebrow">سمانہ · ضلع پٹیالہ · پنجاب</p>
  <h1>مشہدِ ہند</h1>
  <p class="lede">امام زادہ سید مشہد علی کا روضہ، جنہیں حضرت امام علی رضا علیہ السلام کی اولاد میں سے مانا جاتا ہے۔</p>
</section>
<section>
  <h2>خوش آمدید</h2>
  <p>مشہدِ ہند، جو نسلوں سے پنج پیر مزار کے نام سے جانا جاتا ہے، پنجاب کے قدیم قصبے سمانہ میں واقع ہے۔ اسے امام زادہ سید مشہد علی کی آرام گاہ مانا جاتا ہے، جو حضرت محمد مصطفیٰ صلی اللہ علیہ وآلہ وسلم کے خاندان سے تعلق رکھتے ہیں۔ مختلف مذاہب کے زائرین یہاں عقیدت اور دعا کے لیے حاضر ہوتے ہیں۔</p>
  <p>روضے سے ملنے والے ایک فارسی کتبے کے مطابق اس عمارت کی تعمیر ماہِ رمضان ۹۶۷ ہجری میں، شہنشاہ اکبر کے دورِ حکومت کے چوتھے سال ہوئی۔</p>
  <p class="notice"><strong>آج کی زیارت:</strong> {P("زیارت کے اوقات")} · <a href="timings.html">تمام اوقات دیکھیں</a></p>
</section>
<section class="cards" aria-label="حصے">
  <a class="card" href="history.html"><h3>تاریخ</h3><p>قصبۂ سمانہ، روضہ اور اس کا کتبہ۔</p></a>
  <a class="card" href="timings.html"><h3>اوقات</h3><p>روضہ کب کھلا رہتا ہے، اور نماز کے اوقات۔</p></a>
  <a class="card" href="events.html"><h3>تقریبات</h3><p>سال بھر کی مجالس اور مواقع۔</p></a>
  <a class="card" href="contact.html"><h3>رابطہ</h3><p>روضے کی کمیٹی سے رابطہ۔</p></a>
  <a class="card" href="location.html"><h3>مقام</h3><p>سمانہ کا نقشہ اور راستہ۔</p></a>
</section>
"""),
            "history": ("تاریخ",
                        "سمانہ اور مشہدِ ہند، امام زادہ سید مشہد علی کے روضے کی تاریخ۔",
                        f"""
<p class="uncertain">یہ تاریخ شائع شدہ بیانات اور مقامی روایات سے مرتب کی گئی ہے۔ جہاں ماخذ مختلف ہیں وہاں دونوں آراء درج ہیں۔ روضے کی کمیٹی اس عبارت کا جائزہ لے رہی ہے۔</p>

<h2>قصبۂ سمانہ</h2>
<p>سمانہ ضلع پٹیالہ، پنجاب کا ایک قدیم قصبہ اور میونسپل کونسل ہے، جو پٹیالہ اور پاتڑاں کے درمیان اسٹیٹ ہائی وے ۱۰ پر واقع ہے۔ اس علاقے کا ذکر راجہ جے پال کے زمانے کے بیانات میں ملتا ہے، اور محمد غوری کی فتوحات کے بعد ۱۱۹۲ء میں اسے قطب الدین ایبک کے سپرد کیا گیا۔ شہنشاہ اکبر کے دور میں <em>آئینِ اکبری</em> میں سمانہ کو سرکارِ سرہند کا ایک پرگنہ درج کیا گیا ہے۔</p>
<p>صدیوں تک سمانہ اولیا اور علما کے قصبے کے طور پر جانا جاتا رہا، اور ۱۹۴۷ء تک یہاں بہت سے سادات خاندان اور شیعہ علما آباد تھے۔ مقامی روایت کے مطابق اس قصبے کا نام ایک پرہیزگار خاتون، سمانہ، کے نام پر ہے جن کا تعلق ائمہ کے خاندان سے بتایا جاتا ہے؛ یہ ایک روایت ہے اور قدیم ماخذ میں درج نہیں۔</p>

<h2>امام زادہ سید مشہد علی</h2>
<p>یہ روضہ امام زادہ سید مشہد علی کی آرام گاہ مانا جاتا ہے۔ روایت کے مطابق وہ عباسی خلیفہ مامون کے دور میں، جب خاندانِ ائمہ پر سختی کا زمانہ تھا، خراسان کے شہر مشہد سے اس علاقے میں تشریف لائے۔</p>
<p class="uncertain">ان کے نسب کے بارے میں روایات مختلف ہیں۔ بعض انہیں حضرت امام علی رضا علیہ السلام کا فرزند، بعض امام کی بعد کی نسل سے، اور بعض حضرت امام محمد تقی علیہ السلام کا فرزند بیان کرتے ہیں۔</p>

<h2>روضہ اور اس کا کتبہ</h2>
<p>ایک عرصے تک یہ مزار صرف پنج پیر مزار کے نام سے جانا جاتا تھا۔ لاہور ہائی کورٹ کے جسٹس شبر رضوی کی تجویز پر، جن کا خاندان تقسیم سے پہلے سمانہ میں آباد تھا، جب روضے کے احاطے کی صفائی کی گئی تو ایک فارسی کتبہ سامنے آیا۔</p>
<p>بیان کے مطابق اس کتبے میں اس مزار کو امام مشہد علی کا مزار کہا گیا ہے اور درج ہے کہ یہ عمارت اجرالدین خان مغل ولد بخش اللہ خان نے ماہِ رمضان ۹۶۷ ہجری میں، شہنشاہ اکبر کے دورِ حکومت کے چوتھے سال تعمیر کروائی۔ یہ تقریباً ۱۵۶۰ء بنتا ہے؛ بعض بیانات میں ۱۵۵۹ء درج ہے۔</p>
<p class="uncertain">بیان کیا جاتا ہے کہ اس کتبے کی قرأت کا جائزہ علمائے دین، مؤرخین اور آنے والے حکام نے لیا۔ اس کی کوئی شائع شدہ علمی قرأت ابھی تک نہیں ملی۔</p>

<h2>۱۹۴۷ء کے بعد</h2>
<p>۱۹۴۷ء میں تقسیم کے وقت سمانہ کے بہت سے سادات خاندان پاکستان چلے گئے۔ روضہ اپنی جگہ قائم رہا، اور حالیہ برسوں میں یہ پھر سے شیعہ اور سنی مسلمانوں اور سکھ عقیدت مندوں کے لیے زیارت گاہ بن گیا ہے۔ مشہدِ ہند میں ہر سال ایک سالانہ مجلس منعقد ہوتی ہے۔</p>

<h2>ماخذ</h2>
<ul class="sources">
  <li>ویکیپیڈیا، "Samana, India" (تاریخ کا حصہ، بشمول آئینِ اکبری کا اندراج)۔</li>
  <li>mashadehind.in، "About Samana"۔</li>
  <li>وی ایس گل، "Imami Shrine at Samana: Most Noteworthy and Neglected"، ہیریٹیج گرو بلاگ، ۲۰۱۴ء۔</li>
  <li>اہلِ سمانہ کی زبانی روایات۔</li>
</ul>
"""),
            "timings": ("اوقات",
                        "مشہدِ ہند، سمانہ میں زیارت اور نماز کے اوقات۔",
                        f"""
<p>تمام اوقات مقامی (بھارتی معیاری وقت) ہیں۔ خاص مواقع پر سفر سے پہلے کمیٹی سے تصدیق کر لیں۔</p>
<div class="table-scroll"><table>
  <thead><tr><th>دن</th><th>زیارت کے اوقات</th></tr></thead>
  <tbody>
    <tr><td>روزانہ</td><td>صبح ۶ بجے سے رات ۹ بجے تک</td></tr>
    <tr><td>جمعہ</td><td>نمازِ جمعہ ظہر کے وقت</td></tr>
  </tbody>
</table></div>

<h2>روزانہ نمازیں</h2>
<p>پٹیالہ کے مقامی شیعہ اوقاتِ نماز کے مطابق۔</p>

<h2>محرم اور خاص مواقع</h2>
<p>کوئی پروگرام طے ہونے پر کمیٹی اس کا اعلان کرے گی۔</p>

<h2>زیارت کے آداب</h2>
<ul>
  <li>براہِ کرم باوقار لباس پہنیں اور سر ڈھانپیں۔</li>
  <li>روضے میں داخل ہونے سے پہلے جوتے اتار دیں۔</li>
  <li>مزار کے قریب خاموشی رکھیں اور نماز پڑھنے والوں کا احترام کریں۔</li>
</ul>
"""),
            "events": ("تقریبات",
                       "مشہدِ ہند، سمانہ میں مجالس اور مواقع۔",
                       f"""
<p>اسلامی تاریخیں قمری تقویم کے مطابق ہوتی ہیں، اس لیے عیسوی تاریخیں ہر سال بدلتی ہیں۔ کمیٹی صحیح تاریخوں کا اعلان کرے گی۔</p>
<div class="table-scroll"><table>
  <thead><tr><th>موقع</th><th>اسلامی تاریخ</th><th>اس سال</th></tr></thead>
  <tbody>
    <tr><td>مشہدِ ہند کی سالانہ مجلس</td><td>۱۱–۱۲ جمادی الثانی ۱۴۴۸ھ</td><td>۲۱–۲۲ نومبر ۲۰۲۶ء</td></tr>
  </tbody>
</table></div>
<p>گزشتہ مجالس کے پروگرام روضے کے سوشل میڈیا صفحات پر دیکھے جا سکتے ہیں۔</p>
"""),
            "contact": ("رابطہ",
                        "مشہدِ ہند، سمانہ کی کمیٹی سے رابطہ۔",
                        f"""
<p>زیارت، تقریبات اور معلومات کے لیے براہِ کرم روضے کی کمیٹی سے رابطہ کریں۔</p>
<div class="table-scroll"><table>
  <tbody>
    <tr><th>کمیٹی</th><td>{P("انتظامی کمیٹی کا نام")}</td></tr>
    <tr><th>فون</th><td>{P("فون نمبر")}</td></tr>
    <tr><th>ای میل</th><td>–</td></tr>
    <tr><th>پتہ</th><td>سمانہ، ضلع پٹیالہ، پنجاب <bdi dir="ltr">147101</bdi>، بھارت</td></tr>
  </tbody>
</table></div>
<p>راستے کے لیے <a href="location.html">مقام</a> کا صفحہ دیکھیں۔</p>
"""),
            "location": ("مقام",
                         "سمانہ، ضلع پٹیالہ، پنجاب میں مشہدِ ہند تک کیسے پہنچیں۔",
                         f"""
<p>مشہدِ ہند ضلع پٹیالہ، پنجاب کے قصبے سمانہ میں واقع ہے۔ سمانہ پٹیالہ اور پاتڑاں کے درمیان اسٹیٹ ہائی وے ۱۰ پر ہے۔</p>
<iframe class="map" src="{MAP_EMBED}" title="سمانہ کا نقشہ" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
<p><a href="{MAP_LINK}" target="_blank" rel="noopener">گوگل میپس میں کھولیں</a> · {P("کمیٹی نقشے پر صحیح مقام کی تصدیق کرے")}</p>

<h2>یہاں کیسے پہنچیں</h2>
<ul>
  <li><strong>سڑک کے راستے:</strong> پٹیالہ سے تقریباً ۲۷ کلومیٹر جنوب مغرب میں، اسٹیٹ ہائی وے ۱۰ پر (اندازاً)۔</li>
  <li><strong>ریل کے ذریعے:</strong> قریب ترین بڑا ریلوے اسٹیشن پٹیالہ ہے۔</li>
  <li><strong>ہوائی سفر:</strong> قریب ترین ہوائی اڈہ چندی گڑھ ہے، تقریباً ۹۵ کلومیٹر دور (اندازاً)۔</li>
  <li>{P("سمانہ کے اندر راستہ، نمایاں مقامات اور پارکنگ")}</li>
</ul>
"""),
        }

    if lang == "hi":
        return {
            "index": ("दरगाह-ए-आलिया मशहद-ए-हिंद, समाना: आधिकारिक वेबसाइट",
                      "मशहद-ए-हिंद (पंज पीर मज़ार), इमामज़ादा सैयद मशहद अली की दरगाह, समाना, ज़िला पटियाला, पंजाब की आधिकारिक वेबसाइट।",
                      f"""
<section class="hero">
  <img class="arch" src="../assets/arch.svg" alt="">
  <p class="eyebrow">समाना · ज़िला पटियाला · पंजाब</p>
  <h1>मशहद-ए-हिंद</h1>
  <p class="lede">इमामज़ादा सैयद मशहद अली का रौज़ा, जिन्हें हज़रत इमाम अली रज़ा (अलैहिस्सलाम) की औलाद में से माना जाता है।</p>
</section>
<section>
  <h2>स्वागत है</h2>
  <p>मशहद-ए-हिंद, जिसे पीढ़ियों से पंज पीर मज़ार के नाम से जाना जाता है, पंजाब के प्राचीन क़स्बे समाना में स्थित है। इसे इमामज़ादा सैयद मशहद अली की आरामगाह माना जाता है, जो हज़रत मुहम्मद साहब (सल्लल्लाहु अलैहि व आलिही व सल्लम) के ख़ानदान से संबंध रखते हैं। विभिन्न धर्मों के श्रद्धालु यहाँ श्रद्धा और दुआ के लिए आते हैं।</p>
  <p>रौज़े से मिले एक फ़ारसी शिलालेख के अनुसार इस इमारत का निर्माण रमज़ान के महीने, 967 हिजरी में, बादशाह अकबर के शासन के चौथे वर्ष में हुआ।</p>
  <p class="notice"><strong>आज की ज़ियारत:</strong> {P("खुलने का समय")} · <a href="timings.html">सभी समय देखें</a></p>
</section>
<section class="cards" aria-label="भाग">
  <a class="card" href="history.html"><h3>इतिहास</h3><p>समाना क़स्बा, रौज़ा और उसका शिलालेख।</p></a>
  <a class="card" href="timings.html"><h3>समय</h3><p>रौज़ा कब खुला रहता है, और नमाज़ के समय।</p></a>
  <a class="card" href="events.html"><h3>कार्यक्रम</h3><p>साल भर की मजलिसें और अवसर।</p></a>
  <a class="card" href="contact.html"><h3>संपर्क</h3><p>रौज़े की कमेटी से संपर्क।</p></a>
  <a class="card" href="location.html"><h3>स्थान</h3><p>समाना का नक्शा और रास्ता।</p></a>
</section>
"""),
            "history": ("इतिहास",
                        "समाना और मशहद-ए-हिंद, इमामज़ादा सैयद मशहद अली के रौज़े का इतिहास।",
                        f"""
<p class="uncertain">यह इतिहास प्रकाशित विवरणों और स्थानीय परंपराओं से तैयार किया गया है। जहाँ स्रोत अलग-अलग हैं, वहाँ दोनों मत दिए गए हैं। रौज़े की कमेटी इस लेख की समीक्षा कर रही है।</p>

<h2>समाना क़स्बा</h2>
<p>समाना ज़िला पटियाला, पंजाब का एक प्राचीन क़स्बा और नगर परिषद है, जो पटियाला और पातड़ां के बीच स्टेट हाईवे 10 पर स्थित है। इस क्षेत्र का उल्लेख राजा जयपाल के समय के विवरणों में मिलता है, और मुहम्मद ग़ोरी की विजयों के बाद 1192 में इसे क़ुतुबुद्दीन ऐबक को सौंपा गया। बादशाह अकबर के समय <em>आईन-ए-अकबरी</em> में समाना को सरहिंद सरकार का एक परगना दर्ज किया गया है।</p>
<p>सदियों तक समाना संतों और विद्वानों के क़स्बे के रूप में जाना जाता रहा, और 1947 तक यहाँ कई सैयद परिवार और शिया विद्वान बसे हुए थे। स्थानीय परंपरा के अनुसार क़स्बे का नाम समाना नाम की एक नेक बीबी के नाम पर है, जिनका संबंध इमामों के ख़ानदान से बताया जाता है; यह एक परंपरा है और पुराने स्रोतों में दर्ज नहीं है।</p>

<h2>इमामज़ादा सैयद मशहद अली</h2>
<p>यह रौज़ा इमामज़ादा सैयद मशहद अली की आरामगाह माना जाता है। परंपरा के अनुसार वे अब्बासी ख़लीफ़ा मामून के समय, जब इमामों के ख़ानदान पर कठिन समय था, ख़ुरासान के शहर मशहद से इस क्षेत्र में आए।</p>
<p class="uncertain">उनकी वंशावली के बारे में विवरण अलग-अलग हैं। कुछ उन्हें हज़रत इमाम अली रज़ा (अलैहिस्सलाम) का पुत्र, कुछ इमाम की बाद की पीढ़ी से, और कुछ हज़रत इमाम मुहम्मद तक़ी (अलैहिस्सलाम) का पुत्र बताते हैं।</p>

<h2>रौज़ा और उसका शिलालेख</h2>
<p>लंबे समय तक यह मज़ार केवल पंज पीर मज़ार के नाम से जाना जाता था। लाहौर हाई कोर्ट के जस्टिस शब्बर रिज़वी के सुझाव पर, जिनका परिवार विभाजन से पहले समाना में बसा था, जब रौज़े के अहाते की सफ़ाई की गई तो एक फ़ारसी शिलालेख सामने आया।</p>
<p>बताए अनुसार इस शिलालेख में इस मज़ार को इमाम मशहद अली का मज़ार कहा गया है और दर्ज है कि यह इमारत अजरुद्दीन ख़ान मुग़ल, पुत्र बख़्श अल्लाह ख़ान, ने रमज़ान के महीने 967 हिजरी में, बादशाह अकबर के शासन के चौथे वर्ष में बनवाई। यह लगभग 1560 ई. बनता है; कुछ विवरणों में 1559 दर्ज है।</p>
<p class="uncertain">बताया जाता है कि इस शिलालेख के पाठ की जाँच धार्मिक विद्वानों, इतिहासकारों और आए हुए अधिकारियों ने की। इसका कोई प्रकाशित विद्वत्तापूर्ण पाठ अभी तक नहीं मिला है।</p>

<h2>1947 के बाद</h2>
<p>1947 के विभाजन के समय समाना के कई सैयद परिवार पाकिस्तान चले गए। रौज़ा अपनी जगह क़ायम रहा, और हाल के वर्षों में यह फिर से शिया और सुन्नी मुसलमानों और सिख श्रद्धालुओं के लिए ज़ियारतगाह बन गया है। मशहद-ए-हिंद में हर साल एक सालाना मजलिस होती है।</p>

<h2>स्रोत</h2>
<ul class="sources">
  <li>विकिपीडिया, "Samana, India" (इतिहास भाग, आईन-ए-अकबरी की प्रविष्टि सहित)।</li>
  <li>mashadehind.in, "About Samana"।</li>
  <li>वी. एस. गिल, "Imami Shrine at Samana: Most Noteworthy and Neglected", हेरिटेज गुरु ब्लॉग, 2014।</li>
  <li>समाना वासियों की मौखिक परंपराएँ।</li>
</ul>
"""),
            "timings": ("समय",
                        "मशहद-ए-हिंद, समाना में ज़ियारत और नमाज़ के समय।",
                        f"""
<p>सभी समय स्थानीय (भारतीय मानक समय) हैं। विशेष अवसरों पर आने से पहले कमेटी से पुष्टि कर लें।</p>
<div class="table-scroll"><table>
  <thead><tr><th>दिन</th><th>खुलने का समय</th></tr></thead>
  <tbody>
    <tr><td>प्रतिदिन</td><td>सुबह 6 बजे से रात 9 बजे तक</td></tr>
    <tr><td>शुक्रवार</td><td>जुमे की नमाज़ ज़ुहर के समय</td></tr>
  </tbody>
</table></div>

<h2>रोज़ाना नमाज़</h2>
<p>पटियाला के स्थानीय शिया नमाज़ समय के अनुसार।</p>

<h2>मुहर्रम और विशेष अवसर</h2>
<p>कोई कार्यक्रम तय होने पर कमेटी उसकी घोषणा करेगी।</p>

<h2>ज़ियारत के आदाब</h2>
<ul>
  <li>कृपया सादे और मर्यादित वस्त्र पहनें और सिर ढकें।</li>
  <li>रौज़े में प्रवेश करने से पहले जूते उतार दें।</li>
  <li>मज़ार के पास शांति रखें और नमाज़ पढ़ने वालों का सम्मान करें।</li>
</ul>
"""),
            "events": ("कार्यक्रम",
                       "मशहद-ए-हिंद, समाना में मजलिसें और अवसर।",
                       f"""
<p>इस्लामी तारीख़ें चंद्र कैलेंडर के अनुसार होती हैं, इसलिए अंग्रेज़ी तारीख़ें हर साल बदलती हैं। कमेटी सही तारीख़ों की घोषणा करेगी।</p>
<div class="table-scroll"><table>
  <thead><tr><th>अवसर</th><th>इस्लामी तारीख़</th><th>इस वर्ष</th></tr></thead>
  <tbody>
    <tr><td>मशहद-ए-हिंद की सालाना मजलिस</td><td>11–12 जमादी-उस-सानी 1448 हिजरी</td><td>21–22 नवंबर 2026</td></tr>
  </tbody>
</table></div>
<p>पिछली मजलिसों के कार्यक्रम रौज़े के सोशल मीडिया पेजों पर देखे जा सकते हैं।</p>
"""),
            "contact": ("संपर्क",
                        "मशहद-ए-हिंद, समाना की कमेटी से संपर्क।",
                        f"""
<p>ज़ियारत, कार्यक्रमों और जानकारी के लिए कृपया रौज़े की कमेटी से संपर्क करें।</p>
<div class="table-scroll"><table>
  <tbody>
    <tr><th>कमेटी</th><td>{P("प्रबंधक कमेटी का नाम")}</td></tr>
    <tr><th>फ़ोन</th><td>{P("फ़ोन नंबर")}</td></tr>
    <tr><th>ईमेल</th><td>–</td></tr>
    <tr><th>पता</th><td>समाना, ज़िला पटियाला, पंजाब 147101, भारत</td></tr>
  </tbody>
</table></div>
<p>रास्ते के लिए <a href="location.html">स्थान</a> पेज देखें।</p>
"""),
            "location": ("स्थान",
                         "समाना, ज़िला पटियाला, पंजाब में मशहद-ए-हिंद तक कैसे पहुँचें।",
                         f"""
<p>मशहद-ए-हिंद ज़िला पटियाला, पंजाब के क़स्बे समाना में स्थित है। समाना पटियाला और पातड़ां के बीच स्टेट हाईवे 10 पर है।</p>
<iframe class="map" src="{MAP_EMBED}" title="समाना का नक्शा" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
<p><a href="{MAP_LINK}" target="_blank" rel="noopener">गूगल मैप्स में खोलें</a> · {P("कमेटी नक्शे पर सही स्थान की पुष्टि करे")}</p>

<h2>यहाँ कैसे पहुँचें</h2>
<ul>
  <li><strong>सड़क से:</strong> पटियाला से लगभग 27 किलोमीटर दक्षिण-पश्चिम में, स्टेट हाईवे 10 पर (अनुमानित)।</li>
  <li><strong>रेल से:</strong> सबसे नज़दीकी बड़ा रेलवे स्टेशन पटियाला है।</li>
  <li><strong>हवाई मार्ग से:</strong> सबसे नज़दीकी हवाई अड्डा चंडीगढ़ है, लगभग 95 किलोमीटर दूर (अनुमानित)।</li>
  <li>{P("समाना के अंदर रास्ता, पहचान के स्थान और पार्किंग")}</li>
</ul>
"""),
        }

    if lang == "pa":
        return {
            "index": ("ਦਰਗਾਹ-ਏ-ਆਲੀਆ ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ: ਅਧਿਕਾਰਤ ਵੈੱਬਸਾਈਟ",
                      "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ (ਪੰਜ ਪੀਰ ਮਜ਼ਾਰ), ਇਮਾਮਜ਼ਾਦਾ ਸੱਯਦ ਮਸ਼ਹਦ ਅਲੀ ਦਾ ਰੌਜ਼ਾ, ਸਮਾਣਾ, ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ ਦੀ ਅਧਿਕਾਰਤ ਵੈੱਬਸਾਈਟ।",
                      f"""
<section class="hero">
  <img class="arch" src="../assets/arch.svg" alt="">
  <p class="eyebrow">ਸਮਾਣਾ · ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ · ਪੰਜਾਬ</p>
  <h1>ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ</h1>
  <p class="lede">ਇਮਾਮਜ਼ਾਦਾ ਸੱਯਦ ਮਸ਼ਹਦ ਅਲੀ ਦਾ ਰੌਜ਼ਾ, ਜਿਨ੍ਹਾਂ ਨੂੰ ਹਜ਼ਰਤ ਇਮਾਮ ਅਲੀ ਰਜ਼ਾ (ਅਲੈਹਿਸ-ਸਲਾਮ) ਦੀ ਔਲਾਦ ਵਿੱਚੋਂ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ।</p>
</section>
<section>
  <h2>ਜੀ ਆਇਆਂ ਨੂੰ</h2>
  <p>ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਜਿਸ ਨੂੰ ਪੀੜ੍ਹੀਆਂ ਤੋਂ ਪੰਜ ਪੀਰ ਮਜ਼ਾਰ ਦੇ ਨਾਂ ਨਾਲ ਜਾਣਿਆ ਜਾਂਦਾ ਹੈ, ਪੰਜਾਬ ਦੇ ਪੁਰਾਣੇ ਸ਼ਹਿਰ ਸਮਾਣਾ ਵਿੱਚ ਸਥਿਤ ਹੈ। ਇਸ ਨੂੰ ਇਮਾਮਜ਼ਾਦਾ ਸੱਯਦ ਮਸ਼ਹਦ ਅਲੀ ਦੀ ਆਰਾਮਗਾਹ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ, ਜੋ ਹਜ਼ਰਤ ਮੁਹੰਮਦ ਸਾਹਿਬ (ਸੱਲੱਲਾਹੁ ਅਲੈਹਿ ਵ ਆਲਿਹੀ ਵ ਸੱਲਮ) ਦੇ ਖ਼ਾਨਦਾਨ ਨਾਲ ਸੰਬੰਧ ਰੱਖਦੇ ਹਨ। ਵੱਖ-ਵੱਖ ਧਰਮਾਂ ਦੇ ਸ਼ਰਧਾਲੂ ਇੱਥੇ ਸ਼ਰਧਾ ਅਤੇ ਦੁਆ ਲਈ ਆਉਂਦੇ ਹਨ।</p>
  <p>ਰੌਜ਼ੇ ਤੋਂ ਮਿਲੇ ਇੱਕ ਫ਼ਾਰਸੀ ਸ਼ਿਲਾਲੇਖ ਅਨੁਸਾਰ ਇਸ ਇਮਾਰਤ ਦੀ ਉਸਾਰੀ ਰਮਜ਼ਾਨ ਦੇ ਮਹੀਨੇ, 967 ਹਿਜਰੀ ਵਿੱਚ, ਬਾਦਸ਼ਾਹ ਅਕਬਰ ਦੇ ਰਾਜ ਦੇ ਚੌਥੇ ਸਾਲ ਹੋਈ।</p>
  <p class="notice"><strong>ਅੱਜ ਦੀ ਜ਼ਿਆਰਤ:</strong> {P("ਖੁੱਲ੍ਹਣ ਦਾ ਸਮਾਂ")} · <a href="timings.html">ਸਾਰੇ ਸਮੇਂ ਵੇਖੋ</a></p>
</section>
<section class="cards" aria-label="ਭਾਗ">
  <a class="card" href="history.html"><h3>ਇਤਿਹਾਸ</h3><p>ਸਮਾਣਾ ਸ਼ਹਿਰ, ਰੌਜ਼ਾ ਅਤੇ ਇਸ ਦਾ ਸ਼ਿਲਾਲੇਖ।</p></a>
  <a class="card" href="timings.html"><h3>ਸਮਾਂ</h3><p>ਰੌਜ਼ਾ ਕਦੋਂ ਖੁੱਲ੍ਹਾ ਰਹਿੰਦਾ ਹੈ, ਅਤੇ ਨਮਾਜ਼ ਦੇ ਸਮੇਂ।</p></a>
  <a class="card" href="events.html"><h3>ਸਮਾਗਮ</h3><p>ਸਾਲ ਭਰ ਦੀਆਂ ਮਜਲਿਸਾਂ ਅਤੇ ਮੌਕੇ।</p></a>
  <a class="card" href="contact.html"><h3>ਸੰਪਰਕ</h3><p>ਰੌਜ਼ੇ ਦੀ ਕਮੇਟੀ ਨਾਲ ਸੰਪਰਕ।</p></a>
  <a class="card" href="location.html"><h3>ਟਿਕਾਣਾ</h3><p>ਸਮਾਣਾ ਦਾ ਨਕਸ਼ਾ ਅਤੇ ਰਸਤਾ।</p></a>
</section>
"""),
            "history": ("ਇਤਿਹਾਸ",
                        "ਸਮਾਣਾ ਅਤੇ ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਇਮਾਮਜ਼ਾਦਾ ਸੱਯਦ ਮਸ਼ਹਦ ਅਲੀ ਦੇ ਰੌਜ਼ੇ ਦਾ ਇਤਿਹਾਸ।",
                        f"""
<p class="uncertain">ਇਹ ਇਤਿਹਾਸ ਛਪੇ ਹੋਏ ਬਿਰਤਾਂਤਾਂ ਅਤੇ ਸਥਾਨਕ ਰਵਾਇਤਾਂ ਤੋਂ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਿੱਥੇ ਸਰੋਤ ਵੱਖਰੇ ਹਨ, ਉੱਥੇ ਦੋਵੇਂ ਵਿਚਾਰ ਦਿੱਤੇ ਗਏ ਹਨ। ਰੌਜ਼ੇ ਦੀ ਕਮੇਟੀ ਇਸ ਲਿਖਤ ਦੀ ਸਮੀਖਿਆ ਕਰ ਰਹੀ ਹੈ।</p>

<h2>ਸਮਾਣਾ ਸ਼ਹਿਰ</h2>
<p>ਸਮਾਣਾ ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ ਦਾ ਇੱਕ ਪੁਰਾਣਾ ਸ਼ਹਿਰ ਅਤੇ ਨਗਰ ਕੌਂਸਲ ਹੈ, ਜੋ ਪਟਿਆਲਾ ਅਤੇ ਪਾਤੜਾਂ ਦੇ ਵਿਚਕਾਰ ਸਟੇਟ ਹਾਈਵੇ 10 ਉੱਤੇ ਸਥਿਤ ਹੈ। ਇਸ ਇਲਾਕੇ ਦਾ ਜ਼ਿਕਰ ਰਾਜਾ ਜੈਪਾਲ ਦੇ ਸਮੇਂ ਦੇ ਬਿਰਤਾਂਤਾਂ ਵਿੱਚ ਮਿਲਦਾ ਹੈ, ਅਤੇ ਮੁਹੰਮਦ ਗ਼ੌਰੀ ਦੀਆਂ ਜਿੱਤਾਂ ਤੋਂ ਬਾਅਦ 1192 ਵਿੱਚ ਇਸ ਨੂੰ ਕੁਤਬੁੱਦੀਨ ਐਬਕ ਦੇ ਹਵਾਲੇ ਕੀਤਾ ਗਿਆ। ਬਾਦਸ਼ਾਹ ਅਕਬਰ ਦੇ ਸਮੇਂ <em>ਆਈਨ-ਏ-ਅਕਬਰੀ</em> ਵਿੱਚ ਸਮਾਣਾ ਨੂੰ ਸਰਹਿੰਦ ਸਰਕਾਰ ਦਾ ਇੱਕ ਪਰਗਣਾ ਦਰਜ ਕੀਤਾ ਗਿਆ ਹੈ।</p>
<p>ਸਦੀਆਂ ਤੱਕ ਸਮਾਣਾ ਸੰਤਾਂ ਅਤੇ ਵਿਦਵਾਨਾਂ ਦੇ ਸ਼ਹਿਰ ਵਜੋਂ ਜਾਣਿਆ ਜਾਂਦਾ ਰਿਹਾ, ਅਤੇ 1947 ਤੱਕ ਇੱਥੇ ਬਹੁਤ ਸਾਰੇ ਸੱਯਦ ਪਰਿਵਾਰ ਅਤੇ ਸ਼ੀਆ ਵਿਦਵਾਨ ਵੱਸਦੇ ਸਨ। ਸਥਾਨਕ ਰਵਾਇਤ ਅਨੁਸਾਰ ਸ਼ਹਿਰ ਦਾ ਨਾਂ ਸਮਾਣਾ ਨਾਂ ਦੀ ਇੱਕ ਨੇਕ ਬੀਬੀ ਦੇ ਨਾਂ ਉੱਤੇ ਹੈ, ਜਿਨ੍ਹਾਂ ਦਾ ਸੰਬੰਧ ਇਮਾਮਾਂ ਦੇ ਖ਼ਾਨਦਾਨ ਨਾਲ ਦੱਸਿਆ ਜਾਂਦਾ ਹੈ; ਇਹ ਇੱਕ ਰਵਾਇਤ ਹੈ ਅਤੇ ਪੁਰਾਣੇ ਸਰੋਤਾਂ ਵਿੱਚ ਦਰਜ ਨਹੀਂ।</p>

<h2>ਇਮਾਮਜ਼ਾਦਾ ਸੱਯਦ ਮਸ਼ਹਦ ਅਲੀ</h2>
<p>ਇਹ ਰੌਜ਼ਾ ਇਮਾਮਜ਼ਾਦਾ ਸੱਯਦ ਮਸ਼ਹਦ ਅਲੀ ਦੀ ਆਰਾਮਗਾਹ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ। ਰਵਾਇਤ ਅਨੁਸਾਰ ਉਹ ਅੱਬਾਸੀ ਖ਼ਲੀਫ਼ਾ ਮਾਮੂਨ ਦੇ ਸਮੇਂ, ਜਦੋਂ ਇਮਾਮਾਂ ਦੇ ਖ਼ਾਨਦਾਨ ਉੱਤੇ ਔਖਾ ਸਮਾਂ ਸੀ, ਖ਼ੁਰਾਸਾਨ ਦੇ ਸ਼ਹਿਰ ਮਸ਼ਹਦ ਤੋਂ ਇਸ ਇਲਾਕੇ ਵਿੱਚ ਆਏ।</p>
<p class="uncertain">ਉਨ੍ਹਾਂ ਦੀ ਵੰਸ਼ਾਵਲੀ ਬਾਰੇ ਬਿਰਤਾਂਤ ਵੱਖਰੇ ਹਨ। ਕੁਝ ਉਨ੍ਹਾਂ ਨੂੰ ਹਜ਼ਰਤ ਇਮਾਮ ਅਲੀ ਰਜ਼ਾ (ਅਲੈਹਿਸ-ਸਲਾਮ) ਦੇ ਪੁੱਤਰ, ਕੁਝ ਇਮਾਮ ਦੀ ਬਾਅਦ ਦੀ ਪੀੜ੍ਹੀ ਵਿੱਚੋਂ, ਅਤੇ ਕੁਝ ਹਜ਼ਰਤ ਇਮਾਮ ਮੁਹੰਮਦ ਤਕੀ (ਅਲੈਹਿਸ-ਸਲਾਮ) ਦੇ ਪੁੱਤਰ ਦੱਸਦੇ ਹਨ।</p>

<h2>ਰੌਜ਼ਾ ਅਤੇ ਇਸ ਦਾ ਸ਼ਿਲਾਲੇਖ</h2>
<p>ਲੰਮੇ ਸਮੇਂ ਤੱਕ ਇਹ ਮਜ਼ਾਰ ਸਿਰਫ਼ ਪੰਜ ਪੀਰ ਮਜ਼ਾਰ ਦੇ ਨਾਂ ਨਾਲ ਜਾਣਿਆ ਜਾਂਦਾ ਸੀ। ਲਾਹੌਰ ਹਾਈ ਕੋਰਟ ਦੇ ਜਸਟਿਸ ਸ਼ੱਬਰ ਰਿਜ਼ਵੀ ਦੇ ਸੁਝਾਅ ਉੱਤੇ, ਜਿਨ੍ਹਾਂ ਦਾ ਪਰਿਵਾਰ ਵੰਡ ਤੋਂ ਪਹਿਲਾਂ ਸਮਾਣਾ ਵਿੱਚ ਵੱਸਦਾ ਸੀ, ਜਦੋਂ ਰੌਜ਼ੇ ਦੇ ਅਹਾਤੇ ਦੀ ਸਫ਼ਾਈ ਕੀਤੀ ਗਈ ਤਾਂ ਇੱਕ ਫ਼ਾਰਸੀ ਸ਼ਿਲਾਲੇਖ ਸਾਹਮਣੇ ਆਇਆ।</p>
<p>ਦੱਸੇ ਅਨੁਸਾਰ ਇਸ ਸ਼ਿਲਾਲੇਖ ਵਿੱਚ ਇਸ ਮਜ਼ਾਰ ਨੂੰ ਇਮਾਮ ਮਸ਼ਹਦ ਅਲੀ ਦਾ ਮਜ਼ਾਰ ਕਿਹਾ ਗਿਆ ਹੈ ਅਤੇ ਦਰਜ ਹੈ ਕਿ ਇਹ ਇਮਾਰਤ ਅਜਰੁੱਦੀਨ ਖ਼ਾਨ ਮੁਗ਼ਲ, ਪੁੱਤਰ ਬਖ਼ਸ਼ ਅੱਲਾਹ ਖ਼ਾਨ, ਨੇ ਰਮਜ਼ਾਨ ਦੇ ਮਹੀਨੇ 967 ਹਿਜਰੀ ਵਿੱਚ, ਬਾਦਸ਼ਾਹ ਅਕਬਰ ਦੇ ਰਾਜ ਦੇ ਚੌਥੇ ਸਾਲ ਬਣਵਾਈ। ਇਹ ਲਗਭਗ 1560 ਈ. ਬਣਦਾ ਹੈ; ਕੁਝ ਬਿਰਤਾਂਤਾਂ ਵਿੱਚ 1559 ਦਰਜ ਹੈ।</p>
<p class="uncertain">ਦੱਸਿਆ ਜਾਂਦਾ ਹੈ ਕਿ ਇਸ ਸ਼ਿਲਾਲੇਖ ਦੀ ਪੜ੍ਹਤ ਦੀ ਜਾਂਚ ਧਾਰਮਿਕ ਵਿਦਵਾਨਾਂ, ਇਤਿਹਾਸਕਾਰਾਂ ਅਤੇ ਆਏ ਅਧਿਕਾਰੀਆਂ ਨੇ ਕੀਤੀ। ਇਸ ਦੀ ਕੋਈ ਛਪੀ ਹੋਈ ਵਿਦਵਤਾਪੂਰਨ ਪੜ੍ਹਤ ਹਾਲੇ ਨਹੀਂ ਮਿਲੀ।</p>

<h2>1947 ਤੋਂ ਬਾਅਦ</h2>
<p>1947 ਦੀ ਵੰਡ ਵੇਲੇ ਸਮਾਣਾ ਦੇ ਬਹੁਤ ਸਾਰੇ ਸੱਯਦ ਪਰਿਵਾਰ ਪਾਕਿਸਤਾਨ ਚਲੇ ਗਏ। ਰੌਜ਼ਾ ਆਪਣੀ ਥਾਂ ਕਾਇਮ ਰਿਹਾ, ਅਤੇ ਹਾਲ ਦੇ ਸਾਲਾਂ ਵਿੱਚ ਇਹ ਮੁੜ ਸ਼ੀਆ ਅਤੇ ਸੁੰਨੀ ਮੁਸਲਮਾਨਾਂ ਅਤੇ ਸਿੱਖ ਸ਼ਰਧਾਲੂਆਂ ਲਈ ਜ਼ਿਆਰਤਗਾਹ ਬਣ ਗਿਆ ਹੈ। ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ ਵਿੱਚ ਹਰ ਸਾਲ ਇੱਕ ਸਾਲਾਨਾ ਮਜਲਿਸ ਹੁੰਦੀ ਹੈ।</p>

<h2>ਸਰੋਤ</h2>
<ul class="sources">
  <li>ਵਿਕੀਪੀਡੀਆ, "Samana, India" (ਇਤਿਹਾਸ ਭਾਗ, ਆਈਨ-ਏ-ਅਕਬਰੀ ਦੇ ਇੰਦਰਾਜ ਸਮੇਤ)।</li>
  <li>mashadehind.in, "About Samana"।</li>
  <li>ਵੀ. ਐੱਸ. ਗਿੱਲ, "Imami Shrine at Samana: Most Noteworthy and Neglected", ਹੈਰੀਟੇਜ ਗੁਰੂ ਬਲੌਗ, 2014।</li>
  <li>ਸਮਾਣਾ ਵਾਸੀਆਂ ਦੀਆਂ ਜ਼ੁਬਾਨੀ ਰਵਾਇਤਾਂ।</li>
</ul>
"""),
            "timings": ("ਸਮਾਂ",
                        "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ ਵਿਖੇ ਜ਼ਿਆਰਤ ਅਤੇ ਨਮਾਜ਼ ਦੇ ਸਮੇਂ।",
                        f"""
<p>ਸਾਰੇ ਸਮੇਂ ਸਥਾਨਕ (ਭਾਰਤੀ ਮਿਆਰੀ ਸਮਾਂ) ਹਨ। ਖ਼ਾਸ ਮੌਕਿਆਂ ਉੱਤੇ ਆਉਣ ਤੋਂ ਪਹਿਲਾਂ ਕਮੇਟੀ ਤੋਂ ਪੁਸ਼ਟੀ ਕਰ ਲਓ।</p>
<div class="table-scroll"><table>
  <thead><tr><th>ਦਿਨ</th><th>ਖੁੱਲ੍ਹਣ ਦਾ ਸਮਾਂ</th></tr></thead>
  <tbody>
    <tr><td>ਰੋਜ਼ਾਨਾ</td><td>ਸਵੇਰੇ 6 ਵਜੇ ਤੋਂ ਰਾਤ 9 ਵਜੇ ਤੱਕ</td></tr>
    <tr><td>ਸ਼ੁੱਕਰਵਾਰ</td><td>ਜੁਮੇ ਦੀ ਨਮਾਜ਼ ਜ਼ੁਹਰ ਦੇ ਵੇਲੇ</td></tr>
  </tbody>
</table></div>

<h2>ਰੋਜ਼ਾਨਾ ਨਮਾਜ਼</h2>
<p>ਪਟਿਆਲਾ ਦੇ ਸਥਾਨਕ ਸ਼ੀਆ ਨਮਾਜ਼ ਸਮਿਆਂ ਅਨੁਸਾਰ।</p>

<h2>ਮੁਹੱਰਮ ਅਤੇ ਖ਼ਾਸ ਮੌਕੇ</h2>
<p>ਕੋਈ ਪ੍ਰੋਗਰਾਮ ਤੈਅ ਹੋਣ ਉੱਤੇ ਕਮੇਟੀ ਉਸ ਦਾ ਐਲਾਨ ਕਰੇਗੀ।</p>

<h2>ਜ਼ਿਆਰਤ ਦੇ ਅਦਬ</h2>
<ul>
  <li>ਕਿਰਪਾ ਕਰਕੇ ਸਾਦਾ ਅਤੇ ਮਰਿਆਦਾ ਵਾਲਾ ਪਹਿਰਾਵਾ ਪਾਓ ਅਤੇ ਸਿਰ ਢੱਕੋ।</li>
  <li>ਰੌਜ਼ੇ ਵਿੱਚ ਦਾਖ਼ਲ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਜੁੱਤੀਆਂ ਉਤਾਰ ਦਿਓ।</li>
  <li>ਮਜ਼ਾਰ ਦੇ ਨੇੜੇ ਚੁੱਪ ਰੱਖੋ ਅਤੇ ਨਮਾਜ਼ ਪੜ੍ਹਨ ਵਾਲਿਆਂ ਦਾ ਸਤਿਕਾਰ ਕਰੋ।</li>
</ul>
"""),
            "events": ("ਸਮਾਗਮ",
                       "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ ਵਿਖੇ ਮਜਲਿਸਾਂ ਅਤੇ ਮੌਕੇ।",
                       f"""
<p>ਇਸਲਾਮੀ ਤਰੀਕਾਂ ਚੰਦਰ ਕੈਲੰਡਰ ਅਨੁਸਾਰ ਹੁੰਦੀਆਂ ਹਨ, ਇਸ ਲਈ ਅੰਗਰੇਜ਼ੀ ਤਰੀਕਾਂ ਹਰ ਸਾਲ ਬਦਲਦੀਆਂ ਹਨ। ਕਮੇਟੀ ਸਹੀ ਤਰੀਕਾਂ ਦਾ ਐਲਾਨ ਕਰੇਗੀ।</p>
<div class="table-scroll"><table>
  <thead><tr><th>ਮੌਕਾ</th><th>ਇਸਲਾਮੀ ਤਰੀਕ</th><th>ਇਸ ਸਾਲ</th></tr></thead>
  <tbody>
    <tr><td>ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ ਦੀ ਸਾਲਾਨਾ ਮਜਲਿਸ</td><td>11–12 ਜਮਾਦੀ-ਉਸ-ਸਾਨੀ 1448 ਹਿਜਰੀ</td><td>21–22 ਨਵੰਬਰ 2026</td></tr>
  </tbody>
</table></div>
<p>ਪਿਛਲੀਆਂ ਮਜਲਿਸਾਂ ਦੇ ਪ੍ਰੋਗਰਾਮ ਰੌਜ਼ੇ ਦੇ ਸੋਸ਼ਲ ਮੀਡੀਆ ਪੰਨਿਆਂ ਉੱਤੇ ਵੇਖੇ ਜਾ ਸਕਦੇ ਹਨ।</p>
"""),
            "contact": ("ਸੰਪਰਕ",
                        "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ ਦੀ ਕਮੇਟੀ ਨਾਲ ਸੰਪਰਕ।",
                        f"""
<p>ਜ਼ਿਆਰਤ, ਸਮਾਗਮਾਂ ਅਤੇ ਜਾਣਕਾਰੀ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਰੌਜ਼ੇ ਦੀ ਕਮੇਟੀ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।</p>
<div class="table-scroll"><table>
  <tbody>
    <tr><th>ਕਮੇਟੀ</th><td>{P("ਪ੍ਰਬੰਧਕ ਕਮੇਟੀ ਦਾ ਨਾਂ")}</td></tr>
    <tr><th>ਫ਼ੋਨ</th><td>{P("ਫ਼ੋਨ ਨੰਬਰ")}</td></tr>
    <tr><th>ਈਮੇਲ</th><td>–</td></tr>
    <tr><th>ਪਤਾ</th><td>ਸਮਾਣਾ, ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ 147101, ਭਾਰਤ</td></tr>
  </tbody>
</table></div>
<p>ਰਸਤੇ ਲਈ <a href="location.html">ਟਿਕਾਣਾ</a> ਪੰਨਾ ਵੇਖੋ।</p>
"""),
            "location": ("ਟਿਕਾਣਾ",
                         "ਸਮਾਣਾ, ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ ਵਿੱਚ ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ ਤੱਕ ਕਿਵੇਂ ਪਹੁੰਚੀਏ।",
                         f"""
<p>ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ ਦੇ ਸ਼ਹਿਰ ਸਮਾਣਾ ਵਿੱਚ ਸਥਿਤ ਹੈ। ਸਮਾਣਾ ਪਟਿਆਲਾ ਅਤੇ ਪਾਤੜਾਂ ਦੇ ਵਿਚਕਾਰ ਸਟੇਟ ਹਾਈਵੇ 10 ਉੱਤੇ ਹੈ।</p>
<iframe class="map" src="{MAP_EMBED}" title="ਸਮਾਣਾ ਦਾ ਨਕਸ਼ਾ" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
<p><a href="{MAP_LINK}" target="_blank" rel="noopener">ਗੂਗਲ ਮੈਪਸ ਵਿੱਚ ਖੋਲ੍ਹੋ</a> · {P("ਕਮੇਟੀ ਨਕਸ਼ੇ ਉੱਤੇ ਸਹੀ ਥਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੇ")}</p>

<h2>ਇੱਥੇ ਕਿਵੇਂ ਪਹੁੰਚੀਏ</h2>
<ul>
  <li><strong>ਸੜਕ ਰਾਹੀਂ:</strong> ਪਟਿਆਲਾ ਤੋਂ ਲਗਭਗ 27 ਕਿਲੋਮੀਟਰ ਦੱਖਣ-ਪੱਛਮ ਵੱਲ, ਸਟੇਟ ਹਾਈਵੇ 10 ਉੱਤੇ (ਅੰਦਾਜ਼ਨ)।</li>
  <li><strong>ਰੇਲ ਰਾਹੀਂ:</strong> ਸਭ ਤੋਂ ਨੇੜਲਾ ਵੱਡਾ ਰੇਲਵੇ ਸਟੇਸ਼ਨ ਪਟਿਆਲਾ ਹੈ।</li>
  <li><strong>ਹਵਾਈ ਰਾਹੀਂ:</strong> ਸਭ ਤੋਂ ਨੇੜਲਾ ਹਵਾਈ ਅੱਡਾ ਚੰਡੀਗੜ੍ਹ ਹੈ, ਲਗਭਗ 95 ਕਿਲੋਮੀਟਰ ਦੂਰ (ਅੰਦਾਜ਼ਨ)।</li>
  <li>{P("ਸਮਾਣਾ ਦੇ ਅੰਦਰ ਰਸਤਾ, ਨਿਸ਼ਾਨੀਆਂ ਅਤੇ ਪਾਰਕਿੰਗ")}</li>
</ul>
"""),
        }
    raise KeyError(lang)


# ---------------------------------------------------------------------------
# Home page: News and Message from the Chairman. Newest news item first.
# ---------------------------------------------------------------------------

HOME_TEXT = {
    "en": {
        "news": "News",
        "message": "Message from the Chairman",
        "video_fallback": "Your browser cannot play this video.",
        "chairman": "Adv. Zaigam Abbas, Chairman, Dargah-e-Aliya Mashhad-e-Hind, Samana",
    },
    "hi": {
        "news": "समाचार",
        "message": "चेयरमैन का संदेश",
        "video_fallback": "आपका ब्राउज़र यह वीडियो नहीं चला सकता।",
        "chairman": "एडवोकेट ज़ैग़म अब्बास, चेयरमैन, दरगाह-ए-आलिया मशहद-ए-हिंद, समाना",
    },
    "pa": {
        "news": "ਖ਼ਬਰਾਂ",
        "message": "ਚੇਅਰਮੈਨ ਦਾ ਸੁਨੇਹਾ",
        "video_fallback": "ਤੁਹਾਡਾ ਬ੍ਰਾਊਜ਼ਰ ਇਹ ਵੀਡੀਓ ਨਹੀਂ ਚਲਾ ਸਕਦਾ।",
        "chairman": "ਐਡਵੋਕੇਟ ਜ਼ੈਗ਼ਮ ਅੱਬਾਸ, ਚੇਅਰਮੈਨ, ਦਰਗਾਹ-ਏ-ਆਲੀਆ ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ",
    },
    "ur": {
        "news": "خبریں",
        "message": "چیئرمین کا پیغام",
        "video_fallback": "آپ کا براؤزر یہ ویڈیو نہیں چلا سکتا۔",
        "chairman": "ایڈووکیٹ ضیغم عباس، چیئرمین، درگاہِ عالیہ مشہدِ ہند، سمانہ",
    },
}

NEWS = [
    {
        "images": ["assets/news/majalis-2026-poster.jpg", "assets/news/majalis-2026-banner.jpg"],
        "en": ("Salana Majalis, Juloos-e-Aza wa Mehfil",
               "21 and 22 November 2026, Samana, Punjab. All devotees of the Ahl al-Bayt are humbly requested to attend."),
        "hi": ("सालाना मजालिस, जुलूस-ए-अज़ा व महफ़िल",
               "21 और 22 नवंबर 2026, समाना, पंजाब। तमाम आशिक़ान-ए-अहलेबैत से शिरकत की गुज़ारिश है।"),
        "pa": ("ਸਾਲਾਨਾ ਮਜਾਲਿਸ, ਜਲੂਸ-ਏ-ਅਜ਼ਾ ਵ ਮਹਿਫ਼ਲ",
               "21 ਅਤੇ 22 ਨਵੰਬਰ 2026, ਸਮਾਣਾ, ਪੰਜਾਬ। ਸਾਰੇ ਆਸ਼ਿਕਾਨ-ਏ-ਅਹਿਲੇਬੈਤ ਨੂੰ ਸ਼ਿਰਕਤ ਦੀ ਗੁਜ਼ਾਰਿਸ਼ ਹੈ।"),
        "ur": ("سالانہ مجالس، جلوسِ عزا و محفل",
               "۲۱ اور ۲۲ نومبر ۲۰۲۶ء، سمانہ، پنجاب۔ تمام عاشقانِ اہلِ بیت سے شرکت کی گزارش ہے۔"),
    },
]


def home_sections(lang):
    T = HOME_TEXT[lang]
    up = "../" if LANGS[lang]["prefix"] else ""
    items = []
    for item in NEWS:
        heading, text = item[lang]
        pics = "".join(
            f'<a href="{up}{img}" target="_blank" rel="noopener"><img src="{up}{img}" alt="{heading}" loading="lazy"></a>'
            for img in item["images"]
        )
        items.append(f'<article class="news-item"><div class="news-pics">{pics}</div>'
                     f'<div><h3>{heading}</h3><p>{text}</p></div></article>')
    return f"""<section class="news">
  <h2>{T['news']}</h2>
  {"".join(items)}
</section>
<section class="message">
  <h2>{T['message']}</h2>
  <figure>
    <video controls preload="none" playsinline poster="{up}assets/media/chairman-message.jpg">
      <source src="{up}assets/media/chairman-message.mp4" type="video/mp4">
      {T['video_fallback']}
    </video>
    <figcaption>{T['chairman']}</figcaption>
  </figure>
</section>
"""


# Interface text used by the page shell, home hero and footer.
UI = {
    "en": {"cta_visit": "Plan your visit", "cta_history": "Read the history",
           "hours": "Opening hours", "hours_link": "Daily 6 AM – 9 PM",
           "next": "Next event", "next_text": "Annual majlis · 21–22 November 2026",
           "where": "Location", "where_text": "Samana, Patiala district, Punjab",
           "photo_alt": "Mashhad-e-Hind shrine, Samana", "quick": "Quick links",
           "country": "Samana, Patiala district, Punjab, India"},
    "hi": {"cta_visit": "ज़ियारत की योजना बनाएँ", "cta_history": "इतिहास पढ़ें",
           "hours": "खुलने का समय", "hours_link": "प्रतिदिन सुबह 6 से रात 9 बजे",
           "next": "अगला कार्यक्रम", "next_text": "सालाना मजलिस · 21–22 नवंबर 2026",
           "where": "स्थान", "where_text": "समाना, ज़िला पटियाला, पंजाब",
           "photo_alt": "मशहद-ए-हिंद का रौज़ा, समाना", "quick": "त्वरित लिंक",
           "country": "समाना, ज़िला पटियाला, पंजाब, भारत"},
    "pa": {"cta_visit": "ਜ਼ਿਆਰਤ ਦੀ ਯੋਜਨਾ ਬਣਾਓ", "cta_history": "ਇਤਿਹਾਸ ਪੜ੍ਹੋ",
           "hours": "ਖੁੱਲ੍ਹਣ ਦਾ ਸਮਾਂ", "hours_link": "ਰੋਜ਼ਾਨਾ ਸਵੇਰੇ 6 ਤੋਂ ਰਾਤ 9 ਵਜੇ",
           "next": "ਅਗਲਾ ਸਮਾਗਮ", "next_text": "ਸਾਲਾਨਾ ਮਜਲਿਸ · 21–22 ਨਵੰਬਰ 2026",
           "where": "ਟਿਕਾਣਾ", "where_text": "ਸਮਾਣਾ, ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ",
           "photo_alt": "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ ਦਾ ਰੌਜ਼ਾ, ਸਮਾਣਾ", "quick": "ਤੁਰੰਤ ਲਿੰਕ",
           "country": "ਸਮਾਣਾ, ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ, ਭਾਰਤ"},
    "ur": {"cta_visit": "زیارت کا منصوبہ بنائیں", "cta_history": "تاریخ پڑھیں",
           "hours": "زیارت کے اوقات", "hours_link": "روزانہ صبح ۶ سے رات ۹ بجے",
           "next": "اگلی تقریب", "next_text": "سالانہ مجلس · ۲۱–۲۲ نومبر ۲۰۲۶ء",
           "where": "مقام", "where_text": "سمانہ، ضلع پٹیالہ، پنجاب",
           "photo_alt": "مشہدِ ہند کا روضہ، سمانہ", "quick": "فوری روابط",
           "country": "سمانہ، ضلع پٹیالہ، پنجاب، بھارت"},
}

BISMILLAH = "بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"


def home_hero(lang, body):
    """Turn the home page's hero section into the full-width banner and info strip."""
    import re
    U = UI[lang]
    up = "../" if LANGS[lang]["prefix"] else ""
    m = re.search(r'<section class="hero">(.*?)</section>', body, re.S)
    inner = re.sub(r'\s*<img class="arch"[^>]*>', "", m.group(1)).strip()
    hero = f"""<section class="hero">
  <div class="wrap hero-inner">
    <div class="hero-text">
      <p class="bismillah" lang="ar" dir="rtl">{BISMILLAH}</p>
      {inner}
      <div class="cta"><a class="btn btn-gold" href="location.html">{U['cta_visit']}</a><a class="btn btn-ghost" href="history.html">{U['cta_history']}</a></div>
    </div>
    <figure class="hero-photo"><img src="{up}assets/media/shrine.jpg" alt="{U['photo_alt']}" width="372" height="296"></figure>
  </div>
</section>
<section class="info-strip" aria-label="{U['hours']}">
  <div class="wrap info-grid">
    <a class="info" href="timings.html"><span class="info-label">{U['hours']}</span><span class="info-value">{U['hours_link']}</span></a>
    <a class="info" href="events.html"><span class="info-label">{U['next']}</span><span class="info-value">{U['next_text']}</span></a>
    <a class="info" href="location.html"><span class="info-label">{U['where']}</span><span class="info-value">{U['where_text']}</span></a>
  </div>
</section>
"""
    body = body[:m.start()] + body[m.end():]
    body = re.sub(r'\s*<p class="notice">.*?</p>', "", body, count=1, flags=re.S)
    body = body.replace("<section>", '<section class="welcome">', 1)
    return hero, body


# ---------------------------------------------------------------------------
# Managing committee, shown on the Committee page and the Contact page.
# ---------------------------------------------------------------------------

COMMITTEE = [
    {"photo": "assets/committee/zaigam-abbas.jpg", "phone": "+919779097254", "phone_text": "97790 97254",
     "en": ("Adv. Zaigam Abbas", "Chairman"), "hi": ("एडवोकेट ज़ैग़म अब्बास", "चेयरमैन"),
     "pa": ("ਐਡਵੋਕੇਟ ਜ਼ੈਗ਼ਮ ਅੱਬਾਸ", "ਚੇਅਰਮੈਨ"), "ur": ("ایڈووکیٹ ضیغم عباس", "چیئرمین")},
    {"photo": "assets/committee/naseem-haider.jpg", "phone": "+918146887031", "phone_text": "81468 87031",
     "en": ("Naseem Haider", "President"), "hi": ("नसीम हैदर", "अध्यक्ष"),
     "pa": ("ਨਸੀਮ ਹੈਦਰ", "ਪ੍ਰਧਾਨ"), "ur": ("نسیم حیدر", "صدر")},
    {"photo": "assets/committee/shabbir-hussain.jpg", "phone": "+919876160462", "phone_text": "98761 60462",
     "en": ("Shabbir Hussain", "General Secretary"), "hi": ("शब्बीर हुसैन", "महासचिव"),
     "pa": ("ਸ਼ੱਬੀਰ ਹੁਸੈਨ", "ਜਨਰਲ ਸਕੱਤਰ"), "ur": ("شبیر حسین", "جنرل سیکرٹری")},
]

ABOUT = {
    "en": ("Committee", "The managing committee of Dargah-e-Aliya Mashhad-e-Hind, Samana, with phone numbers.",
           "The Dargah",
           "Dargah-e-Aliya Mashhad-e-Hind in Samana is the shrine of Imamzada Syed Mashhad Ali. It is an undertaking of the {waqf} and is managed by the committee below.",
           "Punjab Waqf Board", "Managing committee",
           "For visits, events and enquiries, please call a member of the committee or see the {contact} page.",
           "Managing committee of Dargah-e-Aliya Mashhad-e-Hind"),
    "hi": ("कमेटी", "दरगाह-ए-आलिया मशहद-ए-हिंद, समाना की प्रबंधक कमेटी और फ़ोन नंबर।",
           "दरगाह",
           "समाना में दरगाह-ए-आलिया मशहद-ए-हिंद इमामज़ादा सैयद मशहद अली का रौज़ा है। यह {waqf} का उपक्रम है और इसका प्रबंध नीचे दी गई कमेटी करती है।",
           "पंजाब वक़्फ़ बोर्ड", "प्रबंधक कमेटी",
           "ज़ियारत, कार्यक्रमों और जानकारी के लिए कृपया कमेटी के किसी सदस्य को फ़ोन करें या {contact} पेज देखें।",
           "दरगाह-ए-आलिया मशहद-ए-हिंद की प्रबंधक कमेटी"),
    "pa": ("ਕਮੇਟੀ", "ਦਰਗਾਹ-ਏ-ਆਲੀਆ ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ ਦੀ ਪ੍ਰਬੰਧਕ ਕਮੇਟੀ ਅਤੇ ਫ਼ੋਨ ਨੰਬਰ।",
           "ਦਰਗਾਹ",
           "ਸਮਾਣਾ ਵਿੱਚ ਦਰਗਾਹ-ਏ-ਆਲੀਆ ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ ਇਮਾਮਜ਼ਾਦਾ ਸੱਯਦ ਮਸ਼ਹਦ ਅਲੀ ਦਾ ਰੌਜ਼ਾ ਹੈ। ਇਹ {waqf} ਦੇ ਅਧੀਨ ਹੈ ਅਤੇ ਇਸ ਦਾ ਪ੍ਰਬੰਧ ਹੇਠਾਂ ਦਿੱਤੀ ਕਮੇਟੀ ਕਰਦੀ ਹੈ।",
           "ਪੰਜਾਬ ਵਕਫ਼ ਬੋਰਡ", "ਪ੍ਰਬੰਧਕ ਕਮੇਟੀ",
           "ਜ਼ਿਆਰਤ, ਸਮਾਗਮਾਂ ਅਤੇ ਜਾਣਕਾਰੀ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਕਮੇਟੀ ਦੇ ਕਿਸੇ ਮੈਂਬਰ ਨੂੰ ਫ਼ੋਨ ਕਰੋ ਜਾਂ {contact} ਪੰਨਾ ਵੇਖੋ।",
           "ਦਰਗਾਹ-ਏ-ਆਲੀਆ ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ ਦੀ ਪ੍ਰਬੰਧਕ ਕਮੇਟੀ"),
    "ur": ("کمیٹی", "درگاہِ عالیہ مشہدِ ہند، سمانہ کی انتظامی کمیٹی اور فون نمبر۔",
           "درگاہ",
           "سمانہ میں درگاہِ عالیہ مشہدِ ہند امام زادہ سید مشہد علی کا روضہ ہے۔ یہ {waqf} کے زیرِ انتظام ہے اور اس کا انتظام نیچے دی گئی کمیٹی کرتی ہے۔",
           "پنجاب وقف بورڈ", "انتظامی کمیٹی",
           "زیارت، تقریبات اور معلومات کے لیے براہِ کرم کمیٹی کے کسی رکن کو فون کریں یا {contact} کا صفحہ دیکھیں۔",
           "درگاہِ عالیہ مشہدِ ہند کی انتظامی کمیٹی"),
}


def phone_link(member):
    return f'<a href="tel:{member["phone"]}"><bdi dir="ltr">{member["phone_text"]}</bdi></a>'


def committee_page(lang):
    title, desc, h_dargah, intro, waqf, h_committee, outro, _ = ABOUT[lang]
    up = "../" if LANGS[lang]["prefix"] else ""
    contact_label = dict(zip(PAGES, LANGS[lang]["nav"]))["contact"]
    cards = "".join(
        f'<article class="member"><img src="{up}{m["photo"]}" alt="{m[lang][0]}" width="158" height="200" loading="lazy">'
        f'<h3>{m[lang][0]}</h3><p class="role">{m[lang][1]}</p><p class="phone">{phone_link(m)}</p></article>'
        for m in COMMITTEE
    )
    body = f"""
<h2>{h_dargah}</h2>
<p>{intro.format(waqf=f'<a href="{WAQF_URL}" target="_blank" rel="noopener">{waqf}</a>')}</p>
<h2>{h_committee}</h2>
<div class="committee">{cards}</div>
<p>{outro.format(contact=f'<a href="contact.html">{contact_label}</a>')}</p>
"""
    return title, desc, body


def contact_committee(lang, body):
    """Fill the Contact page's committee and phone rows from COMMITTEE."""
    committee_ph = {"en": "name of the managing committee", "hi": "प्रबंधक कमेटी का नाम",
                    "pa": "ਪ੍ਰਬੰਧਕ ਕਮੇਟੀ ਦਾ ਨਾਂ", "ur": "انتظامی کمیٹی کا نام"}[lang]
    phone_ph = {"en": "phone number", "hi": "फ़ोन नंबर", "pa": "ਫ਼ੋਨ ਨੰਬਰ", "ur": "فون نمبر"}[lang]
    committee_label = dict(zip(PAGES, LANGS[lang]["nav"]))["committee"]
    phones = "<br>".join(f"{m[lang][0]} ({m[lang][1]}): {phone_link(m)}" for m in COMMITTEE)
    body = body.replace(ph(lang, committee_ph), f'{ABOUT[lang][7]} · <a href="committee.html">{committee_label}</a>')
    return body.replace(ph(lang, phone_ph), phones)


# ---------------------------------------------------------------------------
# Page shell
# ---------------------------------------------------------------------------

def href_to(page, from_lang, to_lang):
    """Relative link from a page in from_lang to the same page in to_lang."""
    up = "../" if LANGS[from_lang]["prefix"] else ""
    return f"{up}{LANGS[to_lang]['prefix']}{page}.html"


OG_LOCALE = {"en": "en_IN", "hi": "hi_IN", "pa": "pa_IN", "ur": "ur_IN"}


def page_url(page, lang):
    """Absolute address of a page, used by search engines."""
    return f"{SITE_URL}/{LANGS[lang]['prefix']}{'' if page == 'index' else page + '.html'}"


def json_ld(lang, desc):
    """Structured data so search engines know this is the shrine's own site."""
    import json
    data = {
        "@context": "https://schema.org",
        "@type": ["PlaceOfWorship", "TouristAttraction"],
        "name": "Mashhad-e-Hind",
        "alternateName": ["Dargah-e-Aliya Mashhad-e-Hind", "Mashhad e Hind", "Mashad-e-Hind", "Panj Peer Mazar, Samana",
                          "Roza-e-Imam Mashhad Ali", "मशहद-ए-हिंद", "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ", "مشہدِ ہند"],
        "description": desc,
        "url": page_url("index", lang),
        "openingHours": "Mo-Su 06:00-21:00",
        "inLanguage": lang,
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Samana",
            "addressRegion": "Punjab",
            "postalCode": "147101",
            "addressCountry": "IN",
        },
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def sitemap():
    urls = []
    for page in PAGES:
        for lang in LANGS:
            alts = "".join(
                f'\n    <xhtml:link rel="alternate" hreflang="{o}" href="{page_url(page, o)}"/>' for o in LANGS
            )
            urls.append(f"  <url>\n    <loc>{page_url(page, lang)}</loc>{alts}\n  </url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")


def render(lang, page, title, desc, body):
    L = LANGS[lang]
    up = "../" if L["prefix"] else ""
    nav = "\n".join(
        f'    <li><a href="{p}.html"{" aria-current=\"page\"" if p == page else ""}>{label}</a></li>'
        for p, label in zip(PAGES, L["nav"])
    )
    switch = " ".join(
        f'<a href="{href_to(page, lang, other)}" lang="{other}" hreflang="{other}"'
        f'{" aria-current=\"true\"" if other == lang else ""}>{LANGS[other]["label"]}</a>'
        for other in LANGS
    )
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{other}" href="{page_url(page, other)}">'
        for other in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{page_url(page, "en")}">'
    seo = f"""<link rel="canonical" href="{page_url(page, lang)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{L['site']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{page_url(page, lang)}">
<meta property="og:locale" content="{OG_LOCALE[lang]}">"""
    if page == "index":
        seo += "\n" + json_ld(lang, desc)
    full_title = title if page == "index" else f"{title} · {L['site']}"
    U = UI[lang]
    if page == "index":
        top, body = home_hero(lang, body)
    else:
        top = f"""<section class="page-banner">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">{L['nav'][0]}</a> <span aria-hidden="true">/</span> {title}</p>
    <h1>{title}</h1>
  </div>
</section>
"""
    fonts = L["fonts"] + ("&family=Amiri:wght@400;700" if page == "index" else "")
    import re
    footer_note = re.split(r"[.।۔] ", L["footer"], maxsplit=1)[-1]
    label = dict(zip(PAGES, L["nav"]))
    quick = "".join(f'<li><a href="{p}.html">{label}</a></li>' for p, label in zip(PAGES, L["nav"]))
    return f"""<!doctype html>
<html lang="{lang}" dir="{L['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
{seo}
{alternates}
<link rel="icon" href="{up}assets/arch.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={fonts}&display=swap">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<a class="skip" href="#main">{L['skip']}</a>
<div class="topbar">
  <div class="wrap topbar-inner">
    <a class="authority" href="{WAQF_URL}" target="_blank" rel="noopener">{L['authority']}</a>
    <div class="lang-switch">{switch}</div>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><span class="emblem"><img src="{up}assets/arch.svg" alt=""></span><span class="brand-name">{L['site']}</span></a>
  </div>
</header>
<nav class="main" aria-label="{L['nav'][0]}">
  <ul>
{nav}
  </ul>
</nav>
{top}<main id="main" class="wrap">
{body.strip()}
</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <p class="footer-name">{L['site']}</p>
      <p><a href="{WAQF_URL}" target="_blank" rel="noopener">{L['authority']}</a></p>
    </div>
    <div>
      <p class="footer-head">{U['quick']}</p>
      <ul class="footer-links">{quick}</ul>
    </div>
    <div>
      <p class="footer-head">{label['contact']}</p>
      <p>{U['country']}</p>
      <p><a href="contact.html">{label['contact']}</a> · <a href="location.html">{label['location']}</a></p>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="wrap">© 2026 {L['site']} · {footer_note}</div>
  </div>
</footer>
</body>
</html>
"""


def main():
    for lang, L in LANGS.items():
        pages = content(lang)
        outdir = ROOT / L["prefix"]
        outdir.mkdir(parents=True, exist_ok=True)
        for page in PAGES:
            title, desc, body = committee_page(lang) if page == "committee" else pages[page]
            if page == "contact":
                body = contact_committee(lang, body)
            if page == "index":
                body = body.replace('<section class="cards"', home_sections(lang) + '<section class="cards"', 1)
            (outdir / f"{page}.html").write_text(render(lang, page, title, desc, body), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print("Wrote", len(LANGS) * len(PAGES), "pages, sitemap.xml and robots.txt")


if __name__ == "__main__":
    main()
