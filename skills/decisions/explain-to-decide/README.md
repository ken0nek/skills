# explain-to-decide

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Expand one option far enough that the user can choose it.

One of seven skills built on one rule: **reversal cost decides who decides.**

**The moment it owns.** After a decision is correctly routed to the user and
before they can answer it. The argument was made and did not land.

**Fires on**

- they name a row of a list you gave them
- they ask for a choice in detail (examples, pros and cons, the actual diff)
  so that they can decide

**Not for** a plain explanation with no decision behind it, or the round of
questions owed when the settling information is theirs.

**Leaves behind** the option expanded: a real instance from their tree, the
change as a diff, the consequence under each option. Then a pick, and its
strongest counter.

## Why each line exists

One entry per requirement in `SKILL.md`: the failure it corrects.

**Why it is its own moment.** The checkpoint skill is capped at a screen and
spreads attention across everything open, which is the opposite instruction.
The diagnostic is the second ask: the same request arrives again with *using
examples* appended.

- **The target is a subject, not an instruction** — a quoted line of the
  agent's own is usually phrased as a directive (*say which of these to
  apply*). Obeying it produces a confident turn that answers a question
  nobody asked. Naming the target first bounds a wrong guess to one sentence.
- **Three misdiagnoses are sorted here** because the reader describes every
  kind of stuck the same way. Shape is routed by role because the reader
  installs this directory alone. Plain language is the branch that models
  resist. Adding depth feels like effort, restating feels like retreat, and
  depth on an unreadable answer compounds the failure.
- **One question, not a guess** — three pages on an assumed constraint cost
  the round and read as thorough.
- **Reversal cost guards the reader's attention, not the decision** — a
  well-formed request can arrive about a row that was never theirs to
  answer. Expanding it spends attention twice. The conversion carries its
  cost guard because almost anything can go behind a flag. An unguarded
  conversion swallows the one-way doors. The written-reverse test keeps the
  guard checkable: a row whose reverse the agent can write was never theirs.
- **Explain, never perform** — the attention guard licenses saying that a row
  was not theirs. Without this line, it licenses doing the work instead of
  answering, which the reader cannot undo by reading.
- **Read the source** — a row in a list the agent wrote is already a lossy
  compression. Expanding it from the conversation compresses it again, and
  the detail comes back confident and ungrounded. The return path is named
  because the conversation is always the nearer source.
- **That row only** — re-explaining the list is what made them name a row.
  Averaging attention across several rows reproduces the thinness.
- **The instance is theirs and locatable** — a generic case proves
  comprehension and answers nothing. An instance they cannot go and look at
  is an assertion. The line says "the thing" rather than "the file", because
  a rule in code vocabulary silently exempts sentences, settings, and cases.
  The constructed case is labelled, because an invented example presented as
  found is worse than either.
- **Diff, not description** — a sentence about a change carries the
  ambiguity that the change resolves, and the request names diffs
  explicitly. The extension to prose and config matters because that is
  where describing survives longest.
- **Consequence, pick, counter** — shared with the rest of the set. A
  two-name choice cannot be made from outside the problem. A survey returns
  the work. A pick without its strongest counter hides what the reader needs
  to overrule it.
- **Stop when they can answer** — a length cap on a depth skill defeats it.
  The bound is the decision. Closing on an offer to go deeper converts a
  decision they were about to make into one they hand back.

## Tuning

A model that pads reverts to elaboration: the reply grows without ever
reaching a file path or a diff. The instance and diff requirements correct
it. Keep both concrete and early, rather than add a length instruction,
which this skill cannot afford.

A model that widens scope re-opens the whole list instead of the named row,
or explains the domain around the row before it reaches it. Tighten the
only-that-one line first.

A model that stops early gives the instance and skips the pick, which leaves
a well-illustrated survey. The argue-and-they-decide clause is the
correction.

A model that avoids commitment states both options fairly and declines the
counter-argument. That reads as balance and functions as a refusal to help.
Watch for a recommendation that appears only in the final sentence and
carries no reason.

Over-firing looks like this skill activating on a plain request to explain
something, with no decision behind it. If that appears, sharpen the
description toward the decision frame and the named row, rather than add
rules to the body. The body is fine. The trigger is what widened.

## Install

```sh
npx skills add ken0nek/skills --skill explain-to-decide
```

MIT.
