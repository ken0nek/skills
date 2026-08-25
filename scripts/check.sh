#!/bin/sh
# The repo's one mechanical check. Everything else is verified by reading.
#
# 1. Every verbatim embed of the decision policy matches POLICY.md
#    byte-for-byte: README.md, generate-plan, and the execution-prompt
#    template. The decisions/ skills carry a compression no diff can check.
# 2. Every SKILL.md frontmatter stays inside the Agent Skills bounds: name
#    matches its directory, description is one line within 1024 characters,
#    a license is declared, README.md (with a `## Tuning` section) sits
#    beside it, the README index lists it, and nothing meant for whoever
#    edits rides along on every fire.
# 3. Every SKILL.md frontmatter parses as flat YAML. Descriptions are
#    unquoted plain scalars on purpose, so naive regex parsers read them;
#    the price is that a `: ` inside one turns the file into a nested
#    mapping the installer silently skips. Rephrase, never quote.
# 4. Every relative link in a shipped skill file resolves inside that
#    skill's own directory — a single-skill install copies nothing else.
#
# harvest-run's `disable-model-invocation` is a Claude Code field outside
# the Agent Skills spec, kept because the skill deletes a directory.
#
# Needs nothing beyond a POSIX shell and its usual utilities.

set -u
cd "$(dirname "$0")/.." || exit 1
fail=0
tmp=$(mktemp -d) || exit 1
trap 'rm -rf "$tmp"' EXIT

fence() { # extract the ```text block of $1
  awk '/^```text$/{f=1;next} /^```$/{f=0} f' "$1"
}

fence POLICY.md >"$tmp/canon"
[ -s "$tmp/canon" ] || { echo "FAIL: POLICY.md has no \`\`\`text policy block"; exit 1; }

check_embed() { # $1 label, $2 file holding the extracted embed
  if diff -u "$tmp/canon" "$2" >/dev/null; then
    echo "ok: $1 embeds the policy verbatim"
  else
    echo "FAIL: $1 drifted from POLICY.md —"
    diff -u "$tmp/canon" "$2" | head -20
    fail=1
  fi
}

fence README.md >"$tmp/readme"
check_embed "README.md" "$tmp/readme"

fence skills/run-lifecycle/generate-plan/SKILL.md >"$tmp/plan"
check_embed "generate-plan" "$tmp/plan"

# The execution-prompt template embeds the policy unfenced, inside its own
# ```text fence, so cut the span by the canon's first and last lines instead.
awk -v first="$(head -n 1 "$tmp/canon")" -v last="$(tail -n 1 "$tmp/canon")" \
  '$0==first{f=1} f; $0==last{f=0}' \
  skills/run-lifecycle/generate-execution-prompt/SKILL.md >"$tmp/prompt"
check_embed "generate-execution-prompt (template)" "$tmp/prompt"

plain_yaml() { # $1 SKILL.md — frontmatter must parse as a flat YAML mapping
  awk -v f="$1" '
    NR==1 { if ($0 != "---") { printf "FAIL: %s does not open with a --- frontmatter line\n", f; bad=1; exit } ; next }
    /^---$/ { closed=1; exit }
    {
      if ($0 !~ /^[A-Za-z][A-Za-z0-9_-]*:/) {
        printf "FAIL: %s line %d is not a `key: value` mapping\n", f, NR; bad=1; next
      }
      p = index($0, ": ")
      if (p == 0) { printf "FAIL: %s line %d declares a key with no value\n", f, NR; bad=1; next }
      key = substr($0, 1, p - 1)
      val = substr($0, p + 2)
      q = substr(val, 1, 1)
      if (q == "\"" || q == "\047") next   # a quoted scalar; YAML quoting rules apply, not these
      if (index(val, ": ")) {
        printf "FAIL: %s %s holds \": \" — YAML reads a colon-space inside a plain scalar as a nested mapping, so the file does not parse. Rephrase the prose; do not add quotes.\n", f, key; bad=1
      }
      if (substr(val, length(val), 1) == ":") {
        printf "FAIL: %s %s ends in \":\" — a plain scalar cannot. Rephrase.\n", f, key; bad=1
      }
      if (index(val, " #")) {
        printf "FAIL: %s %s holds \" #\" — YAML reads the rest of the line as a comment. Rephrase.\n", f, key; bad=1
      }
      if (index("-?:,[]{}#&*!|>%@`", q)) {
        printf "FAIL: %s %s opens with \"%s\", which YAML reads as an indicator, not as text. Rephrase.\n", f, key, q; bad=1
      }
    }
    END {
      if (!closed && !bad) { printf "FAIL: %s frontmatter is never closed by ---\n", f; bad=1 }
      exit bad
    }
  ' "$1"
}

