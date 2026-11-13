#!/usr/bin/env bash
# Gather the raw signals for a HIG contrast + touch-target audit in one shot —
# project-agnostic. Surfaces the app's COLORS (asset-catalog colorsets + Color/UIColor/RGBA
# literals + the Theme/palette type), the text-on-background MATERIAL (foreground vs
# background/material usage, INCLUDING the two families a foreground grep cannot see —
# forced-label button styles and color arriving as a parameter), any EXISTING legibility
# infra to respect, the accessibility-env COVERAGE (Increase Contrast / Differentiate
# Without Color / Reduce Transparency / Dynamic Type), and TOUCH-TARGET candidates.
# It does NOT compute ratios — pair the colors it finds and run contrast-ratio.py.
# Nor does it decide a touch-target finding: it prints small frames and tappable surfaces
# separately, because the effective hit rect is what counts and padding/contentShape move it.
#
# Usage:  bash <skill-dir>/scripts/gather-color-signals.sh
# No args. Reads current working-tree state. Run it from inside the repo you're auditing.
#
# It guesses and labels every guess. The hard part of this audit is FINDING THE PAIRS;
# this script gives you the two halves (foreground colors, background colors) and where
# they're declared — you decide which actually ship together on screen.
set -uo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo .)"
cd "$ROOT" || exit 1
SW=(grep -rn --include='*.swift' --exclude-dir=.build --exclude-dir=build --exclude-dir=DerivedData --exclude-dir=Pods --exclude-dir=checkouts --exclude-dir=Screenshots)
SWO=(grep -roh --include='*.swift' --exclude-dir=.build --exclude-dir=build --exclude-dir=DerivedData --exclude-dir=Pods --exclude-dir=checkouts --exclude-dir=Screenshots)
# Screenshots/ is excluded: App Store screenshot tooling's colors never ship on device.

echo "========== PROJECT: $ROOT =========="

echo
echo "========== [0] ASSET-CATALOG COLORSETS (appearance variants + COLOR SPACE) =========="
echo "  Each colorset should ideally carry light + dark + a HIGH-CONTRAST variant."
echo "  A missing 'value: high' appearance = no Increase-Contrast fallback (HIG asks for one)."
echo "  COLOR SPACE matters for the math: 'display-p3' components are NOT sRGB — pass them"
echo "  to contrast-ratio.py with the p3: prefix, or the ratio is wrong near thresholds."
found=0
while IFS= read -r cj; do
  [[ -z "$cj" ]] && continue
  found=1
  name=$(basename "$(dirname "$cj")")
  variants=""
  grep -q '"luminosity" *: *"dark"\|"value" *: *"dark"' "$cj" 2>/dev/null && variants+="dark "
  grep -q '"value" *: *"high"' "$cj" 2>/dev/null && variants+="HIGH-CONTRAST " || variants+="(no-high-contrast) "
  spaces=$(grep -o '"color-space" *: *"[^"]*"' "$cj" 2>/dev/null | cut -d'"' -f4 | sort -u | tr '\n' ' ')
  echo "  • $name — variants: light ${variants}— color-space: ${spaces:-srgb(unspecified)}"
done < <(find . -path '*.colorset/Contents.json' -not -path '*/.build/*' -not -path '*/build/*' -not -path '*/checkouts/*' -not -path '*/Screenshots/*' 2>/dev/null | sort)
[[ "$found" == 0 ]] && echo "  (no .colorset catalogs — colors are defined in code; see [1])"

echo
echo "========== [1] COLOR LITERALS & THE PALETTE TYPE (the foreground/background ingredients) =========="
echo "  --- the Theme / palette / color-scheme type(s) ---"
"${SW[@]}" -lE 'enum (Theme|Palette|ColorScheme)\b|extension Color\b|struct (Theme|Palette)\b' . 2>/dev/null \
  | grep -viE 'Test' | sed 's/^/  /' || echo "  (none — likely all-system-color app)"
echo
echo "  --- raw color literals (each is a concrete sRGB value you can feed the ratio script) ---"
echo "      SwiftUI Color(red:green:blue:) is 0..1; hex 0xRRGGBB is 0..255."
"${SW[@]}" -E 'Color\(red:|Color\(hex:|Color\(0x|Color\(light:|UIColor\(red:|RGBA\(|adaptiveColor\(|\bColor\(\.sRGB' . 2>/dev/null \
  | grep -viE '/Tests?/|Test\.swift' | head -60
