---
name: a5-coin
description: Generates print-ready A5 Filofax binder coin collection checklists as PDF. ALWAYS activate when the user asks for a printable coin checklist, binder insert, coin collection PDF, A5 coin list, or anything combining "coin" + "print" / "binder" / "checklist" / "PDF". Also activate when iterating on an existing coin checklist PDF — reformatting, adding series, fixing layout. This skill encodes hard-won formatting rules for ReportLab on A5 paper with 6-hole punch margins, grayscale laser printing, and Carlito (Calibri-equivalent) font.
---

# A5 Coin Checklist PDF Generator

## When to use
- User wants a printable coin collection checklist
- User mentions A5, Filofax, binder, or planner pages for coins
- User wants to cross-reference a Numista export against a series master list
- User is iterating on a previously generated coin checklist PDF

## Page Setup

```python
from reportlab.lib.pagesizes import A5
PAGE_W, PAGE_H = A5  # 148mm x 210mm (419.53 x 595.28 pts)

LEFT_M = 18*mm    # WIDER — clears 6-hole Filofax punch
RIGHT_M = 6*mm
TOP_M = 9*mm
BOT_M = 8*mm
USABLE_W = PAGE_W - LEFT_M - RIGHT_M  # ~124mm
```

## 6-Hole Punch Guides

Draw on every page. Filofax A5 standard hole positions from top edge:

```python
HOLE_POSITIONS_MM = [19, 51, 70, 140, 159, 191]
for h in HOLE_POSITIONS_MM:
    y = PAGE_H - h*mm
    c.setStrokeColor(HexColor("#CCCCCC"))
    c.setLineWidth(0.25)
    c.circle(4.5*mm, y, 2.2*mm, stroke=1, fill=0)
```

## Font

Use **Carlito** (metric-compatible with Calibri, free under the SIL Open Font License). On Linux it is usually at:
```
/usr/share/fonts/truetype/crosextra/Carlito-Regular.ttf
/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf
/usr/share/fonts/truetype/crosextra/Carlito-Italic.ttf
```
On Windows or macOS, download Carlito from Google Fonts and point to those files instead.

Register all three variants. Never fall back to Helvetica: the layout below is tuned for Calibri-style metrics.

## Typography Rules (HARD CONSTRAINTS)

| Element | Font | Size | Notes |
|---------|------|------|-------|
| Cover title | Carlito-Bold | 20pt | Centered in black banner |
| Cover subtitle | Carlito-Bold | 16pt | Below title |
| Section headers | Carlito-Bold | 8.5-9pt | White on black bar |
| Column headers | Carlito-Bold | 7.5pt | Grey, above separator line |
| **Body text — ALL columns** | Carlito / Carlito-Bold | **11pt** | Uniform across Name, Period, Now |
| Collected detail line | Carlito-Italic | 8.5pt | Grey, below collected row |
| Footer | Carlito | 6pt | Page number + checklist name |
| Face value column | Carlito | 9pt | Right-aligned, abbreviated (5Y, 10Y, 1J) |

**Critical: Keep Name, Period, and Now columns at the SAME font size (11pt).** Mixed sizes look unprofessional on a printed page.

## Row Layout

```python
ROW_H = 16-18      # pts — generous spacing between lines
SEC_H = 17          # section header bar height
COL_H = 13          # column header height
COLLECTED_EXTRA = 11 # extra height for detail line on collected rows
```

- Draw a subtle separator line (0.2pt, #DDDDDD) at the bottom of each row
- Alternate row backgrounds: every even row gets #EBEBEB fill
- Collected rows: bold text + tick mark in checkbox

## Column Positions (from LEFT_M)

```python
COL_CK = 0          # checkbox
COL_YR = 11         # year
COL_NM = 36         # coin name (primary column)
# Right-side columns — push right to avoid overlap with period text
COL_ERA = 84*mm     # era marker (B/P/N) or face value
COL_NOW = 89*mm     # current state / secondary info
```

**Key lesson: Period/date strings like "300 BCE-1279" are ~28mm wide at 11pt. The era marker and NOW column MUST start after 84mm to avoid overlap.** This was a multi-iteration fix.

## Grayscale Design (MANDATORY)

Designed for a grayscale laser printer. Never rely on color for meaning.

| Visual element | Grayscale approach |
|---|---|
| Collected row highlight | Diagonal line hatching (not color fill) |
| Section headers | White text on solid black bar |
| Alternating rows | #EBEBEB vs white |
| Era indicators | Text letters (B/P/N) not colored dots |
| Collected mint marks | Bold vs regular weight (not color) |
| Checkboxes | Tick mark drawn with lines, not Unicode |

### Hatching implementation:
```python
def hatch(c, x, y, w, h):
    c.saveState()
    p = c.beginPath(); p.rect(x, y, w, h)
    c.clipPath(p, stroke=0)
    c.setStrokeColor(HexColor("#CCCCCC"))
    c.setLineWidth(0.35)
    for i in range(-int(h), int(w+h), 5):
        c.line(x+i, y, x+i+h, y+h)
    c.restoreState()
```

### Tick mark (not X, not Unicode):
```python
c.setStrokeColor(BLK); c.setLineWidth(1.2)
cx = LEFT_M + COL_CK + 1; cy = ty - 1
c.line(cx+2, cy+4, cx+4, cy+1.5)
c.line(cx+4, cy+1.5, cx+8, cy+7.5)
```

## Page Flow (Continuous)

**Never give each section its own page.** Sections flow continuously. Small sections (3-5 items) must pack onto the same page as the previous section's tail.

```python
# Prevent orphan: section header needs header + col_header + 1 row minimum
if item_type == 'section_header':
    needed = h + COL_H + 2 + ROW_H + 4
    if y - needed < BOT_M:
        y = new_page(c)
```

## Cover Page Structure

1. Black banner with title (20pt) and subtitle (16pt)
2. Subtitle line below banner (12pt, grey)
3. Horizontal rule
4. Stats box (#EBEBEB fill): "Total: X  Have: Y  Need: Z" (14pt bold)
5. Coverage percentage (11pt, grey)
6. Collector name (14pt bold) + Numista handle (11pt)
7. Legend section (if applicable)
8. Series summary with counts right-aligned

## Do NOT Include

- Separate blank notes page (wastes paper)
- Color-dependent elements
- Unicode checkmarks or special characters (font coverage issues)
- Font sizes below 7pt for any element
- More than 1 page of whitespace anywhere in the document

## Output

Save the PDF where the user can open it (on claude.ai: `/mnt/user-data/outputs/` and call `present_files`; in Claude Code: the working folder). Render pages with `pdf2image` for visual QA before delivering.
