from enum import Enum

class ActorType(Enum):
   USER = 'USER' ##Indicates a user actor.
   TEAM = 'TEAM' ##Indicates a team actor.

class AuditLogOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order audit log entries by timestamp

class CheckAnnotationLevel(Enum):
   FAILURE = 'FAILURE' ##An annotation indicating an inescapable error.
   NOTICE = 'NOTICE' ##An annotation indicating some information.
   WARNING = 'WARNING' ##An annotation indicating an ignorable error.

class CheckConclusionState(Enum):
   ACTION_REQUIRED = 'ACTION_REQUIRED' ##The check suite or run requires action.
   TIMED_OUT = 'TIMED_OUT' ##The check suite or run has timed out.
   CANCELLED = 'CANCELLED' ##The check suite or run has been cancelled.
   FAILURE = 'FAILURE' ##The check suite or run has failed.
   SUCCESS = 'SUCCESS' ##The check suite or run has succeeded.
   NEUTRAL = 'NEUTRAL' ##The check suite or run was neutral.
   SKIPPED = 'SKIPPED' ##The check suite or run was skipped.
   STARTUP_FAILURE = 'STARTUP_FAILURE' ##The check suite or run has failed at startup.
   STALE = 'STALE' ##The check suite or run was marked stale by GitHub. Only GitHub can use this conclusion.

class CheckRunState(Enum):
   ACTION_REQUIRED = 'ACTION_REQUIRED' ##The check run requires action.
   CANCELLED = 'CANCELLED' ##The check run has been cancelled.
   COMPLETED = 'COMPLETED' ##The check run has been completed.
   FAILURE = 'FAILURE' ##The check run has failed.
   IN_PROGRESS = 'IN_PROGRESS' ##The check run is in progress.
   NEUTRAL = 'NEUTRAL' ##The check run was neutral.
   PENDING = 'PENDING' ##The check run is in pending state.
   QUEUED = 'QUEUED' ##The check run has been queued.
   SKIPPED = 'SKIPPED' ##The check run was skipped.
   STALE = 'STALE' ##The check run was marked stale by GitHub. Only GitHub can use this conclusion.
   STARTUP_FAILURE = 'STARTUP_FAILURE' ##The check run has failed at startup.
   SUCCESS = 'SUCCESS' ##The check run has succeeded.
   TIMED_OUT = 'TIMED_OUT' ##The check run has timed out.
   WAITING = 'WAITING' ##The check run is in waiting state.

class CheckRunType(Enum):
   ALL = 'ALL' ##Every check run available.
   LATEST = 'LATEST' ##The latest check run.

class CheckStatusState(Enum):
   QUEUED = 'QUEUED' ##The check suite or run has been queued.
   IN_PROGRESS = 'IN_PROGRESS' ##The check suite or run is in progress.
   COMPLETED = 'COMPLETED' ##The check suite or run has been completed.
   WAITING = 'WAITING' ##The check suite or run is in waiting state.
   PENDING = 'PENDING' ##The check suite or run is in pending state.
   REQUESTED = 'REQUESTED' ##The check suite or run has been requested.

class CollaboratorAffiliation(Enum):
   OUTSIDE = 'OUTSIDE' ##All outside collaborators of an organization-owned subject.
   DIRECT = 'DIRECT' ##All collaborators with permissions to an organization-owned subject, regardless of organization membership status.
   ALL = 'ALL' ##All collaborators the authenticated user can see.

class CommentAuthorAssociation(Enum):
   MEMBER = 'MEMBER' ##Author is a member of the organization that owns the repository.
   OWNER = 'OWNER' ##Author is the owner of the repository.
   MANNEQUIN = 'MANNEQUIN' ##Author is a placeholder for an unclaimed user.
   COLLABORATOR = 'COLLABORATOR' ##Author has been invited to collaborate on the repository.
   CONTRIBUTOR = 'CONTRIBUTOR' ##Author has previously committed to the repository.
   FIRST_TIME_CONTRIBUTOR = 'FIRST_TIME_CONTRIBUTOR' ##Author has not previously committed to the repository.
   FIRST_TIMER = 'FIRST_TIMER' ##Author has not previously committed to GitHub.
   NONE = 'NONE' ##Author has no association with the repository.

class CommentCannotUpdateReason(Enum):
   ARCHIVED = 'ARCHIVED' ##Unable to create comment because repository is archived.
   INSUFFICIENT_ACCESS = 'INSUFFICIENT_ACCESS' ##You must be the author or have write access to this repository to update this comment.
   LOCKED = 'LOCKED' ##Unable to create comment because issue is locked.
   LOGIN_REQUIRED = 'LOGIN_REQUIRED' ##You must be logged in to update this comment.
   MAINTENANCE = 'MAINTENANCE' ##Repository is under maintenance.
   VERIFIED_EMAIL_REQUIRED = 'VERIFIED_EMAIL_REQUIRED' ##At least one email address must be verified to update this comment.
   DENIED = 'DENIED' ##You cannot update this comment

class CommitContributionOrderField(Enum):
   OCCURRED_AT = 'OCCURRED_AT' ##Order commit contributions by when they were made.
   COMMIT_COUNT = 'COMMIT_COUNT' ##Order commit contributions by how many commits they represent.

class ComparisonStatus(Enum):
   DIVERGED = 'DIVERGED' ##The head ref is both ahead and behind of the base ref, indicating git history has diverged.
   AHEAD = 'AHEAD' ##The head ref is ahead of the base ref.
   BEHIND = 'BEHIND' ##The head ref is behind the base ref.
   IDENTICAL = 'IDENTICAL' ##The head ref and base ref are identical.

class ContributionLevel(Enum):
   NONE = 'NONE' ##No contributions occurred.
   FIRST_QUARTILE = 'FIRST_QUARTILE' ##Lowest 25% of days of contributions.
   SECOND_QUARTILE = 'SECOND_QUARTILE' ##Second lowest 25% of days of contributions. More contributions than the first quartile.
   THIRD_QUARTILE = 'THIRD_QUARTILE' ##Second highest 25% of days of contributions. More contributions than second quartile, less than the fourth quartile.
   FOURTH_QUARTILE = 'FOURTH_QUARTILE' ##Highest 25% of days of contributions. More contributions than the third quartile.

class DefaultRepositoryPermissionField(Enum):
   NONE = 'NONE' ##No access
   READ = 'READ' ##Can read repos by default
   WRITE = 'WRITE' ##Can read and write repos by default
   ADMIN = 'ADMIN' ##Can read, write, and administrate repos by default

class DependencyGraphEcosystem(Enum):
   RUBYGEMS = 'RUBYGEMS' ##Ruby gems hosted at RubyGems.org
   NPM = 'NPM' ##JavaScript packages hosted at npmjs.com
   PIP = 'PIP' ##Python packages hosted at PyPI.org
   MAVEN = 'MAVEN' ##Java artifacts hosted at the Maven central repository
   NUGET = 'NUGET' ##.NET packages hosted at the NuGet Gallery
   COMPOSER = 'COMPOSER' ##PHP packages hosted at packagist.org
   GO = 'GO' ##Go modules
   ACTIONS = 'ACTIONS' ##GitHub Actions
   RUST = 'RUST' ##Rust crates
   PUB = 'PUB' ##Dart packages hosted at pub.dev

class DeploymentOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order collection by creation time

class DeploymentProtectionRuleType(Enum):
   REQUIRED_REVIEWERS = 'REQUIRED_REVIEWERS' ##Required reviewers
   WAIT_TIMER = 'WAIT_TIMER' ##Wait timer

class DeploymentReviewState(Enum):
   APPROVED = 'APPROVED' ##The deployment was approved.
   REJECTED = 'REJECTED' ##The deployment was rejected.

class DeploymentState(Enum):
   ABANDONED = 'ABANDONED' ##The pending deployment was not updated after 30 minutes.
   ACTIVE = 'ACTIVE' ##The deployment is currently active.
   DESTROYED = 'DESTROYED' ##An inactive transient deployment.
   ERROR = 'ERROR' ##The deployment experienced an error.
   FAILURE = 'FAILURE' ##The deployment has failed.
   INACTIVE = 'INACTIVE' ##The deployment is inactive.
   PENDING = 'PENDING' ##The deployment is pending.
   QUEUED = 'QUEUED' ##The deployment has queued
   IN_PROGRESS = 'IN_PROGRESS' ##The deployment is in progress.
   WAITING = 'WAITING' ##The deployment is waiting.

class DeploymentStatusState(Enum):
   PENDING = 'PENDING' ##The deployment is pending.
   SUCCESS = 'SUCCESS' ##The deployment was successful.
   FAILURE = 'FAILURE' ##The deployment has failed.
   INACTIVE = 'INACTIVE' ##The deployment is inactive.
   ERROR = 'ERROR' ##The deployment experienced an error.
   QUEUED = 'QUEUED' ##The deployment is queued
   IN_PROGRESS = 'IN_PROGRESS' ##The deployment is in progress.
   WAITING = 'WAITING' ##The deployment is waiting.

class DiffSide(Enum):
   LEFT = 'LEFT' ##The left side of the diff.
   RIGHT = 'RIGHT' ##The right side of the diff.

class DiscussionOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order discussions by creation time.
   UPDATED_AT = 'UPDATED_AT' ##Order discussions by most recent modification time.

class DiscussionPollOptionOrderField(Enum):
   AUTHORED_ORDER = 'AUTHORED_ORDER' ##Order poll options by the order that the poll author specified when creating the poll.
   VOTE_COUNT = 'VOTE_COUNT' ##Order poll options by the number of votes it has.

class DismissReason(Enum):
   FIX_STARTED = 'FIX_STARTED' ##A fix has already been started
   NO_BANDWIDTH = 'NO_BANDWIDTH' ##No bandwidth to fix this
   TOLERABLE_RISK = 'TOLERABLE_RISK' ##Risk is tolerable to this project
   INACCURATE = 'INACCURATE' ##This alert is inaccurate or incorrect
   NOT_USED = 'NOT_USED' ##Vulnerable code is not actually used

class EnterpriseAdministratorInvitationOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order enterprise administrator member invitations by creation time

class EnterpriseAdministratorRole(Enum):
   OWNER = 'OWNER' ##Represents an owner of the enterprise account.
   BILLING_MANAGER = 'BILLING_MANAGER' ##Represents a billing manager of the enterprise account.

