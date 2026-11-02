# AI skills, agents and prompts by Sameer Mittimani

Also in this repo: [9 Claude Code agents](agents/) and [6 question-led prompts](prompts/) for ChatGPT, Gemini or Claude.

## Skills

Nine AI skills (for Claude) I built for my own work in auto finance, product management and a few hobbies. Each folder is one skill. Drop a folder into `~/.claude/skills/` (Claude Code) or zip it and upload it in claude.ai under Settings → Capabilities → Skills.

Fill in the `<placeholders>` in a skill before you use it. None of them ship with my personal details.

| Skill | What it does | Setup needed |
|---|---|---|
| [resume](resume/) | Tailored 2-page résumé PDF from a job description. Honest fit verdict, JD keyword matching, and checks for page count, forbidden phrases and AI-sounding words. Only uses facts from your master profile. | Fill `templates/master-profile.template.md` and `templates/profile.example.json`. Needs Python, `playwright`, `pymupdf`. |
| [linkedin](linkedin/) | LinkedIn hook writer for Indian professionals: mobile-length first lines, ₹/lakh/crore, calm tone, no negative or controversial headlines. | Fill "Who is writing". |
| [human](human/) | Writes in your own voice (personal, casual, professional) and strips AI-writing tells. | Fill Part 1 and your own phrases. |
| [sam](sam/) | The anti-AI-writing filter on its own, plus rules for sentence rhythm and word choice. | None. |
| [daily-auto-brief](daily-auto-brief/) | Morning news brief PDF for Indian auto finance: your company, OEM numbers, Vahan, NBFC and RBI news. Optional email draft (never sends). | Fill the Settings table. |
| [diary](diary/) | Turns scanned handwritten diary pages into clean markdown notes. | Set input and output folders. |
| [route](route/) | Picks where a task should go (Claude, Gemini, a local model, an agent runner) with a privacy check first. | Copy `ROUTING.example.md` to `ROUTING.md` and edit. |
| [coin-plan](coin-plan/) | Coin collection gap analysis and shopping lists from a Numista CSV export. | Fill the Collector profile. |
| [a5-coin](a5-coin/) | Print-ready A5 Filofax coin checklists (grayscale, 6-hole punch). | Carlito font installed. |

## Credits and licences

- **linkedin**: adapted from Distinctiva's free *LinkedIn Hook Writer* (distinctiva.io). The width model and mobile length rules are theirs; the tone rules, Indian context, hook styles and examples are mine.
- **human** and **sam**: the content, language, style and communication rules are adapted from Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). These two skills are shared under the same licence.
- **a5-coin**: uses the Carlito font (SIL Open Font License).
- Everything else: my own work.

Built with Claude.
