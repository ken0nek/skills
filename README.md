# skills

[![check](https://github.com/ken0nek/skills/actions/workflows/check.yml/badge.svg)](https://github.com/ken0nek/skills/actions/workflows/check.yml)
[![skills.sh](https://skills.sh/b/ken0nek/skills)](https://skills.sh/ken0nek/skills)

One decision policy, and the seven skills that carry it. Process frameworks
teach an agent to brainstorm, plan, and execute. This repo settles what they
leave open. It says who decides each choice a run meets, what a run leaves on
disk, and what graduates at the close. The same policy runs in sessions with
no run at all. There it decides which decisions reach you, and in what shape.

| Skill | The decisions it owns | Leaves behind |
|---|---|---|
| [generate-plan](skills/run-lifecycle/generate-plan/) | decisions the plan can settle in advance | `plan.md` — decision table, STOP gates, per-task verification |
| [generate-execution-prompt](skills/run-lifecycle/generate-execution-prompt/) | decisions the executor will meet, and who owns each | `execution-prompt.md` — the policy verbatim, the §0–8 handoff contract |
| [decide-and-log](skills/decisions/decide-and-log/) | decisions met in the moment, any session, in or out of the flow | a decision-log row, and a session that keeps moving |
| [now-what](skills/decisions/now-what/) | decisions the user must make, when they have lost track of what those are | an answer they can act on — what to know, what to do, what only they decide |
| [explain-to-decide](skills/decisions/explain-to-decide/) | one decision the user cannot evaluate yet | the option expanded — a real instance, the diff, the consequence, a pick and its counter |
| [clarify-to-decide](skills/decisions/clarify-to-decide/) | a decision the user brings, before the options exist | only the questions that change the answer — then a pick, its counter, and a row to paste forward |
| [harvest-run](skills/run-lifecycle/harvest-run/) | decisions graduating out of the run | decision records, lessons, backlog rows — and no run directory |

```sh
npx skills add ken0nek/skills                                  # every skill
npx skills add ken0nek/skills --skill decide-and-log           # one, by name
npx skills add ken0nek/skills/skills/decisions/decide-and-log  # one, by path
```

Six of the seven use only the Agent Skills spec's fields, so any harness that
reads `SKILL.md` runs them. harvest-run deletes a directory, so only the user
invokes it — a rule the spec has no field for. `disable-model-invocation`
carries it for Claude Code, `agents/openai.yaml` for Codex. A skill installed
alone is whole: nothing in its folder points outside it.

This is the **governance** layer of a three-layer stack. A **process** layer
([superpowers](https://github.com/obra/superpowers),
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills))
generates. A **correctives** layer
([mattpocock/skills](https://github.com/mattpocock/skills)) handles handoff,
grilling, and research. This layer decides who decides. No neighbor is
required, and no skill here names one. Each routes by role ("an installed
plan-writing skill writes the plan; this skill governs it"), so any pack
that fills the role composes.

## The policy

**Reversal cost decides who decides. Resolution cost decides whether to build
the options.** Reversible — the agent can write the reverse: it decides, logs
the row with that reverse, and keeps going. Irreversible: the human decides.
A cheap flag, a parameter, or both variants side by side turn the second into
the first, and then the agent builds the options instead of asking. The
executor cannot switch the rule off. The row is written at the moment of the
call, and the same row travels plan → execution prompt → handoff → harvest.
Three of the seven exist for the case where the answer really is yours: they
decide what reaches you, in what shape, and how few questions it takes to
settle.

The rule corrects two failures with one cause — no shared rule for which
decisions are the agent's. **Over-asking**: the run stalls behind a
reversible question nobody needed answered. **Silent taste decisions**: the
agent makes a judgment call, often rightly, and never records it. The call
surfaces during review of work already built on it, or never.

[POLICY.md](POLICY.md) is canonical. Each skill carries the clauses its
moment reaches — two of them the whole block — because a zero-context session
can only read what it was handed. In full:

```text
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
```

The one-way / two-way door framing comes from the shareholder letters of
Jeff Bezos.

### The policy on one choice

A run meets something the plan did not settle: how to key the response cache.
Reversal is cheap, so the run decides and keeps moving, with a row behind it:

> **Cache key format.** Options: `sha256(url)` · `sha256(url + variant)` ·
> a versioned prefix. Chose `v1:` + `sha256(url + variant)` — a later format
> change can then coexist with live entries instead of invalidating all of
> them at once. Reverse: bump the prefix constant in `cache/key.ts`. Entries
> under the old prefix expire on their own TTL. **Status: settled.**

An hour later, the same run has to name the column the key is written into.
Two other services already read that table, and nothing makes that cheap to
undo. The run stops, asks, and ends its turn there — not on a promise.
That is the whole policy: not *ask less*, but ask about the decisions that
are yours to answer.

The row is the artifact. A recap assembled at the end of a run cannot be
reviewed during it, and dies with the session. A row carries its own
reversal recipe: six weeks later, someone who was never in the room can
still overturn the decision.

## The run

**Chat is disposable. Artifacts are not. The run directory is, once the
close has graduated what is durable.** The context is cleared between planning and execution
on purpose. Every step ends in a file, and the next step reads the file,
never the conversation.

1. **Brainstorm** — your process layer runs the dialogue and writes the
   design spec into the run directory as `spec.md`. `clarify-to-decide`
   shapes the asks inside it.
2. **[generate-plan](skills/run-lifecycle/generate-plan/)** governs the plan,
   whoever writes it.
3. **[generate-execution-prompt](skills/run-lifecycle/generate-execution-prompt/)**
   writes the executor session's first message as a file.
4. **Clear** the planning context. The artifacts carry the run.
5. **Execute** — a fresh session runs the prompt and keeps `notes.md`, with
   the decision log inside. It ends on `handoff.md`, or at a STOP gate on that
   gate's handoff.
6. **[harvest-run](skills/run-lifecycle/harvest-run/)**, once the work lands
   and you have answered the handoff's keep-or-change questions, graduates
   what is durable and deletes the run directory, in one closing commit.

```
idea ─1→ spec.md ─2→ plan.md ─3→ execution-prompt.md
                                      │ paste (step 5)
                        notes.md (decision log inside)
                                      │ run ends
                                 handoff.md
                                      │ review · work lands (step 6)
                 decision log · lessons · backlog  (run directory deleted)
```

`harvest-run` is the one skill you invoke by name.

## The four that run anywhere

One policy at four distances from the user, inside the flow or outside it:

- **[decide-and-log](skills/decisions/decide-and-log/)** suppresses a
  hand-back the policy does not require. This is the atom: the lifecycle
  skills are the same call, scheduled. Take it alone, and most over-asking
  goes away.
- **[now-what](skills/decisions/now-what/)** makes a required hand-back
  legible, answering from the tree and the written record.
- **[explain-to-decide](skills/decisions/explain-to-decide/)** expands the one
  row you still cannot answer, and re-checks that it was yours.
- **[clarify-to-decide](skills/decisions/clarify-to-decide/)** runs the other
  way: you bring the choice, and the settling information is yours. Where an
  interview skill is installed, clarify-to-decide governs its rounds instead
  of running them.

## Contributing

An eighth skill has to own a decision moment these seven do not. What helps:
prose that tightens, drift fixes, and a requirement change shipped with the
failure it corrects. That failure goes in the skill's `README.md`, under *Why
each line exists*, beside the `Tuning` section for whoever edits it. Run
`sh scripts/check.sh` before a PR. CI runs the same check. The root
`CLAUDE.md` is for whoever edits this repo, not for users of the skills.

## Provenance

Written by Ken Tominaga with Claude, and dogfooded on real runs before it
ships. No executable code in a skill folder: audit one by reading it.
MIT ([LICENSE](LICENSE)).