echo
echo "  --- count by file (where the palette really lives) ---"
"${SW[@]}" -E 'Color\(red:|Color\(hex:|Color\(0x|Color\(light:|UIColor\(red:|RGBA\(|adaptiveColor\(' . 2>/dev/null \
  | grep -viE '/Tests?/|Test\.swift' | cut -d: -f1 | sort | uniq -c | sort -rn | head -15

echo
echo "========== [2] FOREGROUND vs BACKGROUND (raw material for the on-screen PAIRS) =========="
echo "  --- foreground (text/icon) colors: .foregroundStyle / .foregroundColor / .tint / .fill ---"
"${SWO[@]}" -E '\.foregroundStyle\([^)]*\)|\.foregroundColor\([^)]*\)|\.tint\([^)]*\)' . 2>/dev/null \
  | grep -viE 'foregroundStyle\(\.tint\)|foregroundStyle\(\.primary\)' \
  | sed -E 's/^[[:space:]]*//' | sort | uniq -c | sort -rn | head -25 || echo "  (none)"
echo
echo "  --- FORCED-LABEL styles: a foreground that appears NOWHERE in the source ---"
echo "      .borderedProminent & friends draw a WHITE label with no .foregroundStyle to"
echo "      grep, so the subsection above is structurally blind to them. Each hit below is"
echo "      a real pair: the forced label × whatever fill/tint the style resolves to."
"${SW[@]}" -E '\.buttonStyle\(\.[A-Za-z]*[Pp]rominent\)|\.buttonStyle\(\.bordered\)|\.pickerStyle\(\.segmented\)|\.toggleStyle\(|\.controlProminence|\.prominent\b' . 2>/dev/null \
  | grep -viE '/Tests?/|Test\.swift' | head -25 || echo "  (none)"
echo
echo "  --- PARAMETERIZED color inputs: each is a SET of pairs, not a pair ---"
echo "      A fill arriving as an argument has as many backgrounds as it has callers, so no"
echo "      fixed label color is right for all of them. Grep each one's call sites and"
echo "      enumerate the arguments actually passed, or resolve the label at runtime."
"${SW[@]}" -E '\b[a-zA-Z]*([Tt]int|[Cc]olor|[Ff]ill|[Bb]ackground|[Aa]ccent)[A-Za-z]*: *Color\b|: *Color *=|-> *Color\b' . 2>/dev/null \
  | grep -viE '/Tests?/|Test\.swift' | head -25 || echo "  (none)"

echo
echo "  --- backgrounds & materials sitting BEHIND that text ---"
"${SWO[@]}" -E '\.background\([^)]*\)|\.(ultraThin|thin|regular|thick|ultraThick)Material|Material\b|LinearGradient|\.fill\([^)]*\)' . 2>/dev/null \
  | sed -E 's/^[[:space:]]*//' | sort | uniq -c | sort -rn | head -25 || echo "  (none)"
echo
echo "  NOTE: text drawn over a GRADIENT, IMAGE, or Material has no single background color."
echo "  Test the WORST-CASE stop (the lightest part of the gradient under light text, etc.)"
echo "  or confirm a scrim/vibrancy guarantees the floor. Material is adaptive — don't hard-pair it."

echo
echo "========== [3] EXISTING LEGIBILITY INFRA — respect it, don't re-flag what it already solves =========="
"${SW[@]}" -iE 'scrim|legib|contrastRatio|relativeLuminance|readout|vibranc|\.shadow\(' . 2>/dev/null \
  | grep -viE '/Tests?/|Test\.swift' | head -20 || echo "  (none found — no scrim/vibrancy/shadow safety net)"

echo
echo "========== [4] ACCESSIBILITY-ENV COVERAGE (does the UI react to the contrast settings?) =========="
echo "  HIG: if you don't meet contrast by DEFAULT, you MUST raise it when Increase Contrast is on,"
echo "  and you must not encode meaning with color alone. These are the env reads that do that:"
for needle in colorSchemeContrast accessibilityDifferentiateWithoutColor differentiateWithoutColor accessibilityReduceTransparency reduceTransparency accessibilityInvertColors; do
  n=$("${SW[@]}" -E "\.$needle\b|$needle" . 2>/dev/null | grep -viE '/Tests?/|Test\.swift' | wc -l | tr -d ' ')
  printf "  %-42s %s read-site(s)\n" "$needle" "$n"
done

