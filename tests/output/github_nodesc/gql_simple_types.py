from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class ITKNL_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class WHZHN_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class SBGUI_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class RTGBY_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class QMJPZ_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class HDSAY_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class WLIHN_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class ACEAV_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class ACXRV_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class OCGFU_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class XRZWP_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class ACXCR_organizationVerifiedDomainEmails_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: strArgs



class QDFYO_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class TRPGF_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: boolArgs



class KCOBC_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class HFWZO_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class AVBAQ_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class KJKSS_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class ZBXCL_text_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      truncate: int

   _args: strArgs



class DAXNX_totalRepositoryContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool

   _args: intArgs



class CSZXV_totalRepositoriesWithContributedPullRequests_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class RLDGW_totalRepositoriesWithContributedIssues_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class SCDZL_totalPullRequestContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class QDXTZ_totalIssueContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class XSWWW_isRequired_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class RFWIB_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class RIJZT_isRequired_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class DDGXG_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class UQTDZ_viewerMergeHeadlineText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      mergeType: PullRequestMergeMethod

   _args: strArgs



class EGLHV_viewerMergeBodyText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      mergeType: PullRequestMergeMethod

   _args: strArgs



class GPMGM_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class BEYLW_trackedIssuesCount_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      states: list[TrackedIssueStates]

   _args: intArgs



class HLTJY_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class TWNLY_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class HDADO_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class BFFZN_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class UIDRE_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class GVMEJ_isRequired_Field(ArguedBool):
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

class Submodule(GQLObject):
   branch: str
   gitUrl: URI
   name: str
   nameRaw: Base64String
   path: str
   pathRaw: Base64String
   subprojectCommitOid: GitObjectID

class StatusContextStateCount(GQLObject):
   count: int
   state: StatusState

class StatusCheckConfiguration(GQLObject):
   context: str
   integrationId: int

class StartOrganizationMigrationInput(GQLObject):
   sourceOrgUrl: URI
   targetOrgName: str
   targetEnterpriseId: ID
   sourceAccessToken: str
   clientMutationId: str

class SponsorshipOrder(GQLObject):
   field: SponsorshipOrderField
   direction: OrderDirection

class SponsorsTierOrder(GQLObject):
   field: SponsorsTierOrderField
   direction: OrderDirection

class SponsorsActivityOrder(GQLObject):
   field: SponsorsActivityOrderField
   direction: OrderDirection

class SponsorOrder(GQLObject):
   field: SponsorOrderField
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

class RequiredDeploymentsParameters(GQLObject):
   requiredDeploymentEnvironments: list[str]

class RequirableByPullRequest(GQLObject):
   isRequired: GVMEJ_isRequired_Field

class RepositoryRulesetBypassActorInput(GQLObject):
   actorId: ID
   repositoryRoleDatabaseId: int
   organizationAdmin: bool
   bypassMode: RepositoryRulesetBypassActorBypassMode

class RepositoryNameConditionTargetInput(GQLObject):
   exclude: list[str]
   include: list[str]
   protected: bool

class RepositoryMigrationOrder(GQLObject):
   field: RepositoryMigrationOrderField
   direction: RepositoryMigrationOrderDirection

class RepositoryInteractionAbility(GQLObject):
   expiresAt: DateTime
   limit: RepositoryInteractionLimit
   origin: RepositoryInteractionLimitOrigin

class RepositoryIdConditionTarget(GQLObject):
   repositoryIds: list[ID]

class RepositoryCodeownersError(GQLObject):
   column: int
   kind: str
   line: int
   message: str
   path: str
   source: str
   suggestion: str

class ReopenIssueInput(GQLObject):
   issueId: ID
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
   labelIds: list[ID]
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

class RefNameConditionTarget(GQLObject):
   exclude: list[str]
   include: list[str]

class RateLimit(GQLObject):
   cost: int
   limit: int
   nodeCount: int
   remaining: int
   resetAt: DateTime
   used: int

