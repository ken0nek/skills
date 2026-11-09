# generate-plan

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Write or govern any implementation plan for a zero-context executor.

One of six skills built on one rule: **reversal cost decides who decides.**

**The moment it owns.** Plan time: every decision that a plan can settle
before the executor meets it, and the contract the executor works under
when it meets the rest.

**Fires on**

- a plan is about to be written, including when another plan-writing skill
  writes it (that skill runs inside this one)
- "plan this" or "let's build X", once the design is settled
- an existing plan that assumes the conversation that produced it

**Not for** the design dialogue that precedes a plan.

**Leaves behind** `plan.md`: a decision table, a one-way-door sweep, STOP
gates, a runnable verification per task, the policy verbatim, and the
executor contract with its §0–8 handoff.

## Why each line exists

One entry per requirement in `SKILL.md`: the failure it corrects and, where
it came from outside, its source.

**The governance boundary.** This skill governs plan-writing. It does not
teach it. Generation is delegated to whatever plan-writing skill is
installed, and execution to whatever execution skill is installed. A
requirement survives here only where neither does the job to the same bar.
The fallback is one sentence of bar. The description carries the run's
entry trigger, so the run has one entry point. Dialogue-time decisions are
captured at plan time through requirement 3. The flow's only read-back
lives here: a continuation opens the prior run's artifacts and carries its
OPEN rows forward. Without it, the three things a close graduates into are
write-only.

**The plan is the executor's only file.** The executor opens in a fresh
session from a short message that names `plan.md`. Nothing is pasted, so
whatever the executor must obey travels inside the plan: the policy
(requirement 5) and the contract (requirement 6). A separate prompt file
duplicated the plan's policy, drifted from it, and needed its own
generator.

- **Layer, never replace** — an installed plan-writing skill can
  over-prescribe. When plans come out bloated or rigid, suspect its
  prescriptiveness first.
- **The execution-approach answer** — the plan-writing skill closes on a
  question the flow already settles. Subagent-driven keeps each task's
  context fresh. A fresh session keeps the planning conversation out of the
  executor, which is the condition every requirement here is written for.
- **The deliverable boundary** — a session that holds a finished plan and a
  default approach slides from writing into executing work the user never
  approved.
- **The existing-plan path** — the description promises to fire on a plan
  that assumes its conversation. The body gives that promise a procedure.
- **The spec lives in the run directory** — a spec written beside the run
  directory outlived the close as an orphan. One directory is the whole
  record, and one deletion ends it.
- **Done, stated first (1)** — a plan-writing skill's header states the goal
  and the global constraints. What it leaves out is a finish line the
  executor can check, and an executor without one either stops at a first
  implementation or keeps going past the scope.
- **One-way-door sweep (2)** — over-asking fixed at the root. Questions are
  front-loaded into the one session where the user is present. The
  classifier and the conversion come from the one-way / two-way door framing
  in the shareholder letters of Jeff Bezos. Buying answers early through
  cheap exploration is Thariq Shihipar's know-your-unknowns principle,
  distilled with sources in
  [unknowns-at-plan-time.md](references/unknowns-at-plan-time.md). The
  can-you-state-your-pick test separates *who decides* from *whether
  reasoning can resolve it*. A visual call on an outward surface usually
  cannot be reasoned out, and a default there is a deferral in a decision's
  clothes. The STOP gate appears only where later work depends on the pick.
  A converted door is settled here, where the policy logs it OPEN at run
  time: the user reviews the plan's table before the clear and is absent
  during execution.
- **The measurement gate (2)** — a plan whose later task depended on a
  measurement only the user can take argued at length that the hand-back was
  a gate at all. Naming the second earning condition spares the argument:
  nothing depends on it, no gate.
- **Decision table (3)** — decisions become queryable state from day zero,
  instead of archaeology at handoff. The settled/OPEN split is the handoff's
  §3 versus §4, moved upstream. The filled row anchors a format that an
  abstract field list renders divergently.
- **Verification already run (4)** — the plan-writing skill specifies each
  command and its expected output without ever running it. An unrun command
  measures its own phrasing: a check that fails on the base commit reports
  capitalization, not content. The baseline, the gate command, and the
  commit convention each close a gap a fresh-eyes reader hits: an unpinned
  baseline, a contract that says "run the full gate" with no gate named, and
  exact `-m` strings read as a ban on a standing trailer.
- **Deletion beside reintroduction (4)** — a new suite turned red on every
  reintroduced bug and stayed green with either arm of the default mode
  deleted. Reintroduction proves a case fires. Deletion proves the suite
  covers the path the product depends on. No plan-writing or review skill
  asks for the second.
- **Policy verbatim (5)** — an alluded-to policy is no policy after the
  clear. The copy boundary is enumerated (markers, fence, text), because an
  unenumerated one is the literal-string ambiguity requirement 7 catches.
  Execution skills ship their own stop list. The policy section is what
  makes an executor log a reverse beside every call, and what turns "ask
  before X" into "ask only if X cannot be reversed".
