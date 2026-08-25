# Running implementation notes

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

A distillation of the during-implementation pattern this skill's template
borrows, written from scratch in our own words.

## The method

**A file kept as the work happens, never a summary assembled afterwards.** An
agent that implements a specification makes judgment calls continuously. The
spec was silent on something. An edge case in the code ruled out the obvious
approach. Two designs were close, and one had to win. Ask for those at the
end, and what you get is a reconstruction. The reasons are gone, and a tidy
narrative of the diff takes their place. Ask instead for a notes file appended
to at the moment each call is made. Then you get the calls themselves, with
the trade-offs that were live when they were made.

Four categories cover what a reviewer needs. Naming them in the prompt
turns the file from a log into review material:

- **Decisions** — calls that the specification left open or ambiguous, and
  how they were settled.
- **Deviations** — where the implementation knowingly departed from what was
  written, and what forced it.
- **Tradeoffs** — the alternatives that were weighed, and why the chosen one
  won.
- **Open questions** — anything the author has to confirm, ratify, or
  reverse.

The pattern rests on one assumption: planning closes the gaps it can name,
and the agent meets the rest mid-implementation and has to choose. The
notes file turns that choosing into reviewable material instead of
archaeology across a diff. It also feeds the next attempt, since a gap that
opened once tends to open again.

Two mechanics matter. The notes live in a **file**, so they outlast the
session that produced them, and they can be handed to someone who was not
there. And the file is written for a reader, not for storage. It is meant to
be read once the work is done, then to stop existing.

## How this skill applies it

The generated prompt's "Running notes" block points at `notes.md` in the run
directory and asks for exactly these categories: decision log, deviations,
tradeoffs, open questions. It adds *surprises*, this set's own category for
anything that contradicted the plan's assumptions. "At the moment things
happen" is the line the pattern turns on: without it, the file degrades into
the end-of-run reconstruction it exists to replace. The handoff's §3 and §4
then re-render those rows. The reconcile at each stop checks them against the
tree, instead of rebuilding either from memory.

## Attribution

- **Author:** Thariq Shihipar, Anthropic
- **Primary source:** "A field guide to Claude Fable 5: Finding your
  unknowns", published 2026-07-06 —
  https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns
  — which sets the running-notes pattern inside its wider method.
- Read the source for the author's own framing and prompts.
