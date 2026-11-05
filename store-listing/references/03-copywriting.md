# 03 — Copywriting

Write from the claims ledger, never from the feature wish-list. Each field below has a job, a length target, and failure modes.

## 1. Principles

1. **Position in one sentence** before any field: "For [audience] who [situation], [Brand] is the [category] that [differentiator] unlike [alternative]." The sentence decides what every headline leads with.
2. **Lead with the user's problem and outcome**, then how it works. Features appear as proof.
3. **Specific beats superlative.** "See price, bills and move-in date on every card" outranks "the best way to find a room". Superlatives are banned in several fields anyway (`08-compliance-guardrails.md`).
4. **One idea per line.** Mobile users skim: short paragraphs, line breaks, a handful of bullets.
5. **Honest scope.** If a claim needs an asterisk, the claim is too big. Region, hardware and subscription requirements are stated where the claim is made (Apple 2.3.2).
6. **Respect positioning rules.** Projects often ban words (a housing app avoiding dating vocabulary; a fitness app avoiding medical claims). Load the banned/required terms in Step 1 and lint them. A negated mention ("not a dating app") still plants the word; prefer a positive formulation unless the owner's rule allows it.

## 2. Field recipes

### Apple

| Field | Job | Target | Pattern |
|---|---|---|---|
| Name | Recognition + one core term | ≤ 30 | `Brand: core term` or `Brand – core term`; no prices, claims, emojis |
| Subtitle | The value statement | ≤ 30 | benefit + audience, verb-led or noun phrase; complements the name |
| Promotional text | What is current | ≤ 170 | One hook + current news; editable any time, so seasonal copy and launches live here; not indexed |
| Description | Convert the reader who tapped "more" | 1500–3000 | Hook (first two lines are visible before the fold, T) → how it works (3 short steps) → for-whom blocks → trust (safety, privacy, price) → links. Plain text only |
| Keywords | Indexed terms | ≤ 100 | `02-keyword-research.md` §5 |
| What's New | Update notes | see `05-release-notes.md` | |

### Google Play

| Field | Job | Target | Pattern |
|---|---|---|---|
| Title | Recognition + one core term | ≤ 30 | `Brand: descriptor`; no "Free", "No ads", emojis, ALL CAPS |
| Short description | The one-line pitch (shown before expanding) | ≤ 80 | One benefit sentence, one primary term, no CTA, no emojis |
| Full description | Convert and inform | 1500–3000 | Hook → how it works → for-whom → trust → links. Do not repeat the short description; no testimonials; no keyword lists |
| Release notes | What changed | ≤ 500 | `05-release-notes.md` |

## 3. Description skeleton (both stores)

```
[Hook: the problem or desire, 1–2 lines]
[Outcome line: what changes for the user]

HOW IT WORKS
1. [Step]
2. [Step]
3. [Step]

FOR [AUDIENCE A]
• [Benefit]
• [Benefit]
• [Benefit]

FOR [AUDIENCE B]
• …

[TRUST BLOCK — safety, privacy, moderation, who it's for]
• [Verifiable facts only]

[PRICE: "Free" only if the ledger confirms no purchase, subscription or ads]

Privacy Policy: https://…
Terms: https://…
Support: https://…
```

- Section headings in capitals are common on Apple; Play's Metadata policy targets ALL CAPS in the *title, icon and developer name* (V), but avoid shouting in the short description. Use title case or sentence case on Play if in doubt.
- Bullets: use "•" (renders on both stores). No HTML (Apple plain text; Play supports limited tags, T, skip them).
- Links: Apple descriptions do not make links tappable except URLs (T); keep them last.

## 4. Social proof and trust

| Allowed | Not allowed |
|---|---|
| Verifiable facts: "reviewed by a person before publishing", "no ads" (if true) | Unattributed testimonials (Play, V) |
| Awards you actually hold, in the description (not the icon/title) | "Best of Play 20XX", "#1", "App of the year" in title/icon (Play, V); unverifiable superlatives (Apple 2.3.7) |
| Named, attributed quotes with permission | Fake ratings, press quotes, "million downloads" claims in short description (Play, V) |

## 5. Safety, minors and sensitive domains

- Say who the product is for ("18+") when the product enforces it; do not claim protections that are not shipped.
- Safety claims need ledger evidence (moderation process, response times). Dated promises ("reports read within 24 hours") need an owner who will keep them true.
- Health, finance and legal claims: state what the product is and is not; add the required disclaimers (Apple 1.4.1 etc.).
- Never use "For Kids"/"For Children" outside the Kids Category (Apple 2.3.8).

## 6. Style guide checks

- Tone: consistent person (tu/Lei in Italian; you in English). Consumer apps usually use informal address in Italian.
- Terminology: one name per concept across store, app UI and website.
- Typography: straight vs curly quotes consistently; no decorative symbols in name/subtitle/title; apostrophes in Italian (`l'app`) typed consistently.
- Inclusive language: prefer neutral phrasings over generic masculine plurals when natural (e.g. "chi cerca una stanza").
- Accessibility: plain words; avoid emoji clusters (screen readers read them aloud).
- Numbers: only those in the ledger; prices and limits with currency and period.

## 7. Revision checklist (use before lint)

- [ ] Every sentence maps to a ledger row.
- [ ] The first two lines of each description can stand alone.
- [ ] No banned or competitor terms; no other-platform mentions (Apple 2.3.10).
- [ ] No claim contradicts the privacy label / Data safety (e.g. "no data collected" with analytics).
- [ ] Price statement matches billing reality (free vs IAP vs subscription; Apple 2.3.2).
- [ ] Locale versions say the same true things (not necessarily the same words).
- [ ] Links resolve (support, privacy, terms).
