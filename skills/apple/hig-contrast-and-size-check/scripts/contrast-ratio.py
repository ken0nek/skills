#!/usr/bin/env python3
"""Compute the WCAG 2.x contrast ratio for color pairs and print pass/fail.

The ratio uses *relative luminance* with the sRGB linearization the WCAG
definition mandates — NOT a naive RGB difference. This is the one place the
audit's math lives, so every pair check is deterministic and reproducible.

Thresholds reported (WCAG 2.1/2.2 AA + AAA):
  AA  normal text  >= 4.5:1     AAA normal text >= 7.0:1
  AA  large text   >= 3.0:1     AAA large text  >= 4.5:1
  UI components / graphical objects >= 3.0:1   (non-text controls, focus rings, icons)
Large text = >= 18pt regular OR >= 14pt bold (WCAG, in CSS points). Apple's
HIG table differs: >= 18pt at any weight, or bold at ANY size, drops to the
3:1 row. The script can't see the font, so it reports every row; you pick the
one that fits and say which standard you picked it under.

Color spaces — sRGB is the default; Display-P3 is supported and MATTERS:
asset-catalog colorsets are often "display-p3", and P3 component
values fed through sRGB luminance give wrong ratios (worst near the 4.5:1 line).
  p3:0.72,0.52,0.04      per-token prefix: this token is Display-P3
  --p3                   flag: treat every unprefixed token as Display-P3
A pair may mix spaces (a P3 colorset value on an sRGB system background).
Luminance is computed with each space's own Y coefficients (Display-P3 D65),
which is exact — no gamut mapping is involved for a luminance-only ratio.

Color formats (foreground first, background second):
  hex          fff  #fff  ffffff  #FFFFFF
  sRGB 0..1    0.72,0.52,0.04        (matches SwiftUI Color(red:green:blue:))
  sRGB 0..255  with --255:  184,134,11
Translucency — any token may carry '@alpha' (0..1), and a background may be a
stack of layers, top first, joined by ' on '. The bottom layer must be opaque.
Layers are composited source-over in encoded extended sRGB (P3 layers are
converted first), then the foreground is composited over the result:
  contrast-ratio.py "#fff@0.7 on #3A3A3C"              # .white.opacity(0.7)
  contrast-ratio.py "#fff on #000@0.76 on #F2C94C"     # label on a scrim over a tint
Stacks need the ' on ' form; stdin lines take '@alpha' tokens but no stacks.
Pairs:
  contrast-ratio.py "#777 on #fff"        # ' on ' or '/' separates fg/bg in one arg
  contrast-ratio.py 777/fff
  contrast-ratio.py 777 fff               # two bare colors = one pair
  contrast-ratio.py 777 fff 000 ffcc00    # flat list, paired 2-by-2
  contrast-ratio.py "p3:1,0,0 on #fff"    # Display-P3 foreground, sRGB background
  echo "#777 #fff gray label" | contrast-ratio.py   # stdin: 'fg bg [label...]' per line
  (stdin comment lines start with '//' — NOT '#', which is a hex color)
Flags: --255 (channels are 0..255)  --p3 (unprefixed tokens are Display-P3)
       --strict (exit 1 if any pair fails AA normal)
       --regress (before/after gate — see below)
       --selftest (run the known-answer pairs and exit)

--regress: enforce "no appearance may cross from passing to failing"
  Pairs are consumed TWO AT A TIME as (before, after) — the pair you are
  replacing, then the pair you are installing. Every threshold bar is compared
  across the swap and the result is classified:
    REGRESSION  a bar went PASS -> FAIL. Exit 1. This is the failure that ships.
    TRADE       the ratio dropped but crossed no bar. Fine if it is the smallest fix.
    IMPROVED / NEUTRAL   the ratio rose, or nothing moved.
  Run it once per appearance (Light, Dark, Increase Contrast) — a fix is only
  safe when all three come back clean.
    contrast-ratio.py --regress "#fff on #3A3A3C" "#fff on #8E8E93"   # Dark: REGRESSION
    contrast-ratio.py --regress "#fff on #D1D1D6" "#000 on #D1D1D6"   # Light: IMPROVED
    echo "#fff #3A3A3C #fff #8E8E93 avatar Dark" | contrast-ratio.py --regress
  (stdin in this mode: 'before_fg before_bg after_fg after_bg [label...]' per line)
"""
import sys

