from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class KISEW_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class KXYTK_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class POFHR_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class HQOKI_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class KFLRK_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class WAVPH_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class QUYEZ_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class ICQLW_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class WSHCQ_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class VEATV_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class HJMVV_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class YGKUA_organizationVerifiedDomainEmails_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: strArgs



class RLUJY_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class XNNAF_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: boolArgs



class FVDOD_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class KNSCJ_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class FZWIV_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class VYVTZ_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class ZKQVF_text_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      truncate: int

   _args: strArgs



class RESLG_totalRepositoryContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool

   _args: intArgs



class CLSWT_totalRepositoriesWithContributedPullRequests_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class AZLBL_totalRepositoriesWithContributedIssues_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class TDTJO_totalPullRequestContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class QGEPN_totalIssueContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class IKYAO_isRequired_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class QXSLW_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class ZJXHH_isRequired_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class NOIEG_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class PMXXT_viewerMergeHeadlineText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      mergeType: PullRequestMergeMethod

   _args: strArgs



class SCKMP_viewerMergeBodyText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      mergeType: PullRequestMergeMethod

   _args: strArgs



class GVDQD_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class JQEWT_trackedIssuesCount_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      states: list[TrackedIssueStates]

   _args: intArgs



class ADGTL_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class AKNUG_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class VNUPO_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class VSLJM_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



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
   topicNames: list[str]
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
   updateMethod: PullRequestBranchUpdateMethod
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

class UpdateParameters(GQLObject):
   updateAllowsFetchAndMerge: bool

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

class UnmarkProjectV2AsTemplateInput(GQLObject):
   projectId: ID
   clientMutationId: str

class UnmarkFileAsViewedInput(GQLObject):
   pullRequestId: ID
   path: str
   clientMutationId: str

class UnlockLockableInput(GQLObject):
   lockableId: ID
   clientMutationId: str

class UnlinkProjectV2FromTeamInput(GQLObject):
   projectId: ID
   teamId: ID
   clientMutationId: str

class UniformResourceLocatable(GQLObject):
   resourcePath: URI
   url: URI

class UnfollowOrganizationInput(GQLObject):
   organizationId: ID
   clientMutationId: str

class UnarchiveProjectV2ItemInput(GQLObject):
   projectId: ID
   itemId: ID
   clientMutationId: str

class TransferEnterpriseOrganizationInput(GQLObject):
   organizationId: ID
   destinationEnterpriseId: ID
   clientMutationId: str

class TeamRepositoryOrder(GQLObject):
   field: TeamRepositoryOrderField
   direction: OrderDirection

class TeamMemberOrder(GQLObject):
   field: TeamMemberOrderField
   direction: OrderDirection

class TeamDiscussionCommentOrder(GQLObject):
   field: TeamDiscussionCommentOrderField
   direction: OrderDirection

class TagNamePatternParameters(GQLObject):
   name: str
   negate: bool
   operator: str
   pattern: str

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

class StatusCheckConfigurationInput(GQLObject):
   context: str
   integrationId: int

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

class SocialAccount(GQLObject):
   displayName: str
   provider: SocialAccountProvider
   url: URI

class SetRepositoryInteractionLimitInput(GQLObject):
   repositoryId: ID
   limit: RepositoryInteractionLimit
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SetEnterpriseIdentityProviderInput(GQLObject):
   enterpriseId: ID
   ssoUrl: URI
   issuer: str
   idpCertificate: str
   signatureMethod: SamlSignatureAlgorithm
   digestMethod: SamlDigestAlgorithm
   clientMutationId: str

class SecurityAdvisoryReference(GQLObject):
   url: URI

class SecurityAdvisoryPackage(GQLObject):
   ecosystem: SecurityAdvisoryEcosystem
   name: str

class SecurityAdvisoryIdentifierFilter(GQLObject):
   type: SecurityAdvisoryIdentifierType
   value: str

class SavedReplyOrder(GQLObject):
   field: SavedReplyOrderField
   direction: OrderDirection

class RevokeMigratorRoleInput(GQLObject):
   organizationId: ID
   actor: str
   actorType: ActorType
   clientMutationId: str

class ReviewStatusHovercardContext(GQLObject):
   message: str
   octicon: str
   reviewDecision: PullRequestReviewDecision

class RetireSponsorsTierInput(GQLObject):
   tierId: ID
   clientMutationId: str

