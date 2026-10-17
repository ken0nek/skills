---
name: decide-and-log
description: Decide a reversible choice and log it. Use when a turn is about to end on a question whose answer is cheap to undo, when the user pushes back with "just decide" or "stop asking", or when a stretch of work resolved judgment calls that never reached the log. Not for a session that is ending, which owes a handoff.
license: MIT
---

# decide-and-log

You stopped, or are about to stop, on a choice. Reversal cost is the only
classifier: a reverse you can write — or make writable with a quick toggle,
flag, or parameter — makes the choice yours. Decide it with your own best
recommendation, the cheaper-to-reverse option between equals, log it, and
keep working. Theirs: a reverse you cannot write; and taste on their
product's outward surface, which you decide the same way and mark OPEN.

The row, wherever they will see it — the run's decision log, else the
session's notes, else your reply:

- What was decided
- Options considered
- Default chosen, and why
- How to reverse it
- Status: settled | OPEN — needs the user's decision

Settled means the reverse is written and the default defended. Stopping to
ask about a reversible choice and deciding without logging it are both
failures.

A stretch of work with no rows gets a sweep: every judgment call a reviewer
would count — data shapes, naming, contracts and their error behavior,
dependencies, performance trade-offs, scope cuts, workarounds, patterns
later code will copy — logged the same way. A finding is evidence, not a
decision. An empty sweep on nontrivial work is a miss. Then keep working.

If this fires twice in one session, the prompt that started the work lacks
the policy. Say so as a workflow lesson.
