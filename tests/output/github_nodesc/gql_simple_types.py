from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class OXMQI_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class KKNZP_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class OCZPK_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class SILSD_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class BHHDH_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class ARSHS_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class CTFUG_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class DVNDG_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class CTCAJ_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class LQXXH_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class VQVKQ_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class AGOCV_organizationVerifiedDomainEmails_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: strArgs



class VFQRL_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class GROVZ_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: boolArgs



class MLBIQ_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class OZZSE_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class TKSSF_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class KXELZ_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class KTKXF_text_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      truncate: int

   _args: strArgs



class TOYEM_totalRepositoryContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool

   _args: intArgs



class RMZIL_totalRepositoriesWithContributedPullRequests_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class UALFL_totalRepositoriesWithContributedIssues_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class GNBHJ_totalPullRequestContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class TTIHZ_totalIssueContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class JVVIJ_isRequired_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class LNEYZ_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class QBHRC_isRequired_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class LHKDV_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class QNEME_viewerMergeHeadlineText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      mergeType: PullRequestMergeMethod

   _args: strArgs



class ULLSC_viewerMergeBodyText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      mergeType: PullRequestMergeMethod

   _args: strArgs



class TAJTM_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class GKNMZ_trackedIssuesCount_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      states: list[TrackedIssueStates]

   _args: intArgs



class LRQST_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class GCHYR_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class WQJYH_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class OHFBC_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class ZDQQL_isRequired_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class WorkflowRunOrder(GQLObject):
   field: WorkflowRunOrderField
   direction: OrderDirection

class VerifyVerifiableDomainInput(GQLObject):
   id: ID
   clientMutationId: str

class UserStatusOrder(GQLObject):
   field: UserStatusOrderField
   direction: OrderDirection

class UpdateTopicsInput(GQLObject):
   repositoryId: ID
   topicNames: NonNull_list[str]
   clientMutationId: str

class UpdateTeamDiscussionInput(GQLObject):
   id: ID
   title: str
   body: str
   bodyVersion: str
   pinned: bool
   clientMutationId: str

class UpdateSubscriptionInput(GQLObject):
   subscribableId: ID
   state: SubscriptionState
   clientMutationId: str

class UpdateRepositoryWebCommitSignoffSettingInput(GQLObject):
   repositoryId: ID
   webCommitSignoffRequired: bool
   clientMutationId: str

class UpdateRefInput(GQLObject):
   refId: ID
   oid: GitObjectID
   force: bool
   clientMutationId: str

class UpdatePullRequestReviewCommentInput(GQLObject):
   pullRequestReviewCommentId: ID
   body: str
   clientMutationId: str

class UpdatePullRequestBranchInput(GQLObject):
   pullRequestId: ID
   expectedHeadOid: GitObjectID
   clientMutationId: str

class UpdateProjectV2Input(GQLObject):
   projectId: ID
   title: str
   shortDescription: str
   readme: str
   closed: bool
   public: bool
   clientMutationId: str

class UpdateProjectInput(GQLObject):
   projectId: ID
   name: str
   body: str
   state: ProjectState
   public: bool
   clientMutationId: str

class UpdateProjectCardInput(GQLObject):
   projectCardId: ID
   isArchived: bool
   note: str
   clientMutationId: str

class UpdateOrganizationAllowPrivateRepositoryForkingSettingInput(GQLObject):
   organizationId: ID
   forkingEnabled: bool
   clientMutationId: str

class UpdateIssueInput(GQLObject):
   id: ID
   title: str
   body: str
   assigneeIds: list[ID]
   milestoneId: ID
   labelIds: list[ID]
   state: IssueState
   projectIds: list[ID]
   clientMutationId: str

class UpdateIpAllowListForInstalledAppsEnabledSettingInput(GQLObject):
   ownerId: ID
   settingValue: IpAllowListForInstalledAppsEnabledSettingValue
   clientMutationId: str

