from typing import Generic, Union, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from typing import NewType
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

class Votable(GQLObject):
   upvoteCount: int
   viewerCanUpvote: bool
   viewerHasUpvoted: bool

class VerifiableDomainOrder(GQLObject):
   field: VerifiableDomainOrderField
   direction: OrderDirection

class UserEmailMetadata(GQLObject):
   primary: bool
   type: str
   value: str

class UpdateTeamsRepositoryInput(GQLObject):
   repositoryId: ID
   teamIds: list[ID]
   permission: RepositoryPermission
   clientMutationId: str

class UpdateTeamDiscussionCommentInput(GQLObject):
   id: ID
   body: str
   bodyVersion: str
   clientMutationId: str

class UpdateSponsorshipPreferencesInput(GQLObject):
   sponsorId: ID
   sponsorLogin: str
   sponsorableId: ID
   sponsorableLogin: str
   receiveEmails: bool
   privacyLevel: SponsorshipPrivacy
   clientMutationId: str

class UpdateRepositoryInput(GQLObject):
   repositoryId: ID
   name: str
   description: str
   template: bool
   homepageUrl: URI
   hasWikiEnabled: bool
   hasIssuesEnabled: bool
   hasProjectsEnabled: bool
   hasDiscussionsEnabled: bool
   clientMutationId: str

class UpdatePullRequestReviewInput(GQLObject):
   pullRequestReviewId: ID
   body: str
   clientMutationId: str

class UpdatePullRequestInput(GQLObject):
   pullRequestId: ID
   baseRefName: str
   title: str
   body: str
   state: PullRequestUpdateState
   maintainerCanModify: bool
   assigneeIds: list[ID]
   milestoneId: ID
   labelIds: list[ID]
   projectIds: list[ID]
   clientMutationId: str

class UpdateProjectV2ItemPositionInput(GQLObject):
   projectId: ID
   itemId: ID
   afterId: ID
   clientMutationId: str

class UpdateProjectV2DraftIssueInput(GQLObject):
   draftIssueId: ID
   title: str
   body: str
   assigneeIds: list[ID]
   clientMutationId: str

class UpdateProjectColumnInput(GQLObject):
   projectColumnId: ID
   name: str
   clientMutationId: str

class UpdateParametersInput(GQLObject):
   updateAllowsFetchAndMerge: bool

class UpdateOrganizationWebCommitSignoffSettingInput(GQLObject):
   organizationId: ID
   webCommitSignoffRequired: bool
   clientMutationId: str

class UpdateNotificationRestrictionSettingInput(GQLObject):
   ownerId: ID
   settingValue: NotificationRestrictionSettingValue
   clientMutationId: str

class UpdateIssueCommentInput(GQLObject):
   id: ID
   body: str
   clientMutationId: str

class UpdateIpAllowListEntryInput(GQLObject):
   ipAllowListEntryId: ID
   allowListValue: str
   name: str
   isActive: bool
   clientMutationId: str

class UpdateEnvironmentInput(GQLObject):
   environmentId: ID
   waitTimer: int
   reviewers: list[ID]
   clientMutationId: str

class UpdateEnterpriseTeamDiscussionsSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseProfileInput(GQLObject):
   enterpriseId: ID
   name: str
   description: str
   websiteUrl: str
   location: str
   clientMutationId: str

class UpdateEnterpriseOwnerOrganizationRoleInput(GQLObject):
   enterpriseId: ID
   organizationId: ID
   organizationRole: RoleInOrganization
   clientMutationId: str

class UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanMakePurchasesSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseMembersCanMakePurchasesSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanCreateRepositoriesSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseMembersCanCreateRepositoriesSettingValue
   membersCanCreateRepositoriesPolicyEnabled: bool
   membersCanCreatePublicRepositories: bool
   membersCanCreatePrivateRepositories: bool
   membersCanCreateInternalRepositories: bool
   clientMutationId: str

class UpdateEnterpriseDefaultRepositoryPermissionSettingInput(GQLObject):
   enterpriseId: ID
   settingValue: EnterpriseDefaultRepositoryPermissionSettingValue
   clientMutationId: str

class UpdateEnterpriseAdministratorRolePayload(GQLObject):
   clientMutationId: str
   message: str

class UpdateDiscussionInput(GQLObject):
   discussionId: ID
   title: str
   body: str
   categoryId: ID
   clientMutationId: str

class UpdatableComment(GQLObject):
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]

class UnresolveReviewThreadInput(GQLObject):
   threadId: ID
   clientMutationId: str

class UnminimizeCommentInput(GQLObject):
   subjectId: ID
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

class TagNamePatternParametersInput(GQLObject):
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
   avatarUrl: CMDBK_URI_Field
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

class AcceptTopicSuggestionInput(GQLObject):
   repositoryId: ID
   name: str
   clientMutationId: str

class AbortQueuedMigrationsPayload(GQLObject):
   clientMutationId: str
   success: bool

class EnterpriseServerUserAccountEmail(GQLObject):
   createdAt: DateTime
   email: str
   id: ID
   isPrimary: bool
   updatedAt: DateTime
   userAccount: NewType('EnterpriseServerUserAccount', GQLObject) ## Circular Reference for EnterpriseServerUserAccount

class EnterpriseServerUserAccountEmailEdge(GQLObject):
   cursor: str
   node: EnterpriseServerUserAccountEmail

class list_EnterpriseServerUserAccountEmailEdge(list, EnterpriseServerUserAccountEmailEdge): pass

class list_EnterpriseServerUserAccountEmail(list, EnterpriseServerUserAccountEmail): pass

class EnterpriseServerUserAccountEmailConnection(GQLObject):
   edges: list_EnterpriseServerUserAccountEmailEdge[EnterpriseServerUserAccountEmailEdge]
   nodes: list_EnterpriseServerUserAccountEmail[EnterpriseServerUserAccountEmail]
   pageInfo: PageInfo
   totalCount: int

class AZVYJ_EnterpriseServerUserAccountEmailConnection_Field(EnterpriseServerUserAccountEmailConnection):
   class EnterpriseServerUserAccountEmailConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: EnterpriseServerUserAccountEmailOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerUserAccountEmailConnectionArgs



class EnterpriseServerUserAccount(GQLObject):
   createdAt: DateTime
   emails: AZVYJ_EnterpriseServerUserAccountEmailConnection_Field
   enterpriseServerInstallation: NewType('EnterpriseServerInstallation', GQLObject) ## Circular Reference for EnterpriseServerInstallation
   id: ID
   isSiteAdmin: bool
   login: str
   profileName: str
   remoteCreatedAt: DateTime
   remoteUserId: int
   updatedAt: DateTime

class EnterpriseServerUserAccountEdge(GQLObject):
   cursor: str
   node: EnterpriseServerUserAccount

class list_EnterpriseServerUserAccountEdge(list, EnterpriseServerUserAccountEdge): pass

class list_EnterpriseServerUserAccount(list, EnterpriseServerUserAccount): pass

class EnterpriseServerUserAccountConnection(GQLObject):
   edges: list_EnterpriseServerUserAccountEdge[EnterpriseServerUserAccountEdge]
   nodes: list_EnterpriseServerUserAccount[EnterpriseServerUserAccount]
   pageInfo: PageInfo
   totalCount: int

class EnterpriseServerUserAccountsUpload(GQLObject):
   createdAt: DateTime
   enterprise: NewType('Enterprise', GQLObject) ## Circular Reference for Enterprise
   enterpriseServerInstallation: NewType('EnterpriseServerInstallation', GQLObject) ## Circular Reference for EnterpriseServerInstallation
   id: ID
   name: str
   syncState: EnterpriseServerUserAccountsUploadSyncState
   updatedAt: DateTime

class EnterpriseServerUserAccountsUploadEdge(GQLObject):
   cursor: str
   node: EnterpriseServerUserAccountsUpload

class list_EnterpriseServerUserAccountsUploadEdge(list, EnterpriseServerUserAccountsUploadEdge): pass

class list_EnterpriseServerUserAccountsUpload(list, EnterpriseServerUserAccountsUpload): pass

class EnterpriseServerUserAccountsUploadConnection(GQLObject):
   edges: list_EnterpriseServerUserAccountsUploadEdge[EnterpriseServerUserAccountsUploadEdge]
   nodes: list_EnterpriseServerUserAccountsUpload[EnterpriseServerUserAccountsUpload]
   pageInfo: PageInfo
   totalCount: int

class ZHDYC_EnterpriseServerUserAccountConnection_Field(EnterpriseServerUserAccountConnection):
   class EnterpriseServerUserAccountConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: EnterpriseServerUserAccountOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerUserAccountConnectionArgs



class OCBVK_EnterpriseServerUserAccountsUploadConnection_Field(EnterpriseServerUserAccountsUploadConnection):
   class EnterpriseServerUserAccountsUploadConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: EnterpriseServerUserAccountsUploadOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerUserAccountsUploadConnectionArgs



class EnterpriseServerInstallation(GQLObject):
   createdAt: DateTime
   customerName: str
   hostName: str
   id: ID
   isConnected: bool
   updatedAt: DateTime
   userAccounts: ZHDYC_EnterpriseServerUserAccountConnection_Field
   userAccountsUploads: OCBVK_EnterpriseServerUserAccountsUploadConnection_Field

class EnterpriseServerInstallationMembershipEdge(GQLObject):
   cursor: str
   node: EnterpriseServerInstallation
   role: EnterpriseUserAccountMembershipRole

class list_EnterpriseServerInstallationMembershipEdge(list, EnterpriseServerInstallationMembershipEdge): pass

class list_EnterpriseServerInstallation(list, EnterpriseServerInstallation): pass

class EnterpriseServerInstallationMembershipConnection(GQLObject):
   edges: list_EnterpriseServerInstallationMembershipEdge[EnterpriseServerInstallationMembershipEdge]
   nodes: list_EnterpriseServerInstallation[EnterpriseServerInstallation]
   pageInfo: PageInfo
   totalCount: int

class UserEdge(GQLObject):
   cursor: str
   node: NewType('User', GQLObject) ## Circular Reference for User

class list_UserEdge(list, UserEdge): pass

class list_GQLObject(list, GQLObject): pass

