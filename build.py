"""Build index.html (Thai) and en.html (English) from src/page.html.

Edit terminal data and wording here, then run:  python build.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent

UI = {
    "th": {
        "eyebrow": "Thai Ports · Laem Chabang · Bangkok · UNITHAI",
        "h1": "ลิงก์เว็บไซต์ท่าเรือ",
        "lede": "รวมเว็บไซต์ ลิงก์ Open Gate ตารางเรือ และเบอร์โทรของท่าเรือแหลมฉบัง ท่าเรือกรุงเทพ และท่าเรือ UNITHAI ไว้ในที่เดียว",
        "clock": "เวลาท่าเรือ (ICT)",
        "map_title": "แผนผังท่าเรือ",
        "map_hint": "กดที่ท่าเพื่อไปยังข้อมูลติดต่อ",
        "lcb_name": "ท่าเรือแหลมฉบัง",
        "river_name": "แม่น้ำเจ้าพระยา",
        "bkp_short": "ท่าเรือกรุงเทพ",
        "list_title": "ท่าเรือและท่าเทียบเรือ",
        "search_label": "ค้นหาท่า",
        "search_ph": "ค้นหาชื่อท่า รหัสท่า หรือเบอร์โทร เช่น LCIT, B3, UTCT",
        "empty": "ไม่พบท่าที่ตรงกับคำค้นหา ลองพิมพ์รหัสท่า เช่น A0 หรือ UTCT",
        "foot_src": "ข้อมูลท่าเรือ:",
        "foot_pat": "การท่าเรือแห่งประเทศไทย",
        "foot_note": "เบอร์โทรเป็นเบอร์กลางของแต่ละท่า",
        "js": {"website": "เว็บไซต์", "phone": "โทรศัพท์", "copy": "คัดลอก", "copyPhone": "คัดลอกเบอร์",
               "openSite": "เปิดเว็บไซต์", "copyLink": "คัดลอกลิงก์", "copied": "คัดลอกแล้ว", "pressCopy": "กด Ctrl+C"},
        "groups": {"lcb": {"name": "ท่าเรือแหลมฉบัง", "sub": "ชลบุรี · THLCH"},
                   "bkk": {"name": "ท่าเรือกรุงเทพ และท่าเรือ UNITHAI", "sub": "แม่น้ำเจ้าพระยา · THBKK"}},
    },
    "en": {
        "eyebrow": "Thai Ports · Laem Chabang · Bangkok · UNITHAI",
        "h1": "Port Website Links",
        "lede": "Websites, Open Gate and vessel schedules, and phone numbers for Laem Chabang Port, Bangkok Port and UNITHAI terminal in one place.",
        "clock": "Port time (ICT)",
        "map_title": "Port map",
        "map_hint": "Select a terminal to jump to its contacts",
        "lcb_name": "Laem Chabang Port",
        "river_name": "Chao Phraya River",
        "bkp_short": "Bangkok Port",
        "list_title": "Ports and terminals",
        "search_label": "Search terminals",
        "search_ph": "Search by name, berth or phone, e.g. LCIT, B3, UTCT",
        "empty": "No terminal matches your search. Try a code such as A0 or UTCT.",
        "foot_src": "Port information:",
        "foot_pat": "Port Authority of Thailand",
        "foot_note": "Phone numbers are each terminal's main line.",
        "js": {"website": "Website", "phone": "Phone", "copy": "Copy", "copyPhone": "Copy phone",
               "openSite": "Open website", "copyLink": "Copy link", "copied": "Copied", "pressCopy": "Press Ctrl+C"},
        "groups": {"lcb": {"name": "Laem Chabang Port", "sub": "Chonburi · THLCH"},
                   "bkk": {"name": "Bangkok Port and UNITHAI", "sub": "Chao Phraya River · THBKK"}},
    },
}

# Each terminal: text fields are {"th": ..., "en": ...} or a plain string used for both.
TERMINALS = [
    {"id": "lcmt", "group": "lcb", "code": "LCMT", "color": "var(--c-lcmt)", "markLabel": "BERTH", "mark": "A0",
     "name": "LCMT Co., Ltd.",
     "desc": {"th": "บริษัทในเครือ LCB1 ดำเนินการท่าเทียบเรือ A0", "en": "LCB1 subsidiary operating berth A0."},
     "url": "https://www.lcb1.com/Home", "tel": "038-408-600",
     "links": [{"kind": "gate", "label": "Open Gate", "url": "https://www.lcb1.com/opengate/"}]},
    {"id": "hpt", "group": "lcb", "code": "HPT", "color": "var(--c-hpt)", "markLabel": "BERTH", "mark": "A3",
     "name": "Hutchison Ports Thailand",
     "desc": {"th": "ท่าเทียบเรืออเนกประสงค์ A3 รองรับตู้สินค้าและสินค้าทั่วไป", "en": "Multipurpose terminal A3 handling containers and general cargo."},
     "url": "https://hutchisonports.co.th/terminal-a3/", "tel": "038-408-700",
     "links": [{"kind": "gate", "label": "Open Gate", "url": "https://online.hutchisonports.co.th/hptpcs/f?p=114:17"}]},
    {"id": "esco", "group": "lcb", "code": "ESCO", "color": "var(--c-esco)", "markLabel": "BERTH", "mark": "B3",
     "name": "Eastern Sea Laem Chabang Terminal",
     "desc": {"th": "ท่าเทียบเรือตู้สินค้า B3 เปิดบริการ 24 ชั่วโมง", "en": "Container terminal B3, open 24 hours."},
     "url": "https://www.esco.co.th", "tel": "033-005-678",
     "links": [{"kind": "gate", "label": "Open Gate", "url": "https://service.esco.co.th/BerthSchedule"}]},
    {"id": "lcit", "group": "lcb", "code": "LCIT", "color": "var(--c-lcit)", "markLabel": "BERTH", "mark": "B5 / C3",
     "name": "Laem Chabang International Terminal",
     "desc": {"th": "ท่าเทียบเรือตู้สินค้า B5 และ C3", "en": "Container terminals B5 and C3."},
     "url": "https://www.lcit.com", "tel": "038-408-200",
     "links": [{"kind": "gate", "label": "Open Gate", "url": "https://www.lcit.com/checkopengate"}]},
    {"id": "bkp", "group": "bkk", "code": "BKP", "color": "var(--c-bkp)", "markLabel": "PORT", "mark": "KLONG TOEY",
     "name": {"th": "ท่าเรือกรุงเทพ (การท่าเรือแห่งประเทศไทย)", "en": "Bangkok Port (Port Authority of Thailand)"},
     "desc": {"th": "ท่าเรือคลองเตย ริมแม่น้ำเจ้าพระยา ดำเนินการโดยการท่าเรือแห่งประเทศไทย",
              "en": "Klong Toey port on the Chao Phraya River, run by the Port Authority of Thailand."},
     "url": "https://bkpiservice.port.co.th", "tel": "02-269-3537",
     "links": [{"kind": "schedule", "label": {"th": "ตารางเรือเข้า-ออก", "en": "Vessel schedule"},
                "url": "https://www.port.co.th/port/index.php/vesselentryexit-2/"},
               {"kind": "dashboard", "label": {"th": "Ship Operation Dashboard", "en": "Ship Operation Dashboard"},
                "url": "https://datastudio.google.com/reporting/473cd015-edbb-4011-a58c-b9b2d55090fb/page/xm5rF"}]},
    {"id": "utct", "group": "bkk", "code": "UTCT", "color": "var(--c-utct)", "markLabel": "PORT", "mark": "SAMUT PRAKAN",
     "name": "Unithai Container Terminal (UTCT)",
     "desc": {"th": "ท่าเทียบเรือตู้สินค้าของ UNITHAI ที่สมุทรปราการ ปากแม่น้ำเจ้าพระยา",
              "en": "UNITHAI container terminal in Samut Prakan, at the mouth of the Chao Phraya River."},
     "url": "https://www.unithai.com/services/shipping-logistics/container-terminal/", "tel": "02-755-6888",
     "links": [{"kind": "schedule", "label": {"th": "ตารางเรือ", "en": "Vessel schedule"},
                "url": "https://utctterminal.unithai.com/publishtrg/shSchedule.aspx"},
               {"kind": "track", "label": {"th": "ติดตามตู้", "en": "Container tracking"},
                "url": "https://utctterminal.unithai.com/publishtrg/ctTracking.aspx"}]},
]


def pick(v, lang):
    if isinstance(v, dict) and set(v) == {"th", "en"}:
        return v[lang]
    if isinstance(v, dict):
        return {k: pick(x, lang) for k, x in v.items()}
    if isinstance(v, list):
        return [pick(x, lang) for x in v]
    return v


def build(lang, out):
    page = (ROOT / "src" / "page.html").read_text(encoding="utf-8")
    ui = UI[lang]
    values = {k: v for k, v in ui.items() if isinstance(v, str)}
    values.update({
        "lang": lang,
        "cur_th": ' aria-current="page"' if lang == "th" else "",
        "cur_en": ' aria-current="page"' if lang == "en" else "",
        "ui_json": json.dumps(ui["js"], ensure_ascii=False),
        "groups_json": json.dumps(ui["groups"], ensure_ascii=False),
        "terminals_json": json.dumps(pick(TERMINALS, lang), ensure_ascii=False, indent=1),
    })
    for k, v in values.items():
        page = page.replace("{{" + k + "}}", v)
    assert "{{" not in page.replace("{{@", ""), "unfilled placeholder"
    (ROOT / out).write_text(page, encoding="utf-8")
    print("wrote", out)


build("th", "index.html")
build("en", "en.html")