class UpdateIpAllowListEnabledSettingInput(GQLObject):
   ownerId: ID
   settingValue: IpAllowListEnabledSettingValue
   clientMutationId: str

class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledSettingValue
   clientMutationId: str

class UpdateEnterpriseRepositoryProjectsSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseOwnerOrganizationRolePayload(GQLObject):
   clientMutationId: str
   message: str

class UpdateEnterpriseOrganizationProjectsSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanDeleteIssuesSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   policyValue: EnterpriseAllowPrivateRepositoryForkingPolicyValue
   clientMutationId: str

class UpdateEnterpriseAdministratorRoleInput(GQLObject):
   enterpriseId: ID
   login: str
   role: EnterpriseAdministratorRole
   clientMutationId: str

class UpdateDiscussionCommentInput(GQLObject):
   commentId: ID
   body: str
   clientMutationId: str

class Updatable(GQLObject):
   viewerCanUpdate: bool

class UnpinIssueInput(GQLObject):
   issueId: ID
   clientMutationId: str

class UnmarkIssueAsDuplicateInput(GQLObject):
   duplicateId: ID
   canonicalId: ID
   clientMutationId: str

class UnmarkDiscussionCommentAsAnswerInput(GQLObject):
   id: ID
   clientMutationId: str

class UnlinkRepositoryFromProjectInput(GQLObject):
   projectId: ID
   repositoryId: ID
   clientMutationId: str

class UnlinkProjectV2FromRepositoryInput(GQLObject):
   projectId: ID
   repositoryId: ID
   clientMutationId: str

class UnfollowUserInput(GQLObject):
   userId: ID
   clientMutationId: str

class UnarchiveRepositoryInput(GQLObject):
   repositoryId: ID
   clientMutationId: str

class TransferIssueInput(GQLObject):
   issueId: ID
   repositoryId: ID
   createLabelsIfMissing: bool
   clientMutationId: str

class TextMatchHighlight(GQLObject):
   beginIndice: int
   endIndice: int
   text: str

class TeamOrder(GQLObject):
   field: TeamOrderField
   direction: OrderDirection

class TeamDiscussionOrder(GQLObject):
   field: TeamDiscussionOrderField
   direction: OrderDirection

class Subscribable(GQLObject):
   id: ID
   viewerCanSubscribe: bool
   viewerSubscription: SubscriptionState

class SubmitPullRequestReviewInput(GQLObject):
   pullRequestId: ID
   pullRequestReviewId: ID
   event: PullRequestReviewEvent
   body: str
   clientMutationId: str

class StartRepositoryMigrationInput(GQLObject):
   sourceId: ID
   ownerId: ID
   sourceRepositoryUrl: URI
   repositoryName: str
   continueOnError: bool
   gitArchiveUrl: str
   metadataArchiveUrl: str
   accessToken: str
   githubPat: str
   skipReleases: bool
   targetRepoVisibility: str
   lockSource: bool
   clientMutationId: str

class StarOrder(GQLObject):
   field: StarOrderField
   direction: OrderDirection

class SponsorshipNewsletterOrder(GQLObject):
   field: SponsorshipNewsletterOrderField
   direction: OrderDirection

class SponsorsGoal(GQLObject):
   description: str
   kind: SponsorsGoalKind
   percentComplete: int
   targetValue: int
   title: str

class SponsorableOrder(GQLObject):
   field: SponsorableOrderField
   direction: OrderDirection

class SetUserInteractionLimitInput(GQLObject):
   userId: ID
   limit: RepositoryInteractionLimit
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SetOrganizationInteractionLimitInput(GQLObject):
   organizationId: ID
   limit: RepositoryInteractionLimit
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SecurityVulnerabilityOrder(GQLObject):
   field: SecurityVulnerabilityOrderField
   direction: OrderDirection

class SecurityAdvisoryPackageVersion(GQLObject):
   identifier: str

class SecurityAdvisoryOrder(GQLObject):
   field: SecurityAdvisoryOrderField
   direction: OrderDirection

