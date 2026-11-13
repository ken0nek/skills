# library-seam-audit

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Audit the seam between a library and the apps that consume it, in one reading
pass with two lanes: separation and elevation.

**The moment it owns.** Someone asks whether the layering between a library
and its consumers holds, or what consumer-built machinery should move into
the library (or out of it).

**Fires on**

- "seam audit", "architectural separation", "does the layering hold"
- "elevation audit", "elevate to the package", "what belongs in the
  package/kit", "extract shared code from the apps", "move X into the
  package", "the app hand-rolls something the package vends", "should this
  live in the library"

**Not for** publication leaks, or copying a pattern between peer apps.

**Leaves behind** a read-only report: SHA stamps for every repo read, the
contract as quoted, separation findings by direction, a ranked elevation
table with a visible admission test per candidate, rejected candidates with
the disclaimer that settled each, and a "what changes, where" summary naming
each item's repo. No code changes.

## Why each line exists

**Why one pass, two lanes.** Both lanes need the same expensive reading — the
contract, the interop surface, the type searches — and the central finding (a
consumer hand-transcribing something the library defines) belongs to both.

**Why read-only.** Findings become plans. Applying the trivial ones inline
mixes the audit with changes nobody reviewed.

**Why the consumer set is discovered.** A consumer nobody remembered changes
both lanes' answers.

**Why prior audits are hypotheses but forward notes are required.** Counted
facts go stale between audits. A candidate presented without its relation to
an existing note is a re-discovery.

**Why the downward sweep reads prose.** A doc comment can cite a private
design document while naming no symbol; a zero-hit name search has declared
that direction clean while three such citations sat in the sources.

**Why the obligations walk is explicit.** It is the dimension audits skip
most, and an unhonored obligation is a live consumer bug.

**Why the admission test is visible, all three legs.** The legs that feel
obvious are the ones skipped.

**Why the registry splits from its display strings.** Rejecting the fused
pair as consumer display has lost a real candidate.

**Why grep the type, not the name.** Shared vocabulary buries the few real
seam sites under the app's own surface.

## Tuning

A model that pads lists every duplicated helper. Hold it to the admission
test before a candidate enters the table.

A model that widens scope starts editing. Restate read-only first.

A model that stops early runs one lane, or skips the obligations walk.
Restate that the report contract requires both lanes and the walk.
