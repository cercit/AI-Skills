# Routing rulebook (example)

Copy this file to `ROUTING.md` in your workspace and edit it to match the tools you actually have.

## Step 1: Sensitivity gate

| Data | Where it may go |
|---|---|
| Passwords, IDs, bank/card numbers, health records, private diaries, employer-confidential data | **Local model only** (e.g. Ollama) |
| Personal but not secret (drafts, notes, CVs) | Claude or local |
| Public information | Any |

If the task needs local-only data and the local model can't do it, stop and say so.

## Step 2: Pick the brain

| Task shape | Brain |
|---|---|
| Needs tools, files, code, accuracy, long reasoning | Claude |
| Scheduled, recurring, or messaging-based (WhatsApp/Telegram bots) | Agent runner (e.g. Hermes Agent) |
| Quick text job, not private | Gemini (free tier) or Claude |
| Quick text job, private | Local model |
| Bulk or overnight batch | Local model or agent runner |

## Step 3: Pick the skill

List your installed skills here, one line each, with the trigger words that should pick them.

| Skill | Use for |
|---|---|
| `resume` | Tailored résumé from a job description |
| `human` | Anything written in your voice |
| `linkedin` | LinkedIn post hooks |
| `diary` | Handwritten diary scans to notes |

## Step 4: Pick the agent

| Need | Agent |
|---|---|
| Wide search across many files | Explore / search agent |
| Plan a multi-step build | Plan agent |
| Otherwise | None, do it directly |

## Step 5: Connectors (MCP)

List the connectors you have (Gmail, Calendar, Drive, Sheets...) and which tasks use them. Never send or publish without asking first.

## Step 6: Communication rules

- Show the route block first.
- Plain words, short answers, numbers first.
- Ask before anything that sends, posts, pays or deletes.