class EnterpriseAllowPrivateRepositoryForkingPolicyValue(Enum):
   ENTERPRISE_ORGANIZATIONS = 'ENTERPRISE_ORGANIZATIONS' ##Members can fork a repository to an organization within this enterprise.
   SAME_ORGANIZATION = 'SAME_ORGANIZATION' ##Members can fork a repository only within the same organization (intra-org).
   SAME_ORGANIZATION_USER_ACCOUNTS = 'SAME_ORGANIZATION_USER_ACCOUNTS' ##Members can fork a repository to their user account or within the same organization.
   ENTERPRISE_ORGANIZATIONS_USER_ACCOUNTS = 'ENTERPRISE_ORGANIZATIONS_USER_ACCOUNTS' ##Members can fork a repository to their enterprise-managed user account or an organization inside this enterprise.
   USER_ACCOUNTS = 'USER_ACCOUNTS' ##Members can fork a repository to their user account.
   EVERYWHERE = 'EVERYWHERE' ##Members can fork a repository to their user account or an organization, either inside or outside of this enterprise.

class EnterpriseDefaultRepositoryPermissionSettingValue(Enum):
   NO_POLICY = 'NO_POLICY' ##Organizations in the enterprise choose base repository permissions for their members.
   ADMIN = 'ADMIN' ##Organization members will be able to clone, pull, push, and add new collaborators to all organization repositories.
   WRITE = 'WRITE' ##Organization members will be able to clone, pull, and push all organization repositories.
   READ = 'READ' ##Organization members will be able to clone and pull all organization repositories.
   NONE = 'NONE' ##Organization members will only be able to clone and pull public repositories.

class EnterpriseEnabledDisabledSettingValue(Enum):
   ENABLED = 'ENABLED' ##The setting is enabled for organizations in the enterprise.
   DISABLED = 'DISABLED' ##The setting is disabled for organizations in the enterprise.
   NO_POLICY = 'NO_POLICY' ##There is no policy set for organizations in the enterprise.

class EnterpriseEnabledSettingValue(Enum):
   ENABLED = 'ENABLED' ##The setting is enabled for organizations in the enterprise.
   NO_POLICY = 'NO_POLICY' ##There is no policy set for organizations in the enterprise.

class EnterpriseMemberOrderField(Enum):
   LOGIN = 'LOGIN' ##Order enterprise members by login
   CREATED_AT = 'CREATED_AT' ##Order enterprise members by creation time

class EnterpriseMembersCanCreateRepositoriesSettingValue(Enum):
   NO_POLICY = 'NO_POLICY' ##Organization administrators choose whether to allow members to create repositories.
   ALL = 'ALL' ##Members will be able to create public and private repositories.
   PUBLIC = 'PUBLIC' ##Members will be able to create only public repositories.
   PRIVATE = 'PRIVATE' ##Members will be able to create only private repositories.
   DISABLED = 'DISABLED' ##Members will not be able to create public or private repositories.

class EnterpriseMembersCanMakePurchasesSettingValue(Enum):
   ENABLED = 'ENABLED' ##The setting is enabled for organizations in the enterprise.
   DISABLED = 'DISABLED' ##The setting is disabled for organizations in the enterprise.

class EnterpriseServerInstallationOrderField(Enum):
   HOST_NAME = 'HOST_NAME' ##Order Enterprise Server installations by host name
   CUSTOMER_NAME = 'CUSTOMER_NAME' ##Order Enterprise Server installations by customer name
   CREATED_AT = 'CREATED_AT' ##Order Enterprise Server installations by creation time

class EnterpriseServerUserAccountEmailOrderField(Enum):
   EMAIL = 'EMAIL' ##Order emails by email

class EnterpriseServerUserAccountOrderField(Enum):
   LOGIN = 'LOGIN' ##Order user accounts by login
   REMOTE_CREATED_AT = 'REMOTE_CREATED_AT' ##Order user accounts by creation time on the Enterprise Server installation

class EnterpriseServerUserAccountsUploadOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order user accounts uploads by creation time

class EnterpriseServerUserAccountsUploadSyncState(Enum):
   PENDING = 'PENDING' ##The synchronization of the upload is pending.
   SUCCESS = 'SUCCESS' ##The synchronization of the upload succeeded.
   FAILURE = 'FAILURE' ##The synchronization of the upload failed.

class EnterpriseUserAccountMembershipRole(Enum):
   MEMBER = 'MEMBER' ##The user is a member of an organization in the enterprise.
   OWNER = 'OWNER' ##The user is an owner of an organization in the enterprise.
   UNAFFILIATED = 'UNAFFILIATED' ##The user is not an owner of the enterprise, and not a member or owner of any organizations in the enterprise; only for EMU-enabled enterprises.

class EnterpriseUserDeployment(Enum):
   CLOUD = 'CLOUD' ##The user is part of a GitHub Enterprise Cloud deployment.
   SERVER = 'SERVER' ##The user is part of a GitHub Enterprise Server deployment.

class FileViewedState(Enum):
   DISMISSED = 'DISMISSED' ##The file has new changes since last viewed.
   VIEWED = 'VIEWED' ##The file has been marked as viewed.
   UNVIEWED = 'UNVIEWED' ##The file has not been marked as viewed.

class FundingPlatform(Enum):
   GITHUB = 'GITHUB' ##GitHub funding platform.
   PATREON = 'PATREON' ##Patreon funding platform.
   OPEN_COLLECTIVE = 'OPEN_COLLECTIVE' ##Open Collective funding platform.
   KO_FI = 'KO_FI' ##Ko-fi funding platform.
   TIDELIFT = 'TIDELIFT' ##Tidelift funding platform.
   COMMUNITY_BRIDGE = 'COMMUNITY_BRIDGE' ##Community Bridge funding platform.
   LIBERAPAY = 'LIBERAPAY' ##Liberapay funding platform.
   ISSUEHUNT = 'ISSUEHUNT' ##IssueHunt funding platform.
   OTECHIE = 'OTECHIE' ##Otechie funding platform.
   LFX_CROWDFUNDING = 'LFX_CROWDFUNDING' ##LFX Crowdfunding funding platform.
   CUSTOM = 'CUSTOM' ##Custom funding platform.

class GistOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order gists by creation time
   UPDATED_AT = 'UPDATED_AT' ##Order gists by update time
   PUSHED_AT = 'PUSHED_AT' ##Order gists by push time

class GistPrivacy(Enum):
   PUBLIC = 'PUBLIC' ##Public
   SECRET = 'SECRET' ##Secret
   ALL = 'ALL' ##Gists that are public and secret

class GitSignatureState(Enum):
   VALID = 'VALID' ##Valid signature and verified by GitHub
   INVALID = 'INVALID' ##Invalid signature
   MALFORMED_SIG = 'MALFORMED_SIG' ##Malformed signature
   UNKNOWN_KEY = 'UNKNOWN_KEY' ##Key used for signing not known to GitHub
   BAD_EMAIL = 'BAD_EMAIL' ##Invalid email used for signing
   UNVERIFIED_EMAIL = 'UNVERIFIED_EMAIL' ##Email used for signing unverified on GitHub
   NO_USER = 'NO_USER' ##Email used for signing not known to GitHub
   UNKNOWN_SIG_TYPE = 'UNKNOWN_SIG_TYPE' ##Unknown signature type
   UNSIGNED = 'UNSIGNED' ##Unsigned
   GPGVERIFY_UNAVAILABLE = 'GPGVERIFY_UNAVAILABLE' ##Internal error - the GPG verification service is unavailable at the moment
   GPGVERIFY_ERROR = 'GPGVERIFY_ERROR' ##Internal error - the GPG verification service misbehaved
   NOT_SIGNING_KEY = 'NOT_SIGNING_KEY' ##The usage flags for the key that signed this don't allow signing
   EXPIRED_KEY = 'EXPIRED_KEY' ##Signing key expired
   OCSP_PENDING = 'OCSP_PENDING' ##Valid signature, pending certificate revocation checking
   OCSP_ERROR = 'OCSP_ERROR' ##Valid signature, though certificate revocation check failed
   BAD_CERT = 'BAD_CERT' ##The signing certificate or its chain could not be verified
   OCSP_REVOKED = 'OCSP_REVOKED' ##One or more certificates in chain has been revoked

class IdentityProviderConfigurationState(Enum):
   ENFORCED = 'ENFORCED' ##Authentication with an identity provider is configured and enforced.
   CONFIGURED = 'CONFIGURED' ##Authentication with an identity provider is configured but not enforced.
   UNCONFIGURED = 'UNCONFIGURED' ##Authentication with an identity provider is not configured.

class IpAllowListEnabledSettingValue(Enum):
   ENABLED = 'ENABLED' ##The setting is enabled for the owner.
   DISABLED = 'DISABLED' ##The setting is disabled for the owner.

class IpAllowListEntryOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order IP allow list entries by creation time.
   ALLOW_LIST_VALUE = 'ALLOW_LIST_VALUE' ##Order IP allow list entries by the allow list value.

class IpAllowListForInstalledAppsEnabledSettingValue(Enum):
   ENABLED = 'ENABLED' ##The setting is enabled for the owner.
   DISABLED = 'DISABLED' ##The setting is disabled for the owner.

class IssueClosedStateReason(Enum):
   COMPLETED = 'COMPLETED' ##An issue that has been closed as completed
   NOT_PLANNED = 'NOT_PLANNED' ##An issue that has been closed as not planned

class IssueCommentOrderField(Enum):
   UPDATED_AT = 'UPDATED_AT' ##Order issue comments by update time

class IssueOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order issues by creation time
   UPDATED_AT = 'UPDATED_AT' ##Order issues by update time
   COMMENTS = 'COMMENTS' ##Order issues by comment count

class IssueState(Enum):
   OPEN = 'OPEN' ##An issue that is still open
   CLOSED = 'CLOSED' ##An issue that has been closed

class IssueStateReason(Enum):
   REOPENED = 'REOPENED' ##An issue that has been reopened
   NOT_PLANNED = 'NOT_PLANNED' ##An issue that has been closed as not planned
   COMPLETED = 'COMPLETED' ##An issue that has been closed as completed

