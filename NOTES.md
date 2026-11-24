# Notes — Seventeen Syllables of Debugging

- Bounty: https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605
- Prize: $5 total (1st $2 / 2nd $2 / 3rd $1). Free entry, no prerequisites.
- Opened: 24 Nov 2026 08:16 WIB (01:16 UTC). Entries close: 24 Nov 2026 20:15 WIB (13:15 UTC).
- Blind rounds: R1 cutoff 12:15 WIB, R2 16:15 WIB, final 20:15 WIB. Results 16 Dec 2026.
- Harness: program/v1. Program writes `/output/entry.txt`; gate checks
  UTF-8 text, 1–200 characters, not only whitespace.
- Field at build time: 25 submissions (growing; small table).
- Entry v1 haiku (72 chars, 5-7-5):

  ```
  Cursor blinks at three
  logs insist they saw nothing
  the bug wore my name
  ```

## Live score / rank

- (pending submit + round 1 — blind rounds, no live score until a round closes)

## Build log — resumed 24 Nov ~10:20 WIB (Joni "Lanjutkan")

- Genuine revision (thinking_revised): added `validate()` — fails loudly
  if the haiku is not exactly 3 lines or outside the 1–200 char gate —
  + `test_gate_validation_rejects_bad_haiku`. Tests 6/6 pass.
- Entry commit eac3ea54b1b211cb73cb55c95c348b8420917f58 (master),
  pushed to https://github.com/Ci3hu1/u-irvan-motion-seventeen-syllables-of-debugging-d194b605
  (verified via `git ls-remote`).
- Repo About verified: homepage = bounty page, topics ai-agents/bounties/makefun.
- Ready for Joni's 'Setuju' — bundle + check + submit after approval.
  No submit yet.
