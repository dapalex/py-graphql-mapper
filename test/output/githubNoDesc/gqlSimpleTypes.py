from typing import Generic
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gqlTypes import ID
from pygqlmap.src.gqlArgBuiltin import *
from .enums import *
from .scalars import *

class FGHZRanyPinnableItems_anyPinnableItems_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      type: PinnableItemType

   _args: boolArgs



class TQXXMlogoUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class HKJJHlogoUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class QJWMQavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class DNUPPshortDescriptionHTML_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject): 
      limit: int

   _args: HTMLArgs



class NLRXVavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class SQQASisSponsoredBy_isSponsoredBy_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      accountLogin: str ##NON NULL

   _args: boolArgs



class QKIOIavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class NFATBanyPinnableItems_anyPinnableItems_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      type: PinnableItemType

   _args: boolArgs



class YRBADorganizationVerifiedDomainEmails_organizationVerifiedDomainEmails_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: strArgs



class TYUVPisSponsoredBy_isSponsoredBy_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      accountLogin: str ##NON NULL

   _args: boolArgs



class OHADDcanReceiveOrganizationEmailsWhenNotificationsRestricted_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: boolArgs



class PBEOMavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class ZENZGanyPinnableItems_anyPinnableItems_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      type: PinnableItemType

   _args: boolArgs



class AURXIisSponsoredBy_isSponsoredBy_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      accountLogin: str ##NON NULL

   _args: boolArgs



class IRETUtext_text_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject): 
      truncate: int

   _args: strArgs



class YZKMRtotalRepositoryContributions_totalRepositoryContributions_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      excludeFirst: bool

   _args: intArgs



class GJQECtotalRepositoriesWithContributedPullRequests_totalRepositoriesWithContributedPullRequests_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class NQBDBtotalRepositoriesWithContributedIssues_totalRepositoriesWithContributedIssues_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class WTCKPtotalPullRequestContributions_totalPullRequestContributions_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class WYQXRtotalIssueContributions_totalIssueContributions_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class CKILMisRequired_isRequired_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class APMIUavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class GCYIQisRequired_isRequired_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class RMTYBavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class BJQEFviewerMergeHeadlineText_viewerMergeHeadlineText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject): 
      mergeType: PullRequestMergeMethod

   _args: strArgs



class SNZMLviewerMergeBodyText_viewerMergeBodyText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject): 
      mergeType: PullRequestMergeMethod

   _args: strArgs



class TQXNNavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class KGMMNtrackedIssuesCount_trackedIssuesCount_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      states: TrackedIssueStates ##LIST

   _args: intArgs



class ASOLOshortDescriptionHTML_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject): 
      limit: int

   _args: HTMLArgs



class SNCDXavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class JVCZDshortDescriptionHTML_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject): 
      limit: int

   _args: HTMLArgs



class MIVBDavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class KDKPRavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class XVGUIavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class WorkflowRunOrder(GQLObject):
   field: WorkflowRunOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class VerifyVerifiableDomainInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class UserStatusOrder(GQLObject):
   field: UserStatusOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class UpdateTopicsInput(GQLObject):
   repositoryId: ID ##NON NULL
   topicNames: str ##NON NULL ##LIST
   clientMutationId: str

class UpdateTeamDiscussionInput(GQLObject):
   id: ID ##NON NULL
   title: str
   body: str
   bodyVersion: str
   pinned: bool
   clientMutationId: str

class UpdateSubscriptionInput(GQLObject):
   subscribableId: ID ##NON NULL
   state: SubscriptionState ##NON NULL
   clientMutationId: str

class UpdateRepositoryWebCommitSignoffSettingInput(GQLObject):
   repositoryId: ID ##NON NULL
   webCommitSignoffRequired: bool ##NON NULL
   clientMutationId: str

class UpdateRefInput(GQLObject):
   refId: ID ##NON NULL
   oid: GitObjectID ##NON NULL
   force: bool
   clientMutationId: str