class IssueTimelineItemsItemType(Enum):
   ISSUE_COMMENT = 'ISSUE_COMMENT' ##Represents a comment on an Issue.
   CROSS_REFERENCED_EVENT = 'CROSS_REFERENCED_EVENT' ##Represents a mention made by one issue or pull request to another.
   ADDED_TO_PROJECT_EVENT = 'ADDED_TO_PROJECT_EVENT' ##Represents a 'added_to_project' event on a given issue or pull request.
   ASSIGNED_EVENT = 'ASSIGNED_EVENT' ##Represents an 'assigned' event on any assignable object.
   CLOSED_EVENT = 'CLOSED_EVENT' ##Represents a 'closed' event on any `Closable`.
   COMMENT_DELETED_EVENT = 'COMMENT_DELETED_EVENT' ##Represents a 'comment_deleted' event on a given issue or pull request.
   CONNECTED_EVENT = 'CONNECTED_EVENT' ##Represents a 'connected' event on a given issue or pull request.
   CONVERTED_NOTE_TO_ISSUE_EVENT = 'CONVERTED_NOTE_TO_ISSUE_EVENT' ##Represents a 'converted_note_to_issue' event on a given issue or pull request.
   CONVERTED_TO_DISCUSSION_EVENT = 'CONVERTED_TO_DISCUSSION_EVENT' ##Represents a 'converted_to_discussion' event on a given issue.
   DEMILESTONED_EVENT = 'DEMILESTONED_EVENT' ##Represents a 'demilestoned' event on a given issue or pull request.
   DISCONNECTED_EVENT = 'DISCONNECTED_EVENT' ##Represents a 'disconnected' event on a given issue or pull request.
   LABELED_EVENT = 'LABELED_EVENT' ##Represents a 'labeled' event on a given issue or pull request.
   LOCKED_EVENT = 'LOCKED_EVENT' ##Represents a 'locked' event on a given issue or pull request.
   MARKED_AS_DUPLICATE_EVENT = 'MARKED_AS_DUPLICATE_EVENT' ##Represents a 'marked_as_duplicate' event on a given issue or pull request.
   MENTIONED_EVENT = 'MENTIONED_EVENT' ##Represents a 'mentioned' event on a given issue or pull request.
   MILESTONED_EVENT = 'MILESTONED_EVENT' ##Represents a 'milestoned' event on a given issue or pull request.
   MOVED_COLUMNS_IN_PROJECT_EVENT = 'MOVED_COLUMNS_IN_PROJECT_EVENT' ##Represents a 'moved_columns_in_project' event on a given issue or pull request.
   PINNED_EVENT = 'PINNED_EVENT' ##Represents a 'pinned' event on a given issue or pull request.
   REFERENCED_EVENT = 'REFERENCED_EVENT' ##Represents a 'referenced' event on a given `ReferencedSubject`.
   REMOVED_FROM_PROJECT_EVENT = 'REMOVED_FROM_PROJECT_EVENT' ##Represents a 'removed_from_project' event on a given issue or pull request.
   RENAMED_TITLE_EVENT = 'RENAMED_TITLE_EVENT' ##Represents a 'renamed' event on a given issue or pull request
   REOPENED_EVENT = 'REOPENED_EVENT' ##Represents a 'reopened' event on any `Closable`.
   SUBSCRIBED_EVENT = 'SUBSCRIBED_EVENT' ##Represents a 'subscribed' event on a given `Subscribable`.
   TRANSFERRED_EVENT = 'TRANSFERRED_EVENT' ##Represents a 'transferred' event on a given issue or pull request.
   UNASSIGNED_EVENT = 'UNASSIGNED_EVENT' ##Represents an 'unassigned' event on any assignable object.
   UNLABELED_EVENT = 'UNLABELED_EVENT' ##Represents an 'unlabeled' event on a given issue or pull request.
   UNLOCKED_EVENT = 'UNLOCKED_EVENT' ##Represents an 'unlocked' event on a given issue or pull request.
   USER_BLOCKED_EVENT = 'USER_BLOCKED_EVENT' ##Represents a 'user_blocked' event on a given user.
   UNMARKED_AS_DUPLICATE_EVENT = 'UNMARKED_AS_DUPLICATE_EVENT' ##Represents an 'unmarked_as_duplicate' event on a given issue or pull request.
   UNPINNED_EVENT = 'UNPINNED_EVENT' ##Represents an 'unpinned' event on a given issue or pull request.
   UNSUBSCRIBED_EVENT = 'UNSUBSCRIBED_EVENT' ##Represents an 'unsubscribed' event on a given `Subscribable`.

class LabelOrderField(Enum):
   NAME = 'NAME' ##Order labels by name 
   CREATED_AT = 'CREATED_AT' ##Order labels by creation time

class LanguageOrderField(Enum):
   SIZE = 'SIZE' ##Order languages by the size of all files containing the language

class LockReason(Enum):
   OFF_TOPIC = 'OFF_TOPIC' ##The issue or pull request was locked because the conversation was off-topic.
   TOO_HEATED = 'TOO_HEATED' ##The issue or pull request was locked because the conversation was too heated.
   RESOLVED = 'RESOLVED' ##The issue or pull request was locked because the conversation was resolved.
   SPAM = 'SPAM' ##The issue or pull request was locked because the conversation was spam.

class MannequinOrderField(Enum):
   LOGIN = 'LOGIN' ##Order mannequins alphabetically by their source login.
   CREATED_AT = 'CREATED_AT' ##Order mannequins why when they were created.

class MergeCommitMessage(Enum):
   PR_TITLE = 'PR_TITLE' ##Default to the pull request's title.
   PR_BODY = 'PR_BODY' ##Default to the pull request's body.
   BLANK = 'BLANK' ##Default to a blank commit message.

class MergeCommitTitle(Enum):
   PR_TITLE = 'PR_TITLE' ##Default to the pull request's title.
   MERGE_MESSAGE = 'MERGE_MESSAGE' ##Default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).

class MergeableState(Enum):
   MERGEABLE = 'MERGEABLE' ##The pull request can be merged.
   CONFLICTING = 'CONFLICTING' ##The pull request cannot be merged due to merge conflicts.
   UNKNOWN = 'UNKNOWN' ##The mergeability of the pull request is still being calculated.

class MigrationSourceType(Enum):
   AZURE_DEVOPS = 'AZURE_DEVOPS' ##An Azure DevOps migration source.
   BITBUCKET_SERVER = 'BITBUCKET_SERVER' ##A Bitbucket Server migration source.
   GITHUB_ARCHIVE = 'GITHUB_ARCHIVE' ##A GitHub Migration API source.

class MigrationState(Enum):
   NOT_STARTED = 'NOT_STARTED' ##The migration has not started.
   QUEUED = 'QUEUED' ##The migration has been queued.
   IN_PROGRESS = 'IN_PROGRESS' ##The migration is in progress.
   SUCCEEDED = 'SUCCEEDED' ##The migration has succeeded.
   FAILED = 'FAILED' ##The migration has failed.
   PENDING_VALIDATION = 'PENDING_VALIDATION' ##The migration needs to have its credentials validated.
   FAILED_VALIDATION = 'FAILED_VALIDATION' ##The migration has invalid credentials.

class MilestoneOrderField(Enum):
   DUE_DATE = 'DUE_DATE' ##Order milestones by when they are due.
   CREATED_AT = 'CREATED_AT' ##Order milestones by when they were created.
   UPDATED_AT = 'UPDATED_AT' ##Order milestones by when they were last updated.
   NUMBER = 'NUMBER' ##Order milestones by their number.

class MilestoneState(Enum):
   OPEN = 'OPEN' ##A milestone that is still open.
   CLOSED = 'CLOSED' ##A milestone that has been closed.

class NotificationRestrictionSettingValue(Enum):
   ENABLED = 'ENABLED' ##The setting is enabled for the owner.
   DISABLED = 'DISABLED' ##The setting is disabled for the owner.

class OIDCProviderType(Enum):
   AAD = 'AAD' ##Azure Active Directory

class OauthApplicationCreateAuditEntryState(Enum):
   ACTIVE = 'ACTIVE' ##The OAuth Application was active and allowed to have OAuth Accesses.
   SUSPENDED = 'SUSPENDED' ##The OAuth Application was suspended from generating OAuth Accesses due to abuse or security concerns.
   PENDING_DELETION = 'PENDING_DELETION' ##The OAuth Application was in the process of being deleted.

class OperationType(Enum):
   ACCESS = 'ACCESS' ##An existing resource was accessed
   AUTHENTICATION = 'AUTHENTICATION' ##A resource performed an authentication event
   CREATE = 'CREATE' ##A new resource was created
   MODIFY = 'MODIFY' ##An existing resource was modified
   REMOVE = 'REMOVE' ##An existing resource was removed
   RESTORE = 'RESTORE' ##An existing resource was restored
   TRANSFER = 'TRANSFER' ##An existing resource was transferred between multiple resources

class OrderDirection(Enum):
   ASC = 'ASC' ##Specifies an ascending order for a given `orderBy` argument.
   DESC = 'DESC' ##Specifies a descending order for a given `orderBy` argument.

class OrgAddMemberAuditEntryPermission(Enum):
   READ = 'READ' ##Can read and clone repositories.
   ADMIN = 'ADMIN' ##Can read, clone, push, and add collaborators to repositories.

class OrgCreateAuditEntryBillingPlan(Enum):
   FREE = 'FREE' ##Free Plan
   BUSINESS = 'BUSINESS' ##Team Plan
   BUSINESS_PLUS = 'BUSINESS_PLUS' ##Enterprise Cloud Plan
   UNLIMITED = 'UNLIMITED' ##Legacy Unlimited Plan
   TIERED_PER_SEAT = 'TIERED_PER_SEAT' ##Tiered Per Seat Plan

class OrgEnterpriseOwnerOrderField(Enum):
   LOGIN = 'LOGIN' ##Order enterprise owners by login.

class OrgRemoveBillingManagerAuditEntryReason(Enum):
   TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE = 'TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE' ##The organization required 2FA of its billing managers and this user did not have 2FA enabled.
   SAML_EXTERNAL_IDENTITY_MISSING = 'SAML_EXTERNAL_IDENTITY_MISSING' ##SAML external identity missing
   SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY = 'SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY' ##SAML SSO enforcement requires an external identity

class OrgRemoveMemberAuditEntryMembershipType(Enum):
   SUSPENDED = 'SUSPENDED' ##A suspended member.
   DIRECT_MEMBER = 'DIRECT_MEMBER' ##A direct member is a user that is a member of the Organization.
   ADMIN = 'ADMIN' ##Organization administrators have full access and can change several settings, including the names of repositories that belong to the Organization and Owners team membership. In addition, organization admins can delete the organization and all of its repositories.
   BILLING_MANAGER = 'BILLING_MANAGER' ##A billing manager is a user who manages the billing settings for the Organization, such as updating payment information.
   UNAFFILIATED = 'UNAFFILIATED' ##An unaffiliated collaborator is a person who is not a member of the Organization and does not have access to any repositories in the Organization.
   OUTSIDE_COLLABORATOR = 'OUTSIDE_COLLABORATOR' ##An outside collaborator is a person who isn't explicitly a member of the Organization, but who has Read, Write, or Admin permissions to one or more repositories in the organization.

