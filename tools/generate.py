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

PAGES = ["index", "history", "timings", "events", "contact", "location"]

LANGS = {
    "en": {
        "dir": "ltr", "prefix": "", "label": "English",
        "fonts": "Noto+Serif:wght@400;700",
        "site": "Mashhad-e-Hind, Samana",
        "ph": "To be confirmed by the committee",
        "nav": ["Home", "History", "Timings", "Events", "Contact", "Location"],
        "skip": "Skip to content",
        "footer": "Mashhad-e-Hind · Samana, Patiala district, Punjab, India. "
                  "Text marked in yellow is awaiting confirmation by the shrine committee.",
    },
    "ur": {
        "dir": "rtl", "prefix": "ur/", "label": "اردو",
        "fonts": "Noto+Nastaliq+Urdu:wght@400;700",
        "site": "مشہدِ ہند، سمانہ",
        "ph": "کمیٹی سے تصدیق باقی ہے",
        "nav": ["سرورق", "تاریخ", "اوقات", "تقریبات", "رابطہ", "مقام"],
        "skip": "مواد پر جائیں",
        "footer": "مشہدِ ہند · سمانہ، ضلع پٹیالہ، پنجاب، بھارت۔ "
                  "پیلے رنگ میں نشان زد عبارت کی تصدیق روضے کی کمیٹی سے ابھی باقی ہے۔",
    },
    "pa": {
        "dir": "ltr", "prefix": "pa/", "label": "ਪੰਜਾਬੀ",
        "fonts": "Noto+Sans+Gurmukhi:wght@400;700",
        "site": "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ",
        "ph": "ਕਮੇਟੀ ਵੱਲੋਂ ਪੁਸ਼ਟੀ ਬਾਕੀ ਹੈ",
        "nav": ["ਮੁੱਖ ਪੰਨਾ", "ਇਤਿਹਾਸ", "ਸਮਾਂ", "ਸਮਾਗਮ", "ਸੰਪਰਕ", "ਟਿਕਾਣਾ"],
        "skip": "ਸਮੱਗਰੀ ਵੱਲ ਜਾਓ",
        "footer": "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ · ਸਮਾਣਾ, ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ, ਭਾਰਤ। "
                  "ਪੀਲੇ ਰੰਗ ਵਿੱਚ ਦਰਸਾਈ ਲਿਖਤ ਦੀ ਪੁਸ਼ਟੀ ਰੌਜ਼ੇ ਦੀ ਕਮੇਟੀ ਵੱਲੋਂ ਹਾਲੇ ਬਾਕੀ ਹੈ।",
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
            "index": ("Mashhad-e-Hind, Samana",
                      "Mashhad-e-Hind (Panj Peer Mazar), the shrine of Imamzada Syed Mashhad Ali in Samana, Patiala district, Punjab.",
                      f"""
<section class="hero">
  <img class="arch" src="assets/arch.svg" alt="">
  <p class="eyebrow">Samana · Patiala district · Punjab</p>
  <h1>Mashhad-e-Hind</h1>
  <p class="lede">The shrine of Imamzada Syed Mashhad Ali, revered as a descendant of Imam Ali al-Rida (peace be upon him).</p>
</section>
<section>
  <h2>Welcome</h2>
  <p>Mashhad-e-Hind, known for generations as the Panj Peer Mazar, stands in the old town of Samana in Punjab. It is revered as the resting place of Imamzada Syed Mashhad Ali, of the family of the Holy Prophet Muhammad (peace be upon him and his family). Visitors of many faiths come here to offer their respects and prayers.</p>
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
<p class="uncertain">Accounts differ on his exact lineage. Some describe him as a son of Imam Ali al-Rida (peace be upon him), some as a later descendant of the Imam, and some as a son of Imam Muhammad al-Taqi (peace be upon him). {P("committee to confirm the lineage to be stated")}</p>

<h2>The shrine and its inscription</h2>
<p>For a long time the tomb was known simply as the Panj Peer Mazar. When the shrine complex was being cleaned, at the suggestion of Justice Shabbar Rizvi of the Lahore High Court, whose family had lived in Samana before Partition, a Persian inscription came to light.</p>
<p>As it has been reported, the inscription names the tomb as that of Imam Mashhad Ali and records that the building was raised by Ajruddin Khan Mughal, son of Bakhsh Allah Khan, in the month of Ramadan, 967 AH, in the fourth year of the reign of Emperor Akbar. This corresponds to about 1560 CE; some accounts give 1559.</p>
<p class="uncertain">The reading of the inscription is reported to have been examined by religious scholars, historians and visiting officials. A published scholarly reading has not yet been found. {P("committee to add the full text and translation of the inscription, and a photograph")}</p>

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
    <tr><td>Daily</td><td>{P("e.g. 6:00 am – 9:00 pm")}</td></tr>
    <tr><td>Thursday evening</td><td>{P("Thursday programme, if any")}</td></tr>
    <tr><td>Friday</td><td>{P("Friday prayer time")}</td></tr>
  </tbody>
</table></div>

<h2>Daily prayers</h2>
<p>{P("Times of congregational prayers, if held at the shrine")}</p>

<h2>During Muharram and special occasions</h2>
<p>{P("Extended hours during Muharram and on other occasions")}</p>

<h2>When visiting</h2>
<ul>
  <li>Please dress modestly and cover your head.</li>
  <li>Remove your shoes before entering the shrine.</li>
  <li>Kindly keep silence near the grave and respect those at prayer.</li>
  <li>{P("Rules on photography inside the shrine")}</li>
</ul>
"""),
            "events": ("Events",
                       "Majalis and observances at Mashhad-e-Hind, Samana.",
                       f"""
<p>Islamic dates follow the lunar calendar, so the Gregorian dates change every year. The committee will announce exact dates.</p>
<div class="table-scroll"><table>
  <thead><tr><th>Occasion</th><th>Islamic date</th><th>This year</th></tr></thead>
  <tbody>
    <tr><td>Annual majlis (Salana Majlis) at Mashhad-e-Hind</td><td>{P("date")}</td><td>{P("date and speakers")}</td></tr>
    <tr><td>Majalis of Muharram</td><td>1–10 Muharram</td><td>{P("programme")}</td></tr>
    <tr><td>{P("Other observances held at the shrine")}</td><td>{P("date")}</td><td>{P("date")}</td></tr>
  </tbody>
</table></div>
<p>Programmes of past majalis may be found on the shrine's social media pages. {P("links to official pages")}</p>
"""),
            "contact": ("Contact",
                        "Contact the committee of Mashhad-e-Hind, Samana.",
                        f"""
<p>For visits, events and enquiries, please contact the shrine committee.</p>
<div class="table-scroll"><table>
  <tbody>
    <tr><th>Committee</th><td>{P("name of the managing committee")}</td></tr>
    <tr><th>Phone</th><td>{P("phone number")}</td></tr>
    <tr><th>Email</th><td>{P("email address")}</td></tr>
    <tr><th>Address</th><td>{P("full postal address")}<br>Samana, Patiala district, Punjab {P("PIN code")}, India</td></tr>
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
            "index": ("مشہدِ ہند، سمانہ",
                      "مشہدِ ہند (پنج پیر مزار)، امام زادہ سید مشہد علی کا روضہ، سمانہ، ضلع پٹیالہ، پنجاب۔",
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
<p class="uncertain">ان کے نسب کے بارے میں روایات مختلف ہیں۔ بعض انہیں حضرت امام علی رضا علیہ السلام کا فرزند، بعض امام کی بعد کی نسل سے، اور بعض حضرت امام محمد تقی علیہ السلام کا فرزند بیان کرتے ہیں۔ {P("کمیٹی بیان کیے جانے والے نسب کی تصدیق کرے")}</p>

<h2>روضہ اور اس کا کتبہ</h2>
<p>ایک عرصے تک یہ مزار صرف پنج پیر مزار کے نام سے جانا جاتا تھا۔ لاہور ہائی کورٹ کے جسٹس شبر رضوی کی تجویز پر، جن کا خاندان تقسیم سے پہلے سمانہ میں آباد تھا، جب روضے کے احاطے کی صفائی کی گئی تو ایک فارسی کتبہ سامنے آیا۔</p>
<p>بیان کے مطابق اس کتبے میں اس مزار کو امام مشہد علی کا مزار کہا گیا ہے اور درج ہے کہ یہ عمارت اجرالدین خان مغل ولد بخش اللہ خان نے ماہِ رمضان ۹۶۷ ہجری میں، شہنشاہ اکبر کے دورِ حکومت کے چوتھے سال تعمیر کروائی۔ یہ تقریباً ۱۵۶۰ء بنتا ہے؛ بعض بیانات میں ۱۵۵۹ء درج ہے۔</p>
<p class="uncertain">بیان کیا جاتا ہے کہ اس کتبے کی قرأت کا جائزہ علمائے دین، مؤرخین اور آنے والے حکام نے لیا۔ اس کی کوئی شائع شدہ علمی قرأت ابھی تک نہیں ملی۔ {P("کمیٹی کتبے کا مکمل متن، ترجمہ اور تصویر شامل کرے")}</p>

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
    <tr><td>روزانہ</td><td>{P("مثلاً صبح ۶ بجے سے رات ۹ بجے تک")}</td></tr>
    <tr><td>جمعرات کی شام</td><td>{P("جمعرات کا پروگرام، اگر ہو")}</td></tr>
    <tr><td>جمعہ</td><td>{P("نمازِ جمعہ کا وقت")}</td></tr>
  </tbody>
</table></div>

<h2>روزانہ نمازیں</h2>
<p>{P("باجماعت نماز کے اوقات، اگر روضے پر ادا ہوتی ہو")}</p>

<h2>محرم اور خاص مواقع</h2>
<p>{P("محرم اور دیگر مواقع پر توسیع شدہ اوقات")}</p>

<h2>زیارت کے آداب</h2>
<ul>
  <li>براہِ کرم باوقار لباس پہنیں اور سر ڈھانپیں۔</li>
  <li>روضے میں داخل ہونے سے پہلے جوتے اتار دیں۔</li>
  <li>مزار کے قریب خاموشی رکھیں اور نماز پڑھنے والوں کا احترام کریں۔</li>
  <li>{P("روضے کے اندر تصویر کشی کے قواعد")}</li>
</ul>
"""),
            "events": ("تقریبات",
                       "مشہدِ ہند، سمانہ میں مجالس اور مواقع۔",
                       f"""
<p>اسلامی تاریخیں قمری تقویم کے مطابق ہوتی ہیں، اس لیے عیسوی تاریخیں ہر سال بدلتی ہیں۔ کمیٹی صحیح تاریخوں کا اعلان کرے گی۔</p>
<div class="table-scroll"><table>
  <thead><tr><th>موقع</th><th>اسلامی تاریخ</th><th>اس سال</th></tr></thead>
  <tbody>
    <tr><td>مشہدِ ہند کی سالانہ مجلس</td><td>{P("تاریخ")}</td><td>{P("تاریخ اور خطبا")}</td></tr>
    <tr><td>مجالسِ محرم</td><td>۱ تا ۱۰ محرم</td><td>{P("پروگرام")}</td></tr>
    <tr><td>{P("روضے پر منائے جانے والے دیگر مواقع")}</td><td>{P("تاریخ")}</td><td>{P("تاریخ")}</td></tr>
  </tbody>
</table></div>
<p>گزشتہ مجالس کے پروگرام روضے کے سوشل میڈیا صفحات پر دیکھے جا سکتے ہیں۔ {P("سرکاری صفحات کے لنک")}</p>
"""),
            "contact": ("رابطہ",
                        "مشہدِ ہند، سمانہ کی کمیٹی سے رابطہ۔",
                        f"""
<p>زیارت، تقریبات اور معلومات کے لیے براہِ کرم روضے کی کمیٹی سے رابطہ کریں۔</p>
<div class="table-scroll"><table>
  <tbody>
    <tr><th>کمیٹی</th><td>{P("انتظامی کمیٹی کا نام")}</td></tr>
    <tr><th>فون</th><td>{P("فون نمبر")}</td></tr>
    <tr><th>ای میل</th><td>{P("ای میل پتہ")}</td></tr>
    <tr><th>پتہ</th><td>{P("مکمل ڈاک کا پتہ")}<br>سمانہ، ضلع پٹیالہ، پنجاب {P("پن کوڈ")}، بھارت</td></tr>
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

    if lang == "pa":
        return {
            "index": ("ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ",
                      "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ (ਪੰਜ ਪੀਰ ਮਜ਼ਾਰ), ਇਮਾਮਜ਼ਾਦਾ ਸੱਯਦ ਮਸ਼ਹਦ ਅਲੀ ਦਾ ਰੌਜ਼ਾ, ਸਮਾਣਾ, ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ।",
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
<p class="uncertain">ਉਨ੍ਹਾਂ ਦੀ ਵੰਸ਼ਾਵਲੀ ਬਾਰੇ ਬਿਰਤਾਂਤ ਵੱਖਰੇ ਹਨ। ਕੁਝ ਉਨ੍ਹਾਂ ਨੂੰ ਹਜ਼ਰਤ ਇਮਾਮ ਅਲੀ ਰਜ਼ਾ (ਅਲੈਹਿਸ-ਸਲਾਮ) ਦੇ ਪੁੱਤਰ, ਕੁਝ ਇਮਾਮ ਦੀ ਬਾਅਦ ਦੀ ਪੀੜ੍ਹੀ ਵਿੱਚੋਂ, ਅਤੇ ਕੁਝ ਹਜ਼ਰਤ ਇਮਾਮ ਮੁਹੰਮਦ ਤਕੀ (ਅਲੈਹਿਸ-ਸਲਾਮ) ਦੇ ਪੁੱਤਰ ਦੱਸਦੇ ਹਨ। {P("ਕਮੇਟੀ ਦੱਸੀ ਜਾਣ ਵਾਲੀ ਵੰਸ਼ਾਵਲੀ ਦੀ ਪੁਸ਼ਟੀ ਕਰੇ")}</p>

<h2>ਰੌਜ਼ਾ ਅਤੇ ਇਸ ਦਾ ਸ਼ਿਲਾਲੇਖ</h2>
<p>ਲੰਮੇ ਸਮੇਂ ਤੱਕ ਇਹ ਮਜ਼ਾਰ ਸਿਰਫ਼ ਪੰਜ ਪੀਰ ਮਜ਼ਾਰ ਦੇ ਨਾਂ ਨਾਲ ਜਾਣਿਆ ਜਾਂਦਾ ਸੀ। ਲਾਹੌਰ ਹਾਈ ਕੋਰਟ ਦੇ ਜਸਟਿਸ ਸ਼ੱਬਰ ਰਿਜ਼ਵੀ ਦੇ ਸੁਝਾਅ ਉੱਤੇ, ਜਿਨ੍ਹਾਂ ਦਾ ਪਰਿਵਾਰ ਵੰਡ ਤੋਂ ਪਹਿਲਾਂ ਸਮਾਣਾ ਵਿੱਚ ਵੱਸਦਾ ਸੀ, ਜਦੋਂ ਰੌਜ਼ੇ ਦੇ ਅਹਾਤੇ ਦੀ ਸਫ਼ਾਈ ਕੀਤੀ ਗਈ ਤਾਂ ਇੱਕ ਫ਼ਾਰਸੀ ਸ਼ਿਲਾਲੇਖ ਸਾਹਮਣੇ ਆਇਆ।</p>
<p>ਦੱਸੇ ਅਨੁਸਾਰ ਇਸ ਸ਼ਿਲਾਲੇਖ ਵਿੱਚ ਇਸ ਮਜ਼ਾਰ ਨੂੰ ਇਮਾਮ ਮਸ਼ਹਦ ਅਲੀ ਦਾ ਮਜ਼ਾਰ ਕਿਹਾ ਗਿਆ ਹੈ ਅਤੇ ਦਰਜ ਹੈ ਕਿ ਇਹ ਇਮਾਰਤ ਅਜਰੁੱਦੀਨ ਖ਼ਾਨ ਮੁਗ਼ਲ, ਪੁੱਤਰ ਬਖ਼ਸ਼ ਅੱਲਾਹ ਖ਼ਾਨ, ਨੇ ਰਮਜ਼ਾਨ ਦੇ ਮਹੀਨੇ 967 ਹਿਜਰੀ ਵਿੱਚ, ਬਾਦਸ਼ਾਹ ਅਕਬਰ ਦੇ ਰਾਜ ਦੇ ਚੌਥੇ ਸਾਲ ਬਣਵਾਈ। ਇਹ ਲਗਭਗ 1560 ਈ. ਬਣਦਾ ਹੈ; ਕੁਝ ਬਿਰਤਾਂਤਾਂ ਵਿੱਚ 1559 ਦਰਜ ਹੈ।</p>
<p class="uncertain">ਦੱਸਿਆ ਜਾਂਦਾ ਹੈ ਕਿ ਇਸ ਸ਼ਿਲਾਲੇਖ ਦੀ ਪੜ੍ਹਤ ਦੀ ਜਾਂਚ ਧਾਰਮਿਕ ਵਿਦਵਾਨਾਂ, ਇਤਿਹਾਸਕਾਰਾਂ ਅਤੇ ਆਏ ਅਧਿਕਾਰੀਆਂ ਨੇ ਕੀਤੀ। ਇਸ ਦੀ ਕੋਈ ਛਪੀ ਹੋਈ ਵਿਦਵਤਾਪੂਰਨ ਪੜ੍ਹਤ ਹਾਲੇ ਨਹੀਂ ਮਿਲੀ। {P("ਕਮੇਟੀ ਸ਼ਿਲਾਲੇਖ ਦੀ ਪੂਰੀ ਲਿਖਤ, ਅਨੁਵਾਦ ਅਤੇ ਤਸਵੀਰ ਸ਼ਾਮਲ ਕਰੇ")}</p>

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
    <tr><td>ਰੋਜ਼ਾਨਾ</td><td>{P("ਜਿਵੇਂ ਸਵੇਰੇ 6 ਵਜੇ ਤੋਂ ਰਾਤ 9 ਵਜੇ ਤੱਕ")}</td></tr>
    <tr><td>ਵੀਰਵਾਰ ਸ਼ਾਮ</td><td>{P("ਵੀਰਵਾਰ ਦਾ ਪ੍ਰੋਗਰਾਮ, ਜੇ ਹੋਵੇ")}</td></tr>
    <tr><td>ਸ਼ੁੱਕਰਵਾਰ</td><td>{P("ਜੁਮੇ ਦੀ ਨਮਾਜ਼ ਦਾ ਸਮਾਂ")}</td></tr>
  </tbody>
</table></div>

<h2>ਰੋਜ਼ਾਨਾ ਨਮਾਜ਼</h2>
<p>{P("ਜਮਾਤ ਨਾਲ ਨਮਾਜ਼ ਦੇ ਸਮੇਂ, ਜੇ ਰੌਜ਼ੇ ਉੱਤੇ ਹੁੰਦੀ ਹੋਵੇ")}</p>

<h2>ਮੁਹੱਰਮ ਅਤੇ ਖ਼ਾਸ ਮੌਕੇ</h2>
<p>{P("ਮੁਹੱਰਮ ਅਤੇ ਹੋਰ ਮੌਕਿਆਂ ਉੱਤੇ ਵਧਾਏ ਗਏ ਸਮੇਂ")}</p>

<h2>ਜ਼ਿਆਰਤ ਦੇ ਅਦਬ</h2>
<ul>
  <li>ਕਿਰਪਾ ਕਰਕੇ ਸਾਦਾ ਅਤੇ ਮਰਿਆਦਾ ਵਾਲਾ ਪਹਿਰਾਵਾ ਪਾਓ ਅਤੇ ਸਿਰ ਢੱਕੋ।</li>
  <li>ਰੌਜ਼ੇ ਵਿੱਚ ਦਾਖ਼ਲ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਜੁੱਤੀਆਂ ਉਤਾਰ ਦਿਓ।</li>
  <li>ਮਜ਼ਾਰ ਦੇ ਨੇੜੇ ਚੁੱਪ ਰੱਖੋ ਅਤੇ ਨਮਾਜ਼ ਪੜ੍ਹਨ ਵਾਲਿਆਂ ਦਾ ਸਤਿਕਾਰ ਕਰੋ।</li>
  <li>{P("ਰੌਜ਼ੇ ਦੇ ਅੰਦਰ ਤਸਵੀਰਾਂ ਖਿੱਚਣ ਦੇ ਨਿਯਮ")}</li>
</ul>
"""),
            "events": ("ਸਮਾਗਮ",
                       "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ ਵਿਖੇ ਮਜਲਿਸਾਂ ਅਤੇ ਮੌਕੇ।",
                       f"""
<p>ਇਸਲਾਮੀ ਤਰੀਕਾਂ ਚੰਦਰ ਕੈਲੰਡਰ ਅਨੁਸਾਰ ਹੁੰਦੀਆਂ ਹਨ, ਇਸ ਲਈ ਅੰਗਰੇਜ਼ੀ ਤਰੀਕਾਂ ਹਰ ਸਾਲ ਬਦਲਦੀਆਂ ਹਨ। ਕਮੇਟੀ ਸਹੀ ਤਰੀਕਾਂ ਦਾ ਐਲਾਨ ਕਰੇਗੀ।</p>
<div class="table-scroll"><table>
  <thead><tr><th>ਮੌਕਾ</th><th>ਇਸਲਾਮੀ ਤਰੀਕ</th><th>ਇਸ ਸਾਲ</th></tr></thead>
  <tbody>
    <tr><td>ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ ਦੀ ਸਾਲਾਨਾ ਮਜਲਿਸ</td><td>{P("ਤਰੀਕ")}</td><td>{P("ਤਰੀਕ ਅਤੇ ਬੁਲਾਰੇ")}</td></tr>
    <tr><td>ਮੁਹੱਰਮ ਦੀਆਂ ਮਜਲਿਸਾਂ</td><td>1 ਤੋਂ 10 ਮੁਹੱਰਮ</td><td>{P("ਪ੍ਰੋਗਰਾਮ")}</td></tr>
    <tr><td>{P("ਰੌਜ਼ੇ ਉੱਤੇ ਮਨਾਏ ਜਾਂਦੇ ਹੋਰ ਮੌਕੇ")}</td><td>{P("ਤਰੀਕ")}</td><td>{P("ਤਰੀਕ")}</td></tr>
  </tbody>
</table></div>
<p>ਪਿਛਲੀਆਂ ਮਜਲਿਸਾਂ ਦੇ ਪ੍ਰੋਗਰਾਮ ਰੌਜ਼ੇ ਦੇ ਸੋਸ਼ਲ ਮੀਡੀਆ ਪੰਨਿਆਂ ਉੱਤੇ ਵੇਖੇ ਜਾ ਸਕਦੇ ਹਨ। {P("ਅਧਿਕਾਰਤ ਪੰਨਿਆਂ ਦੇ ਲਿੰਕ")}</p>
"""),
            "contact": ("ਸੰਪਰਕ",
                        "ਮਸ਼ਹਦ-ਏ-ਹਿੰਦ, ਸਮਾਣਾ ਦੀ ਕਮੇਟੀ ਨਾਲ ਸੰਪਰਕ।",
                        f"""
<p>ਜ਼ਿਆਰਤ, ਸਮਾਗਮਾਂ ਅਤੇ ਜਾਣਕਾਰੀ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਰੌਜ਼ੇ ਦੀ ਕਮੇਟੀ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।</p>
<div class="table-scroll"><table>
  <tbody>
    <tr><th>ਕਮੇਟੀ</th><td>{P("ਪ੍ਰਬੰਧਕ ਕਮੇਟੀ ਦਾ ਨਾਂ")}</td></tr>
    <tr><th>ਫ਼ੋਨ</th><td>{P("ਫ਼ੋਨ ਨੰਬਰ")}</td></tr>
    <tr><th>ਈਮੇਲ</th><td>{P("ਈਮੇਲ ਪਤਾ")}</td></tr>
    <tr><th>ਪਤਾ</th><td>{P("ਪੂਰਾ ਡਾਕ ਪਤਾ")}<br>ਸਮਾਣਾ, ਜ਼ਿਲ੍ਹਾ ਪਟਿਆਲਾ, ਪੰਜਾਬ {P("ਪਿੰਨ ਕੋਡ")}, ਭਾਰਤ</td></tr>
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
# Page shell
# ---------------------------------------------------------------------------

def href_to(page, from_lang, to_lang):
    """Relative link from a page in from_lang to the same page in to_lang."""
    up = "../" if LANGS[from_lang]["prefix"] else ""
    return f"{up}{LANGS[to_lang]['prefix']}{page}.html"


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
        f'<link rel="alternate" hreflang="{other}" href="/{LANGS[other]["prefix"]}{"" if page == "index" else page + ".html"}">'
        for other in LANGS
    )
    full_title = title if page == "index" else f"{title} · {L['site']}"
    heading = "" if page == "index" else f'<div class="page-title"><h1>{title}</h1></div>\n'
    return f"""<!doctype html>
<html lang="{lang}" dir="{L['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
{alternates}
<link rel="icon" href="{up}assets/arch.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={L['fonts']}&display=swap">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<a class="skip" href="#main">{L['skip']}</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="{up}assets/arch.svg" alt="">{L['site']}</a>
    <div class="lang-switch">{switch}</div>
  </div>
</header>
<nav class="main" aria-label="{L['nav'][0]}">
  <ul>
{nav}
  </ul>
</nav>
<main id="main" class="wrap">
{heading}{body.strip()}
</main>
<footer class="site-footer">
  <div class="wrap">{L['footer']}</div>
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
            title, desc, body = pages[page]
            (outdir / f"{page}.html").write_text(render(lang, page, title, desc, body), encoding="utf-8")
    print("Wrote", len(LANGS) * len(PAGES), "pages")


if __name__ == "__main__":
    main()
