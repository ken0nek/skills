# Apple Platform Copy, CTAs & Localization — Reusable Guide

> A portable, project-agnostic reference for writing user-facing text on Apple platforms (iOS, iPadOS, macOS, tvOS, watchOS, visionOS): calls-to-action and button labels, in-app strings, error/empty/onboarding copy, and localization/internationalization.
>
> The bundled reference of the `hig-copywriting` skill. It distills Apple's Human Interface Guidelines and Localization developer docs into rules, checklists, and copy-paste patterns. Where Apple gives a component-specific rule, this guide follows the letter of that page rather than a generic principle.
>
> Adjacent lanes, owned elsewhere: in-app string-catalog mechanics (untranslated keys, dead keys, adding a locale) and the App Store listing's copy.

**Last verified against Apple docs:** 2026-10-30 (Apple's first-party `.md` — append `.md` to any HIG URL; none of the ten HIG pages under Sources has a change-log entry after December 16, 2025; Action sheets, Inclusion and Right to left publish no change log, so their content was not diffed). **Applies to:** all Apple platforms. **Scope:** UI/system copy + conversion surfaces + the engineering of localizable strings.

**This guide is a dated summary, not the authority.** Apple's live page wins wherever the two differ. Before citing a rule as Apple's, fetch that page's `.md` and read its *Change log* table: an entry dated after the verification date above means the page may have moved, so read the page. If the fetch fails, cite the rule as "per the bundled summary, verified 2026-10-30", not as current Apple guidance.

**Every rule carries its source,** so a review can tell Apple's guidance from this guide's own taste:

| Tag | Means | How to cite it in a finding |
|---|---|---|
| **[Apple · page]** | Stated on that Apple page | "HIG Alerts" — arguable on Apple's word |
| **[Apple skill]** | Stated in an Apple-written Xcode agent skill | "Apple, swiftui-specialist localization" |
| **[House]** | This guide's default where Apple leaves the choice open | "house default" — arguable on consistency, not on Apple's authority |
| **[Inference]** | Extends an Apple rule past what the page says | Name the rule it extends |

---

## 0. How to use this guide

- **Designers / PMs / writers** → Parts 1–3 (voice, CTAs, string patterns) + the [Copy review checklist](#copy-review-checklist).
- **Engineers** → Part 4 (localization mechanics) + the [Localization checklist](#localization-checklist). Wire the APIs from day one even if you ship one language — retrofitting is the expensive part.
- **Reviewers** → the two checklists are written to paste into a PR template.
- **One rule above all:** Apple's meta-principle is *pick a convention per element type and apply it consistently.* This guide gives you sensible defaults so "consistent" has a concrete target.

There are **two lenses**, and they govern **different surfaces** — don't let them fight:

| Surface | Governing lens | In practice |
|---|---|---|
| **System UI** — buttons, toggles, alerts, settings, empty states, errors, field hints, menus | **Apple HIG** | Concise, verb-first, clarity over cleverness, no marketing voice. |
| **Conversion surfaces** — paywall/upsell, onboarding hero, App Store listing, landing page | **Marketing/conversion craft**, *inside* HIG's honest tone | Benefit-led, specific, customer language. Never fabricated stats or hype. |

> When in doubt, default to HIG: *"Prioritize clarity and avoid the temptation to be too cute or clever."*

---

## Part 1 — Voice, tone & writing principles

### 1.1 Establish a voice, then vary tone by context
*[Apple · HIG Writing]*
- **Voice is constant; tone flexes.** Decide who you're talking to and how you want them to feel (a banking app conveys trust; a game conveys fun). Keep a **shared term list** so vocabulary stays consistent.
- **Match tone to the situation.** A fall-detection alert is straightforward and serious; a "personal record!" message is light and congratulatory. The *same app* uses both.

### 1.2 Be clear
*[Apple · HIG Writing]*
- Choose words that are easily understood. **Check each word — if you can cut it, cut it.** When in doubt, read it aloud.
- Put the **most important information first** on every screen. If you're conveying more than one idea, consider splitting across screens.
- Write for **everyone**: plain language, no jargon, no gendered terms — this also makes text easier to translate. (See [Part 5](#part-5--inclusive--accessible-language).)

### 1.3 Be action-oriented
*[Apple · HIG Writing]*
- **Active voice + verb-first labels** move people through your app. "Send" beats "Let's do it!"
- For links/buttons, **avoid "Click here"** in favor of descriptive phrasing ("Learn more about export options"). This is critical for screen-reader users, who navigate by labels.

### 1.4 Build language patterns
*[Apple · HIG Writing]*
- Consistency builds familiarity and makes future writing easier — reuse the same phrasings for the same actions. Returning to established patterns is a feature, not repetition.

### 1.5 Write for the device
*[Apple · HIG Writing]*
- Keep language consistent across devices, but **adapt to the input model**: say **"tap"** on touch devices, **"click"** on the pointer-driven Mac, etc. Never say "click" on iPhone.
- Small screens (Watch, iPhone) and far-viewing screens (TV) both demand **brevity**. TVs are shared/public — consider who's in the room.

---

## Part 2 — CTAs & buttons

A button combines three attributes: **Style** (size/color/shape), **Content** (symbol, text, or both), **Role** (semantic meaning). Get all three right.

### 2.1 Label content: verb-first, title-style (general buttons)
*[Apple · HIG Buttons, Alerts]*
- **Start with a verb** and write a few words that say what the button does: "Add to Cart", "Save Draft", "Turn On History".
- **Use title-style capitalization** for every button — content, chrome, and alerts alike. *(HIG → Buttons; HIG → Alerts: "As with all button titles, use title-style capitalization and no ending punctuation.")*
- Prefer **text** when a short label is clearer than an icon; pair with a familiar **SF Symbol** when one fits (e.g. `square.and.arrow.up` for share).

### 2.2 Prominence: one or two per view
*[Apple · HIG Buttons]*
- Give the **most likely action** a prominent (filled/accent) style. **Keep prominent buttons to one or two per view** — too many raise cognitive load.
- Distinguish the preferred choice by **style, not size.** Same-size buttons read as a coherent set; mismatched sizes look broken.

### 2.3 Roles (semantic, and they change appearance)
*[Apple · HIG Buttons]*

| Role | Meaning | Appearance |
|---|---|---|
| **Normal** | No special meaning | Default |
| **Primary** | The default / most-likely choice; responds to Return | App accent color |
| **Cancel** | Cancels the current action | Standard |
| **Destructive** | Can destroy data | System red |

- **Assign Primary to the most likely action** so Return confirms it and temporary views (sheets, alerts) auto-close.
- **Never make a destructive action the Primary/prominent button** — people press prominent buttons without reading. Keep Primary on the *non*-destructive option.

### 2.4 Multi-step flow vocabulary
*[Apple · HIG Writing]* Decide labels once and stay consistent across the flow:

`Get Started` → `Continue` / `Next` (optionally hint the next step) → `Done` (signals completion).

### 2.5 Alert / confirmation-dialog buttons
*[Apple · HIG Alerts]* Capitalization matches general buttons; the wording, OK/Cancel and placement rules below are alert-specific.
- **One or two words; verb phrase describing the result.** "View All", "Reply", "Ignore", "Erase", "Convert", "Delete".
- **Use title-style capitalization and no ending punctuation** — the same as all button titles.
- **Avoid "OK" except in purely informational alerts.** "OK" is ambiguous in a confirmation ("OK, do it" vs "OK, I understand"). A specific verb ("Erase", "Clear") tells people what they're doing.
- **In informational alerts, prefer "OK" over "Yes"/"No".**
- **Always title the cancel button "Cancel."** If a destructive action is present, include a Cancel button as the safe escape; **don't make Cancel (or any button) the default** if you want people to actually read the alert.
- **Placement:** default/most-likely button goes **trailing in a row / top in a stack**; Cancel goes **leading / bottom**.
- **Use the destructive style only for a destructive action people did *not* deliberately choose.** If the alert simply confirms an action they explicitly invoked (e.g. "Empty Trash"), the confirming button is *not* styled destructive — convenience of Return wins.
- **Don't explain buttons in body text.** If labels are clear, you don't need "Tap Delete to delete." When you must guide, use "choose" (device-neutral) and the exact title without quotes.

### 2.6 Conversion CTAs (paywalls, upsells)
*[House]* — Apple gives no paywall-specific copy rules; this is conversion craft held to HIG's tone.
- **Put the value in the label.** "Unlock Pro — $4.99" beats "Buy". "Start Free Trial" beats "Subscribe".
- Still obey HIG's tone: honest, no fake urgency. One prominent CTA is the house reading of Apple's "one or two per view".

### 2.7 Mechanics worth knowing
- *[Apple · HIG Buttons, iOS]* **Activity indicator in-button (iOS/iPadOS):** for actions that don't complete instantly, show an indicator and optionally swap the label ("Checkout" → "Checking out…"). Saves space, explains the wait.
- *[Apple · HIG Buttons, macOS push buttons; on iOS, inference]* **Trailing ellipsis = "needs more input."** A control title ending in `…` signals it opens another view/window for additional input before completing (e.g. "Export…"). Don't add an ellipsis to actions that complete immediately.
- *[Apple · HIG Accessibility, Buttons]* **Hit target:** aim for the default control size (44×44 pt on iOS, 60×60 pt on visionOS); never go under the minimum (28×28 pt on both). Other platforms → `hig-contrast-and-size-check`. Always provide a press/pressed state on custom buttons.

---

## Part 3 — In-app strings & text patterns

### 3.1 Capitalization — the system (the #1 source of inconsistency)
*[Apple · HIG Writing]* **Choose a case style per UI element type and apply it consistently.** Title case reads formal; sentence case reads casual. The rows below mix sources, tagged per row: Apple fixes buttons and alerts; the rest are house defaults that give "consistent" a target.

| Element | Case | Examples |
|---|---|---|
| *[Apple · Buttons, Alerts for buttons; House for the rest]* Buttons (alert buttons included), menu items and titles, tab and segment labels, table column headings, notification titles, toggle/row labels, nav titles, section headers | **Title Case**, no end punctuation, verb-first for actions | `Copy Link` · `Restore Purchases` · `View All` · `Keep Editing` · `By Category` |
| *[House]* Headlines / hero titles | Sentence case | "Plan your week in minutes" |
| *[House; Apple · Alerts for alert message text]* Body, footnotes, placeholders, full-sentence messages, errors | Sentence case + punctuation | "Add a photo to get started." |
| *[Apple · Alerts]* **Alert titles that are full sentences** | Sentence case **+ ending punctuation** | "Your subscription has expired." |
| *[Apple · Alerts]* **Alert titles that are fragments** | Title case, **no** punctuation | "Delete Account" |

> Capitalization rules are **language-specific**. Title Case is an English convention — Japanese has no case; German capitalizes nouns by its own rules. Don't force English title case onto translations (see [§4.7](#47-dont-impose-english-typography-on-other-languages)).

### 3.2 Error messages
*[Apple · HIG Writing]*
- **Display the error close to the problem**, avoid blame, and say **how to fix it**.
  - ✅ "Choose a password with at least 8 characters." ✅ "Use only letters for your name."
  - ❌ "That password is too short." ❌ "Don't use numbers or symbols." ❌ "Invalid name."
- **No "oops!" / "uh-oh".** Interjections read as insincere.
- If language alone can't rescue an error that hits many people, **redesign the interaction** — that's the real fix.

### 3.3 Empty states
*[Apple · HIG Writing]*
- A blank screen is an opportunity, but also daunting. **Guide people to the next step and give them a button/link** when possible.
- Don't put crucial, permanent information in an empty state — it disappears once the screen fills.
- *[House]* *Pattern:* a disabled feature's empty state should offer the **enabling button itself** (e.g. "Turn On History"), not a sentence telling people where Settings is.

### 3.4 Settings labels
*[Apple · HIG Writing]*
- Label settings as plainly as possible; add a one-line explanation if the label isn't enough.
- **Describe what ON does — people infer OFF.** ("Apple Watch can detect when you're washing your hands and start a 20-second timer.")
- To send someone to a setting, **link/deep-link to it** — don't describe its location in prose.

### 3.5 Text fields & data entry
*[Apple · HIG Writing, Entering data]*
- **Label every field; show hint/placeholder text** so people know the format: an example (`name@example.com`) or a description ("Your name").
- **Validate dynamically** and show the error **next to the field**, instructing how to enter it correctly — never scold.
- **Offer choices over typing** (picker/menu) when you can; support **paste and drag-and-drop**.
- **Pre-gather** anything the system already knows — don't ask for it. **Never prepopulate a password field.** Use a secure field for sensitive input.
- Gate "Next/Continue" until required data is present.

### 3.6 Possessives, "we", and person
*[Apple · HIG Writing]* for the first two bullets.
- **Use possessive pronouns sparingly.** "Favorites" == "Your Favorites" but shorter. If you use "your", use it consistently and don't switch perspective.
- **Avoid "we"/"our" to mean the app** — it's ambiguous and can feel falsely personal. ✅ "Unable to load content." ❌ "We're having trouble loading this content."
- *[House]* **Address people as "you"**, not "the user"/"the player" (distancing). Reserve "we/our" for the company/brand if at all.

### 3.7 Choose the right delivery method
*[Apple · HIG Writing, Alerts]* Match urgency/importance to channel — don't overuse interruptive UI. The table is a house summary of those pages:

| Need | Use |
|---|---|
| Critical, actionable, right now | **Alert** (sparingly) |
| Choices tied to an intentional action (incl. destructive) | **Action sheet / confirmation dialog** |
| Ambient / non-blocking status | Inline label, badge, banner |
| Time-shifted / outside the app | **Notification** |

- **Use alerts sparingly and only when actionable.** Don't use an alert just to inform — find an inline way. **Don't show an alert at app launch.** Don't alert for common, undoable destructive actions (deleting one email); *do* alert for uncommon, **irreversible** ones.

---

## Part 4 — Localization & internationalization

*[Apple · Xcode localization docs; Apple skill · swiftui-specialist `references/localization.md`]* unless a bullet says otherwise. When that Apple skill is loaded, it decides any string-engineering question this Part answers differently.

> **Internationalization** (engineering for any language/region) comes first; **localization** (translating for a locale) comes second. Build i18n-ready even for a single-language launch.

### 4.1 Wrap every user-facing string in a localizable API
Xcode extracts these into a **String Catalog** (`.xcstrings`) at build time.

```swift
// SwiftUI: string literals typed as LocalizedStringKey are automatically localizable.
Text("Title")
Label("Thanks for shopping with us!", systemImage: "bag")
Button("Checkout") { … }

// Plain Swift / model code:
String(localized: "Add a description here.")

// Different key vs. displayed value:
String(localized: "LIGHTING_KEY", defaultValue: "Lightbulbs")
```
- Pre–string-catalog targets: use `NSLocalizedString`.
- **Inside a SwiftUI view, pass the literal straight to `Text`/`Button`/`.navigationTitle`.** Wrapping it in `NSLocalizedString` or `String(localized:)` resolves it eagerly and ignores a `\.locale` override. A `String` *variable* passed to `Text` is not localized at all; model a known set of values as a type exposing `LocalizedStringResource`.
- **Pass localizable text around as `LocalizedStringResource`**, not `String`, so the comment/table/default travel with it:
  ```swift
  struct UserAction { let title: LocalizedStringResource }
  let action = UserAction(title: "Order items")
  ```

### 4.2 Comments are the highest-leverage habit
Translators see the string but **not the screen**. A one-line comment removes the ambiguity that produces wrong translations (a one-word label, anything with `%@`/`%lld`, a term of art).

```swift
Text("Explore", comment: "Title of the tab that navigates to the Explore screen.")
String(localized: "North America", comment: "The name of a continent.")
```
- **Describe placeholders by position** ("the first variable is finished items, the second is the total") — translators never see Swift variable names.
- Keep one source of truth per string: a comment at the call site *or* in the catalog's Comment field, not both.
- For a SwiftUI view that has no `comment:` initializer (e.g. `Label`), wrap an explicit `Text` to attach one.
- Xcode can **auto-generate comments** (Editor ▸ Settings ▸ "Automatically generate string catalog comments", or Control-click a key ▸ Generate Comment). Exported comments are marked "auto-generated" so reviewers can tell them from human-written ones. Treat auto-comments as a floor, not a substitute for context on tricky keys.

### 4.3 Plurals — never branch on count in code
Languages have different plural categories (English: one/other; Russian: one/few/many/other; Japanese: other only). Let the catalog handle it.

```swift
Text("\(count) items")   // interpolate, then Control-click the key ▸ "Vary by Plural"
```
- ❌ `if count == 1 { "1 item" } else { "\(count) items" }` — breaks in most languages.
- Xcode picks the specifier (`%lld`), adds the language's plural forms, and keeps them in sync as you add languages.

### 4.4 Don't assemble sentences from fragments
- **Localize whole sentences**, never concatenate clauses or `Text + Text` — word order varies by language.
- **Interpolate, don't `+`.** `Text("Error: " + message)` builds a `String`, which is not localized; `Text("Error: \(message)")` stays a localization key with a `%@` in the catalog.
- **Preserve every format specifier** (`%@`, `%lld`). For multi-argument strings use **positional specifiers** (`%1$@`, `%2$lld`) so translators can reorder arguments.
- Format **dates, numbers, currencies, names, lists, and measurements** with system formatters (`Date.FormatStyle`, `NumberFormatter`/`.formatted()`, `ListFormatter`, `MeasurementFormatter`) — never hand-build them. Number systems and separators are locale-specific.

### 4.5 Strings outside the main bundle (packages/frameworks)
Pass the bundle so extraction and lookup resolve to the right module:
```swift
String(localized: "Songs", bundle: #bundle)        // #bundle macro → the current target's bundle
```
- **Don't look up strings from bundles you don't own** — it can break automatic extraction.

### 4.6 Organize large catalogs into tables
```swift
Text("Explore", tableName: "Navigation")
String(localized: "Gorgeous peaks!", table: "LandmarkData")
```
Split into multiple `.xcstrings` when one grows unwieldy.

### 4.7 Don't impose English typography on other languages
- **Capitalization, plurals, and punctuation are per-language.** Title Case is English-only.
- **Put the case in the string, not in a modifier.** `.textCase(.uppercase)`, `.uppercased()`, `.localizedUppercase` and `.localizedCapitalized` on localized text force one casing on every translation. Write `"SECTION HEADER"` in the string instead. Text the person typed displays as-is. If a transform is unavoidable, use the `localized*` variants, which honor the locale (Turkish dotted I, German ß).
- **Budget for text expansion.** Translations run longer (*[Inference]* German often runs ~35% longer than English). Verify constrained layouts — buttons, fixed-width columns, toggle rows — don't truncate. Build flexible layouts *before* translating: no hard-coded text frames, `ViewThatFits` where a row may need to become a stack, text styles (`.body`) rather than `.system(size:)` so line height adapts to tall scripts, `.leading`/`.trailing` rather than `.left`/`.right`.
- **Vary by Device** when space or interaction differs ("Tap to learn more" on iOS vs "Click to learn more" on macOS) — Control-click the key ▸ Vary by Device.

### 4.8 Right-to-left (Arabic, Hebrew)
System frameworks mirror standard layouts automatically. When you customize:
- **Mirror layout & alignment** to reading direction — but **align a paragraph (3+ lines) to its own language**, not the surrounding context, and keep a **list's items uniformly aligned**.
- **Flip directional controls** (sliders, progress, back/next) and the glyphs that mark their start/end. **Don't flip** logos, universal marks (checkmark), real-world-object icons, or the **digits within a number** (`541`, phone numbers stay in order).
- **SF Symbols ship RTL variants** and Arabic/Hebrew localized forms; custom symbols can declare directionality. Prefer them — they streamline localization.
- Arabic/Hebrew next to all-caps Latin can look small; **bump the RTL font ~2 pt** to balance.

### 4.9 Per-locale, beyond text
- **Color carries culture-specific meaning** (e.g. white = purity *or* mourning depending on locale). If color communicates meaning, verify it communicates the *same* thing per locale.
- Adding a language requires registering the locale in the project (Xcode's Localizations list / `knownRegions`), not just filling in catalog values, or the app won't advertise it.

### 4.10 Test localizations
- Preview per language in Xcode Previews; run with a forced language (scheme arg `-AppleLanguages '(de)'`) and **pseudolanguages** (e.g. double-length, accented, RTL) to catch truncation and hard-coded order before translation exists.
- *[House]* **Get a native review** before shipping a locale. Agent translation is a **first draft** — review for tone, formality (です/ます vs. plain; du vs. Sie), and term consistency. Xcode's `translation` and `translation-coordinator` agent skills ship with per-locale style guides (ja and en among them); when they are loaded, the translation itself goes through them, and this guide judges the English source.

---

## Part 5 — Inclusive & accessible language

*[Apple · HIG Inclusion, Writing, Accessibility; Apple Style Guide, Writing inclusively]* Inclusive language is also easier to translate.

- **Plain, direct, respectful tone.** An academic or jokey tone excludes people; humor and idioms rarely survive translation.
- **Define technical terms** before using them, or avoid them. Plain language reads and translates better even for people who know the jargon.
- **Replace colloquialisms** — many are culture-bound or have exclusionary roots (e.g. "grandfathered in", "peanut gallery"). Say "preexisting"/"exempt" instead.
- **Avoid unnecessary gender.** Rewrite around gendered pronouns: ✅ "Subscribers can post recipes." ❌ "Each subscriber can post his or her recipes." This also keeps sentences clean when localized into gendered languages. For generic people, use **non-gendered** images/symbols (SF Symbols `person`, `figure.*`). Collect gender only if truly required, with inclusive options.
- **People-first language about disability;** never use a disability as a negative descriptor. Find out how a specific person/community self-identifies.
- **Don't bake in assumptions** (about family shape, affluence, shared cultural experiences). Security questions like "make of your first car" exclude anyone without that experience.
- **Support accessibility features** (VoiceOver, Dynamic Type, captions). Action-oriented labels (no "Click here") directly help screen-reader users. Write meaningful accessibility labels for icons/images.

---

## Anti-patterns → fixes (quick reference)

| ❌ Don't | ✅ Do | Why |
|---|---|---|
| "Click here" / "Let's do it!" | "Learn more about export" / "Send" | Verb-first, descriptive; screen-reader friendly |
| "Invalid name." | "Use only letters for your name." | Actionable, no blame |
| "Oops! Something went wrong." | "Unable to load. Check your connection and try again." | No insincere interjections; says what to do |
| "We're having trouble loading this." | "Unable to load content." | Avoid ambiguous "we" |
| Destructive action as the filled Primary button | Primary = safe action; Delete = red, non-default | People press prominent buttons unread |
| "OK" to confirm a deletion | "Delete" | Specific verb states the consequence |
| `if count == 1 { "1 item" }` | Catalog "Vary by Plural" | Most languages have >2 plural forms |
| `"Hi " + name + ", welcome!"` | `Text("Hi \(name), welcome!")` in a view; `String(localized:)` outside one | Word order varies; `+` yields an unlocalized `String` |
| `Text("Header").textCase(.uppercase)` | `Text("HEADER")` | Translators can't adjust a runtime case transform |
| `Text(NSLocalizedString("key", comment: ""))` | `Text("key", comment: "…")` | Wrapping resolves eagerly and ignores `\.locale` |
| Hard-coded `%@ %@` | `%1$@ %2$@` (positional) | Translators must reorder |
| Fixed-width button sized to English | Flexible layout, test +35% | Translations expand and truncate |
| Title Case forced onto German/Japanese | Per-language casing | Casing is an English convention |
| Alert at launch to announce news | Discoverable inline UI | Alerts interrupt; reserve for actionable/critical |

---

## Copy review checklist

Paste into a PR template; check before merging UI text.

- [ ] **Voice/tone** fit the surface (system = HIG clarity; conversion = honest benefit).
- [ ] **Buttons/CTAs** are verb-first; Title Case, alert buttons included.
- [ ] **≤ 2 prominent buttons** per view; destructive action is **not** the Primary button.
- [ ] **Alert titles** follow the sentence-vs-fragment punctuation rule; buttons are 1–2 words, "Cancel" titled exactly.
- [ ] **Errors** are close to the problem, blame-free, and say how to fix it. No "oops/uh-oh".
- [ ] **Empty states** guide to a next step (button when possible).
- [ ] **Settings labels** describe what ON does; deep-link instead of describing locations.
- [ ] **Fields** have labels + format hints; validation is inline and instructive.
- [ ] **No stray "we"**; possessives used sparingly and consistently; people addressed as "you".
- [ ] **Device-correct verbs** ("tap" vs "click").
- [ ] **Inclusive:** no unnecessary gender, undefined jargon, idioms, or assumptions.
- [ ] **Consistent** with the project term list / established patterns.

## Localization checklist

- [ ] Every user-facing string goes through a **localizable API** (`Text`, `String(localized:)`, `LocalizedStringResource`). No raw `String` in UI.
- [ ] **Comment** on every ambiguous key (one-word labels, format specifiers, terms of art); placeholders described by position.
- [ ] No runtime case transform (`.textCase`, `.uppercased()`) on localized text.
- [ ] **Plurals** via catalog "Vary by Plural" — zero `if count ==` branches.
- [ ] **No concatenation;** whole sentences only. **Positional** specifiers (`%1$@`) where there's more than one argument.
- [ ] Dates/numbers/currency/lists/measurements use **system formatters**.
- [ ] Package/framework strings pass **`#bundle`**.
- [ ] Layout tolerates **+35% text expansion** and **RTL** mirroring; nothing truncates.
- [ ] New locale **registered in the project** (knownRegions), not just catalog values.
- [ ] **Pseudolocalization + forced-language** run done; **native review** before shipping the locale.
- [ ] Color/imagery meaning verified per locale.

## CTA pattern library (copy-paste starters)

| Intent | Label |
|---|---|
| Start a flow | `Get Started` |
| Advance a flow | `Continue` · `Next` |
| Finish a flow | `Done` |
| Primary create/commit | `Save` · `Add to Cart` · `Send` |
| Destructive (general) | `Delete` (red, not Primary) |
| Destructive confirm (alert) | `Delete` · `Erase` · `Clear` |
| Cancel | `Cancel` (always this exact word) |
| Informational dismiss | `OK` (informational alerts only) |
| Opens another view (needs input) | `Export…` · `Edit…` (trailing ellipsis) |
| Async/slow action | `Checkout` → `Checking out…` (+ activity indicator) |
| Paywall / upsell | `Unlock Pro — $4.99` · `Start Free Trial` |
| Enable a disabled feature (empty state) | `Turn On <Feature>` |

---

## Sources (Apple official)

Human Interface Guidelines:
- **Writing** — https://developer.apple.com/design/human-interface-guidelines/writing *(change log: updated Dec 16, 2025 — possessive-pronoun + language-pattern guidance)*
- **Buttons** — https://developer.apple.com/design/human-interface-guidelines/buttons *(updated Dec 16, 2025 — Liquid Glass)*
- **Alerts** — https://developer.apple.com/design/human-interface-guidelines/alerts
- **Action sheets** — https://developer.apple.com/design/human-interface-guidelines/action-sheets
- **Onboarding** — https://developer.apple.com/design/human-interface-guidelines/onboarding
- **Entering data** — https://developer.apple.com/design/human-interface-guidelines/entering-data · **Text fields** — …/text-fields
- **Inclusion** — https://developer.apple.com/design/human-interface-guidelines/inclusion
- **Right to left** — https://developer.apple.com/design/human-interface-guidelines/right-to-left
- **Accessibility** — https://developer.apple.com/design/human-interface-guidelines/accessibility

Localization / developer docs:
- **Localization (overview)** — https://developer.apple.com/documentation/xcode/localization
- **Preparing your app's text for translation** — https://developer.apple.com/documentation/xcode/preparing-your-apps-text-for-translation
- **Localizing and varying text with a string catalog** — https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog
- **Preparing views for localization (SwiftUI)** — https://developer.apple.com/documentation/swiftui/preparing-views-for-localization
- **Expanding your app to new markets** — https://developer.apple.com/localization/
- **Apple Style Guide** (the canonical word-by-word reference, incl. *Writing inclusively*) — https://help.apple.com/applestyleguide/

Further reading (WWDC):
- *Craft clear names for features and labels* (WWDC25/26 290) · *Make a big impact with small writing changes* (WWDC25 404) · *Writing for interfaces* (WWDC22 10037)
- *Build multilingual-ready apps* (WWDC24 10185) · *Code-along: Explore localization with Xcode* (WWDC25 225) · *Discover String Catalogs* (WWDC23 10155) · *Design for Arabic* (WWDC22 10034)

Apple agent skills (Xcode 27.2; `xcrun agent plugin path --plugin-format claude` prints their folder):
- **swiftui-specialist** — `references/localization.md`: string catalogs, `#bundle`, interpolation vs concatenation, casing, formatting, layout, translator comments.
- **translation**, **translation-coordinator** — catalog translation through Xcode's String Catalog tools, with per-locale style guides readable on disk.

> Apple revises HIG pages periodically. The verification date at the top says when this summary last matched them; the page's change log says whether it still does.
