#!/usr/bin/env python3
"""Lint a store listing written in the canonical markdown format.

Format (see assets/listing-template.md):

    ## Apple — App Store Connect        (store heading: contains Apple / App Store / iOS, or Google / Play / Android)
    ### Italian                          (locale heading: Italian / it-IT, English / en-US, ...)
    **Name** (30)                        (field name + declared limit)

    ```
    value
    ```

Checks (errors fail the run, warnings do not):
  * character limits per field (declared limit, and the store's known limit)
  * Apple keywords: spaces after commas, duplicates, short terms, byte length,
    overlap and likely plural/singular duplicates with name and subtitle
  * Play title / short description rules from the Metadata policy
  * price / ranking claims, other-platform mentions, HTML, keyword stuffing
  * user-supplied banned terms (--banned / --banned-file)
  * missing fields per store and locale

Stdlib only. Usage:
    python3 lint-listing.py docs/store/listing.md [--banned "dating,incontri"] [--banned-file banned.txt]
Exit code 1 when an error is found. Limits last verified 2026-11-05 (see references/01-field-specs.md).
"""
import argparse
import re
import sys
import unicodedata

KNOWN = {
    "apple": {"name": 30, "subtitle": 30, "promo": 170, "keywords": 100, "description": 4000, "whatsnew": 4000},
    "play": {"name": 30, "short": 80, "description": 4000, "whatsnew": 500},
}
REQUIRED = {
    "apple": ["name", "subtitle", "keywords", "description"],
    "play": ["name", "short", "description"],
}
FIELD_ALIASES = [
    (r"^(app )?(name|title)$", "name"),
    (r"^subtitle$", "subtitle"),
    (r"^promo(tional)?( text)?$", "promo"),
    (r"^keywords?$", "keywords"),
    (r"^short( description)?$", "short"),
    (r"^(full )?description$", "description"),
    (r"^(what.?s new|release notes?)$", "whatsnew"),
]
STOP = set(
    "il lo la i gli le un uno una di a da in con su per tra fra e o ma che non del della dei delle al alla ai alle nel nella "
    "the a an of to in on for and or with by at from is are be your you it as app".split()
)
CTA = r"(download|install|play|try|get)\s+now|scarica(\s+ora|\s+subito)?|installa(\s+ora|\s+subito)?|prova(\s+ora|\s+subito)"
RANKING = r"#\s?1|\bnumber\s*1\b|\bbest\b|\btop\b|\bmigliore\b|\bil\s+migliore\b|award|premiato|editor'?s choice|million downloads|milioni di download"
PRICE = r"\bfree\b|\bgratis\b|\bgratuit[oa]\b|\bsale\b|\bsconto\b|\boffert[ae]\b|\bdiscount\b|\d+\s?%\s?(off|di sconto)|[€$£]\s?\d|\d\s?[€$£]"
OTHER_PLATFORM_APPLE = r"\bandroid\b|google play|play store"
OTHER_PLATFORM_PLAY = r"\biphone\b|\bipad\b|app store|\bios\b|\bapple\b"
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\U00002B00-\U00002BFF]")


def normalize(text):
    return unicodedata.normalize("NFC", text)


def strip_accents(text):
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn")


def tokens(text):
    return re.findall(r"[^\W\d_]+", normalize(text).lower())


def lang_of(locale):
    low = locale.lower()
    if re.search(r"ital|\bit\b|it-it", low):
        return "it"
    if re.search(r"engl|\ben\b|en-", low):
        return "en"
    return "xx"


def stem(word, lang):
    word = strip_accents(word)
    if lang == "it":
        return re.sub(r"[aeiou]$", "", word) if len(word) > 3 else word
    if lang == "en":
        if len(word) <= 3:
            return word
        if word.endswith("ies"):
            return word[:-3] + "y"
        if word.endswith(("sses", "xes", "ches", "shes")):
            return word[:-2]
        if word.endswith("s") and not word.endswith("ss"):
            return word[:-1]
        return word
    return word


def field_key(label):
    clean = label.strip().lower()
    for pattern, key in FIELD_ALIASES:
        if re.match(pattern, clean):
            return key
    return None


def store_of(heading):
    low = heading.lower()
    if re.search(r"apple|app store|ios|testflight", low):
        return "apple"
    if re.search(r"google|play|android", low):
        return "play"
    return None


