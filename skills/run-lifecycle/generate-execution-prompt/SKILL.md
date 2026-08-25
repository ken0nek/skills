---
name: generate-execution-prompt
description: Turn an approved plan into the execution prompt file that opens a fresh executor session. Use after plan approval and before the context clear, on a plan with no execution prompt yet, or on "write the orchestrator prompt".
license: MIT
---

# generate-execution-prompt

The step between plan approval and the context clear. Its reader is **the
stranger** — the executor session that opens with this file and the repo,
nothing else. Your only deliverable is the file; never execute the plan.

## Generate

1. Read `plan.md` in the run directory fully —
   `docs/plans/<YYYY-MM-DD>-<slug>/` by default, or wherever this repo keeps
   planning docs. A lone plan file gets a run directory created beside it
   and moves in as `plan.md`.

2. Write `execution-prompt.md` beside it from the template below — the whole
   first message the user pastes. The `text` fence belongs to this file; the
   output opens with the HTML comment.
   - Fixed text stays verbatim. Fill every `{{slot}}` from the plan; expand
     `{{run dir}}` and `{{code repo root}}` to real paths everywhere (they
     can differ); delete slot lines that do not apply.
   - `{{mission}}`: 3–6 sentences from the plan's context preamble, written
     for a reader who has only the file.
   - `{{stop gates}}`: every STOP gate from the plan, with its exact
     question and why it cannot be defaulted — a gate on a measurement names
     the measurement and the task it gates; none → "None — no pre-planned
     stops." One gate: "STOP before task 4 — it drops `legacy_id` from
     `events`. Ask: does any external consumer still read `legacy_id`? Not
     defaultable: the drop is destructive and the consumers live outside
     this repo."
   - `{{repo gate commands from the plan}}`: the plan's full gate, or the
     repo's build, test, and lint invocations — say so in your report.
   - `{{executor addendum}}`: the open rows of this repo's lessons file
     (`docs/LESSONS.md` by default) whose target is the execution prompt,
     each as one line of instruction to the executor; none → delete the
     slot line. Lessons are the only source: an executor's failure mode is
     observed in a run, never cast in advance.
   - `{{handoff path}}`: `{{run dir}}/handoff.md`. When the code repo is
     public, a private home outside it — the run's other artifacts stay
     where they are, and the handoff's §7 points back at them.
   - Policy block: compare its text with the plan's "Decision policy for
     execution" section, ignoring the plan's `--- policy block start/end ---`
     markers and fence. On a difference, tell the user and use the plan's
     text, without markers or fence. No policy section → keep the template's
     and note it.

3. Fresh-eyes check: one subagent as the stranger, told to answer only (the
   file is built to start a run), its context the generated file and the
   repo files it points to — "Following only this prompt, can you start
   executing correctly? List everything you must guess." Without subagents,
   a fresh session on the file alone. Fix what it finds; rerun only for
   load-bearing gaps.

4. Report: the file path, what the check caught, and the user's next steps
   (clear the context, paste).

--- TEMPLATE START ---

