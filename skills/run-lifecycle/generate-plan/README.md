# generate-plan

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Write or govern any implementation plan for a zero-context executor.

One of seven skills built on one rule: **reversal cost decides who decides.**

**The moment it owns.** Plan time: every decision that a plan can settle
before the executor meets it.

**Fires on**

- a plan is about to be written, including when another plan-writing skill
  writes it (that skill runs inside this one)
- "plan this" or "let's build X", once the design is settled
- an existing plan that assumes the conversation that produced it

**Not for** the design dialogue that precedes a plan.

**Leaves behind** `plan.md`: a decision table, a one-way-door sweep, STOP
gates, a runnable verification per task, a review tier per task.

## Why each line exists

One entry per requirement in `SKILL.md`: the failure it corrects and, where
it came from outside, its source.

**The governance boundary.** This skill governs plan-writing. It does not
teach it. Generation is delegated to whatever plan-writing skill is
installed. The fallback is one "bar" paragraph. A fuller in-house guide
duplicates the frameworks that this layer composes with. The description
carries the run's entry trigger, so the run has one entry point. Dialogue-time
decisions are captured at plan time through requirement 3's re-derivation.
The flow's only read-back lives here. A continuation opens the prior run's
artifacts and carries its OPEN rows forward, as source material and as table
rows. Without it, the three things a close graduates into are write-only.
Artifacts are named rather than paths, because the closing step tells its
user to adapt those paths.

- **Layer, never replace** — an installed plan-writing skill can
  over-prescribe (bite-sized tasks, exact snippets). When plans come out
  bloated or rigid, suspect its prescriptiveness first.
- **The execution-approach question is pre-answered** — the plan-writing
  skill closes on a question that the flow already settles downstream.
- **The deliverable boundary** — a session that holds a finished plan and a
  default approach slides from writing into executing work the user never
  approved. This mirrors the execution-prompt skill's "do not execute".
- **The existing-plan path** — the description promises to fire on a plan
  that assumes its conversation. The body gives that promise a procedure.
- **Preamble carries the why (1)** — models perform better when they know
  the intent, and the executor has nothing but the file. A plan-writing
  skill's own header states goal and stack. What it leaves out is the finish
  line and the decisions already made, and that half is what this layer
  requires.
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
  clothes. The variants task and the spike give that state an action without
  a manufactured should-I-ask moment. The STOP gate appears only where later
  work depends on the pick. A converted door is settled here, where the
  policy logs it OPEN at run time. The user reviews the plan's table before
  the clear and is absent during execution.
- **The measurement gate (2)** — the sweep classifies by reversal cost. A plan
  whose later task depended on a measurement only the user can take argued at
  length that the hand-back was a gate at all. Naming the second earning
  condition spares the argument and keeps its test sharp: nothing depends on
  it, no gate.
- **The spec lives in the run directory** — a spec written beside the run
  directory outlived the close as an orphan. The harvest deletes the directory
  and repairs references to it, and the spec was neither. One directory is the
  whole record, and one deletion ends it.
- **Decision table (3)** — decisions become queryable state from day zero,
  instead of archaeology at handoff. The settled/OPEN split is the handoff's
  "decisions you made vs decisions the user owns", moved upstream. The filled
  row anchors a format that an abstract field list renders divergently. The
  `notes.md` binding keeps "the decision log" from floating.
- **Verification already run (4)** — the executor's grounded audit needs
  something to audit against, and the plan-writing skill specifies the
  command without ever running it. An unrun command measures its own
  phrasing: a check that fails on the base commit reports capitalization,
  not content. The requirement is stated tool-free, so that the planner
  finds the defect with whatever search it has. Preconditions, the tolerance
  rule, and the commit convention each close a gap that a fresh-eyes reader
  hits. The gaps: an unpinned baseline, and exact `-m` strings read as a ban
  on a standing trailer.
- **Deletion beside reintroduction (4)** — a plan named the bugs to
  reintroduce, and each turned the new suite red. The suite stayed green with
  either arm of the default mode deleted. Reintroduction proves a case fires.
  Deletion proves the suite covers the path the product depends on.
- **Policy verbatim (5)** — an alluded-to policy is no policy after the
  clear. The copy boundary is enumerated (markers, fence, text), because an
  unenumerated one is the literal-string ambiguity that requirement 6 exists
  to catch.
- **Fresh-eyes check (6)** — a separate reader with fresh context outperforms
  self-critique. This rehearses the clear while fixing is cheap (Thariq's
  comprehension quiz, aimed at the artifact). The self-consistency pass comes
  first. A stranger finds missing information. A plan that mandates text its
  own gate forbids is contradictory information, invisible task by task.
  The mechanism is named (a reader with no context), so that a harness
  without subagents substitutes a fresh session. Rerun only for load-bearing
  gaps, or the check loops on nitpicks.
- **Callers beside parsers (6)** — an audit asked who greps a message and
  concluded the test stubs needed no edit. The same change made a second
  command *invoke* the stub, and a pre-existing case went red inside the task.
  An interface has two audiences, and the self-check names both.
- **Review tier (7)** — a cost that the policy does not touch: verification
  ceremony multiplies with task count. Task boundaries are the plan-writing
  skill's own (a task is one test cycle, reached from either direction), so
  this layer adds only the tag. The tag lets the executor's cadence scale to
  how mechanical the task is. Untagged, a verifier subagent runs on each of a
  batch of trivial prose edits. The definitions travel in the plan, because
  the tag's reader is the stranger.
- **Volatility ordering (8)** — Thariq's implementation-plan pattern. The
  plan gets one human review, before the clear, and the review catches
  things only if the tweakable decisions sit on top.
- **Keep it lean** — a model that reasons hard elaborates past what the task
  needs, and a plan that over-specifies settled things buries the open ones.

## Tuning

These are requirements, not behavioral micromanagement: state them and trust
the model's judgment inside them. Requirement 2 spells out all three sweep
branches anyway. That is cheap insurance that the sweep covers what was
meant, rather than what the model judged was meant.

The "one subagent" in requirement 6 is load-bearing on a model that delegates
readily. One fresh-eyes subagent is the cap, and the check is on the
artifact, never on the model's own work.

On a model that pads the documents it authors, expect the plan to run long.
Reach for the "keep the plan lean" line early, and add "keep each task under
~15 lines" if it balloons anyway. An executor that stops early needs the
STOP-gate discipline pushed harder, so that the only stops are the declared
ones. One that widens scope needs the anti-gold-plating clause damped in.

## Install

```sh
npx skills add ken0nek/skills --skill generate-plan
```

MIT.