for skill in skills/*/*/SKILL.md; do
  dir=$(basename "$(dirname "$skill")")
  plain_yaml "$skill" || fail=1
  name=$(awk -F': ' '$1=="name"{print $2; exit}' "$skill")
  desc=$(awk '$1=="description:"{print substr($0, index($0,": ")+2); exit}' "$skill")
  [ "$name" = "$dir" ] || { echo "FAIL: $skill name '$name' != directory '$dir'"; fail=1; }
  [ -n "$desc" ] || { echo "FAIL: $skill has no single-line description"; fail=1; }
  [ "${#desc}" -le 1024 ] || { echo "FAIL: $skill description over 1024 chars (${#desc})"; fail=1; }
  grep -q '^license:' "$skill" || { echo "FAIL: $skill declares no license"; fail=1; }
  [ -f "$(dirname "$skill")/README.md" ] || { echo "FAIL: $skill ships no README.md beside it — the folder renders as a bare file listing"; fail=1; }
  grep -q '^Editing this skill' "$skill" && { echo "FAIL: $skill carries the maintainer footer — that pointer belongs in README.md, which no run pays for"; fail=1; }
  readme="$(dirname "$skill")/README.md"
  grep -q '^## Tuning' "$readme" 2>/dev/null || { echo "FAIL: $readme carries no '## Tuning' section — tuning lives there, beside why each line exists"; fail=1; }
  [ -e "$(dirname "$skill")/references/rationale.md" ] && { echo "FAIL: $(dirname "$skill")/references/rationale.md exists — its content belongs in README.md, which states that a run reads SKILL.md alone"; fail=1; }
  grep -q "$name" README.md || { echo "FAIL: $name is shipped but missing from the README index"; fail=1; }
done
[ "$fail" -eq 0 ] && echo "ok: frontmatter within Agent Skills bounds"

# Collapse `.` and `..` textually. No realpath: the targets need not exist,
# and a missing one must be reported as missing, not as a resolver error.
norm() {
  printf '%s\n' "$1" | awk -F/ '{
    n = 0
    for (i = 1; i <= NF; i++) {
      if ($i == "..") { if (n > 0) n--; else n = -999 }
      else if ($i != "." && $i != "") s[++n] = $i
    }
    if (n < 0) { print "/ESCAPED"; exit }
    out = ""
    for (i = 1; i <= n; i++) out = out (i > 1 ? "/" : "") s[i]
    print out
  }'
}

linkfail=0
for md in skills/*/*/SKILL.md skills/*/*/README.md skills/*/*/references/*.md; do
  [ -f "$md" ] || continue
  root=$(printf '%s\n' "$md" | awk -F/ '{print $1"/"$2"/"$3}')
  dir=$(dirname "$md")
  awk '{
    s = $0
    while (match(s, /\]\([^)]*\)/)) {
      print substr(s, RSTART + 2, RLENGTH - 3)
      s = substr(s, RSTART + RLENGTH)
    }
  }' "$md" | while IFS= read -r link; do
    case "$link" in
      \#*) continue ;;                # an in-file anchor stays in the file
      *://* | mailto:*) continue ;;   # an external URL is the sanctioned way out
    esac
    target=${link%%#*}
    [ -n "$target" ] || continue
    case "$target" in
      /*) echo "FAIL: $md links '$link' by absolute path — a single-skill install has no repo root"; echo x >>"$tmp/linkfail"; continue ;;
    esac
    res=$(norm "$dir/$target")
    case "$res" in
      "$root"/*) ;;
      *) echo "FAIL: $md links '$link', which resolves outside $root/ — that directory is all a single-skill install copies"; echo x >>"$tmp/linkfail"; continue ;;
    esac
    [ -e "$res" ] || { echo "FAIL: $md links '$link' — no such file"; echo x >>"$tmp/linkfail"; }
  done
done
[ -s "$tmp/linkfail" ] && { linkfail=1; fail=1; }
[ "$linkfail" -eq 0 ] && echo "ok: every skill link resolves inside its own skill directory"

exit "$fail"
