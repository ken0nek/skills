---
name: harvest-run
description: Close a finished run — graduate its decisions, lessons, and follow-ups to their durable homes, then delete the run directory. Run after the work landed, the user read the handoff, and they answered its keep-or-change questions.
disable-model-invocation: true
license: MIT
---

# harvest-run

The last step of a run: graduate what is durable out of the run directory,
then delete it. Deleting without harvesting loses the why; harvesting
without deleting leaves a directory that conceals its own follow-ups.

Preconditions: the work landed, the user read the handoff, and they
answered its keep-or-change questions. Without those answers, ask; they are
the one input this close cannot derive. An abandoned run or a standalone
handoff doc closes the same way, the file playing the directory's part. With
no handoff, reconstruct the three lists below from the notes and plan, ask
the keep-or-change questions that reconstruction raises, and say so.

Read every file in the directory and the handoff. Map it into three homes,
adapting the paths to wherever this repo keeps each:

1. **Decisions** → `docs/decisions/<run date>-<slug>.md`: the settled §3
   rows as amended, plus the §4 rows the answers settle — chosen, rejected,
   why — in the shape of the docs already there. A §4 row still undecided is
   a follow-up.
2. **Workflow lessons** → §6 into the repo's `AGENTS.md`, one line each,
   every open one with one target from *executor* · *plan* · *skill*. A
   line targeting the executor is the one the next plan's executor
   contract carries, paste-ready. A lesson already applied graduates
   nowhere; the commit that applied it keeps it.
3. **Follow-ups**, each with its evidence: §8's undone items, §4 rows still
   the user's, §2 steps not run, §5 concerns worth tracking. Work beyond the
   current version → a row in `docs/ROADMAP.md`; near-term work → the issue
   tracker, or listed in your report for the user to file when you cannot
   write there. One that already shipped graduates nowhere.

Sections the mapping does not name die with the directory.

Then close, in this order:

1. Repair every reference to the run directory in code and in docs that
   claim current truth. Leave a reference inside a dated record, such as a
   decision record, as it stands: it records what that doc cited on its
   date, and repairing it falsifies the record.
2. Commit the graduated files and the repaired references, scoped to those
   paths.
3. Delete the run directory. It was never tracked, so the commit you just
   made is what survives of it; invoking this skill after answering the
   handoff is the user's yes to that deletion.

Report: the decision doc's path, the rows added, what you dropped as already
done, the follow-ups left for the user to file, the closing commit hash.
