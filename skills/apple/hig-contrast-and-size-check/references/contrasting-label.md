# Resolving a label over a parameterized fill

Read from step 2, when a fill arrives as a parameter.

`Color.resolve(in:)` (iOS 17+) honors the appearance *and* Increase Contrast, and its `linear*` components **are** the WCAG linearization already — no gamma step, no P3→sRGB conversion, so this is strictly more accurate than hand-pairing hexes:


```swift
extension Color {
    /// The label — `darkLabel` or `.white` — with the higher WCAG ratio on `self`.
    /// Use wherever the fill is a PARAMETER; a fixed choice is wrong there.
    func contrastingLabel(in env: EnvironmentValues,
                          darkLabel: Color = .black, darkY: Double = 0) -> Color {
        let c = resolve(in: env)                        // iOS 17+
        let y = 0.2126 * Double(c.linearRed)
              + 0.7152 * Double(c.linearGreen)
              + 0.0722 * Double(c.linearBlue)
        return (y + 0.05) / (darkY + 0.05) >= 1.05 / (y + 0.05) ? darkLabel : .white
    }
}
```

It needs `@Environment(\.self) private var environment`, so a `View`-extension modifier that chains inline can't call it — move that body into a `ViewModifier` struct, which can.
