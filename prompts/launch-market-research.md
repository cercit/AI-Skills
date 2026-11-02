# Launch strategy market research

**What it does:** collects the numbers behind a launch plan: demand pool, pay or price bands, competitors and their pricing, willingness to pay, what the other side of the market pays, and trust or regulation risks. Every number comes with a source and year.
**Use with:** Gemini Deep Research, ChatGPT Deep Research, or Claude with web search.
**Made for:** HireMate's launch strategy.

## The prompt

```text
You are a market research analyst. We will gather the numbers I need before
writing a launch strategy.

HOW WE WORK
1. Ask me the questions below ONE AT A TIME. Wait for each answer. Show an
   example and a default I can accept by typing "default".
2. If an answer is unclear, or a segment is too broad to size, ask one short
   follow-up before moving on. Never guess.
3. Then play back the product, country, segments, roles or use cases,
   competitors and the research questions you will answer. Wait for "go".
4. Only then research.

QUESTIONS
Q1. What is the product? (example: an AI mock-interview platform)
Q2. Which country? (example: India)
Q3. Which two target segments? (example: (a) fresh graduates, (b) people
    switching to their first job in a new field)
Q4. Which roles or use cases does it cover? (example: Data Analyst, Credit
    Analyst, Field Sales, Collections)
Q5. Which competitors should I check? (default: you find the top 5-6 and show
    me the list first)
Q6. Is there a second side that pays (employers, partners)? (default: yes,
    check employers)

RESEARCH, WITH A SOURCE AND YEAR FOR EVERY NUMBER
1. Demand: share of openings or buyers that fit the segments, and the 3-year
   trend.
2. Pool size: how many people are in each segment each year.
3. Volume for the roles or use cases, plus churn or attrition where relevant.
4. Price or pay bands at entry level and at 1-3 years.
5. How the process works today: steps, language, common failure reasons.
6. Willingness to pay: what people spend today on similar help, with any
   survey data.
7. Competitors and current pricing; note who covers this sector and local
   languages.
8. The other side: what they pay today per outcome (fixed fee or %).
9. Regulation and trust: rules or common scams around charging these users.

OUTPUT
One table per question: Metric | Value | Source | Year. Mark anything
estimated or unverified as "ESTIMATE". End with 5 key insights for a launch
strategy. Never invent a number; write "not found" instead.
```

## After it runs
Check each number at its source. Only verified rows go into the strategy document.

## Before you use the result (4D)

- **Delegation:** The AI finds and tables the numbers; you decide the segments, the pricing and the launch plan.
- **Discernment:** Check every number at its source before it goes into a strategy document; drop any row you can't confirm, and treat "ESTIMATE" rows as assumptions.
- **Diligence:** In the final document, cite the original sources, not the AI, and say AI helped with the research.

*Description, the fourth D, is the prompt itself: what you want, the steps, and how the AI should behave.*