# WCAG AA / AAA thresholds.
AA_NORMAL, AA_LARGE = 4.5, 3.0
AAA_NORMAL, AAA_LARGE = 7.0, 4.5
UI_COMPONENT = 3.0  # non-text UI elements & graphical objects (WCAG 1.4.11)

# The DISTINCT bars a fix can cross, for --regress. AA-large and UI-component
# share 3.0, and AA-normal and AAA-large share 4.5 — collapsing them keeps a
# single crossing from being reported twice.
BARS = (
    (AA_LARGE, "AA large/bold · UI component (3.0)"),
    (AA_NORMAL, "AA normal · AAA large/bold (4.5)"),
    (AAA_NORMAL, "AAA normal (7.0)"),
)

# Luminance (Y) coefficients per color space. Display-P3 shares the sRGB
# transfer curve but has wider primaries, so its Y row differs.
LUMA = {
    "srgb": (0.2126, 0.7152, 0.0722),
    "p3": (0.2289746, 0.6917385, 0.0792869),  # Display-P3, D65 (RGB->XYZ Y row)
}


def _linearize(c: float) -> float:
    """sRGB-curve encoded channel (0..1) -> linear-light value (WCAG normative
    form; Display-P3 uses the same transfer function)."""
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: tuple[float, float, float], space: str = "srgb") -> float:
    """Relative luminance (CIE Y, D65) from an encoded triple in 0..1."""
    kr, kg, kb = LUMA[space]
    r, g, b = (_linearize(x) for x in rgb)
    return kr * r + kg * g + kb * b


def contrast_ratio(
    fg: tuple[float, float, float],
    bg: tuple[float, float, float],
    fg_space: str = "srgb",
    bg_space: str = "srgb",
) -> float:
    """WCAG contrast ratio in [1, 21]. Order-independent (lighter / darker)."""
    l1, l2 = relative_luminance(fg, fg_space), relative_luminance(bg, bg_space)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def split_space(token: str, default_space: str) -> tuple[str, str]:
    """Peel an optional 'p3:'/'srgb:' prefix off a color token."""
    low = token.strip().lower()
    for prefix, space in (("p3:", "p3"), ("srgb:", "srgb")):
        if low.startswith(prefix):
            return token.strip()[len(prefix):], space
    return token.strip(), default_space


def parse_color(token: str, scale_255: bool = False) -> tuple[float, float, float]:
    """Parse hex (#rgb/#rrggbb) or comma/space triple into a 0..1 triple."""
    t = token.strip().lstrip("#").strip()
    if "," in t or (" " in t and not all(ch in "0123456789abcdefABCDEF" for ch in t.replace(" ", ""))):
        parts = [p for p in t.replace(",", " ").split() if p]
        if len(parts) != 3:
            raise ValueError(f"expected 3 channels, got {token!r}")
        vals = [float(p) for p in parts]
        # Auto-detect range: any value > 1 means 0..255; --255 forces it.
        if scale_255 or any(v > 1.0 for v in vals):
            vals = [v / 255.0 for v in vals]
        return tuple(max(0.0, min(1.0, v)) for v in vals)  # type: ignore[return-value]
    h = t
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    if len(h) != 6 or any(ch not in "0123456789abcdefABCDEF" for ch in h):
        raise ValueError(f"not a hex or RGB color: {token!r}")
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))  # type: ignore[return-value]


def _fmt(rgb: tuple[float, float, float], space: str) -> str:
    if space == "p3":
        return "P3(%.3f,%.3f,%.3f)" % rgb
    if any(c < 0 or c > 1 for c in rgb):
        return "xsRGB(%.3f,%.3f,%.3f)" % rgb
    return "#%02X%02X%02X" % tuple(round(c * 255) for c in rgb)


# Linear Display-P3 -> linear sRGB (both D65). Out-of-gamut results go below 0
# or above 1, which extended sRGB keeps.
P3_TO_SRGB = (
    (1.2249401, -0.2249404, 0.0),
    (-0.0420569, 1.0420571, 0.0),
    (-0.0196376, -0.0786361, 1.0982735),
)


def _encode(c: float) -> float:
    a = abs(c)
    e = a * 12.92 if a <= 0.0031308 else 1.055 * a ** (1 / 2.4) - 0.055
    return e if c >= 0 else -e


