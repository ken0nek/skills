---
name: decide-and-log
description: Decide a reversible choice and log it. Use when a turn is about to end on a question whose answer is cheap to undo, when the user pushes a stalled session back with "just decide", "stop asking", or "log the decision", or when a stretch of work has resolved judgment calls that never reached the log. Not for a session that is ending — an ending session owes a handoff, not another log entry.
license: MIT
---

# decide-and-log

The release for a session that stalled on a reversible choice.

## If you stalled on one question

You stopped to ask about a reversible choice. The only classifier is
reversal cost, tested by writing the reverse: one you can write — or make
writable with a quick toggle, flag, or parameter — is yours; where keeping
both open is itself costly, it is a real one-way door. The user gets only
true one-way doors: decisions genuinely expensive or impossible to reverse.

On a choice that is yours, decide with your own best recommendation now —
between options that serve equally, the one cheaper to reverse — log it,
and continue working. The row:

- What was decided
- Options considered
- Default chosen, and why
- How to reverse it
- Status: settled | OPEN — needs the user's decision

It goes in the run's decision log, created if the run has none. With no
run directory, it goes in the session's notes file, or failing that in
your reply — wherever the user will see it. Genuine taste on the
outward-facing surfaces of the user's product is decided the same way,
with its status OPEN. Settled means the reverse is written and the default
defended; a default you cannot defend is OPEN.

Stopping to ask about a reversible choice and deciding without logging it
are BOTH failures. Now answer your own question this way and proceed.

## If several calls went unlogged

A stretch of work resolved without a row gets a sweep: scan the work so
far for judgment calls a reviewer would count as decisions, and log each
with the same five fields, marking OPEN anything genuinely the user's. The
categories: data shapes and storage, naming, API contracts and their error
behavior, dependencies added, concurrency or performance trade-offs, scope
cuts, workarounds, skipped steps, any pattern later code will imitate.
Only judgment calls belong in the log; a finding you turned up is
evidence, not a decision. An empty sweep on nontrivial work is a miss, not
a pass: something filled every gap the plan left. Then keep working — the
sweep is a checkpoint, not an ending.

## If this fires twice

A second firing means the prompt or standing instructions this work
started from lack the decision policy; the classifier and the row in the
first section above are the block that is missing. Tell the user so as a
workflow lesson: the fix goes in the prompt that starts the next stretch
of work.