- **Executor contract (6)** — the one part of a run no installed skill
  defines, and the input `harvest-run` reads by section number. Each line:
  - *A fresh executor, the plan wins over the spec* — a fresh-eyes check
    once found the spec overriding two corrections the plan had measured.
    An execution skill that ranks the spec above the plan is overridden by
    name, or the executor holds two opposite authority rules.
  - *`notes.md`, at the moment things happen* — Thariq Shihipar's running
    implementation-notes pattern
    (https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns),
    plus *surprises*. A recap at the end is a reconstruction. An execution
    skill's own ledger records rulings with what they cost if wrong, but no
    reverse, and it is deleted when the run finishes; the copy rule keeps
    the row where the harvest finds it.
  - *Claims* — statements shipped verbatim from a plan were untrue of the
    tree, and subagent reports carried arithmetic that did not hold. The
    grounded-report line is adapted from Anthropic's guidance on long
    autonomous runs.
  - *Autonomy* — the vendor guidance for unattended runs agrees on one
    move: name the stops you want and the early stops you do not. The three
    named non-stops are the ones executors produce. The scope line covers
    both directions, because one executor class widens and another takes
    adjacent actions. `{{lessons}}` carries what the last harvest observed;
    an executor's failure mode is observed in a run, never cast in advance.
  - *Gate and reconcile at every stop* — scheduled on completion only, the
    seam review waited until after a long hand session; run at a gate, it
    found a defect in the plan's central feature. An empty reconcile scan is
    a miss, because a self-report under-reports by default.
  - *The handoff path is a slot* — a committed handoff in a public repo
    stays in history after the harvest deletes it. The planner can check
    whether the repo is public; the executor need not.
  - *§0–8, every section kept* — §3 and §4 re-render the decision log as
    the policy's settled/OPEN split: the user audits one and makes the
    other. §6 feeds the lessons file. §8's last item points at the close.
    `harvest-run` maps §2–§6 and §8 by number, so the list is never
    abbreviated, and an empty section reads "None." rather than vanishing.
- **Fresh-eyes check (7)** — a separate reader with fresh context
  outperforms self-critique, and the plan-writing skill's own self-review is
  explicitly not a subagent. This rehearses the clear while fixing is cheap.
  The self-consistency pass comes first: a plan that mandates text its own
  gate forbids is contradictory, invisible task by task. An interface has
  two audiences, callers and parsers, and a change that only checked who
  greps a message broke a test that *invoked* it. Rerun only for
  load-bearing gaps, or the check loops on nitpicks.
- **Volatility ordering (8)** — Thariq's implementation-plan pattern. The
  plan gets one human review, before the clear, and the review catches
  things only if the tweakable decisions sit on top.

## Tuning

These are requirements, not behavioral micromanagement: state them and trust
the model's judgment inside them. Requirement 2 spells out all three sweep
branches anyway. That is cheap insurance that the sweep covers what was
meant, rather than what the model judged was meant.

The "one subagent" in requirement 7 is load-bearing on a model that
delegates readily. One fresh-eyes subagent is the cap, and the check is on
the artifact, never on the model's own work.

On a model that pads the documents it authors, expect the plan to run long.
The plan-writing skill's own proportion check is the first lever; add "keep
each task under ~15 lines" if it balloons anyway.

The executor contract ships one text for every executor. Tune it through
the lessons file, never by carrying variants inside the contract. A
handoff §6 row that names the failure, harvested with the target
*executor*, becomes one line of the next plan's `{{lessons}}`. An executor
that stops early gets a push to keep working. One that widens scope gets a
spawn cap. A line aimed at the wrong failure is worse than none.

The reconcile's two directions fail in opposite ways. Push the session scan
on an executor that under-reports its own judgment calls. Push the
tree check on one that logs eagerly and drifts. Drop either half, and the
handoff re-renders a log that nobody checked.

Lines the body no longer carries, each with the failure that returns it:

- **"Every constraint and prior decision the executor needs"** in the
  preamble — the plan-writing skill's global constraints and the decision
  table carry both. Restore it if a plan's constraints reach the executor
  only through the spec.
- **Review tier per task** (*mechanical* vs *substantive*, and the
  contract's verification cadence scaled to it) — execution skills now
  review every task, batch small same-shape edits, and pick the reviewer's
  model by the diff. Restore it on a harness whose executor runs a full
  verifier on each of a batch of trivial prose edits.
- **"Plan the work this change needs and stop"** — the plan-writing skill's
  proportion check carries it. Restore it if plans over-specify settled
  things and bury the open ones.
- **Tradeoffs** as a notes category — the decision log's *options* field
  carries them. Restore it if handoffs lose the alternatives weighed.
- **"(Mid-run, with them absent, the policy below logs the same conversion
  OPEN)"** — restore it if a plan logs a converted door OPEN, or an executor
  logs one settled.
- **"Without subagents, a fresh session on the file alone"** — restore it on
  a harness where the fresh-eyes check gets skipped for want of a subagent.

## Install

```sh
npx skills add ken0nek/skills --skill generate-plan
```

MIT.