class SecurityAdvisoryIdentifier(GQLObject):
   type: str
   value: str

class RevokeMigratorRolePayload(GQLObject):
   clientMutationId: str
   success: bool

class RevokeEnterpriseOrganizationsMigratorRoleInput(GQLObject):
   enterpriseId: ID
   login: str
   clientMutationId: str

class RevertPullRequestInput(GQLObject):
   pullRequestId: ID
   title: str
   body: str
   draft: bool
   clientMutationId: str

class ResolveReviewThreadInput(GQLObject):
   threadId: ID
   clientMutationId: str

class RequiredStatusCheckInput(GQLObject):
   context: str
   appId: ID

class RequirableByPullRequest(GQLObject):
   isRequired: ZDQQL_isRequired_Field

class RepositoryOrder(GQLObject):
   field: RepositoryOrderField
   direction: OrderDirection

class RepositoryInvitationOrder(GQLObject):
   field: RepositoryInvitationOrderField
   direction: OrderDirection

class RepositoryContactLink(GQLObject):
   about: str
   name: str
   url: URI

class ReopenPullRequestInput(GQLObject):
   pullRequestId: ID
   clientMutationId: str

class RemoveUpvoteInput(GQLObject):
   subjectId: ID
   clientMutationId: str

class RemoveReactionInput(GQLObject):
   subjectId: ID
   content: ReactionContent
   clientMutationId: str

class RemoveLabelsFromLabelableInput(GQLObject):
   labelableId: ID
   labelIds: NonNull_list[ID]
   clientMutationId: str

class RemoveEnterpriseSupportEntitlementInput(GQLObject):
   enterpriseId: ID
   login: str
   clientMutationId: str

class RemoveEnterpriseMemberInput(GQLObject):
   enterpriseId: ID
   userId: ID
   clientMutationId: str

class RemoveEnterpriseAdminInput(GQLObject):
   enterpriseId: ID
   login: str
   clientMutationId: str

class ReleaseOrder(GQLObject):
   field: ReleaseOrderField
   direction: OrderDirection

class RegenerateVerifiableDomainTokenPayload(GQLObject):
   clientMutationId: str
   verificationToken: str

class RegenerateEnterpriseIdentityProviderRecoveryCodesInput(GQLObject):
   enterpriseId: ID
   clientMutationId: str

class RefOrder(GQLObject):
   field: RefOrderField
   direction: OrderDirection

class RateLimit(GQLObject):
   cost: int
   limit: int
   nodeCount: int
   remaining: int
   resetAt: DateTime
   used: int

class PullRequestChangedFile(GQLObject):
   additions: int
   changeType: PatchStatus
   deletions: int
   path: str
   viewerViewedState: FileViewedState

class PublicKey(GQLObject):
   accessedAt: DateTime
   createdAt: DateTime
   fingerprint: str
   id: ID
   isReadOnly: bool
   key: str
   updatedAt: DateTime

class ProjectV2SingleSelectFieldOption(GQLObject):
   id: str
   name: str
   nameHTML: str

class ProjectV2IterationFieldIteration(GQLObject):
   duration: int
   id: str
   startDate: Date
   title: str
   titleHTML: str

class ProjectV2ItemFieldValueOrder(GQLObject):
   field: ProjectV2ItemFieldValueOrderField
   direction: OrderDirection

class ProjectV2FieldValue(GQLObject):
   text: str
   number: float
   date: Date
   singleSelectOptionId: str
   iterationId: str

class ProjectProgress(GQLObject):
   doneCount: int
   donePercentage: float
   enabled: bool
   inProgressCount: int
   inProgressPercentage: float
   todoCount: int
   todoPercentage: float

class PinIssueInput(GQLObject):
   issueId: ID
   clientMutationId: str

class PackageVersionStatistics(GQLObject):
   downloadsTotalCount: int

