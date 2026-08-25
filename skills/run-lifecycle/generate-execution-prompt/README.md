# generate-execution-prompt

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Turn an approved plan into the execution prompt file that opens a fresh
executor session.

One of seven skills built on one rule: **reversal cost decides who decides.**

**The moment it owns.** Execution time. Before the context clear, it names
every decision that the executor will meet, and who owns each.

**Fires on**

- after plan approval and before the context clear
- a plan with no execution prompt yet
- "write the orchestrator prompt"

**Not for** writing the plan itself.

**Leaves behind** `execution-prompt.md`: the policy verbatim, the STOP gates
enumerated, the paths absolute, the §0–8 handoff contract.

## Why each line exists

One entry per requirement in `SKILL.md`: the failure it corrects and, where
it came from outside, its source.

**Generator and template are asymmetric on purpose.** Per-run specifics get
generated. The tuned language stays verbatim, because a fresh paraphrase each
run erodes it. The executor starts after a clear with zero shared context.
The strongest lever for a long autonomous run is a complete specification up
front. So the template is long, and the generator instructions above it are
short.

### Generator

- **"Never execute the plan"** — a capable model handed a finished plan can
  start it. The boundary is stated first (Anthropic's published prompting
  guidance, https://platform.claude.com/docs/en/build-with-claude/prompt-engineering).
- **A file in the run dir** — the coming clear cannot lose an artifact, only
  a chat message.
- **The header names no model and no effort** — both fed a comment line only,
  and "ask, or leave" read as *ask*. A run put the executor's model to the
  user as a four-option question whose every answer produced the same prompt.
  The executor inherits the planning session's setup. Changing it is a
  paste-time choice that needs no slot.
- **`{{executor addendum}}` is filled from the lessons file** — an executor's
  failure mode is observed, never cast. A run that read the Tuning menu put
  "which failure mode" to the user before any executor had run. Harvest writes
  what the last executor did into the lessons file. The rows targeting the
  execution prompt are the addendum's only source, so the first run of a repo
  ships none.
- **Both copy boundaries stated** — the plan wraps its policy in markers and
  a fence. The prompt carries neither. Left implicit, a literal comparison
  always differs, and the remedy pastes the markers in. The template's own
  fence has the same shape.
- **The override is flagged beside "verbatim"** — an unflagged second
  exception reads as not being one, and a careful generator keeps the wrong
  text.
- **The sample STOP gate** — an abstract gate renders divergently. One filled
  example anchors task, question, and why-not-defaultable.
- **Fresh-eyes check** — rehearses the paste before the clear, while fixing
  is cheap. The subagent gets the repo because the executor will. It is told
  not to execute, because the file is engineered to start a run. The
  mechanism is named so that a harness without subagents substitutes a fresh
  session.
- **`{{code repo root}}` is its own slot** — a simulated executor resolves
  the plan's relative paths against the run directory. The two can differ.
- **`{{handoff path}}` is a slot** — a fixed `{{run dir}}/handoff.md` on the
  next line cancels the template's PRIVATE rule. A committed handoff in a
  public repo stays in history after harvest deletes it. The generator
  resolves the slot because it can check whether the repo is public. The
  executor cannot.

### Template

- **"Where a skill says stop and ask, the policy governs"** — the set's one
  standing override. Keep an execution skill's per-task review subagents
  (code quality). Re-route only its ask-the-user moments.
- **Notes categories** — Thariq Shihipar's running implementation-notes
  prompt, distilled with sources in
  [running-implementation-notes.md](references/running-implementation-notes.md),
  plus "surprises". "At the moment things happen" is the fix for silent
  decisions that surface as end-of-run archaeology.
- **Verification scaled to tier** — review ceremony scales to how mechanical
  the task is. Unconditional: the plan's command run green, the grounded
  audit, and the full gate on completion.
- **Grounded progress audit** — adapted from Anthropic's guidance on long
  autonomous runs, which reports that it nearly eliminated fabricated status
  (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering).
- **Autonomy block** — the vendor's autonomous-pipeline reminder fused with
  the policy's stop conditions: over-asking and end-on-a-promise in one
  paragraph. The scope line is shared text, because one executor class
  widens and another takes adjacent actions.
- **Deliverable length calibrated in place** — an executor that writes long
  files runs `notes.md` and `handoff.md` long. The skeleton alone does not
  imply length.
- **Plan wins over spec, in the prompt** — a generator's fresh-eyes check
  found the spec overriding two corrections the plan had measured. An executor
  that copies from the spec ships a clipboard-wiping call. One fixed line
  spares every generator the noticing.
- **The gate handoff** — a run that stopped at a gate had to invent a
  second handoff file and carve the close out of §8 by hand. The contract
  names the file and what §8 ends on, so a gate and a completion read alike.
- **Gate and reconcile at every stop** — scheduled on completion only, the
  seam review waits until after a long hand session. The executor moved it to
  the gate on its own and found a defect in the plan's central feature.
  Running it at each stop is the rule, so it stops being a judgment call.
- **An empty reconcile scan is a miss** — a self-report under-reports by
  default. An executor that finds no unlogged decisions on a run that
  filled gaps the plan left has not looked. The line names what must have
  happened instead, so the scan has a bound other than the executor's own
  memory.
- **Plan text and reports are claims** — statements shipped verbatim from the
  plan were untrue of the tree. The plan's own code carried the defect, and
  subagent reports carried arithmetic that did not hold. The audit line covers
  the executor's claims. These two sentences cover the other two sources a run
  relays. The dispatch channel line exists because reports that did not name
  one never arrived.
- **Handoff §0–8, sole owner of the contract** — §3 and §4 re-render the
  decision log. §6 is the meta-loop that feeds the lessons file. The
  completion sweep checks settled rows against the tree both ways. §8's last
  item points at the close. §3 versus §4 is the policy's settled/OPEN split
  as document structure: the user *audits* one and *makes* the other. That
  is why the list is never abbreviated, and why a section with nothing to
  report is "None." rather than deleted.

## Tuning

This skill has two roles to tune: the generator and the executor.

### The generator

The generator instructions are deliberately brief, which suits a model that
wants requirements and its own judgment inside them. On a model that wants
the complete spec up front, two lines become load-bearing. The first is
"delete slot lines that do not apply": such a model does not improvise
cleanup unasked. The second is the *single* explicit fresh-eyes subagent. On
a readily-delegating model that line reads as a cap. On an under-spawning
one, the same line is a prod.

### The executor

The template ships one text for every executor. Tune through the lessons file,
never by carrying variants inside the template. A handoff §6 row that names
the failure, harvested with the target *execution prompt*, becomes one line of
the next run's `{{executor addendum}}`. An executor that stops early gets a
push to keep working and to dispatch an interval verifier after each phase.
One that widens scope gets a spawn cap and a working-tree contention bound. A
paragraph aimed at the wrong failure is worse than none, which is why the
addendum stays empty until a run has shown the failure.

The completion sweep's two-direction reconcile is itself a dial, and the two
directions fail in opposite ways. Direction one scans the session for
judgment calls missing from the log. It catches decisions made but never
logged. Push it hardest on an executor that under-reports its own judgment
calls. Direction two checks each settled row against the working tree. It
catches the inverse: rows logged but never implemented, or undone by later
work. Push it on an executor that logs eagerly and drifts. Drop either half,
and the handoff re-renders a log that nobody checked.

Give an executor that pads its files a large output budget and expect to trim.
Effort is harness-side. No prompt can set it, and the header names none.

When a run misses, tune it by asking whether the model did not *know* or did
not *try*. Confidently wrong with full context in hand means move the
executor up a tier. Skipping a file, not running the tests, or bailing
partway through a refactor means raise effort.

## Install

```sh
npx skills add ken0nek/skills --skill generate-execution-prompt
```

MIT.