class RerequestCheckSuiteInput(GQLObject):
   repositoryId: ID
   checkSuiteId: ID
   clientMutationId: str

class RequiredDeploymentsParametersInput(GQLObject):
   requiredDeploymentEnvironments: list[str]

class FYIJK_isRequired_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class RequestReviewsInput(GQLObject):
   pullRequestId: ID
   userIds: list[ID]
   teamIds: list[ID]
   union: bool
   clientMutationId: str

class RepositoryOrder(GQLObject):
   field: RepositoryOrderField
   direction: OrderDirection

class RepositoryNameConditionTarget(GQLObject):
   exclude: list[str]
   include: list[str]
   protected: bool

class RepositoryInvitationOrder(GQLObject):
   field: RepositoryInvitationOrderField
   direction: OrderDirection

class RepositoryIdConditionTargetInput(GQLObject):
   repositoryIds: list[ID]

class RepositoryContactLink(GQLObject):
   about: str
   name: str
   url: URI

class ReopenPullRequestInput(GQLObject):
   pullRequestId: ID
   clientMutationId: str

class ReopenDiscussionInput(GQLObject):
   discussionId: ID
   clientMutationId: str

class RemoveStarInput(GQLObject):
   starrableId: ID
   clientMutationId: str

class RemoveOutsideCollaboratorInput(GQLObject):
   userId: ID
   organizationId: ID
   clientMutationId: str

class RemoveEnterpriseSupportEntitlementPayload(GQLObject):
   clientMutationId: str
   message: str

class RemoveEnterpriseOrganizationInput(GQLObject):
   enterpriseId: ID
   organizationId: ID
   clientMutationId: str

class RemoveEnterpriseIdentityProviderInput(GQLObject):
   enterpriseId: ID
   clientMutationId: str

class RemoveAssigneesFromAssignableInput(GQLObject):
   assignableId: ID
   assigneeIds: list[ID]
   clientMutationId: str

class RejectDeploymentsInput(GQLObject):
   workflowRunId: ID
   environmentIds: list[ID]
   comment: str
   clientMutationId: str

class RegenerateVerifiableDomainTokenInput(GQLObject):
   id: ID
   clientMutationId: str

class RefUpdateRule(GQLObject):
   allowsDeletions: bool
   allowsForcePushes: bool
   blocksCreations: bool
   pattern: str
   requiredApprovingReviewCount: int
   requiredStatusCheckContexts: list[str]
   requiresCodeOwnerReviews: bool
   requiresConversationResolution: bool
   requiresLinearHistory: bool
   requiresSignatures: bool
   viewerAllowedToDismissReviews: bool
   viewerCanPush: bool

class RefNameConditionTargetInput(GQLObject):
   exclude: list[str]
   include: list[str]

class ReactionOrder(GQLObject):
   field: ReactionOrderField
   direction: OrderDirection

class PullRequestParametersInput(GQLObject):
   dismissStaleReviewsOnPush: bool
   requireCodeOwnerReview: bool
   requireLastPushApproval: bool
   requiredApprovingReviewCount: int
   requiredReviewThreadResolution: bool

class PullRequestOrder(GQLObject):
   field: PullRequestOrderField
   direction: OrderDirection

class PublishSponsorsTierInput(GQLObject):
   tierId: ID
   clientMutationId: str

class ProjectV2WorkflowOrder(GQLObject):
   field: ProjectV2WorkflowsOrderField
   direction: OrderDirection

class ProjectV2SingleSelectFieldOptionInput(GQLObject):
   name: str
   color: ProjectV2SingleSelectFieldOptionColor
   description: str

class ProjectV2Order(GQLObject):
   field: ProjectV2OrderField
   direction: OrderDirection

class ProjectV2ItemOrder(GQLObject):
   field: ProjectV2ItemOrderField
   direction: OrderDirection

class ProjectV2Filters(GQLObject):
   state: ProjectV2State

class ProjectV2FieldOrder(GQLObject):
   field: ProjectV2FieldOrderField
   direction: OrderDirection

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

class MergeQueueConfiguration(GQLObject):
   checkResponseTimeout: int
   maximumEntriesToBuild: int
   maximumEntriesToMerge: int
   mergeMethod: PullRequestMergeMethod
   mergingStrategy: MergeQueueMergingStrategy
   minimumEntriesToMerge: int
   minimumEntriesToMergeWaitTime: int