def parse(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    store = None
    locale = ""
    fields = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^## (.+)$", line)
        if m:
            store = store_of(m.group(1))
            locale = ""
        m = re.match(r"^### (.+)$", line)
        if m:
            locale = m.group(1).strip()
        f = re.match(r"^\*\*(.+?)\*\*\s*(?:\((\d+)\))?", line)
        if f and store:
            key = field_key(f.group(1))
            if key:
                # The value is the first fenced block before the next field or heading.
                j = i + 1
                same_as = None
                while j < len(lines) and not lines[j].startswith("```"):
                    if re.match(r"^(#{1,6} |\*\*.+?\*\*\s*(\(\d+\))?)", lines[j]):
                        break
                    sm = re.search(r"same[- ]as:\s*(apple|play)\s+(\S+)\s+(\w+)", lines[j], re.I)
                    if sm:
                        same_as = (sm.group(1).lower(), sm.group(2).lower(), sm.group(3).lower())
                    j += 1
                value = None
                if j < len(lines) and lines[j].startswith("```"):
                    body = []
                    j += 1
                    while j < len(lines) and not lines[j].startswith("```"):
                        body.append(lines[j])
                        j += 1
                    value = normalize("\n".join(body).strip())
                fields.append(
                    {
                        "store": store,
                        "locale": locale or "(default)",
                        "key": key,
                        "label": f.group(1),
                        "declared": int(f.group(2)) if f.group(2) else None,
                        "value": value,
                        "same_as": same_as,
                        "line": i + 1,
                    }
                )
        i += 1
    # resolve "same-as: apple Italian description"
    index = {(f["store"], f["locale"].lower(), f["key"]): f for f in fields}
    for f in fields:
        if f["value"] is None and f["same_as"]:
            ref = index.get((f["same_as"][0], f["same_as"][1], f["same_as"][2]))
            if ref and ref["value"] is not None:
                f["value"] = ref["value"]
                f["inherited"] = True
    return fields


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--banned", default="", help="comma separated terms that must not appear in any field")
    ap.add_argument("--banned-file", default="", help="file with one banned term per line")
    ap.add_argument("--stuff-threshold", type=int, default=8, help="occurrences of one non-stop word in a description")
    args = ap.parse_args()

    banned = [t.strip().lower() for t in args.banned.split(",") if t.strip()]
    if args.banned_file:
        banned += [t.strip().lower() for t in open(args.banned_file, encoding="utf-8") if t.strip() and not t.startswith("#")]

    fields = parse(args.file)
    if not fields:
        print(f"ERROR: no fields found in {args.file}. See assets/listing-template.md for the format.")
        sys.exit(2)

    errors, warnings = [], []
    declared_keys = {(f["store"], f["locale"], f["key"]) for f in fields}
    unlinted = [f for f in fields if f["value"] is None]
    fields = [f for f in fields if f["value"] is not None]
    for f in unlinted:
        warnings.append(
            f"{f['store']} · {f['locale']} · {f['label']} (line {f['line']}): no fenced value block, not linted "
            "(add a block or '<!-- same-as: apple Italian description -->')"
        )

    def err(f, msg):
        errors.append(f"{f['store']} · {f['locale']} · {f['label']} (line {f['line']}): {msg}")

    def warn(f, msg):
        warnings.append(f"{f['store']} · {f['locale']} · {f['label']} (line {f['line']}): {msg}")

    by_group = {}
    for f in fields:
        by_group.setdefault((f["store"], f["locale"]), {})[f["key"]] = f

    for f in fields:
        value, key, store = f["value"], f["key"], f["store"]
        limit = KNOWN.get(store, {}).get(key)
        length = len(value)
        if limit and length > limit:
            err(f, f"{length} characters, store limit {limit}")
        if f["declared"] and length > f["declared"]:
            err(f, f"{length} characters, declared limit {f['declared']}")
        if limit and f["declared"] and f["declared"] != limit:
            warn(f, f"declared limit {f['declared']} differs from the store limit {limit}")
        low = value.lower()

        for term in banned:
            for hit in re.finditer(r"(?<![^\W_])" + re.escape(term) + r"(?![^\W_])", low):
                before = low[max(0, hit.start() - 30):hit.start()]
                if re.search(r"(non\s+(è|e'|sono)|not\s+(a|an)|isn'?t|aren'?t|no|senza|without)\b[^.]*$", before):
                    warn(f, f"banned term '{term}' in a negated sentence: still indexed and quotable, rewrite unless the rule allows it")
                else:
                    err(f, f"banned term '{term}'")
                break

        if re.search(r"<\/?[a-z][^>]*>", value):
            warn(f, "HTML tags: descriptions are plain text")

        if key in ("name", "subtitle"):
            strict = err if (store == "play" and key == "name") else warn
            if re.search(PRICE, low):
                strict(f, "price or promotion wording (Play Metadata policy forbids it in the title; Apple 2.3.7 in name/subtitle)")
            if re.search(RANKING, low):
                strict(f, "ranking or superlative claim (Play Metadata policy forbids it in the title; Apple 2.3.7 in name/subtitle)")
            if EMOJI.search(value):
                (err if store == "play" else warn)(f, "emoji in name/subtitle")
        if store == "play" and key == "name":
            caps = [w for w in re.findall(r"[A-Za-zÀ-ÿ]{4,}", value) if w.isupper()]
            if caps:
                warn(f, f"ALL CAPS word(s) {caps}: allowed only as the brand name")
        if store == "play" and key == "short":
            if re.search(CTA, low):
                err(f, "call to action (download/install/play/try now)")
            if re.search(RANKING, low) or re.search(r"\bnew\b|\bnuovo\b|\bsale\b|\bdiscount\b", low):
                err(f, "forbidden word (best, #1, top, new, discount, sale, million downloads)")
            if EMOJI.search(value) or "\n" in value or re.search(r"([!?.,;:])\1", value):
                err(f, "emoji, line break or repeated punctuation")
            if value.endswith(".") and len(re.findall(r"[.!?](\s|$)", value)) < 2:
                warn(f, "final period on a single sentence")
        if key == "description":
            other = OTHER_PLATFORM_APPLE if store == "apple" else OTHER_PLATFORM_PLAY
            if re.search(other, low):
                warn(f, "mentions the other platform/store" + (" (Apple 2.3.10)" if store == "apple" else ""))
            counts = {}
            for t in tokens(value):
                if len(t) > 3 and t not in STOP:
                    counts[t] = counts.get(t, 0) + 1
            heavy = [f"{t}×{n}" for t, n in counts.items() if n >= args.stuff_threshold]
            if heavy:
                warn(f, f"possible keyword stuffing: {', '.join(sorted(heavy))}")
        if key == "whatsnew" and store == "play" and re.search(CTA + "|" + RANKING, low):
            warn(f, "promotional wording in release notes (Play: not allowed)")
        if key == "whatsnew" and re.search(r"^(bug ?fix(es)?|miglioramenti|bug fixes and improvements)\.?$", low):
            warn(f, "generic text: allowed only for bug fixes (Apple 2.3.12)")

    for (store, locale), group in by_group.items():
        for required in REQUIRED.get(store, []):
            if required not in group and (store, locale, required) not in declared_keys:
                warnings.append(f"{store} · {locale}: missing field '{required}'")
        if store != "apple" or "keywords" not in group:
            continue
        kw = group["keywords"]
        raw = kw["value"]
        lang = lang_of(locale)
        terms = [t for t in raw.split(",")]
        if re.search(r",\s", raw):
            warn(kw, "space after a comma wastes characters (use 'a,b,c')")
        if raw.endswith(",") or ",," in raw:
            warn(kw, "empty term or trailing comma")
        clean = [t.strip().lower() for t in terms if t.strip()]
        if len(set(clean)) != len(clean):
            warn(kw, "duplicate terms")
        if len(raw.encode("utf-8")) > 100 and len(raw) <= 100:
            warn(kw, f"{len(raw.encode('utf-8'))} UTF-8 bytes: one Apple page says bytes, others say characters; trim to be safe")
        for t in clean:
            if len(t) <= 2:
                warn(kw, f"term '{t}' is two characters or fewer")
            if t in ("app", "game", "apps", "games"):
                warn(kw, f"generic term '{t}'")
        used = set()
        for other in ("name", "subtitle"):
            if other in group:
                used |= {stem(t, lang) for t in tokens(group[other]["value"])}
        used_exact = set()
        for other in ("name", "subtitle"):
            if other in group:
                used_exact |= set(tokens(group[other]["value"]))
        wasted = []
        for t in clean:
            for w in tokens(t):
                if w in used_exact:
                    wasted.append(f"'{w}' (already in name/subtitle)")
                elif stem(w, lang) in used and w not in STOP:
                    wasted.append(f"'{w}' (plural/singular of a name/subtitle word)")
        if wasted:
            warn(kw, "wasted keyword space, Apple indexes name and subtitle already: " + "; ".join(sorted(set(wasted))))

    print(f"\nStore listing lint — {args.file}\n")
    print(f"{len(fields)} linted fields · {len({(f['store'], f['locale']) for f in fields})} store/locale groups\n")
    for f in fields:
        limit = KNOWN.get(f["store"], {}).get(f["key"]) or f["declared"] or 0
        n = len(f["value"])
        mark = "✗" if limit and n > limit else "✓"
        print(f"  {mark} {f['store']:<5} {f['locale']:<12} {f['label']:<22} {n:>5}/{limit or '-'}")
    if warnings:
        print("\nWarnings")
        for w in warnings:
            print("  ! " + w)
    if errors:
        print("\nErrors")
        for e in errors:
            print("  ✗ " + e)
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)\n")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
