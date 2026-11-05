# 07 — Experiments and variants

Use after launch, with the user's traffic. Never promise uplift.

## 1. Tools and limits

| Tool | What can differ | Limits | Conf |
|---|---|---|---|
| **Apple product page optimization (PPO)** | App icon, screenshots, app previews | up to 3 treatments vs the original; test name ≤ 64 characters; up to 90 days; one test at a time; cannot edit once started; you choose the traffic share; localized treatments possible; icon treatments need all icon variants in the binary and an app update; not available for custom product pages | V |
| **Apple custom product pages (CPP)** | Screenshots, previews, promotional text (keywords per locale per help page) | up to 70 per app; own URL; own analytics; reviewed separately from an app update; deep link on iOS/iPadOS 18+ | V / V\* |
| **Google Play store listing experiments** | Default graphics (icon, feature graphic, screenshots) or localized listings in up to five languages (adds descriptions) | one default-graphics experiment or up to five localized at once; up to 2 variants vs current; name ≤ 50; stops after 6 months; metrics: unique install clicks, open clicks, pre-registration clicks | V |
| **Google custom store listings** | Name, icon, descriptions, graphics | up to 50; privacy policy, category, contact shared; one custom listing per country; URL `…&listing=<param>`; audiences (lapsed, buyers, ads traffic, search keywords, …); not auto-translated | V |

## 2. What to test first (impact order, T)

1. **Screenshot 1–3**: message and order (they appear in search on Apple).
2. **Icon** (high traffic apps).
3. **Feature graphic / preview video** (Play).
4. **Short description** (Play localized experiment) and **subtitle/promotional text** (via CPP/versions on Apple).
5. Descriptions rarely move conversion; test last.

## 3. Hypothesis template

```
Because [evidence: analytics/reviews/support],
we believe changing [one variable] for [locale/store]
will [metric] for [audience].
Success: [metric] difference of ≥ [threshold the owner sets] at [confidence the tool reports].
Run: [start] to [end], traffic [%], stop rules [..].
```

## 4. Discipline

- **One variable** per test; one locale per test where possible.
- Wait for the tool's confidence indicator; do not stop on a good day. Run at least full weekly cycles (T).
- Low traffic (a few hundred impressions a day) rarely reaches significance: say so and recommend sequential before/after with a caveat, or custom pages for paid traffic.
- Seasonal effects: avoid starting around launches, holidays, price changes.
- Keep a **results log** (hypothesis, variant files, dates, outcome, decision) in the repo next to the listing.
- Apply winners through the normal metadata/version process and update the screenshot plan and `listing.md`.

## 5. Custom product pages by intent

Map traffic sources to pages: paid campaigns per audience, keyword-specific pages for Search, referral/QR pages for offline campaigns. Each page's message must be true for the product; lint them like the main listing.
