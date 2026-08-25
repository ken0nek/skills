# Agent guidance

For whoever edits this repo. Nothing here ships with a skill.

One decision policy and the seven skills that carry it: **reversal cost
decides who decides. Resolution cost decides whether to build the options.** A
line that does not serve that is not this repo's to carry.

`sh scripts/check.sh` is the one mechanical check. CI runs it on every push.
Everything else is verified by reading the prose and using the skill on a
real run.

## Layout

- `POLICY.md` — the canonical policy.
- `README.md` — the index. Every shipped skill appears there.
- `skills/<group>/<name>/` — one installable skill: `SKILL.md` (what the model
  reads) and `README.md` (for whoever edits: the browse surface, the failure
  each requirement corrects, and `## Tuning` for a model that stops early,
  widens scope, or pads). Its first line says a run reads `SKILL.md` alone. A
  run that opens it anyway stops there.

## Invariants

- **Seven skills, one per decision moment.** An eighth must own a moment
  these do not. Otherwise it belongs inside one. Each `README.md` opens
  with the moment it claims.
- **Each skill installs alone.** The policy is embedded, never linked. No
  skill names a repo-level file. A third-party source is cited by URL.
  `check.sh` fails a link that leaves the folder.
- **Compose with the packs the README names.** A requirement that restates a
  neighbor loads twice, and the more conservative bound wins. Hand a separable
  *action* to a role ("an installed plan-writing skill writes it; this governs
  it"). A *judgment* applied to every line stays in the body even where a
  neighbor states it. Three do: the reversal-cost classifier, *would a
  different answer change my recommendation*, *is this row theirs*.
- **A rule earns SKILL.md by correcting a failure that recurs.** What one
  run hit is a harvest lesson, not a rule.
- **POLICY.md is canonical.** The README, `generate-plan`, and
  `generate-execution-prompt` embed it verbatim. The `decisions/` skills
  compress it to the clauses they reach. Edit POLICY.md first, then every
  embed (`grep -rli "reversal cost" skills README.md`), then run `check.sh`.
  Carrying an edit into a compression is a reading job.
- **SKILL.md instructs. README.md points, justifies, and tunes.** SKILL.md
  loads in full on every fire, so it carries only what the run reads. Why a
  line exists → README.md's *Why each line exists*, present tense, no dates,
  no counts. A note for whoever edits → this file.
- **No file casts by model name.** `## Tuning` names failure modes and lets
  the reader cast.
- **Tool-neutral.** `git` is the one assumed dependency. State the property
  a command must have, never a tool or a flag.
- **The execution-prompt template owns the handoff contract** (its §0–8
  list). Never abbreviate it. Route every contract change there.
- **The four `decisions/` skills are one policy at four distances.** Three
  claims recur and must not drift: the reversal-cost classifier, the
  taste-on-their-surfaces exception, *you argue, they decide*. A change to
  what the policy reserves for the user lands in all four or in none.
- **A description carries triggers and boundaries, never the output
  recipe.** The output shape lives in the body. Its human summary is the
  README's *Leaves behind* column.
- **`decisions/` skills route to neighbors by role, never by name.**
- **`generate-execution-prompt` reads `generate-plan`'s *decision table*
  and *STOP gates* by name.** Rename either and the downstream skill stops
  finding it.
- **Ask for work products, never for reasoning.**

## Testing distribution

Install with the README's commands from a directory outside this repo and
open the copied folder: a single-skill install must be whole.