class PackageStatistics(GQLObject):
   downloadsTotalCount: int

class PackageFileOrder(GQLObject):
   field: PackageFileOrderField
   direction: OrderDirection

class OrganizationMigration(GQLObject):
   createdAt: DateTime
   databaseId: str
   failureReason: str
   id: ID
   remainingRepositoriesCount: int
   sourceOrgName: str
   sourceOrgUrl: URI
   state: OrganizationMigrationState
   targetOrgName: str
   totalRepositoriesCount: int

class OauthApplicationAuditEntryData(GQLObject):
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI

class MoveProjectColumnInput(GQLObject):
   columnId: ID
   afterColumnId: ID
   clientMutationId: str

class MinimizeCommentInput(GQLObject):
   subjectId: ID
   classifier: ReportedContentClassifiers
   clientMutationId: str

class MilestoneOrder(GQLObject):
   field: MilestoneOrderField
   direction: OrderDirection

class MergePullRequestInput(GQLObject):
   pullRequestId: ID
   commitHeadline: str
   commitBody: str
   expectedHeadOid: GitObjectID
   mergeMethod: PullRequestMergeMethod
   authorEmail: str
   clientMutationId: str

class MarketplaceCategory(GQLObject):
   description: str
   howItWorks: str
   id: ID
   name: str
   primaryListingCount: int
   resourcePath: URI
   secondaryListingCount: int
   slug: str
   url: URI

class MarkFileAsViewedInput(GQLObject):
   pullRequestId: ID
   path: str
   clientMutationId: str

class MannequinOrder(GQLObject):
   field: MannequinOrderField
   direction: OrderDirection

class LockLockableInput(GQLObject):
   lockableId: ID
   lockReason: LockReason
   clientMutationId: str

class LinkProjectV2ToTeamInput(GQLObject):
   projectId: ID
   teamId: ID
   clientMutationId: str

class LicenseRule(GQLObject):
   description: str
   key: str
   label: str

class Language(GQLObject):
   color: str
   id: ID
   name: str

class IssueTemplate(GQLObject):
   about: str
   body: str
   filename: str
   name: str
   title: str

class IssueFilters(GQLObject):
   assignee: str
   createdBy: str
   labels: list[str]
   mentioned: str
   milestone: str
   milestoneNumber: str
   since: DateTime
   states: list[IssueState]
   viewerSubscribed: bool

class IpAllowListEntryOrder(GQLObject):
   field: IpAllowListEntryOrderField
   direction: OrderDirection

class HovercardContext(GQLObject):
   message: str
   octicon: str

class GrantMigratorRoleInput(GQLObject):
   organizationId: ID
   actor: str
   actorType: ActorType
   clientMutationId: str

class GitHubMetadata(GQLObject):
   gitHubServicesSha: GitObjectID
   gitIpAddresses: list[str]
   hookIpAddresses: list[str]
   importerIpAddresses: list[str]
   isPasswordAuthenticationVerifiable: bool
   pagesIpAddresses: list[str]

class GenericHovercardContext(GQLObject):
   message: str
   octicon: str

class FollowUserInput(GQLObject):
   userId: ID
   clientMutationId: str

class FileDeletion(GQLObject):
   path: str

class ExternalIdentityAttribute(GQLObject):
   metadata: str
   name: str
   value: str

class EnterpriseServerUserAccountOrder(GQLObject):
   field: EnterpriseServerUserAccountOrderField
   direction: OrderDirection

class EnterpriseServerInstallationOrder(GQLObject):
   field: EnterpriseServerInstallationOrderField
   direction: OrderDirection

class EnterpriseMemberOrder(GQLObject):
   field: EnterpriseMemberOrderField
   direction: OrderDirection

class EnterpriseAuditEntryData(GQLObject):
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI

class EnablePullRequestAutoMergeInput(GQLObject):
   pullRequestId: ID
   commitHeadline: str
   commitBody: str
   mergeMethod: PullRequestMergeMethod
   authorEmail: str
   clientMutationId: str

