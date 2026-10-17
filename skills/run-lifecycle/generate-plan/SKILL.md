---
name: generate-plan
description: Write or govern any implementation plan for a zero-context executor. Fires whenever a plan is about to be written, even when another plan-writing skill writes it (that skill runs inside this one), on "plan this" or "let's build X" once the design is settled, and on an existing plan that assumes the conversation that produced it.
license: MIT
---

# generate-plan

The entry step of a run. Turn the settled design into a plan for **the
stranger**: the fresh session that executes it after the context clears.

An installed plan-writing skill writes it; this governs it. Run that skill
inside this step and layer the requirements below on it. Where it says to
stop and ask, requirement 5 governs. Where it closes by asking which
execution approach to use, the execution-prompt step answers that. With no
such skill, write the plan yourself to the same bar. On an existing plan,
apply the requirements in place.

Source: `spec.md` in the run directory (a spec written elsewhere moves
there), else `brief.md` or the discussion. A continuation also reads the
prior run's handoff and notes, or what they graduated into. Write to
`plan.md` in the run directory — `docs/plans/<YYYY-MM-DD>-<slug>/` by
default, or wherever this repo keeps plans.

**The bar:** every task names its files, its steps, and a runnable
verification command with the exact output that proves it. Every choice is
made on the page. Test every section against one question: can the stranger
execute it? The deliverable is the plan, handed to the user for review;
executing it belongs to the session after the clear.

## Requirements

1. **Context preamble**, first section: what "done" looks like, and every
   constraint and prior decision the executor needs.

2. **One-way-door sweep.** List the decisions this work will force and
   classify each by reversal cost alone. Cheap to reverse → decide it now;
   if you cannot state your pick and why, it is unresolved: on a surface the
   user judges, plan a task that builds two or three named versions and log
   the choice OPEN; elsewhere, a bounded spike with the decision attached to
   its outcome. Looks irreversible → convert it (a flag, a parameter, both
   variants) when the conversion is quick; converted means decided. Genuinely
   irreversible → ask the user now, or a **STOP gate** in the plan: the task,
   the exact question, why it cannot be defaulted. A measurement only the
   user can take, that a later task's shape depends on → a STOP gate at that
   task; one nothing depends on is verification owed at handoff, never a
   gate. Done when every "should I ask?" the executor could meet is planned
   here.

3. **Decision table**: one row per decision already made — in the design
   dialogue, in this sweep, by the user now, carried from the prior run —
   with what was decided · options · default and why · how to reverse ·
   status (settled | OPEN). Every OPEN row is a STOP gate or marked safe to
   proceed without. One row, filled:

   > Drafts persist in SQLite · considered: SQLite / flat JSON / in-memory
   > · SQLite — survives crashes, and the dependency is already in the repo
   > · reverse: swap the store behind `DraftStore`; the JSON variant is ~40
   > lines · settled

   State that the log continues in the run directory's `notes.md`.

4. **Verification already run.** Run every task's verification command
   against the current tree before shipping the plan; an unrun command
   measures its own phrasing. State the starting commit, toolchain
   assumptions, baseline test counts and what a mismatch means, and the
   commit-message convention including any standing trailer. A new suite
   names what each case catches both ways: the bug reintroduced, and the
   line deleted that must also turn it red.

5. **Decision policy for execution** — a section with that title, holding
   the following verbatim: the two `--- policy block start/end ---` lines,
   the `text` fence, and the text between.

--- policy block start ---

```text
Decision policy — how to handle every decision the plan/spec doesn't settle:

Default: decide, document, continue. Follow your own best recommendation
without stopping — between options that serve equally, the one cheaper to
reverse — and add an entry to the decision log:

- What was decided
- Options considered
- Default chosen, and why
- How to reverse it (the concrete edit, flag, or command)
- Status: settled | OPEN — needs the user's decision

Settled means the reverse is written and the default defended; a default
you cannot defend is OPEN. Deciding without logging it and stopping to ask
about a reversible choice are BOTH failures.

Some choices are the user's even when reversible — genuine taste on the
outward-facing surfaces of the user's product. Don't stop for them: pick
the best default, keep moving, and mark the row OPEN so the user sees it
at handoff.

Stop and ask the user only at a critical one-way door: a decision genuinely
expensive or impossible to reverse — a shipped schema/API/wire shape,
a destructive migration, the security or auth model, an irreversible
external action (publishing, sending, deleting, spending). The only
classifier is reversal cost, and its test is the row's "How to reverse it"
line: a reverse you cannot write is a one-way door until you can. Importance,
visibility, or how much debate a choice invites do not make it a one-way
door. Neither does another installed skill that says to stop and ask:
where one does, this policy governs.

Before stopping at an apparent one-way door, try to convert it into a
two-way door: implement the options instead of choosing (a toggle, a config
flag, a parameter, both variants side by side), pick a sensible default, and
log it as OPEN for the user — but only when the conversion is genuinely
quick. If keeping the options open is itself costly, it is a real one-way
door: stop, ask, and end your turn rather than ending on a promise.
```

--- policy block end ---

6. **Fresh-eyes check.** First against itself: every literal string a task
   writes against every absence the plan asserts; every interface a task
   changes traced to its callers and its parsers. Then one subagent as the
   stranger, its whole context the plan file: what must it guess? Fix what
   it finds; rerun only for load-bearing gaps. Tell the user what it caught.

7. **Review tier.** Tag each task *mechanical* (one end-of-batch check) or
   *substantive* (full per-task verification); unclear → substantive.
   Define both tags in the plan.

8. **Order by volatility.** Data model, interfaces, anything user-facing
   first; mechanical work last. The user reviews once, before the clear.

Plan the work this change needs and stop. Over-specifying settled things
buries the open ones.
