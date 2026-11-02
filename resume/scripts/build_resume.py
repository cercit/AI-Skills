"""Build a tailored resume PDF from a job folder's resume.json, then check it.

Usage:  python build_resume.py <profile.json> <job-folder>

Reads   <profile.json>               (your fixed details: name, contact, education...)
        <job-folder>/resume.json     (the tailored content for one job)
        <job-folder>/jd.txt          (optional, kept next to it for reference)
Writes  resume.html, <file_name>.pdf and check-report.md in the job folder.

Checks: 2 pages max (tightens spacing up to 4 times), JD keywords found,
forbidden phrases, banned AI words, em dashes.

Needs:  pip install playwright pymupdf  &&  playwright install chromium
"""
import html
import json
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

BANNED = re.compile(r"\b(delve\w*|leverag\w*|utili[sz]\w*|facilitat\w*|comprehensive|robust|seamless\w*|cutting-edge|"
                    r"innovative|game-changer|revolutioni[sz]\w*|empower\w*|harness\w*|paradigm|synerg\w*|foster\w*|"
                    r"spearhead\w*|bolster\w*|crucial|vital|pivotal|showcas\w*|tapestry|testament|underscor\w*|"
                    r"passionate|dynamic|results-driven|go-getter|proven track record)\b", re.I)

# spacing steps: (line-height, section gap px, top margin mm)
STEPS = [(1.38, 11, 14), (1.33, 9, 12), (1.30, 8, 11), (1.27, 7, 10), (1.24, 6, 9)]

e = html.escape


def link(url):
    href = url if url.startswith("http") else "https://" + url
    return f'<a href="{e(href)}">{e(url)}</a>'


def contact_line(items):
    # items: plain text, emails and URLs; emails and URLs become links
    out = []
    for it in items:
        if "@" in it and " " not in it:
            out.append(f'<a href="mailto:{e(it)}">{e(it)}</a>')
        elif "." in it and " " not in it and not it.replace("+", "").replace(" ", "").isdigit():
            out.append(link(it))
        else:
            out.append(e(it))
    return " | ".join(out)


def render(prof, d, step):
    lh, gap, top = step
    css = f"""
@page {{ size: A4; margin: {top}mm 15mm 11mm 15mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: Calibri, Carlito, Arial, sans-serif; color: #111; font-size: 9.4pt; line-height: {lh}; margin: 0; }}
h1 {{ font-size: 21pt; margin: 0 0 3px; }}
.role {{ font-weight: bold; margin: 0; }}
.contact {{ color: #333; font-size: 9pt; margin: 1px 0 0; }}
a {{ color: #0b57b0; }}
h2 {{ font-size: 10pt; letter-spacing: 2.2px; text-transform: uppercase; margin: {gap}px 0 {max(3, gap // 2)}px; padding-bottom: 3px; border-bottom: 1px solid #bbb; }}
p {{ margin: 0 0 3px; }}
.row {{ display: flex; justify-content: space-between; gap: 12px; font-weight: bold; margin: 6px 0 2px; }}
.row span:last-child {{ font-weight: normal; color: #333; white-space: nowrap; }}
ul {{ margin: 2px 0 3px 18px; padding: 0; }}
li {{ margin-bottom: 2px; }}
.co {{ font-weight: bold; margin: 5px 0 3px; }}
.keep {{ break-inside: avoid; }}
"""
    name = prof["name"]
    out = [f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Resume {e(name)}</title><style>{css}</style></head><body>",
           f"<h1>{e(name)}</h1>",
           f"<p class='role'>{e(d.get('role_line', prof.get('default_role_line', '')))}</p>",
           f"<p class='contact'>{contact_line(prof['contact'])}</p>",
           "<h2>Summary</h2>", *[f"<p>{e(x)}</p>" for x in d["summary"]],
           "<h2>Skills</h2>", *[f"<p><b>{e(k)}:</b> {e(v)}</p>" for k, v in d["skills"]],
           "<h2>Tools</h2>", f"<p>{e(d['tools'])}</p>"]

    def experience():
        o = ["<h2>Experience</h2>"]
        if prof.get("company_line"):
            o.append(f"<p class='co'>{e(prof['company_line'])}</p>")
        for j in d["experience"]:
            o.append("<div class='keep'>")
            o.append(f"<div class='row'><span>{e(j['title'])}</span><span>{e(j['dates'])}</span></div>")
            if j.get("intro"):
                o.append(f"<p>{e(j['intro'])}</p>")
            if j.get("bullets"):
                o.append("<ul>" + "".join(f"<li>{e(b)}</li>" for b in j["bullets"]) + "</ul>")
            o.append("</div>")
        return o

    def portfolio():
        o = ["<h2>Portfolio</h2>"]
        for p in d.get("portfolio", []):
            o.append("<div class='keep'>")
            o.append(f"<div class='row'><span>{e(p['name'])}</span><span>{e(p.get('date', ''))}</span></div>")
            if p.get("link"):
                o.append(f"<p>{link(p['link'])}</p>")
            o.append("<ul>" + "".join(f"<li>{e(b)}</li>" for b in p["bullets"]) + "</ul></div>")
        return o

    for part in d.get("order", ["experience", "portfolio"]):
        out += experience() if part == "experience" else portfolio()
    out.append("<h2>Education</h2>")
    for ed in prof.get("education", []):
        out.append(f"<div class='row'><span>{e(ed['title'])}</span><span>{e(ed['dates'])}</span></div><p>{e(ed['place'])}</p>")
    if d.get("certifications", prof.get("certifications")):
        out += ["<h2>Certifications</h2>", f"<p>{e(d.get('certifications', prof.get('certifications')))}</p>"]
    if prof.get("languages"):
        out += ["<h2>Languages</h2>", f"<p>{e(prof['languages'])}</p>"]
    if prof.get("hobbies"):
        out += ["<h2>Hobbies</h2>", f"<p>{e(prof['hobbies'])}</p>"]
    out.append("</body></html>")
    return "\n".join(out)


