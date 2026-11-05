# Google Play Data safety worksheet

Derive from the inventory (`05-google-data-safety.md` §4). Collection = transmitted off-device (including by SDKs). Sharing = transfer to a third party that is not merely your service provider acting on your behalf (also not user-initiated, legally required, or fully anonymised). Ephemeral = in memory only for the real-time request, not retained; profiles cannot be ephemeral.

Purposes: AF = App functionality · AN = Analytics · DC = Developer communications · AM = Advertising or marketing · FS = Fraud prevention, security and compliance · PE = Personalisation · AC = Account management.

| Group | Data type | Collected? | Shared? | Required / Optional | Ephemeral? | Purposes | Source (feature / SDK) |
|---|---|---|---|---|---|---|---|
| Location | Approximate location | | | | | | |
| Location | Precise location | | | | | | |
| Personal info | Name | | | | | | |
| Personal info | Email address | | | | | | |
| Personal info | User IDs | | | | | | |
| Personal info | Address | | | | | | |
| Personal info | Phone number | | | | | | |
| Personal info | Race and ethnicity | | | | | | |
| Personal info | Political or religious beliefs | | | | | | |
| Personal info | Sexual orientation | | | | | | |
| Personal info | Other info | | | | | | |
| Financial info | User payment info | | | | | | |
| Financial info | Purchase history | | | | | | |
| Financial info | Credit score | | | | | | |
| Financial info | Other financial info | | | | | | |
| Health and fitness | Health info | | | | | | |
| Health and fitness | Fitness info | | | | | | |
| Messages | Emails | | | | | | |
| Messages | SMS or MMS | | | | | | |
| Messages | Other in-app messages | | | | | | |
| Photos and videos | Photos | | | | | | |
| Photos and videos | Videos | | | | | | |
| Audio files | Voice or sound recordings | | | | | | |
| Audio files | Music files | | | | | | |
| Audio files | Other audio files | | | | | | |
| Files and docs | Files and docs | | | | | | |
| Calendar | Calendar events | | | | | | |
| Contacts | Contacts | | | | | | |
| App activity | App interactions | | | | | | |
| App activity | In-app search history | | | | | | |
| App activity | Installed apps | | | | | | |
| App activity | Other user-generated content | | | | | | |
| App activity | Other actions | | | | | | |
| Web browsing | Web browsing history | | | | | | |
| App info and performance | Crash logs | | | | | | |
| App info and performance | Diagnostics | | | | | | |
| App info and performance | Other app performance data | | | | | | |
| Device or other IDs | Device or other IDs (advertising ID, Firebase installation ID, …) | | | | | | |

## Security practices

- Data encrypted in transit: {{yes (TLS/HTTPS everywhere; cleartext disabled) | no}}
- Users can request deletion: {{in-app | web form/email | auto-deleted within 90 days}}
- Optional badges: {{independent security review | Families commitment}}

## Linked declarations

- Privacy policy URL: {{public HTML}}
- Account deletion: in-app path {{…}}; web URL {{…}}
- Ads: {{contains ads: yes/no}}; AD_ID permission {{present/absent}} consistent with this form
- Target audience: {{ages}}; Families policy {{applies/not}}

## Diff against the Play Console export

Export the CSV from Play Console → App content → Data safety. **Importing a CSV overwrites existing answers**: warn the user before suggesting an import.

| Data type | Console (CSV) | Worksheet | Action |
|---|---|---|---|