class DraftPullRequestReviewComment(GQLObject):
   path: str
   position: int
   body: str

class DismissPullRequestReviewInput(GQLObject):
   pullRequestReviewId: ID
   message: str
   clientMutationId: str

class DiscussionOrder(GQLObject):
   field: DiscussionOrderField
   direction: OrderDirection

class DeploymentOrder(GQLObject):
   field: DeploymentOrderField
   direction: OrderDirection

class DependabotUpdateError(GQLObject):
   body: str
   errorType: str
   title: str

class DeleteTeamDiscussionPayload(GQLObject):
   clientMutationId: str

class DeleteTeamDiscussionCommentPayload(GQLObject):
   clientMutationId: str

class DeleteRefPayload(GQLObject):
   clientMutationId: str

class DeletePullRequestReviewInput(GQLObject):
   pullRequestReviewId: ID
   clientMutationId: str

class DeleteProjectV2ItemPayload(GQLObject):
   clientMutationId: str
   deletedItemId: ID

class DeleteProjectInput(GQLObject):
   projectId: ID
   clientMutationId: str

class DeleteProjectCardInput(GQLObject):
   cardId: ID
   clientMutationId: str

class DeleteIssueInput(GQLObject):
   issueId: ID
   clientMutationId: str

class DeleteIssueCommentInput(GQLObject):
   id: ID
   clientMutationId: str

class DeleteEnvironmentPayload(GQLObject):
   clientMutationId: str

class DeleteDiscussionInput(GQLObject):
   id: ID
   clientMutationId: str

class DeleteDeploymentPayload(GQLObject):
   clientMutationId: str

class DeleteBranchProtectionRulePayload(GQLObject):
   clientMutationId: str

class Deletable(GQLObject):
   viewerCanDelete: bool

class CreateTeamDiscussionInput(GQLObject):
   teamId: ID
   title: str
   body: str
   private: bool
   clientMutationId: str

class CreateSponsorshipInput(GQLObject):
   sponsorId: ID
   sponsorLogin: str
   sponsorableId: ID
   sponsorableLogin: str
   tierId: ID
   amount: int
   isRecurring: bool
   receiveEmails: bool
   privacyLevel: SponsorshipPrivacy
   clientMutationId: str

class CreateSponsorsListingInput(GQLObject):
   sponsorableLogin: str
   fiscalHostLogin: str
   fiscallyHostedProjectProfileUrl: str
   billingCountryOrRegionCode: SponsorsCountryOrRegionCode
   residenceCountryOrRegionCode: SponsorsCountryOrRegionCode
   contactEmail: str
   fullDescription: str
   clientMutationId: str

class CreateRefInput(GQLObject):
   repositoryId: ID
   name: str
   oid: GitObjectID
   clientMutationId: str

class CreateProjectV2Input(GQLObject):
   ownerId: ID
   title: str
   repositoryId: ID
   teamId: ID
   clientMutationId: str

class CreateMigrationSourceInput(GQLObject):
   name: str
   url: str
   accessToken: str
   type: MigrationSourceType
   ownerId: ID
   githubPat: str
   clientMutationId: str

class CreateIssueInput(GQLObject):
   repositoryId: ID
   title: str
   body: str
   assigneeIds: list[ID]
   milestoneId: ID
   labelIds: list[ID]
   projectIds: list[ID]
   issueTemplate: str
   clientMutationId: str

class CreateEnvironmentInput(GQLObject):
   repositoryId: ID
   name: str
   clientMutationId: str

class CreateDiscussionInput(GQLObject):
   repositoryId: ID
   title: str
   body: str
   categoryId: ID
   clientMutationId: str

class CreateAttributionInvitationInput(GQLObject):
   ownerId: ID
   sourceId: ID
   targetId: ID
   clientMutationId: str

class ConvertProjectCardNoteToIssueInput(GQLObject):
   projectCardId: ID
   repositoryId: ID
   title: str
   body: str
   clientMutationId: str