def _signed_linearize(c: float) -> float:
    return _linearize(c) if c >= 0 else -_linearize(-c)


def to_srgb(rgb: tuple[float, float, float], space: str) -> tuple[float, float, float]:
    """Encoded triple in `space` -> encoded extended-sRGB triple."""
    if space == "srgb":
        return rgb
    lin = [_linearize(x) for x in rgb]
    out = (sum(m * v for m, v in zip(row, lin)) for row in P3_TO_SRGB)
    return tuple(_encode(x) for x in out)  # type: ignore[return-value]


def split_alpha(token: str) -> tuple[str, float]:
    """Peel an optional '@alpha' (0..1) suffix off a color token."""
    if "@" not in token:
        return token, 1.0
    body, a = token.rsplit("@", 1)
    alpha = float(a)
    if not 0.0 <= alpha <= 1.0:
        raise ValueError(f"alpha must be 0..1, got {a!r}")
    return body, alpha


def _layer(token: str, scale_255: bool, default_space: str):
    body, alpha = split_alpha(token.strip())
    tok, space = split_space(body, default_space)
    return parse_color(tok, scale_255), space, alpha


def _over(top, alpha: float, bottom):
    return tuple(alpha * t + (1 - alpha) * b for t, b in zip(top, bottom))


def resolve_pair(fg_s: str, bg_s: str, scale_255: bool = False, default_space: str = "srgb"):
    """Return (fg_rgb, fg_space, bg_rgb, bg_space) as they render.

    Opaque, single-layer inputs come back untouched in their own space, so
    the plain path stays exact. Anything translucent is composited in
    extended sRGB and comes back as 'srgb'.
    """
    layers = [_layer(t, scale_255, default_space) for t in bg_s.split(" on ")]
    fg, fg_space, fg_alpha = _layer(fg_s, scale_255, default_space)
    if layers[-1][2] < 1.0:
        raise ValueError(f"bottom background layer must be opaque: {bg_s!r}")
    if len(layers) == 1 and fg_alpha == 1.0:
        bg, bg_space, _ = layers[0]
        return fg, fg_space, bg, bg_space
    rgb, space, _ = layers[-1]
    bg = to_srgb(rgb, space)
    for rgb, space, alpha in reversed(layers[:-1]):
        bg = _over(to_srgb(rgb, space), alpha, bg)
    fg = _over(to_srgb(fg, fg_space), fg_alpha, bg)
    return fg, "srgb", bg, "srgb"


def _luminance_any(rgb, space: str) -> float:
    kr, kg, kb = LUMA[space]
    r, g, b = (_signed_linearize(x) for x in rgb)
    return kr * r + kg * g + kb * b


def pair_ratio(fg, bg, fg_space: str, bg_space: str) -> float:
    l1, l2 = _luminance_any(fg, fg_space), _luminance_any(bg, bg_space)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def check(fg_s: str, bg_s: str, label: str = "", scale_255: bool = False,
          default_space: str = "srgb") -> bool:
    fg, fg_space, bg, bg_space = resolve_pair(fg_s, bg_s, scale_255, default_space)
    ratio = pair_ratio(fg, bg, fg_space, bg_space)

    def mark(ok: bool) -> str:
        return "PASS" if ok else "FAIL"

    head = f"{_fmt(fg, fg_space)} on {_fmt(bg, bg_space)}"
    if "@" in fg_s or " on " in bg_s or "@" in bg_s:
        head += f"  [composited from {fg_s} on {bg_s}]"
    if label:
        head += f"  ({label})"
    print(f"{head}\n  ratio {ratio:6.2f}:1")
    print(f"    AA  normal (4.5) {mark(ratio >= AA_NORMAL)}   "
          f"AA  large/bold (3.0) {mark(ratio >= AA_LARGE)}   "
          f"UI component (3.0) {mark(ratio >= UI_COMPONENT)}")
    print(f"    AAA normal (7.0) {mark(ratio >= AAA_NORMAL)}   "
          f"AAA large/bold (4.5) {mark(ratio >= AAA_LARGE)}")
    return ratio >= AA_NORMAL


def _ratio_of(fg_s: str, bg_s: str, scale_255: bool = False, default_space: str = "srgb") -> float:
    fg, fg_space, bg, bg_space = resolve_pair(fg_s, bg_s, scale_255, default_space)
    return pair_ratio(fg, bg, fg_space, bg_space)