class MergeBranchInput(GQLObject):
   repositoryId: ID
   base: str
   head: str
   commitMessage: str
   authorEmail: str
   clientMutationId: str

class MarkPullRequestReadyForReviewInput(GQLObject):
   pullRequestId: ID
   clientMutationId: str

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

class IssueOrder(GQLObject):
   field: IssueOrderField
   direction: OrderDirection

class IssueCommentOrder(GQLObject):
   field: IssueCommentOrderField
   direction: OrderDirection

class InviteEnterpriseAdminInput(GQLObject):
   enterpriseId: ID
   invitee: str
   email: str
   role: EnterpriseAdministratorRole
   clientMutationId: str

class GrantMigratorRolePayload(GQLObject):
   clientMutationId: str
   success: bool

class GrantEnterpriseOrganizationsMigratorRoleInput(GQLObject):
   enterpriseId: ID
   login: str
   clientMutationId: str

class GistOrder(GQLObject):
   field: GistOrderField
   direction: OrderDirection

class FundingLink(GQLObject):
   platform: FundingPlatform
   url: URI

class FollowOrganizationInput(GQLObject):
   organizationId: ID
   clientMutationId: str

class FileAddition(GQLObject):
   path: str
   contents: Base64String

class Environments(GQLObject):
   field: EnvironmentOrderField
   direction: OrderDirection

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

class EnqueuePullRequestInput(GQLObject):
   pullRequestId: ID
   jump: bool
   expectedHeadOid: GitObjectID
   clientMutationId: str

class DraftPullRequestReviewThread(GQLObject):
   path: str
   line: int
   side: DiffSide
   startLine: int
   startSide: DiffSide
   body: str

class DismissRepositoryVulnerabilityAlertInput(GQLObject):
   repositoryVulnerabilityAlertId: ID
   dismissReason: DismissReason
   clientMutationId: str

class DiscussionPollOptionOrder(GQLObject):
   field: DiscussionPollOptionOrderField
   direction: OrderDirection

class DisablePullRequestAutoMergeInput(GQLObject):
   pullRequestId: ID
   clientMutationId: str

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

class DeleteRepositoryRulesetPayload(GQLObject):
   clientMutationId: str

class DeleteRefPayload(GQLObject):
   clientMutationId: str

class DeletePullRequestReviewInput(GQLObject):
   pullRequestReviewId: ID
   clientMutationId: str

class DeleteProjectV2WorkflowInput(GQLObject):
   workflowId: ID
   clientMutationId: str

class DeleteProjectV2ItemInput(GQLObject):
   projectId: ID
   itemId: ID
   clientMutationId: str

class DeleteProjectV2FieldInput(GQLObject):
   fieldId: ID
   clientMutationId: str

class DeleteProjectColumnInput(GQLObject):
   columnId: ID
   clientMutationId: str

class DeleteLinkedBranchInput(GQLObject):
   linkedBranchId: ID
   clientMutationId: str

class DeleteIssueCommentPayload(GQLObject):
   clientMutationId: str

class DeleteIpAllowListEntryInput(GQLObject):
   ipAllowListEntryId: ID
   clientMutationId: str

class DeleteEnvironmentInput(GQLObject):
   id: ID
   clientMutationId: str

class DeleteDiscussionCommentInput(GQLObject):
   id: ID
   clientMutationId: str

class DeleteDeploymentInput(GQLObject):
   id: ID
   clientMutationId: str

class DeleteBranchProtectionRuleInput(GQLObject):
   branchProtectionRuleId: ID
   clientMutationId: str

class DeclineTopicSuggestionInput(GQLObject):
   repositoryId: ID
   name: str
   reason: TopicSuggestionDeclineReason
   clientMutationId: str

class CreateTeamDiscussionCommentInput(GQLObject):
   discussionId: ID
   body: str
   clientMutationId: str

class CreateSponsorsTierInput(GQLObject):
   sponsorableId: ID
   sponsorableLogin: str
   amount: int
   isRecurring: bool
   repositoryId: ID
   repositoryOwnerLogin: str
   repositoryName: str
   welcomeMessage: str
   description: str
   publish: bool
   clientMutationId: str