class OrgRemoveMemberAuditEntryReason(Enum):
   TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE = 'TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE' ##The organization required 2FA of its billing managers and this user did not have 2FA enabled.
   SAML_EXTERNAL_IDENTITY_MISSING = 'SAML_EXTERNAL_IDENTITY_MISSING' ##SAML external identity missing
   SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY = 'SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY' ##SAML SSO enforcement requires an external identity
   USER_ACCOUNT_DELETED = 'USER_ACCOUNT_DELETED' ##User account has been deleted
   TWO_FACTOR_ACCOUNT_RECOVERY = 'TWO_FACTOR_ACCOUNT_RECOVERY' ##User was removed from organization during account recovery

class OrgRemoveOutsideCollaboratorAuditEntryMembershipType(Enum):
   OUTSIDE_COLLABORATOR = 'OUTSIDE_COLLABORATOR' ##An outside collaborator is a person who isn't explicitly a member of the Organization, but who has Read, Write, or Admin permissions to one or more repositories in the organization.
   UNAFFILIATED = 'UNAFFILIATED' ##An unaffiliated collaborator is a person who is not a member of the Organization and does not have access to any repositories in the organization.
   BILLING_MANAGER = 'BILLING_MANAGER' ##A billing manager is a user who manages the billing settings for the Organization, such as updating payment information.

class OrgRemoveOutsideCollaboratorAuditEntryReason(Enum):
   TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE = 'TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE' ##The organization required 2FA of its billing managers and this user did not have 2FA enabled.
   SAML_EXTERNAL_IDENTITY_MISSING = 'SAML_EXTERNAL_IDENTITY_MISSING' ##SAML external identity missing

class OrgUpdateDefaultRepositoryPermissionAuditEntryPermission(Enum):
   READ = 'READ' ##Can read and clone repositories.
   WRITE = 'WRITE' ##Can read, clone and push to repositories.
   ADMIN = 'ADMIN' ##Can read, clone, push, and add collaborators to repositories.
   NONE = 'NONE' ##No default permission value.

class OrgUpdateMemberAuditEntryPermission(Enum):
   READ = 'READ' ##Can read and clone repositories.
   ADMIN = 'ADMIN' ##Can read, clone, push, and add collaborators to repositories.

class OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility(Enum):
   ALL = 'ALL' ##All organization members are restricted from creating any repositories.
   PUBLIC = 'PUBLIC' ##All organization members are restricted from creating public repositories.
   NONE = 'NONE' ##All organization members are allowed to create any repositories.
   PRIVATE = 'PRIVATE' ##All organization members are restricted from creating private repositories.
   INTERNAL = 'INTERNAL' ##All organization members are restricted from creating internal repositories.
   PUBLIC_INTERNAL = 'PUBLIC_INTERNAL' ##All organization members are restricted from creating public or internal repositories.
   PRIVATE_INTERNAL = 'PRIVATE_INTERNAL' ##All organization members are restricted from creating private or internal repositories.
   PUBLIC_PRIVATE = 'PUBLIC_PRIVATE' ##All organization members are restricted from creating public or private repositories.

class OrganizationInvitationRole(Enum):
   DIRECT_MEMBER = 'DIRECT_MEMBER' ##The user is invited to be a direct member of the organization.
   ADMIN = 'ADMIN' ##The user is invited to be an admin of the organization.
   BILLING_MANAGER = 'BILLING_MANAGER' ##The user is invited to be a billing manager of the organization.
   REINSTATE = 'REINSTATE' ##The user's previous role will be reinstated.

class OrganizationInvitationType(Enum):
   USER = 'USER' ##The invitation was to an existing user.
   EMAIL = 'EMAIL' ##The invitation was to an email address.

class OrganizationMemberRole(Enum):
   MEMBER = 'MEMBER' ##The user is a member of the organization.
   ADMIN = 'ADMIN' ##The user is an administrator of the organization.

class OrganizationMembersCanCreateRepositoriesSettingValue(Enum):
   ALL = 'ALL' ##Members will be able to create public and private repositories.
   PRIVATE = 'PRIVATE' ##Members will be able to create only private repositories.
   INTERNAL = 'INTERNAL' ##Members will be able to create only internal repositories.
   DISABLED = 'DISABLED' ##Members will not be able to create public or private repositories.

class OrganizationOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order organizations by creation time
   LOGIN = 'LOGIN' ##Order organizations by login

class PackageFileOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order package files by creation time

class PackageOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order packages by creation time

class PackageType(Enum):
   DEBIAN = 'DEBIAN' ##A debian package.
   PYPI = 'PYPI' ##A python package.

class PackageVersionOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order package versions by creation time

class PatchStatus(Enum):
   ADDED = 'ADDED' ##The file was added. Git status 'A'.
   DELETED = 'DELETED' ##The file was deleted. Git status 'D'.
   RENAMED = 'RENAMED' ##The file was renamed. Git status 'R'.
   COPIED = 'COPIED' ##The file was copied. Git status 'C'.
   MODIFIED = 'MODIFIED' ##The file's contents were changed. Git status 'M'.
   CHANGED = 'CHANGED' ##The file's type was changed. Git status 'T'.

class PinnableItemType(Enum):
   REPOSITORY = 'REPOSITORY' ##A repository.
   GIST = 'GIST' ##A gist.
   ISSUE = 'ISSUE' ##An issue.
   PROJECT = 'PROJECT' ##A project.
   PULL_REQUEST = 'PULL_REQUEST' ##A pull request.
   USER = 'USER' ##A user.
   ORGANIZATION = 'ORGANIZATION' ##An organization.
   TEAM = 'TEAM' ##A team.

class PinnedDiscussionGradient(Enum):
   RED_ORANGE = 'RED_ORANGE' ##A gradient of red to orange
   BLUE_MINT = 'BLUE_MINT' ##A gradient of blue to mint
   BLUE_PURPLE = 'BLUE_PURPLE' ##A gradient of blue to purple
   PINK_BLUE = 'PINK_BLUE' ##A gradient of pink to blue
   PURPLE_CORAL = 'PURPLE_CORAL' ##A gradient of purple to coral

class PinnedDiscussionPattern(Enum):
   DOT_FILL = 'DOT_FILL' ##A solid dot pattern
   PLUS = 'PLUS' ##A plus sign pattern
   ZAP = 'ZAP' ##A lightning bolt pattern
   CHEVRON_UP = 'CHEVRON_UP' ##An upward-facing chevron pattern
   DOT = 'DOT' ##A hollow dot pattern
   HEART_FILL = 'HEART_FILL' ##A heart pattern

class ProjectCardArchivedState(Enum):
   ARCHIVED = 'ARCHIVED' ##A project card that is archived
   NOT_ARCHIVED = 'NOT_ARCHIVED' ##A project card that is not archived

class ProjectCardState(Enum):
   CONTENT_ONLY = 'CONTENT_ONLY' ##The card has content only.
   NOTE_ONLY = 'NOTE_ONLY' ##The card has a note only.
   REDACTED = 'REDACTED' ##The card is redacted.

class ProjectColumnPurpose(Enum):
   TODO = 'TODO' ##The column contains cards still to be worked on
   IN_PROGRESS = 'IN_PROGRESS' ##The column contains cards which are currently being worked on
   DONE = 'DONE' ##The column contains cards which are complete

class ProjectItemType(Enum):
   ISSUE = 'ISSUE' ##Issue
   PULL_REQUEST = 'PULL_REQUEST' ##Pull Request
   DRAFT_ISSUE = 'DRAFT_ISSUE' ##Draft Issue
   REDACTED = 'REDACTED' ##Redacted Item

class ProjectOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order projects by creation time
   UPDATED_AT = 'UPDATED_AT' ##Order projects by update time
   NAME = 'NAME' ##Order projects by name

class ProjectState(Enum):
   OPEN = 'OPEN' ##The project is open.
   CLOSED = 'CLOSED' ##The project is closed.

class ProjectTemplate(Enum):
   BASIC_KANBAN = 'BASIC_KANBAN' ##Create a board with columns for To do, In progress and Done.
   AUTOMATED_KANBAN_V2 = 'AUTOMATED_KANBAN_V2' ##Create a board with v2 triggers to automatically move cards across To do, In progress and Done columns.
   AUTOMATED_REVIEWS_KANBAN = 'AUTOMATED_REVIEWS_KANBAN' ##Create a board with triggers to automatically move cards across columns with review automation.
   BUG_TRIAGE = 'BUG_TRIAGE' ##Create a board to triage and prioritize bugs with To do, priority, and Done columns.

class ProjectV2FieldOrderField(Enum):
   POSITION = 'POSITION' ##Order project v2 fields by position
   CREATED_AT = 'CREATED_AT' ##Order project v2 fields by creation time
   NAME = 'NAME' ##Order project v2 fields by name

class ProjectV2FieldType(Enum):
   ASSIGNEES = 'ASSIGNEES' ##Assignees
   LINKED_PULL_REQUESTS = 'LINKED_PULL_REQUESTS' ##Linked Pull Requests
   REVIEWERS = 'REVIEWERS' ##Reviewers
   LABELS = 'LABELS' ##Labels
   MILESTONE = 'MILESTONE' ##Milestone
   REPOSITORY = 'REPOSITORY' ##Repository
   TITLE = 'TITLE' ##Title
   TEXT = 'TEXT' ##Text
   SINGLE_SELECT = 'SINGLE_SELECT' ##Single Select
   NUMBER = 'NUMBER' ##Number
   DATE = 'DATE' ##Date
   ITERATION = 'ITERATION' ##Iteration
   TRACKS = 'TRACKS' ##Tracks
   TRACKED_BY = 'TRACKED_BY' ##Tracked by

class ProjectV2ItemFieldValueOrderField(Enum):
   POSITION = 'POSITION' ##Order project v2 item field values by the their position in the project

class ProjectV2ItemOrderField(Enum):
   POSITION = 'POSITION' ##Order project v2 items by the their position in the project

class ProjectV2ItemType(Enum):
   ISSUE = 'ISSUE' ##Issue
   PULL_REQUEST = 'PULL_REQUEST' ##Pull Request
   DRAFT_ISSUE = 'DRAFT_ISSUE' ##Draft Issue
   REDACTED = 'REDACTED' ##Redacted Item

class ProjectV2OrderField(Enum):
   TITLE = 'TITLE' ##The project's title
   NUMBER = 'NUMBER' ##The project's number
   UPDATED_AT = 'UPDATED_AT' ##The project's date and time of update
   CREATED_AT = 'CREATED_AT' ##The project's date and time of creation

class ProjectV2State(Enum):
   OPEN = 'OPEN' ##A project v2 that is still open
   CLOSED = 'CLOSED' ##A project v2 that has been closed

class ProjectV2ViewLayout(Enum):
   BOARD_LAYOUT = 'BOARD_LAYOUT' ##Board layout
   TABLE_LAYOUT = 'TABLE_LAYOUT' ##Table layout