def check_regression(before: tuple[str, str], after: tuple[str, str], label: str = "",
                     scale_255: bool = False, default_space: str = "srgb") -> bool:
    """Compare a pair swap against every bar. True = safe to ship (no bar lost).

    This is the gate the skill's step 7 states in prose: a fix that raises the
    appearance you are looking at while dropping one you are not is the
    regression that actually ships.
    """
    r_before = _ratio_of(before[0], before[1], scale_255, default_space)
    r_after = _ratio_of(after[0], after[1], scale_255, default_space)

    lost = [name for bar, name in BARS if r_before >= bar > r_after]
    gained = [name for bar, name in BARS if r_after >= bar > r_before]

    head = f"{before[0]} on {before[1]}  ->  {after[0]} on {after[1]}"
    if label:
        head += f"  ({label})"
    print(head)
    print(f"  ratio {r_before:6.2f}:1  ->  {r_after:6.2f}:1   ({r_after - r_before:+.2f})")

    if lost:
        print("  REGRESSION — bar(s) crossed PASS -> FAIL:")
        for name in lost:
            print(f"    ✗ {name}")
        print("  Fix the PAIRING, not the foreground: change the background or add a scrim.")
        return False
    if gained:
        print("  IMPROVED — bar(s) crossed FAIL -> PASS:")
        for name in gained:
            print(f"    ✓ {name}")
        return True
    if r_after < r_before - 0.005:
        print("  TRADE — ratio dropped but crossed no bar. Take it if it is the smallest fix,")
        print("  and mark it as a trade in the step-7 table.")
        return True
    print("  NEUTRAL — no bar moved.")
    return True


def _quads_from_args(args: list[str]) -> list[tuple[tuple[str, str], tuple[str, str], str]]:
    """Consume pair-args TWO AT A TIME as (before, after) for --regress."""
    pairs = _pairs_from_args(args)
    if len(pairs) % 2 != 0:
        raise ValueError("--regress needs pairs two at a time: before after [before after ...]")
    return [((pairs[i][0], pairs[i][1]), (pairs[i + 1][0], pairs[i + 1][1]), "")
            for i in range(0, len(pairs), 2)]


def _pairs_from_args(args: list[str]) -> list[tuple[str, str, str]]:
    """Yield (fg, bg, label). An arg with ' on ' or '/' is one pair; else flat 2-by-2."""
    joined = [a for a in args if (" on " in a) or ("/" in a)]
    if joined:
        out = []
        for a in joined:
            sep = " on " if " on " in a else "/"
            fg, bg = a.split(sep, 1)
            out.append((fg.strip(), bg.strip(), ""))
        return out
    if len(args) % 2 != 0:
        raise ValueError("flat color list must have an even count (fg bg fg bg ...)")
    return [(args[i], args[i + 1], "") for i in range(0, len(args), 2)]


SELFTEST = [  # (fg, bg, label, expected_ratio_rounded_2dp)
    ("#000", "#fff", "black on white (max)", 21.00),
    ("#fff", "#fff", "white on white (min)", 1.00),
    ("#777", "#fff", "mid-gray on white (just fails AA)", 4.48),
    ("#767676", "#fff", "AA-normal boundary gray", 4.54),
    ("#0088ff", "#fff", "saturated blue on white (passes UI 3.0, fails AA 4.5)", 3.52),
    ("f00", "#fff", "sRGB red on white", 4.00),
    ("p3:1,0,0", "#fff", "Display-P3 red on white (P3 Y row, not sRGB)", 3.76),
    ("p3:1,1,1", "p3:0,0,0", "P3 white on P3 black (max)", 21.00),
    ("#595959", "#fff", "AAA-normal boundary gray", 7.00),
    ("#949494", "#fff", "UI-component boundary gray", 3.03),
    ("#fff@0.5", "#000", "50% white over black composites to encoded 0.5", 5.28),
    ("#fff@0", "#3A3A3C", "fully transparent fg is the background itself", 1.00),
    ("#fff@1", "#3A3A3C", "alpha 1 is the opaque color", 11.35),
    ("#fff", "#000@0.76 on #F2C94C", "white on a 0.76 black scrim over a yellow tint", 12.99),
    ("p3:1,1,1@0.5", "p3:0,0,0", "P3 layers composite after conversion to sRGB", 5.28),
]