class CreateRepositoryInput(GQLObject):
   name: str
   ownerId: ID
   description: str
   visibility: RepositoryVisibility
   template: bool
   homepageUrl: URI
   hasWikiEnabled: bool
   hasIssuesEnabled: bool
   teamId: ID
   clientMutationId: str

class CreatePullRequestInput(GQLObject):
   repositoryId: ID
   baseRefName: str
   headRefName: str
   headRepositoryId: ID
   title: str
   body: str
   maintainerCanModify: bool
   draft: bool
   clientMutationId: str

class CreateProjectInput(GQLObject):
   ownerId: ID
   name: str
   body: str
   template: ProjectTemplate
   repositoryIds: list[ID]
   clientMutationId: str

class CreateLinkedBranchInput(GQLObject):
   issueId: ID
   oid: GitObjectID
   name: str
   repositoryId: ID
   clientMutationId: str

class CreateIpAllowListEntryInput(GQLObject):
   ownerId: ID
   allowListValue: str
   name: str
   isActive: bool
   clientMutationId: str

class CreateEnterpriseOrganizationInput(GQLObject):
   enterpriseId: ID
   login: str
   profileName: str
   billingEmail: str
   adminLogins: list[str]
   clientMutationId: str

class CreateCheckSuiteInput(GQLObject):
   repositoryId: ID
   headSha: GitObjectID
   clientMutationId: str

class CopyProjectV2Input(GQLObject):
   projectId: ID
   ownerId: ID
   title: str
   includeDraftIssues: bool
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

class CommitterEmailPatternParametersInput(GQLObject):
   name: str
   negate: bool
   operator: str
   pattern: str

class CommittableBranch(GQLObject):
   id: ID
   repositoryNameWithOwner: str
   branchName: str

class CommitMessagePatternParameters(GQLObject):
   name: str
   negate: bool
   operator: str
   pattern: str

class CommitContributionOrder(GQLObject):
   field: CommitContributionOrderField
   direction: OrderDirection

class CommitAuthorEmailPatternParameters(GQLObject):
   name: str
   negate: bool
   operator: str
   pattern: str

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

class Closable(GQLObject):
   closed: bool
   closedAt: DateTime
   viewerCanClose: bool
   viewerCanReopen: bool

class CloneProjectInput(GQLObject):
   targetOwnerId: ID
   sourceId: ID
   includeWorkflows: bool
   name: str
   body: str
   public: bool
   clientMutationId: str

class ClearLabelsFromLabelableInput(GQLObject):
   labelableId: ID
   clientMutationId: str

class CheckSuiteAutoTriggerPreference(GQLObject):
   appId: ID
   setting: bool

class CheckRunStateCount(GQLObject):
   count: int
   state: CheckRunState

class CheckRunFilter(GQLObject):
   checkType: CheckRunType
   appId: int
   checkName: str
   status: CheckStatusState
   statuses: list[CheckStatusState]
   conclusions: list[CheckConclusionState]

class CheckAnnotationRange(GQLObject):
   startLine: int
   startColumn: int
   endLine: int
   endColumn: int

class ChangeUserStatusInput(GQLObject):
   emoji: str
   message: str
   organizationId: ID
   limitedAvailability: bool
   expiresAt: DateTime
   clientMutationId: str

class CancelEnterpriseAdminInvitationInput(GQLObject):
   invitationId: ID
   clientMutationId: str

class CVSS(GQLObject):
   score: float
   vectorString: str

class BranchNamePatternParametersInput(GQLObject):
   name: str
   negate: bool
   operator: str
   pattern: str

class NVXRV_URI_Field(ArguedStr):
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
   environmentIds: list[ID]
   comment: str
   clientMutationId: str

class AddVerifiableDomainInput(GQLObject):
   ownerId: ID
   domain: URI
   clientMutationId: str

class AddStarInput(GQLObject):
   starrableId: ID
   clientMutationId: str

class AddPullRequestReviewThreadReplyInput(GQLObject):
   pullRequestReviewId: ID
   pullRequestReviewThreadId: ID
   body: str
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
   userIds: list[ID]
   role: OrganizationMemberRole
   clientMutationId: str

class AddDiscussionCommentInput(GQLObject):
   discussionId: ID
   replyToId: ID
   body: str
   clientMutationId: str

class AddAssigneesToAssignableInput(GQLObject):
   assignableId: ID
   assigneeIds: list[ID]
   clientMutationId: str

class MJKUR_URI_Field(ArguedStr):
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
