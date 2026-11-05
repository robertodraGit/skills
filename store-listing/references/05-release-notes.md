# 05 — Release notes from a changelog

Developer changelogs (conventional commits, release-please, GitHub releases) are not release notes. Users read two to five lines about what they can now do or what stopped breaking.

## 1. Store rules

| | Apple "What's New" | Google Play "Release notes" |
|---|---|---|
| Limit | 4000 characters (V\*) | **500 characters per language** (V) |
| Per locale | Yes (localizable, V\*) | Yes, with language tags (V) |
| First version | Not available/required (V\*) | Required if you ship notes |
| Required | For every update (V\*) | Optional but expected |
| Content | New features and product changes; generic text allowed only for bug fixes, security updates, performance improvements (Apple 2.3.12, V) | No promotion or calls to action (V) |
| Format | Plain text | `<it-IT>text</it-IT>` tags each on their own line; add translations before adding notes (V) |
| Editable | With the version | Per release; "copy from previous release" copies notes and translations (V) |

TestFlight "What to Test" and Firebase distribution notes are tester-facing, separate from store notes.

## 2. Procedure

1. **Locate the range.** Last released tag/version → current. Check changelog freshness: if the changelog's latest version is older than `package.json`/app version or the newest tag, ignore it and use git: `git log --no-merges --pretty='%s' <last-tag>..HEAD`. Say which source was used.
2. **Draft raw material.**
   `python3 scripts/changelog-to-notes.py --changelog CHANGELOG.md --version X.Y.Z` or `--git <last-tag>..HEAD`.
   It groups conventional commits into user-facing candidates (`feat`, `fix`, `perf`) and internal items (`chore`, `docs`, `refactor`, `test`, `ci`, `build`).
3. **Filter by visibility.** Keep a change only if a user can see or feel it. Drop refactors, dependency bumps, tests, CI, docs, internal tooling, landing-site/web-only work when the notes are for the app.
4. **Translate to user language.** Subject-verb-benefit, past or present tense consistently, no ticket ids, commit scopes, or jargon (see §3).
5. **Merge and order.** One line per user-visible change; most valuable first; merge near-duplicates ("fixes" in the same area).
6. **Fit.** Apple: 1–6 bullets is plenty. Play: ≤ 500 characters per language, so 2–4 bullets.
7. **Localize** natively (IT/EN rules in `06-localization-it-en.md`).
8. **Verify against the diff**: every bullet corresponds to a shipped change; nothing promised for later; nothing that is feature-flagged off.
9. **Lint**: `python3 scripts/lint-listing.py listing.md` (What's New / Release notes fields).

## 3. Conversion table: developer → user language

| Commit/changelog line | Release note |
|---|---|
| `feat(cards): bios and room descriptions reach the cards` | Now you can read people's bios and room descriptions right on the cards. |
| `fix(onboarding): never ask a Sign in with Apple user for their name` | Signing in with Apple is quicker: we no longer ask for your name again. |
| `fix(ios): App Review 3.5.0 — Apple name reuse and camera purpose string` | _(Internal review fix; fold into "Improvements to sign-in and camera permission text" only if user-visible.)_ |
| `refactor(swipe): one deck module` | _omit_ |
| `perf(feed): lazy-load images` | The feed loads faster. |
| `chore(deps): bump expo` | _omit_ (or "Stability improvements" if nothing else) |
| `docs: …`, `test: …`, `ci: …` | _omit_ |

If nothing user-visible shipped, write a truthful generic line: "Bug fixes and stability improvements." (Apple allows it only for bug fixes, security and performance; Play: keep it plain.)

## 4. Templates

**Apple, Italian**
```
Novità
• Ora puoi leggere bio e descrizione della stanza direttamente sulle schede.
• Accedere con Apple è più rapido: non ti chiediamo più il nome.
• Correzioni e miglioramenti di stabilità.
```

**Apple, English**
```
What's new
• You can now read bios and room descriptions right on the cards.
• Signing in with Apple is quicker: we no longer ask for your name.
• Fixes and stability improvements.
```

**Play (both languages in one field)**
```
<it-IT>
• Bio e descrizione della stanza ora sulle schede.
• Accesso con Apple più rapido.
• Correzioni di stabilità.
</it-IT>
<en-US>
• Bios and room descriptions now appear on the cards.
• Faster Sign in with Apple.
• Stability fixes.
</en-US>
```

## 5. Style

- Start with the benefit or the thing the user can do; avoid "We have updated".
- Same verbs for the same features across versions.
- No promotion, discounts, calls to action on Play; no "rate us" requests (also Apple 5.6.1/3.2.2(x) context).
- No version numbers in the body (the store shows them).
- Honest: never describe a fix you did not ship; never imply security issues beyond what you disclose.
- Length targets: Apple ≤ 400 characters in practice (T); Play ≤ 500 hard.

## 6. Repository wiring

| Tool | Where notes live |
|---|---|
| fastlane `deliver` | `fastlane/metadata/<locale>/release_notes.txt` (T) |
| fastlane `supply` | `fastlane/metadata/android/<locale>/changelogs/<versionCode>.txt` (T) |
| EAS Submit | notes are entered in the console; EAS does not set store release notes |
| release-please | `CHANGELOG.md` is developer-facing; keep a separate user-facing source (`docs/store/release-notes/<version>.md`) |

Placeholder files such as a one-line "beta build" note must not be the file shipped as store notes (Apple 2.3.12, 2.1(a) placeholder text); flag them.