class ProjectV2ViewOrderField(Enum):
   POSITION = 'POSITION' ##Order project v2 views by position
   CREATED_AT = 'CREATED_AT' ##Order project v2 views by creation time
   NAME = 'NAME' ##Order project v2 views by name

class ProjectViewLayout(Enum):
   BOARD_LAYOUT = 'BOARD_LAYOUT' ##Board layout
   TABLE_LAYOUT = 'TABLE_LAYOUT' ##Table layout

class PullRequestMergeMethod(Enum):
   MERGE = 'MERGE' ##Add all commits from the head branch to the base branch with a merge commit.
   SQUASH = 'SQUASH' ##Combine all commits from the head branch into a single commit in the base branch.
   REBASE = 'REBASE' ##Add all commits from the head branch onto the base branch individually.

class PullRequestOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order pull_requests by creation time
   UPDATED_AT = 'UPDATED_AT' ##Order pull_requests by update time

class PullRequestReviewCommentState(Enum):
   PENDING = 'PENDING' ##A comment that is part of a pending review
   SUBMITTED = 'SUBMITTED' ##A comment that is part of a submitted review

class PullRequestReviewDecision(Enum):
   CHANGES_REQUESTED = 'CHANGES_REQUESTED' ##Changes have been requested on the pull request.
   APPROVED = 'APPROVED' ##The pull request has received an approving review.
   REVIEW_REQUIRED = 'REVIEW_REQUIRED' ##A review is required before the pull request can be merged.

class PullRequestReviewEvent(Enum):
   COMMENT = 'COMMENT' ##Submit general feedback without explicit approval.
   APPROVE = 'APPROVE' ##Submit feedback and approve merging these changes.
   REQUEST_CHANGES = 'REQUEST_CHANGES' ##Submit feedback that must be addressed before merging.
   DISMISS = 'DISMISS' ##Dismiss review so it now longer effects merging.

class PullRequestReviewState(Enum):
   PENDING = 'PENDING' ##A review that has not yet been submitted.
   COMMENTED = 'COMMENTED' ##An informational review.
   APPROVED = 'APPROVED' ##A review allowing the pull request to merge.
   CHANGES_REQUESTED = 'CHANGES_REQUESTED' ##A review blocking the pull request from merging.
   DISMISSED = 'DISMISSED' ##A review that has been dismissed.

class PullRequestState(Enum):
   OPEN = 'OPEN' ##A pull request that is still open.
   CLOSED = 'CLOSED' ##A pull request that has been closed without being merged.
   MERGED = 'MERGED' ##A pull request that has been closed by being merged.

class PullRequestTimelineItemsItemType(Enum):
   PULL_REQUEST_COMMIT = 'PULL_REQUEST_COMMIT' ##Represents a Git commit part of a pull request.
   PULL_REQUEST_COMMIT_COMMENT_THREAD = 'PULL_REQUEST_COMMIT_COMMENT_THREAD' ##Represents a commit comment thread part of a pull request.
   PULL_REQUEST_REVIEW = 'PULL_REQUEST_REVIEW' ##A review object for a given pull request.
   PULL_REQUEST_REVIEW_THREAD = 'PULL_REQUEST_REVIEW_THREAD' ##A threaded list of comments for a given pull request.
   PULL_REQUEST_REVISION_MARKER = 'PULL_REQUEST_REVISION_MARKER' ##Represents the latest point in the pull request timeline for which the viewer has seen the pull request's commits.
   AUTOMATIC_BASE_CHANGE_FAILED_EVENT = 'AUTOMATIC_BASE_CHANGE_FAILED_EVENT' ##Represents a 'automatic_base_change_failed' event on a given pull request.
   AUTOMATIC_BASE_CHANGE_SUCCEEDED_EVENT = 'AUTOMATIC_BASE_CHANGE_SUCCEEDED_EVENT' ##Represents a 'automatic_base_change_succeeded' event on a given pull request.
   AUTO_MERGE_DISABLED_EVENT = 'AUTO_MERGE_DISABLED_EVENT' ##Represents a 'auto_merge_disabled' event on a given pull request.
   AUTO_MERGE_ENABLED_EVENT = 'AUTO_MERGE_ENABLED_EVENT' ##Represents a 'auto_merge_enabled' event on a given pull request.
   AUTO_REBASE_ENABLED_EVENT = 'AUTO_REBASE_ENABLED_EVENT' ##Represents a 'auto_rebase_enabled' event on a given pull request.
   AUTO_SQUASH_ENABLED_EVENT = 'AUTO_SQUASH_ENABLED_EVENT' ##Represents a 'auto_squash_enabled' event on a given pull request.
   BASE_REF_CHANGED_EVENT = 'BASE_REF_CHANGED_EVENT' ##Represents a 'base_ref_changed' event on a given issue or pull request.
   BASE_REF_FORCE_PUSHED_EVENT = 'BASE_REF_FORCE_PUSHED_EVENT' ##Represents a 'base_ref_force_pushed' event on a given pull request.
   BASE_REF_DELETED_EVENT = 'BASE_REF_DELETED_EVENT' ##Represents a 'base_ref_deleted' event on a given pull request.
   DEPLOYED_EVENT = 'DEPLOYED_EVENT' ##Represents a 'deployed' event on a given pull request.
   DEPLOYMENT_ENVIRONMENT_CHANGED_EVENT = 'DEPLOYMENT_ENVIRONMENT_CHANGED_EVENT' ##Represents a 'deployment_environment_changed' event on a given pull request.
   HEAD_REF_DELETED_EVENT = 'HEAD_REF_DELETED_EVENT' ##Represents a 'head_ref_deleted' event on a given pull request.
   HEAD_REF_FORCE_PUSHED_EVENT = 'HEAD_REF_FORCE_PUSHED_EVENT' ##Represents a 'head_ref_force_pushed' event on a given pull request.
   HEAD_REF_RESTORED_EVENT = 'HEAD_REF_RESTORED_EVENT' ##Represents a 'head_ref_restored' event on a given pull request.
   MERGED_EVENT = 'MERGED_EVENT' ##Represents a 'merged' event on a given pull request.
   REVIEW_DISMISSED_EVENT = 'REVIEW_DISMISSED_EVENT' ##Represents a 'review_dismissed' event on a given issue or pull request.
   REVIEW_REQUESTED_EVENT = 'REVIEW_REQUESTED_EVENT' ##Represents an 'review_requested' event on a given pull request.
   REVIEW_REQUEST_REMOVED_EVENT = 'REVIEW_REQUEST_REMOVED_EVENT' ##Represents an 'review_request_removed' event on a given pull request.
   READY_FOR_REVIEW_EVENT = 'READY_FOR_REVIEW_EVENT' ##Represents a 'ready_for_review' event on a given pull request.
   CONVERT_TO_DRAFT_EVENT = 'CONVERT_TO_DRAFT_EVENT' ##Represents a 'convert_to_draft' event on a given pull request.
   ADDED_TO_MERGE_QUEUE_EVENT = 'ADDED_TO_MERGE_QUEUE_EVENT' ##Represents an 'added_to_merge_queue' event on a given pull request.
   REMOVED_FROM_MERGE_QUEUE_EVENT = 'REMOVED_FROM_MERGE_QUEUE_EVENT' ##Represents a 'removed_from_merge_queue' event on a given pull request.
   ISSUE_COMMENT = 'ISSUE_COMMENT' ##Represents a comment on an Issue.
   CROSS_REFERENCED_EVENT = 'CROSS_REFERENCED_EVENT' ##Represents a mention made by one issue or pull request to another.
   ADDED_TO_PROJECT_EVENT = 'ADDED_TO_PROJECT_EVENT' ##Represents a 'added_to_project' event on a given issue or pull request.
   ASSIGNED_EVENT = 'ASSIGNED_EVENT' ##Represents an 'assigned' event on any assignable object.
   CLOSED_EVENT = 'CLOSED_EVENT' ##Represents a 'closed' event on any `Closable`.
   COMMENT_DELETED_EVENT = 'COMMENT_DELETED_EVENT' ##Represents a 'comment_deleted' event on a given issue or pull request.
   CONNECTED_EVENT = 'CONNECTED_EVENT' ##Represents a 'connected' event on a given issue or pull request.
   CONVERTED_NOTE_TO_ISSUE_EVENT = 'CONVERTED_NOTE_TO_ISSUE_EVENT' ##Represents a 'converted_note_to_issue' event on a given issue or pull request.
   CONVERTED_TO_DISCUSSION_EVENT = 'CONVERTED_TO_DISCUSSION_EVENT' ##Represents a 'converted_to_discussion' event on a given issue.
   DEMILESTONED_EVENT = 'DEMILESTONED_EVENT' ##Represents a 'demilestoned' event on a given issue or pull request.
   DISCONNECTED_EVENT = 'DISCONNECTED_EVENT' ##Represents a 'disconnected' event on a given issue or pull request.
   LABELED_EVENT = 'LABELED_EVENT' ##Represents a 'labeled' event on a given issue or pull request.
   LOCKED_EVENT = 'LOCKED_EVENT' ##Represents a 'locked' event on a given issue or pull request.
   MARKED_AS_DUPLICATE_EVENT = 'MARKED_AS_DUPLICATE_EVENT' ##Represents a 'marked_as_duplicate' event on a given issue or pull request.
   MENTIONED_EVENT = 'MENTIONED_EVENT' ##Represents a 'mentioned' event on a given issue or pull request.
   MILESTONED_EVENT = 'MILESTONED_EVENT' ##Represents a 'milestoned' event on a given issue or pull request.
   MOVED_COLUMNS_IN_PROJECT_EVENT = 'MOVED_COLUMNS_IN_PROJECT_EVENT' ##Represents a 'moved_columns_in_project' event on a given issue or pull request.
   PINNED_EVENT = 'PINNED_EVENT' ##Represents a 'pinned' event on a given issue or pull request.
   REFERENCED_EVENT = 'REFERENCED_EVENT' ##Represents a 'referenced' event on a given `ReferencedSubject`.
   REMOVED_FROM_PROJECT_EVENT = 'REMOVED_FROM_PROJECT_EVENT' ##Represents a 'removed_from_project' event on a given issue or pull request.
   RENAMED_TITLE_EVENT = 'RENAMED_TITLE_EVENT' ##Represents a 'renamed' event on a given issue or pull request
   REOPENED_EVENT = 'REOPENED_EVENT' ##Represents a 'reopened' event on any `Closable`.
   SUBSCRIBED_EVENT = 'SUBSCRIBED_EVENT' ##Represents a 'subscribed' event on a given `Subscribable`.
   TRANSFERRED_EVENT = 'TRANSFERRED_EVENT' ##Represents a 'transferred' event on a given issue or pull request.
   UNASSIGNED_EVENT = 'UNASSIGNED_EVENT' ##Represents an 'unassigned' event on any assignable object.
   UNLABELED_EVENT = 'UNLABELED_EVENT' ##Represents an 'unlabeled' event on a given issue or pull request.
   UNLOCKED_EVENT = 'UNLOCKED_EVENT' ##Represents an 'unlocked' event on a given issue or pull request.
   USER_BLOCKED_EVENT = 'USER_BLOCKED_EVENT' ##Represents a 'user_blocked' event on a given user.
   UNMARKED_AS_DUPLICATE_EVENT = 'UNMARKED_AS_DUPLICATE_EVENT' ##Represents an 'unmarked_as_duplicate' event on a given issue or pull request.
   UNPINNED_EVENT = 'UNPINNED_EVENT' ##Represents an 'unpinned' event on a given issue or pull request.
   UNSUBSCRIBED_EVENT = 'UNSUBSCRIBED_EVENT' ##Represents an 'unsubscribed' event on a given `Subscribable`.

