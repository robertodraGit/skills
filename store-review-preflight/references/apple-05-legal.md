# Apple 05 — Guideline 5: Legal

Source: App Review Guidelines, section 5 and "After You Submit". Confidence **V** (verbatim, read 2026-11-05; *Last Updated: October 16, 2026*). Paraphrased.

**Intro**: comply with all laws where the app is offered. Apps that solicit or encourage criminal or clearly reckless behaviour are rejected. Apps facilitating human trafficking or child exploitation are removed and authorities notified.

## 5.1.1 Data collection and storage

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 5.1.1(i) **Privacy policy** | Link in App Store Connect metadata **and in the app**. Must state what data is collected, how, and all uses; confirm third parties (analytics, ad networks, SDKs, parents, subsidiaries, related entities) give **equal protection**; explain retention/deletion and how to revoke consent or request deletion | Always | Open the policy URL (must load, public). Find the in-app link. Compare policy to the SDK inventory: every SDK data flow must be covered. Deep check → `privacy-audit` | C, K, L |
| 5.1.1(ii) **Permission** | Get consent for collection even if data is anonymous. **Paid functionality must not depend on granting access.** Provide an easy withdrawal method. **Purpose strings must be complete** (clear, specific). Collecting on GDPR "legitimate interest" without consent requires complying with all of that law | Always | Review every `*UsageDescription` string (specific, not "needed for the app"). Verify analytics consent flow or lawful-basis justification. Verify withdrawal path in settings | C |
| 5.1.1(iii) **Data minimisation** | Request only data needed for core functionality; where possible use the out-of-process picker or share sheet instead of full Photos/Contacts access | Photos, contacts, files | Prefer `PHPicker`/`UIDocumentPicker`; flag full library access without need | C |
| 5.1.1(iv) **Access** | Do not manipulate or force consent to unnecessary access (example: photo upload must not require microphone access). **Offer alternatives** (e.g. manual address entry if Location is declined) | Permission-gated features | Test the denied-permission path of each permission: the app must still work or degrade gracefully | C |
| 5.1.1(v) **Account sign-in** | Allow use without login if there are no significant account features. **If accounts can be created, offer account deletion within the app.** No personal information required unless core or legally required. Apps not tied to a specific social network must offer access without login or another mechanism. Pulling basic profile, sharing, inviting friends is not core. Provide an in-app way to revoke social-network credentials and disable data access. Do not store social credentials/tokens off-device | Any account creation | Find the delete-account flow (`deleteAccount`, `delete_user`). It must delete the **account record and associated personal data**, not deactivate; be easy to find; link to the web page if a website is required; inform about timing, subscriptions, retained data. See `apple-06` G-A7 for the FAQ rules (Sign in with Apple revocation, guest accounts, subscription messaging) | C |
| 5.1.1(vi) | Apps used to surreptitiously discover passwords or private data are removed from the Program | Always | — | C |
| 5.1.1(vii) | `SFSafariViewController` must be visibly presented, not hidden/obscured, and must not track users without knowledge and consent | In-app browsers | Review usage | C |
| 5.1.1(viii) | No compiling personal information from non-user or non-consented sources, even public databases | Scrapers, data brokers, lead tools | Search for scraping of personal data | C |
| 5.1.1(ix) | Highly regulated fields (banking and financial services, healthcare, gambling, legal cannabis use, air travel, crypto exchanges) or sensitive-data apps must be submitted by a **legal entity**, not an individual developer. Cannabis sale apps geo-restricted | Regulated domains | Check developer account type (K) against the domain | K |
| 5.1.1(x) | Basic contact info (name, email) may be requested only if optional, features are not conditional on it, and kids limits are respected | Sign-up forms | Review required fields | C |

