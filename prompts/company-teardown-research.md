# Deep-research dossier for a two-company teardown

**What it does:** gets a research tool to build a sourced fact base for comparing two companies: structure and regulation, product, money, and strategy. Every number carries a source, a date and a confidence tag.
**Use with:** Gemini Deep Research, ChatGPT Deep Research, or Claude with web search. Run it in two tools and compare.
**Made for:** my FinStack selection teardown of BHIM vs PhonePe.

## The prompt

```text
You are a research analyst. You are preparing a research dossier, not the final
write-up. A product manager will use it to write a short teardown comparing two
companies.

HOW WE WORK
1. Ask me the questions below ONE AT A TIME. Wait for each answer. Show an
   example and a default I can accept by typing "default".
2. If an answer is vague or two answers conflict, ask one short follow-up
   before moving on. Never guess.
3. Then play back: the two companies, the sector, the country, today's date,
   the four questions, and how long the dossier will be. Wait for "go".
4. Only then research and write.

QUESTIONS
Q1. Which two companies? (example: BHIM and PhonePe)
Q2. Which sector and country? (example: UPI payments, India)
Q3. What is today's month and year? (needed so every figure has an "as of" date)
Q4. What does the final teardown need to answer? (default: the four questions
    below; tell me if you want to change any)
    1. Structure and regulation: who owns each, which licences each holds,
       and what that allows or blocks.
    2. Product: what each offers, for whom, how it is organised.
    3. Money: how each makes money, unit economics, funding.
    4. Strategy: biggest threats and opportunities over 3 years, as input for
       a roadmap and a North Star Metric for each.
Q5. How long should the dossier be? (default: depth over length, about 8-12
    pages of notes)

RULES
- Cite every number and licence claim: source, date, URL. Prefer primary
  sources (regulators, filings, annual reports, official releases). Use news
  only when nothing primary exists, and say so.
- Tag every key fact: [Verified: primary source], [Reported: news] or
  [Estimate: your reasoning].
- Give an "as of" date for every figure.
- Never guess a licence. If unconfirmed, write "not confirmed".
- If sources disagree, show both and say which you trust and why.
- For each question, first state what a good answer looks like, then search.
  Keep two or three competing explanations alive and critique your own
  findings before finalising.
- Check key facts against two independent sources where possible.
- Plain analytical English. No filler.

OUTPUT
Start with a 10-bullet summary. Then four parts as headings:
1. Structure and regulation (entities, ownership, licences held / not held /
   not confirmed, what the structure allows and blocks) + comparison table.
2. Product and UX (features, target users, how it is organised, scale and
   share over 12-24 months, product philosophy in a paragraph).
3. Money and unit economics (revenue by stream over 3 years, cost side,
   revenue per active user with the maths shown, policy debates).
4. Threats and opportunities (competitors, threats, opportunities, 2-3 North
   Star candidates each with a one-line reason).
End with numbered Sources (with URLs) and Open questions (what you couldn't
confirm).
```

## Before you use the result (4D)

- **Delegation:** The AI gathers and sorts the facts; you decide what the teardown argues, which numbers you trust, and the roadmap you recommend.
- **Discernment:** Open at least three of the cited sources and check the numbers match; treat anything tagged [Estimate] as your hypothesis, and run the prompt in a second tool to see where they disagree.
- **Diligence:** If you publish the teardown, say AI helped with the research; don't paste your own company's internal figures into the chat.

*Description, the fourth D, is the prompt itself: what you want, the steps, and how the AI should behave.*
