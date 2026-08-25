# clarify-to-decide

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Filter which questions are worth putting to the user, when the information
that settles a choice is theirs.

One of seven skills built on one rule: **reversal cost decides who decides.**

**The moment it owns.** Before any option exists. The user brings the choice,
and the information that settles it is theirs: their constraint, their
appetite for cost, or their taste.

**Fires on**

- "ask me clarifying questions" or "interview me first"
- "give me options and your pick"
- any installed interview skill that is about to work its whole tree. This
  skill governs which of its questions reach the user.

**Not for** a design dialogue an installed brainstorming skill owns, or a row
already in front of them.

**Leaves behind** only the questions whose answer changes the recommendation.
Then a pick, its strongest counter, and a row to paste forward.

## Why each line exists

One entry per requirement in `SKILL.md`: the failure it corrects.

**Why it is its own moment.** Every other skill in the set runs outward: the
agent holds the information and decides how much to hand back. This one runs
inward. The options do not exist yet, and the constraint of the user is what
settles them. The expand-the-row skill routes here in one branch, which
presupposes a decision already in front of the reader. The checkpoint skill
forbids the interview. The two failures it corrects both look like diligence:
a checklist whose answers change nothing, and a balanced survey with no pick.

- **It governs the rounds, it does not run them** — most machines that
  install this already have an interview skill. A second one produces two
  sets of round mechanics in one context window. This layer owns which
  questions survive and what returns with them. The fallback covers a machine
  with no interview skill. It is one clause, not a second interview.
- **A test, not a count (1)** — a cap on questions is satisfied by the four
  weakest. The counterfactual test removes them by construction. The clause
  about answers that sit in the tree bounds the survivors to things only the
  user holds. A question whose answer is one file away reads as an interview.
- **The obvious default is a decision (2)** — the same test at its other end.
  The reversal-cost block keeps it from cutting the questions that most need
  asking. The conversion carries its cost guard for that reason. The block
  stays in the body rather than behind a pointer. It is the clause a model
  reaches for when asking feels more respectful than deciding. The
  written-reverse test is what lets it cut a question cleanly: a default
  whose reverse writes is a decision, stated with that reverse.
- **Taste is asked here, defaulted in a run (2)** — the policy's taste clause
  says default it and mark it OPEN. This skill asks. Side by side the two read
  as drift. The difference is the moment: in a dialogue the user is present
  and the question costs a line, in a run it costs the run. One sentence names
  the moment so the clause and the skill stop reading as a contradiction.
- **Candidates, pick first, at most four (3)** — a bare question hands a
  blank page to the one person who cannot see the space. A pick placed last
  among equals reads as one more option. The requirement is on content only.
  How the round renders belongs to whoever runs it. Serial questions cost a
  turn each, and a reader under interview stops volunteering the constraint
  that settles the choice. The map is capped and conditional. A map of a
  space for someone who lives in it is padding, and it delays the part they
  came for.
- **Stop on the recommendation, not on the tree (4)** — the governing line.
  The stop condition of an interview skill is an emptied tree, every branch
  visited. Loaded beside this one, the exhaustive criterion wins by default,
  because asking is always safer than committing. Naming both halves is what
  makes the override legible. The skipped-answer escape exists because the
  other failure is a round stalled on an answer the user was never going to
  give.
- **The strongest counter, specified (5)** — unspecified, it degrades to a
  token caveat that reads as balance and carries nothing. Shared with the
  rest of the set on purpose.
- **A row, not a summary (5)** — chat is disposable. The fields are those of
  the decision log, so a conversational decision lands in the same shape as a
  run's.
- **Boundaries name roles, not skills** — the reader installs this directory
  alone, onto a machine whose interview, brainstorming, and expand-the-row
  skills this repo cannot know. The checkpoint exclusion is stated from this
  side too, because a reader who installed only one of the two needs it here.

## Tuning

A model that pads restores the checklist: the round grows past four
questions, and the map appears for a reader who plainly knows the space.
Sharpen the counterfactual test and the skip-the-map clause before you touch
anything else. A cap on the count alone is satisfied by the four weakest
questions.

A model that widens scope turns the find-it-yourself clause into an audit of
the whole repository before the first question. Bound it by naming what the
answer turns on, not by naming more places to look.

A model that stops early asks well and then declines to recommend, which
leaves a clean survey. Requirement 5 is the correction, and the
counter-argument requirement is the half that goes missing first.

A model that avoids commitment produces the subtler version of the same
failure. The pick appears only in the last sentence, carries no reason, and
is hedged into a tie. Watch for candidate lists where nothing is marked.

A model that over-defers asks about choices that were its own to settle,
because asking reads as respectful. Requirement 2 corrects that.

Where an installed interview skill does the asking, watch for its stop
condition surviving requirement 4. The round keeps going after the
recommendation stops moving. Sharpen requirement 4 rather than add rules
elsewhere.

Over-firing looks like this skill activating on a request that already
carries its own constraint, where the answer needed no round at all. If that
appears, sharpen the description toward the case where the information is
genuinely the user's, rather than add rules to the body.

## Install

```sh
npx skills add ken0nek/skills --skill clarify-to-decide
```

MIT.
