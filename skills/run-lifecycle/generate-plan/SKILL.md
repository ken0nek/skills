---
name: generate-plan
description: Write or govern any implementation plan for a zero-context executor. Fires whenever a plan is about to be written, even when another plan-writing skill writes it (that skill runs inside this one), on "plan this" or "let's build X" once the design is settled, and on an existing plan that assumes the conversation that produced it.
license: MIT
---

# generate-plan

The entry step of a run. Turn the settled design into `plan.md` for **the
stranger**: the fresh session that executes it with only that file and the
repo.

An installed plan-writing skill writes the plan; this governs it. Run that
skill inside this step and add the requirements below. Where it says to
stop and ask, requirement 5 governs. Where it asks which execution approach
to use, answer: subagent-driven, or inline where no subagent tool exists,
either way in a fresh session whose opening message names `plan.md`. With
no such skill, write the plan yourself: every task names its files, its
steps, and a verification command with the output that proves it. On an
existing plan, apply the requirements in place.

Source: `spec.md` in the run directory (a spec written elsewhere moves
there), else `brief.md` or the discussion. A continuation also reads the
prior run's handoff and notes, or what they graduated into. Write `plan.md`
in the run directory: `docs/plans/<YYYY-MM-DD>-<slug>/` by default, or
wherever this repo keeps plans.

The deliverable is the plan, handed to the user for review. Executing it
belongs to the session after the clear. Test every section against one
question: can the stranger execute it without guessing?

## Requirements

1. **Done, stated first.** The opening section says what "done" looks like
   in terms the executor can check before it stops.

2. **One-way-door sweep.** List the decisions this work will force and
   classify each by reversal cost alone. Cheap to reverse → decide it now;
   if you cannot state your pick and why, it is unresolved: on an
   outward-facing surface the user judges by eye, plan a task that builds
   two or three named versions and log the choice OPEN; elsewhere, a
   bounded spike with the decision attached to its outcome. Looks irreversible → convert it (a flag, a parameter, both
   variants) when the conversion is quick; converted means decided. Genuinely
   irreversible → ask the user before handing the plan over, or a **STOP
   gate** in the plan: the task, the exact question, why it cannot be
   defaulted. A measurement only the
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

4. **Verification already run.** Run every task's verification command
   against the current tree before handing the plan over; an unrun command
   measures its own phrasing. State the starting commit, baseline test
   counts and what a mismatch means, the one command that runs the full
   gate, and the commit-message convention including any standing trailer.
   A new suite names what each case catches both ways: the bug
   reintroduced, and the line deleted that must also turn it red.

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
quick. For a surface the user judges by eye, the options are a throwaway
prototype with every variant behind one switcher (an installed prototyping
skill builds it); for a code or document shape, several candidates built
in parallel, judged against a rubric written before any is read, with the
best parts grafted into one (an installed arena-style skill runs it). If
keeping the options open is itself costly, it is a real one-way door:
stop, ask, and end your turn rather than ending on a promise.
```

--- policy block end ---

6. **Executor contract** — the plan's last section: the text inside the
   `markdown` fence between the two `--- contract start/end ---` lines
   below, its heading included, markers and fence left out. Fill
   `{{handoff path}}` with `handoff.md` in the run
   directory, or with a path outside the repo when the repo is public and
   the handoff will name strategy, other projects, or unpublished
   decisions. Replace `{{lessons}}` with the open rows of the lessons file
   (`docs/LESSONS.md` by default) that target the *executor*, one line
   each; with none, delete that line.

7. **Fresh-eyes check.** First against itself: every literal string a task
   writes against every absence the plan asserts; every interface a task
   changes traced to its callers and its parsers. Then one subagent as the
   stranger, its whole context the plan file: what must it guess? Fix what
   it finds; rerun only for load-bearing gaps. Tell the user what it caught
   when you hand the plan over.

8. **Order by volatility.** Data model, interfaces, and anything
   user-facing first; mechanical work last. The user reviews once, before
   the clear.

--- contract start ---

```markdown
## Executor contract

You are executing this plan with no other context. Run it through an
installed subagent-driven execution skill if there is one, else task by
task yourself. Where the spec differs from the plan, the plan wins, even
where a skill ranks the spec first; the decision table says why. Where
any skill says to stop and ask the user, the decision policy above
governs instead.

Keep `notes.md` beside this plan, appended at the moment things happen,
never in batches:
- The decision log the policy names: this plan's decision table, then
  one row per decision you make, in the policy's five fields. A ruling an
  execution skill records in its own ledger is copied here with its
  reverse; that ledger is deleted at the end, and this file is not.
- Deviations from the plan, and why.
- Surprises: anything that contradicted the plan's assumptions.
- Open questions for the user.

Text and code this plan supplies verbatim are claims about the tree: check
each against the tree before committing it, and log a mismatch you fix
as a deviation. A subagent's report is a claim: re-measure its numbers
before relaying them. Report only what a tool result from this session
shows, and say plainly what is not verified.

The user is not watching and cannot answer mid-run. Proceed through
reversible work without asking. Deliver the plan's scope: a flaw or a
better approach gets one line in notes.md and the plan continues as
written; don't narrow, widen, or swap it, and take no adjacent action it
did not ask for. End a turn only at a STOP gate, at a one-way door the
policy could not convert, or at completion; stopping means writing the
handoff below and ending on its question. A summary that announces the
next step, an offer to continue, and a list of decisions none of which
blocks the work are not stops: do the next thing instead.

{{lessons}}

At every stop and at completion:
1. Run the full gate. Green at completion; at a stop, list in §5 each red
   that a later task owns.
2. Reconcile the decision log both ways. Scan this session for judgment
   calls missing from it and add each, flagged as a log miss; an empty
   scan on nontrivial work is itself a miss, because something filled
   every gap the plan left. Then check each settled row against the
   working tree, noting the evidence; a row the tree contradicts is a
   coverage gap for the handoff's §3.
3. Write {{handoff path}} (at a stop, `handoff-task-<N>.md` beside it,
   named for the task it stopped before), true
   to what ran: real commands, numbers, and commit ranges. Keep every
   section; one with nothing to report reads "None." Tables and tight
   bullets; a decision that changes the user's product gets its own row.
   0. Snapshot — repo, branch, HEAD, working-tree state, push status, the
      date, and one copy-pasteable command that proves the deliverable
      green, with the numbers it just produced.
   1. Per-task table — what shipped, commits, key files.
   2. Verification checklist — checkbox steps the user runs; anything only
      their environment can verify (device, credentials, prod) marked as
      owed to them.
   3. Decisions you made — every settled row you added, as a keep-or-change
      question with its tradeoff and the evidence it landed; coverage gaps
      as reinstate-or-ratify questions.
   4. Decisions the user owns — every OPEN row, and why it stopped with
      them.
   5. Concerns — anomalies, near-misses, waived gates, verification debt.
   6. Workflow lessons — where this plan made you over-ask, decide
      silently, or guess, and what the next plan should fix.
   7. Where the detail lives — the plan, notes, and per-task reports (say
      if any were deleted).
   8. Next steps — the user's ordered list. At a stop it ends on the
      stop's question; at completion it ends with: once the work lands,
      close the run — graduate this directory's decisions, lessons, and
      follow-ups to their durable homes, then delete it.
4. Close with a five-line chat summary that links the handoff and names
   the most important decision the user owes.
```

--- contract end ---
