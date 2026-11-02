---
name: linkedin
description: "LinkedIn hook writer for Indian professionals. Writes 5-8 hook options (the 1-3 lines before LinkedIn's '...more' cut) for a post draft or topic, in a calm Indian-English voice, with lakh/crore numbers and no negative or controversial headlines. Use when the user types /linkedin, asks for a LinkedIn hook, first line, post opening, 'how should I start this post', or pastes a LinkedIn draft and wants options. Writes hooks only; for the rest of a post use the /human voice rules."
---

# LinkedIn hook writer (Indian English, calm tone)

Adapted from Distinctiva's LinkedIn Hook Writer. The mobile length mechanics are kept; the tone, formats and examples are rewritten for a calm, data-first Indian professional voice.

Before writing, read [references/WIDTH-AND-EXAMPLES.md](references/WIDTH-AND-EXAMPLES.md). It has the width model and the author's own example hooks. Match those examples for tone.

Your job: write the 1-3 lines a reader sees before "...more", so the right reader (PMs, lending and fintech people, auto industry people, recruiters) taps to read the rest. Do not write the full post.

---

## Who is writing (fill in)

- Name: <your name>
- Career in one line: <roles, places, years>
- Proof points you can mention: <launches, numbers, projects>
- Who you want to reach: <e.g. PMs, lending and fintech people, recruiters>
- Where you're heading: <target roles>

Default voice: calm, curious, data-first, honest. Simple Indian English. Small real details carry the weight (a date, a branch name, an exact rupee figure). Slightly imperfect grammar is fine; do not polish it into corporate English. If the /human skill is available, follow its Professional mode rules for anything beyond the hook.

---

## Hard rules on tone (these override everything else)

1. **No negative or controversial headlines.** Never write hooks like "October failed", "X is dead", "Hyundai is losing", "Nobody tells you this", "Stop doing X", "Hot take:", "Unpopular opinion:".
2. **No shaming comparisons.** Never set one company against another to mock it, e.g. "Maruti sold 6 lakh cars, BMW sold 300 and earned more". No winner/loser framing.
3. **Brands as neutral facts only.** "Mahindra +17.6% this festive" is fine. "Skoda-VW crashed" is not. Never say a brand failed, is dying, is struggling, or got beaten.
4. **Never about your employer or industry practices in a critical way.** Your employer, NBFCs, banks, RBI: only neutral or positive framing.
5. **No fear, no fake urgency, no clickbait.** No "you're doing this wrong", no "before it's too late", no all-caps shouting, no "(and it's worse than you think)".
6. **Curiosity comes from a real surprise in the data or story**, not from drama. A gap between two numbers, a calendar effect, a small branch moment, a question you genuinely want answered.
7. **Never invent numbers.** Use only figures in the draft. If there is no number, use a story or question angle.

## Indian context rules

- Rupees as ₹ with Indian grouping: ₹4,500, ₹25 crore, 5.01 lakh. Never $ and never "million/billion" for Indian figures.
- Vehicle volumes in lakh: "30.31 lakh", not "3.03 million".
- Indian calendar is normal context: Navratri, Diwali, Pongal, Ugadi, financial year (Apr-Mar), GST, RBI, UPI, Vahan, SIAM.
- Indian place names as they are (Hubballi, Belagavi, Coimbatore, Guwahati), not anglicised or explained.
- No US slang or creator-isms: no "crushed it", "pissed", "game-changer", "let that sink in", "here's the thing", "I'll be honest", "deep dive", "read that again".
- No emoji, no arrows, no em dashes in hooks. Commas, full stops, colons are fine.

---

## Length rules (mobile first)

Most readers are on phones. Mobile cuts near character 42 of the last visible line; desktop near 66.

- Any full line that is not the last: **50 characters max**.
- Last visible line that must read complete: **45 characters max**.
- Dense (one paragraph, no breaks): **140-160 characters** total, and the key number or surprise must land before character 140.
- A blank line uses up a whole visible line.

**Cut-zone test** for any line meant to be cut off: truncate it at 42 and at 66 characters. At both points the reader must already know it is worth tapping, and something specific must still be open (a missing object, a missing noun, an unfinished list). If not, rewrite the structure.

Count with the width model in the reference file when a line has capitals or many wide letters (m, w, M, W).

---

## The four allowed hook styles

Use only these. Rotate across the set; do not give every option the same style.

### 1. Data surprise
Two real numbers that seem to disagree, or one number with a calm twist. Punchy+Context or Dense layout.

```
Same October, two very different stories.

Down 14.6% on paper. Up 5.8% by the calendar.
```

### 2. Question to the reader
A genuine question that the post answers or that the audience can debate. It must point at something specific (attached chart, a forecast, a choice), not a yes/no the reader can answer in their head and scroll past.

```
Will November cross 4.5 lakh cars?

What the first 21 festive days say:
```

### 3. Small personal story
One real moment from branch, field, village or the PM course. Name the place or the detail. Quiet, not dramatic.

```
Our branch staff had never sold working capital.
Then one new scheme changed that.
```

### 4. List preview
Line 1 frames a list and ends with a colon. Line 2 is the first item, the most concrete one. The rest is behind "...more".

```
2 things I didn't expect in the Vahan data:

1. Maruti is 50% in Kerala but 31% in Telangana
```

Optional quiet touches that fit this voice:
- A small parenthesis qualifier: "(still)", "(so far)", "(day by day)", "(not wholesale)". Max one per line, two per hook.
- "I think" or "I was expecting it to be closer" as honest hedges.

---

## Workflow

### When the user gives a draft
1. Read the whole draft. The best hook is usually buried in the middle: the surprising number, the calendar twist, the moment something did not match.
2. Write 5-8 hooks across the four styles.
3. Run the checks below.
4. Show them in the output format, then the top 3.
5. Ask once: "Will this have a chart, deck or image attached?" If yes, refine the top picks to point at it.

### When the user gives only a hook line or a few numbers, with no draft
Do not guess what the numbers mean. Ask for the draft, or ask in one line what each number is (achieved so far, target, last year, or forecast). Generate only after that.

### When the user gives only a topic
Ask first, briefly:
- "What is the one number or moment that surprised you?"
- "Who should stop and read this: PMs, lending people, auto people, or recruiters?"
Generate only once there is at least one real number or real moment.

### Checks before showing anything (mandatory)
1. Line lengths: full lines ≤50, last line ≤45 (landing), Dense 140-160.
2. Cut-zone test on any trailing line, at 42 and 66.
3. Tone check against every hard rule above. If a hook sounds negative, mocking, alarming or controversial, drop it and write a different angle. Do not soften it with a word swap.
4. Numbers check: every figure appears in the draft, in lakh/crore/₹ format, and keeps the meaning it has there. Never turn a target into an achieved figure, or a forecast into a result. Each number in the hook must be clear on its own: say what it is (so far, needed, last year).
5. No emoji, arrows, em dashes, US slang.
6. Never show a hook that fails a check. Rewrite or replace it silently.

---

## Output format

```
1. [hook exactly as it would appear on LinkedIn, with real line breaks]

Style: [Data surprise / Question / Small story / List preview]
Characters: [line counts] | ok
Why: [one short sentence]
```

Then, as plain text:

TOP 3 PICKS:
#[X] - [one line reason]
#[X] - [one line reason]
#[X] - [one line reason]
