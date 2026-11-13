---
name: hig-contrast-and-size-check
description: Audit a SwiftUI app against the HIG's two numeric floors — color contrast (WCAG AA/AAA on the text and control-on-background pairs that ship, in Light, Dark AND Increase Contrast) and touch-target size (hit rect vs Apple's default and minimum). Use when checking that colors are readable or controls tappable, auditing or changing a palette, shipping a new screen, paywall or widget, or prepping the App Store accessibility label. TRIGGER on "check color contrast", "contrast audit", "is this readable", "is this legible", "WCAG contrast", "accessibility contrast", "HIG color check", "does this pass contrast", "dark mode contrast", "accessible colors", "contrast ratio", "increase contrast", "is my text readable on that background", "are these colors accessible", "touch target", "tap target", "hit area", "44 points", "is this button too small", "too small to tap". Not for picking colors aesthetically, chart palettes, or the wording of UI text.
license: MIT
allowed-tools: Bash(bash*gather-color-signals.sh*) Bash(python3*contrast-ratio.py*) Bash(grep*) Bash(rg*) Bash(find*) Bash(git diff*) Read WebFetch(domain:developer.apple.com)
---

# Contrast & size — the HIG's numeric floors

Two checks, one shape: **a threshold Apple states as a number, and a pairing you have to go find.** Text and meaningful controls clear **4.5:1** (or 3:1) against the background they actually sit on — in Light, Dark, and Increase Contrast. Tappable things clear Apple's **minimum** control size and should reach its **default** one in effective hit rect — on iOS, 28×28 pt and 44×44 pt. Both are arithmetic once you have the pair; in both, finding the pair *is* the work, and in both the thing you can name is not the thing that ships — the background is a **composite**, and the hit rect is not the frame.

This skill is **propose-then-fix**: it audits, then on your go-ahead nudges the offending color (or adds a scrim, a high-contrast asset variant, a `.contentShape`). The ratio math is bundled and deterministic so no audit re-derives it, and the no-regression gate is enforced by the script rather than trusted to the table.

## The mental model — read this first; the rules below are consequences of it

**Contrast is a property of a PAIR in a CONTEXT — never of a single color.** "Is this color accessible?" has no answer; "does *this text color* on *that background* clear 4.5:1 *in dark mode*?" does. So the skill's whole value is in step 2: enumerating the foreground×background pairs that genuinely ship together, each in all three appearances. A pair that passes in Light routinely fails in Dark (the colors move independently), and apps often have **zero** Increase-Contrast path, so that appearance fails silently — verify rather than assume; the gatherer prints which colorsets carry a `high` variant. Find the pairs; the rest is arithmetic.

**The background half of a pair is the COMPOSITE at the site, not the color you can name.** What renders behind the text is every layer stacked there: a scrim over a photo, a material, a gradient, `.opacity(0.7)` over a tint. Resolve the stack in the file and measure *that* — the composite is the background. Two consequences to carry: a scrim pins its surface dark in **both** appearances, so a label that reads in the palette can fail on it; and a gradient or image has no single value, so you measure its **worst-case stop** (the lightest part under light text) or require a scrim that guarantees the floor.

**A color that arrives as a PARAMETER is a set of pairs, not a pair.** `func chip(selected:tint: Color)`, a `StateColor` whose `.tint` varies by case, a marker that takes its fill from a category — each has as many backgrounds as it has callers, so **no fixed label color is right for all of them**. Grep the call sites and enumerate the arguments actually passed; if they span light and dark fills, don't pick one — resolve at runtime (step 2). A fixed `.white`, or a fixed dark token, over a fill that moves is wrong by construction, and it reads as correct in the one appearance you happened to check.

**Measure what you are REPLACING, not just what you are installing.** A fix is a pair swap, and the pair you swapped out had a ratio in every appearance too. In one real pass, **five of ten mis-applied tokens made contrast worse than before the audit** — each by raising the appearance under inspection and never re-measuring the other. So every fix carries a `before → after` in *all three* appearances (step 7), and **no appearance may cross from passing to failing.**

