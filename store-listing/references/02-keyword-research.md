# 02 — Keyword research and field allocation

Goal: choose the words people use to find this product, and place each in the field where it earns the most. Practice rows are **T** unless marked; store facts cite `01-field-specs.md`.

## 1. What the stores say (V)

- **Apple** search relevance uses text matches in **name, subtitle, keywords and primary category** (and the optional secondary category), plus behaviour (downloads, ratings, reviews). Promotional text does not affect ranking; descriptions are not documented as indexed. Do not repeat a word across name, subtitle, keywords or category.
- **Google Play** pages do not state which fields are indexed. The Play listing guidance warns against keyword lists and repetition; unnecessary keywords "will not impact ranking" and hurt readability. Write for people, keep the main term natural in title, short and full description.

## 2. Inputs (use what the user has; never invent numbers)

| Source | Gives | Where |
|---|---|---|
| Product truth | What the product really does (claims ledger) | repo, README, spec |
| Users' words | Phrases customers use, complaints, jobs-to-be-done | reviews, support tickets, interviews, landing-page survey answers |
| Store autocomplete | Phrases people type | App Store / Play search box, typed by the user and pasted |
| Competitor listings | Terms rivals use in name, subtitle, short description | public store pages the user names |
| Apple Search Ads (keyword suggestions, popularity) | Relative search popularity | user's Apple Search Ads account |
| App Store Connect Analytics | Search impressions → page views → downloads by source | user's console |
| Play Console search terms (Store listing acquisition) | Queries leading to the listing | user's console |
| Third-party ASO tools | Volume, difficulty, rank | user's subscription |

If no volume source exists, say so in the worksheet: volume column **unknown**; ranking of candidates is by relevance and specificity, and the report recommends validating with Search Ads popularity or Analytics after launch.

## 3. Candidate generation

1. **Seeds** — nouns and verbs from the claims ledger: what it is, what it does, who it's for, where.
2. **Expand** — synonyms, regional variants, spoken vs written forms, compound forms, common misspellings (Apple tolerates some; do not spend characters on them), category words, adjacent intents ("room" → "flatmate", "roommate", "shared flat").
3. **Localize** — generate in each target language from user intent, not from translation (`06-localization-it-en.md`).
4. **Prune** — remove terms the product does not satisfy (relevance gate), brand names of others (2.3.7), generic filler ("app", "best"), and any term on the project's banned list.

## 4. Scoring (qualitative unless data is supplied)

| Criterion | Question | Score 0–2 |
|---|---|---|
| Relevance | Does the product fully satisfy someone typing it? | 0 = partly, 2 = exactly |
| Specificity | Is the intent narrow enough to convert? | 0 = broad head term |
| Competition proxy | How many strong apps already own it in name/subtitle? | 0 = crowded |
| Volume | From supplied data | unknown / 0–2 |
| Fit | Reads naturally in the copy | 0–2 |

Prefer **long-tail, high-relevance** phrases for a new app; head terms in the name only when the brand can carry them.

## 5. Field allocation — Apple

Budget: name 30 + subtitle 30 + keywords 100 = 160 indexed characters per locale, plus category.

1. **Name** — brand first, plus at most one descriptor with the single most valuable term ("Brand: descriptor"). The name is the strongest field and also the one users read.
2. **Subtitle** — a different high-value phrase set; reads as a value statement; complements the name (never repeats a name word).
3. **Keywords** — everything else, packed:
   - separate with commas, **no spaces** after commas;
   - **no repeats** of any word in name, subtitle or category (the lint flags exact and plural/singular repeats);
   - singular only, unless the plural is the dominant search form; Apple matches simple variants for several languages (T), so test with Search Ads popularity before spending characters on both;
   - drop "app", "game", filler words, punctuation, trademarks of others;
   - multi-word phrases can be built from single words across fields (Apple combines terms from name, subtitle and keywords, T): `rent` in the name and `room` in the subtitle already cover "room rent";
   - leave a few characters of headroom for the bytes limit when using accents.
4. **Category** — choose the primary by the dominant intent; the secondary adds indexed terms (V).
5. **Check** — `python3 scripts/lint-listing.py listing.md` reports wasted space and over-limit fields.

Worked pattern (generic): name `Brand: core term`, subtitle `benefit + audience`, keywords `synonym1,synonym2,adjacent1,adjacent2,…` with zero overlap.

## 6. Field allocation — Google Play

- **Title (30)**: brand + one natural descriptor. No "free", "no ads", emojis, ALL CAPS, rankings (V).
- **Short description (80)**: one benefit sentence containing the primary term once; no CTA, no superlatives, no emojis (V).
- **Full description (4000)**: the primary term in the first sentence and naturally across sections; no keyword lists, no repetition of the short description, no testimonials (V). Keyword density is not a lever; readability and conversion are.
- Treat any "Play ranks X" statement as **T**.

## 7. Per-locale rules

- Run the process per locale; a term good in Italian is not a translation of the English one.
- Apple indexes **per localization** (V\*): a missing localization is lost indexed space; adding an English (U.S.) localization to an Italian-primary app is a common way to cover English queries (T).
- Do not copy keyword sets across locales without checking intent.

## 8. Maintenance loop

After release, with the user's data: compare impressions by source, queries, conversion; replace the weakest 20–30% of keywords each cycle; keep a changelog of keyword sets (the worksheet's history table). Apple keyword changes ship with a version; Play text changes go live via console (experiments for descriptions per localized listing, `07-experiments.md`).

## 9. Anti-patterns

| Pattern | Why it fails |
|---|---|
| Competitor names and trademarks in keywords | Rejection risk (2.3.7); misleading intent |
| Repeating name words in the keyword field | Wasted indexed characters |
| Spaces after commas | Each space burns a character |
| Plural + singular of the same word | Two slots for one query (T) |
| Stuffing the description with keyword repeats | No Apple ranking benefit (not indexed), Play keyword-spam risk (V) |
| Writing for volume you cannot show | Irrelevant traffic, low conversion, rating damage |
| Putting price/promo/ranking claims in name/subtitle/title | Policy violation (Apple 2.3.7, Play Metadata) |
