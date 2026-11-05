# Apple 01 — Guideline 1: Safety

Source: App Review Guidelines, section 1. Confidence **V** (read verbatim 2026-11-05; page footer *Last Updated: October 16, 2026*). Paraphrased; cite by rule number.

Columns: **Ev** = evidence class (C code, B build, K console, L listing; see `00-method.md` §2).

## 1.1 Objectionable content

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 1.1 | No offensive, disgusting or "just plain creepy" content | Any content app, any UGC | Read sample content, seed data, onboarding copy, store screenshots | C, L |
| 1.1.1 | No defamatory/discriminatory/mean-spirited content targeting religion, race, orientation, gender, national/ethnic origin or other groups. Professional satire is generally exempt | Content, UGC, AI output | Search copy and prompts for slurs/targeting; for AI features, review system prompts and safety settings | C |
| 1.1.2 | No realistic depictions of killing/maiming/torture/abuse; no violence encouragement. Game enemies may not target a real race, culture, government, corporation or other real entity | Games, media | Review art/text assets; enemy naming and flags | C, L |
| 1.1.3 | No depictions encouraging illegal/reckless use of weapons; no facilitating purchase of firearms or ammunition | Weapon-related content or marketplaces | Search `gun|firearm|ammo|weapon` in listings and content | C |
| 1.1.4 | No overtly sexual/pornographic material; includes hookup apps and anything facilitating prostitution or trafficking | Dating, social, AI image/chat | Review NSFW policies, filters, AI image/chat safety config; check age gating | C |
| 1.1.5 | No inflammatory religious commentary or misleading quotations of religious texts | Religion/news content | Review content sources | C |
| 1.1.6 | No false information or features (fake location trackers, inaccurate device data). "For entertainment" is no excuse. Anonymous/prank call or SMS/MMS apps are rejected | Utility, prank, fake-data features | Search for fabricated readings: `fake|prank|simulate` in sensors, battery, location, call/SMS | C |
| 1.1.7 | No harmful content capitalising on current events (conflicts, attacks, epidemics) | Topical apps | Review listing copy and content | L |

## 1.2 User-generated content

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 1.2 | UGC apps (social, UGC platforms, **AI content generation**) need: (1) filtering of objectionable material from posts, (2) a mechanism to report offensive content with timely responses, (3) the ability to block abusive users, (4) published contact information. Chatroulette-style random/anonymous chat, "hot-or-not" objectification, threats and bullying risk removal without notice. Web-sourced UGC with incidental NSFW content must be hidden by default and enabled via the developer's website | Any user can publish text, image, audio, video or generated content visible to others | Find the four mechanisms in code and UI: report action, block action, filter/moderation pipeline, contact in app and Support URL. Each missing mechanism is a separate 🔴. For AI generators, check output moderation and a report path | C, K |
| 1.2.1 | Moderated "creator" communities may offer creator content as UGC if it does not change the app's core features; also follow 1.2 and 3.1.1 and tell users which content needs extra purchases | App hosts creator content (video, articles, audio, casual games) | Check the moderation claim, purchase labelling | C, L |
| 1.2.1(a) | Creator apps must let users identify content above the app's age rating and use an age-restriction mechanism based on verified or declared age | Creator content exceeds the rating | Find the age-restriction mechanism and its trigger; check content flags | C |

## 1.3 Kids Category

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 1.3 | Kids Category apps: no links out, purchase opportunities or other distractions unless behind a **parental gate**. Must comply with children's privacy laws. No sending PII or device info to third parties. **No third-party analytics or advertising**, except limited analytics that collect no IDFA or identifiable child info (name, DOB, email), location or device info; limited contextual ads only with publicly documented Kids policies and human review of creatives. Rules persist after leaving the category | Kids Category selected, or "Made for Kids" age category | List every third-party SDK; mark any that collect identifiers. Locate parental gate on every external link, IAP and ad. Check ATT absent | C, K |

## 1.4 Physical harm

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 1.4.1 | Medical apps get extra scrutiny; accuracy claims need disclosed data and methodology. Apps claiming x-ray, blood pressure, body temperature, blood glucose or blood oxygen measurement **using only device sensors** are not permitted. Remind users to consult a doctor. Submit regulatory clearance documentation if you have it | Health/medical/measurement features | Search measurement claims in code and listing; look for disclaimers and methodology notes | C, L |
| 1.4.2 | Drug dosage calculators must come from an approved source (manufacturer, hospital, university, insurer, pharmacy) or have FDA/international approval; long-term support | Dosage/medication calculators | Verify sources cited in-app and in review notes | C, L |
| 1.4.3 | No apps encouraging tobacco/vape, illegal drugs or excessive alcohol; none encouraging minors to do so; no selling controlled substances or tobacco (except licensed pharmacies and licensed cannabis dispensaries) | Drinking games, cannabis, vape content | Review content and commerce flows | C, L |
| 1.4.4 | DUI checkpoint info only if published by law enforcement; no encouragement of drunk or reckless driving | Navigation/driving apps | Review data sources | C |
| 1.4.5 | No urging users into bets, challenges or device use that risks physical harm | Challenge/fitness/AR games | Review challenge mechanics and warnings | C |

## 1.5–1.7

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 1.5 | The app **and its Support URL** must give users an easy way to contact the developer. Wallet passes need valid issuer contact info and a dedicated certificate tied to the brand/trademark owner | Always | Open the Support URL (must be live and show contact path). Find a contact route inside the app (Settings/About). Wallet passes: check certificate ownership | C, K, L |
| 1.6 | Implement appropriate security to protect user data (see 5.1) from unauthorised use, disclosure or access by third parties | Any app handling user data | Spot-check: TLS everywhere (no cleartext), tokens in Keychain/Keystore not plain storage, no secrets in the bundle, backend access control (RLS/rules). Deep review belongs to a security audit | C |
| 1.7 | Apps for reporting alleged crimes must involve local law enforcement and be offered only where that involvement is active | Crime/incident reporting | Verify the law-enforcement integration and geo-limits | C, L |

## Rule-of-thumb verdicts

- A UGC/AI-generation app missing **any** of report / block / filter / contact → 🔴 (1.2).
- Kids Category with any third-party analytics SDK that reads identifiers → 🔴 (1.3).
- Camera-only vital sign measurement claim → 🔴 (1.4.1).
- Support URL dead or contact-less → 🔴 (1.5); fix is minutes.