class ContributionCalendarMonth(GQLObject):
   firstDay: Date
   name: str
   totalWeeks: int
   year: int

class CommittableBranch(GQLObject):
   id: ID
   repositoryNameWithOwner: str
   branchName: str

class CommitContributionOrder(GQLObject):
   field: CommitContributionOrderField
   direction: OrderDirection

class CodeOfConduct(GQLObject):
   body: str
   id: ID
   key: str
   name: str
   resourcePath: URI
   url: URI

class CloseIssueInput(GQLObject):
   issueId: ID
   stateReason: IssueClosedStateReason
   clientMutationId: str

class CloneTemplateRepositoryInput(GQLObject):
   repositoryId: ID
   name: str
   ownerId: ID
   description: str
   visibility: RepositoryVisibility
   includeAllBranches: bool
   clientMutationId: str

class ClearProjectV2ItemFieldValueInput(GQLObject):
   projectId: ID
   itemId: ID
   fieldId: ID
   clientMutationId: str

class CheckSuiteFilter(GQLObject):
   appId: int
   checkName: str

class CheckStep(GQLObject):
   completedAt: DateTime
   conclusion: CheckConclusionState
   externalId: str
   name: str
   number: int
   secondsToCompletion: int
   startedAt: DateTime
   status: CheckStatusState

class CheckRunOutputImage(GQLObject):
   alt: str
   imageUrl: URI
   caption: str

class CheckRunAction(GQLObject):
   label: str
   description: str
   identifier: str

class CheckAnnotationPosition(GQLObject):
   column: int
   line: int

class CancelSponsorshipInput(GQLObject):
   sponsorId: ID
   sponsorLogin: str
   sponsorableId: ID
   sponsorableLogin: str
   clientMutationId: str

class CWE(GQLObject):
   cweId: str
   description: str
   id: ID
   name: str

class FKOKY_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class AuditLogOrder(GQLObject):
   field: AuditLogOrderField
   direction: OrderDirection

class ArchiveProjectV2ItemInput(GQLObject):
   projectId: ID
   itemId: ID
   clientMutationId: str

class ApproveDeploymentsInput(GQLObject):
   workflowRunId: ID
   environmentIds: NonNull_list[ID]
   comment: str
   clientMutationId: str

class AddUpvoteInput(GQLObject):
   subjectId: ID
   clientMutationId: str

class AddReactionInput(GQLObject):
   subjectId: ID
   content: ReactionContent
   clientMutationId: str

class AddPullRequestReviewCommentInput(GQLObject):
   pullRequestId: ID
   pullRequestReviewId: ID
   commitOID: GitObjectID
   body: str
   path: str
   position: int
   inReplyTo: ID
   clientMutationId: str

class AddProjectV2DraftIssueInput(GQLObject):
   projectId: ID
   title: str
   body: str
   assigneeIds: list[ID]
   clientMutationId: str

class AddProjectCardInput(GQLObject):
   projectColumnId: ID
   contentId: ID
   note: str
   clientMutationId: str

class AddEnterpriseSupportEntitlementPayload(GQLObject):
   clientMutationId: str
   message: str

class AddEnterpriseOrganizationMemberInput(GQLObject):
   enterpriseId: ID
   organizationId: ID
   userIds: NonNull_list[ID]
   role: OrganizationMemberRole
   clientMutationId: str

class AddDiscussionCommentInput(GQLObject):
   discussionId: ID
   replyToId: ID
   body: str
   clientMutationId: str

class AddAssigneesToAssignableInput(GQLObject):
   assignableId: ID
   assigneeIds: NonNull_list[ID]
   clientMutationId: str

class MJJUJ_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class AcceptTopicSuggestionInput(GQLObject):
   repositoryId: ID
   name: str
   clientMutationId: str

class AbortQueuedMigrationsPayload(GQLObject):
   clientMutationId: str
   success: bool