class UserConnection(GQLObject):
   edges: list_UserEdge[UserEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for User
   pageInfo: PageInfo
   totalCount: int

class AutoMergeRequest(GQLObject):
   authorEmail: str
   commitBody: str
   commitHeadline: str
   enabledAt: DateTime
   enabledBy: Actor
   mergeMethod: PullRequestMergeMethod
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class BranchProtectionRuleConflict(GQLObject):
   branchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   conflictingBranchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   ref: NewType('Ref', GQLObject) ## Circular Reference for Ref

class BranchProtectionRuleConflictEdge(GQLObject):
   cursor: str
   node: BranchProtectionRuleConflict

class list_BranchProtectionRuleConflictEdge(list, BranchProtectionRuleConflictEdge): pass

class list_BranchProtectionRuleConflict(list, BranchProtectionRuleConflict): pass

class BranchProtectionRuleConflictConnection(GQLObject):
   edges: list_BranchProtectionRuleConflictEdge[BranchProtectionRuleConflictEdge]
   nodes: list_BranchProtectionRuleConflict[BranchProtectionRuleConflict]
   pageInfo: PageInfo
   totalCount: int

class TeamEdge(GQLObject):
   cursor: str
   node: NewType('Team', GQLObject) ## Circular Reference for Team

class list_TeamEdge(list, TeamEdge): pass

class TeamConnection(GQLObject):
   edges: list_TeamEdge[TeamEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Team
   pageInfo: PageInfo
   totalCount: int

class Mannequin(GQLObject):
   avatarUrl: BFFZN_URI_Field
   claimant: NewType('User', GQLObject) ## Circular Reference for User
   createdAt: DateTime
   databaseId: int
   email: str
   id: ID
   login: str
   resourcePath: URI
   updatedAt: DateTime
   url: URI

class Reactor(GQLObject): 
   pass

class ReactorEdge(GQLObject):
   cursor: str
   node: Reactor
   reactedAt: DateTime

class list_ReactorEdge(list, ReactorEdge): pass

class list_Reactor(list, Reactor): pass

class ReactorConnection(GQLObject):
   edges: list_ReactorEdge[ReactorEdge]
   nodes: list_Reactor[Reactor]
   pageInfo: PageInfo
   totalCount: int

class Reaction(GQLObject):
   content: ReactionContent
   createdAt: DateTime
   databaseId: int
   id: ID
   reactable: NewType('Reactable', GQLObject) ## Circular Reference for Reactable
   user: NewType('User', GQLObject) ## Circular Reference for User

class ReactionEdge(GQLObject):
   cursor: str
   node: Reaction

class list_ReactionEdge(list, ReactionEdge): pass

class list_Reaction(list, Reaction): pass

class ReactionConnection(GQLObject):
   edges: list_ReactionEdge[ReactionEdge]
   nodes: list_Reaction[Reaction]
   pageInfo: PageInfo
   totalCount: int
   viewerHasReacted: bool

class JGAUM_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class Reactable(GQLObject):
   databaseId: int
   id: ID
   reactionGroups: list_GQLObject[GQLObject] ## Circular Reference for ReactionGroup
   reactions: JGAUM_ReactionConnection_Field
   viewerCanReact: bool

class ReactingUserEdge(GQLObject):
   cursor: str
   node: NewType('User', GQLObject) ## Circular Reference for User
   reactedAt: DateTime

class list_ReactingUserEdge(list, ReactingUserEdge): pass

class ReactingUserConnection(GQLObject):
   edges: list_ReactingUserEdge[ReactingUserEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for User
   pageInfo: PageInfo
   totalCount: int

class EACWK_ReactorConnection_Field(ReactorConnection):
   class ReactorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ReactorConnectionArgs



class ReactionGroup(GQLObject):
   content: ReactionContent
   createdAt: DateTime
   reactors: EACWK_ReactorConnection_Field
   subject: Reactable
   viewerHasReacted: bool

class UserContentEdit(GQLObject):
   createdAt: DateTime
   deletedAt: DateTime
   deletedBy: Actor
   diff: str
   editedAt: DateTime
   editor: Actor
   id: ID
   updatedAt: DateTime

class UserContentEditEdge(GQLObject):
   cursor: str
   node: UserContentEdit

class list_UserContentEditEdge(list, UserContentEditEdge): pass

class list_UserContentEdit(list, UserContentEdit): pass

class UserContentEditConnection(GQLObject):
   edges: list_UserContentEditEdge[UserContentEditEdge]
   nodes: list_UserContentEdit[UserContentEdit]
   pageInfo: PageInfo
   totalCount: int

class list_ReactionGroup(list, ReactionGroup): pass

class TVNJL_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class ETDMW_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class TeamDiscussionComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyText: str
   bodyVersion: str
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   discussion: NewType('TeamDiscussion', GQLObject) ## Circular Reference for TeamDiscussion
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   lastEditedAt: DateTime
   number: int
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: TVNJL_ReactionConnection_Field
   resourcePath: URI
   updatedAt: DateTime
   url: URI
   userContentEdits: ETDMW_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanReact: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]
   viewerDidAuthor: bool

class TeamDiscussionCommentEdge(GQLObject):
   cursor: str
   node: TeamDiscussionComment

class list_TeamDiscussionCommentEdge(list, TeamDiscussionCommentEdge): pass

class list_TeamDiscussionComment(list, TeamDiscussionComment): pass

class TeamDiscussionCommentConnection(GQLObject):
   edges: list_TeamDiscussionCommentEdge[TeamDiscussionCommentEdge]
   nodes: list_TeamDiscussionComment[TeamDiscussionComment]
   pageInfo: PageInfo
   totalCount: int

class RXIEP_TeamDiscussionCommentConnection_Field(TeamDiscussionCommentConnection):
   class TeamDiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: TeamDiscussionCommentOrder
      fromComment: int

   _args: TeamDiscussionCommentConnectionArgs



class BYYXU_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class WUXHL_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class TeamDiscussion(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyText: str
   bodyVersion: str
   comments: RXIEP_TeamDiscussionCommentConnection_Field
   commentsResourcePath: URI
   commentsUrl: URI
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   isPinned: bool
   isPrivate: bool
   lastEditedAt: DateTime
   number: int
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: BYYXU_ReactionConnection_Field
   resourcePath: URI
   team: NewType('Team', GQLObject) ## Circular Reference for Team
   title: str
   updatedAt: DateTime
   url: URI
   userContentEdits: WUXHL_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanPin: bool
   viewerCanReact: bool
   viewerCanSubscribe: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]
   viewerDidAuthor: bool
   viewerSubscription: SubscriptionState

class TeamDiscussionEdge(GQLObject):
   cursor: str
   node: TeamDiscussion

class list_TeamDiscussionEdge(list, TeamDiscussionEdge): pass

class list_TeamDiscussion(list, TeamDiscussion): pass

class TeamDiscussionConnection(GQLObject):
   edges: list_TeamDiscussionEdge[TeamDiscussionEdge]
   nodes: list_TeamDiscussion[TeamDiscussion]
   pageInfo: PageInfo
   totalCount: int

class OrganizationInvitation(GQLObject):
   createdAt: DateTime
   email: str
   id: ID
   invitationSource: OrganizationInvitationSource
   invitationType: OrganizationInvitationType
   invitee: NewType('User', GQLObject) ## Circular Reference for User
   inviter: NewType('User', GQLObject) ## Circular Reference for User
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   role: OrganizationInvitationRole

class OrganizationInvitationEdge(GQLObject):
   cursor: str
   node: OrganizationInvitation

class list_OrganizationInvitationEdge(list, OrganizationInvitationEdge): pass

class list_OrganizationInvitation(list, OrganizationInvitation): pass

class OrganizationInvitationConnection(GQLObject):
   edges: list_OrganizationInvitationEdge[OrganizationInvitationEdge]
   nodes: list_OrganizationInvitation[OrganizationInvitation]
   pageInfo: PageInfo
   totalCount: int

class UserStatus(GQLObject):
   createdAt: DateTime
   emoji: str
   emojiHTML: HTML
   expiresAt: DateTime
   id: ID
   indicatesLimitedAvailability: bool
   message: str
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   updatedAt: DateTime
   user: NewType('User', GQLObject) ## Circular Reference for User

class UserStatusEdge(GQLObject):
   cursor: str
   node: UserStatus

class list_UserStatusEdge(list, UserStatusEdge): pass

class list_UserStatus(list, UserStatus): pass

class UserStatusConnection(GQLObject):
   edges: list_UserStatusEdge[UserStatusEdge]
   nodes: list_UserStatus[UserStatus]
   pageInfo: PageInfo
   totalCount: int

class TeamMemberEdge(GQLObject):
   cursor: str
   memberAccessResourcePath: URI
   memberAccessUrl: URI
   node: NewType('User', GQLObject) ## Circular Reference for User
   role: TeamMemberRole

class list_TeamMemberEdge(list, TeamMemberEdge): pass

class TeamMemberConnection(GQLObject):
   edges: list_TeamMemberEdge[TeamMemberEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for User
   pageInfo: PageInfo
   totalCount: int

class ProjectV2Field(GQLObject):
   createdAt: DateTime
   dataType: ProjectV2FieldType
   databaseId: int
   id: ID
   name: str
   project: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2
   updatedAt: DateTime

class list_ProjectV2IterationFieldIteration(list, ProjectV2IterationFieldIteration): pass

class ProjectV2IterationFieldConfiguration(GQLObject):
   completedIterations: list_ProjectV2IterationFieldIteration[ProjectV2IterationFieldIteration]
   duration: int
   iterations: list_ProjectV2IterationFieldIteration[ProjectV2IterationFieldIteration]
   startDay: int

class ProjectV2IterationField(GQLObject):
   configuration: ProjectV2IterationFieldConfiguration
   createdAt: DateTime
   dataType: ProjectV2FieldType
   databaseId: int
   id: ID
   name: str
   project: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2
   updatedAt: DateTime

class AGFLW_ProjectV2SingleSelectFieldOption_Field(ProjectV2SingleSelectFieldOption):
   class ProjectV2SingleSelectFieldOptionArgs(GQLArgsSet, GQLObject):
      names: list[NonNull_str]

   _args: ProjectV2SingleSelectFieldOptionArgs



class list_ProjectV2SingleSelectFieldOption(list, ProjectV2SingleSelectFieldOption): pass

class ProjectV2SingleSelectField(GQLObject):
   createdAt: DateTime
   dataType: ProjectV2FieldType
   databaseId: int
   id: ID
   name: str
   options: AGFLW_ProjectV2SingleSelectFieldOption_Field
   project: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2
   updatedAt: DateTime

class ProjectV2FieldConfiguration(GQLObject): 
   pass

class ProjectV2FieldConfigurationEdge(GQLObject):
   cursor: str
   node: ProjectV2FieldConfiguration

class list_ProjectV2FieldConfigurationEdge(list, ProjectV2FieldConfigurationEdge): pass

class list_ProjectV2FieldConfiguration(list, ProjectV2FieldConfiguration): pass

class ProjectV2FieldConfigurationConnection(GQLObject):
   edges: list_ProjectV2FieldConfigurationEdge[ProjectV2FieldConfigurationEdge]
   nodes: list_ProjectV2FieldConfiguration[ProjectV2FieldConfiguration]
   pageInfo: PageInfo
   totalCount: int

class ProjectV2Edge(GQLObject):
   cursor: str
   node: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2

class list_ProjectV2Edge(list, ProjectV2Edge): pass

class ProjectV2Connection(GQLObject):
   edges: list_ProjectV2Edge[ProjectV2Edge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for ProjectV2
   pageInfo: PageInfo
   totalCount: int

class GSJBU_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class ALFYF_ProjectV2ItemConnection_Field(Generic[ProjectV2ItemConnection]):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class LKYIX_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class DraftIssue(GQLObject):
   assignees: GSJBU_UserConnection_Field
   body: str
   bodyHTML: HTML
   bodyText: str
   createdAt: DateTime
   creator: Actor
   id: ID
   projectV2Items: ALFYF_ProjectV2ItemConnection_Field ## Circular Reference for ProjectV2ItemConnection
   projectsV2: LKYIX_ProjectV2Connection_Field
   title: str
   updatedAt: DateTime

class BranchProtectionRuleEdge(GQLObject):
   cursor: str
   node: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule

class list_BranchProtectionRuleEdge(list, BranchProtectionRuleEdge): pass

class BranchProtectionRuleConnection(GQLObject):
   edges: list_BranchProtectionRuleEdge[BranchProtectionRuleEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for BranchProtectionRule
   pageInfo: PageInfo
   totalCount: int

class list_RepositoryCodeownersError(list, RepositoryCodeownersError): pass

class RepositoryCodeowners(GQLObject):
   errors: list_RepositoryCodeownersError[RepositoryCodeownersError]

class PermissionGranter(GQLObject): 
   pass

class PermissionSource(GQLObject):
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   permission: DefaultRepositoryPermissionField
   source: PermissionGranter

class list_PermissionSource(list, PermissionSource): pass

class RepositoryCollaboratorEdge(GQLObject):
   cursor: str
   node: NewType('User', GQLObject) ## Circular Reference for User
   permission: RepositoryPermission
   permissionSources: list_PermissionSource[PermissionSource]

class list_RepositoryCollaboratorEdge(list, RepositoryCollaboratorEdge): pass

class RepositoryCollaboratorConnection(GQLObject):
   edges: list_RepositoryCollaboratorEdge[RepositoryCollaboratorEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for User
   pageInfo: PageInfo
   totalCount: int

class DeployKeyEdge(GQLObject):
   cursor: str
   node: DeployKey

class list_DeployKeyEdge(list, DeployKeyEdge): pass

class list_DeployKey(list, DeployKey): pass

class DeployKeyConnection(GQLObject):
   edges: list_DeployKeyEdge[DeployKeyEdge]
   nodes: list_DeployKey[DeployKey]
   pageInfo: PageInfo
   totalCount: int

class DeploymentStatus(GQLObject):
   createdAt: DateTime
   creator: Actor
   deployment: NewType('Deployment', GQLObject) ## Circular Reference for Deployment
   description: str
   environmentUrl: URI
   id: ID
   logUrl: URI
   state: DeploymentStatusState
   updatedAt: DateTime

class DeploymentStatusEdge(GQLObject):
   cursor: str
   node: DeploymentStatus

class list_DeploymentStatusEdge(list, DeploymentStatusEdge): pass

class list_DeploymentStatus(list, DeploymentStatus): pass

class DeploymentStatusConnection(GQLObject):
   edges: list_DeploymentStatusEdge[DeploymentStatusEdge]
   nodes: list_DeploymentStatus[DeploymentStatus]
   pageInfo: PageInfo
   totalCount: int

class BMXYG_DeploymentStatusConnection_Field(DeploymentStatusConnection):
   class DeploymentStatusConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentStatusConnectionArgs



class Deployment(GQLObject):
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   commitOid: str
   createdAt: DateTime
   creator: Actor
   databaseId: int
   description: str
   environment: str
   id: ID
   latestEnvironment: str
   latestStatus: DeploymentStatus
   originalEnvironment: str
   payload: str
   ref: NewType('Ref', GQLObject) ## Circular Reference for Ref
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   state: DeploymentState
   statuses: BMXYG_DeploymentStatusConnection_Field
   task: str
   updatedAt: DateTime

class DeploymentEdge(GQLObject):
   cursor: str
   node: Deployment

class list_DeploymentEdge(list, DeploymentEdge): pass

class list_Deployment(list, Deployment): pass

class DeploymentConnection(GQLObject):
   edges: list_DeploymentEdge[DeploymentEdge]
   nodes: list_Deployment[Deployment]
   pageInfo: PageInfo
   totalCount: int

class DiscussionCommentEdge(GQLObject):
   cursor: str
   node: NewType('DiscussionComment', GQLObject) ## Circular Reference for DiscussionComment

class list_DiscussionCommentEdge(list, DiscussionCommentEdge): pass

class DiscussionCommentConnection(GQLObject):
   edges: list_DiscussionCommentEdge[DiscussionCommentEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for DiscussionComment
   pageInfo: PageInfo
   totalCount: int

class VLUIC_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class QXRLH_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DiscussionCommentConnectionArgs



class TZVNM_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class DiscussionComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyText: str
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   deletedAt: DateTime
   discussion: NewType('Discussion', GQLObject) ## Circular Reference for Discussion
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   isAnswer: bool
   isMinimized: bool
   lastEditedAt: DateTime
   minimizedReason: str
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: VLUIC_ReactionConnection_Field
   replies: QXRLH_DiscussionCommentConnection_Field
   replyTo: NewType('DiscussionComment', GQLObject) ## Circular Reference for DiscussionComment
   resourcePath: URI
   updatedAt: DateTime
   upvoteCount: int
   url: URI
   userContentEdits: TZVNM_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanMarkAsAnswer: bool
   viewerCanMinimize: bool
   viewerCanReact: bool
   viewerCanUnmarkAsAnswer: bool
   viewerCanUpdate: bool
   viewerCanUpvote: bool
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]
   viewerDidAuthor: bool
   viewerHasUpvoted: bool

class DiscussionCategory(GQLObject):
   createdAt: DateTime
   description: str
   emoji: str
   emojiHTML: HTML
   id: ID
   isAnswerable: bool
   name: str
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   slug: str
   updatedAt: DateTime

class IssueEdge(GQLObject):
   cursor: str
   node: NewType('Issue', GQLObject) ## Circular Reference for Issue

class list_IssueEdge(list, IssueEdge): pass

class IssueConnection(GQLObject):
   edges: list_IssueEdge[IssueEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Issue
   pageInfo: PageInfo
   totalCount: int

class NonNull_IssueState(GQLObject): pass

class UVKOP_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueOrder
      labels: list[NonNull_str]
      states: list[NonNull_IssueState]
      filterBy: IssueFilters
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class NonNull_PullRequestState(GQLObject): pass

class NVWYL_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      states: list[NonNull_PullRequestState]
      labels: list[NonNull_str]
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class Label(GQLObject):
   color: str
   createdAt: DateTime
   description: str
   id: ID
   isDefault: bool
   issues: UVKOP_IssueConnection_Field
   name: str
   pullRequests: NVWYL_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   resourcePath: URI
   updatedAt: DateTime
   url: URI

class LabelEdge(GQLObject):
   cursor: str
   node: Label

class list_LabelEdge(list, LabelEdge): pass

class list_Label(list, Label): pass

class LabelConnection(GQLObject):
   edges: list_LabelEdge[LabelEdge]
   nodes: list_Label[Label]
   pageInfo: PageInfo
   totalCount: int

class DiscussionPollOption(GQLObject):
   id: ID
   option: str
   poll: NewType('DiscussionPoll', GQLObject) ## Circular Reference for DiscussionPoll
   totalVoteCount: int
   viewerHasVoted: bool

class DiscussionPollOptionEdge(GQLObject):
   cursor: str
   node: DiscussionPollOption

class list_DiscussionPollOptionEdge(list, DiscussionPollOptionEdge): pass

class list_DiscussionPollOption(list, DiscussionPollOption): pass

class DiscussionPollOptionConnection(GQLObject):
   edges: list_DiscussionPollOptionEdge[DiscussionPollOptionEdge]
   nodes: list_DiscussionPollOption[DiscussionPollOption]
   pageInfo: PageInfo
   totalCount: int

class FFVSZ_DiscussionPollOptionConnection_Field(DiscussionPollOptionConnection):
   class DiscussionPollOptionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionPollOptionOrder

   _args: DiscussionPollOptionConnectionArgs



class DiscussionPoll(GQLObject):
   discussion: NewType('Discussion', GQLObject) ## Circular Reference for Discussion
   id: ID
   options: FFVSZ_DiscussionPollOptionConnection_Field
   question: str
   totalVoteCount: int
   viewerCanVote: bool
   viewerHasVoted: bool

class TAJTP_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DiscussionCommentConnectionArgs



class EGRCS_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class CIFHG_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class VBSJH_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class Discussion(GQLObject):
   activeLockReason: LockReason
   answer: DiscussionComment
   answerChosenAt: DateTime
   answerChosenBy: Actor
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyText: str
   category: DiscussionCategory
   closed: bool
   closedAt: DateTime
   comments: TAJTP_DiscussionCommentConnection_Field
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   labels: EGRCS_LabelConnection_Field
   lastEditedAt: DateTime
   locked: bool
   number: int
   poll: DiscussionPoll
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: CIFHG_ReactionConnection_Field
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   resourcePath: URI
   stateReason: DiscussionStateReason
   title: str
   updatedAt: DateTime
   upvoteCount: int
   url: URI
   userContentEdits: VBSJH_UserContentEditConnection_Field
   viewerCanClose: bool
   viewerCanDelete: bool
   viewerCanReact: bool
   viewerCanReopen: bool
   viewerCanSubscribe: bool
   viewerCanUpdate: bool
   viewerCanUpvote: bool
   viewerDidAuthor: bool
   viewerHasUpvoted: bool
   viewerSubscription: SubscriptionState

class DiscussionCategoryEdge(GQLObject):
   cursor: str
   node: DiscussionCategory

class list_DiscussionCategoryEdge(list, DiscussionCategoryEdge): pass

class list_DiscussionCategory(list, DiscussionCategory): pass

class DiscussionCategoryConnection(GQLObject):
   edges: list_DiscussionCategoryEdge[DiscussionCategoryEdge]
   nodes: list_DiscussionCategory[DiscussionCategory]
   pageInfo: PageInfo
   totalCount: int

class DiscussionEdge(GQLObject):
   cursor: str
   node: Discussion

class list_DiscussionEdge(list, DiscussionEdge): pass

class list_Discussion(list, Discussion): pass

class DiscussionConnection(GQLObject):
   edges: list_DiscussionEdge[DiscussionEdge]
   nodes: list_Discussion[Discussion]
   pageInfo: PageInfo
   totalCount: int

class DeploymentReviewer(GQLObject): 
   pass

class DeploymentReviewerEdge(GQLObject):
   cursor: str
   node: DeploymentReviewer

class list_DeploymentReviewerEdge(list, DeploymentReviewerEdge): pass

class list_DeploymentReviewer(list, DeploymentReviewer): pass

class DeploymentReviewerConnection(GQLObject):
   edges: list_DeploymentReviewerEdge[DeploymentReviewerEdge]
   nodes: list_DeploymentReviewer[DeploymentReviewer]
   pageInfo: PageInfo
   totalCount: int

class UTCCH_DeploymentReviewerConnection_Field(DeploymentReviewerConnection):
   class DeploymentReviewerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewerConnectionArgs



class DeploymentProtectionRule(GQLObject):
   databaseId: int
   reviewers: UTCCH_DeploymentReviewerConnection_Field
   timeout: int
   type: DeploymentProtectionRuleType

class DeploymentProtectionRuleEdge(GQLObject):
   cursor: str
   node: DeploymentProtectionRule

class list_DeploymentProtectionRuleEdge(list, DeploymentProtectionRuleEdge): pass

class list_DeploymentProtectionRule(list, DeploymentProtectionRule): pass

class DeploymentProtectionRuleConnection(GQLObject):
   edges: list_DeploymentProtectionRuleEdge[DeploymentProtectionRuleEdge]
   nodes: list_DeploymentProtectionRule[DeploymentProtectionRule]
   pageInfo: PageInfo
   totalCount: int

class WVTBY_DeploymentProtectionRuleConnection_Field(DeploymentProtectionRuleConnection):
   class DeploymentProtectionRuleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentProtectionRuleConnectionArgs



class Environment(GQLObject):
   databaseId: int
   id: ID
   name: str
   protectionRules: WVTBY_DeploymentProtectionRuleConnection_Field

class EnvironmentEdge(GQLObject):
   cursor: str
   node: Environment

class list_EnvironmentEdge(list, EnvironmentEdge): pass

class list_Environment(list, Environment): pass

class EnvironmentConnection(GQLObject):
   edges: list_EnvironmentEdge[EnvironmentEdge]
   nodes: list_Environment[Environment]
   pageInfo: PageInfo
   totalCount: int

class RepositoryEdge(GQLObject):
   cursor: str
   node: NewType('Repository', GQLObject) ## Circular Reference for Repository

class list_RepositoryEdge(list, RepositoryEdge): pass

class RepositoryConnection(GQLObject):
   edges: list_RepositoryEdge[RepositoryEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Repository
   pageInfo: PageInfo
   totalCount: int
   totalDiskUsage: int

class IssueOrPullRequest(GQLObject): 
   pass

class QGNOM_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class VERBQ_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class IssueTemplate(GQLObject):
   about: str
   assignees: QGNOM_UserConnection_Field
   body: str
   filename: str
   labels: VERBQ_LabelConnection_Field
   name: str
   title: str

class LanguageEdge(GQLObject):
   cursor: str
   node: Language
   size: int

class list_LanguageEdge(list, LanguageEdge): pass

class list_Language(list, Language): pass

class LanguageConnection(GQLObject):
   edges: list_LanguageEdge[LanguageEdge]
   nodes: list_Language[Language]
   pageInfo: PageInfo
   totalCount: int
   totalSize: int

class ReleaseAsset(GQLObject):
   contentType: str
   createdAt: DateTime
   downloadCount: int
   downloadUrl: URI
   id: ID
   name: str
   release: NewType('Release', GQLObject) ## Circular Reference for Release
   size: int
   updatedAt: DateTime
   uploadedBy: NewType('User', GQLObject) ## Circular Reference for User
   url: URI

class ReleaseAssetEdge(GQLObject):
   cursor: str
   node: ReleaseAsset

class list_ReleaseAssetEdge(list, ReleaseAssetEdge): pass

class list_ReleaseAsset(list, ReleaseAsset): pass

class ReleaseAssetConnection(GQLObject):
   edges: list_ReleaseAssetEdge[ReleaseAssetEdge]
   nodes: list_ReleaseAsset[ReleaseAsset]
   pageInfo: PageInfo
   totalCount: int

class WTYNF_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class HBZIJ_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class MDJRQ_ReleaseAssetConnection_Field(ReleaseAssetConnection):
   class ReleaseAssetConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      name: str

   _args: ReleaseAssetConnectionArgs



class Release(GQLObject):
   author: NewType('User', GQLObject) ## Circular Reference for User
   createdAt: DateTime
   databaseId: int
   description: str
   descriptionHTML: HTML
   id: ID
   isDraft: bool
   isLatest: bool
   isPrerelease: bool
   mentions: WTYNF_UserConnection_Field
   name: str
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: HBZIJ_ReactionConnection_Field
   releaseAssets: MDJRQ_ReleaseAssetConnection_Field
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   resourcePath: URI
   shortDescriptionHTML: HDADO_HTML_Field
   tag: NewType('Ref', GQLObject) ## Circular Reference for Ref
   tagCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   tagName: str
   updatedAt: DateTime
   url: URI
   viewerCanReact: bool

class list_LicenseRule(list, LicenseRule): pass

class License(GQLObject):
   body: str
   conditions: list_LicenseRule[LicenseRule]
   description: str
   featured: bool
   hidden: bool
   id: ID
   implementation: str
   key: str
   limitations: list_LicenseRule[LicenseRule]
   name: str
   nickname: str
   permissions: list_LicenseRule[LicenseRule]
   pseudoLicense: bool
   spdxId: str
   url: URI

class MergeQueueEntry(GQLObject):
   baseCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   enqueuedAt: DateTime
   enqueuer: Actor
   estimatedTimeToMerge: int
   headCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   id: ID
   jump: bool
   mergeQueue: NewType('MergeQueue', GQLObject) ## Circular Reference for MergeQueue
   position: int
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   solo: bool
   state: MergeQueueEntryState

class MergeQueueEntryEdge(GQLObject):
   cursor: str
   node: MergeQueueEntry

class list_MergeQueueEntryEdge(list, MergeQueueEntryEdge): pass

class list_MergeQueueEntry(list, MergeQueueEntry): pass

class MergeQueueEntryConnection(GQLObject):
   edges: list_MergeQueueEntryEdge[MergeQueueEntryEdge]
   nodes: list_MergeQueueEntry[MergeQueueEntry]
   pageInfo: PageInfo
   totalCount: int

class OEELC_MergeQueueEntryConnection_Field(MergeQueueEntryConnection):
   class MergeQueueEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: MergeQueueEntryConnectionArgs



class MergeQueue(GQLObject):
   configuration: MergeQueueConfiguration
   entries: OEELC_MergeQueueEntryConnection_Field
   id: ID
   nextEntryEstimatedTimeToMerge: int
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   resourcePath: URI
   url: URI

class JRFYZ_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueOrder
      labels: list[NonNull_str]
      states: list[NonNull_IssueState]
      filterBy: IssueFilters
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class ZGEDV_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      states: list[NonNull_PullRequestState]
      labels: list[NonNull_str]
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class Milestone(GQLObject):
   closed: bool
   closedAt: DateTime
   createdAt: DateTime
   creator: Actor
   description: str
   dueOn: DateTime
   id: ID
   issues: JRFYZ_IssueConnection_Field
   number: int
   progressPercentage: float
   pullRequests: ZGEDV_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   resourcePath: URI
   state: MilestoneState
   title: str
   updatedAt: DateTime
   url: URI
   viewerCanClose: bool
   viewerCanReopen: bool

class MilestoneEdge(GQLObject):
   cursor: str
   node: Milestone

class list_MilestoneEdge(list, MilestoneEdge): pass

class list_Milestone(list, Milestone): pass

class MilestoneConnection(GQLObject):
   edges: list_MilestoneEdge[MilestoneEdge]
   nodes: list_Milestone[Milestone]
   pageInfo: PageInfo
   totalCount: int

class GitObject(GQLObject):
   abbreviatedOid: str
   commitResourcePath: URI
   commitUrl: URI
   id: ID
   oid: GitObjectID
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository

class KVVJA_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: list[RepositoryAffiliation]
      ownerAffiliations: list[RepositoryAffiliation]
      isLocked: bool
      after: str
      before: str
      first: int
      last: int
      isFork: bool

   _args: RepositoryConnectionArgs



class CTQNV_Repository_Field(Generic[Repository]):
   class RepositoryArgs(GQLArgsSet, GQLObject):
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs



class RepositoryOwner(GQLObject):
   avatarUrl: TWNLY_URI_Field
   id: ID
   login: str
   repositories: KVVJA_RepositoryConnection_Field
   repository: CTQNV_Repository_Field ## Circular Reference for Repository
   resourcePath: URI
   url: URI

class PackageFile(GQLObject):
   id: ID
   md5: str
   name: str
   packageVersion: NewType('PackageVersion', GQLObject) ## Circular Reference for PackageVersion
   sha1: str
   sha256: str
   size: int
   updatedAt: DateTime
   url: URI

class PackageFileEdge(GQLObject):
   cursor: str
   node: PackageFile

class list_PackageFileEdge(list, PackageFileEdge): pass

class list_PackageFile(list, PackageFile): pass

class PackageFileConnection(GQLObject):
   edges: list_PackageFileEdge[PackageFileEdge]
   nodes: list_PackageFile[PackageFile]
   pageInfo: PageInfo
   totalCount: int

class HTMFX_PackageFileConnection_Field(PackageFileConnection):
   class PackageFileConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: PackageFileOrder
      after: str
      before: str
      first: int
      last: int

   _args: PackageFileConnectionArgs



class PackageVersion(GQLObject):
   files: HTMFX_PackageFileConnection_Field
   id: ID
   package: NewType('Package', GQLObject) ## Circular Reference for Package
   platform: str
   preRelease: bool
   readme: str
   release: Release
   statistics: PackageVersionStatistics
   summary: str
   version: str

class PackageVersionEdge(GQLObject):
   cursor: str
   node: PackageVersion

class list_PackageVersionEdge(list, PackageVersionEdge): pass

class list_PackageVersion(list, PackageVersion): pass

class PackageVersionConnection(GQLObject):
   edges: list_PackageVersionEdge[PackageVersionEdge]
   nodes: list_PackageVersion[PackageVersion]
   pageInfo: PageInfo
   totalCount: int

class YKVDH_PackageVersion_Field(PackageVersion):
   class PackageVersionArgs(GQLArgsSet, GQLObject):
      version: NonNull_str

   _args: PackageVersionArgs



class PZGPW_PackageVersionConnection_Field(PackageVersionConnection):
   class PackageVersionConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: PackageVersionOrder
      after: str
      before: str
      first: int
      last: int

   _args: PackageVersionConnectionArgs



class Package(GQLObject):
   id: ID
   latestVersion: PackageVersion
   name: str
   packageType: PackageType
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   statistics: PackageStatistics
   version: YKVDH_PackageVersion_Field
   versions: PZGPW_PackageVersionConnection_Field

class PackageEdge(GQLObject):
   cursor: str
   node: Package

class list_PackageEdge(list, PackageEdge): pass

class list_Package(list, Package): pass

class PackageConnection(GQLObject):
   edges: list_PackageEdge[PackageEdge]
   nodes: list_Package[Package]
   pageInfo: PageInfo
   totalCount: int

class PinnedDiscussion(GQLObject):
   createdAt: DateTime
   databaseId: int
   discussion: Discussion
   gradientStopColors: list[str]
   id: ID
   pattern: PinnedDiscussionPattern
   pinnedBy: Actor
   preconfiguredGradient: PinnedDiscussionGradient
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   updatedAt: DateTime

class PinnedDiscussionEdge(GQLObject):
   cursor: str
   node: PinnedDiscussion

class list_PinnedDiscussionEdge(list, PinnedDiscussionEdge): pass

class list_PinnedDiscussion(list, PinnedDiscussion): pass

class PinnedDiscussionConnection(GQLObject):
   edges: list_PinnedDiscussionEdge[PinnedDiscussionEdge]
   nodes: list_PinnedDiscussion[PinnedDiscussion]
   pageInfo: PageInfo
   totalCount: int

class PinnedIssue(GQLObject):
   databaseId: int
   fullDatabaseId: BigInt
   id: ID
   issue: NewType('Issue', GQLObject) ## Circular Reference for Issue
   pinnedBy: Actor
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository

class PinnedIssueEdge(GQLObject):
   cursor: str
   node: PinnedIssue

class list_PinnedIssueEdge(list, PinnedIssueEdge): pass

class list_PinnedIssue(list, PinnedIssue): pass

class PinnedIssueConnection(GQLObject):
   edges: list_PinnedIssueEdge[PinnedIssueEdge]
   nodes: list_PinnedIssue[PinnedIssue]
   pageInfo: PageInfo
   totalCount: int

class ProjectCardItem(GQLObject): 
   pass

class ProjectCard(GQLObject):
   column: NewType('ProjectColumn', GQLObject) ## Circular Reference for ProjectColumn
   content: ProjectCardItem
   createdAt: DateTime
   creator: Actor
   databaseId: int
   id: ID
   isArchived: bool
   note: str
   project: NewType('Project', GQLObject) ## Circular Reference for Project
   resourcePath: URI
   state: ProjectCardState
   updatedAt: DateTime
   url: URI

class ProjectCardEdge(GQLObject):
   cursor: str
   node: ProjectCard

class list_ProjectCardEdge(list, ProjectCardEdge): pass

class list_ProjectCard(list, ProjectCard): pass

class ProjectCardConnection(GQLObject):
   edges: list_ProjectCardEdge[ProjectCardEdge]
   nodes: list_ProjectCard[ProjectCard]
   pageInfo: PageInfo
   totalCount: int

class QCTXF_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: ProjectCardConnectionArgs



class ProjectColumn(GQLObject):
   cards: QCTXF_ProjectCardConnection_Field
   createdAt: DateTime
   databaseId: int
   id: ID
   name: str
   project: NewType('Project', GQLObject) ## Circular Reference for Project
   purpose: ProjectColumnPurpose
   resourcePath: URI
   updatedAt: DateTime
   url: URI

class ProjectColumnEdge(GQLObject):
   cursor: str
   node: ProjectColumn

class list_ProjectColumnEdge(list, ProjectColumnEdge): pass

class list_ProjectColumn(list, ProjectColumn): pass

class ProjectColumnConnection(GQLObject):
   edges: list_ProjectColumnEdge[ProjectColumnEdge]
   nodes: list_ProjectColumn[ProjectColumn]
   pageInfo: PageInfo
   totalCount: int

class ProjectEdge(GQLObject):
   cursor: str
   node: NewType('Project', GQLObject) ## Circular Reference for Project

class list_ProjectEdge(list, ProjectEdge): pass

class ProjectConnection(GQLObject):
   edges: list_ProjectEdge[ProjectEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Project
   pageInfo: PageInfo
   totalCount: int

class IBIJP_Project_Field(Generic[Project]):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class NonNull_ProjectState(GQLObject): pass

class QZDLI_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: ProjectOrder
      search: str
      states: list[NonNull_ProjectState]
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class ProjectOwner(GQLObject):
   id: ID
   project: IBIJP_Project_Field ## Circular Reference for Project
   projects: QZDLI_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   viewerCanCreateProjects: bool

class YCPCL_ProjectColumnConnection_Field(ProjectColumnConnection):
   class ProjectColumnConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectColumnConnectionArgs



class BWOXS_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: ProjectCardConnectionArgs



class Project(GQLObject):
   body: str
   bodyHTML: HTML
   closed: bool
   closedAt: DateTime
   columns: YCPCL_ProjectColumnConnection_Field
   createdAt: DateTime
   creator: Actor
   databaseId: int
   id: ID
   name: str
   number: int
   owner: ProjectOwner
   pendingCards: BWOXS_ProjectCardConnection_Field
   progress: ProjectProgress
   resourcePath: URI
   state: ProjectState
   updatedAt: DateTime
   url: URI
   viewerCanClose: bool
   viewerCanReopen: bool
   viewerCanUpdate: bool

class PullRequestTemplate(GQLObject):
   body: str
   filename: str
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository

class RefEdge(GQLObject):
   cursor: str
   node: NewType('Ref', GQLObject) ## Circular Reference for Ref

class list_RefEdge(list, RefEdge): pass

class RefConnection(GQLObject):
   edges: list_RefEdge[RefEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Ref
   pageInfo: PageInfo
   totalCount: int

class ReleaseEdge(GQLObject):
   cursor: str
   node: Release

class list_ReleaseEdge(list, ReleaseEdge): pass

class list_Release(list, Release): pass

class ReleaseConnection(GQLObject):
   edges: list_ReleaseEdge[ReleaseEdge]
   nodes: list_Release[Release]
   pageInfo: PageInfo
   totalCount: int

class StargazerEdge(GQLObject):
   cursor: str
   node: NewType('User', GQLObject) ## Circular Reference for User
   starredAt: DateTime

class list_StargazerEdge(list, StargazerEdge): pass

class StargazerConnection(GQLObject):
   edges: list_StargazerEdge[StargazerEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for User
   pageInfo: PageInfo
   totalCount: int

class TJJBG_Topic_Field(Generic[Topic]):
   class TopicArgs(GQLArgsSet, GQLObject):
      first: int

   _args: TopicArgs



class FDOQN_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: list[RepositoryAffiliation]
      ownerAffiliations: list[RepositoryAffiliation]
      isLocked: bool
      after: str
      before: str
      first: int
      last: int
      sponsorableOnly: bool

   _args: RepositoryConnectionArgs



class LEDMO_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class Topic(GQLObject):
   id: ID
   name: str
   relatedTopics: TJJBG_Topic_Field ## Circular Reference for Topic
   repositories: FDOQN_RepositoryConnection_Field
   stargazerCount: int
   stargazers: LEDMO_StargazerConnection_Field
   viewerHasStarred: bool

class RepositoryTopic(GQLObject):
   id: ID
   resourcePath: URI
   topic: Topic
   url: URI

class RepositoryTopicEdge(GQLObject):
   cursor: str
   node: RepositoryTopic

class list_RepositoryTopicEdge(list, RepositoryTopicEdge): pass

class list_RepositoryTopic(list, RepositoryTopic): pass

class RepositoryTopicConnection(GQLObject):
   edges: list_RepositoryTopicEdge[RepositoryTopicEdge]
   nodes: list_RepositoryTopic[RepositoryTopic]
   pageInfo: PageInfo
   totalCount: int

class BypassActor(GQLObject): 
   pass

class RepositoryRulesetBypassActor(GQLObject):
   actor: BypassActor
   bypassMode: RepositoryRulesetBypassActorBypassMode
   id: ID
   organizationAdmin: bool
   repositoryRoleDatabaseId: int
   repositoryRoleName: str
   repositoryRuleset: NewType('RepositoryRuleset', GQLObject) ## Circular Reference for RepositoryRuleset

class RepositoryRulesetBypassActorEdge(GQLObject):
   cursor: str
   node: RepositoryRulesetBypassActor

class list_RepositoryRulesetBypassActorEdge(list, RepositoryRulesetBypassActorEdge): pass

class list_RepositoryRulesetBypassActor(list, RepositoryRulesetBypassActor): pass

class RepositoryRulesetBypassActorConnection(GQLObject):
   edges: list_RepositoryRulesetBypassActorEdge[RepositoryRulesetBypassActorEdge]
   nodes: list_RepositoryRulesetBypassActor[RepositoryRulesetBypassActor]
   pageInfo: PageInfo
   totalCount: int

class RepositoryRuleConditions(GQLObject):
   refName: RefNameConditionTarget
   repositoryId: RepositoryIdConditionTarget
   repositoryName: RepositoryNameConditionTarget

class list_StatusCheckConfiguration(list, StatusCheckConfiguration): pass

class RequiredStatusChecksParameters(GQLObject):
   requiredStatusChecks: list_StatusCheckConfiguration[StatusCheckConfiguration]
   strictRequiredStatusChecksPolicy: bool

class RuleParameters(GQLObject): 
   pass

class RepositoryRule(GQLObject):
   id: ID
   parameters: RuleParameters
   type: RepositoryRuleType

class RepositoryRuleEdge(GQLObject):
   cursor: str
   node: RepositoryRule

class list_RepositoryRuleEdge(list, RepositoryRuleEdge): pass

class list_RepositoryRule(list, RepositoryRule): pass

class RepositoryRuleConnection(GQLObject):
   edges: list_RepositoryRuleEdge[RepositoryRuleEdge]
   nodes: list_RepositoryRule[RepositoryRule]
   pageInfo: PageInfo
   totalCount: int

class RuleSource(GQLObject): 
   pass

class TBHLK_RepositoryRulesetBypassActorConnection_Field(RepositoryRulesetBypassActorConnection):
   class RepositoryRulesetBypassActorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryRulesetBypassActorConnectionArgs



class BMHMH_RepositoryRuleConnection_Field(RepositoryRuleConnection):
   class RepositoryRuleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      type: RepositoryRuleType

   _args: RepositoryRuleConnectionArgs



class RepositoryRuleset(GQLObject):
   bypassActors: TBHLK_RepositoryRulesetBypassActorConnection_Field
   conditions: RepositoryRuleConditions
   createdAt: DateTime
   databaseId: int
   enforcement: RuleEnforcement
   id: ID
   name: str
   rules: BMHMH_RepositoryRuleConnection_Field
   source: RuleSource
   target: RepositoryRulesetTarget
   updatedAt: DateTime

class RepositoryRulesetEdge(GQLObject):
   cursor: str
   node: RepositoryRuleset

class list_RepositoryRulesetEdge(list, RepositoryRulesetEdge): pass

class list_RepositoryRuleset(list, RepositoryRuleset): pass

class RepositoryRulesetConnection(GQLObject):
   edges: list_RepositoryRulesetEdge[RepositoryRulesetEdge]
   nodes: list_RepositoryRuleset[RepositoryRuleset]
   pageInfo: PageInfo
   totalCount: int

class SubmoduleEdge(GQLObject):
   cursor: str
   node: Submodule

class list_SubmoduleEdge(list, SubmoduleEdge): pass

class list_Submodule(list, Submodule): pass

class SubmoduleConnection(GQLObject):
   edges: list_SubmoduleEdge[SubmoduleEdge]
   nodes: list_Submodule[Submodule]
   pageInfo: PageInfo
   totalCount: int

class DependabotUpdate(GQLObject):
   error: DependabotUpdateError
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository

class CWEEdge(GQLObject):
   cursor: str
   node: CWE

class list_CWEEdge(list, CWEEdge): pass

class list_CWE(list, CWE): pass

class CWEConnection(GQLObject):
   edges: list_CWEEdge[CWEEdge]
   nodes: list_CWE[CWE]
   pageInfo: PageInfo
   totalCount: int

class SecurityVulnerability(GQLObject):
   advisory: NewType('SecurityAdvisory', GQLObject) ## Circular Reference for SecurityAdvisory
   firstPatchedVersion: SecurityAdvisoryPackageVersion
   package: SecurityAdvisoryPackage
   severity: SecurityAdvisorySeverity
   updatedAt: DateTime
   vulnerableVersionRange: str

class SecurityVulnerabilityEdge(GQLObject):
   cursor: str
   node: SecurityVulnerability

class list_SecurityVulnerabilityEdge(list, SecurityVulnerabilityEdge): pass

class list_SecurityVulnerability(list, SecurityVulnerability): pass

class SecurityVulnerabilityConnection(GQLObject):
   edges: list_SecurityVulnerabilityEdge[SecurityVulnerabilityEdge]
   nodes: list_SecurityVulnerability[SecurityVulnerability]
   pageInfo: PageInfo
   totalCount: int

class KDIPR_CWEConnection_Field(CWEConnection):
   class CWEConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CWEConnectionArgs



class list_SecurityAdvisoryIdentifier(list, SecurityAdvisoryIdentifier): pass

class list_SecurityAdvisoryReference(list, SecurityAdvisoryReference): pass

class NonNull_SecurityAdvisorySeverity(GQLObject): pass

class NonNull_SecurityAdvisoryClassification(GQLObject): pass

class ABPNZ_SecurityVulnerabilityConnection_Field(SecurityVulnerabilityConnection):
   class SecurityVulnerabilityConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: SecurityVulnerabilityOrder
      ecosystem: SecurityAdvisoryEcosystem
      package: str
      severities: list[NonNull_SecurityAdvisorySeverity]
      classifications: list[NonNull_SecurityAdvisoryClassification]
      after: str
      before: str
      first: int
      last: int

   _args: SecurityVulnerabilityConnectionArgs



class SecurityAdvisory(GQLObject):
   classification: SecurityAdvisoryClassification
   cvss: CVSS
   cwes: KDIPR_CWEConnection_Field
   databaseId: int
   description: str
   ghsaId: str
   id: ID
   identifiers: list_SecurityAdvisoryIdentifier[SecurityAdvisoryIdentifier]
   notificationsPermalink: URI
   origin: str
   permalink: URI
   publishedAt: DateTime
   references: list_SecurityAdvisoryReference[SecurityAdvisoryReference]
   severity: SecurityAdvisorySeverity
   summary: str
   updatedAt: DateTime
   vulnerabilities: ABPNZ_SecurityVulnerabilityConnection_Field
   withdrawnAt: DateTime

class RepositoryVulnerabilityAlert(GQLObject):
   autoDismissedAt: DateTime
   createdAt: DateTime
   dependabotUpdate: DependabotUpdate
   dependencyScope: RepositoryVulnerabilityAlertDependencyScope
   dismissComment: str
   dismissReason: str
   dismissedAt: DateTime
   dismisser: NewType('User', GQLObject) ## Circular Reference for User
   fixedAt: DateTime
   id: ID
   number: int
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   securityAdvisory: SecurityAdvisory
   securityVulnerability: SecurityVulnerability
   state: RepositoryVulnerabilityAlertState
   vulnerableManifestFilename: str
   vulnerableManifestPath: str
   vulnerableRequirements: str

class RepositoryVulnerabilityAlertEdge(GQLObject):
   cursor: str
   node: RepositoryVulnerabilityAlert

class list_RepositoryVulnerabilityAlertEdge(list, RepositoryVulnerabilityAlertEdge): pass

class list_RepositoryVulnerabilityAlert(list, RepositoryVulnerabilityAlert): pass

class RepositoryVulnerabilityAlertConnection(GQLObject):
   edges: list_RepositoryVulnerabilityAlertEdge[RepositoryVulnerabilityAlertEdge]
   nodes: list_RepositoryVulnerabilityAlert[RepositoryVulnerabilityAlert]
   pageInfo: PageInfo
   totalCount: int

class SMRIM_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class NRMSB_BranchProtectionRuleConnection_Field(BranchProtectionRuleConnection):
   class BranchProtectionRuleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BranchProtectionRuleConnectionArgs



class RYGFK_RepositoryCodeowners_Field(RepositoryCodeowners):
   class RepositoryCodeownersArgs(GQLArgsSet, GQLObject):
      refName: str

   _args: RepositoryCodeownersArgs



class DOYFO_RepositoryCollaboratorConnection_Field(RepositoryCollaboratorConnection):
   class RepositoryCollaboratorConnectionArgs(GQLArgsSet, GQLObject):
      affiliation: CollaboratorAffiliation
      login: str
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryCollaboratorConnectionArgs



class BORMY_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class list_RepositoryContactLink(list, RepositoryContactLink): pass

class HVTBZ_DeployKeyConnection_Field(DeployKeyConnection):
   class DeployKeyConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeployKeyConnectionArgs



class JMIAE_DeploymentConnection_Field(DeploymentConnection):
   class DeploymentConnectionArgs(GQLArgsSet, GQLObject):
      environments: list[NonNull_str]
      orderBy: DeploymentOrder
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentConnectionArgs



class HIQRU_Discussion_Field(Discussion):
   class DiscussionArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: DiscussionArgs



class PIJSL_DiscussionCategoryConnection_Field(DiscussionCategoryConnection):
   class DiscussionCategoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      filterByAssignable: bool

   _args: DiscussionCategoryConnectionArgs



class JZMBV_DiscussionCategory_Field(DiscussionCategory):
   class DiscussionCategoryArgs(GQLArgsSet, GQLObject):
      slug: NonNull_str

   _args: DiscussionCategoryArgs



class NonNull_DiscussionState(GQLObject): pass

class ZOJWH_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      categoryId: ID
      states: list[NonNull_DiscussionState]
      orderBy: DiscussionOrder

   _args: DiscussionConnectionArgs



class DEESG_Environment_Field(Environment):
   class EnvironmentArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: EnvironmentArgs



class YAOHS_EnvironmentConnection_Field(EnvironmentConnection):
   class EnvironmentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: EnvironmentConnectionArgs



class PORGP_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: list[RepositoryAffiliation]
      ownerAffiliations: list[RepositoryAffiliation]
      isLocked: bool
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryConnectionArgs



class list_FundingLink(list, FundingLink): pass

class DJLDV_Issue_Field(Generic[Issue]):
   class IssueArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: IssueArgs



class DVPEI_IssueOrPullRequest_Field(IssueOrPullRequest):
   class IssueOrPullRequestArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: IssueOrPullRequestArgs



class list_IssueTemplate(list, IssueTemplate): pass

class WIGVN_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueOrder
      labels: list[NonNull_str]
      states: list[NonNull_IssueState]
      filterBy: IssueFilters
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class CQBJS_Label_Field(Label):
   class LabelArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: LabelArgs



class EPFNL_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int
      query: str

   _args: LabelConnectionArgs



class NQPZM_LanguageConnection_Field(LanguageConnection):
   class LanguageConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: LanguageOrder

   _args: LanguageConnectionArgs



class IKIWG_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class WKPCQ_MergeQueue_Field(MergeQueue):
   class MergeQueueArgs(GQLArgsSet, GQLObject):
      branch: str

   _args: MergeQueueArgs



class YDWSU_Milestone_Field(Milestone):
   class MilestoneArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: MilestoneArgs



class NonNull_MilestoneState(GQLObject): pass

class VQSDG_MilestoneConnection_Field(MilestoneConnection):
   class MilestoneConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      states: list[NonNull_MilestoneState]
      orderBy: MilestoneOrder
      query: str

   _args: MilestoneConnectionArgs



class XEJAM_GitObject_Field(GitObject):
   class GitObjectArgs(GQLArgsSet, GQLObject):
      oid: GitObjectID
      expression: str

   _args: GitObjectArgs



class DJOBN_PackageConnection_Field(PackageConnection):
   class PackageConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      names: list[str]
      repositoryId: ID
      packageType: PackageType
      orderBy: PackageOrder

   _args: PackageConnectionArgs



class AFPBV_PinnedDiscussionConnection_Field(PinnedDiscussionConnection):
   class PinnedDiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PinnedDiscussionConnectionArgs



class OWFDP_PinnedIssueConnection_Field(PinnedIssueConnection):
   class PinnedIssueConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PinnedIssueConnectionArgs



class IAQOI_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class RPGUB_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class LLASC_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: ProjectOrder
      search: str
      states: list[NonNull_ProjectState]
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class NCMTX_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: ProjectV2Order

   _args: ProjectV2ConnectionArgs



class VRUNR_PullRequest_Field(Generic[PullRequest]):
   class PullRequestArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: PullRequestArgs



class list_PullRequestTemplate(list, PullRequestTemplate): pass

class TISPD_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      states: list[NonNull_PullRequestState]
      labels: list[NonNull_str]
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class WNQGM_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class GLZFZ_Ref_Field(Generic[Ref]):
   class RefArgs(GQLArgsSet, GQLObject):
      qualifiedName: NonNull_str

   _args: RefArgs



class ZHCOC_RefConnection_Field(RefConnection):
   class RefConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int
      refPrefix: NonNull_str
      direction: OrderDirection
      orderBy: RefOrder

   _args: RefConnectionArgs



class LFGJF_Release_Field(Release):
   class ReleaseArgs(GQLArgsSet, GQLObject):
      tagName: NonNull_str

   _args: ReleaseArgs



class EMWSE_ReleaseConnection_Field(ReleaseConnection):
   class ReleaseConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ReleaseOrder

   _args: ReleaseConnectionArgs



class WIWJZ_RepositoryTopicConnection_Field(RepositoryTopicConnection):
   class RepositoryTopicConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryTopicConnectionArgs



class IMMLA_RepositoryRuleset_Field(RepositoryRuleset):
   class RepositoryRulesetArgs(GQLArgsSet, GQLObject):
      includeParents: bool
      databaseId: NonNull_int

   _args: RepositoryRulesetArgs



class QQTDL_RepositoryRulesetConnection_Field(RepositoryRulesetConnection):
   class RepositoryRulesetConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includeParents: bool

   _args: RepositoryRulesetConnectionArgs



class FUVSG_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class SUJEY_SubmoduleConnection_Field(SubmoduleConnection):
   class SubmoduleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: SubmoduleConnectionArgs



class XOQTS_RepositoryVulnerabilityAlert_Field(RepositoryVulnerabilityAlert):
   class RepositoryVulnerabilityAlertArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: RepositoryVulnerabilityAlertArgs



class NonNull_RepositoryVulnerabilityAlertState(GQLObject): pass

class NonNull_RepositoryVulnerabilityAlertDependencyScope(GQLObject): pass

class LMWED_RepositoryVulnerabilityAlertConnection_Field(RepositoryVulnerabilityAlertConnection):
   class RepositoryVulnerabilityAlertConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      states: list[NonNull_RepositoryVulnerabilityAlertState]
      dependencyScopes: list[NonNull_RepositoryVulnerabilityAlertDependencyScope]

   _args: RepositoryVulnerabilityAlertConnectionArgs



class JGAUG_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class Repository(GQLObject):
   allowUpdateBranch: bool
   archivedAt: DateTime
   assignableUsers: SMRIM_UserConnection_Field
   autoMergeAllowed: bool
   branchProtectionRules: NRMSB_BranchProtectionRuleConnection_Field
   codeOfConduct: CodeOfConduct
   codeowners: RYGFK_RepositoryCodeowners_Field
   collaborators: DOYFO_RepositoryCollaboratorConnection_Field
   commitComments: BORMY_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
   contactLinks: list_RepositoryContactLink[RepositoryContactLink]
   createdAt: DateTime
   databaseId: int
   defaultBranchRef: NewType('Ref', GQLObject) ## Circular Reference for Ref
   deleteBranchOnMerge: bool
   deployKeys: HVTBZ_DeployKeyConnection_Field
   deployments: JMIAE_DeploymentConnection_Field
   description: str
   descriptionHTML: HTML
   discussion: HIQRU_Discussion_Field
   discussionCategories: PIJSL_DiscussionCategoryConnection_Field
   discussionCategory: JZMBV_DiscussionCategory_Field
   discussions: ZOJWH_DiscussionConnection_Field
   diskUsage: int
   environment: DEESG_Environment_Field
   environments: YAOHS_EnvironmentConnection_Field
   forkCount: int
   forkingAllowed: bool
   forks: PORGP_RepositoryConnection_Field
   fundingLinks: list_FundingLink[FundingLink]
   hasDiscussionsEnabled: bool
   hasIssuesEnabled: bool
   hasProjectsEnabled: bool
   hasVulnerabilityAlertsEnabled: bool
   hasWikiEnabled: bool
   homepageUrl: URI
   id: ID
   interactionAbility: RepositoryInteractionAbility
   isArchived: bool
   isBlankIssuesEnabled: bool
   isDisabled: bool
   isEmpty: bool
   isFork: bool
   isInOrganization: bool
   isLocked: bool
   isMirror: bool
   isPrivate: bool
   isSecurityPolicyEnabled: bool
   isTemplate: bool
   isUserConfigurationRepository: bool
   issue: DJLDV_Issue_Field ## Circular Reference for Issue
   issueOrPullRequest: DVPEI_IssueOrPullRequest_Field
   issueTemplates: list_IssueTemplate[IssueTemplate]
   issues: WIGVN_IssueConnection_Field
   label: CQBJS_Label_Field
   labels: EPFNL_LabelConnection_Field
   languages: NQPZM_LanguageConnection_Field
   latestRelease: Release
   licenseInfo: License
   lockReason: RepositoryLockReason
   mentionableUsers: IKIWG_UserConnection_Field
   mergeCommitAllowed: bool
   mergeCommitMessage: MergeCommitMessage
   mergeCommitTitle: MergeCommitTitle
   mergeQueue: WKPCQ_MergeQueue_Field
   milestone: YDWSU_Milestone_Field
   milestones: VQSDG_MilestoneConnection_Field
   mirrorUrl: URI
   name: str
   nameWithOwner: str
   object: XEJAM_GitObject_Field
   openGraphImageUrl: URI
   owner: RepositoryOwner
   packages: DJOBN_PackageConnection_Field
   parent: NewType('Repository', GQLObject) ## Circular Reference for Repository
   pinnedDiscussions: AFPBV_PinnedDiscussionConnection_Field
   pinnedIssues: OWFDP_PinnedIssueConnection_Field
   primaryLanguage: Language
   project: IAQOI_Project_Field
   projectV2: RPGUB_ProjectV2_Field ## Circular Reference for ProjectV2
   projects: LLASC_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   projectsV2: NCMTX_ProjectV2Connection_Field
   pullRequest: VRUNR_PullRequest_Field ## Circular Reference for PullRequest
   pullRequestTemplates: list_PullRequestTemplate[PullRequestTemplate]
   pullRequests: TISPD_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   pushedAt: DateTime
   rebaseMergeAllowed: bool
   recentProjects: WNQGM_ProjectV2Connection_Field
   ref: GLZFZ_Ref_Field ## Circular Reference for Ref
   refs: ZHCOC_RefConnection_Field
   release: LFGJF_Release_Field
   releases: EMWSE_ReleaseConnection_Field
   repositoryTopics: WIWJZ_RepositoryTopicConnection_Field
   resourcePath: URI
   ruleset: IMMLA_RepositoryRuleset_Field
   rulesets: QQTDL_RepositoryRulesetConnection_Field
   securityPolicyUrl: URI
   shortDescriptionHTML: HLTJY_HTML_Field
   squashMergeAllowed: bool
   squashMergeCommitMessage: SquashMergeCommitMessage
   squashMergeCommitTitle: SquashMergeCommitTitle
   sshUrl: GitSSHRemote
   stargazerCount: int
   stargazers: FUVSG_StargazerConnection_Field
   submodules: SUJEY_SubmoduleConnection_Field
   tempCloneToken: str
   templateRepository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   updatedAt: DateTime
   url: URI
   usesCustomOpenGraphImage: bool
   viewerCanAdminister: bool
   viewerCanCreateProjects: bool
   viewerCanSubscribe: bool
   viewerCanUpdateTopics: bool
   viewerDefaultCommitEmail: str
   viewerDefaultMergeMethod: PullRequestMergeMethod
   viewerHasStarred: bool
   viewerPermission: RepositoryPermission
   viewerPossibleCommitEmails: list[str]
   viewerSubscription: SubscriptionState
   visibility: RepositoryVisibility
   vulnerabilityAlert: XOQTS_RepositoryVulnerabilityAlert_Field
   vulnerabilityAlerts: LMWED_RepositoryVulnerabilityAlertConnection_Field
   watchers: JGAUG_UserConnection_Field
   webCommitSignoffRequired: bool

class NVBBF_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class OXMJE_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class IssueComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyText: str
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   fullDatabaseId: BigInt
   id: ID
   includesCreatedEdit: bool
   isMinimized: bool
   issue: NewType('Issue', GQLObject) ## Circular Reference for Issue
   lastEditedAt: DateTime
   minimizedReason: str
   publishedAt: DateTime
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: NVBBF_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   updatedAt: DateTime
   url: URI
   userContentEdits: OXMJE_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanMinimize: bool
   viewerCanReact: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]
   viewerDidAuthor: bool

class IssueCommentEdge(GQLObject):
   cursor: str
   node: IssueComment

class list_IssueCommentEdge(list, IssueCommentEdge): pass

class list_IssueComment(list, IssueComment): pass

class IssueCommentConnection(GQLObject):
   edges: list_IssueCommentEdge[IssueCommentEdge]
   nodes: list_IssueComment[IssueComment]
   pageInfo: PageInfo
   totalCount: int

class list_HovercardContext(list, HovercardContext): pass

class Hovercard(GQLObject):
   contexts: list_HovercardContext[HovercardContext]

class LinkedBranch(GQLObject):
   id: ID
   ref: NewType('Ref', GQLObject) ## Circular Reference for Ref

class LinkedBranchEdge(GQLObject):
   cursor: str
   node: LinkedBranch

class list_LinkedBranchEdge(list, LinkedBranchEdge): pass

class list_LinkedBranch(list, LinkedBranch): pass

class LinkedBranchConnection(GQLObject):
   edges: list_LinkedBranchEdge[LinkedBranchEdge]
   nodes: list_LinkedBranch[LinkedBranch]
   pageInfo: PageInfo
   totalCount: int

class VBOMQ_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class Assignable(GQLObject):
   assignees: VBOMQ_UserConnection_Field

class Assignee(GQLObject): 
   pass

class AssignedEvent(GQLObject):
   actor: Actor
   assignable: Assignable
   assignee: Assignee
   createdAt: DateTime
   id: ID

class Closer(GQLObject): 
   pass

class ClosedEvent(GQLObject):
   actor: Actor
   closable: Closable
   closer: Closer
   createdAt: DateTime
   id: ID
   resourcePath: URI
   stateReason: IssueStateReason
   url: URI

class ReferencedSubject(GQLObject): 
   pass

class CrossReferencedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   isCrossRepository: bool
   referencedAt: DateTime
   resourcePath: URI
   source: ReferencedSubject
   target: ReferencedSubject
   url: URI
   willCloseTarget: bool

class MilestoneItem(GQLObject): 
   pass

class DemilestonedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   milestoneTitle: str
   subject: MilestoneItem

class KECJZ_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class Labelable(GQLObject):
   labels: KECJZ_LabelConnection_Field

class LabeledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   label: Label
   labelable: Labelable

class LockedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   lockReason: LockReason
   lockable: Lockable

class MilestonedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   milestoneTitle: str
   subject: MilestoneItem

class ReferencedEvent(GQLObject):
   actor: Actor
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   commitRepository: Repository
   createdAt: DateTime
   id: ID
   isCrossRepository: bool
   isDirectReference: bool
   subject: ReferencedSubject

class RenamedTitleSubject(GQLObject): 
   pass

class RenamedTitleEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   currentTitle: str
   id: ID
   previousTitle: str
   subject: RenamedTitleSubject

class ReopenedEvent(GQLObject):
   actor: Actor
   closable: Closable
   createdAt: DateTime
   id: ID
   stateReason: IssueStateReason

class SubscribedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   subscribable: Subscribable

class TransferredEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   fromRepository: Repository
   id: ID
   issue: NewType('Issue', GQLObject) ## Circular Reference for Issue

class UnassignedEvent(GQLObject):
   actor: Actor
   assignable: Assignable
   assignee: Assignee
   createdAt: DateTime
   id: ID

class UnlabeledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   label: Label
   labelable: Labelable

class UnlockedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   lockable: Lockable

class UnsubscribedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   subscribable: Subscribable

class UserBlockedEvent(GQLObject):
   actor: Actor
   blockDuration: UserBlockDuration
   createdAt: DateTime
   id: ID
   subject: NewType('User', GQLObject) ## Circular Reference for User

class IssueTimelineItem(GQLObject): 
   pass

class IssueTimelineItemEdge(GQLObject):
   cursor: str
   node: IssueTimelineItem

class list_IssueTimelineItemEdge(list, IssueTimelineItemEdge): pass

class list_IssueTimelineItem(list, IssueTimelineItem): pass

class IssueTimelineConnection(GQLObject):
   edges: list_IssueTimelineItemEdge[IssueTimelineItemEdge]
   nodes: list_IssueTimelineItem[IssueTimelineItem]
   pageInfo: PageInfo
   totalCount: int

class AddedToProjectEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   databaseId: int
   id: ID

class CommentDeletedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   databaseId: int
   deletedCommentAuthor: Actor
   id: ID

class ConnectedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   isCrossRepository: bool
   source: ReferencedSubject
   subject: ReferencedSubject

class ConvertedNoteToIssueEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   databaseId: int
   id: ID

class ConvertedToDiscussionEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   discussion: Discussion
   id: ID

class DisconnectedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   isCrossRepository: bool
   source: ReferencedSubject
   subject: ReferencedSubject

class MarkedAsDuplicateEvent(GQLObject):
   actor: Actor
   canonical: IssueOrPullRequest
   createdAt: DateTime
   duplicate: IssueOrPullRequest
   id: ID
   isCrossRepository: bool

class MentionedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   databaseId: int
   id: ID

class MovedColumnsInProjectEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   databaseId: int
   id: ID

class PinnedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   issue: NewType('Issue', GQLObject) ## Circular Reference for Issue

class RemovedFromProjectEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   databaseId: int
   id: ID

class UnmarkedAsDuplicateEvent(GQLObject):
   actor: Actor
   canonical: IssueOrPullRequest
   createdAt: DateTime
   duplicate: IssueOrPullRequest
   id: ID
   isCrossRepository: bool

class UnpinnedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   issue: NewType('Issue', GQLObject) ## Circular Reference for Issue

class IssueTimelineItems(GQLObject): 
   pass

class IssueTimelineItemsEdge(GQLObject):
   cursor: str
   node: IssueTimelineItems

class list_IssueTimelineItemsEdge(list, IssueTimelineItemsEdge): pass

class list_IssueTimelineItems(list, IssueTimelineItems): pass

class IssueTimelineItemsConnection(GQLObject):
   edges: list_IssueTimelineItemsEdge[IssueTimelineItemsEdge]
   filteredCount: int
   nodes: list_IssueTimelineItems[IssueTimelineItems]
   pageCount: int
   pageInfo: PageInfo
   totalCount: int
   updatedAt: DateTime

class CONGC_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class HPINQ_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class WFHEC_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject):
      includeNotificationContexts: bool

   _args: HovercardArgs



class OIOLZ_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class ETDLM_LinkedBranchConnection_Field(LinkedBranchConnection):
   class LinkedBranchConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: LinkedBranchConnectionArgs



class VSNTH_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class MKUAJ_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: ProjectCardConnectionArgs



class BUXHO_ProjectV2ItemConnection_Field(Generic[ProjectV2ItemConnection]):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class VBDIS_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class JRSWE_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class EJUON_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class NonNull_IssueTimelineItemsItemType(GQLObject): pass

class ZLADT_IssueTimelineItemsConnection_Field(IssueTimelineItemsConnection):
   class IssueTimelineItemsConnectionArgs(GQLArgsSet, GQLObject):
      since: DateTime
      skip: int
      itemTypes: list[NonNull_IssueTimelineItemsItemType]
      after: str
      before: str
      first: int
      last: int

   _args: IssueTimelineItemsConnectionArgs



class OMRNC_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class BBHNN_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class IRGFP_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class Issue(GQLObject):
   activeLockReason: LockReason
   assignees: CONGC_UserConnection_Field
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyResourcePath: URI
   bodyText: str
   bodyUrl: URI
   closed: bool
   closedAt: DateTime
   comments: HPINQ_IssueCommentConnection_Field
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   fullDatabaseId: BigInt
   hovercard: WFHEC_Hovercard_Field
   id: ID
   includesCreatedEdit: bool
   isPinned: bool
   isReadByViewer: bool
   labels: OIOLZ_LabelConnection_Field
   lastEditedAt: DateTime
   linkedBranches: ETDLM_LinkedBranchConnection_Field
   locked: bool
   milestone: Milestone
   number: int
   participants: VSNTH_UserConnection_Field
   projectCards: MKUAJ_ProjectCardConnection_Field
   projectItems: BUXHO_ProjectV2ItemConnection_Field ## Circular Reference for ProjectV2ItemConnection
   projectV2: VBDIS_ProjectV2_Field ## Circular Reference for ProjectV2
   projectsV2: JRSWE_ProjectV2Connection_Field
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: EJUON_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   state: IssueState
   stateReason: IssueStateReason
   timelineItems: ZLADT_IssueTimelineItemsConnection_Field
   title: str
   titleHTML: str
   trackedInIssues: OMRNC_IssueConnection_Field
   trackedIssues: BBHNN_IssueConnection_Field
   trackedIssuesCount: BEYLW_trackedIssuesCount_Field
   updatedAt: DateTime
   url: URI
   userContentEdits: IRGFP_UserContentEditConnection_Field
   viewerCanClose: bool
   viewerCanDelete: bool
   viewerCanReact: bool
   viewerCanReopen: bool
   viewerCanSubscribe: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]
   viewerDidAuthor: bool
   viewerSubscription: SubscriptionState

class ProjectV2ItemContent(GQLObject): 
   pass

class ProjectV2ItemFieldDateValue(GQLObject):
   createdAt: DateTime
   creator: Actor
   databaseId: int
   date: Date
   field: ProjectV2FieldConfiguration
   id: ID
   item: NewType('ProjectV2Item', GQLObject) ## Circular Reference for ProjectV2Item
   updatedAt: DateTime

class ProjectV2ItemFieldIterationValue(GQLObject):
   createdAt: DateTime
   creator: Actor
   databaseId: int
   duration: int
   field: ProjectV2FieldConfiguration
   id: ID
   item: NewType('ProjectV2Item', GQLObject) ## Circular Reference for ProjectV2Item
   iterationId: str
   startDate: Date
   title: str
   titleHTML: str
   updatedAt: DateTime

class WCEAF_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class ProjectV2ItemFieldLabelValue(GQLObject):
   field: ProjectV2FieldConfiguration
   labels: WCEAF_LabelConnection_Field

class ProjectV2ItemFieldMilestoneValue(GQLObject):
   field: ProjectV2FieldConfiguration
   milestone: Milestone

class ProjectV2ItemFieldNumberValue(GQLObject):
   createdAt: DateTime
   creator: Actor
   databaseId: int
   field: ProjectV2FieldConfiguration
   id: ID
   item: NewType('ProjectV2Item', GQLObject) ## Circular Reference for ProjectV2Item
   number: float
   updatedAt: DateTime

class STJRV_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: PullRequestOrder

   _args: PullRequestConnectionArgs



class ProjectV2ItemFieldPullRequestValue(GQLObject):
   field: ProjectV2FieldConfiguration
   pullRequests: STJRV_PullRequestConnection_Field ## Circular Reference for PullRequestConnection

class ProjectV2ItemFieldRepositoryValue(GQLObject):
   field: ProjectV2FieldConfiguration
   repository: Repository

class RequestedReviewer(GQLObject): 
   pass

class RequestedReviewerEdge(GQLObject):
   cursor: str
   node: RequestedReviewer

class list_RequestedReviewerEdge(list, RequestedReviewerEdge): pass

class list_RequestedReviewer(list, RequestedReviewer): pass

class RequestedReviewerConnection(GQLObject):
   edges: list_RequestedReviewerEdge[RequestedReviewerEdge]
   nodes: list_RequestedReviewer[RequestedReviewer]
   pageInfo: PageInfo
   totalCount: int

class TMQLM_RequestedReviewerConnection_Field(RequestedReviewerConnection):
   class RequestedReviewerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: RequestedReviewerConnectionArgs



class ProjectV2ItemFieldReviewerValue(GQLObject):
   field: ProjectV2FieldConfiguration
   reviewers: TMQLM_RequestedReviewerConnection_Field

class ProjectV2ItemFieldSingleSelectValue(GQLObject):
   color: ProjectV2SingleSelectFieldOptionColor
   createdAt: DateTime
   creator: Actor
   databaseId: int
   description: str
   descriptionHTML: str
   field: ProjectV2FieldConfiguration
   id: ID
   item: NewType('ProjectV2Item', GQLObject) ## Circular Reference for ProjectV2Item
   name: str
   nameHTML: str
   optionId: str
   updatedAt: DateTime

class ProjectV2ItemFieldTextValue(GQLObject):
   createdAt: DateTime
   creator: Actor
   databaseId: int
   field: ProjectV2FieldConfiguration
   id: ID
   item: NewType('ProjectV2Item', GQLObject) ## Circular Reference for ProjectV2Item
   text: str
   updatedAt: DateTime

class SMHDV_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class ProjectV2ItemFieldUserValue(GQLObject):
   field: ProjectV2FieldConfiguration
   users: SMHDV_UserConnection_Field

class ProjectV2ItemFieldValue(GQLObject): 
   pass

class ProjectV2ItemFieldValueEdge(GQLObject):
   cursor: str
   node: ProjectV2ItemFieldValue

class list_ProjectV2ItemFieldValueEdge(list, ProjectV2ItemFieldValueEdge): pass

class list_ProjectV2ItemFieldValue(list, ProjectV2ItemFieldValue): pass

class ProjectV2ItemFieldValueConnection(GQLObject):
   edges: list_ProjectV2ItemFieldValueEdge[ProjectV2ItemFieldValueEdge]
   nodes: list_ProjectV2ItemFieldValue[ProjectV2ItemFieldValue]
   pageInfo: PageInfo
   totalCount: int

class PYPCQ_ProjectV2ItemFieldValue_Field(ProjectV2ItemFieldValue):
   class ProjectV2ItemFieldValueArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: ProjectV2ItemFieldValueArgs



class KKEGC_ProjectV2ItemFieldValueConnection_Field(ProjectV2ItemFieldValueConnection):
   class ProjectV2ItemFieldValueConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ItemFieldValueOrder

   _args: ProjectV2ItemFieldValueConnectionArgs



class ProjectV2Item(GQLObject):
   content: ProjectV2ItemContent
   createdAt: DateTime
   creator: Actor
   databaseId: int
   fieldValueByName: PYPCQ_ProjectV2ItemFieldValue_Field
   fieldValues: KKEGC_ProjectV2ItemFieldValueConnection_Field
   id: ID
   isArchived: bool
   project: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2
   type: ProjectV2ItemType
   updatedAt: DateTime

class ProjectV2ItemEdge(GQLObject):
   cursor: str
   node: ProjectV2Item

class list_ProjectV2ItemEdge(list, ProjectV2ItemEdge): pass

class list_ProjectV2Item(list, ProjectV2Item): pass

class ProjectV2ItemConnection(GQLObject):
   edges: list_ProjectV2ItemEdge[ProjectV2ItemEdge]
   nodes: list_ProjectV2Item[ProjectV2Item]
   pageInfo: PageInfo
   totalCount: int

class RPPKD_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class QRWJB_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class ProjectV2Owner(GQLObject):
   id: ID
   projectV2: RPPKD_ProjectV2_Field ## Circular Reference for ProjectV2
   projectsV2: QRWJB_ProjectV2Connection_Field

class ProjectV2FieldEdge(GQLObject):
   cursor: str
   node: ProjectV2Field

class list_ProjectV2FieldEdge(list, ProjectV2FieldEdge): pass

class list_ProjectV2Field(list, ProjectV2Field): pass

class ProjectV2FieldConnection(GQLObject):
   edges: list_ProjectV2FieldEdge[ProjectV2FieldEdge]
   nodes: list_ProjectV2Field[ProjectV2Field]
   pageInfo: PageInfo
   totalCount: int

class ProjectV2SortBy(GQLObject):
   direction: OrderDirection
   field: ProjectV2Field

class ProjectV2SortByEdge(GQLObject):
   cursor: str
   node: ProjectV2SortBy

class list_ProjectV2SortByEdge(list, ProjectV2SortByEdge): pass

class list_ProjectV2SortBy(list, ProjectV2SortBy): pass

class ProjectV2SortByConnection(GQLObject):
   edges: list_ProjectV2SortByEdge[ProjectV2SortByEdge]
   nodes: list_ProjectV2SortBy[ProjectV2SortBy]
   pageInfo: PageInfo
   totalCount: int

class ProjectV2SortByField(GQLObject):
   direction: OrderDirection
   field: ProjectV2FieldConfiguration

class ProjectV2SortByFieldEdge(GQLObject):
   cursor: str
   node: ProjectV2SortByField

class list_ProjectV2SortByFieldEdge(list, ProjectV2SortByFieldEdge): pass

class list_ProjectV2SortByField(list, ProjectV2SortByField): pass

class ProjectV2SortByFieldConnection(GQLObject):
   edges: list_ProjectV2SortByFieldEdge[ProjectV2SortByFieldEdge]
   nodes: list_ProjectV2SortByField[ProjectV2SortByField]
   pageInfo: PageInfo
   totalCount: int

class NVDHU_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class DGQOV_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class TNIXA_ProjectV2SortByFieldConnection_Field(ProjectV2SortByFieldConnection):
   class ProjectV2SortByFieldConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2SortByFieldConnectionArgs



class AOQYM_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class ProjectV2View(GQLObject):
   createdAt: DateTime
   databaseId: int
   fields: NVDHU_ProjectV2FieldConfigurationConnection_Field
   filter: str
   groupByFields: DGQOV_ProjectV2FieldConfigurationConnection_Field
   id: ID
   layout: ProjectV2ViewLayout
   name: str
   number: int
   project: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2
   sortByFields: TNIXA_ProjectV2SortByFieldConnection_Field
   updatedAt: DateTime
   verticalGroupByFields: AOQYM_ProjectV2FieldConfigurationConnection_Field

class ProjectV2ViewEdge(GQLObject):
   cursor: str
   node: ProjectV2View

class list_ProjectV2ViewEdge(list, ProjectV2ViewEdge): pass

class list_ProjectV2View(list, ProjectV2View): pass

class ProjectV2ViewConnection(GQLObject):
   edges: list_ProjectV2ViewEdge[ProjectV2ViewEdge]
   nodes: list_ProjectV2View[ProjectV2View]
   pageInfo: PageInfo
   totalCount: int

class ProjectV2Workflow(GQLObject):
   createdAt: DateTime
   databaseId: int
   enabled: bool
   id: ID
   name: str
   number: int
   project: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2
   updatedAt: DateTime

class ProjectV2WorkflowEdge(GQLObject):
   cursor: str
   node: ProjectV2Workflow

class list_ProjectV2WorkflowEdge(list, ProjectV2WorkflowEdge): pass

class list_ProjectV2Workflow(list, ProjectV2Workflow): pass

class ProjectV2WorkflowConnection(GQLObject):
   edges: list_ProjectV2WorkflowEdge[ProjectV2WorkflowEdge]
   nodes: list_ProjectV2Workflow[ProjectV2Workflow]
   pageInfo: PageInfo
   totalCount: int

class HGFTD_ProjectV2FieldConfiguration_Field(ProjectV2FieldConfiguration):
   class ProjectV2FieldConfigurationArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: ProjectV2FieldConfigurationArgs



class VYHHQ_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class ZWPHJ_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ItemOrder

   _args: ProjectV2ItemConnectionArgs



class PAHCQ_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: RepositoryOrder

   _args: RepositoryConnectionArgs



class YVBJA_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: TeamOrder

   _args: TeamConnectionArgs



class XZTOJ_ProjectV2View_Field(ProjectV2View):
   class ProjectV2ViewArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2ViewArgs



class FFXKI_ProjectV2ViewConnection_Field(ProjectV2ViewConnection):
   class ProjectV2ViewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ViewOrder

   _args: ProjectV2ViewConnectionArgs



class ZZDNC_ProjectV2Workflow_Field(ProjectV2Workflow):
   class ProjectV2WorkflowArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2WorkflowArgs



class HSYCR_ProjectV2WorkflowConnection_Field(ProjectV2WorkflowConnection):
   class ProjectV2WorkflowConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2WorkflowOrder

   _args: ProjectV2WorkflowConnectionArgs



class ProjectV2(GQLObject):
   closed: bool
   closedAt: DateTime
   createdAt: DateTime
   creator: Actor
   databaseId: int
   field: HGFTD_ProjectV2FieldConfiguration_Field
   fields: VYHHQ_ProjectV2FieldConfigurationConnection_Field
   id: ID
   items: ZWPHJ_ProjectV2ItemConnection_Field
   number: int
   owner: ProjectV2Owner
   public: bool
   readme: str
   repositories: PAHCQ_RepositoryConnection_Field
   resourcePath: URI
   shortDescription: str
   teams: YVBJA_TeamConnection_Field
   template: bool
   title: str
   updatedAt: DateTime
   url: URI
   view: XZTOJ_ProjectV2View_Field
   viewerCanClose: bool
   viewerCanReopen: bool
   viewerCanUpdate: bool
   views: FFXKI_ProjectV2ViewConnection_Field
   workflow: ZZDNC_ProjectV2Workflow_Field
   workflows: HSYCR_ProjectV2WorkflowConnection_Field

class TeamRepositoryEdge(GQLObject):
   cursor: str
   node: Repository
   permission: RepositoryPermission

class list_TeamRepositoryEdge(list, TeamRepositoryEdge): pass

class list_Repository(list, Repository): pass

class TeamRepositoryConnection(GQLObject):
   edges: list_TeamRepositoryEdge[TeamRepositoryEdge]
   nodes: list_Repository[Repository]
   pageInfo: PageInfo
   totalCount: int

class MIRBO_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class FWSPZ_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: TeamOrder
      userLogins: list[NonNull_str]
      immediateOnly: bool
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class HGHRN_TeamDiscussion_Field(TeamDiscussion):
   class TeamDiscussionArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: TeamDiscussionArgs



class ZOFSU_TeamDiscussionConnection_Field(TeamDiscussionConnection):
   class TeamDiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      isPinned: bool
      orderBy: TeamDiscussionOrder

   _args: TeamDiscussionConnectionArgs



class EQNVX_OrganizationInvitationConnection_Field(OrganizationInvitationConnection):
   class OrganizationInvitationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationInvitationConnectionArgs



class XPXLU_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class ENGYK_TeamMemberConnection_Field(TeamMemberConnection):
   class TeamMemberConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: str
      membership: TeamMembershipType
      role: TeamMemberRole
      orderBy: TeamMemberOrder

   _args: TeamMemberConnectionArgs



class IWRXD_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class MOBEO_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2Order
      filterBy: ProjectV2Filters
      query: str

   _args: ProjectV2ConnectionArgs



class ELZPX_TeamRepositoryConnection_Field(TeamRepositoryConnection):
   class TeamRepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: TeamRepositoryOrder

   _args: TeamRepositoryConnectionArgs



class Team(GQLObject):
   ancestors: MIRBO_TeamConnection_Field
   avatarUrl: GPMGM_URI_Field
   childTeams: FWSPZ_TeamConnection_Field
   combinedSlug: str
   createdAt: DateTime
   databaseId: int
   description: str
   discussion: HGHRN_TeamDiscussion_Field
   discussions: ZOFSU_TeamDiscussionConnection_Field
   discussionsResourcePath: URI
   discussionsUrl: URI
   editTeamResourcePath: URI
   editTeamUrl: URI
   id: ID
   invitations: EQNVX_OrganizationInvitationConnection_Field
   memberStatuses: XPXLU_UserStatusConnection_Field
   members: ENGYK_TeamMemberConnection_Field
   membersResourcePath: URI
   membersUrl: URI
   name: str
   newTeamResourcePath: URI
   newTeamUrl: URI
   notificationSetting: TeamNotificationSetting
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   parentTeam: NewType('Team', GQLObject) ## Circular Reference for Team
   privacy: TeamPrivacy
   projectV2: IWRXD_ProjectV2_Field
   projectsV2: MOBEO_ProjectV2Connection_Field
   repositories: ELZPX_TeamRepositoryConnection_Field
   repositoriesResourcePath: URI
   repositoriesUrl: URI
   resourcePath: URI
   slug: str
   teamsResourcePath: URI
   teamsUrl: URI
   updatedAt: DateTime
   url: URI
   viewerCanAdminister: bool
   viewerCanSubscribe: bool
   viewerSubscription: SubscriptionState

class BranchActorAllowanceActor(GQLObject): 
   pass

class BypassForcePushAllowance(GQLObject):
   actor: BranchActorAllowanceActor
   branchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   id: ID

class BypassForcePushAllowanceEdge(GQLObject):
   cursor: str
   node: BypassForcePushAllowance

class list_BypassForcePushAllowanceEdge(list, BypassForcePushAllowanceEdge): pass

class list_BypassForcePushAllowance(list, BypassForcePushAllowance): pass

class BypassForcePushAllowanceConnection(GQLObject):
   edges: list_BypassForcePushAllowanceEdge[BypassForcePushAllowanceEdge]
   nodes: list_BypassForcePushAllowance[BypassForcePushAllowance]
   pageInfo: PageInfo
   totalCount: int

class BypassPullRequestAllowance(GQLObject):
   actor: BranchActorAllowanceActor
   branchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   id: ID

class BypassPullRequestAllowanceEdge(GQLObject):
   cursor: str
   node: BypassPullRequestAllowance

class list_BypassPullRequestAllowanceEdge(list, BypassPullRequestAllowanceEdge): pass

class list_BypassPullRequestAllowance(list, BypassPullRequestAllowance): pass

class BypassPullRequestAllowanceConnection(GQLObject):
   edges: list_BypassPullRequestAllowanceEdge[BypassPullRequestAllowanceEdge]
   nodes: list_BypassPullRequestAllowance[BypassPullRequestAllowance]
   pageInfo: PageInfo
   totalCount: int

class PushAllowanceActor(GQLObject): 
   pass

class PushAllowance(GQLObject):
   actor: PushAllowanceActor
   branchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   id: ID

class PushAllowanceEdge(GQLObject):
   cursor: str
   node: PushAllowance

class list_PushAllowanceEdge(list, PushAllowanceEdge): pass

class list_PushAllowance(list, PushAllowance): pass

class PushAllowanceConnection(GQLObject):
   edges: list_PushAllowanceEdge[PushAllowanceEdge]
   nodes: list_PushAllowance[PushAllowance]
   pageInfo: PageInfo
   totalCount: int

class RequiredStatusCheckDescription(GQLObject):
   app: NewType('App', GQLObject) ## Circular Reference for App
   context: str

class ReviewDismissalAllowanceActor(GQLObject): 
   pass

class ReviewDismissalAllowance(GQLObject):
   actor: ReviewDismissalAllowanceActor
   branchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   id: ID

class ReviewDismissalAllowanceEdge(GQLObject):
   cursor: str
   node: ReviewDismissalAllowance

class list_ReviewDismissalAllowanceEdge(list, ReviewDismissalAllowanceEdge): pass

class list_ReviewDismissalAllowance(list, ReviewDismissalAllowance): pass

class ReviewDismissalAllowanceConnection(GQLObject):
   edges: list_ReviewDismissalAllowanceEdge[ReviewDismissalAllowanceEdge]
   nodes: list_ReviewDismissalAllowance[ReviewDismissalAllowance]
   pageInfo: PageInfo
   totalCount: int

class QJUQJ_BranchProtectionRuleConflictConnection_Field(BranchProtectionRuleConflictConnection):
   class BranchProtectionRuleConflictConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BranchProtectionRuleConflictConnectionArgs



class XTKPP_BypassForcePushAllowanceConnection_Field(BypassForcePushAllowanceConnection):
   class BypassForcePushAllowanceConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BypassForcePushAllowanceConnectionArgs



class HCXKZ_BypassPullRequestAllowanceConnection_Field(BypassPullRequestAllowanceConnection):
   class BypassPullRequestAllowanceConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BypassPullRequestAllowanceConnectionArgs



class EGJIF_RefConnection_Field(RefConnection):
   class RefConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: RefConnectionArgs



class OGDVO_PushAllowanceConnection_Field(PushAllowanceConnection):
   class PushAllowanceConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PushAllowanceConnectionArgs



class list_RequiredStatusCheckDescription(list, RequiredStatusCheckDescription): pass

class YGAFV_ReviewDismissalAllowanceConnection_Field(ReviewDismissalAllowanceConnection):
   class ReviewDismissalAllowanceConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ReviewDismissalAllowanceConnectionArgs



class BranchProtectionRule(GQLObject):
   allowsDeletions: bool
   allowsForcePushes: bool
   blocksCreations: bool
   branchProtectionRuleConflicts: QJUQJ_BranchProtectionRuleConflictConnection_Field
   bypassForcePushAllowances: XTKPP_BypassForcePushAllowanceConnection_Field
   bypassPullRequestAllowances: HCXKZ_BypassPullRequestAllowanceConnection_Field
   creator: Actor
   databaseId: int
   dismissesStaleReviews: bool
   id: ID
   isAdminEnforced: bool
   lockAllowsFetchAndMerge: bool
   lockBranch: bool
   matchingRefs: EGJIF_RefConnection_Field
   pattern: str
   pushAllowances: OGDVO_PushAllowanceConnection_Field
   repository: Repository
   requireLastPushApproval: bool
   requiredApprovingReviewCount: int
   requiredDeploymentEnvironments: list[str]
   requiredStatusCheckContexts: list[str]
   requiredStatusChecks: list_RequiredStatusCheckDescription[RequiredStatusCheckDescription]
   requiresApprovingReviews: bool
   requiresCodeOwnerReviews: bool
   requiresCommitSignatures: bool
   requiresConversationResolution: bool
   requiresDeployments: bool
   requiresLinearHistory: bool
   requiresStatusChecks: bool
   requiresStrictStatusChecks: bool
   restrictsPushes: bool
   restrictsReviewDismissals: bool
   reviewDismissalAllowances: YGAFV_ReviewDismissalAllowanceConnection_Field

class CommitEdge(GQLObject):
   cursor: str
   node: NewType('Commit', GQLObject) ## Circular Reference for Commit

class list_CommitEdge(list, CommitEdge): pass

class ComparisonCommitConnection(GQLObject):
   authorCount: int
   edges: list_CommitEdge[CommitEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Commit
   pageInfo: PageInfo
   totalCount: int

class BETEI_ComparisonCommitConnection_Field(ComparisonCommitConnection):
   class ComparisonCommitConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ComparisonCommitConnectionArgs



class Comparison(GQLObject):
   aheadBy: int
   baseTarget: GitObject
   behindBy: int
   commits: BETEI_ComparisonCommitConnection_Field
   headTarget: GitObject
   id: ID
   status: ComparisonStatus

class CDOFX_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      states: list[NonNull_PullRequestState]
      labels: list[NonNull_str]
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class ISHTN_Comparison_Field(Comparison):
   class ComparisonArgs(GQLArgsSet, GQLObject):
      headRef: NonNull_str

   _args: ComparisonArgs



class Ref(GQLObject):
   associatedPullRequests: CDOFX_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   branchProtectionRule: BranchProtectionRule
   compare: ISHTN_Comparison_Field
   id: ID
   name: str
   prefix: str
   refUpdateRule: RefUpdateRule
   repository: Repository
   target: GitObject

class PullRequestCommit(GQLObject):
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   resourcePath: URI
   url: URI

class PullRequestCommitEdge(GQLObject):
   cursor: str
   node: PullRequestCommit

class list_PullRequestCommitEdge(list, PullRequestCommitEdge): pass

class list_PullRequestCommit(list, PullRequestCommit): pass

class PullRequestCommitConnection(GQLObject):
   edges: list_PullRequestCommitEdge[PullRequestCommitEdge]
   nodes: list_PullRequestCommit[PullRequestCommit]
   pageInfo: PageInfo
   totalCount: int

class PullRequestChangedFileEdge(GQLObject):
   cursor: str
   node: PullRequestChangedFile

class list_PullRequestChangedFileEdge(list, PullRequestChangedFileEdge): pass

class list_PullRequestChangedFile(list, PullRequestChangedFile): pass

class PullRequestChangedFileConnection(GQLObject):
   edges: list_PullRequestChangedFileEdge[PullRequestChangedFileEdge]
   nodes: list_PullRequestChangedFile[PullRequestChangedFile]
   pageInfo: PageInfo
   totalCount: int

class UFPWB_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class QGUBD_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class PullRequestReviewComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyText: str
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   diffHunk: str
   draftedAt: DateTime
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   isMinimized: bool
   lastEditedAt: DateTime
   line: int
   minimizedReason: str
   originalCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   originalLine: int
   originalStartLine: int
   outdated: bool
   path: str
   publishedAt: DateTime
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   pullRequestReview: NewType('PullRequestReview', GQLObject) ## Circular Reference for PullRequestReview
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: UFPWB_ReactionConnection_Field
   replyTo: NewType('PullRequestReviewComment', GQLObject) ## Circular Reference for PullRequestReviewComment
   repository: Repository
   resourcePath: URI
   startLine: int
   state: PullRequestReviewCommentState
   subjectType: PullRequestReviewThreadSubjectType
   updatedAt: DateTime
   url: URI
   userContentEdits: QGUBD_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanMinimize: bool
   viewerCanReact: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]
   viewerDidAuthor: bool

class PullRequestReviewCommentEdge(GQLObject):
   cursor: str
   node: PullRequestReviewComment

class list_PullRequestReviewCommentEdge(list, PullRequestReviewCommentEdge): pass

class list_PullRequestReviewComment(list, PullRequestReviewComment): pass

class PullRequestReviewCommentConnection(GQLObject):
   edges: list_PullRequestReviewCommentEdge[PullRequestReviewCommentEdge]
   nodes: list_PullRequestReviewComment[PullRequestReviewComment]
   pageInfo: PageInfo
   totalCount: int

class FKZTD_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewCommentConnectionArgs



class FXECN_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class DDXQU_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class EEBDN_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class PullRequestReview(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation
   authorCanPushToRepository: bool
   body: str
   bodyHTML: HTML
   bodyText: str
   comments: FKZTD_PullRequestReviewCommentConnection_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   lastEditedAt: DateTime
   onBehalfOf: FXECN_TeamConnection_Field
   publishedAt: DateTime
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: DDXQU_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   state: PullRequestReviewState
   submittedAt: DateTime
   updatedAt: DateTime
   url: URI
   userContentEdits: EEBDN_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanReact: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]
   viewerDidAuthor: bool

class PullRequestReviewEdge(GQLObject):
   cursor: str
   node: PullRequestReview

class list_PullRequestReviewEdge(list, PullRequestReviewEdge): pass

class list_PullRequestReview(list, PullRequestReview): pass

class PullRequestReviewConnection(GQLObject):
   edges: list_PullRequestReviewEdge[PullRequestReviewEdge]
   nodes: list_PullRequestReview[PullRequestReview]
   pageInfo: PageInfo
   totalCount: int

class ReviewRequest(GQLObject):
   asCodeOwner: bool
   databaseId: int
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   requestedReviewer: RequestedReviewer

class ReviewRequestEdge(GQLObject):
   cursor: str
   node: ReviewRequest

class list_ReviewRequestEdge(list, ReviewRequestEdge): pass

class list_ReviewRequest(list, ReviewRequest): pass

class ReviewRequestConnection(GQLObject):
   edges: list_ReviewRequestEdge[ReviewRequestEdge]
   nodes: list_ReviewRequest[ReviewRequest]
   pageInfo: PageInfo
   totalCount: int

class GZAHI_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      skip: int

   _args: PullRequestReviewCommentConnectionArgs



class PullRequestReviewThread(GQLObject):
   comments: GZAHI_PullRequestReviewCommentConnection_Field
   diffSide: DiffSide
   id: ID
   isCollapsed: bool
   isOutdated: bool
   isResolved: bool
   line: int
   originalLine: int
   originalStartLine: int
   path: str
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   repository: Repository
   resolvedBy: NewType('User', GQLObject) ## Circular Reference for User
   startDiffSide: DiffSide
   startLine: int
   subjectType: PullRequestReviewThreadSubjectType
   viewerCanReply: bool
   viewerCanResolve: bool
   viewerCanUnresolve: bool

class PullRequestReviewThreadEdge(GQLObject):
   cursor: str
   node: PullRequestReviewThread

class list_PullRequestReviewThreadEdge(list, PullRequestReviewThreadEdge): pass

class list_PullRequestReviewThread(list, PullRequestReviewThread): pass

class PullRequestReviewThreadConnection(GQLObject):
   edges: list_PullRequestReviewThreadEdge[PullRequestReviewThreadEdge]
   nodes: list_PullRequestReviewThread[PullRequestReviewThread]
   pageInfo: PageInfo
   totalCount: int

class SuggestedReviewer(GQLObject):
   isAuthor: bool
   isCommenter: bool
   reviewer: NewType('User', GQLObject) ## Circular Reference for User

class BaseRefDeletedEvent(GQLObject):
   actor: Actor
   baseRefName: str
   createdAt: DateTime
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class BaseRefForcePushedEvent(GQLObject):
   actor: Actor
   afterCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   beforeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   ref: Ref

class KTSAK_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class CommitCommentThread(GQLObject):
   comments: KTSAK_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   id: ID
   path: str
   position: int
   repository: Repository

class DeployedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   databaseId: int
   deployment: Deployment
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   ref: Ref

class DeploymentEnvironmentChangedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   deploymentStatus: DeploymentStatus
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class HeadRefDeletedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   headRef: Ref
   headRefName: str
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class HeadRefForcePushedEvent(GQLObject):
   actor: Actor
   afterCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   beforeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   ref: Ref

class HeadRefRestoredEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class MergedEvent(GQLObject):
   actor: Actor
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime
   id: ID
   mergeRef: Ref
   mergeRefName: str
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   resourcePath: URI
   url: URI

class ReviewDismissedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   databaseId: int
   dismissalMessage: str
   dismissalMessageHTML: str
   id: ID
   previousReviewState: PullRequestReviewState
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   pullRequestCommit: PullRequestCommit
   resourcePath: URI
   review: PullRequestReview
   url: URI

class ReviewRequestRemovedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   requestedReviewer: RequestedReviewer

class ReviewRequestedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   requestedReviewer: RequestedReviewer

class PullRequestTimelineItem(GQLObject): 
   pass

class PullRequestTimelineItemEdge(GQLObject):
   cursor: str
   node: PullRequestTimelineItem

class list_PullRequestTimelineItemEdge(list, PullRequestTimelineItemEdge): pass

class list_PullRequestTimelineItem(list, PullRequestTimelineItem): pass

class PullRequestTimelineConnection(GQLObject):
   edges: list_PullRequestTimelineItemEdge[PullRequestTimelineItemEdge]
   nodes: list_PullRequestTimelineItem[PullRequestTimelineItem]
   pageInfo: PageInfo
   totalCount: int

class AddedToMergeQueueEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   enqueuer: NewType('User', GQLObject) ## Circular Reference for User
   id: ID
   mergeQueue: MergeQueue
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class AutoMergeDisabledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   disabler: NewType('User', GQLObject) ## Circular Reference for User
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   reason: str
   reasonCode: str

class AutoMergeEnabledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   enabler: NewType('User', GQLObject) ## Circular Reference for User
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class AutoRebaseEnabledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   enabler: NewType('User', GQLObject) ## Circular Reference for User
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class AutoSquashEnabledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   enabler: NewType('User', GQLObject) ## Circular Reference for User
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class AutomaticBaseChangeFailedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   newBase: str
   oldBase: str
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class AutomaticBaseChangeSucceededEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   newBase: str
   oldBase: str
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class BaseRefChangedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   currentRefName: str
   databaseId: int
   id: ID
   previousRefName: str
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class ConvertToDraftEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   resourcePath: URI
   url: URI

class MRBRF_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class PullRequestCommitCommentThread(GQLObject):
   comments: MRBRF_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   id: ID
   path: str
   position: int
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   repository: Repository

class PullRequestRevisionMarker(GQLObject):
   createdAt: DateTime
   lastSeenCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest

class ReadyForReviewEvent(GQLObject):
   actor: Actor
   createdAt: DateTime
   id: ID
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   resourcePath: URI
   url: URI

class RemovedFromMergeQueueEvent(GQLObject):
   actor: Actor
   beforeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime
   enqueuer: NewType('User', GQLObject) ## Circular Reference for User
   id: ID
   mergeQueue: MergeQueue
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   reason: str

class PullRequestTimelineItems(GQLObject): 
   pass

class PullRequestTimelineItemsEdge(GQLObject):
   cursor: str
   node: PullRequestTimelineItems

class list_PullRequestTimelineItemsEdge(list, PullRequestTimelineItemsEdge): pass

class list_PullRequestTimelineItems(list, PullRequestTimelineItems): pass

class PullRequestTimelineItemsConnection(GQLObject):
   edges: list_PullRequestTimelineItemsEdge[PullRequestTimelineItemsEdge]
   filteredCount: int
   nodes: list_PullRequestTimelineItems[PullRequestTimelineItems]
   pageCount: int
   pageInfo: PageInfo
   totalCount: int
   updatedAt: DateTime

class WYEZL_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class TKMHD_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      userLinkedOnly: bool
      after: str
      before: str
      first: int
      last: int
      orderBy: IssueOrder

   _args: IssueConnectionArgs



class VIIXG_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class FBXSR_PullRequestCommitConnection_Field(PullRequestCommitConnection):
   class PullRequestCommitConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestCommitConnectionArgs



class ESEJA_PullRequestChangedFileConnection_Field(PullRequestChangedFileConnection):
   class PullRequestChangedFileConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestChangedFileConnectionArgs



class MQRJW_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject):
      includeNotificationContexts: bool

   _args: HovercardArgs



class ZMFIG_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class TCBMR_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      writersOnly: bool

   _args: PullRequestReviewConnectionArgs



class PSTPY_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewConnectionArgs



class GRSDP_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class DPOAN_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: ProjectCardConnectionArgs



class WDGZN_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class YCKZH_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class PHJAP_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class ZOKGU_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class JVLKG_ReviewRequestConnection_Field(ReviewRequestConnection):
   class ReviewRequestConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ReviewRequestConnectionArgs



class NJYQT_PullRequestReviewThreadConnection_Field(PullRequestReviewThreadConnection):
   class PullRequestReviewThreadConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewThreadConnectionArgs



class NonNull_PullRequestReviewState(GQLObject): pass

class RDBTP_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      states: list[NonNull_PullRequestReviewState]
      author: str

   _args: PullRequestReviewConnectionArgs



class list_SuggestedReviewer(list, SuggestedReviewer): pass

class NonNull_PullRequestTimelineItemsItemType(GQLObject): pass

class BKKAU_PullRequestTimelineItemsConnection_Field(PullRequestTimelineItemsConnection):
   class PullRequestTimelineItemsConnectionArgs(GQLArgsSet, GQLObject):
      since: DateTime
      skip: int
      itemTypes: list[NonNull_PullRequestTimelineItemsItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestTimelineItemsConnectionArgs



class KWEIK_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class PullRequest(GQLObject):
   activeLockReason: LockReason
   additions: int
   assignees: WYEZL_UserConnection_Field
   author: Actor
   authorAssociation: CommentAuthorAssociation
   autoMergeRequest: AutoMergeRequest
   baseRef: Ref
   baseRefName: str
   baseRefOid: GitObjectID
   baseRepository: Repository
   body: str
   bodyHTML: HTML
   bodyText: str
   changedFiles: int
   checksResourcePath: URI
   checksUrl: URI
   closed: bool
   closedAt: DateTime
   closingIssuesReferences: TKMHD_IssueConnection_Field
   comments: VIIXG_IssueCommentConnection_Field
   commits: FBXSR_PullRequestCommitConnection_Field
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   deletions: int
   editor: Actor
   files: ESEJA_PullRequestChangedFileConnection_Field
   headRef: Ref
   headRefName: str
   headRefOid: GitObjectID
   headRepository: Repository
   headRepositoryOwner: RepositoryOwner
   hovercard: MQRJW_Hovercard_Field
   id: ID
   includesCreatedEdit: bool
   isCrossRepository: bool
   isDraft: bool
   isReadByViewer: bool
   labels: ZMFIG_LabelConnection_Field
   lastEditedAt: DateTime
   latestOpinionatedReviews: TCBMR_PullRequestReviewConnection_Field
   latestReviews: PSTPY_PullRequestReviewConnection_Field
   locked: bool
   maintainerCanModify: bool
   mergeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   mergeQueueEntry: MergeQueueEntry
   mergeable: MergeableState
   merged: bool
   mergedAt: DateTime
   mergedBy: Actor
   milestone: Milestone
   number: int
   participants: GRSDP_UserConnection_Field
   permalink: URI
   potentialMergeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   projectCards: DPOAN_ProjectCardConnection_Field
   projectItems: WDGZN_ProjectV2ItemConnection_Field
   projectV2: YCKZH_ProjectV2_Field
   projectsV2: PHJAP_ProjectV2Connection_Field
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: ZOKGU_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   revertResourcePath: URI
   revertUrl: URI
   reviewDecision: PullRequestReviewDecision
   reviewRequests: JVLKG_ReviewRequestConnection_Field
   reviewThreads: NJYQT_PullRequestReviewThreadConnection_Field
   reviews: RDBTP_PullRequestReviewConnection_Field
   state: PullRequestState
   suggestedReviewers: list_SuggestedReviewer[SuggestedReviewer]
   timelineItems: BKKAU_PullRequestTimelineItemsConnection_Field
   title: str
   titleHTML: HTML
   totalCommentsCount: int
   updatedAt: DateTime
   url: URI
   userContentEdits: KWEIK_UserContentEditConnection_Field
   viewerCanApplySuggestion: bool
   viewerCanClose: bool
   viewerCanDeleteHeadRef: bool
   viewerCanDisableAutoMerge: bool
   viewerCanEditFiles: bool
   viewerCanEnableAutoMerge: bool
   viewerCanMergeAsAdmin: bool
   viewerCanReact: bool
   viewerCanReopen: bool
   viewerCanSubscribe: bool
   viewerCanUpdate: bool
   viewerCanUpdateBranch: bool
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]
   viewerDidAuthor: bool
   viewerLatestReview: PullRequestReview
   viewerLatestReviewRequest: ReviewRequest
   viewerMergeBodyText: EGLHV_viewerMergeBodyText_Field
   viewerMergeHeadlineText: UQTDZ_viewerMergeHeadlineText_Field
   viewerSubscription: SubscriptionState

class PullRequestEdge(GQLObject):
   cursor: str
   node: PullRequest

class list_PullRequestEdge(list, PullRequestEdge): pass

class list_PullRequest(list, PullRequest): pass

class PullRequestConnection(GQLObject):
   edges: list_PullRequestEdge[PullRequestEdge]
   nodes: list_PullRequest[PullRequest]
   pageInfo: PageInfo
   totalCount: int

class GitActor(GQLObject):
   avatarUrl: DDGXG_URI_Field
   date: GitTimestamp
   email: str
   name: str
   user: NewType('User', GQLObject) ## Circular Reference for User

class GitActorEdge(GQLObject):
   cursor: str
   node: GitActor

class list_GitActorEdge(list, GitActorEdge): pass

class list_GitActor(list, GitActor): pass

class GitActorConnection(GQLObject):
   edges: list_GitActorEdge[GitActorEdge]
   nodes: list_GitActor[GitActor]
   pageInfo: PageInfo
   totalCount: int

class BlameRange(GQLObject):
   age: int
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   endingLine: int
   startingLine: int

class list_BlameRange(list, BlameRange): pass

class Blame(GQLObject):
   ranges: list_BlameRange[BlameRange]

class CheckSuiteEdge(GQLObject):
   cursor: str
   node: NewType('CheckSuite', GQLObject) ## Circular Reference for CheckSuite

class list_CheckSuiteEdge(list, CheckSuiteEdge): pass

class CheckSuiteConnection(GQLObject):
   edges: list_CheckSuiteEdge[CheckSuiteEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for CheckSuite
   pageInfo: PageInfo
   totalCount: int

class TreeEntry(GQLObject):
   extension: str
   isGenerated: bool
   language: Language
   lineCount: int
   mode: int
   name: str
   nameRaw: Base64String
   object: GitObject
   oid: GitObjectID
   path: str
   pathRaw: Base64String
   repository: Repository
   size: int
   submodule: Submodule
   type: str

class CommitHistoryConnection(GQLObject):
   edges: list_CommitEdge[CommitEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Commit
   pageInfo: PageInfo
   totalCount: int

class CommitConnection(GQLObject):
   edges: list_CommitEdge[CommitEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Commit
   pageInfo: PageInfo
   totalCount: int

class GitSignature(GQLObject):
   email: str
   isValid: bool
   payload: str
   signature: str
   signer: NewType('User', GQLObject) ## Circular Reference for User
   state: GitSignatureState
   wasSignedByGitHub: bool

class CheckAnnotationSpan(GQLObject):
   end: CheckAnnotationPosition
   start: CheckAnnotationPosition

class CheckAnnotation(GQLObject):
   annotationLevel: CheckAnnotationLevel
   blobUrl: URI
   databaseId: int
   location: CheckAnnotationSpan
   message: str
   path: str
   rawDetails: str
   title: str

class CheckAnnotationEdge(GQLObject):
   cursor: str
   node: CheckAnnotation

class list_CheckAnnotationEdge(list, CheckAnnotationEdge): pass

class list_CheckAnnotation(list, CheckAnnotation): pass

class CheckAnnotationConnection(GQLObject):
   edges: list_CheckAnnotationEdge[CheckAnnotationEdge]
   nodes: list_CheckAnnotation[CheckAnnotation]
   pageInfo: PageInfo
   totalCount: int

class OYHJO_DeploymentReviewerConnection_Field(DeploymentReviewerConnection):
   class DeploymentReviewerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewerConnectionArgs



class DeploymentRequest(GQLObject):
   currentUserCanApprove: bool
   environment: Environment
   reviewers: OYHJO_DeploymentReviewerConnection_Field
   waitTimer: int
   waitTimerStartedAt: DateTime

class CheckStepEdge(GQLObject):
   cursor: str
   node: CheckStep

class list_CheckStepEdge(list, CheckStepEdge): pass

class list_CheckStep(list, CheckStep): pass

class CheckStepConnection(GQLObject):
   edges: list_CheckStepEdge[CheckStepEdge]
   nodes: list_CheckStep[CheckStep]
   pageInfo: PageInfo
   totalCount: int

class RMUVW_CheckAnnotationConnection_Field(CheckAnnotationConnection):
   class CheckAnnotationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CheckAnnotationConnectionArgs



class MHLSJ_CheckStepConnection_Field(CheckStepConnection):
   class CheckStepConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      number: int

   _args: CheckStepConnectionArgs



class CheckRun(GQLObject):
   annotations: RMUVW_CheckAnnotationConnection_Field
   checkSuite: NewType('CheckSuite', GQLObject) ## Circular Reference for CheckSuite
   completedAt: DateTime
   conclusion: CheckConclusionState
   databaseId: int
   deployment: Deployment
   detailsUrl: URI
   externalId: str
   id: ID
   isRequired: RIJZT_isRequired_Field
   name: str
   pendingDeploymentRequest: DeploymentRequest
   permalink: URI
   repository: Repository
   resourcePath: URI
   startedAt: DateTime
   status: CheckStatusState
   steps: MHLSJ_CheckStepConnection_Field
   summary: str
   text: str
   title: str
   url: URI

class StatusContext(GQLObject):
   avatarUrl: RFWIB_URI_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   context: str
   createdAt: DateTime
   creator: Actor
   description: str
   id: ID
   isRequired: XSWWW_isRequired_Field
   state: StatusState
   targetUrl: URI

class StatusCheckRollupContext(GQLObject): 
   pass

class StatusCheckRollupContextEdge(GQLObject):
   cursor: str
   node: StatusCheckRollupContext

class list_CheckRunStateCount(list, CheckRunStateCount): pass

class list_StatusCheckRollupContextEdge(list, StatusCheckRollupContextEdge): pass

class list_StatusCheckRollupContext(list, StatusCheckRollupContext): pass

class list_StatusContextStateCount(list, StatusContextStateCount): pass

class StatusCheckRollupContextConnection(GQLObject):
   checkRunCount: int
   checkRunCountsByState: list_CheckRunStateCount[CheckRunStateCount]
   edges: list_StatusCheckRollupContextEdge[StatusCheckRollupContextEdge]
   nodes: list_StatusCheckRollupContext[StatusCheckRollupContext]
   pageInfo: PageInfo
   statusContextCount: int
   statusContextCountsByState: list_StatusContextStateCount[StatusContextStateCount]
   totalCount: int

class JXHBL_StatusCheckRollupContextConnection_Field(StatusCheckRollupContextConnection):
   class StatusCheckRollupContextConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: StatusCheckRollupContextConnectionArgs



class BKUFE_StatusContext_Field(StatusContext):
   class StatusContextArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: StatusContextArgs



class list_StatusContext(list, StatusContext): pass

class Status(GQLObject):
   combinedContexts: JXHBL_StatusCheckRollupContextConnection_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   context: BKUFE_StatusContext_Field
   contexts: list_StatusContext[StatusContext]
   id: ID
   state: StatusState

class BMJOP_StatusCheckRollupContextConnection_Field(StatusCheckRollupContextConnection):
   class StatusCheckRollupContextConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: StatusCheckRollupContextConnectionArgs



class StatusCheckRollup(GQLObject):
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   contexts: BMJOP_StatusCheckRollupContextConnection_Field
   id: ID
   state: StatusState

class list_TreeEntry(list, TreeEntry): pass

class Tree(GQLObject):
   abbreviatedOid: str
   commitResourcePath: URI
   commitUrl: URI
   entries: list_TreeEntry[TreeEntry]
   id: ID
   oid: GitObjectID
   repository: Repository

class IPEON_PullRequestConnection_Field(PullRequestConnection):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: PullRequestOrder

   _args: PullRequestConnectionArgs



class UGQDX_GitActorConnection_Field(GitActorConnection):
   class GitActorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: GitActorConnectionArgs



class ALALR_Blame_Field(Blame):
   class BlameArgs(GQLArgsSet, GQLObject):
      path: NonNull_str

   _args: BlameArgs



class NSWTW_CheckSuiteConnection_Field(CheckSuiteConnection):
   class CheckSuiteConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      filterBy: CheckSuiteFilter

   _args: CheckSuiteConnectionArgs



class CAURM_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class IVYVG_DeploymentConnection_Field(DeploymentConnection):
   class DeploymentConnectionArgs(GQLArgsSet, GQLObject):
      environments: list[NonNull_str]
      orderBy: DeploymentOrder
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentConnectionArgs



class OHLIQ_TreeEntry_Field(TreeEntry):
   class TreeEntryArgs(GQLArgsSet, GQLObject):
      path: NonNull_str

   _args: TreeEntryArgs



class ARYWN_CommitHistoryConnection_Field(CommitHistoryConnection):
   class CommitHistoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      path: str
      author: CommitAuthor
      since: GitTimestamp
      until: GitTimestamp

   _args: CommitHistoryConnectionArgs



class BUGMG_CommitConnection_Field(CommitConnection):
   class CommitConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitConnectionArgs



class GJNXC_SubmoduleConnection_Field(SubmoduleConnection):
   class SubmoduleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: SubmoduleConnectionArgs



class Commit(GQLObject):
   abbreviatedOid: str
   additions: int
   associatedPullRequests: IPEON_PullRequestConnection_Field
   author: GitActor
   authoredByCommitter: bool
   authoredDate: DateTime
   authors: UGQDX_GitActorConnection_Field
   blame: ALALR_Blame_Field
   changedFilesIfAvailable: int
   checkSuites: NSWTW_CheckSuiteConnection_Field
   comments: CAURM_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
   commitResourcePath: URI
   commitUrl: URI
   committedDate: DateTime
   committedViaWeb: bool
   committer: GitActor
   deletions: int
   deployments: IVYVG_DeploymentConnection_Field
   file: OHLIQ_TreeEntry_Field
   history: ARYWN_CommitHistoryConnection_Field
   id: ID
   message: str
   messageBody: str
   messageBodyHTML: HTML
   messageHeadline: str
   messageHeadlineHTML: HTML
   oid: GitObjectID
   onBehalfOf: NewType('Organization', GQLObject) ## Circular Reference for Organization
   parents: BUGMG_CommitConnection_Field
   repository: Repository
   resourcePath: URI
   signature: GitSignature
   status: Status
   statusCheckRollup: StatusCheckRollup
   submodules: GJNXC_SubmoduleConnection_Field
   tarballUrl: URI
   tree: Tree
   treeResourcePath: URI
   treeUrl: URI
   url: URI
   viewerCanSubscribe: bool
   viewerSubscription: SubscriptionState
   zipballUrl: URI

class QYXRA_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class GRFJK_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class CommitComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyText: str
   commit: Commit
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   isMinimized: bool
   lastEditedAt: DateTime
   minimizedReason: str
   path: str
   position: int
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: QYXRA_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   updatedAt: DateTime
   url: URI
   userContentEdits: GRFJK_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanMinimize: bool
   viewerCanReact: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]
   viewerDidAuthor: bool

class CommitCommentEdge(GQLObject):
   cursor: str
   node: CommitComment

class list_CommitCommentEdge(list, CommitCommentEdge): pass

class list_CommitComment(list, CommitComment): pass

class CommitCommentConnection(GQLObject):
   edges: list_CommitCommentEdge[CommitCommentEdge]
   nodes: list_CommitComment[CommitComment]
   pageInfo: PageInfo
   totalCount: int

class CreatedCommitContribution(GQLObject):
   commitCount: int
   isRestricted: bool
   occurredAt: DateTime
   repository: Repository
   resourcePath: URI
   url: URI
   user: NewType('User', GQLObject) ## Circular Reference for User

class CreatedCommitContributionEdge(GQLObject):
   cursor: str
   node: CreatedCommitContribution

class list_CreatedCommitContributionEdge(list, CreatedCommitContributionEdge): pass

class list_CreatedCommitContribution(list, CreatedCommitContribution): pass

class CreatedCommitContributionConnection(GQLObject):
   edges: list_CreatedCommitContributionEdge[CreatedCommitContributionEdge]
   nodes: list_CreatedCommitContribution[CreatedCommitContribution]
   pageInfo: PageInfo
   totalCount: int

class YMBWU_CreatedCommitContributionConnection_Field(CreatedCommitContributionConnection):
   class CreatedCommitContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: CommitContributionOrder

   _args: CreatedCommitContributionConnectionArgs



class CommitContributionsByRepository(GQLObject):
   contributions: YMBWU_CreatedCommitContributionConnection_Field
   repository: Repository
   resourcePath: URI
   url: URI

class list_ContributionCalendarDay(list, ContributionCalendarDay): pass

class ContributionCalendarWeek(GQLObject):
   contributionDays: list_ContributionCalendarDay[ContributionCalendarDay]
   firstDay: Date

class list_ContributionCalendarMonth(list, ContributionCalendarMonth): pass

class list_ContributionCalendarWeek(list, ContributionCalendarWeek): pass

class ContributionCalendar(GQLObject):
   colors: list[str]
   isHalloween: bool
   months: list_ContributionCalendarMonth[ContributionCalendarMonth]
   totalContributions: int
   weeks: list_ContributionCalendarWeek[ContributionCalendarWeek]

class CreatedIssueContribution(GQLObject):
   isRestricted: bool
   issue: Issue
   occurredAt: DateTime
   resourcePath: URI
   url: URI
   user: NewType('User', GQLObject) ## Circular Reference for User

class RestrictedContribution(GQLObject):
   isRestricted: bool
   occurredAt: DateTime
   resourcePath: URI
   url: URI
   user: NewType('User', GQLObject) ## Circular Reference for User

class CreatedIssueOrRestrictedContribution(GQLObject): 
   pass

class CreatedPullRequestContribution(GQLObject):
   isRestricted: bool
   occurredAt: DateTime
   pullRequest: PullRequest
   resourcePath: URI
   url: URI
   user: NewType('User', GQLObject) ## Circular Reference for User

class CreatedPullRequestOrRestrictedContribution(GQLObject): 
   pass

class CreatedRepositoryContribution(GQLObject):
   isRestricted: bool
   occurredAt: DateTime
   repository: Repository
   resourcePath: URI
   url: URI
   user: NewType('User', GQLObject) ## Circular Reference for User

class CreatedRepositoryOrRestrictedContribution(GQLObject): 
   pass

class CreatedIssueContributionEdge(GQLObject):
   cursor: str
   node: CreatedIssueContribution

class list_CreatedIssueContributionEdge(list, CreatedIssueContributionEdge): pass

class list_CreatedIssueContribution(list, CreatedIssueContribution): pass

class CreatedIssueContributionConnection(GQLObject):
   edges: list_CreatedIssueContributionEdge[CreatedIssueContributionEdge]
   nodes: list_CreatedIssueContribution[CreatedIssueContribution]
   pageInfo: PageInfo
   totalCount: int

class MFXMM_CreatedIssueContributionConnection_Field(CreatedIssueContributionConnection):
   class CreatedIssueContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedIssueContributionConnectionArgs



class IssueContributionsByRepository(GQLObject):
   contributions: MFXMM_CreatedIssueContributionConnection_Field
   repository: Repository

class JoinedGitHubContribution(GQLObject):
   isRestricted: bool
   occurredAt: DateTime
   resourcePath: URI
   url: URI
   user: NewType('User', GQLObject) ## Circular Reference for User

class CreatedPullRequestContributionEdge(GQLObject):
   cursor: str
   node: CreatedPullRequestContribution

class list_CreatedPullRequestContributionEdge(list, CreatedPullRequestContributionEdge): pass

class list_CreatedPullRequestContribution(list, CreatedPullRequestContribution): pass

class CreatedPullRequestContributionConnection(GQLObject):
   edges: list_CreatedPullRequestContributionEdge[CreatedPullRequestContributionEdge]
   nodes: list_CreatedPullRequestContribution[CreatedPullRequestContribution]
   pageInfo: PageInfo
   totalCount: int

class JSAHL_CreatedPullRequestContributionConnection_Field(CreatedPullRequestContributionConnection):
   class CreatedPullRequestContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestContributionConnectionArgs



class PullRequestContributionsByRepository(GQLObject):
   contributions: JSAHL_CreatedPullRequestContributionConnection_Field
   repository: Repository

class CreatedPullRequestReviewContribution(GQLObject):
   isRestricted: bool
   occurredAt: DateTime
   pullRequest: PullRequest
   pullRequestReview: PullRequestReview
   repository: Repository
   resourcePath: URI
   url: URI
   user: NewType('User', GQLObject) ## Circular Reference for User

class CreatedPullRequestReviewContributionEdge(GQLObject):
   cursor: str
   node: CreatedPullRequestReviewContribution

class list_CreatedPullRequestReviewContributionEdge(list, CreatedPullRequestReviewContributionEdge): pass

class list_CreatedPullRequestReviewContribution(list, CreatedPullRequestReviewContribution): pass

class CreatedPullRequestReviewContributionConnection(GQLObject):
   edges: list_CreatedPullRequestReviewContributionEdge[CreatedPullRequestReviewContributionEdge]
   nodes: list_CreatedPullRequestReviewContribution[CreatedPullRequestReviewContribution]
   pageInfo: PageInfo
   totalCount: int

class EEBRB_CreatedPullRequestReviewContributionConnection_Field(CreatedPullRequestReviewContributionConnection):
   class CreatedPullRequestReviewContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestReviewContributionConnectionArgs



class PullRequestReviewContributionsByRepository(GQLObject):
   contributions: EEBRB_CreatedPullRequestReviewContributionConnection_Field
   repository: Repository

class CreatedRepositoryContributionEdge(GQLObject):
   cursor: str
   node: CreatedRepositoryContribution

class list_CreatedRepositoryContributionEdge(list, CreatedRepositoryContributionEdge): pass

class list_CreatedRepositoryContribution(list, CreatedRepositoryContribution): pass

class CreatedRepositoryContributionConnection(GQLObject):
   edges: list_CreatedRepositoryContributionEdge[CreatedRepositoryContributionEdge]
   nodes: list_CreatedRepositoryContribution[CreatedRepositoryContribution]
   pageInfo: PageInfo
   totalCount: int

class RPLHK_CommitContributionsByRepository_Field(CommitContributionsByRepository):
   class CommitContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int

   _args: CommitContributionsByRepositoryArgs



class list_CommitContributionsByRepository(list, CommitContributionsByRepository): pass

class ILATG_CreatedIssueContributionConnection_Field(CreatedIssueContributionConnection):
   class CreatedIssueContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      excludePopular: bool
      orderBy: ContributionOrder

   _args: CreatedIssueContributionConnectionArgs



class FGBQD_IssueContributionsByRepository_Field(IssueContributionsByRepository):
   class IssueContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int
      excludeFirst: bool
      excludePopular: bool

   _args: IssueContributionsByRepositoryArgs



class list_IssueContributionsByRepository(list, IssueContributionsByRepository): pass

class MNQTV_CreatedPullRequestContributionConnection_Field(CreatedPullRequestContributionConnection):
   class CreatedPullRequestContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      excludePopular: bool
      orderBy: ContributionOrder

   _args: CreatedPullRequestContributionConnectionArgs



class DFTAG_PullRequestContributionsByRepository_Field(PullRequestContributionsByRepository):
   class PullRequestContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int
      excludeFirst: bool
      excludePopular: bool

   _args: PullRequestContributionsByRepositoryArgs



class list_PullRequestContributionsByRepository(list, PullRequestContributionsByRepository): pass

class LDLJX_CreatedPullRequestReviewContributionConnection_Field(CreatedPullRequestReviewContributionConnection):
   class CreatedPullRequestReviewContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestReviewContributionConnectionArgs



class MPHPI_PullRequestReviewContributionsByRepository_Field(PullRequestReviewContributionsByRepository):
   class PullRequestReviewContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int

   _args: PullRequestReviewContributionsByRepositoryArgs



class list_PullRequestReviewContributionsByRepository(list, PullRequestReviewContributionsByRepository): pass

class LOIHZ_CreatedRepositoryContributionConnection_Field(CreatedRepositoryContributionConnection):
   class CreatedRepositoryContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      orderBy: ContributionOrder

   _args: CreatedRepositoryContributionConnectionArgs



class ContributionsCollection(GQLObject):
   commitContributionsByRepository: RPLHK_CommitContributionsByRepository_Field
   contributionCalendar: ContributionCalendar
   contributionYears: list[int]
   doesEndInCurrentMonth: bool
   earliestRestrictedContributionDate: Date
   endedAt: DateTime
   firstIssueContribution: CreatedIssueOrRestrictedContribution
   firstPullRequestContribution: CreatedPullRequestOrRestrictedContribution
   firstRepositoryContribution: CreatedRepositoryOrRestrictedContribution
   hasActivityInThePast: bool
   hasAnyContributions: bool
   hasAnyRestrictedContributions: bool
   isSingleDay: bool
   issueContributions: ILATG_CreatedIssueContributionConnection_Field
   issueContributionsByRepository: FGBQD_IssueContributionsByRepository_Field
   joinedGitHubContribution: JoinedGitHubContribution
   latestRestrictedContributionDate: Date
   mostRecentCollectionWithActivity: NewType('ContributionsCollection', GQLObject) ## Circular Reference for ContributionsCollection
   mostRecentCollectionWithoutActivity: NewType('ContributionsCollection', GQLObject) ## Circular Reference for ContributionsCollection
   popularIssueContribution: CreatedIssueContribution
   popularPullRequestContribution: CreatedPullRequestContribution
   pullRequestContributions: MNQTV_CreatedPullRequestContributionConnection_Field
   pullRequestContributionsByRepository: DFTAG_PullRequestContributionsByRepository_Field
   pullRequestReviewContributions: LDLJX_CreatedPullRequestReviewContributionConnection_Field
   pullRequestReviewContributionsByRepository: MPHPI_PullRequestReviewContributionsByRepository_Field
   repositoryContributions: LOIHZ_CreatedRepositoryContributionConnection_Field
   restrictedContributionsCount: int
   startedAt: DateTime
   totalCommitContributions: int
   totalIssueContributions: QDXTZ_totalIssueContributions_Field
   totalPullRequestContributions: SCDZL_totalPullRequestContributions_Field
   totalPullRequestReviewContributions: int
   totalRepositoriesWithContributedCommits: int
   totalRepositoriesWithContributedIssues: RLDGW_totalRepositoriesWithContributedIssues_Field
   totalRepositoriesWithContributedPullRequestReviews: int
   totalRepositoriesWithContributedPullRequests: CSZXV_totalRepositoriesWithContributedPullRequests_Field
   totalRepositoryContributions: DAXNX_totalRepositoryContributions_Field
   user: NewType('User', GQLObject) ## Circular Reference for User

class FollowerConnection(GQLObject):
   edges: list_UserEdge[UserEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for User
   pageInfo: PageInfo
   totalCount: int

class FollowingConnection(GQLObject):
   edges: list_UserEdge[UserEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for User
   pageInfo: PageInfo
   totalCount: int

class WGJLB_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class GistComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyText: str
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   gist: NewType('Gist', GQLObject) ## Circular Reference for Gist
   id: ID
   includesCreatedEdit: bool
   isMinimized: bool
   lastEditedAt: DateTime
   minimizedReason: str
   publishedAt: DateTime
   updatedAt: DateTime
   userContentEdits: WGJLB_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanMinimize: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: list[CommentCannotUpdateReason]
   viewerDidAuthor: bool

class GistCommentEdge(GQLObject):
   cursor: str
   node: GistComment

class list_GistCommentEdge(list, GistCommentEdge): pass

class list_GistComment(list, GistComment): pass

class GistCommentConnection(GQLObject):
   edges: list_GistCommentEdge[GistCommentEdge]
   nodes: list_GistComment[GistComment]
   pageInfo: PageInfo
   totalCount: int

class GistFile(GQLObject):
   encodedName: str
   encoding: str
   extension: str
   isImage: bool
   isTruncated: bool
   language: Language
   name: str
   size: int
   text: ZBXCL_text_Field

class GistEdge(GQLObject):
   cursor: str
   node: NewType('Gist', GQLObject) ## Circular Reference for Gist

class list_GistEdge(list, GistEdge): pass

class GistConnection(GQLObject):
   edges: list_GistEdge[GistEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Gist
   pageInfo: PageInfo
   totalCount: int

class LOEAM_GistCommentConnection_Field(GistCommentConnection):
   class GistCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: GistCommentConnectionArgs



class ZXKQP_GistFile_Field(GistFile):
   class GistFileArgs(GQLArgsSet, GQLObject):
      limit: int
      oid: GitObjectID

   _args: GistFileArgs



class list_GistFile(list, GistFile): pass

class RGWWW_GistConnection_Field(GistConnection):
   class GistConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: GistOrder

   _args: GistConnectionArgs



class FQIBJ_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class Gist(GQLObject):
   comments: LOEAM_GistCommentConnection_Field
   createdAt: DateTime
   description: str
   files: ZXKQP_GistFile_Field
   forks: RGWWW_GistConnection_Field
   id: ID
   isFork: bool
   isPublic: bool
   name: str
   owner: RepositoryOwner
   pushedAt: DateTime
   resourcePath: URI
   stargazerCount: int
   stargazers: FQIBJ_StargazerConnection_Field
   updatedAt: DateTime
   url: URI
   viewerHasStarred: bool

class PinnableItem(GQLObject): 
   pass

class PinnableItemEdge(GQLObject):
   cursor: str
   node: PinnableItem

class list_PinnableItemEdge(list, PinnableItemEdge): pass

class list_PinnableItem(list, PinnableItem): pass

class PinnableItemConnection(GQLObject):
   edges: list_PinnableItemEdge[PinnableItemEdge]
   nodes: list_PinnableItem[PinnableItem]
   pageInfo: PageInfo
   totalCount: int

class ZIWNG_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class ProfileItemShowcase(GQLObject):
   hasPinnedItems: bool
   items: ZIWNG_PinnableItemConnection_Field

class OrganizationEdge(GQLObject):
   cursor: str
   node: NewType('Organization', GQLObject) ## Circular Reference for Organization

class list_OrganizationEdge(list, OrganizationEdge): pass

class OrganizationConnection(GQLObject):
   edges: list_OrganizationEdge[OrganizationEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Organization
   pageInfo: PageInfo
   totalCount: int

class PublicKeyEdge(GQLObject):
   cursor: str
   node: PublicKey

class list_PublicKeyEdge(list, PublicKeyEdge): pass

class list_PublicKey(list, PublicKey): pass

class PublicKeyConnection(GQLObject):
   edges: list_PublicKeyEdge[PublicKeyEdge]
   nodes: list_PublicKey[PublicKey]
   pageInfo: PageInfo
   totalCount: int

class SavedReply(GQLObject):
   body: str
   bodyHTML: HTML
   databaseId: int
   id: ID
   title: str
   user: Actor

class SavedReplyEdge(GQLObject):
   cursor: str
   node: SavedReply

class list_SavedReplyEdge(list, SavedReplyEdge): pass

class list_SavedReply(list, SavedReply): pass

class SavedReplyConnection(GQLObject):
   edges: list_SavedReplyEdge[SavedReplyEdge]
   nodes: list_SavedReply[SavedReply]
   pageInfo: PageInfo
   totalCount: int

class SocialAccountEdge(GQLObject):
   cursor: str
   node: SocialAccount

class list_SocialAccountEdge(list, SocialAccountEdge): pass

class list_SocialAccount(list, SocialAccount): pass

class SocialAccountConnection(GQLObject):
   edges: list_SocialAccountEdge[SocialAccountEdge]
   nodes: list_SocialAccount[SocialAccount]
   pageInfo: PageInfo
   totalCount: int

class Sponsor(GQLObject): 
   pass

class SponsorEdge(GQLObject):
   cursor: str
   node: Sponsor

class list_SponsorEdge(list, SponsorEdge): pass

class list_Sponsor(list, Sponsor): pass

class SponsorConnection(GQLObject):
   edges: list_SponsorEdge[SponsorEdge]
   nodes: list_Sponsor[Sponsor]
   pageInfo: PageInfo
   totalCount: int

class StripeConnectAccount(GQLObject):
   accountId: str
   billingCountryOrRegion: str
   countryOrRegion: str
   isActive: bool
   sponsorsListing: NewType('SponsorsListing', GQLObject) ## Circular Reference for SponsorsListing
   stripeDashboardUrl: URI

class SponsorsListingFeatureableItem(GQLObject): 
   pass

class SponsorsListingFeaturedItem(GQLObject):
   createdAt: DateTime
   description: str
   featureable: SponsorsListingFeatureableItem
   id: ID
   position: int
   sponsorsListing: NewType('SponsorsListing', GQLObject) ## Circular Reference for SponsorsListing
   updatedAt: DateTime

class SponsorsTierEdge(GQLObject):
   cursor: str
   node: NewType('SponsorsTier', GQLObject) ## Circular Reference for SponsorsTier

class list_SponsorsTierEdge(list, SponsorsTierEdge): pass

class SponsorsTierConnection(GQLObject):
   edges: list_SponsorsTierEdge[SponsorsTierEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for SponsorsTier
   pageInfo: PageInfo
   totalCount: int

class NonNull_SponsorsListingFeaturedItemFeatureableType(GQLObject): pass

class IIQDT_SponsorsListingFeaturedItem_Field(SponsorsListingFeaturedItem):
   class SponsorsListingFeaturedItemArgs(GQLArgsSet, GQLObject):
      featureableTypes: list[NonNull_SponsorsListingFeaturedItemFeatureableType]

   _args: SponsorsListingFeaturedItemArgs



class list_SponsorsListingFeaturedItem(list, SponsorsListingFeaturedItem): pass

class ETOJK_SponsorsTierConnection_Field(SponsorsTierConnection):
   class SponsorsTierConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorsTierOrder
      includeUnpublished: bool

   _args: SponsorsTierConnectionArgs



class SponsorsListing(GQLObject):
   activeGoal: SponsorsGoal
   activeStripeConnectAccount: StripeConnectAccount
   billingCountryOrRegion: str
   contactEmailAddress: str
   createdAt: DateTime
   dashboardResourcePath: URI
   dashboardUrl: URI
   featuredItems: IIQDT_SponsorsListingFeaturedItem_Field
   fiscalHost: NewType('Organization', GQLObject) ## Circular Reference for Organization
   fullDescription: str
   fullDescriptionHTML: HTML
   id: ID
   isPublic: bool
   name: str
   nextPayoutDate: Date
   residenceCountryOrRegion: str
   resourcePath: URI
   shortDescription: str
   slug: str
   sponsorable: NewType('Sponsorable', GQLObject) ## Circular Reference for Sponsorable
   tiers: ETOJK_SponsorsTierConnection_Field
   url: URI

class SponsorshipNewsletter(GQLObject):
   author: NewType('User', GQLObject) ## Circular Reference for User
   body: str
   createdAt: DateTime
   id: ID
   isPublished: bool
   sponsorable: NewType('Sponsorable', GQLObject) ## Circular Reference for Sponsorable
   subject: str
   updatedAt: DateTime

class SponsorshipNewsletterEdge(GQLObject):
   cursor: str
   node: SponsorshipNewsletter

class list_SponsorshipNewsletterEdge(list, SponsorshipNewsletterEdge): pass

class list_SponsorshipNewsletter(list, SponsorshipNewsletter): pass

class SponsorshipNewsletterConnection(GQLObject):
   edges: list_SponsorshipNewsletterEdge[SponsorshipNewsletterEdge]
   nodes: list_SponsorshipNewsletter[SponsorshipNewsletter]
   pageInfo: PageInfo
   totalCount: int

class TCFPU_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class PTMFD_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class NonNull_SponsorsActivityAction(GQLObject): pass

class CTJOX_SponsorsActivityConnection_Field(Generic[SponsorsActivityConnection]):
   class SponsorsActivityConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      period: SponsorsActivityPeriod
      since: DateTime
      until: DateTime
      orderBy: SponsorsActivityOrder
      actions: list[NonNull_SponsorsActivityAction]
      includeAsSponsor: bool

   _args: SponsorsActivityConnectionArgs



class NLRYY_Sponsorship_Field(Generic[Sponsorship]):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class AEXPY_Sponsorship_Field(Generic[Sponsorship]):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class CRBTZ_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class DCXZV_SponsorshipConnection_Field(Generic[SponsorshipConnection]):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class JRELZ_SponsorshipConnection_Field(Generic[SponsorshipConnection]):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipOrder
      maintainerLogins: list[NonNull_str]
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class Sponsorable(GQLObject):
   estimatedNextSponsorsPayoutInCents: int
   hasSponsorsListing: bool
   isSponsoredBy: KJKSS_isSponsoredBy_Field
   isSponsoringViewer: bool
   monthlyEstimatedSponsorsIncomeInCents: int
   sponsoring: TCFPU_SponsorConnection_Field
   sponsors: PTMFD_SponsorConnection_Field
   sponsorsActivities: CTJOX_SponsorsActivityConnection_Field ## Circular Reference for SponsorsActivityConnection
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: NLRYY_Sponsorship_Field ## Circular Reference for Sponsorship
   sponsorshipForViewerAsSponsorable: AEXPY_Sponsorship_Field ## Circular Reference for Sponsorship
   sponsorshipNewsletters: CRBTZ_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: DCXZV_SponsorshipConnection_Field ## Circular Reference for SponsorshipConnection
   sponsorshipsAsSponsor: JRELZ_SponsorshipConnection_Field ## Circular Reference for SponsorshipConnection
   totalSponsorshipAmountAsSponsorInCents: AVBAQ_totalSponsorshipAmountAsSponsorInCents_Field
   viewerCanSponsor: bool
   viewerIsSponsoring: bool

class Sponsorship(GQLObject):
   createdAt: DateTime
   id: ID
   isActive: bool
   isOneTimePayment: bool
   isSponsorOptedIntoEmail: bool
   privacyLevel: SponsorshipPrivacy
   sponsorEntity: Sponsor
   sponsorable: Sponsorable
   tier: NewType('SponsorsTier', GQLObject) ## Circular Reference for SponsorsTier
   tierSelectedAt: DateTime

class SponsorshipEdge(GQLObject):
   cursor: str
   node: Sponsorship

class list_SponsorshipEdge(list, SponsorshipEdge): pass

class list_Sponsorship(list, Sponsorship): pass

class SponsorshipConnection(GQLObject):
   edges: list_SponsorshipEdge[SponsorshipEdge]
   nodes: list_Sponsorship[Sponsorship]
   pageInfo: PageInfo
   totalCount: int
   totalRecurringMonthlyPriceInCents: int
   totalRecurringMonthlyPriceInDollars: int

class TNATS_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder

   _args: SponsorshipConnectionArgs



class SponsorsTierAdminInfo(GQLObject):
   isDraft: bool
   isPublished: bool
   isRetired: bool
   sponsorships: TNATS_SponsorshipConnection_Field

class SponsorsTier(GQLObject):
   adminInfo: SponsorsTierAdminInfo
   closestLesserValueTier: NewType('SponsorsTier', GQLObject) ## Circular Reference for SponsorsTier
   createdAt: DateTime
   description: str
   descriptionHTML: HTML
   id: ID
   isCustomAmount: bool
   isOneTime: bool
   monthlyPriceInCents: int
   monthlyPriceInDollars: int
   name: str
   sponsorsListing: SponsorsListing
   updatedAt: DateTime

class SponsorsActivity(GQLObject):
   action: SponsorsActivityAction
   id: ID
   previousSponsorsTier: SponsorsTier
   sponsor: Sponsor
   sponsorable: Sponsorable
   sponsorsTier: SponsorsTier
   timestamp: DateTime
   viaBulkSponsorship: bool

class SponsorsActivityEdge(GQLObject):
   cursor: str
   node: SponsorsActivity

class list_SponsorsActivityEdge(list, SponsorsActivityEdge): pass

class list_SponsorsActivity(list, SponsorsActivity): pass

class SponsorsActivityConnection(GQLObject):
   edges: list_SponsorsActivityEdge[SponsorsActivityEdge]
   nodes: list_SponsorsActivity[SponsorsActivity]
   pageInfo: PageInfo
   totalCount: int

class StarredRepositoryEdge(GQLObject):
   cursor: str
   node: Repository
   starredAt: DateTime

class list_StarredRepositoryEdge(list, StarredRepositoryEdge): pass

class StarredRepositoryConnection(GQLObject):
   edges: list_StarredRepositoryEdge[StarredRepositoryEdge]
   isOverLimit: bool
   nodes: list_Repository[Repository]
   pageInfo: PageInfo
   totalCount: int

class SOETF_CommitCommentConnection_Field(CommitCommentConnection):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class QUUWL_ContributionsCollection_Field(ContributionsCollection):
   class ContributionsCollectionArgs(GQLArgsSet, GQLObject):
      organizationID: ID
      from_: DateTime
      to: DateTime

   _args: ContributionsCollectionArgs



class OPPUW_FollowerConnection_Field(FollowerConnection):
   class FollowerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: FollowerConnectionArgs



class AHMXO_FollowingConnection_Field(FollowingConnection):
   class FollowingConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: FollowingConnectionArgs



class HDSOZ_Gist_Field(Gist):
   class GistArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: GistArgs



class MQUMH_GistCommentConnection_Field(GistCommentConnection):
   class GistCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: GistCommentConnectionArgs



class CZUVL_GistConnection_Field(GistConnection):
   class GistConnectionArgs(GQLArgsSet, GQLObject):
      privacy: GistPrivacy
      orderBy: GistOrder
      after: str
      before: str
      first: int
      last: int

   _args: GistConnectionArgs



class BFMAV_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject):
      primarySubjectId: ID

   _args: HovercardArgs



class NJSXG_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class BKQPI_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueOrder
      labels: list[NonNull_str]
      states: list[NonNull_IssueState]
      filterBy: IssueFilters
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class GKPOH_Organization_Field(Generic[Organization]):
   class OrganizationArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: OrganizationArgs



class VVSFO_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: OrganizationOrder
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class DXPPU_PackageConnection_Field(PackageConnection):
   class PackageConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      names: list[str]
      repositoryId: ID
      packageType: PackageType
      orderBy: PackageOrder

   _args: PackageConnectionArgs



class NonNull_PinnableItemType(GQLObject): pass

class QLXLH_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class RKDYT_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class BNXAX_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class ZNDMO_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class BLEGS_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: ProjectOrder
      search: str
      states: list[NonNull_ProjectState]
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class RLUHW_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class TCVCS_PublicKeyConnection_Field(PublicKeyConnection):
   class PublicKeyConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PublicKeyConnectionArgs



class GWTZF_PullRequestConnection_Field(PullRequestConnection):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      states: list[NonNull_PullRequestState]
      labels: list[NonNull_str]
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class UTDVA_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class VEKCZ_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: list[RepositoryAffiliation]
      ownerAffiliations: list[RepositoryAffiliation]
      isLocked: bool
      after: str
      before: str
      first: int
      last: int
      isFork: bool

   _args: RepositoryConnectionArgs



class RTDPU_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      isLocked: bool
      includeUserRepositories: bool
      contributionTypes: list[RepositoryContributionType]
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryConnectionArgs



class JFTXY_Repository_Field(Repository):
   class RepositoryArgs(GQLArgsSet, GQLObject):
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs



class PYTJE_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class ZSVLQ_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionOrder
      repositoryId: ID
      answered: bool
      states: list[NonNull_DiscussionState]

   _args: DiscussionConnectionArgs



class QHNOI_SavedReplyConnection_Field(SavedReplyConnection):
   class SavedReplyConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SavedReplyOrder

   _args: SavedReplyConnectionArgs



class UDDGB_SocialAccountConnection_Field(SocialAccountConnection):
   class SocialAccountConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: SocialAccountConnectionArgs



class NJJUA_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class IMAFU_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class ZVAKZ_SponsorsActivityConnection_Field(SponsorsActivityConnection):
   class SponsorsActivityConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      period: SponsorsActivityPeriod
      since: DateTime
      until: DateTime
      orderBy: SponsorsActivityOrder
      actions: list[NonNull_SponsorsActivityAction]
      includeAsSponsor: bool

   _args: SponsorsActivityConnectionArgs



class PJLBO_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class VJYVQ_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class NLXGU_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class KNMDN_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class PRDHS_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipOrder
      maintainerLogins: list[NonNull_str]
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class ASQXD_StarredRepositoryConnection_Field(StarredRepositoryConnection):
   class StarredRepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      ownedByViewer: bool
      orderBy: StarOrder

   _args: StarredRepositoryConnectionArgs



class NonNull_RepositoryOrder(RepositoryOrder): pass

class ERLIM_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: NonNull_RepositoryOrder
      since: DateTime

   _args: RepositoryConnectionArgs



class ZRJXJ_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: list[RepositoryAffiliation]
      ownerAffiliations: list[RepositoryAffiliation]
      isLocked: bool
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryConnectionArgs



class User(GQLObject):
   anyPinnableItems: HFWZO_anyPinnableItems_Field
   avatarUrl: KCOBC_URI_Field
   bio: str
   bioHTML: HTML
   canReceiveOrganizationEmailsWhenNotificationsRestricted: TRPGF_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field
   commitComments: SOETF_CommitCommentConnection_Field
   company: str
   companyHTML: HTML
   contributionsCollection: QUUWL_ContributionsCollection_Field
   createdAt: DateTime
   databaseId: int
   email: str
   estimatedNextSponsorsPayoutInCents: int
   followers: OPPUW_FollowerConnection_Field
   following: AHMXO_FollowingConnection_Field
   gist: HDSOZ_Gist_Field
   gistComments: MQUMH_GistCommentConnection_Field
   gists: CZUVL_GistConnection_Field
   hasSponsorsListing: bool
   hovercard: BFMAV_Hovercard_Field
   id: ID
   interactionAbility: RepositoryInteractionAbility
   isBountyHunter: bool
   isCampusExpert: bool
   isDeveloperProgramMember: bool
   isEmployee: bool
   isFollowingViewer: bool
   isGitHubStar: bool
   isHireable: bool
   isSiteAdmin: bool
   isSponsoredBy: QDFYO_isSponsoredBy_Field
   isSponsoringViewer: bool
   isViewer: bool
   issueComments: NJSXG_IssueCommentConnection_Field
   issues: BKQPI_IssueConnection_Field
   itemShowcase: ProfileItemShowcase
   location: str
   login: str
   monthlyEstimatedSponsorsIncomeInCents: int
   name: str
   organization: GKPOH_Organization_Field ## Circular Reference for Organization
   organizationVerifiedDomainEmails: ACXCR_organizationVerifiedDomainEmails_Field
   organizations: VVSFO_OrganizationConnection_Field
   packages: DXPPU_PackageConnection_Field
   pinnableItems: QLXLH_PinnableItemConnection_Field
   pinnedItems: RKDYT_PinnableItemConnection_Field
   pinnedItemsRemaining: int
   project: BNXAX_Project_Field
   projectV2: ZNDMO_ProjectV2_Field
   projects: BLEGS_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   projectsV2: RLUHW_ProjectV2Connection_Field
   pronouns: str
   publicKeys: TCVCS_PublicKeyConnection_Field
   pullRequests: GWTZF_PullRequestConnection_Field
   recentProjects: UTDVA_ProjectV2Connection_Field
   repositories: VEKCZ_RepositoryConnection_Field
   repositoriesContributedTo: RTDPU_RepositoryConnection_Field
   repository: JFTXY_Repository_Field
   repositoryDiscussionComments: PYTJE_DiscussionCommentConnection_Field
   repositoryDiscussions: ZSVLQ_DiscussionConnection_Field
   resourcePath: URI
   savedReplies: QHNOI_SavedReplyConnection_Field
   socialAccounts: UDDGB_SocialAccountConnection_Field
   sponsoring: NJJUA_SponsorConnection_Field
   sponsors: IMAFU_SponsorConnection_Field
   sponsorsActivities: ZVAKZ_SponsorsActivityConnection_Field
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: PJLBO_Sponsorship_Field
   sponsorshipForViewerAsSponsorable: VJYVQ_Sponsorship_Field
   sponsorshipNewsletters: NLXGU_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: KNMDN_SponsorshipConnection_Field
   sponsorshipsAsSponsor: PRDHS_SponsorshipConnection_Field
   starredRepositories: ASQXD_StarredRepositoryConnection_Field
   status: UserStatus
   topRepositories: ERLIM_RepositoryConnection_Field
   totalSponsorshipAmountAsSponsorInCents: XRZWP_totalSponsorshipAmountAsSponsorInCents_Field
   twitterUsername: str
   updatedAt: DateTime
   url: URI
   viewerCanChangePinnedItems: bool
   viewerCanCreateProjects: bool
   viewerCanFollow: bool
   viewerCanSponsor: bool
   viewerIsFollowing: bool
   viewerIsSponsoring: bool
   watching: ZRJXJ_RepositoryConnection_Field
   websiteUrl: URI

class AuditEntryActor(GQLObject): 
   pass

class MembersCanDeleteReposClearAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class MembersCanDeleteReposDisableAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class MembersCanDeleteReposEnableAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OauthApplicationCreateAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   applicationUrl: URI
   callbackUrl: URI
   createdAt: PreciseDateTime
   id: ID
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   rateLimit: int
   state: OauthApplicationCreateAuditEntryState
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgAddBillingManagerAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   invitationEmail: str
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgAddMemberAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   permission: OrgAddMemberAuditEntryPermission
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgBlockUserAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   blockedUser: User
   blockedUserName: str
   blockedUserResourcePath: URI
   blockedUserUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgConfigDisableCollaboratorsOnlyAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgConfigEnableCollaboratorsOnlyAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgCreateAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   billingPlan: OrgCreateAuditEntryBillingPlan
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgDisableOauthAppRestrictionsAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgDisableSamlAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   digestMethodUrl: URI
   id: ID
   issuerUrl: URI
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   signatureMethodUrl: URI
   singleSignOnUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgDisableTwoFactorRequirementAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgEnableOauthAppRestrictionsAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgEnableSamlAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   digestMethodUrl: URI
   id: ID
   issuerUrl: URI
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   signatureMethodUrl: URI
   singleSignOnUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgEnableTwoFactorRequirementAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgInviteMemberAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   email: str
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationInvitation: OrganizationInvitation
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgInviteToBusinessAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgOauthAppAccessApprovedAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgOauthAppAccessBlockedAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgOauthAppAccessDeniedAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgOauthAppAccessRequestedAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgOauthAppAccessUnblockedAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgRemoveBillingManagerAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   reason: OrgRemoveBillingManagerAuditEntryReason
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgRemoveMemberAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   membershipTypes: list[OrgRemoveMemberAuditEntryMembershipType]
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   reason: OrgRemoveMemberAuditEntryReason
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgRemoveOutsideCollaboratorAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   membershipTypes: list[OrgRemoveOutsideCollaboratorAuditEntryMembershipType]
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   reason: OrgRemoveOutsideCollaboratorAuditEntryReason
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgRestoreMemberMembershipOrganizationAuditEntryData(GQLObject):
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI

class OrgRestoreMemberMembershipRepositoryAuditEntryData(GQLObject):
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI

class OrgRestoreMemberMembershipTeamAuditEntryData(GQLObject):
   team: Team
   teamName: str
   teamResourcePath: URI
   teamUrl: URI

class OrgRestoreMemberAuditEntryMembership(GQLObject): 
   pass

class list_OrgRestoreMemberAuditEntryMembership(list, OrgRestoreMemberAuditEntryMembership): pass

class OrgRestoreMemberAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   restoredCustomEmailRoutingsCount: int
   restoredIssueAssignmentsCount: int
   restoredMemberships: list_OrgRestoreMemberAuditEntryMembership[OrgRestoreMemberAuditEntryMembership]
   restoredMembershipsCount: int
   restoredRepositoriesCount: int
   restoredRepositoryStarsCount: int
   restoredRepositoryWatchesCount: int
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgUnblockUserAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   blockedUser: User
   blockedUserName: str
   blockedUserResourcePath: URI
   blockedUserUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgUpdateDefaultRepositoryPermissionAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   permission: OrgUpdateDefaultRepositoryPermissionAuditEntryPermission
   permissionWas: OrgUpdateDefaultRepositoryPermissionAuditEntryPermission
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgUpdateMemberAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   permission: OrgUpdateMemberAuditEntryPermission
   permissionWas: OrgUpdateMemberAuditEntryPermission
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgUpdateMemberRepositoryCreationPermissionAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   canCreateRepositories: bool
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI
   visibility: OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility

class OrgUpdateMemberRepositoryInvitationPermissionAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   canInviteOutsideCollaboratorsToRepositories: bool
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class PrivateRepositoryForkingDisableAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class PrivateRepositoryForkingEnableAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoAccessAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI
   visibility: RepoAccessAuditEntryVisibility

class RepoAddMemberAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI
   visibility: RepoAddMemberAuditEntryVisibility

class RepoAddTopicAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   topic: Topic
   topicName: str
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoArchivedAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI
   visibility: RepoArchivedAuditEntryVisibility

class RepoChangeMergeSettingAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   isEnabled: bool
   mergeType: RepoChangeMergeSettingAuditEntryMergeType
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoConfigDisableAnonymousGitAccessAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoConfigDisableCollaboratorsOnlyAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoConfigDisableContributorsOnlyAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoConfigDisableSockpuppetDisallowedAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoConfigEnableAnonymousGitAccessAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoConfigEnableCollaboratorsOnlyAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoConfigEnableContributorsOnlyAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoConfigEnableSockpuppetDisallowedAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoConfigLockAnonymousGitAccessAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoConfigUnlockAnonymousGitAccessAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepoCreateAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   forkParentName: str
   forkSourceName: str
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI
   visibility: RepoCreateAuditEntryVisibility

class RepoDestroyAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI
   visibility: RepoDestroyAuditEntryVisibility

class RepoRemoveMemberAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI
   visibility: RepoRemoveMemberAuditEntryVisibility

class RepoRemoveTopicAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   topic: Topic
   topicName: str
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepositoryVisibilityChangeDisableAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepositoryVisibilityChangeEnableAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class TeamAddMemberAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   isLdapMapped: bool
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   team: Team
   teamName: str
   teamResourcePath: URI
   teamUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class TeamAddRepositoryAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   isLdapMapped: bool
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   team: Team
   teamName: str
   teamResourcePath: URI
   teamUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class TeamChangeParentTeamAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   isLdapMapped: bool
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   parentTeam: Team
   parentTeamName: str
   parentTeamNameWas: str
   parentTeamResourcePath: URI
   parentTeamUrl: URI
   parentTeamWas: Team
   parentTeamWasResourcePath: URI
   parentTeamWasUrl: URI
   team: Team
   teamName: str
   teamResourcePath: URI
   teamUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class TeamRemoveMemberAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   isLdapMapped: bool
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   team: Team
   teamName: str
   teamResourcePath: URI
   teamUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class TeamRemoveRepositoryAuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   id: ID
   isLdapMapped: bool
   operationType: OperationType
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI
   team: Team
   teamName: str
   teamResourcePath: URI
   teamUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrganizationAuditEntry(GQLObject): 
   pass

class OrganizationAuditEntryEdge(GQLObject):
   cursor: str
   node: OrganizationAuditEntry

class list_OrganizationAuditEntryEdge(list, OrganizationAuditEntryEdge): pass

class list_OrganizationAuditEntry(list, OrganizationAuditEntry): pass

class OrganizationAuditEntryConnection(GQLObject):
   edges: list_OrganizationAuditEntryEdge[OrganizationAuditEntryEdge]
   nodes: list_OrganizationAuditEntry[OrganizationAuditEntry]
   pageInfo: PageInfo
   totalCount: int

class VerifiableDomainOwner(GQLObject): 
   pass

class VerifiableDomain(GQLObject):
   createdAt: DateTime
   databaseId: int
   dnsHostName: URI
   domain: URI
   hasFoundHostName: bool
   hasFoundVerificationToken: bool
   id: ID
   isApproved: bool
   isRequiredForPolicyEnforcement: bool
   isVerified: bool
   owner: VerifiableDomainOwner
   punycodeEncodedDomain: URI
   tokenExpirationTime: DateTime
   updatedAt: DateTime
   verificationToken: str

class VerifiableDomainEdge(GQLObject):
   cursor: str
   node: VerifiableDomain

class list_VerifiableDomainEdge(list, VerifiableDomainEdge): pass

class list_VerifiableDomain(list, VerifiableDomain): pass

class VerifiableDomainConnection(GQLObject):
   edges: list_VerifiableDomainEdge[VerifiableDomainEdge]
   nodes: list_VerifiableDomain[VerifiableDomain]
   pageInfo: PageInfo
   totalCount: int

class OrganizationEnterpriseOwnerEdge(GQLObject):
   cursor: str
   node: User
   organizationRole: RoleInOrganization

class list_OrganizationEnterpriseOwnerEdge(list, OrganizationEnterpriseOwnerEdge): pass

class list_User(list, User): pass

class OrganizationEnterpriseOwnerConnection(GQLObject):
   edges: list_OrganizationEnterpriseOwnerEdge[OrganizationEnterpriseOwnerEdge]
   nodes: list_User[User]
   pageInfo: PageInfo
   totalCount: int

class MannequinEdge(GQLObject):
   cursor: str
   node: Mannequin

class list_MannequinEdge(list, MannequinEdge): pass

class list_Mannequin(list, Mannequin): pass

class MannequinConnection(GQLObject):
   edges: list_MannequinEdge[MannequinEdge]
   nodes: list_Mannequin[Mannequin]
   pageInfo: PageInfo
   totalCount: int

class OrganizationMemberEdge(GQLObject):
   cursor: str
   hasTwoFactorEnabled: bool
   node: User
   role: OrganizationMemberRole

class list_OrganizationMemberEdge(list, OrganizationMemberEdge): pass

class OrganizationMemberConnection(GQLObject):
   edges: list_OrganizationMemberEdge[OrganizationMemberEdge]
   nodes: list_User[User]
   pageInfo: PageInfo
   totalCount: int

class RepositoryMigration(GQLObject):
   continueOnError: bool
   createdAt: DateTime
   databaseId: str
   failureReason: str
   id: ID
   migrationLogUrl: URI
   migrationSource: MigrationSource
   repositoryName: str
   sourceUrl: URI
   state: MigrationState
   warningsCount: int

class RepositoryMigrationEdge(GQLObject):
   cursor: str
   node: RepositoryMigration

class list_RepositoryMigrationEdge(list, RepositoryMigrationEdge): pass

class list_RepositoryMigration(list, RepositoryMigration): pass

class RepositoryMigrationConnection(GQLObject):
   edges: list_RepositoryMigrationEdge[RepositoryMigrationEdge]
   nodes: list_RepositoryMigration[RepositoryMigration]
   pageInfo: PageInfo
   totalCount: int

class list_ExternalIdentityAttribute(list, ExternalIdentityAttribute): pass

class list_UserEmailMetadata(list, UserEmailMetadata): pass

class ExternalIdentitySamlAttributes(GQLObject):
   attributes: list_ExternalIdentityAttribute[ExternalIdentityAttribute]
   emails: list_UserEmailMetadata[UserEmailMetadata]
   familyName: str
   givenName: str
   groups: list[str]
   nameId: str
   username: str

class ExternalIdentityScimAttributes(GQLObject):
   emails: list_UserEmailMetadata[UserEmailMetadata]
   familyName: str
   givenName: str
   groups: list[str]
   username: str

class ExternalIdentity(GQLObject):
   guid: str
   id: ID
   organizationInvitation: OrganizationInvitation
   samlIdentity: ExternalIdentitySamlAttributes
   scimIdentity: ExternalIdentityScimAttributes
   user: User

class ExternalIdentityEdge(GQLObject):
   cursor: str
   node: ExternalIdentity

class list_ExternalIdentityEdge(list, ExternalIdentityEdge): pass

class list_ExternalIdentity(list, ExternalIdentity): pass

class ExternalIdentityConnection(GQLObject):
   edges: list_ExternalIdentityEdge[ExternalIdentityEdge]
   nodes: list_ExternalIdentity[ExternalIdentity]
   pageInfo: PageInfo
   totalCount: int

class LRYLW_ExternalIdentityConnection_Field(ExternalIdentityConnection):
   class ExternalIdentityConnectionArgs(GQLArgsSet, GQLObject):
      membersOnly: bool
      login: str
      userName: str
      after: str
      before: str
      first: int
      last: int

   _args: ExternalIdentityConnectionArgs



class OrganizationIdentityProvider(GQLObject):
   digestMethod: URI
   externalIdentities: LRYLW_ExternalIdentityConnection_Field
   id: ID
   idpCertificate: X509Certificate
   issuer: str
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   signatureMethod: URI
   ssoUrl: URI

class JBKXF_OrganizationAuditEntryConnection_Field(OrganizationAuditEntryConnection):
   class OrganizationAuditEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: AuditLogOrder

   _args: OrganizationAuditEntryConnectionArgs



class WYOXC_VerifiableDomainConnection_Field(VerifiableDomainConnection):
   class VerifiableDomainConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      isVerified: bool
      isApproved: bool
      orderBy: VerifiableDomainOrder

   _args: VerifiableDomainConnectionArgs



class PORMI_OrganizationEnterpriseOwnerConnection_Field(OrganizationEnterpriseOwnerConnection):
   class OrganizationEnterpriseOwnerConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      organizationRole: RoleInOrganization
      orderBy: OrgEnterpriseOwnerOrder
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationEnterpriseOwnerConnectionArgs



class VAMQZ_IpAllowListEntryConnection_Field(Generic[IpAllowListEntryConnection]):
   class IpAllowListEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: IpAllowListEntryConnectionArgs



class DWIBB_MannequinConnection_Field(MannequinConnection):
   class MannequinConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: MannequinOrder

   _args: MannequinConnectionArgs



class EKYNL_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class YBHER_OrganizationMemberConnection_Field(OrganizationMemberConnection):
   class OrganizationMemberConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationMemberConnectionArgs



class KKUDZ_PackageConnection_Field(PackageConnection):
   class PackageConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      names: list[str]
      repositoryId: ID
      packageType: PackageType
      orderBy: PackageOrder

   _args: PackageConnectionArgs



class IOXAI_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class ONTPO_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class MRLRQ_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class UMLPL_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class XOOMN_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class NYWVA_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: ProjectOrder
      search: str
      states: list[NonNull_ProjectState]
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class ZYLFU_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class JUNKH_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class XAFRE_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: list[RepositoryAffiliation]
      ownerAffiliations: list[RepositoryAffiliation]
      isLocked: bool
      after: str
      before: str
      first: int
      last: int
      isFork: bool

   _args: RepositoryConnectionArgs



class SNURH_Repository_Field(Repository):
   class RepositoryArgs(GQLArgsSet, GQLObject):
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs



class MNLBT_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class HOIXH_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionOrder
      repositoryId: ID
      answered: bool
      states: list[NonNull_DiscussionState]

   _args: DiscussionConnectionArgs



class MZBHE_RepositoryMigrationConnection_Field(RepositoryMigrationConnection):
   class RepositoryMigrationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      state: MigrationState
      repositoryName: str
      orderBy: RepositoryMigrationOrder

   _args: RepositoryMigrationConnectionArgs



class BHATQ_RepositoryRuleset_Field(RepositoryRuleset):
   class RepositoryRulesetArgs(GQLArgsSet, GQLObject):
      databaseId: NonNull_int

   _args: RepositoryRulesetArgs



class FOZQV_RepositoryRulesetConnection_Field(RepositoryRulesetConnection):
   class RepositoryRulesetConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includeParents: bool

   _args: RepositoryRulesetConnectionArgs



class XKOYS_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class PJHIC_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class GZDRI_SponsorsActivityConnection_Field(SponsorsActivityConnection):
   class SponsorsActivityConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      period: SponsorsActivityPeriod
      since: DateTime
      until: DateTime
      orderBy: SponsorsActivityOrder
      actions: list[NonNull_SponsorsActivityAction]
      includeAsSponsor: bool

   _args: SponsorsActivityConnectionArgs



class ZXFIO_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class CCFBY_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class TCBYD_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class CTXYE_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class XMEVU_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipOrder
      maintainerLogins: list[NonNull_str]
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class LGNUW_Team_Field(Team):
   class TeamArgs(GQLArgsSet, GQLObject):
      slug: NonNull_str

   _args: TeamArgs



class AIJQS_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      privacy: TeamPrivacy
      notificationSetting: TeamNotificationSetting
      role: TeamRole
      query: str
      userLogins: list[NonNull_str]
      orderBy: TeamOrder
      ldapMapped: bool
      rootTeamsOnly: bool
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class Organization(GQLObject):
   announcement: str
   announcementExpiresAt: DateTime
   announcementUserDismissible: bool
   anyPinnableItems: OCGFU_anyPinnableItems_Field
   auditLog: JBKXF_OrganizationAuditEntryConnection_Field
   avatarUrl: ACXRV_URI_Field
   createdAt: DateTime
   databaseId: int
   description: str
   descriptionHTML: str
   domains: WYOXC_VerifiableDomainConnection_Field
   email: str
   enterpriseOwners: PORMI_OrganizationEnterpriseOwnerConnection_Field
   estimatedNextSponsorsPayoutInCents: int
   hasSponsorsListing: bool
   id: ID
   interactionAbility: RepositoryInteractionAbility
   ipAllowListEnabledSetting: IpAllowListEnabledSettingValue
   ipAllowListEntries: VAMQZ_IpAllowListEntryConnection_Field ## Circular Reference for IpAllowListEntryConnection
   ipAllowListForInstalledAppsEnabledSetting: IpAllowListForInstalledAppsEnabledSettingValue
   isSponsoredBy: ACEAV_isSponsoredBy_Field
   isSponsoringViewer: bool
   isVerified: bool
   itemShowcase: ProfileItemShowcase
   location: str
   login: str
   mannequins: DWIBB_MannequinConnection_Field
   memberStatuses: EKYNL_UserStatusConnection_Field
   membersCanForkPrivateRepositories: bool
   membersWithRole: YBHER_OrganizationMemberConnection_Field
   monthlyEstimatedSponsorsIncomeInCents: int
   name: str
   newTeamResourcePath: URI
   newTeamUrl: URI
   notificationDeliveryRestrictionEnabledSetting: NotificationRestrictionSettingValue
   organizationBillingEmail: str
   packages: KKUDZ_PackageConnection_Field
   pendingMembers: IOXAI_UserConnection_Field
   pinnableItems: ONTPO_PinnableItemConnection_Field
   pinnedItems: MRLRQ_PinnableItemConnection_Field
   pinnedItemsRemaining: int
   project: UMLPL_Project_Field
   projectV2: XOOMN_ProjectV2_Field
   projects: NYWVA_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   projectsV2: ZYLFU_ProjectV2Connection_Field
   recentProjects: JUNKH_ProjectV2Connection_Field
   repositories: XAFRE_RepositoryConnection_Field
   repository: SNURH_Repository_Field
   repositoryDiscussionComments: MNLBT_DiscussionCommentConnection_Field
   repositoryDiscussions: HOIXH_DiscussionConnection_Field
   repositoryMigrations: MZBHE_RepositoryMigrationConnection_Field
   requiresTwoFactorAuthentication: bool
   resourcePath: URI
   ruleset: BHATQ_RepositoryRuleset_Field
   rulesets: FOZQV_RepositoryRulesetConnection_Field
   samlIdentityProvider: OrganizationIdentityProvider
   sponsoring: XKOYS_SponsorConnection_Field
   sponsors: PJHIC_SponsorConnection_Field
   sponsorsActivities: GZDRI_SponsorsActivityConnection_Field
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: ZXFIO_Sponsorship_Field
   sponsorshipForViewerAsSponsorable: CCFBY_Sponsorship_Field
   sponsorshipNewsletters: TCBYD_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: CTXYE_SponsorshipConnection_Field
   sponsorshipsAsSponsor: XMEVU_SponsorshipConnection_Field
   team: LGNUW_Team_Field
   teams: AIJQS_TeamConnection_Field
   teamsResourcePath: URI
   teamsUrl: URI
   totalSponsorshipAmountAsSponsorInCents: WLIHN_totalSponsorshipAmountAsSponsorInCents_Field
   twitterUsername: str
   updatedAt: DateTime
   url: URI
   viewerCanAdminister: bool
   viewerCanChangePinnedItems: bool
   viewerCanCreateProjects: bool
   viewerCanCreateRepositories: bool
   viewerCanCreateTeams: bool
   viewerCanSponsor: bool
   viewerIsAMember: bool
   viewerIsFollowing: bool
   viewerIsSponsoring: bool
   webCommitSignoffRequired: bool
   websiteUrl: URI

class EnterpriseOrganizationMembershipEdge(GQLObject):
   cursor: str
   node: Organization
   role: EnterpriseUserAccountMembershipRole

class list_EnterpriseOrganizationMembershipEdge(list, EnterpriseOrganizationMembershipEdge): pass

class list_Organization(list, Organization): pass

class EnterpriseOrganizationMembershipConnection(GQLObject):
   edges: list_EnterpriseOrganizationMembershipEdge[EnterpriseOrganizationMembershipEdge]
   nodes: list_Organization[Organization]
   pageInfo: PageInfo
   totalCount: int

class ECDON_EnterpriseServerInstallationMembershipConnection_Field(EnterpriseServerInstallationMembershipConnection):
   class EnterpriseServerInstallationMembershipConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: EnterpriseServerInstallationOrder
      role: EnterpriseUserAccountMembershipRole
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerInstallationMembershipConnectionArgs



class GOPLL_EnterpriseOrganizationMembershipConnection_Field(EnterpriseOrganizationMembershipConnection):
   class EnterpriseOrganizationMembershipConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: OrganizationOrder
      role: EnterpriseUserAccountMembershipRole
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseOrganizationMembershipConnectionArgs



class EnterpriseUserAccount(GQLObject):
   avatarUrl: HDSAY_URI_Field
   createdAt: DateTime
   enterprise: NewType('Enterprise', GQLObject) ## Circular Reference for Enterprise
   enterpriseInstallations: ECDON_EnterpriseServerInstallationMembershipConnection_Field
   id: ID
   login: str
   name: str
   organizations: GOPLL_EnterpriseOrganizationMembershipConnection_Field
   resourcePath: URI
   updatedAt: DateTime
   url: URI
   user: User

class EnterpriseMember(GQLObject): 
   pass

class EnterpriseMemberEdge(GQLObject):
   cursor: str
   node: EnterpriseMember

class list_EnterpriseMemberEdge(list, EnterpriseMemberEdge): pass

class list_EnterpriseMember(list, EnterpriseMember): pass

class EnterpriseMemberConnection(GQLObject):
   edges: list_EnterpriseMemberEdge[EnterpriseMemberEdge]
   nodes: list_EnterpriseMember[EnterpriseMember]
   pageInfo: PageInfo
   totalCount: int

class EnterpriseAdministratorEdge(GQLObject):
   cursor: str
   node: User
   role: EnterpriseAdministratorRole

class list_EnterpriseAdministratorEdge(list, EnterpriseAdministratorEdge): pass

class EnterpriseAdministratorConnection(GQLObject):
   edges: list_EnterpriseAdministratorEdge[EnterpriseAdministratorEdge]
   nodes: list_User[User]
   pageInfo: PageInfo
   totalCount: int

class EnterpriseServerInstallationEdge(GQLObject):
   cursor: str
   node: EnterpriseServerInstallation

class list_EnterpriseServerInstallationEdge(list, EnterpriseServerInstallationEdge): pass

class EnterpriseServerInstallationConnection(GQLObject):
   edges: list_EnterpriseServerInstallationEdge[EnterpriseServerInstallationEdge]
   nodes: list_EnterpriseServerInstallation[EnterpriseServerInstallation]
   pageInfo: PageInfo
   totalCount: int

class EnterpriseFailedInvitationEdge(GQLObject):
   cursor: str
   node: OrganizationInvitation

class list_EnterpriseFailedInvitationEdge(list, EnterpriseFailedInvitationEdge): pass

class EnterpriseFailedInvitationConnection(GQLObject):
   edges: list_EnterpriseFailedInvitationEdge[EnterpriseFailedInvitationEdge]
   nodes: list_OrganizationInvitation[OrganizationInvitation]
   pageInfo: PageInfo
   totalCount: int
   totalUniqueUserCount: int

class DHIOK_ExternalIdentityConnection_Field(ExternalIdentityConnection):
   class ExternalIdentityConnectionArgs(GQLArgsSet, GQLObject):
      membersOnly: bool
      login: str
      userName: str
      after: str
      before: str
      first: int
      last: int

   _args: ExternalIdentityConnectionArgs



class OIDCProvider(GQLObject):
   enterprise: NewType('Enterprise', GQLObject) ## Circular Reference for Enterprise
   externalIdentities: DHIOK_ExternalIdentityConnection_Field
   id: ID
   providerType: OIDCProviderType
   tenantId: str

class EnterpriseRepositoryInfoEdge(GQLObject):
   cursor: str
   node: EnterpriseRepositoryInfo

class list_EnterpriseRepositoryInfoEdge(list, EnterpriseRepositoryInfoEdge): pass

class list_EnterpriseRepositoryInfo(list, EnterpriseRepositoryInfo): pass

class EnterpriseRepositoryInfoConnection(GQLObject):
   edges: list_EnterpriseRepositoryInfoEdge[EnterpriseRepositoryInfoEdge]
   nodes: list_EnterpriseRepositoryInfo[EnterpriseRepositoryInfo]
   pageInfo: PageInfo
   totalCount: int

class XFDVD_EnterpriseRepositoryInfoConnection_Field(EnterpriseRepositoryInfoConnection):
   class EnterpriseRepositoryInfoConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: RepositoryOrder

   _args: EnterpriseRepositoryInfoConnectionArgs



class EnterpriseOutsideCollaboratorEdge(GQLObject):
   cursor: str
   node: User
   repositories: XFDVD_EnterpriseRepositoryInfoConnection_Field

class list_EnterpriseOutsideCollaboratorEdge(list, EnterpriseOutsideCollaboratorEdge): pass

class EnterpriseOutsideCollaboratorConnection(GQLObject):
   edges: list_EnterpriseOutsideCollaboratorEdge[EnterpriseOutsideCollaboratorEdge]
   nodes: list_User[User]
   pageInfo: PageInfo
   totalCount: int

class EnterpriseAdministratorInvitation(GQLObject):
   createdAt: DateTime
   email: str
   enterprise: NewType('Enterprise', GQLObject) ## Circular Reference for Enterprise
   id: ID
   invitee: User
   inviter: User
   role: EnterpriseAdministratorRole

class EnterpriseAdministratorInvitationEdge(GQLObject):
   cursor: str
   node: EnterpriseAdministratorInvitation

class list_EnterpriseAdministratorInvitationEdge(list, EnterpriseAdministratorInvitationEdge): pass

class list_EnterpriseAdministratorInvitation(list, EnterpriseAdministratorInvitation): pass

class EnterpriseAdministratorInvitationConnection(GQLObject):
   edges: list_EnterpriseAdministratorInvitationEdge[EnterpriseAdministratorInvitationEdge]
   nodes: list_EnterpriseAdministratorInvitation[EnterpriseAdministratorInvitation]
   pageInfo: PageInfo
   totalCount: int

class RepositoryInfo(GQLObject):
   archivedAt: DateTime
   createdAt: DateTime
   description: str
   descriptionHTML: HTML
   forkCount: int
   hasDiscussionsEnabled: bool
   hasIssuesEnabled: bool
   hasProjectsEnabled: bool
   hasWikiEnabled: bool
   homepageUrl: URI
   isArchived: bool
   isFork: bool
   isInOrganization: bool
   isLocked: bool
   isMirror: bool
   isPrivate: bool
   isTemplate: bool
   licenseInfo: License
   lockReason: RepositoryLockReason
   mirrorUrl: URI
   name: str
   nameWithOwner: str
   openGraphImageUrl: URI
   owner: RepositoryOwner
   pushedAt: DateTime
   resourcePath: URI
   shortDescriptionHTML: QMJPZ_HTML_Field
   updatedAt: DateTime
   url: URI
   usesCustomOpenGraphImage: bool
   visibility: RepositoryVisibility

class RepositoryInvitation(GQLObject):
   email: str
   id: ID
   invitee: User
   inviter: User
   permalink: URI
   permission: RepositoryPermission
   repository: RepositoryInfo

class RepositoryInvitationEdge(GQLObject):
   cursor: str
   node: RepositoryInvitation

class list_RepositoryInvitationEdge(list, RepositoryInvitationEdge): pass

class list_RepositoryInvitation(list, RepositoryInvitation): pass

class RepositoryInvitationConnection(GQLObject):
   edges: list_RepositoryInvitationEdge[RepositoryInvitationEdge]
   nodes: list_RepositoryInvitation[RepositoryInvitation]
   pageInfo: PageInfo
   totalCount: int

class EnterprisePendingMemberInvitationEdge(GQLObject):
   cursor: str
   node: OrganizationInvitation

class list_EnterprisePendingMemberInvitationEdge(list, EnterprisePendingMemberInvitationEdge): pass

class EnterprisePendingMemberInvitationConnection(GQLObject):
   edges: list_EnterprisePendingMemberInvitationEdge[EnterprisePendingMemberInvitationEdge]
   nodes: list_OrganizationInvitation[OrganizationInvitation]
   pageInfo: PageInfo
   totalCount: int
   totalUniqueUserCount: int

class HNWYB_ExternalIdentityConnection_Field(ExternalIdentityConnection):
   class ExternalIdentityConnectionArgs(GQLArgsSet, GQLObject):
      membersOnly: bool
      login: str
      userName: str
      after: str
      before: str
      first: int
      last: int

   _args: ExternalIdentityConnectionArgs



class EnterpriseIdentityProvider(GQLObject):
   digestMethod: SamlDigestAlgorithm
   enterprise: NewType('Enterprise', GQLObject) ## Circular Reference for Enterprise
   externalIdentities: HNWYB_ExternalIdentityConnection_Field
   id: ID
   idpCertificate: X509Certificate
   issuer: str
   recoveryCodes: list[str]
   signatureMethod: SamlSignatureAlgorithm
   ssoUrl: URI

class XDREB_EnterpriseAdministratorConnection_Field(EnterpriseAdministratorConnection):
   class EnterpriseAdministratorConnectionArgs(GQLArgsSet, GQLObject):
      organizationLogins: list[NonNull_str]
      query: str
      role: EnterpriseAdministratorRole
      orderBy: EnterpriseMemberOrder
      hasTwoFactorEnabled: bool
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseAdministratorConnectionArgs



class CLKDX_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class ECZAE_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class NonNull_DefaultRepositoryPermissionField(GQLObject): pass

class VZXUY_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_DefaultRepositoryPermissionField
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class ALSTO_VerifiableDomainConnection_Field(VerifiableDomainConnection):
   class VerifiableDomainConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      isVerified: bool
      isApproved: bool
      orderBy: VerifiableDomainOrder

   _args: VerifiableDomainConnectionArgs



class ZDFQK_EnterpriseServerInstallationConnection_Field(EnterpriseServerInstallationConnection):
   class EnterpriseServerInstallationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      connectedOnly: bool
      orderBy: EnterpriseServerInstallationOrder

   _args: EnterpriseServerInstallationConnectionArgs



class IEVDB_EnterpriseFailedInvitationConnection_Field(EnterpriseFailedInvitationConnection):
   class EnterpriseFailedInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseFailedInvitationConnectionArgs



class NQBNI_IpAllowListEntryConnection_Field(Generic[IpAllowListEntryConnection]):
   class IpAllowListEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: IpAllowListEntryConnectionArgs



class PQPKR_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class NonNull_OrganizationMembersCanCreateRepositoriesSettingValue(GQLObject): pass

class GHAVP_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_OrganizationMembersCanCreateRepositoriesSettingValue
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class LANDP_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class SMPOD_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class OSYVL_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class XOHZC_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class OGNAT_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class ZDRQT_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class BFGSX_EnterpriseOutsideCollaboratorConnection_Field(EnterpriseOutsideCollaboratorConnection):
   class EnterpriseOutsideCollaboratorConnectionArgs(GQLArgsSet, GQLObject):
      login: str
      query: str
      orderBy: EnterpriseMemberOrder
      visibility: RepositoryVisibility
      hasTwoFactorEnabled: bool
      organizationLogins: list[NonNull_str]
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseOutsideCollaboratorConnectionArgs



class RHMAR_EnterpriseAdministratorInvitationConnection_Field(EnterpriseAdministratorInvitationConnection):
   class EnterpriseAdministratorInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: EnterpriseAdministratorInvitationOrder
      role: EnterpriseAdministratorRole
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseAdministratorInvitationConnectionArgs



class KSOOK_RepositoryInvitationConnection_Field(RepositoryInvitationConnection):
   class RepositoryInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: RepositoryInvitationOrder
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryInvitationConnectionArgs



class KHRUB_EnterprisePendingMemberInvitationConnection_Field(EnterprisePendingMemberInvitationConnection):
   class EnterprisePendingMemberInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      organizationLogins: list[NonNull_str]
      invitationSource: OrganizationInvitationSource
      after: str
      before: str
      first: int
      last: int

   _args: EnterprisePendingMemberInvitationConnectionArgs



class FCYWY_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class NonNull_IdentityProviderConfigurationState(GQLObject): pass

class FAJQV_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_IdentityProviderConfigurationState
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class UXBGK_EnterpriseMemberConnection_Field(EnterpriseMemberConnection):
   class EnterpriseMemberConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: EnterpriseMemberOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseMemberConnectionArgs



class TPPUT_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class ZNEXR_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class EnterpriseOwnerInfo(GQLObject):
   admins: XDREB_EnterpriseAdministratorConnection_Field
   affiliatedUsersWithTwoFactorDisabled: CLKDX_UserConnection_Field
   affiliatedUsersWithTwoFactorDisabledExist: bool
   allowPrivateRepositoryForkingSetting: EnterpriseEnabledDisabledSettingValue
   allowPrivateRepositoryForkingSettingOrganizations: ECZAE_OrganizationConnection_Field
   allowPrivateRepositoryForkingSettingPolicyValue: EnterpriseAllowPrivateRepositoryForkingPolicyValue
   defaultRepositoryPermissionSetting: EnterpriseDefaultRepositoryPermissionSettingValue
   defaultRepositoryPermissionSettingOrganizations: VZXUY_OrganizationConnection_Field
   domains: ALSTO_VerifiableDomainConnection_Field
   enterpriseServerInstallations: ZDFQK_EnterpriseServerInstallationConnection_Field
   failedInvitations: IEVDB_EnterpriseFailedInvitationConnection_Field
   ipAllowListEnabledSetting: IpAllowListEnabledSettingValue
   ipAllowListEntries: NQBNI_IpAllowListEntryConnection_Field ## Circular Reference for IpAllowListEntryConnection
   ipAllowListForInstalledAppsEnabledSetting: IpAllowListForInstalledAppsEnabledSettingValue
   isUpdatingDefaultRepositoryPermission: bool
   isUpdatingTwoFactorRequirement: bool
   membersCanChangeRepositoryVisibilitySetting: EnterpriseEnabledDisabledSettingValue
   membersCanChangeRepositoryVisibilitySettingOrganizations: PQPKR_OrganizationConnection_Field
   membersCanCreateInternalRepositoriesSetting: bool
   membersCanCreatePrivateRepositoriesSetting: bool
   membersCanCreatePublicRepositoriesSetting: bool
   membersCanCreateRepositoriesSetting: EnterpriseMembersCanCreateRepositoriesSettingValue
   membersCanCreateRepositoriesSettingOrganizations: GHAVP_OrganizationConnection_Field
   membersCanDeleteIssuesSetting: EnterpriseEnabledDisabledSettingValue
   membersCanDeleteIssuesSettingOrganizations: LANDP_OrganizationConnection_Field
   membersCanDeleteRepositoriesSetting: EnterpriseEnabledDisabledSettingValue
   membersCanDeleteRepositoriesSettingOrganizations: SMPOD_OrganizationConnection_Field
   membersCanInviteCollaboratorsSetting: EnterpriseEnabledDisabledSettingValue
   membersCanInviteCollaboratorsSettingOrganizations: OSYVL_OrganizationConnection_Field
   membersCanMakePurchasesSetting: EnterpriseMembersCanMakePurchasesSettingValue
   membersCanUpdateProtectedBranchesSetting: EnterpriseEnabledDisabledSettingValue
   membersCanUpdateProtectedBranchesSettingOrganizations: XOHZC_OrganizationConnection_Field
   membersCanViewDependencyInsightsSetting: EnterpriseEnabledDisabledSettingValue
   membersCanViewDependencyInsightsSettingOrganizations: OGNAT_OrganizationConnection_Field
   notificationDeliveryRestrictionEnabledSetting: NotificationRestrictionSettingValue
   oidcProvider: OIDCProvider
   organizationProjectsSetting: EnterpriseEnabledDisabledSettingValue
   organizationProjectsSettingOrganizations: ZDRQT_OrganizationConnection_Field
   outsideCollaborators: BFGSX_EnterpriseOutsideCollaboratorConnection_Field
   pendingAdminInvitations: RHMAR_EnterpriseAdministratorInvitationConnection_Field
   pendingCollaboratorInvitations: KSOOK_RepositoryInvitationConnection_Field
   pendingMemberInvitations: KHRUB_EnterprisePendingMemberInvitationConnection_Field
   repositoryProjectsSetting: EnterpriseEnabledDisabledSettingValue
   repositoryProjectsSettingOrganizations: FCYWY_OrganizationConnection_Field
   samlIdentityProvider: EnterpriseIdentityProvider
   samlIdentityProviderSettingOrganizations: FAJQV_OrganizationConnection_Field
   supportEntitlements: UXBGK_EnterpriseMemberConnection_Field
   teamDiscussionsSetting: EnterpriseEnabledDisabledSettingValue
   teamDiscussionsSettingOrganizations: TPPUT_OrganizationConnection_Field
   twoFactorRequiredSetting: EnterpriseEnabledSettingValue
   twoFactorRequiredSettingOrganizations: ZNEXR_OrganizationConnection_Field

class JQZGU_EnterpriseMemberConnection_Field(EnterpriseMemberConnection):
   class EnterpriseMemberConnectionArgs(GQLArgsSet, GQLObject):
      organizationLogins: list[NonNull_str]
      query: str
      orderBy: EnterpriseMemberOrder
      role: EnterpriseUserAccountMembershipRole
      deployment: EnterpriseUserDeployment
      hasTwoFactorEnabled: bool
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseMemberConnectionArgs



class LTMAN_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      viewerOrganizationRole: RoleInOrganization
      orderBy: OrganizationOrder
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class Enterprise(GQLObject):
   announcement: str
   announcementExpiresAt: DateTime
   announcementUserDismissible: bool
   avatarUrl: RTGBY_URI_Field
   billingInfo: EnterpriseBillingInfo
   createdAt: DateTime
   databaseId: int
   description: str
   descriptionHTML: HTML
   id: ID
   location: str
   members: JQZGU_EnterpriseMemberConnection_Field
   name: str
   organizations: LTMAN_OrganizationConnection_Field
   ownerInfo: EnterpriseOwnerInfo
   resourcePath: URI
   slug: str
   url: URI
   viewerIsAdmin: bool
   websiteUrl: URI

class IpAllowListOwner(GQLObject): 
   pass

class IpAllowListEntry(GQLObject):
   allowListValue: str
   createdAt: DateTime
   id: ID
   isActive: bool
   name: str
   owner: IpAllowListOwner
   updatedAt: DateTime

class IpAllowListEntryEdge(GQLObject):
   cursor: str
   node: IpAllowListEntry

class list_IpAllowListEntryEdge(list, IpAllowListEntryEdge): pass

class list_IpAllowListEntry(list, IpAllowListEntry): pass

class IpAllowListEntryConnection(GQLObject):
   edges: list_IpAllowListEntryEdge[IpAllowListEntryEdge]
   nodes: list_IpAllowListEntry[IpAllowListEntry]
   pageInfo: PageInfo
   totalCount: int

class JHKRQ_IpAllowListEntryConnection_Field(IpAllowListEntryConnection):
   class IpAllowListEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: IpAllowListEntryConnectionArgs



class App(GQLObject):
   createdAt: DateTime
   databaseId: int
   description: str
   id: ID
   ipAllowListEntries: JHKRQ_IpAllowListEntryConnection_Field
   logoBackgroundColor: str
   logoUrl: SBGUI_URI_Field
   name: str
   slug: str
   updatedAt: DateTime
   url: URI

class CheckRunEdge(GQLObject):
   cursor: str
   node: CheckRun

class list_CheckRunEdge(list, CheckRunEdge): pass

class list_CheckRun(list, CheckRun): pass

class CheckRunConnection(GQLObject):
   edges: list_CheckRunEdge[CheckRunEdge]
   nodes: list_CheckRun[CheckRun]
   pageInfo: PageInfo
   totalCount: int

class Push(GQLObject):
   id: ID
   nextSha: GitObjectID
   permalink: URI
   previousSha: GitObjectID
   pusher: Actor
   repository: Repository

class DCKEH_CheckRunConnection_Field(CheckRunConnection):
   class CheckRunConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      filterBy: CheckRunFilter

   _args: CheckRunConnectionArgs



class YRRKU_PullRequestConnection_Field(PullRequestConnection):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      states: list[NonNull_PullRequestState]
      labels: list[NonNull_str]
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class CheckSuite(GQLObject):
   app: App
   branch: Ref
   checkRuns: DCKEH_CheckRunConnection_Field
   commit: Commit
   conclusion: CheckConclusionState
   createdAt: DateTime
   creator: User
   databaseId: int
   id: ID
   matchingPullRequests: YRRKU_PullRequestConnection_Field
   push: Push
   repository: Repository
   resourcePath: URI
   status: CheckStatusState
   updatedAt: DateTime
   url: URI
   workflowRun: NewType('WorkflowRun', GQLObject) ## Circular Reference for WorkflowRun

class FVVDL_EnvironmentConnection_Field(EnvironmentConnection):
   class EnvironmentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: EnvironmentConnectionArgs



class DeploymentReview(GQLObject):
   comment: str
   databaseId: int
   environments: FVVDL_EnvironmentConnection_Field
   id: ID
   state: DeploymentReviewState
   user: User

class DeploymentReviewEdge(GQLObject):
   cursor: str
   node: DeploymentReview

class list_DeploymentReviewEdge(list, DeploymentReviewEdge): pass

class list_DeploymentReview(list, DeploymentReview): pass

class DeploymentReviewConnection(GQLObject):
   edges: list_DeploymentReviewEdge[DeploymentReviewEdge]
   nodes: list_DeploymentReview[DeploymentReview]
   pageInfo: PageInfo
   totalCount: int

class WorkflowRunFile(GQLObject):
   id: ID
   path: str
   repositoryFileUrl: URI
   repositoryName: URI
   resourcePath: URI
   run: NewType('WorkflowRun', GQLObject) ## Circular Reference for WorkflowRun
   url: URI
   viewerCanPushRepository: bool
   viewerCanReadRepository: bool

class DeploymentRequestEdge(GQLObject):
   cursor: str
   node: DeploymentRequest

class list_DeploymentRequestEdge(list, DeploymentRequestEdge): pass

class list_DeploymentRequest(list, DeploymentRequest): pass

class DeploymentRequestConnection(GQLObject):
   edges: list_DeploymentRequestEdge[DeploymentRequestEdge]
   nodes: list_DeploymentRequest[DeploymentRequest]
   pageInfo: PageInfo
   totalCount: int

class VXWAG_WorkflowRunConnection_Field(Generic[WorkflowRunConnection]):
   class WorkflowRunConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: WorkflowRunOrder

   _args: WorkflowRunConnectionArgs



class Workflow(GQLObject):
   createdAt: DateTime
   databaseId: int
   id: ID
   name: str
   resourcePath: URI
   runs: VXWAG_WorkflowRunConnection_Field ## Circular Reference for WorkflowRunConnection
   state: WorkflowState
   updatedAt: DateTime
   url: URI

class XFABR_DeploymentReviewConnection_Field(DeploymentReviewConnection):
   class DeploymentReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewConnectionArgs



class PBBDS_DeploymentRequestConnection_Field(DeploymentRequestConnection):
   class DeploymentRequestConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentRequestConnectionArgs



class WorkflowRun(GQLObject):
   checkSuite: CheckSuite
   createdAt: DateTime
   databaseId: int
   deploymentReviews: XFABR_DeploymentReviewConnection_Field
   event: str
   file: WorkflowRunFile
   id: ID
   pendingDeploymentRequests: PBBDS_DeploymentRequestConnection_Field
   resourcePath: URI
   runNumber: int
   updatedAt: DateTime
   url: URI
   workflow: Workflow

class WorkflowRunEdge(GQLObject):
   cursor: str
   node: WorkflowRun

class list_WorkflowRunEdge(list, WorkflowRunEdge): pass

class list_WorkflowRun(list, WorkflowRun): pass

class WorkflowRunConnection(GQLObject):
   edges: list_WorkflowRunEdge[WorkflowRunEdge]
   nodes: list_WorkflowRun[WorkflowRun]
   pageInfo: PageInfo
   totalCount: int

class list_Team(list, Team): pass

class UpdateTeamsRepositoryPayload(GQLObject):
   clientMutationId: str
   repository: Repository
   teams: list_Team[Team]

class list_StatusCheckConfigurationInput(list, StatusCheckConfigurationInput): pass

class RequiredStatusChecksParametersInput(GQLObject):
   requiredStatusChecks: list_StatusCheckConfigurationInput[StatusCheckConfigurationInput]
   strictRequiredStatusChecksPolicy: bool

class RuleParametersInput(GQLObject):
   update: UpdateParametersInput
   requiredDeployments: RequiredDeploymentsParametersInput
   pullRequest: PullRequestParametersInput
   requiredStatusChecks: RequiredStatusChecksParametersInput
   commitMessagePattern: CommitMessagePatternParametersInput
   commitAuthorEmailPattern: CommitAuthorEmailPatternParametersInput
   committerEmailPattern: CommitterEmailPatternParametersInput
   branchNamePattern: BranchNamePatternParametersInput
   tagNamePattern: TagNamePatternParametersInput

class RepositoryRuleInput(GQLObject):
   id: ID
   type: RepositoryRuleType
   parameters: RuleParametersInput

class RepositoryRuleConditionsInput(GQLObject):
   refName: RefNameConditionTargetInput
   repositoryName: RepositoryNameConditionTargetInput
   repositoryId: RepositoryIdConditionTargetInput

class list_RepositoryRuleInput(list, RepositoryRuleInput): pass

class list_RepositoryRulesetBypassActorInput(list, RepositoryRulesetBypassActorInput): pass

class UpdateRepositoryRulesetInput(GQLObject):
   repositoryRulesetId: ID
   name: str
   target: RepositoryRulesetTarget
   rules: list_RepositoryRuleInput[RepositoryRuleInput]
   conditions: RepositoryRuleConditionsInput
   enforcement: RuleEnforcement
   bypassActors: list_RepositoryRulesetBypassActorInput[RepositoryRulesetBypassActorInput]
   clientMutationId: str

class UpdatePullRequestPayload(GQLObject):
   actor: Actor
   clientMutationId: str
   pullRequest: PullRequest

class UpdateIssuePayload(GQLObject):
   actor: Actor
   clientMutationId: str
   issue: Issue

class CheckAnnotationData(GQLObject):
   path: str
   location: CheckAnnotationRange
   annotationLevel: CheckAnnotationLevel
   message: str
   title: str
   rawDetails: str

class list_CheckAnnotationData(list, CheckAnnotationData): pass

class list_CheckRunOutputImage(list, CheckRunOutputImage): pass

class CheckRunOutput(GQLObject):
   title: str
   summary: str
   text: str
   annotations: list_CheckAnnotationData[CheckAnnotationData]
   images: list_CheckRunOutputImage[CheckRunOutputImage]

class list_CheckRunAction(list, CheckRunAction): pass

class UpdateCheckRunInput(GQLObject):
   repositoryId: ID
   checkRunId: ID
   name: str
   detailsUrl: URI
   externalId: str
   status: RequestableCheckStatusState
   startedAt: DateTime
   conclusion: CheckConclusionState
   completedAt: DateTime
   output: CheckRunOutput
   actions: list_CheckRunAction[CheckRunAction]
   clientMutationId: str

class UnlockLockablePayload(GQLObject):
   actor: Actor
   clientMutationId: str
   unlockedRecord: Lockable

class UnlinkRepositoryFromProjectPayload(GQLObject):
   clientMutationId: str
   project: Project
   repository: Repository

class Tag(GQLObject):
   abbreviatedOid: str
   commitResourcePath: URI
   commitUrl: URI
   id: ID
   message: str
   name: str
   oid: GitObjectID
   repository: Repository
   tagger: GitActor
   target: GitObject

class SponsorableItem(GQLObject): 
   pass

class SponsorableItemEdge(GQLObject):
   cursor: str
   node: SponsorableItem

class list_SponsorableItemEdge(list, SponsorableItemEdge): pass

class list_SponsorableItem(list, SponsorableItem): pass

class SponsorableItemConnection(GQLObject):
   edges: list_SponsorableItemEdge[SponsorableItemEdge]
   nodes: list_SponsorableItem[SponsorableItem]
   pageInfo: PageInfo
   totalCount: int

class SecurityAdvisoryEdge(GQLObject):
   cursor: str
   node: SecurityAdvisory

class list_SecurityAdvisoryEdge(list, SecurityAdvisoryEdge): pass

class list_SecurityAdvisory(list, SecurityAdvisory): pass

class SecurityAdvisoryConnection(GQLObject):
   edges: list_SecurityAdvisoryEdge[SecurityAdvisoryEdge]
   nodes: list_SecurityAdvisory[SecurityAdvisory]
   pageInfo: PageInfo
   totalCount: int

class MarketplaceListing(GQLObject):
   app: App
   companyUrl: URI
   configurationResourcePath: URI
   configurationUrl: URI
   documentationUrl: URI
   extendedDescription: str
   extendedDescriptionHTML: HTML
   fullDescription: str
   fullDescriptionHTML: HTML
   hasPublishedFreeTrialPlans: bool
   hasTermsOfService: bool
   hasVerifiedOwner: bool
   howItWorks: str
   howItWorksHTML: HTML
   id: ID
   installationUrl: URI
   installedForViewer: bool
   isArchived: bool
   isDraft: bool
   isPaid: bool
   isPublic: bool
   isRejected: bool
   isUnverified: bool
   isUnverifiedPending: bool
   isVerificationPendingFromDraft: bool
   isVerificationPendingFromUnverified: bool
   isVerified: bool
   logoBackgroundColor: str
   logoUrl: WHZHN_URI_Field
   name: str
   normalizedShortDescription: str
   pricingUrl: URI
   primaryCategory: MarketplaceCategory
   privacyPolicyUrl: URI
   resourcePath: URI
   screenshotUrls: list[str]
   secondaryCategory: MarketplaceCategory
   shortDescription: str
   slug: str
   statusUrl: URI
   supportEmail: str
   supportUrl: URI
   termsOfServiceUrl: URI
   url: URI
   viewerCanAddPlans: bool
   viewerCanApprove: bool
   viewerCanDelist: bool
   viewerCanEdit: bool
   viewerCanEditCategories: bool
   viewerCanEditPlans: bool
   viewerCanRedraft: bool
   viewerCanReject: bool
   viewerCanRequestApproval: bool
   viewerHasPurchased: bool
   viewerHasPurchasedForAllOrganizations: bool
   viewerIsListingAdmin: bool

class SearchResultItem(GQLObject): 
   pass

class list_TextMatchHighlight(list, TextMatchHighlight): pass

class TextMatch(GQLObject):
   fragment: str
   highlights: list_TextMatchHighlight[TextMatchHighlight]
   property: str

class list_TextMatch(list, TextMatch): pass

class SearchResultItemEdge(GQLObject):
   cursor: str
   node: SearchResultItem
   textMatches: list_TextMatch[TextMatch]

class list_SearchResultItemEdge(list, SearchResultItemEdge): pass

class list_SearchResultItem(list, SearchResultItem): pass

class SearchResultItemConnection(GQLObject):
   codeCount: int
   discussionCount: int
   edges: list_SearchResultItemEdge[SearchResultItemEdge]
   issueCount: int
   nodes: list_SearchResultItem[SearchResultItem]
   pageInfo: PageInfo
   repositoryCount: int
   userCount: int
   wikiCount: int

class RevertPullRequestPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest
   revertPullRequest: PullRequest

class RequestReviewsPayload(GQLObject):
   actor: Actor
   clientMutationId: str
   pullRequest: PullRequest
   requestedReviewersEdge: UserEdge

class RemoveReactionPayload(GQLObject):
   clientMutationId: str
   reaction: Reaction
   reactionGroups: list_ReactionGroup[ReactionGroup]
   subject: Reactable

class RemoveEnterpriseOrganizationPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   organization: Organization
   viewer: User

class RemoveEnterpriseMemberPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   user: User
   viewer: User

class RemoveEnterpriseAdminPayload(GQLObject):
   admin: User
   clientMutationId: str
   enterprise: Enterprise
   message: str
   viewer: User

class ITRUH_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      skip: int

   _args: PullRequestReviewCommentConnectionArgs



class PullRequestThread(GQLObject):
   comments: ITRUH_PullRequestReviewCommentConnection_Field
   diffSide: DiffSide
   id: ID
   isCollapsed: bool
   isOutdated: bool
   isResolved: bool
   line: int
   path: str
   pullRequest: PullRequest
   repository: Repository
   resolvedBy: User
   startDiffSide: DiffSide
   startLine: int
   subjectType: PullRequestReviewThreadSubjectType
   viewerCanReply: bool
   viewerCanResolve: bool
   viewerCanUnresolve: bool

class ProjectV2ItemFieldValueCommon(GQLObject):
   createdAt: DateTime
   creator: Actor
   databaseId: int
   field: ProjectV2FieldConfiguration
   id: ID
   item: ProjectV2Item
   updatedAt: DateTime

class ProjectV2Actor(GQLObject): 
   pass

class ProjectV2ActorEdge(GQLObject):
   cursor: str
   node: ProjectV2Actor

class list_ProjectV2ActorEdge(list, ProjectV2ActorEdge): pass

class list_ProjectV2Actor(list, ProjectV2Actor): pass

class ProjectV2ActorConnection(GQLObject):
   edges: list_ProjectV2ActorEdge[ProjectV2ActorEdge]
   nodes: list_ProjectV2Actor[ProjectV2Actor]
   pageInfo: PageInfo
   totalCount: int

class QYVZS_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class TSWGA_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class ProfileOwner(GQLObject):
   anyPinnableItems: ITKNL_anyPinnableItems_Field
   email: str
   id: ID
   itemShowcase: ProfileItemShowcase
   location: str
   login: str
   name: str
   pinnableItems: QYVZS_PinnableItemConnection_Field
   pinnedItems: TSWGA_PinnableItemConnection_Field
   pinnedItemsRemaining: int
   viewerCanChangePinnedItems: bool
   websiteUrl: URI

class OrganizationOrUser(GQLObject): 
   pass

class MergePullRequestPayload(GQLObject):
   actor: Actor
   clientMutationId: str
   pullRequest: PullRequest

class MarketplaceListingEdge(GQLObject):
   cursor: str
   node: MarketplaceListing

class list_MarketplaceListingEdge(list, MarketplaceListingEdge): pass

class list_MarketplaceListing(list, MarketplaceListing): pass

class MarketplaceListingConnection(GQLObject):
   edges: list_MarketplaceListingEdge[MarketplaceListingEdge]
   nodes: list_MarketplaceListing[MarketplaceListing]
   pageInfo: PageInfo
   totalCount: int

class LockLockablePayload(GQLObject):
   actor: Actor
   clientMutationId: str
   lockedRecord: Lockable

class LinkRepositoryToProjectPayload(GQLObject):
   clientMutationId: str
   project: Project
   repository: Repository

class list_FileDeletion(list, FileDeletion): pass

class list_FileAddition(list, FileAddition): pass

class FileChanges(GQLObject):
   deletions: list_FileDeletion[FileDeletion]
   additions: list_FileAddition[FileAddition]

class EnablePullRequestAutoMergePayload(GQLObject):
   actor: Actor
   clientMutationId: str
   pullRequest: PullRequest

class DisablePullRequestAutoMergePayload(GQLObject):
   actor: Actor
   clientMutationId: str
   pullRequest: PullRequest

class DeletePullRequestReviewCommentPayload(GQLObject):
   clientMutationId: str
   pullRequestReview: PullRequestReview
   pullRequestReviewComment: PullRequestReviewComment

class CreateRepositoryRulesetInput(GQLObject):
   sourceId: ID
   name: str
   target: RepositoryRulesetTarget
   rules: list_RepositoryRuleInput[RepositoryRuleInput]
   conditions: RepositoryRuleConditionsInput
   enforcement: RuleEnforcement
   bypassActors: list_RepositoryRulesetBypassActorInput[RepositoryRulesetBypassActorInput]
   clientMutationId: str

class CreateEnterpriseOrganizationPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   organization: Organization

class CreateCommitOnBranchPayload(GQLObject):
   clientMutationId: str
   commit: Commit
   ref: Ref

class CreateCommitOnBranchInput(GQLObject):
   branch: CommittableBranch
   fileChanges: FileChanges
   message: CommitMessage
   expectedHeadOid: GitObjectID
   clientMutationId: str

class CreateCheckRunInput(GQLObject):
   repositoryId: ID
   name: str
   headSha: GitObjectID
   detailsUrl: URI
   externalId: str
   status: RequestableCheckStatusState
   startedAt: DateTime
   conclusion: CheckConclusionState
   completedAt: DateTime
   output: CheckRunOutput
   actions: list_CheckRunAction[CheckRunAction]
   clientMutationId: str

class Claimable(GQLObject): 
   pass

class CreateAttributionInvitationPayload(GQLObject):
   clientMutationId: str
   owner: Organization
   source: Claimable
   target: Claimable

class MYGQB_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class Comment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyText: str
   createdAt: DateTime
   createdViaEmail: bool
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   lastEditedAt: DateTime
   publishedAt: DateTime
   updatedAt: DateTime
   userContentEdits: MYGQB_UserContentEditConnection_Field
   viewerDidAuthor: bool

class AuditEntry(GQLObject):
   action: str
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime
   operationType: OperationType
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class AddReactionPayload(GQLObject):
   clientMutationId: str
   reaction: Reaction
   reactionGroups: list_ReactionGroup[ReactionGroup]
   subject: Reactable

class AddPullRequestReviewPayload(GQLObject):
   clientMutationId: str
   pullRequestReview: PullRequestReview
   reviewEdge: PullRequestReviewEdge

class list_DraftPullRequestReviewComment(list, DraftPullRequestReviewComment): pass

class list_DraftPullRequestReviewThread(list, DraftPullRequestReviewThread): pass

class AddPullRequestReviewInput(GQLObject):
   pullRequestId: ID
   commitOID: GitObjectID
   body: str
   event: PullRequestReviewEvent
   comments: list_DraftPullRequestReviewComment[DraftPullRequestReviewComment]
   threads: list_DraftPullRequestReviewThread[DraftPullRequestReviewThread]
   clientMutationId: str

class AddPullRequestReviewCommentPayload(GQLObject):
   clientMutationId: str
   comment: PullRequestReviewComment
   commentEdge: PullRequestReviewCommentEdge

class AddProjectColumnPayload(GQLObject):
   clientMutationId: str
   columnEdge: ProjectColumnEdge
   project: Project

class AddProjectCardPayload(GQLObject):
   cardEdge: ProjectCardEdge
   clientMutationId: str
   projectColumn: ProjectColumn

class AddCommentPayload(GQLObject):
   clientMutationId: str
   commentEdge: IssueCommentEdge
   subject: Node
   timelineEdge: IssueTimelineItemEdge

class AcceptEnterpriseAdministratorInvitationPayload(GQLObject):
   clientMutationId: str
   invitation: EnterpriseAdministratorInvitation
   message: str

class AcceptTopicSuggestionPayload(GQLObject):
   clientMutationId: str
   topic: Topic

class AddAssigneesToAssignablePayload(GQLObject):
   assignable: Assignable
   clientMutationId: str

class AddDiscussionCommentPayload(GQLObject):
   clientMutationId: str
   comment: DiscussionComment

class AddDiscussionPollVotePayload(GQLObject):
   clientMutationId: str
   pollOption: DiscussionPollOption

class AddEnterpriseOrganizationMemberPayload(GQLObject):
   clientMutationId: str
   users: list_User[User]

class AddLabelsToLabelablePayload(GQLObject):
   clientMutationId: str
   labelable: Labelable

class AddProjectV2DraftIssuePayload(GQLObject):
   clientMutationId: str
   projectItem: ProjectV2Item

class AddProjectV2ItemByIdPayload(GQLObject):
   clientMutationId: str
   item: ProjectV2Item

class AddPullRequestReviewThreadPayload(GQLObject):
   clientMutationId: str
   thread: PullRequestReviewThread

class ZAKRA_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class Starrable(GQLObject):
   id: ID
   stargazerCount: int
   stargazers: ZAKRA_StargazerConnection_Field
   viewerHasStarred: bool

class AddStarPayload(GQLObject):
   clientMutationId: str
   starrable: Starrable

class AddUpvotePayload(GQLObject):
   clientMutationId: str
   subject: Votable

class AddVerifiableDomainPayload(GQLObject):
   clientMutationId: str
   domain: VerifiableDomain

class ApproveDeploymentsPayload(GQLObject):
   clientMutationId: str
   deployments: list_Deployment[Deployment]

class ApproveVerifiableDomainPayload(GQLObject):
   clientMutationId: str
   domain: VerifiableDomain

class ArchiveProjectV2ItemPayload(GQLObject):
   clientMutationId: str
   item: ProjectV2Item

class ArchiveRepositoryPayload(GQLObject):
   clientMutationId: str
   repository: Repository

class Blob(GQLObject):
   abbreviatedOid: str
   byteSize: int
   commitResourcePath: URI
   commitUrl: URI
   id: ID
   isBinary: bool
   isTruncated: bool
   oid: GitObjectID
   repository: Repository
   text: str

class CancelEnterpriseAdminInvitationPayload(GQLObject):
   clientMutationId: str
   invitation: EnterpriseAdministratorInvitation
   message: str

class CancelSponsorshipPayload(GQLObject):
   clientMutationId: str
   sponsorsTier: SponsorsTier

class ChangeUserStatusPayload(GQLObject):
   clientMutationId: str
   status: UserStatus

class ClearLabelsFromLabelablePayload(GQLObject):
   clientMutationId: str
   labelable: Labelable

class ClearProjectV2ItemFieldValuePayload(GQLObject):
   clientMutationId: str
   projectV2Item: ProjectV2Item

class CloneProjectPayload(GQLObject):
   clientMutationId: str
   jobStatusId: str
   project: Project

class CloneTemplateRepositoryPayload(GQLObject):
   clientMutationId: str
   repository: Repository

class CloseDiscussionPayload(GQLObject):
   clientMutationId: str
   discussion: Discussion

class CloseIssuePayload(GQLObject):
   clientMutationId: str
   issue: Issue

class ClosePullRequestPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest

class Contribution(GQLObject):
   isRestricted: bool
   occurredAt: DateTime
   resourcePath: URI
   url: URI
   user: User

class ConvertProjectCardNoteToIssuePayload(GQLObject):
   clientMutationId: str
   projectCard: ProjectCard

class ConvertPullRequestToDraftPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest

class CopyProjectV2Payload(GQLObject):
   clientMutationId: str
   projectV2: ProjectV2

class list_RequiredStatusCheckInput(list, RequiredStatusCheckInput): pass

class CreateBranchProtectionRuleInput(GQLObject):
   repositoryId: ID
   pattern: str
   requiresApprovingReviews: bool
   requiredApprovingReviewCount: int
   requiresCommitSignatures: bool
   requiresLinearHistory: bool
   blocksCreations: bool
   allowsForcePushes: bool
   allowsDeletions: bool
   isAdminEnforced: bool
   requiresStatusChecks: bool
   requiresStrictStatusChecks: bool
   requiresCodeOwnerReviews: bool
   dismissesStaleReviews: bool
   restrictsReviewDismissals: bool
   reviewDismissalActorIds: list[ID]
   bypassPullRequestActorIds: list[ID]
   bypassForcePushActorIds: list[ID]
   restrictsPushes: bool
   pushActorIds: list[ID]
   requiredStatusCheckContexts: list[str]
   requiredStatusChecks: list_RequiredStatusCheckInput[RequiredStatusCheckInput]
   requiresDeployments: bool
   requiredDeploymentEnvironments: list[str]
   requiresConversationResolution: bool
   requireLastPushApproval: bool
   lockBranch: bool
   lockAllowsFetchAndMerge: bool
   clientMutationId: str

class CreateBranchProtectionRulePayload(GQLObject):
   branchProtectionRule: BranchProtectionRule
   clientMutationId: str

class CreateCheckRunPayload(GQLObject):
   checkRun: CheckRun
   clientMutationId: str

class CreateCheckSuitePayload(GQLObject):
   checkSuite: CheckSuite
   clientMutationId: str

class CreateDiscussionPayload(GQLObject):
   clientMutationId: str
   discussion: Discussion

class CreateEnvironmentPayload(GQLObject):
   clientMutationId: str
   environment: Environment

class CreateIpAllowListEntryPayload(GQLObject):
   clientMutationId: str
   ipAllowListEntry: IpAllowListEntry

class CreateIssuePayload(GQLObject):
   clientMutationId: str
   issue: Issue

class CreateLinkedBranchPayload(GQLObject):
   clientMutationId: str
   linkedBranch: LinkedBranch

class CreateMigrationSourcePayload(GQLObject):
   clientMutationId: str
   migrationSource: MigrationSource

class CreateProjectPayload(GQLObject):
   clientMutationId: str
   project: Project

class list_ProjectV2SingleSelectFieldOptionInput(list, ProjectV2SingleSelectFieldOptionInput): pass

class CreateProjectV2FieldInput(GQLObject):
   projectId: ID
   dataType: ProjectV2CustomFieldType
   name: str
   singleSelectOptions: list_ProjectV2SingleSelectFieldOptionInput[ProjectV2SingleSelectFieldOptionInput]
   clientMutationId: str

class CreateProjectV2FieldPayload(GQLObject):
   clientMutationId: str
   projectV2Field: ProjectV2FieldConfiguration

class CreateProjectV2Payload(GQLObject):
   clientMutationId: str
   projectV2: ProjectV2

class CreatePullRequestPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest

class CreateRefPayload(GQLObject):
   clientMutationId: str
   ref: Ref

class CreateRepositoryPayload(GQLObject):
   clientMutationId: str
   repository: Repository

class CreateRepositoryRulesetPayload(GQLObject):
   clientMutationId: str
   ruleset: RepositoryRuleset

class CreateSponsorsListingPayload(GQLObject):
   clientMutationId: str
   sponsorsListing: SponsorsListing

class CreateSponsorsTierPayload(GQLObject):
   clientMutationId: str
   sponsorsTier: SponsorsTier

class CreateSponsorshipPayload(GQLObject):
   clientMutationId: str
   sponsorship: Sponsorship

class list_BulkSponsorship(list, BulkSponsorship): pass

class CreateSponsorshipsInput(GQLObject):
   sponsorLogin: str
   sponsorships: list_BulkSponsorship[BulkSponsorship]
   receiveEmails: bool
   privacyLevel: SponsorshipPrivacy
   clientMutationId: str

class list_Sponsorable(list, Sponsorable): pass

class CreateSponsorshipsPayload(GQLObject):
   clientMutationId: str
   sponsorables: list_Sponsorable[Sponsorable]

class CreateTeamDiscussionCommentPayload(GQLObject):
   clientMutationId: str
   teamDiscussionComment: TeamDiscussionComment

class CreateTeamDiscussionPayload(GQLObject):
   clientMutationId: str
   teamDiscussion: TeamDiscussion

class DeclineTopicSuggestionPayload(GQLObject):
   clientMutationId: str
   topic: Topic

class DeleteDiscussionCommentPayload(GQLObject):
   clientMutationId: str
   comment: DiscussionComment

class DeleteDiscussionPayload(GQLObject):
   clientMutationId: str
   discussion: Discussion

class DeleteIpAllowListEntryPayload(GQLObject):
   clientMutationId: str
   ipAllowListEntry: IpAllowListEntry

class DeleteIssuePayload(GQLObject):
   clientMutationId: str
   repository: Repository

class DeleteLinkedBranchPayload(GQLObject):
   clientMutationId: str
   issue: Issue

class DeleteProjectCardPayload(GQLObject):
   clientMutationId: str
   column: ProjectColumn
   deletedCardId: ID

class DeleteProjectColumnPayload(GQLObject):
   clientMutationId: str
   deletedColumnId: ID
   project: Project

class DeleteProjectPayload(GQLObject):
   clientMutationId: str
   owner: ProjectOwner

class DeleteProjectV2FieldPayload(GQLObject):
   clientMutationId: str
   projectV2Field: ProjectV2FieldConfiguration

class DeleteProjectV2Payload(GQLObject):
   clientMutationId: str
   projectV2: ProjectV2

class DeleteProjectV2WorkflowPayload(GQLObject):
   clientMutationId: str
   deletedWorkflowId: ID
   projectV2: ProjectV2

class DeletePullRequestReviewPayload(GQLObject):
   clientMutationId: str
   pullRequestReview: PullRequestReview

class DeleteVerifiableDomainPayload(GQLObject):
   clientMutationId: str
   owner: VerifiableDomainOwner

class DequeuePullRequestPayload(GQLObject):
   clientMutationId: str
   mergeQueueEntry: MergeQueueEntry

class DismissPullRequestReviewPayload(GQLObject):
   clientMutationId: str
   pullRequestReview: PullRequestReview

class DismissRepositoryVulnerabilityAlertPayload(GQLObject):
   clientMutationId: str
   repositoryVulnerabilityAlert: RepositoryVulnerabilityAlert

class EnqueuePullRequestPayload(GQLObject):
   clientMutationId: str
   mergeQueueEntry: MergeQueueEntry

class FollowOrganizationPayload(GQLObject):
   clientMutationId: str
   organization: Organization

class FollowUserPayload(GQLObject):
   clientMutationId: str
   user: User

class GpgSignature(GQLObject):
   email: str
   isValid: bool
   keyId: str
   payload: str
   signature: str
   signer: User
   state: GitSignatureState
   wasSignedByGitHub: bool

class RBDXB_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class GrantEnterpriseOrganizationsMigratorRolePayload(GQLObject):
   clientMutationId: str
   organizations: RBDXB_OrganizationConnection_Field

class InviteEnterpriseAdminPayload(GQLObject):
   clientMutationId: str
   invitation: EnterpriseAdministratorInvitation

class LinkProjectV2ToRepositoryPayload(GQLObject):
   clientMutationId: str
   repository: Repository

class LinkProjectV2ToTeamPayload(GQLObject):
   clientMutationId: str
   team: Team

class MarkDiscussionCommentAsAnswerPayload(GQLObject):
   clientMutationId: str
   discussion: Discussion

class MarkFileAsViewedPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest

class MarkProjectV2AsTemplatePayload(GQLObject):
   clientMutationId: str
   projectV2: ProjectV2

class MarkPullRequestReadyForReviewPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest

class TFKER_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class MemberStatusable(GQLObject):
   memberStatuses: TFKER_UserStatusConnection_Field

class MergeBranchPayload(GQLObject):
   clientMutationId: str
   mergeCommit: Commit

class Migration(GQLObject):
   continueOnError: bool
   createdAt: DateTime
   databaseId: str
   failureReason: str
   id: ID
   migrationLogUrl: URI
   migrationSource: MigrationSource
   repositoryName: str
   sourceUrl: URI
   state: MigrationState
   warningsCount: int

class MinimizeCommentPayload(GQLObject):
   clientMutationId: str
   minimizedComment: Minimizable

class MoveProjectCardPayload(GQLObject):
   cardEdge: ProjectCardEdge
   clientMutationId: str

class MoveProjectColumnPayload(GQLObject):
   clientMutationId: str
   columnEdge: ProjectColumnEdge

class OrganizationAuditEntryData(GQLObject):
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI

class SIBNA_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class OrganizationTeamsHovercardContext(GQLObject):
   message: str
   octicon: str
   relevantTeams: SIBNA_TeamConnection_Field
   teamsResourcePath: URI
   teamsUrl: URI
   totalTeamCount: int

class GEHIK_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: OrganizationOrder
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class OrganizationsHovercardContext(GQLObject):
   message: str
   octicon: str
   relevantOrganizations: GEHIK_OrganizationConnection_Field
   totalOrganizationCount: int

class ITDUV_PackageConnection_Field(PackageConnection):
   class PackageConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      names: list[str]
      repositoryId: ID
      packageType: PackageType
      orderBy: PackageOrder

   _args: PackageConnectionArgs



class PackageOwner(GQLObject):
   id: ID
   packages: ITDUV_PackageConnection_Field

class PackageTag(GQLObject):
   id: ID
   name: str
   version: PackageVersion

class PinIssuePayload(GQLObject):
   clientMutationId: str
   issue: Issue

class ProjectV2FieldCommon(GQLObject):
   createdAt: DateTime
   dataType: ProjectV2FieldType
   databaseId: int
   id: ID
   name: str
   project: ProjectV2
   updatedAt: DateTime

class VXXED_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class ProjectV2Recent(GQLObject):
   recentProjects: VXXED_ProjectV2Connection_Field

class PublishSponsorsTierPayload(GQLObject):
   clientMutationId: str
   sponsorsTier: SponsorsTier

class RegenerateEnterpriseIdentityProviderRecoveryCodesPayload(GQLObject):
   clientMutationId: str
   identityProvider: EnterpriseIdentityProvider

class RejectDeploymentsPayload(GQLObject):
   clientMutationId: str
   deployments: list_Deployment[Deployment]

class RemoveAssigneesFromAssignablePayload(GQLObject):
   assignable: Assignable
   clientMutationId: str

class RemoveEnterpriseIdentityProviderPayload(GQLObject):
   clientMutationId: str
   identityProvider: EnterpriseIdentityProvider

class RemoveLabelsFromLabelablePayload(GQLObject):
   clientMutationId: str
   labelable: Labelable

class RemoveOutsideCollaboratorPayload(GQLObject):
   clientMutationId: str
   removedUser: User

class RemoveStarPayload(GQLObject):
   clientMutationId: str
   starrable: Starrable

class RemoveUpvotePayload(GQLObject):
   clientMutationId: str
   subject: Votable

class ReopenDiscussionPayload(GQLObject):
   clientMutationId: str
   discussion: Discussion

class ReopenIssuePayload(GQLObject):
   clientMutationId: str
   issue: Issue

class ReopenPullRequestPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest

class RepositoryAuditEntryData(GQLObject):
   repository: Repository
   repositoryName: str
   repositoryResourcePath: URI
   repositoryUrl: URI

class UDEDR_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionOrder
      repositoryId: ID
      answered: bool
      states: list[NonNull_DiscussionState]

   _args: DiscussionConnectionArgs



class RepositoryDiscussionAuthor(GQLObject):
   repositoryDiscussions: UDEDR_DiscussionConnection_Field

class AQGNF_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class RepositoryDiscussionCommentAuthor(GQLObject):
   repositoryDiscussionComments: AQGNF_DiscussionCommentConnection_Field

class RepositoryNode(GQLObject):
   repository: Repository

class RerequestCheckSuitePayload(GQLObject):
   checkSuite: CheckSuite
   clientMutationId: str

class ResolveReviewThreadPayload(GQLObject):
   clientMutationId: str
   thread: PullRequestReviewThread

class RetireSponsorsTierPayload(GQLObject):
   clientMutationId: str
   sponsorsTier: SponsorsTier

class XJAMA_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class RevokeEnterpriseOrganizationsMigratorRolePayload(GQLObject):
   clientMutationId: str
   organizations: XJAMA_OrganizationConnection_Field

class SetEnterpriseIdentityProviderPayload(GQLObject):
   clientMutationId: str
   identityProvider: EnterpriseIdentityProvider

class SetOrganizationInteractionLimitPayload(GQLObject):
   clientMutationId: str
   organization: Organization

class SetRepositoryInteractionLimitPayload(GQLObject):
   clientMutationId: str
   repository: Repository

class SetUserInteractionLimitPayload(GQLObject):
   clientMutationId: str
   user: User

class SmimeSignature(GQLObject):
   email: str
   isValid: bool
   payload: str
   signature: str
   signer: User
   state: GitSignatureState
   wasSignedByGitHub: bool

class SshSignature(GQLObject):
   email: str
   isValid: bool
   keyFingerprint: str
   payload: str
   signature: str
   signer: User
   state: GitSignatureState
   wasSignedByGitHub: bool

class StartOrganizationMigrationPayload(GQLObject):
   clientMutationId: str
   orgMigration: OrganizationMigration

class StartRepositoryMigrationPayload(GQLObject):
   clientMutationId: str
   repositoryMigration: RepositoryMigration

class SubmitPullRequestReviewPayload(GQLObject):
   clientMutationId: str
   pullRequestReview: PullRequestReview

class TeamAuditEntryData(GQLObject):
   team: Team
   teamName: str
   teamResourcePath: URI
   teamUrl: URI

class TopicAuditEntryData(GQLObject):
   topic: Topic
   topicName: str

class TransferEnterpriseOrganizationPayload(GQLObject):
   clientMutationId: str
   organization: Organization

class TransferIssuePayload(GQLObject):
   clientMutationId: str
   issue: Issue

class UnarchiveProjectV2ItemPayload(GQLObject):
   clientMutationId: str
   item: ProjectV2Item

class UnarchiveRepositoryPayload(GQLObject):
   clientMutationId: str
   repository: Repository

class UnfollowOrganizationPayload(GQLObject):
   clientMutationId: str
   organization: Organization

class UnfollowUserPayload(GQLObject):
   clientMutationId: str
   user: User

class UnknownSignature(GQLObject):
   email: str
   isValid: bool
   payload: str
   signature: str
   signer: User
   state: GitSignatureState
   wasSignedByGitHub: bool

class UnlinkProjectV2FromRepositoryPayload(GQLObject):
   clientMutationId: str
   repository: Repository

class UnlinkProjectV2FromTeamPayload(GQLObject):
   clientMutationId: str
   team: Team

class UnmarkDiscussionCommentAsAnswerPayload(GQLObject):
   clientMutationId: str
   discussion: Discussion

class UnmarkFileAsViewedPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest

class UnmarkIssueAsDuplicatePayload(GQLObject):
   clientMutationId: str
   duplicate: IssueOrPullRequest

class UnmarkProjectV2AsTemplatePayload(GQLObject):
   clientMutationId: str
   projectV2: ProjectV2

class UnminimizeCommentPayload(GQLObject):
   clientMutationId: str
   unminimizedComment: Minimizable

class UnpinIssuePayload(GQLObject):
   clientMutationId: str
   issue: Issue

class UnresolveReviewThreadPayload(GQLObject):
   clientMutationId: str
   thread: PullRequestReviewThread

class UpdateBranchProtectionRuleInput(GQLObject):
   branchProtectionRuleId: ID
   pattern: str
   requiresApprovingReviews: bool
   requiredApprovingReviewCount: int
   requiresCommitSignatures: bool
   requiresLinearHistory: bool
   blocksCreations: bool
   allowsForcePushes: bool
   allowsDeletions: bool
   isAdminEnforced: bool
   requiresStatusChecks: bool
   requiresStrictStatusChecks: bool
   requiresCodeOwnerReviews: bool
   dismissesStaleReviews: bool
   restrictsReviewDismissals: bool
   reviewDismissalActorIds: list[ID]
   bypassPullRequestActorIds: list[ID]
   bypassForcePushActorIds: list[ID]
   restrictsPushes: bool
   pushActorIds: list[ID]
   requiredStatusCheckContexts: list[str]
   requiredStatusChecks: list_RequiredStatusCheckInput[RequiredStatusCheckInput]
   requiresDeployments: bool
   requiredDeploymentEnvironments: list[str]
   requiresConversationResolution: bool
   requireLastPushApproval: bool
   lockBranch: bool
   lockAllowsFetchAndMerge: bool
   clientMutationId: str

class UpdateBranchProtectionRulePayload(GQLObject):
   branchProtectionRule: BranchProtectionRule
   clientMutationId: str

class UpdateCheckRunPayload(GQLObject):
   checkRun: CheckRun
   clientMutationId: str

class list_CheckSuiteAutoTriggerPreference(list, CheckSuiteAutoTriggerPreference): pass

class UpdateCheckSuitePreferencesInput(GQLObject):
   repositoryId: ID
   autoTriggerPreferences: list_CheckSuiteAutoTriggerPreference[CheckSuiteAutoTriggerPreference]
   clientMutationId: str

class UpdateCheckSuitePreferencesPayload(GQLObject):
   clientMutationId: str
   repository: Repository

class UpdateDiscussionCommentPayload(GQLObject):
   clientMutationId: str
   comment: DiscussionComment

class UpdateDiscussionPayload(GQLObject):
   clientMutationId: str
   discussion: Discussion

class UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseDefaultRepositoryPermissionSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseMembersCanDeleteIssuesSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseMembersCanMakePurchasesSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseOrganizationProjectsSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseProfilePayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise

class UpdateEnterpriseRepositoryProjectsSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseTeamDiscussionsSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   message: str

class UpdateEnvironmentPayload(GQLObject):
   clientMutationId: str
   environment: Environment

class UpdateIpAllowListEnabledSettingPayload(GQLObject):
   clientMutationId: str
   owner: IpAllowListOwner

class UpdateIpAllowListEntryPayload(GQLObject):
   clientMutationId: str
   ipAllowListEntry: IpAllowListEntry

class UpdateIpAllowListForInstalledAppsEnabledSettingPayload(GQLObject):
   clientMutationId: str
   owner: IpAllowListOwner

class UpdateIssueCommentPayload(GQLObject):
   clientMutationId: str
   issueComment: IssueComment

class UpdateNotificationRestrictionSettingPayload(GQLObject):
   clientMutationId: str
   owner: VerifiableDomainOwner

class UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload(GQLObject):
   clientMutationId: str
   message: str
   organization: Organization

class UpdateOrganizationWebCommitSignoffSettingPayload(GQLObject):
   clientMutationId: str
   message: str
   organization: Organization

class UpdateProjectCardPayload(GQLObject):
   clientMutationId: str
   projectCard: ProjectCard

class UpdateProjectColumnPayload(GQLObject):
   clientMutationId: str
   projectColumn: ProjectColumn

class UpdateProjectPayload(GQLObject):
   clientMutationId: str
   project: Project

class list_ProjectV2Collaborator(list, ProjectV2Collaborator): pass

class UpdateProjectV2CollaboratorsInput(GQLObject):
   projectId: ID
   collaborators: list_ProjectV2Collaborator[ProjectV2Collaborator]
   clientMutationId: str

class UOQNF_ProjectV2ActorConnection_Field(ProjectV2ActorConnection):
   class ProjectV2ActorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ActorConnectionArgs



class UpdateProjectV2CollaboratorsPayload(GQLObject):
   clientMutationId: str
   collaborators: UOQNF_ProjectV2ActorConnection_Field

class UpdateProjectV2DraftIssuePayload(GQLObject):
   clientMutationId: str
   draftIssue: DraftIssue

class UpdateProjectV2ItemFieldValueInput(GQLObject):
   projectId: ID
   itemId: ID
   fieldId: ID
   value: ProjectV2FieldValue
   clientMutationId: str

class UpdateProjectV2ItemFieldValuePayload(GQLObject):
   clientMutationId: str
   projectV2Item: ProjectV2Item

class FDXNO_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class UpdateProjectV2ItemPositionPayload(GQLObject):
   clientMutationId: str
   items: FDXNO_ProjectV2ItemConnection_Field

class UpdateProjectV2Payload(GQLObject):
   clientMutationId: str
   projectV2: ProjectV2

class UpdatePullRequestBranchPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest

class UpdatePullRequestReviewCommentPayload(GQLObject):
   clientMutationId: str
   pullRequestReviewComment: PullRequestReviewComment

class UpdatePullRequestReviewPayload(GQLObject):
   clientMutationId: str
   pullRequestReview: PullRequestReview

class UpdateRefPayload(GQLObject):
   clientMutationId: str
   ref: Ref

class UpdateRepositoryPayload(GQLObject):
   clientMutationId: str
   repository: Repository

class UpdateRepositoryRulesetPayload(GQLObject):
   clientMutationId: str
   ruleset: RepositoryRuleset

class UpdateRepositoryWebCommitSignoffSettingPayload(GQLObject):
   clientMutationId: str
   message: str
   repository: Repository

class UpdateSponsorshipPreferencesPayload(GQLObject):
   clientMutationId: str
   sponsorship: Sponsorship

class UpdateSubscriptionPayload(GQLObject):
   clientMutationId: str
   subscribable: Subscribable

class UpdateTeamDiscussionCommentPayload(GQLObject):
   clientMutationId: str
   teamDiscussionComment: TeamDiscussionComment

class UpdateTeamDiscussionPayload(GQLObject):
   clientMutationId: str
   teamDiscussion: TeamDiscussion

class UpdateTopicsPayload(GQLObject):
   clientMutationId: str
   invalidTopicNames: list[str]
   repository: Repository

class VerifyVerifiableDomainPayload(GQLObject):
   clientMutationId: str
   domain: VerifiableDomain

class ViewerHovercardContext(GQLObject):
   message: str
   octicon: str
   viewer: User
