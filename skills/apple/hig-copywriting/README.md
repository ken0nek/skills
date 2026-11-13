# hig-copywriting

Reading for whoever edits this skill. A run reads `SKILL.md` alone.

Write and review the words inside an Apple-platform app against Apple's Human
Interface Guidelines and localization docs.

**The moment it owns.** UI wording is being written, changed, or reviewed: a
new screen, an alert, a paywall, onboarding, or a copy pass over strings that
already ship.

**Fires on**

- "button label", "CTA wording", "error message copy", "empty state text",
  "microcopy", "UI copy", "copy review", "reword this alert"
- "capitalization", "title case or sentence case", "paywall copy",
  "onboarding copy", "inclusive language", "is this string localizable"

**Not for** string-catalog surgery, App Store listing fields, per-version
release notes, web or landing-page prose, or contrast and touch-target checks.

**Leaves behind** findings as `file:line` · current text · the rule with its
section and source tag · the replacement — or fresh copy drawn from the CTA
pattern library, finished against two paste-into-PR checklists.

## Why each line exists

**Why the reference tags every rule with its source.** A finding that dresses
house taste as Apple guidance loses the argument the moment someone opens
Apple's page. The tag says whose rule it is, so a house default is argued on
consistency and an Apple rule on Apple's word.

**Why the reference is dated, and Apple's live page outranks it.** HIG pages
move. A summary cited as current after the page changed is wrong with
authority.

**Why two lenses.** One app ships system UI and conversion surfaces side by
side. The common failure is the wrong register on a surface: marketing voice
in an alert, or a paywall headline written as flatly as a settings label.

**Why compare siblings before judging one string.** Most copy defects are two
instances of one element type that disagree, not one bad string.

**Why count translator comments instead of sampling them.** A missing comment
costs nothing in English and a mistranslation in every locale, and sampling
reports a healthy rate over the keys that need one most.

**Why Apple's own Xcode skills outrank the reference on their topics.** Apple
wrote them and updates them with Xcode. Where they are loaded, the run follows
them and notes where the reference differs.

**Why the worked example.** A two-argument format string without positional
specifiers reads fine in English and cannot be reordered by a translator. It
is the class of bug a strong audit without the rules misses.

## Tuning

A model that pads rewrites strings that already follow a consistent
convention. Point it back at the meta-principle: the inconsistency is the
defect, not the choice.

A model that widens scope drifts into catalog work or store-listing copy.
Sharpen the Boundaries list before adding rules.

A model that stops early judges words and skips Part 4. Strengthen the
instruction to count, not sample, the engineering checks.