**The arithmetic is settled — use the script, never your eyes or RGB intuition.** The WCAG ratio is built on *relative luminance* (linearize each channel, weight by the color space's Y row), not a naive RGB distance — two colors with equal RGB deltas can have wildly different ratios. `scripts/contrast-ratio.py` is the one source of truth; feed it the pairs and read the verdict. Eyeballing a swatch, or trusting an inline `// ~4.9:1` comment, is how wrong numbers ship.

**Subtract what's already solved before you flag anything.** Some surfaces have legibility infra — a dark scrim behind a readout, a vibrancy/material pass, a contrast-aware type or a shadow under text over the canvas. Infra doesn't merely excuse a pair, it becomes part of the composite, so a protected surface is still measured — against the stack. Decorative graphics (an animated diagram, a chart's fill) and disabled/placeholder text are **not** held to the 4.5:1 text bar. Re-flagging handled cases burns trust; find the infra (step 5) and account for it.

**Fix minimally; the palette is not yours to redesign.** The right fix is the *smallest* one that crosses the line: a few points of L\* on the foreground, a scrim or vibrancy behind text on imagery, a heavier weight / larger size that moves the row to the 3:1 threshold, or a high-contrast asset variant for Increase Contrast. A brand color that can't move keeps its hue — you fix the *pairing* (darken the surface, add a scrim, bump weight), never the brand.

## The thresholds — only the parts the script cannot print

`contrast-ratio.py` prints every bar (3.0 / 4.5 / 7.0) and its PASS/FAIL for every pair, so those numbers live in its output, not here. Three things it cannot decide, because they depend on the font and the role you can see and it cannot. Each carries its source, because a finding cited to the wrong authority loses the argument it was meant to win:

- **Which row applies — and under which standard.** *[Apple, HIG Accessibility table]* text **up to 17 pt** takes 4.5:1; **18 pt at any weight, or bold at any size**, takes 3:1. Accessibility Inspector checks this table. *[WCAG 2.2, "large scale"]* the 3:1 row needs **≥ 18 pt regular or ≥ 14 pt bold**, so bold text alone does not qualify. Apple labels its table "values from WCAG Level AA", yet the two disagree on small bold text. Report under Apple's table by default. When a pair lands in the gap (bold under 14 pt, ratio between 3 and 4.5), write *"passes Apple's table, fails WCAG AA"* rather than a bare PASS, because a claim of WCAG conformance would be false. WCAG's points are CSS points and iOS points are logical points; treat them as equal only as an approximation, and say so when a verdict hangs on it.
- **What is exempt.** *[WCAG 1.4.3 / 1.4.11]* Disabled controls, inactive placeholders, and pure decoration are held to no bar at all. Meaningful non-text — control borders, focus rings, icons, chart strokes that carry data — is held to **3:1**, never to the text bar.
- **Where AAA is owed.** *[house]* Ship to AA (4.5 normal / 3 large+UI). AAA is a stretch goal, except where the app's own design notes already promise 7:1 — then hold them to it.

*[Apple]* If the app misses the minimum by default, it must at least raise contrast when **Increase Contrast** is on, and Dark Mode is checked separately. That is why every pair is measured in three appearances.

The size floor has two tiers, from HIG *Accessibility*'s control-size table (verified 2026-10-30):

| Platform | Default control size | Minimum control size |
| --- | --- | --- |
| iOS, iPadOS | 44×44 pt | 28×28 pt |
| macOS | 28×28 pt | 20×20 pt |
| tvOS | 66×66 pt | 56×56 pt |
| visionOS | 60×60 pt | 28×28 pt |
| watchOS | 44×44 pt | 28×28 pt |

A target **below the minimum fails**. A target **below the default but at or above the minimum is a finding at lower severity** — Apple asks you to strive for the default, not to hit it. *[Apple]* Spacing counts as much as size: about **12 pt of padding around a bezeled control**, about **24 pt around the visible edges of a bezel-less one**. It has the same shape as contrast: the numbers are trivial, deciding *what they apply to* is not. See step 6.

## Step 1 — Gather

Run the bundled, project-agnostic gatherer from inside the app repo, calling it by its path in this skill's folder (the commands below shorten that path to `scripts/`). It takes no arguments and auto-discovers colorsets + their appearance variants, every color literal + where the palette lives, foreground-vs-background usage, existing legibility infra, the accessibility-env coverage, and Dynamic-Type signals:

```bash
bash scripts/gather-color-signals.sh
```

Read it, don't skim — section [1] (where the palette lives) plus [2] (foreground vs background) are the raw halves you assemble into pairs.

Section [2] has four subsections, and **two of them exist because grepping foregrounds cannot find them**: a `.borderedProminent` / `.glassProminent` button draws a forced white label with no `.foregroundStyle` anywhere in the source, and a fill arriving as a `Color` parameter has one background per caller. Both are real pairs; neither appears in the foreground list above them. Read all four.

## Step 2 — Build the pair list (this is the work)

From [1]+[2], write the concrete pairs that actually render together: each *text or control color* × *the background directly behind it*, **once per appearance — Light, Dark, Increase Contrast.** Resolve adaptive colors to their per-appearance component values (the `Color(light:dark:)` / `adaptiveColor(...)` helpers list both; a colorset's Contents.json lists each variant **and its `color-space`** — carry that with the value, because `display-p3` components are not sRGB and the script needs the `p3:` prefix for them). Where there's no Increase-Contrast variant, the appearance simply reuses the default — say so, because that's usually where the failure hides.

**Resolve every background AT THE SITE — open the file and read the stack.** The **composite** is one of three ways an assumed background goes wrong, all three observed in a single pass. The other two: the **token name** (a circle filled with a token called `accentText` is dark rose, so the "on-accent" label is the wrong end — read the definition, not the name), and an **adaptive** value moving under you (`systemGray4` is `#D1D1D6` Light / `#3A3A3C` Dark, so the pair swings both ways and a *fixed* label can only win at one end — see [`references/worked-pass.md`](references/worked-pass.md)). The recurring traps of this step — two-way helpers with no Increase-Contrast path, token names, opacity, hard-coded system hex — are in [`references/sharp-edges.md`](references/sharp-edges.md).

**For a parameterized fill, enumerate or resolve.** Grep the call sites for the arguments actually passed and measure each; if they span light and dark fills, no constant wins and the label must be computed. Resolve at runtime with `Color.resolve(in:)`: [`references/contrasting-label.md`](references/contrasting-label.md) carries the resolver and the one wiring constraint it has.

| Surface | Foreground | Background (resolved at the site) | Appearance | Notes |
| --- | --- | --- | --- | --- |
| Section label | Theme.accent | Theme.paper | Light / Dark / IC | small text → 4.5:1 row |
| CTA label | .white | Theme.accentFill | Light / Dark | large/bold → 3:1 row |
| Readout over canvas | … | gradient/diagram | all | composite → worst-case stop |
| Chip label | ? | `tint:` **param** — teal, indigo, … | all | one row per argument, or resolve |
| Pill over cover photo | … | composite: black `0.76` scrim | all | scrim ⇒ **dark in both** |

**Done when every foreground in gather section [2] is accounted for** — each one appears in a row, or in a one-line note saying why it needs none (decorative, disabled, system-managed). The gatherer prints that list, so this is countable: a pair list shorter than it is unfinished. The sites that ship broken are not the mis-measured ones — they are the ones that never reached the list.

## Step 3 — Compute every ratio

```bash
python3 scripts/contrast-ratio.py "#2F6E92 on #FAF7F3"
python3 scripts/contrast-ratio.py "0.184,0.431,0.573 / 0.98,0.97,0.95"   # SwiftUI 0..1 literals
python3 scripts/contrast-ratio.py "p3:0.612,0.769,0.871 on #FFFFFF"      # display-p3 colorset value
python3 scripts/contrast-ratio.py "#fff@0.7 on #3A3A3C"                  # .white.opacity(0.7)
python3 scripts/contrast-ratio.py "#fff on #000@0.76 on #F2C94C"         # scrim over a tint: layers top first
printf '0.3,0.3,0.3 0.96,0.96,0.96 textSecondary-on-bg\n' | python3 scripts/contrast-ratio.py        # stdin: fg bg label
```

It accepts hex, sRGB 0..1 (the SwiftUI `Color(red:green:blue:)` form), 0..255 (`--255`), and Display-P3 values (`p3:` token prefix, or `--p3` — use whichever space the colorset's Contents.json declares); it prints the ratio and PASS/FAIL for every bar. Any token can carry `@alpha`, and a background can be a stack joined by ` on `, top layer first, ending on an opaque layer — so a scrim or an `.opacity()` is measured as the composite it is. A material, blur, or vibrancy has no fixed value to feed it; those need a measured screenshot or a scrim that guarantees the floor. `--selftest` checks the math against fixed answers; `--help` documents the rest. **Verify any inline contrast comment with the script** — trust the number, not the note.

**Say how each number was obtained.** A ratio from colorset values read in source is *computed from declared colors*; one from a pixel sample of a simulator screenshot is *measured*; one where you assumed what sits behind the text is *assumed*. Label each row with its kind. An assumed background is the most common way a wrong PASS ships.

## Step 4 — Check the non-ratio HIG legibility axes

Contrast is necessary, not sufficient. Also flag, from the gather output and the views:
- **Color-only state encoding** (red/green status, a selected tab by tint alone). HIG: *convey information with more than color alone* — add a shape/glyph/label, and honor **Differentiate Without Color** (`environment(\.colorSchemeContrast)` is contrast; differentiate-without-color is its own env value). Gather section [4] shows whether anything reads it.
- **Text over imagery, Material, or a gradient** is a composite — worst-case stop, or a scrim that guarantees the floor. Material additionally *adapts*, so it pairs to no fixed hex at all.
- **Dynamic Type**: body text on `\.system(size:)` doesn't scale. Section [5] tallies fixed vs Dynamic-Type-aware fonts; fixed sizes are for glyphs/decoration, not reading text.

## Step 5 — Respect existing infra (subtract before flagging)

From gather section [3], find scrims, vibrancy, shadows-under-text, and contrast-aware types (e.g. a readout that goes opaque + scrims under Increase Contrast). A surface those already protect is **not** a finding — but protected is still *measured*, against the composite: a dark warning token on a `0.76` black scrim measured **2.94:1** where the plain tint measured 7.16:1. And **a sibling on the same surface is evidence** — if the pill next to yours is white, the surface is always dark, and a dark label is the wrong end. Decorative graphics take the exemptions under *What is exempt* above.

## Step 6 — Touch targets (the other numeric floor)

From gather section [6]. The bars are the two tiers in the table above, read for the platform the view ships on, and the pairing is *tappable thing × **effective hit rect***. Report a sub-minimum target as a failure and a sub-default one as a lower-severity finding, so the fix list leads with what fails.

**The effective rect is not the frame you can name** — the exact analogue of the composite on the color side. `.padding()`, `.contentShape()`, a `minWidth`/`minHeight`, and the row height a `List` or `Form` imposes all enlarge it, so a 20 pt glyph inside a padded button already passes and is **not** a finding. Resolve the rect at the site the same way you resolve a background: open the file and read what wraps it.

So the two lists in section [6] are deliberately unjoined, and joining them is the work:

- A **small frame that is not tappable** — a swatch, a divider, a rule, a decorative glyph, a chart element — has no bar at all. Don't flag it. This is the size half's version of *decorative ≠ text*, and it is the majority of what the candidate list prints.
- A **tappable thing with no explicit frame** can still fail: an `Image(systemName:)` in a toolbar or a bare `Text` with `.onTapGesture` gets only its intrinsic size. Absence from the small-frame list is not a pass.
- **Adjacent** targets matter as much as small ones: two 44 pt buttons flush against each other still mis-hit. Prefer spacing between them (the 12 / 24 pt guidance above), not shrinking them.

**A source-level size finding is a candidate until the effective geometry is seen.** Modifiers applied by a parent, a custom `ButtonStyle`, or a container's row height can enlarge the rect in ways a single file does not show. Where the verdict is close, confirm the rendered frame: the Xcode `device-interaction` skill (when present) reads the UI hierarchy with element frames, and Accessibility Inspector shows the hit region on device. Report unconfirmed rows as *candidate*.

Fix by **enlarging the rect, not the art**: `.contentShape(Rectangle())` over a padded frame, a `.frame(minWidth: 44, minHeight: 44)`, or extra `.padding` — the glyph keeps its size and the design doesn't change. Growing the icon to 44 pt is the wrong fix and the one that shows.

## Step 7 — Propose minimal fixes (prioritized)

Read [`references/worked-pass.md`](references/worked-pass.md) first: one real fix that cost an appearance, measured end to end.

One table, and it has a **`before → after` cell for every appearance** — the smallest fix is worth nothing if it costs an appearance you didn't look at:

| Pair (fg × resolved bg) | Smallest fix | Kind | Precondition that holds here | Light | Dark | Increase Contrast |
| --- | --- | --- | --- | --- | --- | --- |
| Avatar initial × `systemGray4` | `.white` → `.primary` | code | — (adaptive both sides) | 1.52 → **13.80** | 11.35 → **11.35** | no variant — as default |
| CTA label × Theme.accent | fill → `accentFill` #327599 | code | label is forced white by `.borderedProminent` | 5.58 → 5.07 *(trade)* | 1.85 → **5.07** | no variant — as default |

**Fill every cell, including the appearances that already passed** — a blank is how a regression ships.

**The precondition column travels with the token.** A token is fixed-dark *because* something at this site forces a white label; carried to a site where nothing does, it is wrong. `accentProminentFill` got applied to a progress bar by name similarity, and the name is not the reason. Write the reason down, or the next site inherits the value without it.

Then apply the gate — **the script enforces it, so run it rather than eyeballing the table**:

```bash
# before after, once per appearance; exits 1 on any bar crossing PASS -> FAIL
python3 scripts/contrast-ratio.py \
  --regress "#fff on #3A3A3C" "#fff on #8E8E93"
```

> **No appearance may cross from passing to failing.** That is the regression that actually ships — the worked pass is one. A drop that stays above the bar (5.58 → 5.07, row two) is a **trade**, not a regression: take it if it's the smallest fix, and mark it in the table. If no candidate raises the failing appearance without failing another, the *pairing* is wrong — change the background or add a scrim, not the foreground.

**Fixes propagate by fill, not by file.** After fixing a pair, grep every *other* consumer of that same fill and fix them together — the bug belongs to the fill, and the file you found it in is an accident of where you were looking. Three sites shipped broken in one real pass because the fix stopped at the file boundary.

**Order of operations for a bulk pass** (dozens of files): do the **mechanical sweep first, hand-decided sites last**. A late sweep silently overwrote a deliberate hand-edit, because a sweep cannot tell a considered exception from an unfixed instance. Never sweep after hand-editing.

The fix itself is the *smallest* one that crosses the line: a specific L\*/luminance nudge (give the new hex + its new ratio), an adaptive token where both sides move (`.primary` over `.white`), a scrim/vibrancy, a weight/size bump that drops the row to the 3:1 threshold, or a high-contrast asset variant. Lead with text that fails AA-normal in a default appearance (the most users, the worst read). Mark each as code-fix vs asset-catalog-fix. Stop here; get the pick before editing. On approval, make the change and re-run step 3 **for every appearance** to fill the `after` column — the numbers you ship are the ones the script printed, not the ones you expected.

## External references

- **Apple docs (append `.md` to the developer.apple.com URL):** HIG *Accessibility* (`/design/human-interface-guidelines/accessibility` — the contrast and control-size tables) · HIG *Color* (`/design/human-interface-guidelines/color` — system color Light/Dark/Increase-Contrast values, "supply light, dark, and increased-contrast variants") · HIG *Dark Mode* · App Store Connect *Sufficient Contrast* / *Differentiate Without Color* / *Larger Text* accessibility-label criteria.
- **The tables here are a snapshot, dated where they appear.** Before citing one, fetch the page's `.md` and read its *Change log* table. A dated entry newer than the verification date means the page wins over this file. If the fetch fails, say the number is unverified rather than citing it as current.
- **Xcode's own agent skills, when present.** `xcrun mcpbridge run-agent claude` loads them; `xcrun agent plugin path --plugin-format claude` prints the folder holding all of them (`xcrun agent skills export` writes only a subset, without the accessibility and translation skills). Apple wrote them, so on their topics they outrank this file and training memory. `accessibility-sufficient-contrast-specialist` audits one view's contrast; it applies WCAG's large-text row (≥ 18 pt regular or ≥ 14 pt bold), not the HIG table — more evidence that the bold-text gap above is real. Its PASS / FAIL / NEEDS VERIFICATION verdict matches this skill's computed-vs-assumed labels: an unresolved color is never a guessed PASS. This skill stays the app-wide pass (every pair, three appearances, the regression gate); `accessibility-dynamic-type-specialist` and `accessibility-voiceover-specialist` cover the axes step 4 only flags. Also: `app-resizability` for layouts that must survive window resizing, iPhone Duo, split screen, or Stage Manager — a contrast or target pass on such an app checks each size class it reaches; `swiftui-specialist` for SwiftUI API questions a fix raises; `device-interaction` for screenshots and element frames on a simulator. They are not installed globally — if absent, say so rather than guessing their contents.
- **UI words** — capitalization, button labels, alert wording — are a copywriting pass, not this audit. An installed HIG-copy skill owns them.
