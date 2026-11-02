# Coin image grid PDF from Numista (Claude Code)

**What it does:** in one run, finds missing Numista numbers for your coins, downloads front and back images, and lays them out as printable A5 binder pages, one PDF per checklist.
**Use in:** Claude Code (it needs to run scripts and a browser), in a project folder with your coin list.
**Made for:** my own coin binder. Coin data is public, not confidential.

## Before you start
Open Chrome with remote debugging so the script can use your logged-in Numista session:
`<path to chrome> --remote-debugging-port=9222`

## The prompt

```text
You will help me build printable coin image pages from Numista.

HOW WE WORK
1. Ask me the questions below ONE AT A TIME. Wait for each answer. Show an
   example and a default I can accept by typing "default".
2. If a file is missing or a column name doesn't match, stop and ask. Never
   guess a file or a Numista number.
3. Then play back: the input file, the checklists (one PDF each), the page
   layout, and how coins I have vs coins I want will look. Wait for "go".
4. Then run the three tasks below, reporting after each.

QUESTIONS
Q1. Which spreadsheet holds the coins? Which sheet lists coins I HAVE, and
    which lists coins I WANT? (example: Coin_Image_Input.xlsx, Sheet 1 / 2)
Q2. Which column holds the Numista number (N#)? Which rows still need one?
Q3. How should coins be grouped into PDFs? (example: China, UK, US Quarters,
    India princely states, World for everything else)
Q4. Page size and binder? (default: A5, 6-hole Filofax, left margin 18mm)
Q5. Any formatting skill or existing checklist I should match? (default: none)

TASK 1: Fill missing N# numbers
Search Numista for each coin marked as needing one and fill the column.
Show me any match you are not sure about instead of picking one.

TASK 2: Download images
Connect Playwright to my running Chrome at http://localhost:9222.
For each coin: open https://en.numista.com/{N#}, save the front and back
images as images/{N#}_front.jpg and images/{N#}_back.jpg, and mark the row
DONE with both paths. Wait 2-3 seconds between pages. On error, mark ERROR,
log it and continue. Skip rows already DONE, so the run can resume.

TASK 3: Build the PDFs
- 2 coin pairs per row; each image 2cm square, 1mm gap front to back, 4mm gap
  between pairs; about 5-6 rows per page.
- Label under each pair: line 1 country + denomination + year (bold 8pt),
  line 2 design name (7.5pt), line 3 extra detail only if needed (italic 7pt).
- Margins: left 18mm (punch side), right 6mm, top 9mm, bottom 8mm. Punch
  guides on every page. Works in grayscale.
- Coins I HAVE show normally. Coins I WANT get a light dashed border and a
  faint diagonal "WANT".
- One PDF per group, saved to output/.

END WITH
A short report: coins processed, N# numbers filled, images downloaded,
errors (with the log path), and the PDFs made with page counts.
```

## Before you use the result (4D)

- **Delegation:** The AI runs the lookups, downloads and layout; you check which Numista match is right whenever it isn't sure.
- **Discernment:** Look at the first PDF page printed at 100% scale before printing them all; spot-check a few coins against their Numista pages.
- **Diligence:** Download slowly, as the prompt says, keep the images for your own binder, and respect Numista's terms; don't republish their photos.

*Description, the fourth D, is the prompt itself: what you want, the steps, and how the AI should behave.*