class UpdatePullRequestReviewCommentInput(GQLObject):
   pullRequestReviewCommentId: ID ##NON NULL
   body: str ##NON NULL
   clientMutationId: str

class UpdatePullRequestBranchInput(GQLObject):
   pullRequestId: ID ##NON NULL
   expectedHeadOid: GitObjectID
   clientMutationId: str

class UpdateProjectV2Input(GQLObject):
   projectId: ID ##NON NULL
   title: str
   shortDescription: str
   readme: str
   closed: bool
   public: bool
   clientMutationId: str

class UpdateProjectNextItemFieldInput(GQLObject):
   projectId: ID
   itemId: ID
   fieldId: ID
   value: str
   clientMutationId: str

class UpdateProjectInput(GQLObject):
   projectId: ID ##NON NULL
   name: str
   body: str
   state: ProjectState
   public: bool
   clientMutationId: str

class UpdateProjectColumnInput(GQLObject):
   projectColumnId: ID ##NON NULL
   name: str ##NON NULL
   clientMutationId: str

class UpdateOrganizationWebCommitSignoffSettingInput(GQLObject):
   organizationId: ID ##NON NULL
   webCommitSignoffRequired: bool ##NON NULL
   clientMutationId: str

class UpdateNotificationRestrictionSettingInput(GQLObject):
   ownerId: ID ##NON NULL
   settingValue: NotificationRestrictionSettingValue ##NON NULL
   clientMutationId: str

class UpdateIssueCommentInput(GQLObject):
   id: ID ##NON NULL
   body: str ##NON NULL
   clientMutationId: str

class UpdateIpAllowListEntryInput(GQLObject):
   ipAllowListEntryId: ID ##NON NULL
   allowListValue: str ##NON NULL
   name: str
   isActive: bool ##NON NULL
   clientMutationId: str

class UpdateEnvironmentInput(GQLObject):
   environmentId: ID ##NON NULL
   waitTimer: int
   reviewers: ID ##NON NULL ##LIST
   clientMutationId: str

class UpdateEnterpriseTeamDiscussionsSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseProfileInput(GQLObject):
   enterpriseId: ID ##NON NULL
   name: str
   description: str
   websiteUrl: str
   location: str
   clientMutationId: str

class UpdateEnterpriseOwnerOrganizationRoleInput(GQLObject):
   enterpriseId: ID ##NON NULL
   organizationId: ID ##NON NULL
   organizationRole: RoleInOrganization ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanMakePurchasesSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseMembersCanMakePurchasesSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanCreateRepositoriesSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseMembersCanCreateRepositoriesSettingValue
   membersCanCreateRepositoriesPolicyEnabled: bool
   membersCanCreatePublicRepositories: bool
   membersCanCreatePrivateRepositories: bool
   membersCanCreateInternalRepositories: bool
   clientMutationId: str

class UpdateEnterpriseDefaultRepositoryPermissionSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseDefaultRepositoryPermissionSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseAdministratorRolePayload(GQLObject):
   clientMutationId: str
   message: str

class UpdateDiscussionInput(GQLObject):
   discussionId: ID ##NON NULL
   title: str
   body: str
   categoryId: ID
   clientMutationId: str

class UpdatableComment(GQLObject):
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL

class UnresolveReviewThreadInput(GQLObject):
   threadId: ID ##NON NULL
   clientMutationId: str

class UnminimizeCommentInput(GQLObject):
   subjectId: ID ##NON NULL
   clientMutationId: str

class UnmarkFileAsViewedInput(GQLObject):
   pullRequestId: ID ##NON NULL
   path: str ##NON NULL
   clientMutationId: str

class UnlockLockableInput(GQLObject):
   lockableId: ID ##NON NULL
   clientMutationId: str

class UnlinkProjectV2FromTeamInput(GQLObject):
   projectId: ID ##NON NULL
   teamId: ID ##NON NULL
   clientMutationId: str

