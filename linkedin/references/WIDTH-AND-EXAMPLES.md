# Width model and example hooks

## The width model

Letters are not equal widths. The real limit is pixel width, not character count. (Width model from Distinctiva's LinkedIn Hook Writer.)

| Character class | Units |
|---|---|
| Narrow letters (i, l, 1, !, ., ,, ;, :, ', j, f, t, r) | 1.0 |
| Space | 1.2 |
| Common punctuation (-, (, ), ?, ₹, &, @, ") | 1.5 |
| Uppercase narrow (I, J, L) | 1.5 |
| Regular lowercase and digits | 2.2 |
| Uppercase regular (A-H, K, N-V, X-Z) | 2.6 |
| Wide lowercase (m, w) | 2.8 |
| Uppercase wide (M, W) | 4.0 |

Normal sentence-case text runs at about 1.75 units per character.

| | Full line | Last visible line |
|---|---|---|
| **Mobile** | ~90 units (~50 chars) | ~78 units (~45 chars) |
| LinkedIn desktop feed | ~128 units | ~120 units |

Total mobile hook budget over three lines: ~258 units (~147 characters). The last line is shorter because "...more" sits on it.

The cut zone is characters 40 to 70: mobile cuts near 42, desktop near 66. A line meant to be cut must stay interesting across that whole range.

---

## The author's past openings: what went wrong on mobile

These are real first lines from the author's posts, shown as a phone sees them (cut near 42 characters). Use them to see the problem the skill fixes.

| Post | Opening | Phone sees | Problem |
|---|---|---|---|
| Vahan Oct | "October number came in and first reaction was, oh, 5.01 lakh, down 14.6%." | "October number came in and first reaction" | The number and the twist are both past the cut. |
| Project launch | "https://lnkd.in/..." | a link | No hook at all. |
| Case study | "https://lnkd.in/..." | a link | No hook at all. |
| Survey ask | "5 minute survey for freshers and early-career people: https://..." | "5 minute survey for freshers and early-c" | Reads as an ask, not a story. |
| Parker | "Parker had the Indian pen market for 40 years. Then they stopped paying attention." | fits | Good structure, but "stopped paying attention" leans negative on a brand. Prefer the neutral version below. |

---

## Good hooks in this voice (calibrate to these)

### Data surprise

```
Same October, two very different stories.

Down 14.6% on paper. Up 5.8% by the calendar.
```

```
Navratri started 19 days later this year.
That one date changes the October number.
```

```
30.31 lakh cars so far this year (Apr-Oct).
So I went state by state:
```

### Question to the reader

```
Will November cross 4.5 lakh cars?

What the first 21 festive days say:
```

```
How did you prepare for your first interview?

Mine was one night, YouTube and a friend.
```

### Small personal story

```
Our branch staff had never sold working capital.
Then one new scheme changed that.
```

```
My first job was customer support in a small branch.
Now I build the tools I wished I had.
```

```
Three phones, one food order, ₹1,210.25.
Every phone showed the same split.
```

### List preview

```
2 things I didn't expect in the Vahan data:

1. Maruti is 50% in Kerala but 31% in Telangana
```

```
What a car loan goes through in our app:

1. PAN, Aadhaar, payslips and a live photo from the phone
```

### Neutral brand framing (how to mention companies)

Good: "Mahindra +17.6%, Tata +12.0% in the first 21 festive days."
Good: "VinFast started registering in Sep 2025. 13,751 units so far."
Good: "For 40 years, a Parker was the default gift pen in India."
Not allowed: "Skoda-VW crashed 20%", "Hyundai is losing the plot", "Maruti sold 6 lakh, BMW sold 300 and earned more", "Parker stopped caring".

---

## Never write (examples of what this skill removes)

- "October FAILED. Here's why nobody is talking about it."
- "Car loans are dead."
- "Hot take: NBFCs don't understand customers."
- "Stop using Excel for Vahan data."
- "I'll be honest, this shocked me."
- Anything in ALL CAPS, any emoji, any $ figure for an Indian number.
