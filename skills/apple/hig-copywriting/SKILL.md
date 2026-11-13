---
name: hig-copywriting
description: Write and review user-facing text in an Apple-platform app against the HIG — voice and tone, verb-first CTAs and button labels, the capitalization system, alert, error and empty-state wording, settings labels, inclusive language, and the string-engineering rules that keep copy localizable (comments, plurals, no fragment assembly). Use whenever UI wording is written, changed or reviewed — a new screen, paywall, onboarding, alert, or a copy pass over existing strings. TRIGGER on "button label", "CTA wording", "error message copy", "empty state text", "microcopy", "UI copy", "copy review", "reword this alert", "capitalization", "title case or sentence case", "paywall copy", "onboarding copy", "inclusive language", "is this string localizable". Not for string-catalog surgery (untranslated or dead keys, adding a locale), App Store listing fields and their caps, per-version What's New notes, web or landing-page prose, or contrast and touch-target checks.
license: MIT
allowed-tools: WebFetch(domain:developer.apple.com)
---

# HIG copywriting

## What this is

An Apple copy standard, operationalized. The rules live in the bundled
reference `references/apple-hig-copy-and-localization.md`, distilled from
Apple's HIG and localization docs and keeping each component-specific rule to
the letter rather than flattening it into one principle. This file is the
procedure.

The reference is a dated summary, and it tags every rule with its source:
Apple's page, an Apple-written Xcode skill, a house default (this skill's own
choice where Apple leaves one open), or an inference. Two things follow. Apple's live page outranks the summary, so a rule cited as
Apple's gets checked against the page when the summary's date is old or the
finding is contested. And a house default is cited as one: it is arguable on
consistency, never on Apple's authority. A finding that dresses house taste as
Apple guidance loses the argument the moment someone opens the page.

Two lenses govern two different surfaces. System UI — buttons, alerts,
settings, errors, empty states — takes the HIG register: concise, verb-first,
clarity over cleverness. Conversion surfaces — paywall, onboarding hero — take
benefit-led conversion craft inside HIG's honest tone. One app ships both, and
the common failure is the wrong lens: marketing voice leaking into an alert, or
a paywall headline written as flatly as a settings label. When a surface is
ambiguous, default to HIG.

## Apple's own skills, when they are loaded

Xcode 27.2 ships agent skills that Apple wrote. They load under
`xcrun mcpbridge run-agent claude` and are not installed globally, so check
whether they are present before relying on them. On their topics they outrank
the reference and training memory:

- **`swiftui-specialist`** — its `references/localization.md` decides
  string-engineering questions (Part 4): which API wraps a string, comments,
  interpolation, casing, formatting, layout for longer translations. Where it
  and Part 4 differ, follow it and note the difference.
- **`translation`**, **`translation-coordinator`** — translating catalog
  entries, with per-locale style guides (ja and en among them). This skill
  judges the English source; those produce the translations.

`xcrun agent plugin path --plugin-format claude` prints the folder holding
them; their files can be read from there even when they are not loaded. The
translation skills only work through Xcode's String Catalog tools, which exist
only when the session is connected to Xcode, but their per-locale style guides
(`translation/references/styleguide_<locale>.md`) are plain reading. Otherwise
work from the reference and say that Apple's skill was not consulted.

## Running a copy pass

1. **Discover the strings.** They sit differently in every repo, so find them:
   search the sources for `String(localized:`, `NSLocalizedString`,
   `LocalizedStringResource`, `Text(`, `Label(`, `Button(`, and list the
   `.xcstrings` catalogs. Read the English values out of the catalog JSON — call sites often carry only a
   key, and some apps route every string through a constants file worth
   finding first.
2. **Judge the words against Parts 1–3** — voice, the CTA and alert-button
   rules, the capitalization table. Most findings are an inconsistency between
   two instances rather than one bad string, so compare siblings of the same
   element type before judging any one of them. The per-component rules are
   where an internally consistent app still diverges from Apple: alert titles
   take sentence case with a period when they are sentences and title case
   without one when they are fragments, while every button title — alerts
   included — takes title case (§2.5, §3.1).
