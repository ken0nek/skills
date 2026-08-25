# decide-and-log

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Decide a reversible choice yourself, log it, and keep going.

One of seven skills built on one rule: **reversal cost decides who decides.**

**The moment it owns.** In the moment, in any session, in or out of a run:
the choice that nothing settled in advance.

**Fires on**

- you catch yourself about to end a turn on a question that is cheap to undo
- the user pushes a stalled session back with "just decide", "stop asking", or
  "log the decision"
- a stretch of work resolved judgment calls that never reached the log

**Not for** a session that is ending. That session owes a handoff, not
another log entry.

**Leaves behind** a decision-log row, and a session that keeps moving.

## Why each line exists

One entry per requirement in `SKILL.md`: the failure it corrects.

- The compressed policy ends in an imperative, "answer your own question this
  way and proceed", because the session is mid-stall and needs a release,
  not a lecture.
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
- The section headings are branch conditions, not a sequence. The release
  paragraph is true only for a reader who stalled on a question. A
  sweep-entry reader who meets "answer your own question" has no question to
  answer. Each entry path gets a section whose premise holds for it.
- Both status values are named in the field list itself. A log is written by
  one session and read by another. With only OPEN on the page, every session
  invents its own word for the other state.
- "Creating the log if the run has none" closes the middle rung of the
  fallback chain. A run directory whose log file does not exist yet otherwise
  dead-ends between "log it in the run's log" and "no run directory at all".

## Tuning

A session that stalls on reversible choices needs the explicit release. The
closing imperative is what resumes the turn, so keep it within reach for a
model that stops early. A model already oriented around checkpoints stalls
this way more rarely. When it does, one application is enough.

## Install

```sh
npx skills add ken0nek/skills --skill decide-and-log
```

MIT.
