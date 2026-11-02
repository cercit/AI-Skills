# Role requirements and scenario question bank

**What it does:** researches how a sector really hires for entry-level roles, from real job postings, and builds a scenario question bank per role with strong and weak answers.
**Use with:** any AI with web search (Gemini Deep Research, ChatGPT, Claude).
**Made for:** HireMate, an interview-practice concept for bank and NBFC jobs.

## The prompt

```text
You are a hiring and training expert. We will research how employers hire for
specific entry-level roles and build a question bank from it.

HOW WE WORK
1. Ask me the questions below ONE AT A TIME. Wait for each answer. Show an
   example and a default I can accept by typing "default".
2. If an answer is unclear or too broad (for example a role with many
   sub-types), ask one short follow-up before moving on. Never guess.
3. Then play back: product, audience, sector, country, roles and the
   must-have scenarios. Wait for "go".
4. Only then research and write.

QUESTIONS
Q1. What are you building, and for whom? (example: an AI mock-interview app
    for Indian freshers with 0-3 years' experience)
Q2. Which sector and country? (example: banks and NBFCs, India)
Q3. Which 3-5 roles, with any sub-types? (example: Collections Officer
    (field / tele), Field Sales, Credit Analyst, Data Analyst)
Q4. Which years of job postings should count? (default: the last 2 years)
Q5. Any scenarios that must be included per role? (example: an angry customer
    on a missed payment for Collections; default: you propose, I confirm)
Q6. Should questions have a local-language version? Which language?
    (default: English only)

FOR EACH ROLE, GIVE ME
A. Role requirements (from real postings): typical titles at named employers,
   minimum qualification, experience, salary range, languages, top 5 skills or
   behaviours asked for, regulatory knowledge expected.
B. The interview process: rounds in order, what interviewers really judge in
   each, most common reasons for rejection.
C. Scenario question bank, 12 questions: a mix of role-plays, "what would you
   do if" and knowledge questions. For each: the question as an interviewer
   would say it, what a strong answer covers (3-4 points), a common weak
   answer and why it fails, difficulty level.
D. Gap check: which skills can be practised with an AI mock interview, and
   which need a human?

RULES
- Cite a source (URL + date) for every factual claim. Mark anything without a
  source [UNVERIFIED].
- Never invent statistics. If you can't find a number, say so.
- Stay within the country I named. Simple language. Tables where possible.
```

## After it runs
Check the sources yourself before using any of it as evidence in a document.

## Before you use the result (4D)

- **Delegation:** The AI collects job-post evidence and drafts the questions; you decide which roles and scenarios matter, and which questions are realistic enough to use.
- **Discernment:** Open a few of the job postings it cites and check the salary bands and requirements are really there; rewrite any question that no real interviewer would ask.
- **Diligence:** Mark anything you couldn't verify as unverified when you share it, and say AI helped build the bank.

*Description, the fourth D, is the prompt itself: what you want, the steps, and how the AI should behave.*