class PullRequestUpdateState(Enum):
   OPEN = 'OPEN' ##A pull request that is still open.
   CLOSED = 'CLOSED' ##A pull request that has been closed without being merged.

class ReactionContent(Enum):
   THUMBS_UP = 'THUMBS_UP' ##Represents the `:+1:` emoji.
   THUMBS_DOWN = 'THUMBS_DOWN' ##Represents the `:-1:` emoji.
   LAUGH = 'LAUGH' ##Represents the `:laugh:` emoji.
   HOORAY = 'HOORAY' ##Represents the `:hooray:` emoji.
   CONFUSED = 'CONFUSED' ##Represents the `:confused:` emoji.
   HEART = 'HEART' ##Represents the `:heart:` emoji.
   ROCKET = 'ROCKET' ##Represents the `:rocket:` emoji.
   EYES = 'EYES' ##Represents the `:eyes:` emoji.

class ReactionOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Allows ordering a list of reactions by when they were created.

class RefOrderField(Enum):
   TAG_COMMIT_DATE = 'TAG_COMMIT_DATE' ##Order refs by underlying commit date if the ref prefix is refs/tags/
   ALPHABETICAL = 'ALPHABETICAL' ##Order refs by their alphanumeric name

class ReleaseOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order releases by creation time
   NAME = 'NAME' ##Order releases alphabetically by name

class RepoAccessAuditEntryVisibility(Enum):
   INTERNAL = 'INTERNAL' ##The repository is visible only to users in the same business.
   PRIVATE = 'PRIVATE' ##The repository is visible only to those with explicit access.
   PUBLIC = 'PUBLIC' ##The repository is visible to everyone.

class RepoAddMemberAuditEntryVisibility(Enum):
   INTERNAL = 'INTERNAL' ##The repository is visible only to users in the same business.
   PRIVATE = 'PRIVATE' ##The repository is visible only to those with explicit access.
   PUBLIC = 'PUBLIC' ##The repository is visible to everyone.

class RepoArchivedAuditEntryVisibility(Enum):
   INTERNAL = 'INTERNAL' ##The repository is visible only to users in the same business.
   PRIVATE = 'PRIVATE' ##The repository is visible only to those with explicit access.
   PUBLIC = 'PUBLIC' ##The repository is visible to everyone.

class RepoChangeMergeSettingAuditEntryMergeType(Enum):
   MERGE = 'MERGE' ##The pull request is added to the base branch in a merge commit.
   REBASE = 'REBASE' ##Commits from the pull request are added onto the base branch individually without a merge commit.
   SQUASH = 'SQUASH' ##The pull request's commits are squashed into a single commit before they are merged to the base branch.

class RepoCreateAuditEntryVisibility(Enum):
   INTERNAL = 'INTERNAL' ##The repository is visible only to users in the same business.
   PRIVATE = 'PRIVATE' ##The repository is visible only to those with explicit access.
   PUBLIC = 'PUBLIC' ##The repository is visible to everyone.

class RepoDestroyAuditEntryVisibility(Enum):
   INTERNAL = 'INTERNAL' ##The repository is visible only to users in the same business.
   PRIVATE = 'PRIVATE' ##The repository is visible only to those with explicit access.
   PUBLIC = 'PUBLIC' ##The repository is visible to everyone.

class RepoRemoveMemberAuditEntryVisibility(Enum):
   INTERNAL = 'INTERNAL' ##The repository is visible only to users in the same business.
   PRIVATE = 'PRIVATE' ##The repository is visible only to those with explicit access.
   PUBLIC = 'PUBLIC' ##The repository is visible to everyone.

class ReportedContentClassifiers(Enum):
   SPAM = 'SPAM' ##A spammy piece of content
   ABUSE = 'ABUSE' ##An abusive or harassing piece of content
   OFF_TOPIC = 'OFF_TOPIC' ##An irrelevant piece of content
   OUTDATED = 'OUTDATED' ##An outdated piece of content
   DUPLICATE = 'DUPLICATE' ##A duplicated piece of content
   RESOLVED = 'RESOLVED' ##The content has been resolved

class RepositoryAffiliation(Enum):
   OWNER = 'OWNER' ##Repositories that are owned by the authenticated user.
   COLLABORATOR = 'COLLABORATOR' ##Repositories that the user has been added to as a collaborator.
   ORGANIZATION_MEMBER = 'ORGANIZATION_MEMBER' ##Repositories that the user has access to through being a member of an organization. This includes every repository on every team that the user is on.

class RepositoryContributionType(Enum):
   COMMIT = 'COMMIT' ##Created a commit
   ISSUE = 'ISSUE' ##Created an issue
   PULL_REQUEST = 'PULL_REQUEST' ##Created a pull request
   REPOSITORY = 'REPOSITORY' ##Created the repository
   PULL_REQUEST_REVIEW = 'PULL_REQUEST_REVIEW' ##Reviewed a pull request

class RepositoryInteractionLimit(Enum):
   EXISTING_USERS = 'EXISTING_USERS' ##Users that have recently created their account will be unable to interact with the repository.
   CONTRIBUTORS_ONLY = 'CONTRIBUTORS_ONLY' ##Users that have not previously committed to a repository’s default branch will be unable to interact with the repository.
   COLLABORATORS_ONLY = 'COLLABORATORS_ONLY' ##Users that are not collaborators will not be able to interact with the repository.
   NO_LIMIT = 'NO_LIMIT' ##No interaction limits are enabled.

class RepositoryInteractionLimitExpiry(Enum):
   ONE_DAY = 'ONE_DAY' ##The interaction limit will expire after 1 day.
   THREE_DAYS = 'THREE_DAYS' ##The interaction limit will expire after 3 days.
   ONE_WEEK = 'ONE_WEEK' ##The interaction limit will expire after 1 week.
   ONE_MONTH = 'ONE_MONTH' ##The interaction limit will expire after 1 month.
   SIX_MONTHS = 'SIX_MONTHS' ##The interaction limit will expire after 6 months.

class RepositoryInteractionLimitOrigin(Enum):
   REPOSITORY = 'REPOSITORY' ##A limit that is configured at the repository level.
   ORGANIZATION = 'ORGANIZATION' ##A limit that is configured at the organization level.
   USER = 'USER' ##A limit that is configured at the user-wide level.

class RepositoryInvitationOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order repository invitations by creation time

class RepositoryLockReason(Enum):
   MOVING = 'MOVING' ##The repository is locked due to a move.
   BILLING = 'BILLING' ##The repository is locked due to a billing related reason.
   RENAME = 'RENAME' ##The repository is locked due to a rename.
   MIGRATING = 'MIGRATING' ##The repository is locked due to a migration.
   TRADE_RESTRICTION = 'TRADE_RESTRICTION' ##The repository is locked due to a trade controls related reason.

class RepositoryMigrationOrderDirection(Enum):
   ASC = 'ASC' ##Specifies an ascending order for a given `orderBy` argument.
   DESC = 'DESC' ##Specifies a descending order for a given `orderBy` argument.

class RepositoryMigrationOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order mannequins why when they were created.

class RepositoryOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order repositories by creation time
   UPDATED_AT = 'UPDATED_AT' ##Order repositories by update time
   PUSHED_AT = 'PUSHED_AT' ##Order repositories by push time
   NAME = 'NAME' ##Order repositories by name
   STARGAZERS = 'STARGAZERS' ##Order repositories by number of stargazers

class RepositoryPermission(Enum):
   ADMIN = 'ADMIN' ##Can read, clone, and push to this repository. Can also manage issues, pull requests, and repository settings, including adding collaborators
   MAINTAIN = 'MAINTAIN' ##Can read, clone, and push to this repository. They can also manage issues, pull requests, and some repository settings
   WRITE = 'WRITE' ##Can read, clone, and push to this repository. Can also manage issues and pull requests
   TRIAGE = 'TRIAGE' ##Can read and clone this repository. Can also manage issues and pull requests
   READ = 'READ' ##Can read and clone this repository. Can also open and comment on issues and pull requests

class RepositoryPrivacy(Enum):
   PUBLIC = 'PUBLIC' ##Public
   PRIVATE = 'PRIVATE' ##Private

class RepositoryVisibility(Enum):
   PRIVATE = 'PRIVATE' ##The repository is visible only to those with explicit access.
   PUBLIC = 'PUBLIC' ##The repository is visible to everyone.
   INTERNAL = 'INTERNAL' ##The repository is visible only to users in the same business.

class RepositoryVulnerabilityAlertDependencyScope(Enum):
   RUNTIME = 'RUNTIME' ##A dependency that is leveraged during application runtime
   DEVELOPMENT = 'DEVELOPMENT' ##A dependency that is only used in development

class RepositoryVulnerabilityAlertState(Enum):
   OPEN = 'OPEN' ##An alert that is still open.
   FIXED = 'FIXED' ##An alert that has been resolved by a code change.
   DISMISSED = 'DISMISSED' ##An alert that has been manually closed by a user.

class RequestableCheckStatusState(Enum):
   QUEUED = 'QUEUED' ##The check suite or run has been queued.
   IN_PROGRESS = 'IN_PROGRESS' ##The check suite or run is in progress.
   COMPLETED = 'COMPLETED' ##The check suite or run has been completed.
   WAITING = 'WAITING' ##The check suite or run is in waiting state.
   PENDING = 'PENDING' ##The check suite or run is in pending state.

class RoleInOrganization(Enum):
   OWNER = 'OWNER' ##A user with full administrative access to the organization.
   DIRECT_MEMBER = 'DIRECT_MEMBER' ##A user who is a direct member of the organization.
   UNAFFILIATED = 'UNAFFILIATED' ##A user who is unaffiliated with the organization.

