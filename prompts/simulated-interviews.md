# Simulated interviews (practice and hypotheses only)

**What it does:** the AI role-plays realistic interview participants, both users and the people on the other side, so you can find weak spots in your hypotheses and rehearse your questions before talking to real people.
**Hard rule:** the output is AI-simulated, never user data. Never quote it as a user interview.
**Made for:** HireMate, to sharpen hypotheses before real interviews.

## The prompt

```text
You will role-play interview participants so I can practise and sharpen my
hypotheses. Everything you produce is AI-SIMULATED, NOT REAL USER DATA.

HOW WE WORK
1. Ask me the questions below ONE AT A TIME. Wait for each answer. Show an
   example and a default I can accept by typing "default".
2. If a profile is too thin to play realistically, ask one short follow-up
   (age, city, language, situation) before moving on. Never guess silently.
3. Then play back the cast list (one line per person) and the questions you
   will ask each. Wait for "go".
4. Then run the interviews, one participant at a time.

QUESTIONS
Q1. What is the product, and who is it for? (example: an AI mock-interview
    app for freshers going into bank jobs)
Q2. Which country and context should the people come from? (example: India,
    tier-2 and tier-3 cities)
Q3. Describe 5 users who should differ from each other: age, background,
    city type, language, situation. (default: you propose 5, I edit)
Q4. Describe 2 people on the other side, such as buyers or hiring managers.
    (example: a branch manager, an HR business partner; default: you propose)
Q5. Which questions do you want to rehearse? (default: the sets below)

DEFAULT QUESTIONS FOR EACH USER
1. Tell me about yourself and what you're looking for.
2. Walk me through the last time you faced this problem, start to finish.
3. What was the hardest moment, and what did you do?
4. Afterwards, what did you find out about why it went that way?
5. How do you deal with it today, and have you paid for anything?
6. If you could change one thing, what would it be?

DEFAULT QUESTIONS FOR EACH OTHER-SIDE PERSON
1. What is your part in this, and how often does it come up?
2. Walk me through the last time. How did you decide?
3. Think of a recent case that went badly. What fell short?
4. What happens afterwards? Any case that didn't work out?
5. How do you handle it today, and what does it cost in time or money?
6. What one thing would you want to know beforehand?

RULES
- Answer in first person, casual, with local-language mix where natural, with
  specific stories, not polished answers.
- Realistic, not optimistic. Include people who would NOT use or pay for this,
  and at least one person who thinks free tools are enough.
- No made-up statistics. Stories only.

END WITH
(a) the 5 strongest pains, (b) the 3 biggest reasons someone would NOT use
it, (c) 3 questions I should ask real people that I'm probably not asking.
Label the whole output "AI-SIMULATED - NOT REAL USER DATA".
```

## Before you use the result (4D)

- **Delegation:** The AI plays people so you can rehearse; real users still have to answer your real questions, and that part is yours.
- **Discernment:** Use the output only to sharpen hypotheses and questions: if a pain sounds convincing, test it with real people before believing it.
- **Diligence:** Keep the "AI-simulated, not real user data" label on every copy, and never quote it as a user interview, survey result or evidence.

*Description, the fourth D, is the prompt itself: what you want, the steps, and how the AI should behave.*
