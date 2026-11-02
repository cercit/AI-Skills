# Agents

Nine Claude Code subagents I use day to day. Each is one Markdown file: copy it into `.claude/agents/` in your project (or `~/.claude/agents/` for all projects) and Claude can hand matching work to it.

| Agent | What it does |
|---|---|
| [meeting-notes](meeting-notes.md) | Messy notes or a transcript → decisions, action items with owners, open questions |
| [product-doc](product-doc.md) | PRDs, specs, user stories with acceptance criteria, one-pagers |
| [market-research](market-research.md) | Sourced competitor and market briefs, tuned for Indian auto and NBFCs |
| [data-spreadsheet](data-spreadsheet.md) | Cleans and builds Excel/CSV, charts, plain-language takeaways |
| [finance-modeling](finance-modeling.md) | Budgets, forecasts, ROI, unit economics, pricing |
| [linkedin-post](linkedin-post.md) | LinkedIn drafts and hooks in your own voice; never posts |
| [print](print.md) | Dense, measured PDFs with no half-empty pages, using [pagefit](https://github.com/cercit/pagefit) |
| [coin-research](coin-research.md) | Coin series research and collection gaps from a Numista export |
| [haiku-helper](haiku-helper.md) | A cheap helper for small file jobs, on the Haiku model |

Two habits run through all of them: lead with the answer in plain language, and keep confidential company numbers on your own machine rather than sending them to a cloud model.

Some agents work best with the [skills](../#readme) in this repo. A few have a short "Setup" block at the top to fill in once.

## Using them in Codex or Cursor

The files are in Claude Code's format: a short header (`name`, `description`, `tools`, `model`) and then plain instructions. The instructions work in any coding assistant; only the header is Claude-specific.

- **Codex:** copy the text below the header into your project's `AGENTS.md`, under a heading like `## When I ask for meeting notes`. Codex reads that file at the start of every session.
- **Cursor:** save the text below the header as a rule in `.cursor/rules/<name>.mdc`. Put the agent's `description` line in the rule's description so Cursor picks it up when a task matches, or mention the rule with `@` when you want it.

Drop the `tools` and `model` lines in both cases. Settings like "use the Haiku model" only apply in Claude Code.