## 5.1.2 Data use and sharing

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 5.1.2(i) | Get permission before using, transmitting or sharing personal data. **Disclose where data is shared with third parties, "including with third-party AI", and get explicit permission first.** App data may be shared with third parties only to improve the app or serve advertising (with the disclosures). **Tracking requires the App Tracking Transparency API.** Apps may not require enabling push notifications, location services or tracking to access functionality or receive compensation (incl. gift cards/codes) | Any third-party data flow, any AI API receiving user content, any tracking | Inventory outbound data flows. For each LLM/AI call carrying user content: find the consent/disclosure UI before the first send. ATT only when "tracking" per Apple's definition (see `apple-06` G-A6) | C |
| 5.1.2(ii) | No repurposing data collected for one purpose without further consent unless law permits | Always | Compare stated purposes to actual uses | C |
| 5.1.2(iii) | No covert profiles; no re-identification of anonymous users; no rebuilding profiles from Apple APIs or from data described as "anonymized/aggregated" | Analytics, enrichment | Search for fingerprinting and identity-resolution code | C |
| 5.1.2(iv) | No contact databases built from Contacts/Photos or other user-data APIs for own use or sale; no collecting which other apps are installed for analytics or advertising | Contacts/Photos, app-list collectors | Search for `canOpenURL` probing loops, upload of contacts | C |
| 5.1.2(v) | Contacting people from Contacts/Photos data only on the user's explicit individualised initiative. No "Select All" or default-all. Show a preview of the message and sender before sending | Invite/contact flows | Review invite UI | C |
| 5.1.2(vi) | Data from HomeKit, HealthKit, Clinical Health Records, MovementDisorder APIs, ClassKit, depth/facial mapping tools (ARKit, Camera, Photo APIs) may not be used for marketing, advertising or use-based data mining, including by third parties | Those frameworks | Trace where such data goes (SDKs, analytics) | C |
| 5.1.2(vii) | Apple Pay-acquired data may be shared with third parties only to facilitate or improve delivery of goods and services | Apple Pay | Review | C |

## 5.1.3 Health and health research

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 5.1.3(i) | Health, fitness and medical research data may not be disclosed to third parties or used for advertising, marketing or use-based data mining, except to improve health management or for health research (with permission). A direct user benefit (e.g. reduced insurance premium) allowed if the benefit provider submits the app and data is not shared with third parties. **Disclose the specific health data collected from the device** | Health data | Trace health data to every SDK (analytics, crash reporters) | C |
| 5.1.3(ii) | No false data written into HealthKit; no personal health information in iCloud | HealthKit/iCloud | Review writes | C |
| 5.1.3(iii) | Health research consent (participants or guardians) must cover nature/purpose/duration, procedures/risks/benefits, confidentiality and third-party sharing, a contact point, the withdrawal process | Health research | Review consent text | C |
| 5.1.3(iv) | Independent ethics review board approval; proof on request | Health research | Ask for documentation | K |

## 5.1.4 Kids

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 5.1.4(a) | Care with children's data; review COPPA, GDPR and other laws. Birthdate and parental contact only to comply with those statutes, and the app must have useful or entertainment value regardless of age. Apps intended primarily for kids **should not include third-party analytics or third-party advertising** | Kids audience | Inventory SDKs | C |
| 5.1.4(b) | Limited third-party analytics/ads allowed per 1.3. Kids Category apps, or apps that collect or can share a minor's personal info (name, address, email, location, photos, videos, drawings, chat, persistent identifiers), must have a privacy policy and comply with children's privacy statutes. The **parental gate is generally not parental consent**. Non-Kids apps may not imply a child audience in name, subtitle, icon, screenshots, description | Kids audience | Review | C, L |

## 5.1.5 Location services

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 5.1.5 | Use location only when directly relevant to features. No location APIs for emergency services or autonomous control of vehicles, aircraft and other devices (small devices and toys excepted). Notify and get consent before collecting/transmitting/using location; explain the purpose in-app | Location | Check the permission level (When In Use vs Always), the purpose strings, and that location is not sent to ad/analytics SDKs | C |

