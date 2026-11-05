# Store listing — {{product}}

Canonical format read by `scripts/lint-listing.py`:
- `## <Store>` heading containing Apple / App Store / iOS or Google / Play / Android.
- `### <Locale>` heading (Italian, English, English (UK), …).
- Each field: `**Field name** (limit)` then a fenced block with the value. Prose between the heading and the block is allowed. A field without a block can point to another with `<!-- same-as: apple Italian description -->`.
- Lint: `python3 scripts/lint-listing.py docs/store/listing.md --banned "term1,term2"`.

Last aligned with product truth: {{date}} · build {{version}} · Claims ledger: {{path}}

## Positioning

- Sentence: {{For [audience] who [situation], [Brand] is the [category] that [differentiator].}}
- Banned terms: {{…}}
- Required phrases: {{…}}
- Tone: {{informal tu / formal Lei / en-US plain}}

## Apple — App Store Connect

Primary language: {{Italian}}.

### Italian

**Name** (30)

```
{{Brand: core term}}
```

**Subtitle** (30)

```
{{benefit + audience}}
```

**Promotional text** (170)

```
{{current hook}}
```

**Keywords** (100)

```
{{term1,term2,term3}}
```

**Description** (4000)

```
{{hook

HOW IT WORKS …}}
```

**What's New** (4000)

```
{{release notes}}
```

### English

(same fields)

## Google Play — store listing

### Italian

**App name** (30)

```
{{title}}
```

**Short description** (80)

```
{{one benefit sentence}}
```

**Full description** (4000)

<!-- same-as: apple Italian description -->

**Release notes** (500)

```
{{notes}}
```

### English

(same fields)

## Other fields

| Field | Value |
|---|---|
| Support URL | {{}} |
| Marketing URL | {{}} |
| Privacy Policy URL | {{}} |
| Copyright | {{year owner}} |
| Category | {{Apple primary/secondary; Play category + tags}} |
| Age rating | {{}} |