class UniformResourceLocatable(GQLObject):
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class UnfollowOrganizationInput(GQLObject):
   organizationId: ID ##NON NULL
   clientMutationId: str

class UnarchiveProjectV2ItemInput(GQLObject):
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   clientMutationId: str

class TransferEnterpriseOrganizationInput(GQLObject):
   organizationId: ID ##NON NULL
   destinationEnterpriseId: ID ##NON NULL
   clientMutationId: str

class TeamRepositoryOrder(GQLObject):
   field: TeamRepositoryOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class TeamMemberOrder(GQLObject):
   field: TeamMemberOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class TeamDiscussionCommentOrder(GQLObject):
   field: TeamDiscussionCommentOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class Submodule(GQLObject):
   branch: str
   gitUrl: URI ##NON NULL
   name: str ##NON NULL
   nameRaw: Base64String ##NON NULL
   path: str ##NON NULL
   pathRaw: Base64String ##NON NULL
   subprojectCommitOid: GitObjectID

class StatusContextStateCount(GQLObject):
   count: int ##NON NULL
   state: StatusState ##NON NULL

class StarOrder(GQLObject):
   field: StarOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorshipNewsletterOrder(GQLObject):
   field: SponsorshipNewsletterOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorsGoal(GQLObject):
   description: str
   kind: SponsorsGoalKind ##NON NULL
   percentComplete: int ##NON NULL
   targetValue: int ##NON NULL
   title: str ##NON NULL

class SponsorableOrder(GQLObject):
   field: SponsorableOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SortBy(GQLObject):
   direction: OrderDirection ##NON NULL
   field: int ##NON NULL

class SetRepositoryInteractionLimitInput(GQLObject):
   repositoryId: ID ##NON NULL
   limit: RepositoryInteractionLimit ##NON NULL
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SetEnterpriseIdentityProviderInput(GQLObject):
   enterpriseId: ID ##NON NULL
   ssoUrl: URI ##NON NULL
   issuer: str
   idpCertificate: str ##NON NULL
   signatureMethod: SamlSignatureAlgorithm ##NON NULL
   digestMethod: SamlDigestAlgorithm ##NON NULL
   clientMutationId: str

class SecurityAdvisoryReference(GQLObject):
   url: URI ##NON NULL

class SecurityAdvisoryPackage(GQLObject):
   ecosystem: SecurityAdvisoryEcosystem ##NON NULL
   name: str ##NON NULL

class SecurityAdvisoryIdentifierFilter(GQLObject):
   type: SecurityAdvisoryIdentifierType ##NON NULL
   value: str ##NON NULL

class SavedReplyOrder(GQLObject):
   field: SavedReplyOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class RevokeMigratorRoleInput(GQLObject):
   organizationId: ID ##NON NULL
   actor: str ##NON NULL
   actorType: ActorType ##NON NULL
   clientMutationId: str

class ReviewStatusHovercardContext(GQLObject):
   message: str ##NON NULL
   octicon: str ##NON NULL
   reviewDecision: PullRequestReviewDecision

class RerequestCheckSuiteInput(GQLObject):
   repositoryId: ID ##NON NULL
   checkSuiteId: ID ##NON NULL
   clientMutationId: str

class NGLPZisRequired_isRequired_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class RequestReviewsInput(GQLObject):
   pullRequestId: ID ##NON NULL
   userIds: ID ##NON NULL ##LIST
   teamIds: ID ##NON NULL ##LIST
   union: bool
   clientMutationId: str

class RepositoryMigrationOrder(GQLObject):
   field: RepositoryMigrationOrderField ##NON NULL
   direction: RepositoryMigrationOrderDirection ##NON NULL

class RepositoryInteractionAbility(GQLObject):
   expiresAt: DateTime
   limit: RepositoryInteractionLimit ##NON NULL
   origin: RepositoryInteractionLimitOrigin ##NON NULL

class RepositoryCodeownersError(GQLObject):
   column: int ##NON NULL
   kind: str ##NON NULL
   line: int ##NON NULL
   message: str ##NON NULL
   path: str ##NON NULL
   source: str ##NON NULL
   suggestion: str

