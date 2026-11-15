# harvest-run

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Close a finished run. Graduate its decisions, lessons, and follow-ups to
their durable homes, then delete the run directory.

One of six skills built on one rule: **reversal cost decides who decides.**

**The moment it owns.** The close, once the work landed and the user
answered the handoff's keep-or-change questions.

**Fires on**

- invoked by name, and only by name. It deletes a directory, so it never
  fires on inference.

**Not for** a run still in flight, or one whose handoff the user has not read.

**Leaves behind** decision records, lesson lines in `AGENTS.md`, roadmap or
tracker rows, and no run directory.

## Why each line exists

One entry per requirement in `SKILL.md`: the failure it corrects.

- **Post-review, by construction** — the handoff is written when the session
  ends, before the user's review. A harvest at that point graduates defaults
  the user can still flip, and deletes the doc they are about to read. The
  keep-or-change answers are the input.
- **User-invoked, alone in the set** — this skill deletes a directory, and a
  model that reaches for it on inference guesses the user's answer. The
  spec has no invocation field, so each harness is told in its own place:
  `disable-model-invocation` for Claude Code, `agents/openai.yaml` for
  Codex. The precondition also stays in the body for harnesses with
  neither.
- **The standalone doc plays the directory's part** — the concealment
  argument is about kept artifacts, not directories.
- **The died-run branch reconstructs, then asks** — otherwise the skill
  reads as refusing the branch it documents.
- **The mapping is executed here and stated nowhere else** — a copy inside
  every handoff rots the moment the mapping changes. The handoff's §8 carries
  only the pointer. The three homes name the content they take, so a handoff
  whose sections are not numbered still maps by content.
- **Why delete** — a kept run directory anchors future work to a spec that
  nobody maintains, and conceals the live follow-ups buried in its §8.
- **Lessons go to `AGENTS.md`** — an open lesson is a rule for how to work in
  the repo, and `AGENTS.md` is where every agent already reads those. An
  applied lesson graduates nowhere: the commit that applied it is its record.
- **Follow-ups split by horizon** — near-term work belongs in the issue
  tracker the user triages; work beyond the current version belongs in the
  one roadmap file. A single backlog file mixed the two and duplicated the
  tracker.
- **The already-shipped filter** — a roadmap row that ships leaves entirely.
  The filter is applied at the moment follow-ups are most often found already
  done.
- **Reference search before the deletion** — a harvest that skips it leaves
  code or a current-truth doc pointing at a run that is gone.
- **Dated records are not repaired** — a decision record cites what existed
  on its date. Rewriting its reference makes it claim a citation it never
  made, and the record is worth only its accuracy about that date.
- **Lesson targets are a fixed set** — *executor*, *plan*, *skill*. A
  free-text "candidate target" left the next plan with nothing to select
  on. Executor tuning then had no path back into the run, and surfaced
  instead as a question to the user. A row targeting the executor is
  written as the line the executor will read.
- **The commit pathspec-scoped** — an unscoped commit swallows another
  session's staged files, and the harvest's hash stops meaning "what
  graduated".
- **Invocation is the yes to the deletion** — the run directory is never
  tracked, so deleting it is a real one-way door on the policy's list. The
  preconditions and name-only invocation make it the user's call, and the
  graduations are committed first, so nothing durable goes with the folder.
  The sentence states that, so a policy-carrying session does not stop at
  the gate this skill exists to walk through.

## Tuning

Any model can run this. It is a short, bounded session against files that are
already written. On a model that pads the files it authors, cap the length
of the decision doc. It is a distillation (chosen · rejected · why), not a
transcript, and a decision doc is exactly the agent-authored shape that pads
most. On a model that stops early, the risk is a harvest that graduates the
artifacts and then reports back without deleting. The close is not done
until the commit exists and the run directory is gone.

Lines the body no longer carries, each with the failure that returns it:

- **The content fallback** — "by section number, or by content where its
  sections are not numbered: settled decisions, decisions still the user's,
  workflow lessons, unfinished follow-ups, verification owed to the user,
  concerns worth tracking". Restore it when a handoff without numbered
  sections loses its verification-owed or concerns material in the harvest.
- **"A run under review stays live and keeps its directory"** — the
  preconditions carry it. Restore it if a harvest starts on a run whose
  handoff the user has not answered.
- **"Check each against the code and its git history first"** — folded into
  "one that already shipped graduates nowhere". Restore the explicit check if
  shipped follow-ups start landing in the backlog.
- **"Commit the run directory if dirty; `git rm` it … Every byte stays in
  history"**, and the two-way-door wording before it — true only while run
  directories were committed. Restore both on a repo that commits them.
- **The lessons file and the backlog file** (`docs/LESSONS.md`,
  `docs/BACKLOG.md`) — restore them as homes on a repo that keeps those
  files instead of `AGENTS.md` lines and a roadmap.

## Install

```sh
npx skills add ken0nek/skills --skill harvest-run
```

MIT.
