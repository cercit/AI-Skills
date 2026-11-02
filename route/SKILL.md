---
name: route
description: |
  Route any task through a 6-step decision flow: sensitivity gate, brain selection (Claude / Gemini / an agent runner / a local model), skill matching, and agent selection. Use when the user types /route, or says "route this", "which model", "where should this go", "pick the right tool". Reads your routing rulebook and walks the decision tree for the current task.
---

# Task router

You are the routing engine. Walk the user's request through the decision flow in
the user's routing rulebook. Read it NOW before doing anything else.

## Where the rulebook lives

- First look for `ROUTING.md` in the current workspace (or wherever the user has told you it is).
- If there is none, use `ROUTING.example.md` next to this skill as the rulebook, and tell the user they can copy and edit it.

## Procedure

1. **Read** the rulebook.
2. **Understand** the user's request: what do they actually want done?
3. **Run the 6-step flow** from the rulebook:
   - Step 1: Sensitivity gate: does data need to stay local?
   - Step 2: Pick the brain: Claude / Gemini / agent runner / local model?
   - Step 3: Pick the skill(s): match from the skill tables
   - Step 4: Pick the agent: does it need a specialist?
   - Step 5: MCP tools: any connectors needed?
   - Step 6: Communication rules: how to deliver?
4. **Show the route** in one short block:

```
Route: [brain] → [skill] → [agent if any]
Why: [one sentence]
```

5. **Then do the work.** Don't just route; execute unless the user only asked
   for the routing decision.

## Rules

- If the user typed `/route` with no task, ask what they want to route.
- If the user typed `/route [task]`, route AND execute the task.
- If sensitivity = local only and local can't handle it, STOP and say so.
- Never skip the sensitivity check; it is always Step 1.
- The routing decision must match the rulebook. Don't improvise.
- Show the route so the user sees where their task went.