# The bars are >=, so a ratio a hair under a bar must FAIL it.
SELFTEST_VERDICTS = [  # (fg, bg, bar, expected_pass)
    ("#777", "#fff", AA_NORMAL, False),
    ("#767676", "#fff", AA_NORMAL, True),
    ("#5A5A5A", "#fff", AAA_NORMAL, False),
    ("#595959", "#fff", AAA_NORMAL, True),
    ("#959595", "#fff", UI_COMPONENT, False),
    ("#949494", "#fff", UI_COMPONENT, True),
]

SELFTEST_REGRESS = [  # (before, after, expected_safe, label)
    (("#fff", "#3A3A3C"), ("#fff", "#8E8E93"), False, "avatar Dark: AAA pass -> AA fail"),
    (("#fff", "#D1D1D6"), ("#000", "#D1D1D6"), True, "avatar Light: improved"),
    (("#fff", "#1A1A1A"), ("#fff", "#222222"), True, "small drop above every bar: trade"),
]

SELFTEST_ERRORS = [  # (fg, bg, label)
    ("#fff", "#000@0.5", "a translucent bottom layer has nothing to composite over"),
    ("#fff@1.5", "#000", "alpha above 1"),
]


def _selftest() -> int:
    ok = True
    for fg, bg, label, expected in SELFTEST:
        got = round(_ratio_of(fg, bg), 2)
        status = "ok" if abs(got - expected) <= 0.02 else "MISMATCH"
        ok &= status == "ok"
        print(f"  {status:8} {fg + ' on ' + bg:34} got {got:6.2f}:1  expected {expected:6.2f}:1   {label}")
    for fg, bg, bar, expected in SELFTEST_VERDICTS:
        got = _ratio_of(fg, bg) >= bar
        status = "ok" if got == expected else "MISMATCH"
        ok &= status == "ok"
        print(f"  {status:8} {fg + ' on ' + bg:34} {'PASS' if got else 'FAIL'} the {bar} bar")
    import contextlib
    import io
    for before, after, expected, label in SELFTEST_REGRESS:
        with contextlib.redirect_stdout(io.StringIO()):
            got = check_regression(before, after)
        status = "ok" if got == expected else "MISMATCH"
        ok &= status == "ok"
        print(f"  {status:8} --regress {label}")
    for fg, bg, label in SELFTEST_ERRORS:
        try:
            _ratio_of(fg, bg)
            status = "MISMATCH"
        except ValueError:
            status = "ok"
        ok &= status == "ok"
        print(f"  {status:8} rejects {fg} on {bg}: {label}")
    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    flags = {a for a in argv if a.startswith("--")}
    if "--selftest" in flags:
        return _selftest()
    scale_255 = "--255" in flags
    strict = "--strict" in flags
    default_space = "p3" if "--p3" in flags else "srgb"

    if "--regress" in flags:
        quads: list[tuple[tuple[str, str], tuple[str, str], str]] = []
        if args:
            quads = _quads_from_args(args)
        elif not sys.stdin.isatty():
            for line in sys.stdin:
                line = line.strip()
                if not line or line.startswith("//"):
                    continue
                toks = line.split()
                if len(toks) < 4:
                    continue
                quads.append(((toks[0], toks[1]), (toks[2], toks[3]), " ".join(toks[4:])))
        if not quads:
            print(__doc__)
            return 2
        safe = True
        for before, after, label in quads:
            try:
                if not check_regression(before, after, label, scale_255, default_space):
                    safe = False
            except (ValueError, KeyError) as e:
                print(f"  ERROR: {e}", file=sys.stderr)
                safe = False
            print()
        return 0 if safe else 1

    pairs: list[tuple[str, str, str]] = []
    if args:
        pairs = _pairs_from_args(args)
    elif not sys.stdin.isatty():
        for line in sys.stdin:
            line = line.strip()
            # '//' comments only — '#' starts a hex color, so it can't mark comments.
            if not line or line.startswith("//"):
                continue
            toks = line.split()
            if len(toks) < 2:
                continue
            pairs.append((toks[0], toks[1], " ".join(toks[2:])))
    if not pairs:
        print(__doc__)
        return 2

    all_ok = True
    for fg, bg, label in pairs:
        try:
            if not check(fg, bg, label, scale_255, default_space):
                all_ok = False
        except (ValueError, KeyError) as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            all_ok = False
        print()
    return (0 if all_ok else 1) if strict else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
