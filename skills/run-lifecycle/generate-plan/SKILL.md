---
name: generate-plan
description: Write or govern any implementation plan for a zero-context executor. Fires whenever a plan is about to be written, even when another plan-writing skill writes it (that skill runs inside this one), on "plan this" or "let's build X" once the design is settled, and on an existing plan that assumes the conversation that produced it.
license: MIT
---

# generate-plan

The entry step of a run. Turn the settled design into a plan for **the
stranger** — the fresh session that executes it after the context clears.

## Write the plan

An installed plan-writing skill writes it; this skill governs it. Run that
skill inside this step and layer the requirements below on it. Where it says
to stop and ask the user, the policy in requirement 5 governs. Where it closes
by asking which execution approach to use, the execution-prompt step answers
that (default: a fresh implementer subagent per task). With no such skill,
write the plan yourself to the same bar. On an existing plan, apply the
requirements to the file in place.

Source: `spec.md` in the run directory, the design dialogue's output; a
spec written elsewhere moves there first, so the close deletes it with the
run. With none, `brief.md` or the discussion so far. A continuation also
reads the prior run's handoff and notes — or, once that run is closed, the
decision records, workflow lessons, and backlog rows it graduated into.

Write to `plan.md` in the run directory — `docs/plans/<YYYY-MM-DD>-<slug>/`
by default, or wherever this repo keeps planning docs.

**The bar:** every task names its files, its steps, and a runnable
verification command with the exact output that proves it. Every choice is
made on the page — the name chosen, the step written out where "same as the
task above" would have gone. Test every section against one question: can
the stranger execute it?

The deliverable is the plan, handed to the user for review; executing it
belongs to the session after the clear.

## Requirements

1. **Context preamble**, first section. Whatever header the plan-writing
   skill produces, the preamble also states what "done" looks like and
   carries every constraint and prior decision the executor needs — a goal
   and a stack leave the stranger re-deriving both.

2. **One-way-door sweep**, before finalizing. List the decisions this work
   will force; classify each by reversal cost alone.
   - Cheap to reverse → decide it now. If you cannot state your pick and
     why, it is unresolved, not settled: on a surface the user judges, plan a
     task that builds two or three genuinely different versions (one named
     direction each) and log the choice OPEN — a STOP gate only where later
     work depends on the pick; off their surfaces, a bounded, costed spike
     task with the decision attached to its outcome.
   - Looks irreversible → convert it (a toggle, a flag, a parameter, both
     variants side by side) when the conversion is genuinely quick. Converted
     means decided: a settled row naming the default, since the user reviews
     the table before the clear. (Mid-run, with them absent, the policy below
     logs the same conversion OPEN.)
   - Genuinely expensive or impossible to reverse (shipped schema/API/wire
     shape, destructive migration, security or auth model, publishing or
     spending) → ask the user now. Deferred → a **STOP gate** in the plan:
     the task, the exact question, why it cannot be defaulted.
   - A measurement only the user can take — their device, account,
     terminal, production — that a later task's shape depends on → a STOP
     gate at that task, naming the measurement and the task it gates. One
     that nothing depends on is verification owed to the user at handoff,
     never a gate.

   Done when every "should I ask?" the executor could meet is planned here,
   and every taste question reaching the user comes with something to look
   at.

3. **Decision table**, a plan section. One row per decision already made —
   in the design dialogue (re-derived from its spec), in this sweep, by the
   user now, and carried from the run this continues (its OPEN rows stay
   OPEN): what was decided · options considered · default chosen and why ·
   how to reverse it · status (settled | OPEN — needs the user's decision).
   Every OPEN row is a STOP gate or marked safe to proceed without. One row,
   filled:

   > Drafts persist in SQLite · considered: SQLite / flat JSON / in-memory
   > · SQLite — survives crashes, and the dependency is already in the repo
   > · reverse: swap the store behind `DraftStore`; the JSON variant is ~40
   > lines · settled

   State that during execution the log continues in the run directory's
   `notes.md`.

4. **Verification already run.** The plan-writing skill specifies a command
   per task; this step makes it this repo's own and proves it runs. Run
   every one against the current tree before shipping the plan — an unrun
   command measures its own phrasing. State preconditions and mismatch
   behavior: starting commit (moved-but-clean tree vs dirty), toolchain and
   install assumptions, baseline test counts (a different count with 0
   failures → log and proceed; any failure → stop and fix within the task).
   A new suite names what each case catches both ways: the bug reintroduced
   and the line deleted — a default branch, a guard — that must also turn
   it red. Name the commit-message convention, including any standing
   trailer.

5. **Decision policy for execution** — a plan section with that title,
   holding the following verbatim: the two `--- policy block start/end ---`
   lines, the `text` fence, and the text between.

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

6. **Fresh-eyes check**, after writing. First against itself: every literal
   string a task writes, tested against every absence the plan asserts — no
   gate may forbid what a task produces; every interface a task changes,
   traced to who calls it as well as who parses its output. Then one
   subagent as the stranger, its entire context the plan file: what must it
   guess — terms, paths, assumed decisions? Without subagents, a fresh
   session on the file alone. Fix what it finds; rerun only for load-bearing
   gaps. Tell the user what it caught.

7. **Review tier.** Tag each task *mechanical* (exact-text or rote; one
   end-of-batch check covers a run of them) or *substantive* (logic,
   interfaces, anything a reviewer reasons about; full per-task
   verification); unclear → substantive. Define both tags in the plan, one
   line each.

8. **Order by volatility.** After the preamble: data-model changes, type
   interfaces, anything user-facing; mechanical work last. The user reviews
   once, before the clear.

Plan the work this change needs and stop. Over-specifying settled things
buries the open ones; over-splitting provable ones buries them in
checkpoints.