class SamlDigestAlgorithm(Enum):
   SHA1 = 'SHA1' ##SHA1
   SHA256 = 'SHA256' ##SHA256
   SHA384 = 'SHA384' ##SHA384
   SHA512 = 'SHA512' ##SHA512

class SamlSignatureAlgorithm(Enum):
   RSA_SHA1 = 'RSA_SHA1' ##RSA-SHA1
   RSA_SHA256 = 'RSA_SHA256' ##RSA-SHA256
   RSA_SHA384 = 'RSA_SHA384' ##RSA-SHA384
   RSA_SHA512 = 'RSA_SHA512' ##RSA-SHA512

class SavedReplyOrderField(Enum):
   UPDATED_AT = 'UPDATED_AT' ##Order saved reply by when they were updated.

class SearchType(Enum):
   ISSUE = 'ISSUE' ##Returns results matching issues in repositories.
   REPOSITORY = 'REPOSITORY' ##Returns results matching repositories.
   USER = 'USER' ##Returns results matching users and organizations on GitHub.
   DISCUSSION = 'DISCUSSION' ##Returns matching discussions in repositories.

class SecurityAdvisoryClassification(Enum):
   GENERAL = 'GENERAL' ##Classification of general advisories.
   MALWARE = 'MALWARE' ##Classification of malware advisories.

class SecurityAdvisoryEcosystem(Enum):
   COMPOSER = 'COMPOSER' ##PHP packages hosted at packagist.org
   ERLANG = 'ERLANG' ##Erlang/Elixir packages hosted at hex.pm
   ACTIONS = 'ACTIONS' ##GitHub Actions
   GO = 'GO' ##Go modules
   MAVEN = 'MAVEN' ##Java artifacts hosted at the Maven central repository
   NPM = 'NPM' ##JavaScript packages hosted at npmjs.com
   NUGET = 'NUGET' ##.NET packages hosted at the NuGet Gallery
   PIP = 'PIP' ##Python packages hosted at PyPI.org
   PUB = 'PUB' ##Dart packages hosted at pub.dev
   RUBYGEMS = 'RUBYGEMS' ##Ruby gems hosted at RubyGems.org
   RUST = 'RUST' ##Rust crates

class SecurityAdvisoryIdentifierType(Enum):
   CVE = 'CVE' ##Common Vulnerabilities and Exposures Identifier.
   GHSA = 'GHSA' ##GitHub Security Advisory ID.

class SecurityAdvisoryOrderField(Enum):
   PUBLISHED_AT = 'PUBLISHED_AT' ##Order advisories by publication time
   UPDATED_AT = 'UPDATED_AT' ##Order advisories by update time

class SecurityAdvisorySeverity(Enum):
   LOW = 'LOW' ##Low.
   MODERATE = 'MODERATE' ##Moderate.
   HIGH = 'HIGH' ##High.
   CRITICAL = 'CRITICAL' ##Critical.

class SecurityVulnerabilityOrderField(Enum):
   UPDATED_AT = 'UPDATED_AT' ##Order vulnerability by update time

class SponsorOrderField(Enum):
   LOGIN = 'LOGIN' ##Order sponsorable entities by login (username).
   RELEVANCE = 'RELEVANCE' ##Order sponsors by their relevance to the viewer.

class SponsorableOrderField(Enum):
   LOGIN = 'LOGIN' ##Order sponsorable entities by login (username).

class SponsorsActivityAction(Enum):
   NEW_SPONSORSHIP = 'NEW_SPONSORSHIP' ##The activity was starting a sponsorship.
   CANCELLED_SPONSORSHIP = 'CANCELLED_SPONSORSHIP' ##The activity was cancelling a sponsorship.
   TIER_CHANGE = 'TIER_CHANGE' ##The activity was changing the sponsorship tier, either directly by the sponsor or by a scheduled/pending change.
   REFUND = 'REFUND' ##The activity was funds being refunded to the sponsor or GitHub.
   PENDING_CHANGE = 'PENDING_CHANGE' ##The activity was scheduling a downgrade or cancellation.
   SPONSOR_MATCH_DISABLED = 'SPONSOR_MATCH_DISABLED' ##The activity was disabling matching for a previously matched sponsorship.

class SponsorsActivityOrderField(Enum):
   TIMESTAMP = 'TIMESTAMP' ##Order activities by when they happened.

class SponsorsActivityPeriod(Enum):
   DAY = 'DAY' ##The previous calendar day.
   WEEK = 'WEEK' ##The previous seven days.
   MONTH = 'MONTH' ##The previous thirty days.
   ALL = 'ALL' ##Don't restrict the activity to any date range, include all activity.

class SponsorsCountryOrRegionCode(Enum):
   AF = 'AF' ##Afghanistan
   AX = 'AX' ##Åland
   AL = 'AL' ##Albania
   DZ = 'DZ' ##Algeria
   AS = 'AS' ##American Samoa
   AD = 'AD' ##Andorra
   AO = 'AO' ##Angola
   AI = 'AI' ##Anguilla
   AQ = 'AQ' ##Antarctica
   AG = 'AG' ##Antigua and Barbuda
   AR = 'AR' ##Argentina
   AM = 'AM' ##Armenia
   AW = 'AW' ##Aruba
   AU = 'AU' ##Australia
   AT = 'AT' ##Austria
   AZ = 'AZ' ##Azerbaijan
   BS = 'BS' ##Bahamas
   BH = 'BH' ##Bahrain
   BD = 'BD' ##Bangladesh
   BB = 'BB' ##Barbados
   BY = 'BY' ##Belarus
   BE = 'BE' ##Belgium
   BZ = 'BZ' ##Belize
   BJ = 'BJ' ##Benin
   BM = 'BM' ##Bermuda
   BT = 'BT' ##Bhutan
   BO = 'BO' ##Bolivia
   BQ = 'BQ' ##Bonaire, Sint Eustatius and Saba
   BA = 'BA' ##Bosnia and Herzegovina
   BW = 'BW' ##Botswana
   BV = 'BV' ##Bouvet Island
   BR = 'BR' ##Brazil
   IO = 'IO' ##British Indian Ocean Territory
   BN = 'BN' ##Brunei Darussalam
   BG = 'BG' ##Bulgaria
   BF = 'BF' ##Burkina Faso
   BI = 'BI' ##Burundi
   KH = 'KH' ##Cambodia
   CM = 'CM' ##Cameroon
   CA = 'CA' ##Canada
   CV = 'CV' ##Cape Verde
   KY = 'KY' ##Cayman Islands
   CF = 'CF' ##Central African Republic
   TD = 'TD' ##Chad
   CL = 'CL' ##Chile
   CN = 'CN' ##China
   CX = 'CX' ##Christmas Island
   CC = 'CC' ##Cocos (Keeling) Islands
   CO = 'CO' ##Colombia
   KM = 'KM' ##Comoros
   CG = 'CG' ##Congo (Brazzaville)
   CD = 'CD' ##Congo (Kinshasa)
   CK = 'CK' ##Cook Islands
   CR = 'CR' ##Costa Rica
   CI = 'CI' ##Côte d'Ivoire
   HR = 'HR' ##Croatia
   CW = 'CW' ##Curaçao
   CY = 'CY' ##Cyprus
   CZ = 'CZ' ##Czech Republic
   DK = 'DK' ##Denmark
   DJ = 'DJ' ##Djibouti
   DM = 'DM' ##Dominica
   DO = 'DO' ##Dominican Republic
   EC = 'EC' ##Ecuador
   EG = 'EG' ##Egypt
   SV = 'SV' ##El Salvador
   GQ = 'GQ' ##Equatorial Guinea
   ER = 'ER' ##Eritrea
   EE = 'EE' ##Estonia
   ET = 'ET' ##Ethiopia
   FK = 'FK' ##Falkland Islands
   FO = 'FO' ##Faroe Islands
   FJ = 'FJ' ##Fiji
   FI = 'FI' ##Finland
   FR = 'FR' ##France
   GF = 'GF' ##French Guiana
   PF = 'PF' ##French Polynesia
   TF = 'TF' ##French Southern Lands
   GA = 'GA' ##Gabon
   GM = 'GM' ##Gambia
   GE = 'GE' ##Georgia
   DE = 'DE' ##Germany
   GH = 'GH' ##Ghana
   GI = 'GI' ##Gibraltar
   GR = 'GR' ##Greece
   GL = 'GL' ##Greenland
   GD = 'GD' ##Grenada
   GP = 'GP' ##Guadeloupe
   GU = 'GU' ##Guam
   GT = 'GT' ##Guatemala
   GG = 'GG' ##Guernsey
   GN = 'GN' ##Guinea
   GW = 'GW' ##Guinea-Bissau
   GY = 'GY' ##Guyana
   HT = 'HT' ##Haiti
   HM = 'HM' ##Heard and McDonald Islands
   HN = 'HN' ##Honduras
   HK = 'HK' ##Hong Kong
   HU = 'HU' ##Hungary
   IS = 'IS' ##Iceland
   IN = 'IN' ##India
   ID = 'ID' ##Indonesia
   IR = 'IR' ##Iran
   IQ = 'IQ' ##Iraq
   IE = 'IE' ##Ireland
   IM = 'IM' ##Isle of Man
   IL = 'IL' ##Israel
   IT = 'IT' ##Italy
   JM = 'JM' ##Jamaica
   JP = 'JP' ##Japan
   JE = 'JE' ##Jersey
   JO = 'JO' ##Jordan
   KZ = 'KZ' ##Kazakhstan
   KE = 'KE' ##Kenya
   KI = 'KI' ##Kiribati
   KR = 'KR' ##Korea, South
   KW = 'KW' ##Kuwait
   KG = 'KG' ##Kyrgyzstan
   LA = 'LA' ##Laos
   LV = 'LV' ##Latvia
   LB = 'LB' ##Lebanon
   LS = 'LS' ##Lesotho
   LR = 'LR' ##Liberia
   LY = 'LY' ##Libya
   LI = 'LI' ##Liechtenstein
   LT = 'LT' ##Lithuania
   LU = 'LU' ##Luxembourg
   MO = 'MO' ##Macau
   MK = 'MK' ##Macedonia
   MG = 'MG' ##Madagascar
   MW = 'MW' ##Malawi
   MY = 'MY' ##Malaysia
   MV = 'MV' ##Maldives
   ML = 'ML' ##Mali
   MT = 'MT' ##Malta
   MH = 'MH' ##Marshall Islands
   MQ = 'MQ' ##Martinique
   MR = 'MR' ##Mauritania
   MU = 'MU' ##Mauritius
   YT = 'YT' ##Mayotte
   MX = 'MX' ##Mexico
   FM = 'FM' ##Micronesia
   MD = 'MD' ##Moldova
   MC = 'MC' ##Monaco
   MN = 'MN' ##Mongolia
   ME = 'ME' ##Montenegro
   MS = 'MS' ##Montserrat
   MA = 'MA' ##Morocco
   MZ = 'MZ' ##Mozambique
   MM = 'MM' ##Myanmar
   NA = 'NA' ##Namibia
   NR = 'NR' ##Nauru
   NP = 'NP' ##Nepal
   NL = 'NL' ##Netherlands
   NC = 'NC' ##New Caledonia
   NZ = 'NZ' ##New Zealand
   NI = 'NI' ##Nicaragua
   NE = 'NE' ##Niger
   NG = 'NG' ##Nigeria
   NU = 'NU' ##Niue
   NF = 'NF' ##Norfolk Island
   MP = 'MP' ##Northern Mariana Islands
   NO = 'NO' ##Norway
   OM = 'OM' ##Oman
   PK = 'PK' ##Pakistan
   PW = 'PW' ##Palau
   PS = 'PS' ##Palestine
   PA = 'PA' ##Panama
   PG = 'PG' ##Papua New Guinea
   PY = 'PY' ##Paraguay
   PE = 'PE' ##Peru
   PH = 'PH' ##Philippines
   PN = 'PN' ##Pitcairn
   PL = 'PL' ##Poland
   PT = 'PT' ##Portugal
   PR = 'PR' ##Puerto Rico
   QA = 'QA' ##Qatar
   RE = 'RE' ##Reunion
   RO = 'RO' ##Romania
   RU = 'RU' ##Russian Federation
   RW = 'RW' ##Rwanda
   BL = 'BL' ##Saint Barthélemy
   SH = 'SH' ##Saint Helena
   KN = 'KN' ##Saint Kitts and Nevis
   LC = 'LC' ##Saint Lucia
   MF = 'MF' ##Saint Martin (French part)
   PM = 'PM' ##Saint Pierre and Miquelon
   VC = 'VC' ##Saint Vincent and the Grenadines
   WS = 'WS' ##Samoa
   SM = 'SM' ##San Marino
   ST = 'ST' ##Sao Tome and Principe
   SA = 'SA' ##Saudi Arabia
   SN = 'SN' ##Senegal
   RS = 'RS' ##Serbia
   SC = 'SC' ##Seychelles
   SL = 'SL' ##Sierra Leone
   SG = 'SG' ##Singapore
   SX = 'SX' ##Sint Maarten (Dutch part)
   SK = 'SK' ##Slovakia
   SI = 'SI' ##Slovenia
   SB = 'SB' ##Solomon Islands
   SO = 'SO' ##Somalia
   ZA = 'ZA' ##South Africa
   GS = 'GS' ##South Georgia and South Sandwich Islands
   SS = 'SS' ##South Sudan
   ES = 'ES' ##Spain
   LK = 'LK' ##Sri Lanka
   SD = 'SD' ##Sudan
   SR = 'SR' ##Suriname
   SJ = 'SJ' ##Svalbard and Jan Mayen Islands
   SZ = 'SZ' ##Swaziland
   SE = 'SE' ##Sweden
   CH = 'CH' ##Switzerland
   TW = 'TW' ##Taiwan
   TJ = 'TJ' ##Tajikistan
   TZ = 'TZ' ##Tanzania
   TH = 'TH' ##Thailand
   TL = 'TL' ##Timor-Leste
   TG = 'TG' ##Togo
   TK = 'TK' ##Tokelau
   TO = 'TO' ##Tonga
   TT = 'TT' ##Trinidad and Tobago
   TN = 'TN' ##Tunisia
   TR = 'TR' ##Turkey
   TM = 'TM' ##Turkmenistan
   TC = 'TC' ##Turks and Caicos Islands
   TV = 'TV' ##Tuvalu
   UG = 'UG' ##Uganda
   UA = 'UA' ##Ukraine
   AE = 'AE' ##United Arab Emirates
   GB = 'GB' ##United Kingdom
   UM = 'UM' ##United States Minor Outlying Islands
   US = 'US' ##United States of America
   UY = 'UY' ##Uruguay
   UZ = 'UZ' ##Uzbekistan
   VU = 'VU' ##Vanuatu
   VA = 'VA' ##Vatican City
   VE = 'VE' ##Venezuela
   VN = 'VN' ##Vietnam
   VG = 'VG' ##Virgin Islands, British
   VI = 'VI' ##Virgin Islands, U.S.
   WF = 'WF' ##Wallis and Futuna Islands
   EH = 'EH' ##Western Sahara
   YE = 'YE' ##Yemen
   ZM = 'ZM' ##Zambia
   ZW = 'ZW' ##Zimbabwe

