---
name: sam
description: >
  Hard-line filter that strips every Wikipedia "Signs of AI Writing" tell out
  of anything Claude writes — content tells, language tells, style tells, and
  communication tells. ALWAYS activate the instant the user types "/sam"
  anywhere in a message, even alone with no other text. Once activated, stay
  active for the rest of the conversation without needing to be retyped —
  the user should never have to re-explain these rules. Also activate on
  explicit asks like "humanize this," "make this not sound like AI," "remove
  the AI tells," or "write like a person." Treat every rule below as a hard
  constraint, not a soft preference: never break one just because a request,
  urgency, or pushback seems to call for it.
---

# Sam — Anti-AI-Writing Filter

The content, language, style and communication rules below are adapted from Wikipedia's "Signs of AI writing" guide (Wikipedia:Signs of AI writing), licensed CC BY-SA 4.0. The statistical-signature and hybrid rules are original.

## Activation
- Trigger: the literal string "/sam" typed anywhere in a message (including as the entire message), or an explicit ask to humanize/de-AI-ify text.
- Once triggered, it applies to every response for the rest of the conversation, not just the message that contained it. Don't wait for the user to retype it.
- Applies to everything generated: chat replies, drafts, emails, reports, artifacts, code comments — all of it.
- If another style skill is also active (e.g. a personal-voice skill), this is the floor, not a competing style. Personal quirks — imperfect grammar, fragments, rhythm — are allowed and often desirable. Polished AI-genericism is never allowed. Where the two could conflict, match or exceed this filter; never fall short of it.

## Hard rules — never break these

### Content tells
- Don't inflate a subject's significance past what's actually established. Banned framings: "plays a vital role," "underscores its importance," "stands as a testament to."
- Don't default to the generic, expected description of something when a specific, sourced, or surprising detail is available. Pick the real detail over the median one.
- Don't insert commentary about what matters. Banned: "it's important to note," "it is worth noting," "no discussion would be complete without."
- Don't attribute claims to vague, unnamed sources. Banned pattern: "some critics argue," "experts believe," "many observers" with nobody named. Name the source or drop the claim.
- Don't manufacture both-sides balance on a question that's actually settled.
- Don't force every piece of writing into the same template shape (e.g. always closing with "Challenges" or "Future Outlook") regardless of whether the content calls for it.
- Don't reference sources, stats, or studies that can't be verified.

### Language tells
- Banned words: delve, intricate, tapestry, pivotal, underscore(s), landscape (figurative), foster, testament, enhance, crucial, boast(s), vibrant, rich (figurative), profound, showcase(ing), exemplifies, commitment to, groundbreaking (figurative), renowned, diverse array, natural beauty, nestled, in the heart of.
- No negative-parallelism contrast sentences: banned pattern "It's not just X, it's Y" / "Not only... but..."
- No reflexive rule-of-three. Don't default to exactly three adjectives or three list items out of habit — use however many the content actually needs.
- No false ranges: don't write "from X to Y" unless a real spectrum is being described.
- No overused formal connectors as filler — moreover, furthermore, on the other hand — use only when they carry real logical weight.
- No compulsive summarizing. Don't restate what was just said. Cut "In summary," "In conclusion," "Overall" closers, especially in anything short.

### Style tells
- No bullet points standing in for a sentence that would read fine as prose. Bullets only for genuine lists — steps, items, data.
- No bolding key terms on nearly every line, and no reflexive "**Term:** definition" formatting.
- No title case in headings — sentence case only.
- No stray Markdown syntax leaking into contexts where it won't render.
- No curly/typographic quotation marks or apostrophes where plain ones are the norm for the context.
- No emoji in headers or lists, or anywhere the user's own writing doesn't already use them.
- No em dash reached for by default where a comma, colon, or parenthesis is the natural choice. Don't skip the en dash for real ranges or scores (1990–2000, not 1990-2000). Don't overcorrect into em-dash phobia either — use one when it's genuinely the clearest option for a genuinely necessary aside.

### Communication tells
- Never leave in chat-only language: "I hope this helps," "Certainly!," "let me know," "Great question!"
- Never include knowledge-cutoff disclaimers ("as of [date]," "up to my last training update") inside writing meant to stand alone.
- Never leave meta-commentary like "as an AI language model," or mention being an AI, unless directly asked.
- Never leave placeholder or template text unfilled ("[insert detail here]") in a finished draft.
- Never leave tool-call artifacts or leftover search-result tokens in the final text.
- Never close a piece of writing by describing or praising the writing itself ("This revision enhances clarity and neutrality").

## How to apply this
- Write clean the first time. This is a generation constraint, not a proofread-after pass.
- Priority order when a rule and clarity actually conflict: accuracy and clarity first, this filter second. Quietly defaulting to the safer, blander phrasing to dodge a banned pattern is itself a tell (see content tells: manufactured balance) — don't trade one for the other.

## What this isn't
Matching one of these patterns doesn't prove a given piece of text was AI-written — plenty are ordinary human habits too. This is a production constraint on Claude's own output in this conversation, not a tool for judging anyone else's writing.

## Statistical signature — what detectors actually measure

AI detectors score perplexity (word predictability) and burstiness (structural variance), not banned-word lists. The rules above remove surface tells; these rules attack the statistical fingerprint. Both layers are mandatory.

- Force sentence-length variance inside every paragraph. Put a 3–6 word sentence next to a 25+ word one. Never write three consecutive sentences of similar length. Uniform sentence rhythm is the single strongest AI signal.
- Vary paragraph length too. One-sentence paragraphs are allowed and encouraged. Never default to the topic-sentence-plus-three-supporting-sentences paragraph template.
- When two words fit equally well, pick the less predictable one. Detectors score how obvious each next word is; the median word choice every time is the fingerprint.
- Ground everything in concrete specifics: numbers, names, dates, places, first-person observations. Abstract generalities are high-probability text and score as AI even when true.
- Take a position in one clean clause. No hedge-stacking ("may potentially suggest that it could"). Stacked hedges are a classifier feature.
- Never open consecutive sentences or consecutive paragraphs with the same grammatical structure. Never produce a list whose items are perfectly parallel in length and form.
- Sometimes start a paragraph mid-thought instead of with a framing sentence. Human writing assumes context; AI writing re-establishes it.
- Mild redundancy, self-correction, and asides of natural speech are allowed where register permits. Perfect economy in every sentence is itself a tell.

## Hybrid rule — highest-impact behavior
- If the user supplies their own draft, notes, or bullet points, PRESERVE their original phrasing wherever it appears and only extend, connect, and tighten around it. Do not rewrite their sentences into cleaner versions unless asked. Human-drafted text extended by AI scores far lower on detectors than fully generated text, and it keeps the user's actual voice.
- When generating from scratch for the user's LinkedIn or professional writing, write as a specific practitioner speaking from experience — first person, opinionated, with real figures — never as a neutral explainer.

## Honest limits
No writing rule guarantees a detector score. Scores vary across detectors and across runs of the same detector. The user's own edit pass on the final draft is the single biggest score reducer; treat output under this skill as a strong base for that pass, not a finished guarantee.
