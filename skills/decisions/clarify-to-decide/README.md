# clarify-to-decide

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Settle a choice the user brings, when no option has been laid out yet and
what decides it is theirs.

One of seven skills built on one rule: **reversal cost decides who decides.**

**The moment it owns.** Before any option exists. The user brings the choice,
and the information that settles it is theirs: their constraint, their
appetite for cost or risk, or their taste. Who made the list is the line
between this and the expand-the-row skill: when the agent already laid out
the options, the user is in front of a row; when the user arrives with the
choice and nothing has been expanded yet, the moment is this one.

**Fires on**

- "help me decide", "what would you do here", "ask me what you need to know"
- each question an installed interview or brainstorming skill is about to put
  to the user. This skill decides which of them reach the user and what
  travels with each.

Typed with the choice as the argument:
`/clarify-to-decide help me decide which of the two apps gets the next pass`.

**Not for** a row already in front of them, or for running the dialogue
itself.

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

**Why the body is short.** It keeps the survival test, the default-is-a-decision
clause, what travels with a question, the stop condition, and the close, and
leaves the method to the model. Lines that set a cadence or restated the
description sit under *Tuning* with the failure that would return them.

- **It governs the questions, it does not run the rounds** — most machines
  that install this already have an interview skill, and that skill owns the
  cadence: how many questions per message, how many rounds. A second set of
  round mechanics in one context window collides with the first, and the more
  conservative bound wins anyway. This layer owns which questions survive and
  what returns with them. The fallback covers a machine with no interview
  skill. It is one clause, not a second interview.
- **The description speaks the user's words** — the triggers are the phrases
  a user types when they bring a choice, plus the moment inside an interview
  skill where this layer applies. A trigger written in the vocabulary of the
  skill ("ask me clarifying questions") is one the user never types.
- **A test, not a count** — a cap on questions is satisfied by the weakest
  ones. The counterfactual test removes them by construction. The clause
  about answers that sit in the tree bounds the survivors to things only the
  user holds. A question whose answer is one file away reads as an interview.
- **The obvious default is a decision** — the same test at its other end.
  The written-reverse test is what lets it cut a question cleanly: a default
  whose reverse writes is a decision, stated with that reverse. The block
  stays in the body rather than behind a pointer. It is the clause a model
  reaches for when asking feels more respectful than deciding.
- **Taste is asked here, defaulted in a run** — the policy's taste clause
  says default it and mark it OPEN. This skill asks. Side by side the two read
  as drift. The difference is the moment: in a dialogue the user is present
  and the question costs a line, in a run it costs the run. "Because they are
  present and it costs a line" names the moment so the clause and the skill
  stop reading as a contradiction.
- **Candidates, pick first** — a bare question hands a blank page to the one
  person who cannot see the space. A pick placed last among equals reads as
  one more option. The requirement is on content only. How the round renders
  belongs to whoever runs it, including an interview skill that otherwise
  asks open questions with no menu. The map is capped and conditional. A map
  of a space for someone who lives in it is padding, and it delays the part
  they came for.
- **Stop on the recommendation, not on the tree** — the governing line.
  The stop condition of an interview skill is an emptied tree, every branch
  visited. Loaded beside this one, the exhaustive criterion wins by default,
  because asking is always safer than committing. Naming both halves is what
  makes the override legible. The skipped-answer escape exists because the
  other failure is a round stalled on an answer the user was never going to
  give.
- **The strongest counter, and "you argue, they decide"** — unspecified, the
  counter degrades to a token caveat that reads as balance and carries
  nothing. Shared with the rest of the set on purpose.
- **A row, not a summary** — chat is disposable. The fields are those of the
  decision log, so a conversational decision lands in the same shape as a
  run's.
- **Boundaries name roles, not skills** — the reader installs this directory
  alone, onto a machine whose interview, brainstorming, and expand-the-row
  skills this repo cannot know.

## Tuning

A model that pads restores the checklist: the round grows, and the map
appears for a reader who plainly knows the space. Sharpen the counterfactual
test and the skip-the-map clause before you touch anything else. A cap on the
count alone is satisfied by the weakest questions.

A model that widens scope turns the find-it-yourself clause into an audit of
the whole repository before the first question. Bound it by naming what the
answer turns on, not by naming more places to look.

A model that stops early asks well and then declines to recommend, which
leaves a clean survey. The close is the correction, and the counter-argument
is the half that goes missing first.

A model that avoids commitment produces the subtler version of the same
failure. The pick appears only in the last sentence, carries no reason, and
is hedged into a tie. Watch for candidate lists where nothing is marked.

A model that over-defers asks about choices that were its own to settle,
because asking reads as respectful. The default-is-a-decision clause corrects
that. The opposite drift also appears: a model that settles every question
itself, including one that is the user's appetite for cost or risk. Watch for
a reply that asks nothing while naming a choice as theirs.

Where an installed interview skill does the asking, watch for its stop
condition surviving the stop-on-the-recommendation line. The round keeps
going after the recommendation stops moving. Sharpen that line rather than
add rules elsewhere.

Over-firing looks like this skill activating on a request that already
carries its own constraint, where the answer needed no round at all. If that
appears, sharpen the description toward the case where the information is the
user's, rather than add rules to the body.

Lines the body no longer carries, each with the failure that returns it:

- **"At most four, in one round"** — restore a count only on a machine with
  no interview skill, and only when the direct round grows past what a reader
  answers in one reply.
- **"Where keeping both open is itself costly, it is a real one-way door"** —
  the conversion clause. Restore it if this skill starts offering a flag or
  toggle as the answer to a choice that is the user's.
- **"Inside a run the same taste is defaulted and marked OPEN"** — kept as
  "asked here because they are present". Restore the explicit contrast if a
  run starts stalling on taste questions this skill asked in dialogue.
- **The Boundaries section** — a design dialogue belongs to an installed
  brainstorming skill; a row already in front of them belongs to the
  expand-the-row skill; at a checkpoint, ask for the single fact the answer
  turns on and nothing more. Now carried by the description and the first
  paragraph. Restore it when the skill fires at a checkpoint or on a row.

## Install

```sh
npx skills add ken0nek/skills --skill clarify-to-decide
```

MIT.
