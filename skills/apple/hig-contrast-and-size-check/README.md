# hig-contrast-and-size-check

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Audit a SwiftUI app against the two floors Apple's HIG states as numbers:
color contrast and touch-target size.

**The moment it owns.** A palette, a screen, or a control is about to ship or
change, and someone needs to know it is readable and tappable in Light, Dark,
and Increase Contrast.

**Fires on**

- "check color contrast", "contrast audit", "is this readable", "is this
  legible", "WCAG contrast", "accessibility contrast", "HIG color check",
  "does this pass contrast", "dark mode contrast", "accessible colors",
  "contrast ratio", "increase contrast", "is my text readable on that
  background", "are these colors accessible"
- "touch target", "tap target", "hit area", "44 points", "is this button too
  small", "too small to tap"

**Not for** picking colors aesthetically, chart palettes, or the wording of UI
text.

**Leaves behind** a pair list covering every foreground the gatherer prints,
a ratio per pair per appearance labeled computed, measured or assumed, and a
prioritized fix table with `before → after` in all three appearances. Edits
wait for a go-ahead.

**Ships two scripts.** `scripts/gather-color-signals.sh` (bash, read only) prints the palette, the foreground and background sites, legibility
infra, and touch-target candidates. `scripts/contrast-ratio.py` (Python 3,
standard library only) computes WCAG ratios, composites alpha and scrims, and
enforces the no-regression gate. Read both before running them;
`contrast-ratio.py --selftest` checks its math against fixed answers.

## Why each line exists

**Why contrast is a pair in a context.** "Is this color accessible" has no
answer. The work is enumerating the pairs that render together, each in three
appearances, and the failures hide in the pairs that never reached the list.

**Why the background is the composite.** A scrim, an opacity, a material, or a
gradient sits between the named color and the eye. Measuring the token
instead of the stack is the most common way a wrong PASS ships.

**Why a parameterized fill is a set of pairs.** A fixed label over a fill that
moves can only be right at one end, and reads as correct in the one
appearance checked.

**Why every fix carries `before → after` in all three appearances, and the
gate is a script.** Fixes measured only where they failed have made other
appearances worse — a Light fix that dropped Dark from AAA to an AA failure
shipped. The script enforces the gate instead of trusting a table.

**Why the ratio math is bundled.** WCAG ratios run on relative luminance, not
RGB distance, and Display-P3 values read as sRGB give wrong answers near the
line. One deterministic script keeps every audit from re-deriving it.

**Why Apple's table and WCAG are both cited.** They disagree on small bold
text. A pair in that gap passes one and fails the other, and saying which is
the difference between a true and a false conformance claim.

**Why the hit rect, not the frame.** Padding, `contentShape`, and container
row heights enlarge the tappable area; a glyph that looks small often passes.

**Why mechanical sweeps run before hand-decided fixes.** A late sweep
overwrote a deliberate exception, because a sweep cannot tell one from an
unfixed instance.

## Tuning

A model that pads re-flags surfaces existing infra already protects. Point it
at step 5 before adding rules.

A model that widens scope redesigns the palette. The skill fixes pairings
minimally and leaves brand hues alone; sharpen that line first.

A model that stops early measures one appearance, or skips the pair-list
completeness count. Restate that a pair list shorter than the gatherer's
foreground list is unfinished.