class ReopenIssueInput(GQLObject):
   issueId: ID ##NON NULL
   clientMutationId: str

class RemoveStarInput(GQLObject):
   starrableId: ID ##NON NULL
   clientMutationId: str

class RemoveOutsideCollaboratorInput(GQLObject):
   userId: ID ##NON NULL
   organizationId: ID ##NON NULL
   clientMutationId: str

class RemoveEnterpriseSupportEntitlementPayload(GQLObject):
   clientMutationId: str
   message: str

class RemoveEnterpriseOrganizationInput(GQLObject):
   enterpriseId: ID ##NON NULL
   organizationId: ID ##NON NULL
   clientMutationId: str

class RemoveEnterpriseAdminInput(GQLObject):
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class ReleaseOrder(GQLObject):
   field: ReleaseOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class RegenerateVerifiableDomainTokenPayload(GQLObject):
   clientMutationId: str
   verificationToken: str

class RegenerateEnterpriseIdentityProviderRecoveryCodesInput(GQLObject):
   enterpriseId: ID ##NON NULL
   clientMutationId: str

class RefOrder(GQLObject):
   field: RefOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class RateLimit(GQLObject):
   cost: int ##NON NULL
   limit: int ##NON NULL
   nodeCount: int ##NON NULL
   remaining: int ##NON NULL
   resetAt: DateTime ##NON NULL
   used: int ##NON NULL

class PullRequestChangedFile(GQLObject):
   additions: int ##NON NULL
   changeType: PatchStatus ##NON NULL
   deletions: int ##NON NULL
   path: str ##NON NULL
   viewerViewedState: FileViewedState ##NON NULL

class PublicKey(GQLObject):
   accessedAt: DateTime
   createdAt: DateTime
   fingerprint: str ##NON NULL
   id: ID ##NON NULL
   isReadOnly: bool
   key: str ##NON NULL
   updatedAt: DateTime

class ProjectV2SingleSelectFieldOption(GQLObject):
   id: str ##NON NULL
   name: str ##NON NULL
   nameHTML: str ##NON NULL

class ProjectV2IterationFieldIteration(GQLObject):
   duration: int ##NON NULL
   id: str ##NON NULL
   startDate: Date ##NON NULL
   title: str ##NON NULL
   titleHTML: str ##NON NULL

class ProjectV2ItemFieldValueOrder(GQLObject):
   field: ProjectV2ItemFieldValueOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class ProjectV2FieldValue(GQLObject):
   text: str
   number: float
   date: Date
   singleSelectOptionId: str
   iterationId: str

class ProjectProgress(GQLObject):
   doneCount: int ##NON NULL
   donePercentage: float ##NON NULL
   enabled: bool ##NON NULL
   inProgressCount: int ##NON NULL
   inProgressPercentage: float ##NON NULL
   todoCount: int ##NON NULL
   todoPercentage: float ##NON NULL

class PinIssueInput(GQLObject):
   issueId: ID ##NON NULL
   clientMutationId: str

class PackageVersionStatistics(GQLObject):
   downloadsTotalCount: int ##NON NULL

class PackageStatistics(GQLObject):
   downloadsTotalCount: int ##NON NULL

class PackageFileOrder(GQLObject):
   field: PackageFileOrderField
   direction: OrderDirection

class OrgEnterpriseOwnerOrder(GQLObject):
   field: OrgEnterpriseOwnerOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class Node(GQLObject):
   id: ID ##NON NULL

class MoveProjectCardInput(GQLObject):
   cardId: ID ##NON NULL
   columnId: ID ##NON NULL
   afterCardId: ID
   clientMutationId: str

class Minimizable(GQLObject):
   isMinimized: bool ##NON NULL
   minimizedReason: str
   viewerCanMinimize: bool ##NON NULL

