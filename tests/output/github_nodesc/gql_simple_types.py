from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class HOGCL_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class AOHCF_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class FZRXH_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class SXSCE_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class GDEQP_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class RSSEG_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class VZXBI_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class RPNAL_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class WRICR_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class XCIDQ_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class VLACR_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class LWZUT_organizationVerifiedDomainEmails_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: strArgs



class AAPRS_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class AGBVX_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: boolArgs



class KLZHD_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class AUWAD_anyPinnableItems_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      type: PinnableItemType

   _args: boolArgs



class QFDZZ_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class DTRED_isSponsoredBy_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      accountLogin: NonNull_str

   _args: boolArgs



class YKRCG_text_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      truncate: int

   _args: strArgs



class UBBSL_totalRepositoryContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool

   _args: intArgs



class ZVTAU_totalRepositoriesWithContributedPullRequests_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class JXWCU_totalRepositoriesWithContributedIssues_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class KOZYA_totalPullRequestContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class KBFBZ_totalIssueContributions_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class KIBUZ_isRequired_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class DLFHM_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class DXUCT_isRequired_Field(ArguedBool):
   class boolArgs(GQLArgsSet, GQLObject):
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class DQDRX_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class FKJAG_viewerMergeHeadlineText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      mergeType: PullRequestMergeMethod

   _args: strArgs



class OTOTS_viewerMergeBodyText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      mergeType: PullRequestMergeMethod

   _args: strArgs



class NXVNO_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class LEFZQ_trackedIssuesCount_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject):
      states: list[TrackedIssueStates]

   _args: intArgs



class NXHFP_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class UYXMK_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class WGINF_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject):
      limit: int

   _args: HTMLArgs



class QCNWR_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class ZFXAU_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject):
      size: int

   _args: URIArgs



class ZGTPS_isRequired_Field(ArguedBool):
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
   requiredDeploymentEnvironments: NonNull_list[str]

class RequirableByPullRequest(GQLObject):
   isRequired: ZGTPS_isRequired_Field

class RepositoryOrder(GQLObject):
   field: RepositoryOrderField
   direction: OrderDirection

class RepositoryNameConditionTarget(GQLObject):
   exclude: NonNull_list[str]
   include: NonNull_list[str]
   protected: bool

class RepositoryInvitationOrder(GQLObject):
   field: RepositoryInvitationOrderField
   direction: OrderDirection

class RepositoryIdConditionTargetInput(GQLObject):
   repositoryIds: NonNull_list[ID]

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
   assigneeIds: NonNull_list[ID]
   clientMutationId: str

class RejectDeploymentsInput(GQLObject):
   workflowRunId: ID
   environmentIds: NonNull_list[ID]
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
   exclude: NonNull_list[str]
   include: NonNull_list[str]

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

class EnterpriseServerUserAccountsUploadOrder(GQLObject):
   field: EnterpriseServerUserAccountsUploadOrderField
   direction: OrderDirection

class EnterpriseServerUserAccountEmailOrder(GQLObject):
   field: EnterpriseServerUserAccountEmailOrderField
   direction: OrderDirection

class EnterpriseRepositoryInfo(GQLObject):
   id: ID
   isPrivate: bool
   name: str
   nameWithOwner: str

class EnterpriseBillingInfo(GQLObject):
   allLicensableUsersCount: int
   assetPacks: int
   bandwidthQuota: float
   bandwidthUsage: float
   bandwidthUsagePercentage: int
   storageQuota: float
   storageUsage: float
   storageUsagePercentage: int
   totalAvailableLicenses: int
   totalLicenses: int

class EnterpriseAdministratorInvitationOrder(GQLObject):
   field: EnterpriseAdministratorInvitationOrderField
   direction: OrderDirection

class EnablePullRequestAutoMergeInput(GQLObject):
   pullRequestId: ID
   commitHeadline: str
   commitBody: str
   mergeMethod: PullRequestMergeMethod
   authorEmail: str
   expectedHeadOid: GitObjectID
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

class DequeuePullRequestInput(GQLObject):
   id: ID
   clientMutationId: str

class DeployKey(GQLObject):
   createdAt: DateTime
   id: ID
   key: str
   readOnly: bool
   title: str
   verified: bool

class DeleteVerifiableDomainInput(GQLObject):
   id: ID
   clientMutationId: str

class DeleteTeamDiscussionInput(GQLObject):
   id: ID
   clientMutationId: str

class DeleteTeamDiscussionCommentInput(GQLObject):
   id: ID
   clientMutationId: str

class DeleteRepositoryRulesetInput(GQLObject):
   repositoryRulesetId: ID
   clientMutationId: str

class DeleteRefInput(GQLObject):
   refId: ID
   clientMutationId: str

class DeletePullRequestReviewCommentInput(GQLObject):
   id: ID
   clientMutationId: str

class DeleteProjectV2ItemPayload(GQLObject):
   clientMutationId: str
   deletedItemId: ID

class DeleteProjectV2Input(GQLObject):
   projectId: ID
   clientMutationId: str

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

class ConvertPullRequestToDraftInput(GQLObject):
   pullRequestId: ID
   clientMutationId: str

class ContributionOrder(GQLObject):
   direction: OrderDirection

class ContributionCalendarDay(GQLObject):
   color: str
   contributionCount: int
   contributionLevel: ContributionLevel
   date: Date
   weekday: int

class CommitterEmailPatternParameters(GQLObject):
   name: str
   negate: bool
   operator: str
   pattern: str

class CommitMessagePatternParametersInput(GQLObject):
   name: str
   negate: bool
   operator: str
   pattern: str

class CommitMessage(GQLObject):
   headline: str
   body: str

class CommitAuthorEmailPatternParametersInput(GQLObject):
   name: str
   negate: bool
   operator: str
   pattern: str

class CommitAuthor(GQLObject):
   id: ID
   emails: list[str]

class ClosePullRequestInput(GQLObject):
   pullRequestId: ID
   clientMutationId: str

class CloseDiscussionInput(GQLObject):
   discussionId: ID
   reason: DiscussionCloseReason
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

class BulkSponsorship(GQLObject):
   sponsorableId: ID
   sponsorableLogin: str
   amount: int

class BranchNamePatternParameters(GQLObject):
   name: str
   negate: bool
   operator: str
   pattern: str

class Bot(GQLObject):
   avatarUrl: ZFXAU_URI_Field
   createdAt: DateTime
   databaseId: int
   id: ID
   login: str
   resourcePath: URI
   updatedAt: DateTime
   url: URI

class ArchiveRepositoryInput(GQLObject):
   repositoryId: ID
   clientMutationId: str

class ApproveVerifiableDomainInput(GQLObject):
   id: ID
   clientMutationId: str

class AnnouncementBanner(GQLObject):
   announcement: str
   announcementExpiresAt: DateTime
   announcementUserDismissible: bool

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

class NUJUD_URI_Field(ArguedStr):
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