def main(profile_path, folder):
    prof = json.loads(Path(profile_path).read_text(encoding="utf-8"))
    folder = Path(folder).resolve()
    d = json.loads((folder / "resume.json").read_text(encoding="utf-8"))
    pdf = folder / f"{d['file_name']}.pdf"
    page_html = folder / "resume.html"
    pages, text = 0, ""
    import pymupdf
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for step in STEPS:
            page_html.write_text(render(prof, d, step), encoding="utf-8")
            page = browser.new_page()
            page.goto(page_html.as_uri())
            page.wait_for_timeout(300)
            page.pdf(path=str(pdf), format="A4", print_background=True, prefer_css_page_size=True)
            page.close()
            doc = pymupdf.open(str(pdf))
            pages = len(doc)
            text = "\n".join(pg.get_text() for pg in doc)
            doc.close()
            if pages <= 2:
                break
        browser.close()

    flat = re.sub(r"\s+", " ", text)
    report = [f"# Check report: {d['file_name']}", "", f"- Pages: **{pages}** {'OK' if pages <= 2 else 'OVER 2 PAGES: cut content'}"]
    kws = d.get("jd_keywords", [])
    hit = [k for k in kws if k.lower() in flat.lower()]
    miss = [k for k in kws if k.lower() not in flat.lower()]
    report.append(f"- JD keywords found: **{len(hit)}/{len(kws)}**")
    if miss:
        report.append(f"- Missing keywords: {', '.join(miss)}")
    forb = [f for f in prof.get("forbidden_phrases", []) if f.lower() in flat.lower()]
    report.append(f"- Forbidden phrases: {', '.join(forb) if forb else 'none'}")
    banned = sorted({m.group(0).lower() for m in BANNED.finditer(flat)})
    report.append(f"- Banned AI words: {', '.join(banned) if banned else 'none'}")
    report.append(f"- Em dashes: {flat.count('—')}")
    (folder / "check-report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))
    print("PDF:", pdf)
    ok = pages <= 2 and not forb and not banned
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python build_resume.py <profile.json> <job-folder>")
    main(sys.argv[1], sys.argv[2])
