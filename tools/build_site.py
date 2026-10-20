#!/usr/bin/env python3
"""Builds the Hub2U website (docs/*.html) from the approved page content.
Run:  python3 tools/build_site.py
Text comes from content/*.md (approved by the owner). Edit text here, then rebuild.
"""
import os, html

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs')

def esc(s):
    return html.escape(s, quote=True)

def ph(key, text):
    return f'<span class="ph" data-fill="{key}">{text}</span>'

PH = {
    'phone': ph('phone', '[ใส่เบอร์โทร]'),
    'hours': ph('hours', '[ใส่เวลาทำการ]'),
    'lineId': ph('lineId', '[ใส่ไลน์ไอดี]'),
    'hub': ph('hubLocation', '[ใส่ตำแหน่งจุดฮับ]'),
    'fee': ph('deliveryFee', '[ใส่ค่าส่งที่ยืนยันแล้ว]'),
    'cutoff': ph('orderCutoff', '[ใส่เวลารับออเดอร์]'),
    'rounds': ph('deliveryRounds', '[ใส่รอบส่ง]'),
    'daysoff': ph('daysOff', '[ใส่วันหยุด ถ้ามี]'),
    'outofstock': ph('outOfStock', '[ใส่วิธีที่ทีมงานจัดการ]'),
    'cancel': ph('cancelPolicy', '[ใส่เงื่อนไขการยกเลิกและคืนเงิน]'),
    'shopfee': ph('shopFee', '[ใส่เปอร์เซ็นต์ที่ยืนยันแล้ว]'),
    'shoppay': ph('shopPayCycle', '[ใส่รอบจ่ายเงินร้านค้า]'),
    'shopdocs': ph('shopDocs', '[ใส่เอกสารที่ต้องใช้]'),
    'riderrate': ph('riderRate', '[ใส่ตัวเลขที่ยืนยันแล้ว]'),
    'riderpay': ph('riderPayCycle', '[ใส่รอบจ่ายเงินไรเดอร์]'),
    'riderdocs': ph('riderDocs', '[ใส่เอกสารที่ต้องใช้]'),
    'story': ph('story', '[ใส่เรื่องราวว่าทำไมถึงทำ Hub2U เล่าสั้นๆ 2-3 ประโยค]'),
}

def ms(name):
    return f'<span class="ms" aria-hidden="true">{name}</span>'

def btn(label, href=None, kind='primary', icon=None, link=None, block=False):
    cls = f'btn btn-{kind}' + (' btn-block' if block else '')
    attrs = f'href="{href or "contact.html"}"'
    if link:
        attrs += f' data-link="{link}"'
    return f'<a class="{cls}" {attrs}>{ms(icon) if icon else ""}{label}</a>'

def order_btn(block=False):
    return btn('สั่งของสด', 'order-now.html', 'primary', 'shopping_basket', block=block)

def line_btn(label='แอดไลน์', block=False, kind='secondary'):
    return btn(label, 'contact.html', kind, 'chat', link='line', block=block)

def card(icon, title, text, extra=''):
    return f'<div class="card"><div class="icon">{ms(icon)}</div><h3>{title}</h3><p>{text}</p>{extra}</div>'

def faq(q, a):
    return f'<details><summary>{q}</summary><div><p>{a}</p></div></details>'

def map_svg(label='แผนที่ภาพประกอบ ตลาดวิศิษฐ์ชัยอยู่ตรงกลาง มีวงกลมรัศมี 7 กิโลเมตร'):
    return f'''<svg class="map" viewBox="0 0 400 300" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">
<defs><pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="#FED7AA"/></pattern></defs>
<rect width="400" height="300" fill="#FFF7ED"/><rect width="400" height="300" fill="url(#dots)"/>
<circle cx="200" cy="150" r="120" fill="rgba(234,88,12,.07)" stroke="#EA580C" stroke-width="3" stroke-dasharray="10 8"/>
<line x1="200" y1="150" x2="320" y2="150" stroke="#C2410C" stroke-width="2"/>
<rect x="238" y="118" width="96" height="28" rx="14" fill="#fff" stroke="#FED7AA"/>
<text x="286" y="138" text-anchor="middle" font-size="15" font-weight="600" fill="#C2410C">รัศมี 7 กม.</text>
<circle cx="200" cy="150" r="18" fill="#EA580C"/><circle cx="200" cy="150" r="7" fill="#fff"/>
<rect x="140" y="176" width="120" height="30" rx="15" fill="#fff" stroke="#FED7AA"/>
<text x="200" y="197" text-anchor="middle" font-size="16" font-weight="600" fill="#292524">ตลาดวิศิษฐ์ชัย</text>
</svg>'''

NAV = [
    ('index.html', 'หน้าแรก'),
    ('how-to-order.html', 'วิธีสั่งซื้อ'),
    ('delivery-area.html', 'พื้นที่จัดส่ง'),
    ('join-us.html', 'ร่วมงานกับเรา'),
    ('about.html', 'เกี่ยวกับเรา'),
    ('contact.html', 'ติดต่อเรา'),
]
SUB = [('shop-signup.html', 'สมัครร้านค้า'), ('rider-signup.html', 'สมัครไรเดอร์')]
JOIN_PAGES = {'join-us.html', 'shop-signup.html', 'rider-signup.html'}

