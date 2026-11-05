# 06 — Localization: Italian and English

Localize by intent, not by translation. Italian runs about 15–25% longer than English, so character budgets bite earlier. Store facts: `01-field-specs.md` §2; the rest is practice (**T**).

## 1. Locale strategy

| Decision | Recommendation |
|---|---|
| Primary language (Apple) | The language of the home market (Italian for an Italy-first product). Apple falls back to the primary language wherever a locale has no metadata (V\*) |
| Add English | Add **English (U.S.)** so English-speaking storefronts and devices do not show Italian; add U.K./Australia/Canada only when the copy differs (spelling, terms) or the market matters |
| Play default language | **en-US** by default (V); set the default to the language the full listing is written in first, then add `it-IT` via Manage translations |
| Machine translation on Play | Available for it-IT (V), not human-reviewed: use it only to create a draft, then edit |
| Graphics | Localize screenshots and the feature graphic per language; text translations alone keep default-language graphics (V) |
| Metadata parity | Both stores' descriptions may be identical text, but each store's rules differ (`08-compliance-guardrails.md`); lint both |

## 2. Italian

### Keywords and search
- Italian users search with nouns and short phrases: "affitto stanza", "coinquilini", "posto letto". Check singular/plural dominance before spending characters on both forms.
- Accents (à è é ì ò ù): Apple search tolerates missing accents in practice (T); avoid spending bytes (UTF-8) on accented variants when an unaccented spelling is common.
- Regional vocabulary matters (Nord/Sud, "fuorisede", "studenti"): include terms the audience uses, not only the standard word.
- English borrowings users really type ("coworking", "app") may help in Italian copy but do not put "app" in Apple keywords.

### Copy
- Tone: informal "tu" is standard for consumer apps; "Lei" for banking, health, public services.
- Short sentences; avoid chains of subordinate clauses in the first two description lines.
- Use gender-neutral formulations where natural ("chi cerca una stanza", "chi vive in casa") instead of generic masculine plurals; keep search terms (e.g. "coinquilini") where they carry the query.
- Prices and units: `€ 450 al mese` or `450 €/mese` consistently; use Italian date formats `1 marzo`.
- Capitalisation: Italian headings use sentence case; ALL CAPS section headings in descriptions are legible but avoid them on Play short description/title (V policy targets title/icon/developer name).
- Legal wording: privacy and terms URLs should point to Italian pages for the Italian listing (Apple 5.1.1(i)); consumer-protection language about "gratis" must match billing reality.
- Punctuation: pick curly or straight apostrophes and keep them consistent in all fields; avoid ellipsis characters in names.

## 3. English

| Variant | When | Differences |
|---|---|---|
| **en-US** | Default English; also the safe fallback | US spelling (color, flat→apartment) |
| **en-GB** | UK audience matters | UK spelling and vocabulary (flat, flatmate, tenancy, "let") |
| **en-AU / en-CA** | Only if the product launches there | Local terms; otherwise skip |

- If the product is Italy-first, English copy should be clear to non-native readers: avoid idioms, short words, concrete nouns.
- Use the term your English audience searches ("flatmate" UK, "roommate" US).
- Check that English keywords are not duplicates of name/subtitle words (lint).

## 4. Codes and folders

| Context | Italian | English (US) | English (UK) |
|---|---|---|---|
| App Store Connect UI | Italian | English (U.S.) | English (U.K.) |
| fastlane `deliver` folder | `it` | `en-US` | `en-GB` |
| fastlane `supply` folder | `it-IT` | `en-US` | `en-GB` |
| Play release-notes tag | `<it-IT>` | `<en-US>` | `<en-GB>` |
| Play Console | Italiano – it-IT | English – en-US | English – en-GB |
| Listing file heading in `listing.md` | `### Italian` | `### English` | `### English (UK)` |

(Folder codes **T**; confirm against the installed fastlane version.)

## 5. Process per locale

1. Write the **brief** for the locale: audience, search phrases, tone, words to avoid, local competitors.
2. Draft natively from the claims ledger; do not translate the other locale's copy.
3. Back-check meaning: every claim in one locale appears in the other (or is intentionally absent).
4. Fit budgets: lint reports characters per field; when Italian overflows, cut adjectives before cutting the benefit.
5. Review by a native speaker for tone and search terms when the user can.

## 6. Quality checks

- [ ] No leftover other-language words, placeholder tokens, or untranslated UI references.
- [ ] Screenshots, captions and in-app language agree.
- [ ] Both locales respect the project's banned terms.
- [ ] Support/privacy/terms links exist in the same language when available.
- [ ] Release notes per locale have the same facts.