3. **Judge the engineering against Part 4** (or Apple's localization
   reference, when loaded) — a localizable API around every user-facing string,
   a translator comment wherever the key is ambiguous, plurals via catalog
   variations instead of `if count ==`, whole sentences instead of assembled
   fragments, positional specifiers past one argument, no runtime case
   transforms. Comments are cheap to skip and expensive to lack, so count the
   commented keys rather than sampling them.
4. **Sweep the anti-patterns table** for the traps that read as fine in
   isolation: "Oops", ambiguous "we", "OK" confirming a destructive action, a
   destructive action styled as the prominent button.
5. **Judge conversion surfaces against §2.6** as well — value in the label,
   one prominent CTA, no fabricated urgency.

Report each finding as `file:line` · current text · the rule with its section
and source tag · the proposed replacement. The citation makes a finding
arguable on the rules rather than on taste, and the tag says whose rule it is.

## Writing fresh copy

Start from the reference's CTA pattern library. It already resolves the
recurring intents — start a flow, advance, finish, destructive confirm, cancel,
opens-more-UI, async, paywall, enable-a-feature — and a settled label beats an
invented one: familiar phrasing is a feature, not repetition.

Then pick the convention per element type and apply it consistently. That is
Apple's meta-principle, and it outranks any individual preference. Title case
for every button and sentence case for body text is the house default that
gives "consistent" a concrete target. Where an app has settled a different
convention for an element type Apple leaves open, keep it and flag the
instances that break it — the inconsistency is the defect, not the choice.

Finish against the two checklists (copy review, localization); both are
written to paste into a PR.

## Boundaries

Each of these is a neighbor's job. Where an installed skill owns it, that
skill runs it.

- **`.xcstrings` catalog surgery** — untranslated or dead keys, adding a
  locale, normalizing locale codes. This skill judges the words; catalog
  work moves them.
- **Store listing fields** — name, subtitle, keywords, promo, description, and
  their character caps. Store-listing work composes this skill for the prose
  itself.
- **Per-version "What's New"** — release-notes work.
- **Web and landing-page prose** — marketing copywriting. It owns conversion
  craft off-device; this lane stays Apple.
- **Color contrast and touch-target size** — a contrast and touch-target
  audit. Those are arithmetic against a threshold; this skill is judgement
  about words.

## When to read the reference

`references/apple-hig-copy-and-localization.md`:

- **The header and §0** on every run: the verification date, the source tags,
  and the lens table that decides which register a surface gets.
- **The Part the task touches:** Part 1 voice · Part 2 CTAs and buttons (§2.5
  alerts, §2.6 conversion) · Part 3 in-app strings (§3.1 capitalization, §3.2
  errors, §3.3 empty states) · Part 4 localization engineering · Part 5
  inclusive language.
- **The anti-patterns table** on any review.
- **The two checklists** when the output should be paste-into-PR ready.

## Worked example

A copy pass on a shipped app's string catalog surfaced this in a settings
footer:

**Violation** — `"Free saved filters: %lld of %lld · Pro unlocks unlimited"`.

**Rule** — Part 4.4 *[Apple · Xcode localization docs]*: multi-argument strings
take positional specifiers (`%1$lld`, `%2$lld`) so translators can reorder
arguments; the anti-patterns table carries it as `Hard-coded %@ %@` →
`%1$@ %2$@`.

**Fix** — `"Free filters: %1$lld of %2$lld · Pro unlocks unlimited"`,
applied to every translated value too.

The bug was invisible to a strong no-skill audit of the same catalog: it is the
only two-argument string in the catalog, and nothing about it reads wrong in
English — the shipped Japanese translation already reorders the surrounding
text but cannot reorder the counts. The fix rode along with a terminology
finding on the same string ("saved filters" in a footer under a "Filters" nav title,
Part 1.1 *[Apple · HIG Writing]*), which is the normal shape here: one string,
two Parts.