def header(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if (href == current or (href == 'join-us.html' and current in JOIN_PAGES)) else ''
        if href == 'join-us.html':
            subs = ''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{l}</a></li>' for h, l in SUB)
            items.append(f'<div class="nav-item has-sub"><a href="{href}"{cur}>{label}</a>'
                         f'<button class="sub-toggle" type="button" aria-expanded="false" aria-label="เปิดเมนูย่อยของร่วมงานกับเรา">{ms("expand_more")}</button>'
                         f'<ul class="sub">{subs}</ul></div>')
        else:
            items.append(f'<a href="{href}"{cur}>{label}</a>')
    nav = ''.join(items)
    return f'''<header class="site-header"><div class="container header-inner">
<a class="brand" href="index.html" aria-label="Hub2U หน้าแรก">
<img class="logo" src="assets/img/logo.png" alt="โลโก้ Hub2U" onerror="this.style.display='none';this.nextElementSibling.style.display='grid'">
<span class="logo-ph" aria-hidden="true">Logo</span>
<span class="brand-name">Hub2U<small>ตลาดวิศิษฐ์ชัย บ้านบึง</small></span></a>
<button class="nav-toggle" id="navToggle" type="button" aria-expanded="false" aria-controls="siteNav" aria-label="เปิดหรือปิดเมนู">{ms("menu")}</button>
<nav class="site-nav" id="siteNav" aria-label="เมนูหลัก">{nav}
<a class="btn btn-primary nav-cta" href="order-now.html">{ms("shopping_basket")}สั่งของสด</a></nav>
</div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="container">
<div class="footer-grid">
<div><h3>Hub2U</h3><p>บริการส่งของสดจากตลาดวิศิษฐ์ชัย บ้านบึง ชลบุรี</p>
<p class="small">เปิดผ่านมือถือได้เลย ไม่ต้องโหลดจากสโตร์ กด "เพิ่มลงหน้าจอหลัก" ไว้ใช้เหมือนแอปได้</p></div>
<div><h3>เมนู</h3><ul class="footer-links">
<li><a href="index.html">หน้าแรก</a></li><li><a href="how-to-order.html">วิธีสั่งซื้อ</a></li><li><a href="delivery-area.html">พื้นที่จัดส่ง</a></li>
<li><a href="shop-signup.html">สมัครร้านค้า</a></li><li><a href="rider-signup.html">สมัครไรเดอร์</a></li><li><a href="about.html">เกี่ยวกับเรา</a></li><li><a href="contact.html">ติดต่อเรา</a></li></ul></div>
<div><h3>ติดต่อ</h3><ul class="footer-links">
<li>โทร: {PH['phone']}</li><li>ไลน์: {PH['lineId']}</li><li>เวลาทำการ: {PH['hours']}</li></ul></div>
</div>
<p class="copyright">© 2026 Hub2U</p>
</div></footer>
<nav class="mobile-bar" aria-label="ปุ่มลัด">{order_btn()}{line_btn()}</nav>'''

def page(fname, title, desc, body, current=None):
    current = current or fname
    doc = f'''<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="th_TH">
<meta name="theme-color" content="#EA580C">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kanit:wght@400;500;600;700&family=Prompt:wght@400;500;600&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&display=block">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">ข้ามไปเนื้อหา</a>
{header(current)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/js/config.js"></script>
<script src="assets/js/site.js"></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, fname), 'w', encoding='utf-8') as f:
        f.write(doc)

def page_head(title, sub):
    return f'<section class="hero"><div class="container"><h1>{title}</h1><p class="lead">{sub}</p></div></section>'

def cta_end(text='พร้อมสั่งแล้ว หรือมีอะไรสงสัย'):
    return f'''<section class="block band"><div class="container center"><h2>{text}</h2>
<div class="btn-row" style="justify-content:center;max-width:520px;margin:20px auto 0">{order_btn()}{line_btn()}</div></div></section>'''

CONSENT = '<p class="small muted">การสมัครหมายถึงยินยอมให้ Hub2U เก็บและใช้ข้อมูลเพื่อการให้บริการ</p>'

# ---------------------------------------------------------------- 01 home
home = f'''
<section class="hero"><div class="container hero-grid">
<div>
<span class="tag">{ms("location_on")}บริการส่งของสด จากตลาดวิศิษฐ์ชัย บ้านบึง</span>
<h1>ของสดจากตลาดวิศิษฐ์ชัย <span class="accent">ส่งถึงหน้าบ้าน</span></h1>
<p class="lead">สั่งหลายร้าน ถุงเดียว ค่าส่งรอบเดียว</p>
<div class="btn-row">{order_btn()}{line_btn()}</div>
<p class="small muted" style="margin-top:14px">เปิดผ่านมือถือได้เลย ไม่ต้องโหลดแอป</p>
</div>
<img class="hero-img" src="assets/img/hero-doorstep.jpg" width="1200" height="896" alt="ถุงของสดวางอยู่หน้าบ้าน มีผักและมะเขือเทศ">
</div></section>

<section class="block"><div class="container">
<div class="section-head center"><h2>ทำไมต้องสั่งกับ Hub2U</h2></div>
<div class="grid grid-3">
{card("shopping_basket", "สั่งหลายร้าน ถุงเดียว", "เลือกผัก เนื้อ ผลไม้จากร้านในตลาดไว้ในออเดอร์เดียว ทีมงานจัดรวมใส่ถุงเดียวให้")}
{card("local_shipping", "ค่าส่งรอบเดียว", "สั่งจากหลายร้านก็จ่ายค่าส่งครั้งเดียว ไม่ต้องจ่ายซ้ำทีละร้าน")}
{card("pin_drop", "ปักหมุดบ้าน ดูสถานะได้", "กดเลือกบ้านบนแผนที่ ไม่ต้องพิมพ์ที่อยู่ยาวๆ และดูสถานะออเดอร์ได้ผ่านลิงก์ส่วนตัว")}
</div></div></section>

<section class="block band"><div class="container">
<div class="section-head center"><h2>สั่งง่ายๆ 4 ขั้นตอน</h2></div>
<ol class="steps steps-row">
<li><div><h3>เลือกของและจ่ายเงิน</h3><p>ใส่ของลงตะกร้า ปักหมุดบ้าน แล้วจ่ายผ่านพร้อมเพย์ตอนยืนยันออเดอร์</p></div></li>
<li><div><h3>ทีมในตลาดจัดของให้</h3><p>ทีมงานในตลาดเลือกของ ชั่งน้ำหนัก และจัดรวมใส่ถุงเดียว</p></div></li>
<li><div><h3>ไรเดอร์ส่งถึงบ้าน</h3><p>ไรเดอร์นำถุงของสดไปส่งถึงจุดที่คุณปักหมุดไว้</p></div></li>
<li><div><h3>รับของที่บ้าน</h3><p>รับของสด พร้อมทำอาหารได้เลย</p></div></li>
</ol>
<p class="note-line center">ของที่ขายตามน้ำหนัก เช่น เนื้อหมู คิดราคาตามน้ำหนักจริง ถ้าชั่งได้น้อยกว่าที่สั่ง เราคืนเงินส่วนต่างให้</p>
</div></section>

<section class="block"><div class="container hero-grid">
<div><h2>ส่งถึงบ้านคุณไหม</h2>
<div class="callout"><p class="big">ส่งในรัศมีไม่เกิน 7 กม. จากตลาดวิศิษฐ์ชัย (วัดเป็นเส้นตรง)</p>
<p class="muted" style="margin:0">ไม่แน่ใจว่าบ้านอยู่ในพื้นที่ไหม ทักไลน์มาถามได้</p></div>
<div class="btn-row"><a class="btn btn-secondary" href="delivery-area.html">{ms("map")}ดูพื้นที่จัดส่ง</a></div></div>
<div>{map_svg()}</div>
</div></section>

<section class="block band"><div class="container">
<div class="section-head center"><h2>ร่วมเป็นส่วนหนึ่งกับ Hub2U</h2><p>ร้านค้าและไรเดอร์ในพื้นที่บ้านบึง มาทำงานด้วยกันได้</p></div>
<div class="grid grid-2">
{card("storefront", "ร้านค้า/แผงในตลาด", "สมัครฟรี ไม่มีค่าใช้จ่ายล่วงหน้า เปิด-ปิดร้านเองได้ ไม่ต้องทำแอปเอง", '<div class="btn-row"><a class="btn btn-primary" href="shop-signup.html">สมัครร้านค้า</a></div>')}
{card("two_wheeler", "ไรเดอร์", "เลือกเวลาทำงานเอง สมัครผ่านมือถือ", '<div class="btn-row"><a class="btn btn-primary" href="rider-signup.html">สมัครไรเดอร์</a></div>')}
</div></div></section>

<section class="block"><div class="container hero-grid">
<img class="photo" src="assets/img/market-vendor.jpg" width="1200" height="670" alt="แม่ค้าในตลาดสดยิ้มแย้ม ถือถั่วฝักยาว มีผักและผลไม้เต็มแผง" loading="lazy">
<div><h2>เรื่องราวของ Hub2U</h2>
<p>Hub2U เริ่มต้นจากตลาดวิศิษฐ์ชัย บ้านบึง เรารวมของจากร้านในตลาดให้สั่งได้ในที่เดียว ทีมงานในตลาดเลือกและจัดของให้ แล้วไรเดอร์ในพื้นที่ส่งถึงหน้าบ้าน</p>
<p>{PH['story']}</p>
<div class="btn-row"><a class="btn btn-secondary" href="about.html">เกี่ยวกับเรา</a></div></div>
</div></section>

<section class="block band"><div class="container hero-grid">
<div><h2>คุยกับเราทางไลน์</h2>
<p>สอบถามเรื่องสั่งของ พื้นที่จัดส่ง หรือการสมัคร ทักมาได้เลย</p>
<div class="btn-row">{line_btn('แอดไลน์', kind='primary')}</div>
<ul class="contact-list" style="margin-top:20px"><li>{ms("call")}<span>โทร: {PH['phone']}</span></li><li>{ms("schedule")}<span>เวลาทำการ: {PH['hours']}</span></li></ul></div>
<div class="qr-box" data-image="lineQrImage" data-alt="QR ไลน์ Hub2U"><span>QR ไลน์<br><span class="ph small">[ใส่ QR ไลน์]</span></span></div>
</div></section>
'''
page('index.html', 'Hub2U ของสดจากตลาดวิศิษฐ์ชัย ส่งถึงหน้าบ้าน',
     'สั่งของสดจากตลาดวิศิษฐ์ชัย บ้านบึง ทีมงานจัดใส่ถุงเดียว ไรเดอร์ส่งถึงบ้าน ค่าส่งรอบเดียว ส่งในรัศมี 7 กม. จากตลาด', home)

# ---------------------------------------------------------------- 02 how to order
howto = f'''
{page_head("วิธีสั่งซื้อของสดกับ Hub2U", "ใช้เวลาไม่กี่นาที สั่งผ่านมือถือได้เลย ไม่ต้องโหลดแอป")}
<section class="block band"><div class="container">
<div class="section-head"><h2>4 ขั้นตอนแบบละเอียด</h2></div>
<ol class="steps" style="max-width:760px">
<li><div><h3>เลือกของใส่ตะกร้า</h3><p>เข้าเว็บแอป Hub2U เลือกผัก เนื้อสัตว์ อาหารทะเล หรือผลไม้จากร้านในตลาดวิศิษฐ์ชัย สั่งจากหลายร้านรวมในออเดอร์เดียวได้</p></div></li>
<li><div><h3>ปักหมุดบ้านและจ่ายเงิน</h3><p>กดเลือกตำแหน่งบ้านบนแผนที่ แล้วชำระเงินล่วงหน้าผ่านพร้อมเพย์ตอนยืนยันออเดอร์</p></div></li>
<li><div><h3>ทีมในตลาดจัดของให้</h3><p>ทีมงานเลือกของ ชั่งน้ำหนัก และจัดรวมใส่ถุงเดียวให้</p></div></li>
<li><div><h3>ไรเดอร์ส่งถึงบ้าน</h3><p>ไรเดอร์นำถุงของสดไปส่งถึงจุดที่ปักหมุดไว้ คุณติดตามสถานะได้ผ่านลิงก์ส่วนตัว</p></div></li>
</ol></div></section>

<section class="block"><div class="container">
<div class="section-head"><h2>เพิ่มลงหน้าจอหลัก เปิดสั่งได้เร็วเหมือนแอป</h2>
<p>ไม่ต้องโหลดจากสโตร์ กดเพิ่มไว้บนหน้าจอมือถือครั้งเดียว ครั้งต่อไปเปิดสั่งได้เลย</p></div>
<div class="grid grid-2">
<div class="card"><div class="icon">{ms("smartphone")}</div><h3>iPhone</h3>
<ol style="margin:0;padding-left:22px"><li>เปิดด้วย Safari</li><li>กดปุ่มแชร์</li><li>เลือก "เพิ่มไปยังหน้าจอโฮม"</li></ol></div>
<div class="card"><div class="icon">{ms("add_to_home_screen")}</div><h3>Android</h3>
<ol style="margin:0;padding-left:22px"><li>เปิดด้วย Chrome</li><li>กดเมนูจุดสามจุด</li><li>เลือก "เพิ่มลงในหน้าจอหลัก"</li></ol></div>
</div>
<p class="small muted" style="margin-top:12px">ชื่อปุ่มในมือถือบางรุ่นอาจต่างจากนี้เล็กน้อย</p>
</div></section>

<section class="block band"><div class="container" style="max-width:860px">
<div class="section-head"><h2>คำถามที่พบบ่อย</h2></div>
<div class="faq">
{faq("สั่งจากหลายร้านคิดค่าส่งอย่างไร?", "คิดค่าส่งครั้งเดียวต่อออเดอร์ ไม่ต้องจ่ายซ้ำทีละร้าน ค่าส่ง: " + PH['fee'])}
{faq("ส่งถึงที่ไหนบ้าง?", "ส่งในรัศมีไม่เกิน 7 กม. จากตลาดวิศิษฐ์ชัย (วัดเป็นเส้นตรง)")}
{faq("จ่ายเงินอย่างไร?", "ชำระล่วงหน้าผ่านพร้อมเพย์ตอนยืนยันออเดอร์ สแกน Thai QR ผ่านแอปธนาคาร")}
{faq("ของที่ขายตามน้ำหนักราคาเป็นอย่างไร?", "คิดตามน้ำหนักจริง ถ้าชั่งได้น้อยกว่าที่สั่ง เราคืนเงินส่วนต่างให้")}
{faq("ถ้าของที่สั่งหมด ทำอย่างไร?", PH['outofstock'])}
{faq("ยกเลิกออเดอร์และขอคืนเงินได้ไหม?", PH['cancel'])}
{faq("สั่งได้ถึงกี่โมง?", PH['cutoff'])}
</div></div></section>
{cta_end()}
'''
page('how-to-order.html', 'วิธีสั่งซื้อ | Hub2U',
     'สั่งของสดกับ Hub2U ง่ายๆ 4 ขั้นตอน เลือกของ จ่ายผ่านพร้อมเพย์ ทีมงานจัดของ ไรเดอร์ส่งถึงบ้าน', howto)

# ---------------------------------------------------------------- 03 delivery area
area = f'''
{page_head("พื้นที่จัดส่ง", "เช็กก่อนว่าบ้านคุณอยู่ในพื้นที่ที่เราส่งถึงไหม")}
<section class="block"><div class="container hero-grid">
<div>{map_svg()}</div>
<div>
<div class="callout"><p class="big">ส่งในรัศมีไม่เกิน 7 กม. จากตลาดวิศิษฐ์ชัย</p>
<p class="muted" style="margin:0">ระยะวัดเป็นเส้นตรงจากตลาด อาจต่างจากระยะตามถนนจริงเล็กน้อย</p></div>
<div class="card" style="margin-top:16px"><div class="icon">{ms("pin_drop")}</div><h3>ปักหมุดบ้านตอนสั่ง</h3>
<p>ตอนสั่ง ให้กดปักหมุดบ้านบนแผนที่ ไม่ต้องพิมพ์ที่อยู่ยาวๆ ไรเดอร์จะได้ไปถูกจุด</p></div>
</div></div></section>

<section class="block band"><div class="container" style="max-width:860px">
<div class="section-head"><h2>เวลารับออเดอร์และรอบส่ง</h2></div>
<ul class="contact-list">
<li>{ms("schedule")}<span>เวลารับออเดอร์: {PH['cutoff']}</span></li>
<li>{ms("local_shipping")}<span>รอบส่ง: {PH['rounds']}</span></li>
<li>{ms("event_busy")}<span>วันหยุด: {PH['daysoff']}</span></li>
<li>{ms("payments")}<span>ค่าส่ง: {PH['fee']} คิดครั้งเดียวต่อออเดอร์ ไม่ว่าจะสั่งจากกี่ร้านในออเดอร์เดียว</span></li>
</ul></div></section>

<section class="block"><div class="container" style="max-width:860px">
<div class="card"><h2>ไม่แน่ใจว่าบ้านอยู่ในพื้นที่ไหม</h2>
<p>ทักไลน์มาถามทีมงานก่อนสั่งได้ บอกชื่อหมู่บ้านหรือส่งหมุดบ้านมาให้เราดู</p>
<p class="muted">ตอนนี้เรายังส่งนอกรัศมี 7 กม. ไม่ได้</p>
<div class="btn-row">{line_btn()}</div></div></div></section>
{cta_end('พร้อมสั่งแล้ว หรือมีอะไรสงสัย')}
'''
page('delivery-area.html', 'พื้นที่จัดส่ง | Hub2U',
     'Hub2U ส่งของสดจากตลาดวิศิษฐ์ชัยถึงบ้านในรัศมีไม่เกิน 7 กม. เช็กก่อนสั่งว่าบ้านคุณอยู่ในพื้นที่ไหม', area)

# ---------------------------------------------------------------- 04 join us
join = f'''
{page_head("ร่วมงานกับเรา", "Hub2U เพิ่งเริ่มต้นที่ตลาดวิศิษฐ์ชัย มาเริ่มไปด้วยกันกับเรา")}
<section class="block"><div class="container"><div class="grid grid-2">
{card("storefront", "ร้านค้า/แผงในตลาด", "ขายของได้เพิ่ม โดยไม่ต้องทำแอปเอง สมัครฟรี ไม่มีค่าใช้จ่ายล่วงหน้า", '<div class="btn-row"><a class="btn btn-primary" href="shop-signup.html">สมัครร้านค้า</a></div>')}
{card("two_wheeler", "ไรเดอร์", "เลือกเวลาทำงานเองได้ สมัครผ่านมือถือ", '<div class="btn-row"><a class="btn btn-primary" href="rider-signup.html">สมัครไรเดอร์</a></div>')}
</div></div></section>

<section class="block band"><div class="container">
<div class="section-head center"><h2>สมัครแล้วเป็นอย่างไร</h2></div>
<div class="grid grid-3">
{card("verified_user", "ตรวจเอกสารก่อนเริ่มงานจริง", "ร้านค้าและไรเดอร์ทุกรายผ่านการตรวจเอกสารและรูปถ่ายก่อน")}
{card("lock", "ข้อมูลส่วนตัวเก็บเป็นความลับ", "ร้านค้าเห็นแค่รายการที่ต้องเตรียม ไม่เห็นชื่อ เบอร์ หรือที่อยู่ลูกค้า")}
{card("smartphone", "สมัครผ่านมือถือได้เลย", "ไม่ต้องเดินทางมาสมัคร")}
</div></div></section>

<section class="block"><div class="container center"><h2>มีคำถามก่อนสมัคร</h2>
<p>ยังไม่แน่ใจ ทักมาถามทีมงานก่อนได้</p>
<div class="btn-row" style="justify-content:center;max-width:320px;margin:20px auto 0">{line_btn()}</div></div></section>
'''
page('join-us.html', 'ร่วมงานกับเรา | Hub2U',
     'ร้านค้าในตลาดวิศิษฐ์ชัยและไรเดอร์ในพื้นที่บ้านบึง สมัครร่วมงานกับ Hub2U ผ่านมือถือได้เลย', join)

# ---------------------------------------------------------------- 05 shop signup
shop = f'''
<section class="hero"><div class="container"><h1>ขายของกับ Hub2U</h1>
<p class="lead">สำหรับแม่ค้าพ่อค้าในตลาดวิศิษฐ์ชัย ขายของได้เพิ่ม โดยไม่ต้องทำแอปเอง</p>
<div class="btn-row" style="max-width:320px">{btn("สมัครร้านค้า", link="shop", icon="storefront")}</div></div></section>

<section class="block band"><div class="container">
<div class="section-head"><h2>ทำไมแผงของคุณควรอยู่กับ Hub2U</h2></div>
<div class="grid grid-4">
{card("savings", "สมัครฟรี ไม่มีค่าใช้จ่ายล่วงหน้า", "ไม่ต้องจ่ายค่าสมัคร เริ่มได้เลย")}
{card("toggle_on", "เปิด-ปิดร้านเองได้", "กดเปิดตอนพร้อมขาย กดปิดตอนพัก")}
{card("inventory_2", "แจ้งของหมดได้ทันที", "ไม่ต้องกลัวลูกค้าสั่งของที่ไม่มี")}
{card("qr_code_2", "QR ประจำร้าน", "ให้ลูกค้าประจำสแกนสั่งจากร้านคุณโดยตรง")}
</div></div></section>

<section class="block"><div class="container hero-grid">
<div class="card"><div class="icon">{ms("handshake")}</div><h3>ลูกค้าประจำที่ไม่สะดวกมาตลาด</h3>
<p>ลูกค้าประจำที่ไม่มีเวลามาตลาด ก็สั่งจากแผงคุณได้ ทีมงานช่วยเลือกของและไรเดอร์ช่วยส่งให้</p>
<p>ถ้ามีลูกค้าประจำที่อยากให้ส่งของ แผงคุณเรียกไรเดอร์ส่งได้เอง</p></div>
<div class="card"><div class="icon">{ms("receipt_long")}</div><h3>ค่าธรรมเนียมการขาย</h3>
<p>ค่าธรรมเนียมการขาย {PH['shopfee']} หักจากยอดที่ขายได้เท่านั้น ไม่ขายได้ไม่เสีย</p>
<p>ดูยอดเงินที่จะได้รับในระบบได้ชัดเจน</p>
<p>รอบจ่ายเงินร้านค้า: {PH['shoppay']}</p></div>
</div></section>

<section class="block band"><div class="container" style="max-width:860px">
<div class="callout"><p class="big">ข้อมูลลูกค้าเป็นความลับ</p>
<p style="margin:0">ร้านค้าเห็นแค่รายการที่ต้องเตรียม ไม่เห็นชื่อ เบอร์ หรือที่อยู่ลูกค้า ส่วนการจัดส่ง ทีมงานและไรเดอร์ดูแลให้</p></div></div></section>

<section class="block"><div class="container">
<div class="section-head center"><h2>สมัครง่ายๆ 3 ขั้นตอน</h2></div>
<ol class="steps" style="max-width:760px;margin:0 auto">
<li><div><h3>กรอกข้อมูลร้าน</h3><p>สมัครผ่านมือถือ ไม่ต้องเดินทาง</p></div></li>
<li><div><h3>เราตรวจเอกสารและรูปถ่าย</h3><p>เอกสารที่ต้องใช้ {PH['shopdocs']}</p></div></li>
<li><div><h3>เริ่มขายได้</h3><p>ตั้งสินค้าและกดเปิดร้านเมื่อพร้อม</p></div></li>
</ol></div></section>

<section class="block band"><div class="container center" style="max-width:560px">
<div class="btn-row">{btn("สมัครร้านค้า", link="shop", icon="storefront")}</div>
<p style="margin-top:12px">{CONSENT[3:-4]}</p></div></section>

<section class="block"><div class="container center"><h2>ถามก่อนสมัคร</h2>
<p>ยังไม่แน่ใจ ทักมาคุยกับทีมงานก่อนได้</p>
<div class="btn-row" style="justify-content:center;max-width:320px;margin:20px auto 0">{line_btn()}</div></div></section>
'''
page('shop-signup.html', 'สมัครร้านค้า | Hub2U',
     'แผงในตลาดวิศิษฐ์ชัยสมัครขายของกับ Hub2U ฟรี ไม่มีค่าใช้จ่ายล่วงหน้า เปิด-ปิดร้านเองได้ สมัครผ่านมือถือ', shop)

# ---------------------------------------------------------------- 06 rider signup
rider = f'''
<section class="hero"><div class="container"><h1>ขับส่งของกับ Hub2U</h1>
<p class="lead">สำหรับคนในพื้นที่บ้านบึงที่มีมอเตอร์ไซค์ เลือกเวลาทำงานเองได้</p>
<div class="btn-row" style="max-width:320px">{btn("สมัครไรเดอร์", link="rider", icon="two_wheeler")}</div></div></section>

<section class="block band"><div class="container">
<div class="section-head"><h2>ทำไมต้องขับกับ Hub2U</h2></div>
<div class="grid grid-4">
{card("schedule", "เลือกเวลาทำงานเอง", "ว่างตอนไหน ออกรับงานตอนนั้น")}
{card("assignment", "รับงานได้ 2 แบบ", "กดรับงานเองจากกระดานงาน หรือรับงานที่ทีมงานในตลาดจ่ายให้")}
{card("undo", "คืนงานได้ก่อนออกเดินทาง", "ถ้าติดธุระ กดคืนงานได้ก่อนเริ่มส่ง")}
{card("bar_chart", "ดูรายได้ในระบบ", "ดูรายได้สะสมได้เอง ตรวจสอบได้")}
</div></div></section>

<section class="block"><div class="container hero-grid">
<div class="card"><div class="icon">{ms("payments")}</div><h3>ค่ารอบส่ง</h3>
<p>ค่ารอบต่อเที่ยว {PH['riderrate']} ไม่ถูกหักค่าคอมมิชชัน</p>
<p>รอบจ่ายเงินไรเดอร์: {PH['riderpay']}</p></div>
<div class="card"><div class="icon">{ms("checklist")}</div><h3>คุณสมบัติที่ต้องมี</h3>
<ul class="check"><li>{ms("check_circle")}มีมอเตอร์ไซค์</li><li>{ms("check_circle")}อยู่ในพื้นที่ให้บริการ</li><li>{ms("check_circle")}มีสมาร์ทโฟน</li><li>{ms("check_circle")}เอกสารที่ต้องใช้: {PH['riderdocs']}</li></ul></div>
</div></section>

<section class="block band"><div class="container">
<div class="section-head center"><h2>สมัครง่ายๆ 3 ขั้นตอน</h2></div>
<ol class="steps" style="max-width:760px;margin:0 auto">
<li><div><h3>กรอกข้อมูลผ่านมือถือ</h3><p>ชื่อ เบอร์โทร และรายละเอียดรถ</p></div></li>
<li><div><h3>เราตรวจเอกสารและรูปถ่าย</h3><p>ตรวจก่อนเริ่มงานจริง</p></div></li>
<li><div><h3>เริ่มรับงานได้</h3><p>เมื่อผ่านการตรวจ</p></div></li>
</ol></div></section>

<section class="block"><div class="container center" style="max-width:560px">
<div class="btn-row">{btn("สมัครไรเดอร์", link="rider", icon="two_wheeler")}</div>
<p style="margin-top:12px">{CONSENT[3:-4]}</p></div></section>

<section class="block band"><div class="container center"><h2>ถามก่อนสมัคร</h2>
<p>อยากถามเรื่องเวลางานหรือค่ารอบก่อน ทักมาได้</p>
<div class="btn-row" style="justify-content:center;max-width:320px;margin:20px auto 0">{line_btn()}</div></div></section>
'''
page('rider-signup.html', 'สมัครไรเดอร์ | Hub2U',
     'ไรเดอร์ในพื้นที่บ้านบึงที่มีมอเตอร์ไซค์ สมัครส่งของสดกับ Hub2U เลือกเวลาทำงานเองได้ สมัครผ่านมือถือ', rider)

# ---------------------------------------------------------------- 07 about
about = f'''
{page_head("เกี่ยวกับเรา", "Hub2U ของสดจากตลาดวิศิษฐ์ชัย ส่งถึงบ้านคุณ")}
<section class="block"><div class="container hero-grid">
<div class="photo-ph" data-image="aboutPhoto" data-alt="เจ้าของและทีมงาน Hub2U"><span class="ph">[ใส่รูปเจ้าของหรือทีมงาน]</span></div>
<div><h2>เรื่องราวของเรา</h2>
<p>Hub2U เริ่มต้นจากตลาดวิศิษฐ์ชัย บ้านบึง เรารวมของจากร้านในตลาดให้สั่งได้ในที่เดียว ทีมงานในตลาดเลือกและจัดของให้ แล้วไรเดอร์ในพื้นที่ส่งถึงหน้าบ้าน</p>
<p>{PH['story']}</p>
<p>เราเพิ่งเริ่มต้น และอยากทำให้ดีไปพร้อมกับคนในชุมชน</p></div>
</div></section>

<section class="block band"><div class="container">
<div class="section-head center"><h2>เราทำอะไร</h2></div>
<div class="grid grid-3">
{card("shopping_basket", "เลือกของจากตลาด", "สั่งของสดจากร้านในตลาดวิศิษฐ์ชัยผ่านมือถือ")}
{card("inventory_2", "ทีมในตลาดจัดของให้", "เลือกของ ชั่งน้ำหนัก จัดใส่ถุงเดียว")}
{card("two_wheeler", "ไรเดอร์ส่งถึงบ้าน", "ส่งถึงจุดที่คุณปักหมุดไว้")}
</div></div></section>

<section class="block"><div class="container">
<div class="section-head center"><h2>ทำไมไว้ใจได้</h2></div>
<div class="grid grid-3">
{card("verified_user", "ตรวจเอกสารก่อนเริ่มงานจริง", "ร้านค้าและไรเดอร์ทุกรายผ่านการตรวจเอกสารและรูปถ่าย")}
{card("lock", "ข้อมูลส่วนตัวเก็บเป็นความลับ", "ร้านค้าไม่เห็นชื่อ เบอร์ หรือที่อยู่ลูกค้า")}
{card("smartphone", "เปิดผ่านมือถือได้เลย", "ไม่ต้องโหลดจากสโตร์ กดเพิ่มลงหน้าจอหลักได้")}
</div></div></section>

<section class="block band"><div class="container"><div class="grid grid-2">
<img class="photo" src="assets/img/market-vendor.jpg" width="1200" height="670" alt="แม่ค้าในตลาดสดยิ้มแย้ม ถือถั่วฝักยาว" loading="lazy">
<img class="photo" src="assets/img/hero-doorstep.jpg" width="1200" height="896" alt="ถุงของสดวางอยู่หน้าบ้าน" loading="lazy">
</div></div></section>

<section class="block"><div class="container center"><h2>อยากให้เราช่วยเรื่องอะไร ทักมาได้เลย</h2>
<div class="btn-row" style="justify-content:center;max-width:520px;margin:20px auto 0">{order_btn()}{line_btn()}</div></div></section>
'''
page('about.html', 'เกี่ยวกับเรา | Hub2U',
     'Hub2U บริการส่งของสดจากตลาดวิศิษฐ์ชัย บ้านบึง ชลบุรี ทีมงานในตลาดจัดของ ไรเดอร์ในพื้นที่ส่งถึงบ้าน', about)

# ---------------------------------------------------------------- 08 contact
contact = f'''
<section class="hero"><div class="container"><h1>ติดต่อเรา</h1>
<p class="lead">ทักมาได้ทุกเรื่อง ทางไลน์สะดวกที่สุด</p>
<div class="btn-row" style="max-width:520px">{btn("คุยกับเราทางไลน์", "contact.html", "primary", "chat", link="line", block=True)}</div></div></section>

<section class="block band"><div class="container hero-grid">
<div><h2>ช่องทางติดต่อ</h2>
<ul class="contact-list">
<li>{ms("chat")}<span>ไลน์: {PH['lineId']}</span></li>
<li>{ms("call")}<span>โทร: <a data-tel href="contact.html">{PH['phone']}</a></span></li>
<li>{ms("schedule")}<span>เวลาทำการ: {PH['hours']}</span></li></ul></div>
<div class="qr-box" data-image="lineQrImage" data-alt="QR ไลน์ Hub2U"><span>QR ไลน์<br><span class="ph small">[ใส่ QR ไลน์]</span></span></div>
</div></section>

<section class="block"><div class="container hero-grid">
<div><h2>จุดรวมของในตลาด</h2>
<p>ทีมงานของเราคัดและจัดของใส่ถุงที่ตลาดวิศิษฐ์ชัย อำเภอบ้านบึง จังหวัดชลบุรี ก่อนไรเดอร์นำส่งถึงบ้าน</p>
<p>ตำแหน่ง: {PH['hub']}</p>
<p class="muted">ตอนนี้เรายังไม่เปิดให้มารับของที่ตลาดเอง ส่งถึงบ้านอย่างเดียว</p></div>
<div>{map_svg('แผนที่ภาพประกอบ ตลาดวิศิษฐ์ชัยอยู่ตรงกลาง')}</div>
</div></section>

<section class="block band"><div class="container">
<div class="section-head center"><h2>เรื่องที่ทักมาได้บ่อย</h2></div>
<div class="grid grid-4">
{card("receipt_long", "ถามเรื่องออเดอร์", "")}
{card("map", "ถามพื้นที่จัดส่ง", "")}
{card("storefront", "สมัครร้านค้า", "")}
{card("two_wheeler", "สมัครไรเดอร์", "")}
</div></div></section>
{cta_end('พร้อมสั่งแล้ว หรืออยากคุยก่อน')}
'''
page('contact.html', 'ติดต่อเรา | Hub2U',
     'ติดต่อ Hub2U ทางไลน์ สอบถามเรื่องสั่งของสด พื้นที่จัดส่ง หรือสมัครเป็นร้านค้าและไรเดอร์', contact)

# ---------------------------------------------------------------- 09 order now
ordernow = f'''
<section class="hero"><div class="container"><h1>สั่งของสด</h1>
<p class="lead">เลือกของจากตลาดวิศิษฐ์ชัย แล้วรอรับที่บ้าน</p>
<div class="btn-row" style="max-width:420px">{btn("เปิดหน้าสั่งของ", "#", "primary", "shopping_basket", link="app", block=True)}</div>
<p class="small muted" style="margin-top:10px">ลิงก์เว็บแอป: {ph('appUrlNote', '[ใส่ลิงก์เว็บแอป]')}</p></div></section>

<section class="block band"><div class="container" style="max-width:860px">
<div class="section-head"><h2>ก่อนสั่ง รู้ไว้นิดเดียว</h2></div>
<ul class="contact-list">
<li>{ms("map")}<span>ส่งในรัศมีไม่เกิน 7 กม. จากตลาด (วัดเป็นเส้นตรง)</span></li>
<li>{ms("pin_drop")}<span>ปักหมุดบ้านบนแผนที่ ไม่ต้องพิมพ์ที่อยู่ยาวๆ</span></li>
<li>{ms("payments")}<span>จ่ายล่วงหน้าผ่านพร้อมเพย์ตอนยืนยันออเดอร์</span></li>
</ul></div></section>

<section class="block"><div class="container">
<div class="section-head"><h2>เพิ่มลงหน้าจอหลัก เปิดสั่งได้เร็วเหมือนแอป</h2>
<p>ไม่ต้องโหลดจากสโตร์ กดเพิ่มไว้ครั้งเดียว ครั้งต่อไปเปิดสั่งได้เลย</p></div>
<div class="grid grid-2">
<div class="card"><div class="icon">{ms("smartphone")}</div><h3>iPhone</h3>
<ol style="margin:0;padding-left:22px"><li>เปิดด้วย Safari</li><li>กดปุ่มแชร์</li><li>เลือก "เพิ่มไปยังหน้าจอโฮม"</li></ol></div>
<div class="card"><div class="icon">{ms("add_to_home_screen")}</div><h3>Android</h3>
<ol style="margin:0;padding-left:22px"><li>เปิดด้วย Chrome</li><li>กดเมนูจุดสามจุด</li><li>เลือก "เพิ่มลงในหน้าจอหลัก"</li></ol></div>
</div>
<p class="small muted" style="margin-top:12px">ชื่อปุ่มในมือถือบางรุ่นอาจต่างจากนี้เล็กน้อย</p>
</div></section>

<section class="block band"><div class="container center"><h2>สั่งไม่ได้ หรือติดขัดตรงไหน</h2>
<p>ทักมาถามทีมงานได้เลย</p>
<div class="btn-row" style="justify-content:center;max-width:320px;margin:20px auto 0">{line_btn()}</div></div></section>
'''
page('order-now.html', 'สั่งของสด | Hub2U',
     'สั่งของสดจากตลาดวิศิษฐ์ชัยผ่านมือถือ จ่ายผ่านพร้อมเพย์ ส่งถึงบ้านในรัศมี 7 กม. จากตลาด', ordernow)

# ---------------------------------------------------------------- 404
nf = f'''
{page_head("ไม่พบหน้านี้", "หน้าที่คุณเปิดอาจย้ายหรือพิมพ์ลิงก์ไม่ตรง")}
<section class="block"><div class="container"><div class="btn-row" style="max-width:420px"><a class="btn btn-primary" href="index.html">กลับหน้าแรก</a></div></div></section>
'''
page('404.html', 'ไม่พบหน้านี้ | Hub2U', 'ไม่พบหน้าที่คุณต้องการ กลับไปหน้าแรกของ Hub2U', nf, current='none')
print('built', len([f for f in os.listdir(ROOT) if f.endswith('.html')]), 'pages')
