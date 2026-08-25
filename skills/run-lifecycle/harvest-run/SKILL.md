---
name: harvest-run
description: Close a finished run — graduate its decisions, lessons, and follow-ups to their durable homes, then delete the run directory. Run after the work landed, the user read the handoff, and they answered its keep-or-change questions.
disable-model-invocation: true
license: MIT
---

# harvest-run

The last step of a run: graduate what is durable out of the run directory,
then delete it. Deleting without harvesting loses the why; harvesting without
deleting leaves a directory that conceals its own follow-ups.

## Preconditions

The work landed, the user read the handoff, and they answered its
keep-or-change questions — "keep every §3 default as logged" or the specific
§3 and §4 rows they change. Without those answers, ask; they are the one input
this close cannot derive. A run under review stays live and keeps its
directory.

An abandoned run, or a standalone handoff doc, closes the same way — point at
the file and it plays the directory's part, deletion included. With no
handoff, reconstruct the three lists below from the notes and plan, put the
keep-or-change questions from that reconstruction, and say so.

## Harvest

Read every file in the directory, and the handoff wherever the execution
prompt put it. Then map the handoff into the three homes below — by section
number, or by content where its sections are not numbered: settled decisions,
decisions still the user's, workflow lessons, unfinished follow-ups,
verification owed to the user, concerns worth tracking. Sections the mapping
does not name die with the directory.

1. **Decisions** → one new doc at `docs/decisions/<run date>-<slug>.md`: the
   settled §3 rows as amended, plus the §4 rows the answers settle — chosen,
   rejected, why — in the shape of the docs already there (a plain dated doc
   where none exist). A §4 row still undecided is a follow-up.
2. **Workflow lessons** → §6's rows into the lessons file (`docs/LESSONS.md`
   if none), in its entry format, newest first; a lesson already applied
   to a prompt or skill is marked applied, the rest stay open with one
   target from a fixed set — *execution prompt*, *plan*, *skill*. A row
   targeting the execution prompt is one line of instruction to the next
   executor, written to be pasted as-is.
3. **Follow-ups** → rows in `docs/BACKLOG.md` (create it if new) under the
   fitting heading, each with its evidence: §8's undone items, §4 rows
   still the user's, §2 steps the user has not run, §5 concerns worth
   tracking. Check each against the code and its git history first; one
   that already shipped graduates nowhere.

Adapt the three paths to wherever this repo keeps decision records, lessons,
and backlog.

## Delete

1. Search this repo for references to the harvested path; repair or remove
   each.
2. If the run directory is uncommitted or dirty, commit it first — that
   directory's paths only.
3. `git rm` it, and commit the harvest and the deletion together, scoped to
   the graduated files, the repaired references, and the deletion. With step
   2 behind it, the deletion is a two-way door: every byte stays in history.

Report: the decision doc's path, the lessons and backlog rows added, what you
dropped as already done, and the closing commit hash.
