---
name: resume
description: Build a tailored 2-page resume PDF from a pasted job description, using only facts in your master profile. Gives an honest fit verdict, matches the JD's keywords where they are true, and checks pages, forbidden phrases and AI-sounding words. Use when the user types /resume, pastes a JD and asks for a resume, or says "make my resume for this job".
---

# Resume

The user pastes a job description (JD). You produce a tailored 2-page PDF resume, a fit verdict and a check report. Every fact comes from the master profile. Nothing is invented.

## One-time setup

Create a `Resume-Builder` folder (anywhere) with:

- `master-profile.md`: copy `templates/master-profile.template.md` and fill it in. This is the only source of facts and wording rules.
- `profile.json`: copy `templates/profile.example.json` and fill in your name, contact, education, certifications and forbidden phrases.
- `build_resume.py`: copy `scripts/build_resume.py`.
- `jobs/`: one sub-folder per application.

Install once: `pip install playwright pymupdf` then `playwright install chromium`.

Ask the user where their `Resume-Builder` folder is if you don't know. Never guess paths.

## Optional: one chat per job

If the user prefers each application in its own chat (easy to delete after a rejection), save the JD to `jobs/<yyyy-mm-dd>-<company>-<role>/jd.txt` and start a separate session that runs this skill from Step 1. Any new fact confirmed there still goes into the master profile.

## Steps

1. **Read the master profile in full.** Then read the JD.
2. **Fit verdict first (honest, short).** Table: what the JD asks for vs what the user has (✅ / 🟡 projects only / ❌). Say plainly if it is a stretch (for example "10+ years in PM" when they have 0 years with a PM title). Say if a referral matters more than wording.
3. **Pull 10–15 JD keywords**: the exact skill and duty phrases a screener or ATS will search for. Use only ones the user can back up from the profile.
4. **Write `resume.json`** in the job folder (shape: `templates/resume.example.json`):
   - `file_name`: `Resume_<Name>_<Company>_<Role>` (no spaces)
   - `role_line`: the official title from the master profile
   - `summary`: 2 short paragraphs from the summary blocks; the closing line names the JD's role and sector
   - `skills`: 5–6 `[label, text]` pairs; labels reuse the JD's own phrases where true
   - `tools`, `experience` (all roles; bullets can be reordered or trimmed, never reworded into stronger claims), `portfolio` (3–5 most relevant projects), `order` (`["experience","portfolio"]` or the reverse if projects are the stronger evidence), `jd_keywords`
5. **Save the JD** as `jd.txt` in the same folder.
6. **Build:** `python build_resume.py profile.json jobs/<folder>`. It prints the check report and exits 1 if anything fails.
7. **Fix and rebuild** until: 2 pages, no forbidden phrases, no banned words, and at least 80% of the JD keywords found (or explain why a missing one cannot be claimed truthfully).
8. **Look at both pages** (render to PNG with pymupdf and view them). Check nothing is cut, no orphaned heading, links blue.
9. **Send the PDF** to the user, then reply in 4 lines: What it is / What I've done / What you have to do / What next. Include the fit verdict and any line the user must confirm before sending.

## Hard rules

- No fact that is not in the master profile. If the JD needs something the user may have done, ask one question, then add it to the master profile with the date before using it.
- Follow every wording rule in the master profile exactly (titles, verbs, numbers, things never to mention).
- Write in plain words: no banned AI words, sentence case, numbers first.
- Do not send applications or emails. The user applies themselves.