echo
echo "========== [5] DYNAMIC TYPE / LEGIBLE TEXT (a non-contrast HIG legibility axis) =========="
echo -n "  fixed-size fonts  .system(size:)  (do NOT scale with Dynamic Type): "
"${SWO[@]}" -E '\.system\(size:' . 2>/dev/null | grep -viE '/Tests?/' | wc -l | tr -d ' '
echo -n "  Dynamic-Type-aware  (.font(.body/.title…) / relativeTo: / ScaledMetric / dynamicTypeSize): "
"${SWO[@]}" -E 'ScaledMetric|relativeTo:|dynamicTypeSize|\.font\(\.(largeTitle|title|title2|title3|headline|subheadline|body|callout|footnote|caption)' . 2>/dev/null | grep -viE '/Tests?/' | wc -l | tr -d ' '
echo "  (lots of fixed .system(size:) on body text = a Dynamic Type gap; reserve fixed sizes for glyphs/decor."
echo "   caveat: .system(size:) fed by a @ScaledMetric IS Dynamic-Type-aware — read the hits before flagging.)"

echo
echo "========== [6] TOUCH TARGETS (the other numeric floor: two tiers) =========="
echo "  HIG control sizes, default / minimum: iOS, iPadOS, watchOS 44x44 / 28x28 pt;"
echo "  macOS 28x28 / 20x20; tvOS 66x66 / 56x56; visionOS 60x60 / 28x28. Below the"
echo "  minimum FAILS; below the default is a lower-severity finding. The numbers are trivial;"
echo "  finding the pairs is not — and the pairing here is TAPPABLE THING x EFFECTIVE HIT"
echo "  RECT. The effective rect is NOT the frame you can name: .padding() and"
echo "  .contentShape() enlarge it, so a 20 pt icon inside a padded button already passes."
echo "  Subtract the infra in the third list before flagging anything in the first."
echo
echo "  --- frames declared under 44 pt, [<28] = under the iOS minimum (CANDIDATES, not findings) ---"
"${SW[@]}" -oE '\.frame\([^)]*\)' . 2>/dev/null \
  | grep -viE '/Tests?/|Test\.swift' \
  | awk '{
      rest=$0; small=0; tiny=0
      while (match(rest, /(width|height|minWidth|minHeight)[[:space:]]*:[[:space:]]*[0-9]+(\.[0-9]+)?/)) {
        seg=substr(rest, RSTART, RLENGTH); sub(/^[^0-9]*/, "", seg); v=seg+0
        if (v > 0 && v < 44) small=1
        if (v > 0 && v < 28) tiny=1
        rest=substr(rest, RSTART+RLENGTH)
      }
      if (small) print (tiny ? "  [<28] " : "  [<44] ") $0
    }' | head -30 || echo "  (none)"
echo "  (a small frame on something NON-tappable — a swatch, a divider, a decorative glyph —"
echo "   is not a finding. Cross-reference against the tappable list below.)"
echo
echo "  --- tappable surfaces (each needs an effective rect >= 28x28, should reach 44x44) ---"
"${SW[@]}" -E 'Button\(|Button *\{|\.onTapGesture|NavigationLink|\.onLongPressGesture|Toggle\(|Stepper\(|\.buttonStyle\(' . 2>/dev/null \
  | grep -viE '/Tests?/|Test\.swift' | wc -l | tr -d ' ' | sed 's/^/  tappable call sites: /'
"${SW[@]}" -lE 'Button\(|Button *\{|\.onTapGesture|NavigationLink' . 2>/dev/null \
  | grep -viE '/Tests?/|Test\.swift' | sed 's/^/    /' | head -20
echo
echo "  --- hit-area infra to SUBTRACT (these enlarge the rect; respect them) ---"
"${SW[@]}" -E '\.contentShape\(|\.padding\([^)]*\)[^\n]*\.onTapGesture|\.hitTestPadding|\.frame\([^)]*minWidth: *4[4-9]|\.frame\([^)]*minHeight: *4[4-9]' . 2>/dev/null \
  | grep -viE '/Tests?/|Test\.swift' | head -20 || echo "  (none — no explicit hit-area expansion found)"

echo
echo "========== DONE =========="
echo "Next: from [1]+[2], assemble the PAIRS that actually ship together (text color × the"
echo "background behind it), in EACH appearance — light, dark, AND Increase Contrast. Then:"
echo "  python3 <skill-dir>/scripts/contrast-ratio.py \"<fg> on <bg>\""
echo "Verify any inline '~4.9:1' / 'ensures 7:1' comments with the script — trust the number, not the note."