class MigrationSource(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   type: MigrationSourceType ##NON NULL
   url: URI ##NON NULL

class MergeBranchInput(GQLObject):
   repositoryId: ID ##NON NULL
   base: str ##NON NULL
   head: str ##NON NULL
   commitMessage: str
   authorEmail: str
   clientMutationId: str

class MarkPullRequestReadyForReviewInput(GQLObject):
   pullRequestId: ID ##NON NULL
   clientMutationId: str

class MarkDiscussionCommentAsAnswerInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class Lockable(GQLObject):
   activeLockReason: LockReason
   locked: bool ##NON NULL

class LinkRepositoryToProjectInput(GQLObject):
   projectId: ID ##NON NULL
   repositoryId: ID ##NON NULL
   clientMutationId: str

class LinkProjectV2ToRepositoryInput(GQLObject):
   projectId: ID ##NON NULL
   repositoryId: ID ##NON NULL
   clientMutationId: str

class LanguageOrder(GQLObject):
   field: LanguageOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class LabelOrder(GQLObject):
   field: LabelOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class IssueOrder(GQLObject):
   field: IssueOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class IssueCommentOrder(GQLObject):
   field: IssueCommentOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class InviteEnterpriseAdminInput(GQLObject):
   enterpriseId: ID ##NON NULL
   invitee: str
   email: str
   role: EnterpriseAdministratorRole
   clientMutationId: str

class GrantMigratorRolePayload(GQLObject):
   clientMutationId: str
   success: bool

class GrantEnterpriseOrganizationsMigratorRoleInput(GQLObject):
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class GistOrder(GQLObject):
   field: GistOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class FundingLink(GQLObject):
   platform: FundingPlatform ##NON NULL
   url: URI ##NON NULL

class FollowOrganizationInput(GQLObject):
   organizationId: ID ##NON NULL
   clientMutationId: str

class FileAddition(GQLObject):
   path: str ##NON NULL
   contents: Base64String ##NON NULL

class EnterpriseServerUserAccountsUploadOrder(GQLObject):
   field: EnterpriseServerUserAccountsUploadOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseServerUserAccountEmailOrder(GQLObject):
   field: EnterpriseServerUserAccountEmailOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseRepositoryInfo(GQLObject):
   id: ID ##NON NULL
   isPrivate: bool ##NON NULL
   name: str ##NON NULL
   nameWithOwner: str ##NON NULL

class EnterpriseBillingInfo(GQLObject):
   allLicensableUsersCount: int ##NON NULL
   assetPacks: int ##NON NULL
   bandwidthQuota: float ##NON NULL
   bandwidthUsage: float ##NON NULL
   bandwidthUsagePercentage: int ##NON NULL
   storageQuota: float ##NON NULL
   storageUsage: float ##NON NULL
   storageUsagePercentage: int ##NON NULL
   totalAvailableLicenses: int ##NON NULL
   totalLicenses: int ##NON NULL

class EnterpriseAdministratorInvitationOrder(GQLObject):
   field: EnterpriseAdministratorInvitationOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class DraftPullRequestReviewThread(GQLObject):
   path: str ##NON NULL
   line: int ##NON NULL
   side: DiffSide
   startLine: int
   startSide: DiffSide
   body: str ##NON NULL

class DismissRepositoryVulnerabilityAlertInput(GQLObject):
   repositoryVulnerabilityAlertId: ID ##NON NULL
   dismissReason: DismissReason ##NON NULL
   clientMutationId: str

class DiscussionPollOptionOrder(GQLObject):
   field: DiscussionPollOptionOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class DisablePullRequestAutoMergeInput(GQLObject):
   pullRequestId: ID ##NON NULL
   clientMutationId: str

class DeployKey(GQLObject):
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   key: str ##NON NULL
   readOnly: bool ##NON NULL
   title: str ##NON NULL
   verified: bool ##NON NULL

class DeleteVerifiableDomainInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteTeamDiscussionInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteTeamDiscussionCommentInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteRefInput(GQLObject):
   refId: ID ##NON NULL
   clientMutationId: str

class DeletePullRequestReviewCommentInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteProjectV2ItemInput(GQLObject):
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   clientMutationId: str

class DeleteProjectNextItemInput(GQLObject):
   projectId: ID
   itemId: ID
   clientMutationId: str

class DeleteProjectColumnInput(GQLObject):
   columnId: ID ##NON NULL
   clientMutationId: str

class DeleteLinkedBranchInput(GQLObject):
   linkedBranchId: ID ##NON NULL
   clientMutationId: str

class DeleteIssueCommentPayload(GQLObject):
   clientMutationId: str

class DeleteIpAllowListEntryInput(GQLObject):
   ipAllowListEntryId: ID ##NON NULL
   clientMutationId: str

class DeleteEnvironmentInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteDiscussionCommentInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteDeploymentInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteBranchProtectionRuleInput(GQLObject):
   branchProtectionRuleId: ID ##NON NULL
   clientMutationId: str

class DeclineTopicSuggestionInput(GQLObject):
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   reason: TopicSuggestionDeclineReason ##NON NULL
   clientMutationId: str

class CreateTeamDiscussionCommentInput(GQLObject):
   discussionId: ID ##NON NULL
   body: str ##NON NULL
   clientMutationId: str

class CreateSponsorsTierInput(GQLObject):
   sponsorableId: ID
   sponsorableLogin: str
   amount: int ##NON NULL
   isRecurring: bool
   repositoryId: ID
   repositoryOwnerLogin: str
   repositoryName: str
   welcomeMessage: str
   description: str ##NON NULL
   publish: bool
   clientMutationId: str

class CreateRepositoryInput(GQLObject):
   name: str ##NON NULL
   ownerId: ID
   description: str
   visibility: RepositoryVisibility ##NON NULL
   template: bool
   homepageUrl: URI
   hasWikiEnabled: bool
   hasIssuesEnabled: bool
   teamId: ID
   clientMutationId: str

class CreatePullRequestInput(GQLObject):
   repositoryId: ID ##NON NULL
   baseRefName: str ##NON NULL
   headRefName: str ##NON NULL
   headRepositoryId: ID
   title: str ##NON NULL
   body: str
   maintainerCanModify: bool
   draft: bool
   clientMutationId: str

class CreateProjectInput(GQLObject):
   ownerId: ID ##NON NULL
   name: str ##NON NULL
   body: str
   template: ProjectTemplate
   repositoryIds: ID ##NON NULL ##LIST
   clientMutationId: str

class CreateLinkedBranchInput(GQLObject):
   issueId: ID ##NON NULL
   oid: GitObjectID ##NON NULL
   name: str
   repositoryId: ID
   clientMutationId: str

class CreateIpAllowListEntryInput(GQLObject):
   ownerId: ID ##NON NULL
   allowListValue: str ##NON NULL
   name: str
   isActive: bool ##NON NULL
   clientMutationId: str

class CreateEnterpriseOrganizationInput(GQLObject):
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   profileName: str ##NON NULL
   billingEmail: str ##NON NULL
   adminLogins: str ##NON NULL ##LIST
   clientMutationId: str

class CreateCheckSuiteInput(GQLObject):
   repositoryId: ID ##NON NULL
   headSha: GitObjectID ##NON NULL
   clientMutationId: str

class ConvertPullRequestToDraftInput(GQLObject):
   pullRequestId: ID ##NON NULL
   clientMutationId: str

class ContributionOrder(GQLObject):
   direction: OrderDirection ##NON NULL

class ContributionCalendarDay(GQLObject):
   color: str ##NON NULL
   contributionCount: int ##NON NULL
   contributionLevel: ContributionLevel ##NON NULL
   date: Date ##NON NULL
   weekday: int ##NON NULL

class CommitMessage(GQLObject):
   headline: str ##NON NULL
   body: str

class CommitAuthor(GQLObject):
   id: ID
   emails: str ##NON NULL ##LIST

class ClosePullRequestInput(GQLObject):
   pullRequestId: ID ##NON NULL
   clientMutationId: str

class Closable(GQLObject):
   closed: bool ##NON NULL
   closedAt: DateTime

class CloneProjectInput(GQLObject):
   targetOwnerId: ID ##NON NULL
   sourceId: ID ##NON NULL
   includeWorkflows: bool ##NON NULL
   name: str ##NON NULL
   body: str
   public: bool
   clientMutationId: str

class ClearLabelsFromLabelableInput(GQLObject):
   labelableId: ID ##NON NULL
   clientMutationId: str

class CheckSuiteAutoTriggerPreference(GQLObject):
   appId: ID ##NON NULL
   setting: bool ##NON NULL

class CheckRunStateCount(GQLObject):
   count: int ##NON NULL
   state: CheckRunState ##NON NULL

class CheckRunFilter(GQLObject):
   checkType: CheckRunType
   appId: int
   checkName: str
   status: CheckStatusState
   statuses: CheckStatusState ##NON NULL ##LIST
   conclusions: CheckConclusionState ##NON NULL ##LIST

class CheckAnnotationRange(GQLObject):
   startLine: int ##NON NULL
   startColumn: int
   endLine: int ##NON NULL
   endColumn: int

class ChangeUserStatusInput(GQLObject):
   emoji: str
   message: str
   organizationId: ID
   limitedAvailability: bool
   expiresAt: DateTime
   clientMutationId: str

class CancelEnterpriseAdminInvitationInput(GQLObject):
   invitationId: ID ##NON NULL
   clientMutationId: str

class CVSS(GQLObject):
   score: float ##NON NULL
   vectorString: str

class Bot(GQLObject):
   avatarUrl: XVGUIavatarUrl_URI_Field
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   login: str ##NON NULL
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL

class ArchiveRepositoryInput(GQLObject):
   repositoryId: ID ##NON NULL
   clientMutationId: str

class ApproveVerifiableDomainInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class AddVerifiableDomainInput(GQLObject):
   ownerId: ID ##NON NULL
   domain: URI ##NON NULL
   clientMutationId: str

class AddStarInput(GQLObject):
   starrableId: ID ##NON NULL
   clientMutationId: str

class AddPullRequestReviewThreadInput(GQLObject):
   path: str ##NON NULL
   body: str ##NON NULL
   pullRequestId: ID
   pullRequestReviewId: ID
   line: int ##NON NULL
   side: DiffSide
   startLine: int
   startSide: DiffSide
   clientMutationId: str

class AddProjectV2ItemByIdInput(GQLObject):
   projectId: ID ##NON NULL
   contentId: ID ##NON NULL
   clientMutationId: str

class AddProjectNextItemInput(GQLObject):
   projectId: ID
   contentId: ID
   clientMutationId: str

class AddProjectColumnInput(GQLObject):
   projectId: ID ##NON NULL
   name: str ##NON NULL
   clientMutationId: str

class AddLabelsToLabelableInput(GQLObject):
   labelableId: ID ##NON NULL
   labelIds: ID ##NON NULL ##LIST
   clientMutationId: str

class AddEnterpriseSupportEntitlementInput(GQLObject):
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class AddDiscussionPollVoteInput(GQLObject):
   pollOptionId: ID ##NON NULL
   clientMutationId: str

class AddCommentInput(GQLObject):
   subjectId: ID ##NON NULL
   body: str ##NON NULL
   clientMutationId: str

class ActorLocation(GQLObject):
   city: str
   country: str
   countryCode: str
   region: str
   regionCode: str

class Actor(GQLObject):
   avatarUrl: KDKPRavatarUrl_URI_Field
   login: str ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class AcceptEnterpriseAdministratorInvitationInput(GQLObject):
   invitationId: ID ##NON NULL
   clientMutationId: str

class AbortQueuedMigrationsInput(GQLObject):
   ownerId: ID ##NON NULL
   clientMutationId: str
