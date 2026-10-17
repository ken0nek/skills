# decide-and-log

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Decide a reversible choice yourself, log it, and keep going.

One of seven skills built on one rule: **reversal cost decides who decides.**

**The moment it owns.** In the moment, in any session, in or out of a run:
the choice that nothing settled in advance.

**Fires on**

- you catch yourself about to end a turn on a question that is cheap to undo
- the user pushes back with "just decide" or "stop asking"
- a stretch of work resolved judgment calls that never reached the log

**Not for** a session that is ending. That session owes a handoff, not
another log entry.

**Leaves behind** a decision-log row, and a session that keeps moving.

## Why each line exists

One entry per requirement in `SKILL.md`: the failure it corrects.

- "Keep working" closes both the release and the sweep, because the session
  is mid-stall and needs a release, not a lecture. Said twice, once for each
  way in.
- The reversal-cost-only classifier and the conversion move (toggle, flag,
  parameter) come from the one-way / two-way door framing in the shareholder
  letters of Jeff Bezos. The conversion carries its cost guard because almost
  anything can go behind a flag. An unguarded conversion swallows the one-way
  doors it was meant to open. That is worst here of anywhere in the set: this
  skill fires mid-run, with no reviewer between the reasoning and the commit.
- The classifier has a test, writing the reverse. "Cheap to undo" is a
  judgment, and "we can change it later" is the phrase that hides a one-way
  door. A reverse that will not write is the door. A flag that makes it
  write is the conversion. The row already demands the reverse, so the test
  adds no field.
- The tie-breaker toward the cheaper reverse exists because the user is
  absent when the choice is made. Between routes that both serve, the one
  that keeps rollback beats the cleaner one. "Serve equally" keeps it from
  preferring a commented-out line to a deletion.
- "BOTH failures" keeps the correction symmetric. The fix for over-asking
  must not teach silent deciding.
- Status is two values and nothing in between. A row hedged as settled but
  open to a later override is exactly the ambiguity the field exists to
  remove. Genuine taste on the outward-facing surfaces of the user is OPEN.
  Anything you can defend under review is settled. A default with no defense
  beyond its commonness is OPEN: a guess dressed as a decision is the
  silent-decision failure the log exists to catch.
- The log has a fallback home because this skill also ships alone, outside
  any lifecycle. A standalone session has no run directory, and a row the
  user never sees is still a silent decision.
- The bulk sweep is the same correction at a different scale. One stalled
  choice and a stretch of unlogged ones are both the decision policy
  unapplied, so they are one skill rather than two. The list of what a
  reviewer counts as a decision gives literal-minded models concrete
  categories. They are the ones that survive into later work: data shapes,
  contracts, dependencies, the pattern the next file copies. A sweep that
  lists only naming and scope misses the architecture the user now owns. An
  empty sweep on nontrivial work is a miss, because something filled every gap
  the task left. The finding-is-not-a-decision line keeps corrections out of
  the log. The closing "keep working" stops the sweep from becoming an audit
  that ends the turn on a status report. That is the end-on-a-promise failure
  in another costume. Inside a run, the executor's completion reconcile covers
  this ground. So the sweep earns its place on the sessions that never had a
  prompt.
- The compressed paragraph is the whole of this skill's policy, and it names
  no file outside this folder. Installed alone, the skill gets only its own
  directory, so a pointer to the canonical text dangles. A mid-stall
  session needs the release anyway, not the full policy.
- One paragraph serves both entry paths. "You stopped, or are about to
  stop, on a choice" holds for a reader who stalled and for one about to,
  and the sweep paragraph names its own premise ("a stretch of work with no
  rows"), so neither reader meets an instruction whose premise is false.
- Both status values are named in the field list itself. A log is written by
  one session and read by another. With only OPEN on the page, every session
  invents its own word for the other state.

## Tuning

A session that stalls on reversible choices needs the explicit release.
"Keep working" is what resumes the turn, so keep it within reach for a model
that stops early. A model already oriented around checkpoints stalls this
way more rarely. When it does, one application is enough.

Lines the body no longer carries, each with the failure that returns it:

- **"Now answer your own question this way and proceed"** — the closing
  imperative of the release. Restore it if a model logs the row and then
  ends the turn instead of continuing, above all after a sweep.
- **The three branch headings** (stalled on one question · several calls
  unlogged · fires twice) — restore them if a sweep-entry reader starts
  hunting for a question to answer, or a stalled reader runs a sweep.
- **"Created if the run has none"** — restore it if a run directory without
  a decision log sends the row to the reply instead of creating the log.
- **"A default you cannot defend is OPEN"** — folded into "settled means the
  reverse is written and the default defended". Restore the explicit line if
  undefended defaults start arriving marked settled.

## Install

```sh
npx skills add ken0nek/skills --skill decide-and-log
```

MIT.
