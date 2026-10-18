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
no handoff, reconstruct the three lists below from the notes and plan, put
the keep-or-change questions from that reconstruction, and say so.

Read every file in the directory and the handoff. Map it into three homes,
adapting the paths to wherever this repo keeps each:

1. **Decisions** → `docs/decisions/<run date>-<slug>.md`: the settled §3
   rows as amended, plus the §4 rows the answers settle — chosen, rejected,
   why — in the shape of the docs already there. A §4 row still undecided is
   a follow-up.
2. **Workflow lessons** → §6 into the lessons file (`docs/LESSONS.md` if
   none), newest first; applied ones marked, the rest open with one target
   from *execution prompt* · *plan* · *skill*. A row targeting the execution
   prompt is the line the next executor will read, paste-ready.
3. **Follow-ups** → `docs/BACKLOG.md`, each with its evidence: §8's undone
   items, §4 rows still the user's, §2 steps not run, §5 concerns worth
   tracking. One that already shipped graduates nowhere.

Sections the mapping does not name die with the directory.

Then: repair every reference to the harvested path; commit the run
directory if dirty (its paths only); `git rm` it; commit the harvest and the
deletion together, scoped to the graduated files, the repaired references,
and the deletion. Every byte stays in history.

Report: the decision doc's path, the rows added, what you dropped as already
done, the closing commit hash.
