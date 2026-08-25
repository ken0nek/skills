# Unknowns at plan time

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

A distillation of the planning moves this skill borrows, written from
scratch in our own words.

## The method

**Planning changes when you meet the gaps between the plan and the work.**
A brief and a plan close the gaps you can name. The rest surface during
implementation, where a wrong guess has code built on top of it. So a plan
has two jobs: specify what is settled, and schedule the discovery of what is
still unsettled, early and cheaply.

### Buy the answers before implementation locks them in

Two kinds of question resist thinking harder. One is anything you recognize as
right or wrong on sight but cannot state in advance. The other is anything in
an area you have not worked in. For those, the plan buys the answer instead of
guessing at it. The purchase is a small mockup, a throwaway spike, or a set of
distinct variants to react to. Each is a bounded, costed task inside the plan,
with a decision attached to its outcome. The economics are the whole argument.
A probe run before implementation costs a fraction of the rework when a spec
change lands after the code exists. Small differences in what was wanted imply
very different code, and work an agent already built on is harder to undo than
to skip.

### Check the artifact with fresh eyes

An author cannot tell whether a document stands alone: they know what they
meant, and their eyes fill the holes. So hand it to a reader with no context
and ask what it has to guess to act on it. That is the terms, the paths, the
decisions assumed but never stated. What that reader names is the list of gaps
a fresh executor session hits.

The same check appears at the end of a piece of work, aimed at the person
rather than the plan. After a long session, reading the diff is a thin kind of
understanding. So the author has the agent test whether they can explain what
changed, and a failed test holds the merge. Reviewers begin with the same gaps
the author began with, which is why finished work travels with an explainer.
Moving the check upstream onto the plan is the cheap version of all of that.
The reader is a subagent, the artifact is text, and a gap costs one edit to
fix.

### Order by what the reader is most likely to change

A plan gets one human review, and attention runs out before the document
does. Put the volatile material first: how the data is shaped, the interfaces
between the parts, anything the user will see and react to. Put the rote
mechanical work at the bottom, since that is the part the reviewer already
trusts you with. Ordering by likelihood of revision is what makes a single
pass catch the things worth catching.

## How this skill applies it

- The one-way-door sweep schedules the exploration at plan time. On a surface
  the user judges, it plans a task that builds two or three genuinely
  different versions for them to react to. Off their surfaces, it plans a
  bounded, costed spike with the decision attached to its outcome. The
  alternative is a taste call defaulted, or a task the executor widens
  mid-run.
- The fresh-eyes check dispatches one subagent whose entire context is the
  plan file. Its findings get fixed before the plan ships.
- Requirement 8 is the volatility ordering: the context preamble, then the
  data-model, interface, and user-facing decisions, then the mechanical work.

## Attribution

- **Author:** Thariq Shihipar, Anthropic
- **Primary source:** "A field guide to Claude Fable 5: Finding your
  unknowns", published 2026-07-06 —
  https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns
- Read the source for the author's own framing, examples, and prompts.