## 5.2 Intellectual property

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 5.2 | Use only content you created or are licensed to use | Always | Check asset provenance | C, L |
| 5.2.1 | No unpermitted third-party trademarks, copyrights, patented ideas; no misleading or copycat names/metadata in bundle or developer name | Always | Review names/assets | C, L |
| 5.2.2 | Use or display third-party content only where the service's terms specifically permit it; authorisation on request | Content from third-party APIs | Verify ToS | C |
| 5.2.3 | No saving, converting or downloading media from third-party sources (Apple Music, YouTube, SoundCloud, Vimeo) without explicit authorisation | Downloaders | Review | C |
| 5.2.4 | Don't imply Apple is a source or endorses the app's quality or functionality; "Editor's Choice" is applied by Apple | Marketing copy | Review | L |
| 5.2.5 | No apps confusingly similar to Apple products/interfaces/apps/ad themes; no Apple emoji in apps/extensions; iTunes/Apple Music previews not used for entertainment value; Activity rings must not visualise Move/Exercise/Stand resembling the Activity control; Apple Weather data follows WeatherKit attribution | Look-alike UI | Review | C, L |

## 5.3 Gaming, gambling, lotteries

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 5.3 | Among the most regulated offerings; vet legal obligations everywhere; expect extra review time | Gambling-like features | — | — |
| 5.3.1 | Sweepstakes and contests sponsored by the app developer | Contests | Review | C |
| 5.3.2 | Official rules in the app; Apple is not a sponsor | Contests | Review | C |
| 5.3.3 | No IAP of credit/currency for real-money gaming | Real-money gaming | Review | C |
| 5.3.4 | Real-money gaming (sports betting, poker, casino, horse racing) or lotteries: licensing, geo-restriction to licensed locations, **free on the App Store**; illegal gambling aids (card counters) not permitted; lottery needs consideration, chance, prize | Real-money gaming | Review licences and geo-fence | C, K |

## 5.4–5.6

| ID | Requirement | Applies when | How to check | Ev |
|---|---|---|---|---|
| 5.4 | VPN apps: `NEVPNManager`; organisation developer; clear in-app screen declaring data collected and use before any purchase or use; never sell, use or disclose data; commit in the privacy policy; licence info in review notes where a VPN licence is required | VPN | Review | C, K |
| 5.5 | MDM: request the capability from Apple; limited to enterprises, schools, government (and limited parental control/security cases); same data rules as VPN | MDM | Review | C, K |
| 5.6 | **Developer Code of Conduct**: treat everyone with respect; no manipulation or fraud; apps must not prey on users, trick them into purchases, force unnecessary data sharing, or raise prices in a tricky manner | Always | — | — |
| 5.6.1 | Respond respectfully to App Store reviews; use the provided review-prompt API (**custom review prompts disallowed**) | Review prompts | Search for custom rating prompts that gate or filter; require `SKStoreReviewController` / `requestReview` | C |
| 5.6.2 | Developer information truthful, relevant, up to date | Always | — | K |
| 5.6.3 | No discovery fraud (charts, search, reviews, referrals) | Always | — | — |
| 5.6.4 | Excessive complaints, negative reviews and refund requests may count against Code of Conduct compliance | Ongoing | — | — |

## After You Submit

Review timing is not guaranteed; expedite requests via the Contact Us form only when truly needed; appeals through the appeal topic; **bug fix submissions** for existing apps are not delayed over guideline violations except legal/safety issues (opt in via App Store Connect). A future release date delays visibility until that date (up to 24 hours to appear on all storefronts).

## Rule-of-thumb verdicts

- Account creation without in-app deletion → 🔴 (5.1.1(v)). Deactivation alone is insufficient.
- No privacy policy link in-app or in metadata → 🔴 (5.1.1(i)).
- User text/images sent to a third-party AI API without prior explicit disclosure and consent → 🟠/🔴 (5.1.2(i)).
- Custom "Do you like the app?" gate that routes happy users to the store → 🔴 (5.6.1).
- ATT prompt when nothing tracks, or tracking with no prompt → 🔴/🟠 (5.1.2(i)).
- Kids app with third-party analytics → 🔴 (1.3, 5.1.4).
