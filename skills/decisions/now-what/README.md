# now-what

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Orient a user who has lost the thread and asks what is in front of them.

One of seven skills built on one rule: **reversal cost decides who decides.**

**The moment it owns.** The checkpoint where the user has to decide and cannot
see what the decisions are.

**Fires on**

- "what do I do next", "where are we", "what is left", "what needs my
  decision"
- the same questions about a run, or about a plan or handoff doc they name

**Not for** generating options to choose between, or closing a finished run.

**Leaves behind** an answer they can act on, in three parts: what to know,
what to do, what only they decide.

## Why each line exists

One entry per requirement in `SKILL.md`: the failure it corrects.

**Why it is its own moment.** `generate-plan`, `generate-execution-prompt`,
`decide-and-log`, and `harvest-run` all assume the user knows the question.
This one answers *what is in front of me at all*, which arrives mid-run,
between runs, and in sessions that never had a plan. It mirrors
`decide-and-log`: that skill suppresses a hand-back, this one makes an
unavoidable hand-back legible. Folded together, one skill gets two entry
conditions with opposite outcomes.

- **Ground from the thing, not the conversation** — an answer assembled from
  chat is confident and consistent while wrong about a tree that moved.
  Neither party can tell. The line says "the thing itself" rather than "the
  tree and the run directory", because the question arrives as often where
  neither exists. An empty enumeration sends the answer back to the
  conversation.
- **Claims describe the past** — a plan, a status line, and what either party
  said earlier all read as present tense. That is how a stale "nothing is
  wired yet" survives.
- **Verified-versus-inferred marked inline** — otherwise the reader
  re-verifies everything, which is the work the question was asked to avoid.
  A parenthetical cannot be skipped as preamble.
- **One fact, not an interview** — five opening questions move the work back
  onto the reader.
- **One screen, depth on one decision** — the reader is disoriented. Depth
  spread across everything is indistinguishable from no depth.
- **Empty section is one line, and "nothing changed" is an answer** — a
  heading that must be filled gets padded.
- **Know is filtered by "would this change what they believe or choose"** —
  without the test, the section reverts to a summary of what they already
  have. Lead with a reframe, because one delivered fourth reads as trivia.
- **Name the thing, not its handle** — a reader who asks what to do next is
  the one who will not look up `L-3`.
- **Do is their list only** — a skill framed as *what you do next* pushes
  work at the reader that the agent can do itself. The policy governs
  choices, not tasks, so nothing else catches it. A longer list reads as
  thoroughness.
- **Their verification first** — it is the one class of work genuinely
  blocked on them. Ranking by unblocks-most buries it behind items the agent
  can do itself.
- **Ordered, time-boxed, one action over a checklist** — an unordered list
  returns the question that was asked. Models reach for the exhaustive
  checklist unless told otherwise.
- **Say what is closed** — shrinking the surface is half the value, and the
  reader cannot derive it without the re-read they are avoiding.
- **Stopping is a real recommendation** — asked what to do next, a model
  finds something, and polish reads as remaining work.
- **Decide runs the policy as a filter** — a reversible choice handed back at
  a checkpoint is over-asking in the costume of a status report. Naming the
  resemblance is what makes the filter fire. The filter carries the
  written-reverse test so a settled row reaches the reader with its reverse,
  not with a promise that one exists.
- **The filter is compressed, not the whole policy** — a report skill uses
  two of the policy's clauses: the classifier, and what it reserves for the
  user. The verbatim block also carries the five fields of the log and the
  plan-time conversion. A status report never reaches them, and every fire
  pays for them. The run-lifecycle skills embed it whole, because their
  reader opens with the file and nothing else.
- **Consequence per option, not labels** — a choice shown as two names
  cannot be decided by anyone outside the problem.
- **"Why it is theirs" is required** — without it, the reader cannot tell a
  reserved judgment call from the agent failing to decide. They ask *did you
  fix it, or is it mine*.
- **Settled work kept apart from open choices** — interleaving the two is
  the most reliable way to make the answer unreadable. It happens by default,
  because both "came up".
- **Close on their action** — an ending on an offer to continue hands back
  the problem the question raised.
- **The doc target is stated** — a doc grounded against its own status lines
  is grounded against nothing.

## Tuning

A model that pads will restore the recap: the Know section grows back into a
summary of the conversation, and the reply outgrows a screen. Sharpen the
would-this-change-what-they-choose test and the empty-section-collapses line
before you add anything else.

A model that widens scope turns grounding into an audit. It reads every file
in the repo before it answers, or opens the interview that the one-fact rule
forbids. Bound it by naming what the answer turns on, not by naming more
places to look.

A model that stops early skips the filter and hands back the whole open
list, because listing is cheaper than deciding. The filter corrects that.
Keep it in the body rather than behind a pointer.

A model already oriented around checkpoints tends to under-fire this skill on
a bare *what should we do next* mid-task. It reads it as an ordinary question.
That under-firing is usually right. The skill earns its load when the reader
is disoriented, not when they are mid-flow.

## Install

```sh
npx skills add ken0nek/skills --skill now-what
```

MIT.