class PullRequestParameters(GQLObject):
   dismissStaleReviewsOnPush: bool
   requireCodeOwnerReview: bool
   requireLastPushApproval: bool
   requiredApprovingReviewCount: int
   requiredReviewThreadResolution: bool

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

class ProjectV2ViewOrder(GQLObject):
   field: ProjectV2ViewOrderField
   direction: OrderDirection

class ProjectV2SingleSelectFieldOption(GQLObject):
   color: ProjectV2SingleSelectFieldOptionColor
   description: str
   descriptionHTML: str
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

class ProjectV2Collaborator(GQLObject):
   userId: ID
   teamId: ID
   role: ProjectV2Roles

class ProjectOrder(GQLObject):
   field: ProjectOrderField
   direction: OrderDirection

class PageInfo(GQLObject):
   endCursor: str
   hasNextPage: bool
   hasPreviousPage: bool
   startCursor: str

class PackageVersionOrder(GQLObject):
   field: PackageVersionOrderField
   direction: OrderDirection

class PackageOrder(GQLObject):
   field: PackageOrderField
   direction: OrderDirection

class OrganizationOrder(GQLObject):
   field: OrganizationOrderField
   direction: OrderDirection

class OrgEnterpriseOwnerOrder(GQLObject):
   field: OrgEnterpriseOwnerOrderField
   direction: OrderDirection

class Node(GQLObject):
   id: ID

class MoveProjectCardInput(GQLObject):
   cardId: ID
   columnId: ID
   afterCardId: ID
   clientMutationId: str

class Minimizable(GQLObject):
   isMinimized: bool
   minimizedReason: str
   viewerCanMinimize: bool

class MigrationSource(GQLObject):
   id: ID
   name: str
   type: MigrationSourceType
   url: URI

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

class MarkProjectV2AsTemplateInput(GQLObject):
   projectId: ID
   clientMutationId: str

class MarkDiscussionCommentAsAnswerInput(GQLObject):
   id: ID
   clientMutationId: str

class Lockable(GQLObject):
   activeLockReason: LockReason
   locked: bool

class LinkRepositoryToProjectInput(GQLObject):
   projectId: ID
   repositoryId: ID
   clientMutationId: str

class LinkProjectV2ToRepositoryInput(GQLObject):
   projectId: ID
   repositoryId: ID
   clientMutationId: str

class LanguageOrder(GQLObject):
   field: LanguageOrderField
   direction: OrderDirection

class LabelOrder(GQLObject):
   field: LabelOrderField
   direction: OrderDirection

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

class CMDBK_URI_Field(ArguedStr):
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

class AddPullRequestReviewThreadInput(GQLObject):
   path: str
   body: str
   pullRequestId: ID
   pullRequestReviewId: ID
   line: int
   side: DiffSide
   startLine: int
   startSide: DiffSide
   subjectType: PullRequestReviewThreadSubjectType
   clientMutationId: str

class AddProjectV2ItemByIdInput(GQLObject):
   projectId: ID
   contentId: ID
   clientMutationId: str

class AddProjectColumnInput(GQLObject):
   projectId: ID
   name: str
   clientMutationId: str

class AddLabelsToLabelableInput(GQLObject):
   labelableId: ID
   labelIds: list[ID]
   clientMutationId: str

class AddEnterpriseSupportEntitlementInput(GQLObject):
   enterpriseId: ID
   login: str
   clientMutationId: str

class AddDiscussionPollVoteInput(GQLObject):
   pollOptionId: ID
   clientMutationId: str

class AddCommentInput(GQLObject):
   subjectId: ID
   body: str
   clientMutationId: str

class ActorLocation(GQLObject):
   city: str
   country: str
   countryCode: str
   region: str
   regionCode: str

class Actor(GQLObject):
   avatarUrl: UIDRE_URI_Field
   login: str
   resourcePath: URI
   url: URI

class AcceptEnterpriseAdministratorInvitationInput(GQLObject):
   invitationId: ID
   clientMutationId: str

class AbortQueuedMigrationsInput(GQLObject):
   ownerId: ID
   clientMutationId: str
