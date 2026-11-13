# A worked pass (real numbers — the "fix" that made it worse)

Read before step 7: the shape of a fix that regresses an appearance nobody measured.

An avatar placeholder: one letter on a filled circle. It fails, gets fixed, and the fix is *worse* — and the loop only closes because step 7 measured what it replaced. Every number below is `contrast-ratio.py` output.

1. **Resolve both sides at the site.** The fill is `Color(.systemGray4)` — *adaptive*: `#D1D1D6` Light, `#3A3A3C` Dark. The label is `.white`, fixed. One pair, two backgrounds.
2. **Measure each appearance** (step 3): white on `#D1D1D6` → **1.52:1**, fails everything. White on `#3A3A3C` → **11.35:1**, clears AAA. One real failure, and it is Light-only.
3. **The tempting fix — darken the fill until white reads:** `systemGray4` → `systemGray` (`#8E8E93`, the *same* value in both appearances). Light: **3.26:1** — still fails AA-normal. Dark: **11.35 → 3.26**, AAA pass to AA fail. It fixed nothing and cost an appearance, purely because it was measured only where it failed. **This shipped.**
4. **The actual fix — an adaptive background wants an adaptive foreground.** Keep the fill; change the *label*: `.white` → `.primary`. Light **13.80:1**, Dark **11.35:1** — both AAA. Hard-coding white over a color that moves was the bug, and no new color was invented.
5. **The systemic finding:** *a fixed label over a fill that moves* is the shape, and it recurs wherever the fill is a **parameter** — a chip taking `tint: Color` has no right constant, because `.teal` wants a dark label while `.indigo` wants white in Light and flips to dark in Dark. That's the step-2 resolver, not another per-site tweak.
