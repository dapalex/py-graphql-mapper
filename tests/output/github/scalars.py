from pygqlmap.gql_types import ID

Base64String = str ##A (potentially binary) string encoded using base64.

Boolean = bool ##Represents `true` or `false` values.

Date = str ##An ISO-8601 encoded date string.

DateTime = str ##An ISO-8601 encoded UTC date string.

Float = float ##Represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

GitObjectID = str ##A Git object ID.

GitSSHRemote = str ##Git SSH string

GitTimestamp = str ##An ISO-8601 encoded date string. Unlike the DateTime type, GitTimestamp is not converted in UTC.

HTML = str ##A string containing HTML code.

ID = ID ##Represents a unique identifier that is Base64 obfuscated. It is often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an ID.

Int = int ##Represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

PreciseDateTime = str ##An ISO-8601 encoded UTC date string with millisecond precision.

String = str ##Represents textual data as UTF-8 character sequences. This type is most often used by GraphQL to represent free-form human-readable text.

URI = str ##An RFC 3986, RFC 3987, and RFC 6570 (level 4) compliant URI string.

X509Certificate = str ##A valid x509 certificate string

isRequired = bool ##Whether this is required to pass before merging for a specific pull request.

trackedIssuesCount = int ##The number of tracked issues for this issue

viewerMergeBodyText = str ##The merge body text for the viewer and method.

viewerMergeHeadlineText = str ##The merge headline text for the viewer and method.

totalIssueContributions = int ##How many issues the user opened.

totalPullRequestContributions = int ##How many pull requests the user opened.

totalRepositoriesWithContributedIssues = int ##How many different repositories the user opened issues in.

totalRepositoriesWithContributedPullRequests = int ##How many different repositories the user opened pull requests in.

totalRepositoryContributions = int ##How many repositories the user created.

text = str ##UTF8 text data or null if the file is binary

isSponsoredBy = bool ##Whether the given account is sponsoring this user/organization.

totalSponsorshipAmountAsSponsorInCents = int ##The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

anyPinnableItems = bool ##Determine if this repository owner has any items that can be pinned to their profile.

canReceiveOrganizationEmailsWhenNotificationsRestricted = bool ##Could this user receive email notifications, if the organization had notification restrictions enabled?

organizationVerifiedDomainEmails = str ##Verified email addresses that match verified domains for a specified organization the user is a member of.