```text
<!-- Run: a fresh session, same model and effort as the one that wrote the
plan, cwd {{code repo root}}. Paste this whole file as the first message. -->

You are executing a pre-approved implementation plan. {{mission}}

Ground truth — read before anything else:
- {{run dir}}/plan.md — the contract; read it fully first.
- {{run dir}}/spec.md or brief.md — the deeper why, if you need it. Where
  it differs from plan.md, plan.md wins; its decision table records why.
  {{delete if absent}}
- {{run dir}}/notes.md — your working file; create it now (see below).
- {{branch/worktree instruction from the plan, if any}}
- Your working directory for every plan command: {{code repo root}} — cd
  there first. Artifact paths in this prompt are absolute on purpose; the
  plan's relative paths and commands resolve against {{code repo root}}.

Execute the plan task-by-task. If a subagent-driven execution skill is
installed, run the plan through it; otherwise dispatch a fresh implementer
subagent per task. Every dispatch states the channel its report returns
on. Where that skill — or any skill — says to stop and ask the user, the
decision policy below governs instead.

Decision policy — how to handle every decision the plan/spec doesn't settle:

Default: decide, document, continue. Follow your own best recommendation
without stopping — between options that serve equally, the one cheaper to
reverse — and add an entry to the decision log:

- What was decided
- Options considered
- Default chosen, and why
- How to reverse it (the concrete edit, flag, or command)
- Status: settled | OPEN — needs the user's decision

Settled means the reverse is written and the default defended; a default
you cannot defend is OPEN. Deciding without logging it and stopping to ask
about a reversible choice are BOTH failures.

Some choices are the user's even when reversible — genuine taste on the
outward-facing surfaces of the user's product. Don't stop for them: pick
the best default, keep moving, and mark the row OPEN so the user sees it
at handoff.

Stop and ask the user only at a critical one-way door: a decision genuinely
expensive or impossible to reverse — a shipped schema/API/wire shape,
a destructive migration, the security or auth model, an irreversible
external action (publishing, sending, deleting, spending). The only
classifier is reversal cost, and its test is the row's "How to reverse it"
line: a reverse you cannot write is a one-way door until you can. Importance,
visibility, or how much debate a choice invites do not make it a one-way
door. Neither does another installed skill that says to stop and ask:
where one does, this policy governs.

Before stopping at an apparent one-way door, try to convert it into a
two-way door: implement the options instead of choosing (a toggle, a config
flag, a parameter, both variants side by side), pick a sensible default, and
log it as OPEN for the user — but only when the conversion is genuinely
quick. If keeping the options open is itself costly, it is a real one-way
door: stop, ask, and end your turn rather than ending on a promise.

STOP gates — the only pre-planned stops:
{{stop gates}}

Running notes — maintain {{run dir}}/notes.md as you work, updating at
the moment things happen, never in batches:
- Decision log: start from the plan's decision table (start it empty if
  the plan has none); add a row per decision you make (the five fields
  above).
- Deviations: where you departed from the plan, and why.
- Tradeoffs: alternatives you considered on the way.
- Open questions: anything the user should confirm or revise.
- Surprises: anything that contradicted the plan's assumptions.

Verification discipline — scaled to the plan's review tier (treat any
untagged or unclear task as substantive):
- Substantive task: it's done only when its verification command from the
  plan has run green in this session. Fix what breaks before moving on;
  record surprises in notes.
- Mechanical tasks: batch them. Run the plan's verification command at the
  end of the batch, not per task. A batch is a run of mechanical tasks
  with no substantive task between them.
- Text and code the plan supplies verbatim are claims about the tree;
  check each against the tree before it is committed. A subagent's report
  is a claim, not a measurement; re-measure its numbers before relaying
  them.
- Before reporting progress, audit each claim against a tool result from
  this session. Only report work you can point to evidence for; if
  something is not yet verified, say so explicitly. If tests fail, say so
  with the output; when something is done and verified, state it plainly
  without hedging.

You are operating autonomously: the user is not watching in real time and
cannot answer mid-task. For reversible work that follows from the plan,
proceed without asking. Deliver the plan's scope: if the plan looks wrong or
you see a better approach, say so in one line in notes.md and continue as
planned — don't quietly narrow, widen, or transform it, and don't take
adjacent actions the plan didn't ask for. Before ending a turn, check your
last paragraph: if it is a plan, a question, or a promise of work not yet
done, do that work now. End a turn only at a STOP gate, a true one-way
door the conversion could not make two-way, or completion.
{{executor addendum — one line per lesson targeting the execution prompt;
delete when none}}

At a STOP gate and on completion: run the full gate ({{repo gate commands
from the plan}}) and confirm green. Then reconcile the decision log in both
directions. First, scan this session for judgment calls missing from the
log and add each as a row flagged as a log miss; an empty scan on
nontrivial work is a miss itself, because something filled every gap the
plan left. Then check each settled row against the working tree — the
decision is actually in the shipped work, and later work kept it — noting
the evidence; a row the tree contradicts is a coverage gap for §3 below.
If the handoff names strategy, other projects, or unpublished decisions,
it belongs somewhere PRIVATE, never in a public repo — {{handoff path}} was
set with that in mind. Then write
{{handoff path}} — at a gate, handoff-<gate>.md beside it — accurate to
what actually ran: cite the real commands, numbers, and commit ranges, and
be explicit about what is NOT verified:
0. Snapshot — repo/branch/HEAD, working-tree state, push/publish status,
   the date, and ONE copy-pasteable command that proves the deliverable
   green, with the numbers it just produced.
1. Per-task table — what shipped, commits, key files.
2. Verification checklist — concrete checkbox steps the user runs
   themselves; anything only verifiable in their environment (device,
   credentials, prod) called out as owed to them.
3. Decisions you made — every settled row you added to the decision log,
   each framed as a keep-or-change question with its tradeoff and the
   evidence it landed (commit, file, or command output); coverage gaps
   from the sweep appear here as reinstate-or-ratify questions.
4. Decisions the user owns — every OPEN row (their product's identity,
   outward-facing surfaces, irreversibles, genuine taste), and why it
   stopped with them.
5. Concerns — anomalies, near-misses, waived gates, verification debt.
6. Workflow lessons — where this prompt or the plan made you over-ask,
   decide silently, or guess; what the next run's prompts should fix.
7. Where the detail lives — pointers to the plan, notes, and per-task
   subagent reports (note if any were deleted with worktrees).
8. Next steps — the ordered short list of what the user does next. At a
   gate it ends on the gate's question; on completion it ends with the
   standing last item: once the work lands, close the run — graduate
   {{run dir}}'s decisions, lessons, and follow-ups to their durable homes
   in this repo, then delete the directory.
Write it so the user can scan it — tables and tight bullets; a decision
that changes the user's product gets its own row, on the page.
Match handoff.md and notes.md to what the run actually produced: cover the
substance and skip restated summaries and boilerplate — but keep every
numbered section: one with nothing to report is a single line ("None."),
never a deletion.
Close with a 5-line chat summary that links handoff.md and names the
single most important decision the user owes.
```

--- TEMPLATE END ---