class SponsorsGoalKind(Enum):
   TOTAL_SPONSORS_COUNT = 'TOTAL_SPONSORS_COUNT' ##The goal is about reaching a certain number of sponsors.
   MONTHLY_SPONSORSHIP_AMOUNT = 'MONTHLY_SPONSORSHIP_AMOUNT' ##The goal is about getting a certain amount in USD from sponsorships each month.

class SponsorsListingFeaturedItemFeatureableType(Enum):
   REPOSITORY = 'REPOSITORY' ##A repository owned by the user or organization with the GitHub Sponsors profile.
   USER = 'USER' ##A user who belongs to the organization with the GitHub Sponsors profile.

class SponsorsTierOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order tiers by creation time.
   MONTHLY_PRICE_IN_CENTS = 'MONTHLY_PRICE_IN_CENTS' ##Order tiers by their monthly price in cents

class SponsorshipNewsletterOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order sponsorship newsletters by when they were created.

class SponsorshipOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order sponsorship by creation time.

class SponsorshipPrivacy(Enum):
   PUBLIC = 'PUBLIC' ##Public
   PRIVATE = 'PRIVATE' ##Private

class SquashMergeCommitMessage(Enum):
   PR_BODY = 'PR_BODY' ##Default to the pull request's body.
   COMMIT_MESSAGES = 'COMMIT_MESSAGES' ##Default to the branch's commit messages.
   BLANK = 'BLANK' ##Default to a blank commit message.

class SquashMergeCommitTitle(Enum):
   PR_TITLE = 'PR_TITLE' ##Default to the pull request's title.
   COMMIT_OR_PR_TITLE = 'COMMIT_OR_PR_TITLE' ##Default to the commit's title (if only one commit) or the pull request's title (when more than one commit).

class StarOrderField(Enum):
   STARRED_AT = 'STARRED_AT' ##Allows ordering a list of stars by when they were created.

class StatusState(Enum):
   EXPECTED = 'EXPECTED' ##Status is expected.
   ERROR = 'ERROR' ##Status is errored.
   FAILURE = 'FAILURE' ##Status is failing.
   PENDING = 'PENDING' ##Status is pending.
   SUCCESS = 'SUCCESS' ##Status is successful.

class SubscriptionState(Enum):
   UNSUBSCRIBED = 'UNSUBSCRIBED' ##The User is only notified when participating or @mentioned.
   SUBSCRIBED = 'SUBSCRIBED' ##The User is notified of all conversations.
   IGNORED = 'IGNORED' ##The User is never notified.

class TeamDiscussionCommentOrderField(Enum):
   NUMBER = 'NUMBER' ##Allows sequential ordering of team discussion comments (which is equivalent to chronological ordering).

class TeamDiscussionOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Allows chronological ordering of team discussions.

class TeamMemberOrderField(Enum):
   LOGIN = 'LOGIN' ##Order team members by login
   CREATED_AT = 'CREATED_AT' ##Order team members by creation time

class TeamMemberRole(Enum):
   MAINTAINER = 'MAINTAINER' ##A team maintainer has permission to add and remove team members.
   MEMBER = 'MEMBER' ##A team member has no administrative permissions on the team.

class TeamMembershipType(Enum):
   IMMEDIATE = 'IMMEDIATE' ##Includes only immediate members of the team.
   CHILD_TEAM = 'CHILD_TEAM' ##Includes only child team members for the team.
   ALL = 'ALL' ##Includes immediate and child team members for the team.

class TeamOrderField(Enum):
   NAME = 'NAME' ##Allows ordering a list of teams by name.

class TeamPrivacy(Enum):
   SECRET = 'SECRET' ##A secret team can only be seen by its members.
   VISIBLE = 'VISIBLE' ##A visible team can be seen and @mentioned by every member of the organization.

class TeamRepositoryOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order repositories by creation time
   UPDATED_AT = 'UPDATED_AT' ##Order repositories by update time
   PUSHED_AT = 'PUSHED_AT' ##Order repositories by push time
   NAME = 'NAME' ##Order repositories by name
   PERMISSION = 'PERMISSION' ##Order repositories by permission
   STARGAZERS = 'STARGAZERS' ##Order repositories by number of stargazers

class TeamRole(Enum):
   ADMIN = 'ADMIN' ##User has admin rights on the team.
   MEMBER = 'MEMBER' ##User is a member of the team.

class TopicSuggestionDeclineReason(Enum):
   NOT_RELEVANT = 'NOT_RELEVANT' ##The suggested topic is not relevant to the repository.
   TOO_SPECIFIC = 'TOO_SPECIFIC' ##The suggested topic is too specific for the repository (e.g. #ruby-on-rails-version-4-2-1).
   PERSONAL_PREFERENCE = 'PERSONAL_PREFERENCE' ##The viewer does not like the suggested topic.
   TOO_GENERAL = 'TOO_GENERAL' ##The suggested topic is too general for the repository.

class TrackedIssueStates(Enum):
   OPEN = 'OPEN' ##The tracked issue is open
   CLOSED = 'CLOSED' ##The tracked issue is closed

class UserBlockDuration(Enum):
   ONE_DAY = 'ONE_DAY' ##The user was blocked for 1 day
   THREE_DAYS = 'THREE_DAYS' ##The user was blocked for 3 days
   ONE_WEEK = 'ONE_WEEK' ##The user was blocked for 7 days
   ONE_MONTH = 'ONE_MONTH' ##The user was blocked for 30 days
   PERMANENT = 'PERMANENT' ##The user was blocked permanently

class UserStatusOrderField(Enum):
   UPDATED_AT = 'UPDATED_AT' ##Order user statuses by when they were updated.

class VerifiableDomainOrderField(Enum):
   DOMAIN = 'DOMAIN' ##Order verifiable domains by the domain name.
   CREATED_AT = 'CREATED_AT' ##Order verifiable domains by their creation date.

class WorkflowRunOrderField(Enum):
   CREATED_AT = 'CREATED_AT' ##Order workflow runs by most recently created

