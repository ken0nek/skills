---
name: library-seam-audit
description: Audit the seam between a library you maintain and the app(s) consuming it, in one reading pass with two lanes — architectural separation (does the layering hold, both directions) and elevation (what consumer-built machinery belongs in the library, what library machinery is really consumer policy). Works while the library is private and after it goes public. TRIGGER on "seam audit", "architectural separation", "does the layering hold", "elevation audit", "elevate to the package", "what belongs in the package/kit", "extract shared code from the apps", "move X into the package", "the app hand-rolls something the package vends", "should this live in the library". Not for publication leaks or whether a repo can go public, or for copying a pattern between peer apps. Moving shared machinery from consumers into their common library is this skill.
license: MIT
---

# library-seam-audit

A library and its consumers trade across a seam, and the seam fails two ways:
**violations** (something references, wears, or extends the wrong side) and
**misplacements** (machinery living on the wrong side). Those are the two
lanes. They share the expensive part — the contract, the interop surface, the
type-greps — so when both questions are live, run both from one reading pass.
The central finding class sits in both lanes at once: a consumer
hand-transcription of something the library defines is a separation finding
*and* an elevation candidate.

Read-only, in every repo touched. Findings become plans; they are never
applied inline, even the trivial ones.

## Setup (both lanes)

1. **Identify the parties.** The consumer set is discovered, not assumed: grep
   candidate app repos' package manifests (`Package.swift`, `Package.resolved`,
   `*.pbxproj`) for the library name. A consumer you didn't know about changes
   both lanes' answers.
2. **Stamp every repo read** — SHA, branch, cleanliness. A finding without a
   SHA-anchored file:line cannot be re-checked.
3. **Contract first.** Read the library's README, module doc comments, and
   tracked CLAUDE.md, plus the consumer's interop rules. Quote the written rule
   each violation violates; where the rule turns out to be unwritten, that gap
   is itself a finding. The charter's explicit disclaimers ("X is the
   consumer's policy") settle elevation questions later — collect them now.
4. **Prior analyses are hypotheses; forward-looking notes are required
   reading.** These are different uses of the maintainers' own notes, and
   conflating them causes both failure modes. Earlier audit answers describe
   an older tree — verify every claim at HEAD (counted facts have gone stale
   between audits before). But the library's findings and direction notes
   must be read *now*: an elevation candidate presented without its relation
   to an existing item is a re-discovery, and "unpublished notes aren't
   evidence" is not a reason to skip that check. Find where the maintainers
   keep them — the library's own docs, a private notes repo, a consumer's
   `docs/` — and check every place; backlogs and public docs alone have
   missed a recorded relation once.

## Separation lane

- **DOWNWARD, names then prose.** Grep the library for consumer names, types,
  and frameworks — then sweep for **citation phrases**: "the design doc",
  "the consumer's", "ported from", "§N.N", "see the … note". A doc comment can
  point straight at a private design document while naming no symbol, and a
  zero-hit name grep has already been used to declare this direction clean
  while three such citations sat in the sources. Prose references need a
  reader, not a symbol grep.
- **UPWARD.** List every file importing the library; check each against the
  written import rule (re-export vs peer import); count at HEAD yourself.
- **VOCABULARY-WEARING.** Where the consumer throws or reuses a library type,
  read what that case is *documented* to mean. App conditions (network
  outcomes, storage limits) inside a library error enum blur a shipped
  analytics taxonomy before anyone notices.
- **NAMESPACE.** Consumer extensions that add members to library types are a
  collision surface the library cannot see — list them and the labels at risk.
- **OBLIGATIONS — the most-skipped dimension; walk it explicitly.** Collect
  every consumer obligation the library documents ("a surface that shows X
  must say so", ordering rules, display duties) from its README and property
  docs, and grep each consumer for each one. An unhonored obligation is a live
  consumer bug routed to the consumer's backlog — not a tidiness item, and not
  the library's problem to fix.
- **DUPLICATION.** Where the consumer reimplements library machinery, check
  (a) the justifying comment's reason still holds — reasons expire — and
  (b) whether the copies still *agree*. Diverged duplicates are the worst
  case: two entry points accepting different sets of inputs. When a divergence
  is justified by citing a documented freeze or contract, check which side the
  contract actually binds — an emit-side freeze says nothing about a read
  path.

## Elevation lane

The admission test, applied **visibly, per candidate, all three legs** — the
legs that feel obvious are the ones that get skipped:

1. It is about the library's domain, not this app — an unrelated consumer
   would need it too. Implemented independently in two or more consumers is
   the strongest form of this evidence; count them.
2. It is not consumer policy. The charter disclaimers collected in setup
   settle this leg — quote the one that applies.
3. Moving it adds no dependency to the library and widens no platform
   requirement. Say so explicitly even when the answer is "none".

Where to look: **tests first** (format/domain machinery in app test targets),
hand-transcribed registries, defaults and bounds (grep the spec's own tokens
and see which are retyped rather than imported), helpers born of internal
visibility or cross-repo cost, fixtures and corpora proving something about
the library's domain rather than the app.

A hand-transcribed registry is two things fused: the **registry** (domain —
the spec's closed sets and defaults) and its **display strings** (policy).
Split them before judging. When the library already vends typed views of the
same species (a `Known*`-style family), the registry half is a candidate **by
precedent**, and only the strings stay behind. Rejecting the fused pair as
"consumer display" has already lost a real candidate once — the library's
"a consumer localizes these" prose is about the strings, not the registry.

For each candidate: the **neutralization cost** (names to scrub), **what stays
behind** (localized strings, storage shape, policy), **deliberate behavioral
differences that must survive the move** (an uncapped variant kept uncapped),
and **which existing forward-note it relates to** — related items are decided
together, not re-pinned twice. Record **rejected candidates** with the
disclaimer that settled each; that is what stops the next run re-auditing
them. Check the reverse direction too: library machinery that is really
consumer policy is a push-down candidate.

## Method notes

- **Grep the TYPE, not the name.** Shared vocabulary (the same field name on
  both sides) buries the handful of real seam sites under the app's own
  surface — a name grep has returned 37 files where six mattered.
- Every claim cites current file:line; every remedy names **which repo** the
  fix lands in.

## Report contract

Stamps for every repo · the contract as quoted · separation findings grouped
by direction, each with the rule it violates, and a statement of which
direction is healthier · elevation ranked table (value / effort / consumer
churn) · per-candidate visible admission test, neutralization cost, and
forward-note relation · rejected candidates · a final "what changes, where"
summary with each item's repo named.

