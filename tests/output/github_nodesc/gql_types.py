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
   teamIds: NonNull_list[ID]
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
   viewerCannotUpdateReasons: CommentCannotUpdateReason

class UnresolveReviewThreadInput(GQLObject):
   threadId: ID
   clientMutationId: str

class UnminimizeCommentInput(GQLObject):
   subjectId: ID
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

class RequestReviewsInput(GQLObject):
   pullRequestId: ID
   userIds: list[ID]
   teamIds: list[ID]
   union: bool
   clientMutationId: str

class RepositoryMigrationOrder(GQLObject):
   field: RepositoryMigrationOrderField
   direction: RepositoryMigrationOrderDirection

class RepositoryInteractionAbility(GQLObject):
   expiresAt: DateTime
   limit: RepositoryInteractionLimit
   origin: RepositoryInteractionLimitOrigin

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

class ReactionOrder(GQLObject):
   field: ReactionOrderField
   direction: OrderDirection

class PullRequestOrder(GQLObject):
   field: PullRequestOrderField
   direction: OrderDirection

class PublishSponsorsTierInput(GQLObject):
   tierId: ID
   clientMutationId: str

class ProjectV2ViewOrder(GQLObject):
   field: ProjectV2ViewOrderField
   direction: OrderDirection

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

class DeleteRefInput(GQLObject):
   refId: ID
   clientMutationId: str

class DeletePullRequestReviewCommentInput(GQLObject):
   id: ID
   clientMutationId: str

class DeleteProjectV2ItemInput(GQLObject):
   projectId: ID
   itemId: ID
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
   adminLogins: NonNull_list[str]
   clientMutationId: str

class CreateCheckSuiteInput(GQLObject):
   repositoryId: ID
   headSha: GitObjectID
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

class CommitMessage(GQLObject):
   headline: str
   body: str

class CommitAuthor(GQLObject):
   id: ID
   emails: list[str]

class ClosePullRequestInput(GQLObject):
   pullRequestId: ID
   clientMutationId: str

class Closable(GQLObject):
   closed: bool
   closedAt: DateTime

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

class Bot(GQLObject):
   avatarUrl: LYBCE_URI_Field
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

class AcceptTopicSuggestionInput(GQLObject):
   repositoryId: ID
   name: str
   clientMutationId: str

class AbortQueuedMigrationsPayload(GQLObject):
   clientMutationId: str
   success: bool

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
   avatarUrl: EUZPS_URI_Field
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

class XHITR_ReactionConnection_Field(ReactionConnection):
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
   reactions: XHITR_ReactionConnection_Field
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

class BHTMX_ReactorConnection_Field(ReactorConnection):
   class ReactorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ReactorConnectionArgs



class ReactionGroup(GQLObject):
   content: ReactionContent
   createdAt: DateTime
   reactors: BHTMX_ReactorConnection_Field
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

class EUCKB_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class FTMKE_UserContentEditConnection_Field(UserContentEditConnection):
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
   reactions: EUCKB_ReactionConnection_Field
   resourcePath: URI
   updatedAt: DateTime
   url: URI
   userContentEdits: FTMKE_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanReact: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: CommentCannotUpdateReason
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

class MDSEN_TeamDiscussionCommentConnection_Field(TeamDiscussionCommentConnection):
   class TeamDiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: TeamDiscussionCommentOrder
      fromComment: int

   _args: TeamDiscussionCommentConnectionArgs



class ANYDB_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class EFIED_UserContentEditConnection_Field(UserContentEditConnection):
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
   comments: MDSEN_TeamDiscussionCommentConnection_Field
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
   reactions: ANYDB_ReactionConnection_Field
   resourcePath: URI
   team: NewType('Team', GQLObject) ## Circular Reference for Team
   title: str
   updatedAt: DateTime
   url: URI
   userContentEdits: EFIED_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanPin: bool
   viewerCanReact: bool
   viewerCanSubscribe: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: CommentCannotUpdateReason
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

class ProjectV2IterationFieldConfiguration(GQLObject):
   completedIterations: ProjectV2IterationFieldIteration
   duration: int
   iterations: ProjectV2IterationFieldIteration
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

class ProjectV2SingleSelectField(GQLObject):
   createdAt: DateTime
   dataType: ProjectV2FieldType
   databaseId: int
   id: ID
   name: str
   options: ProjectV2SingleSelectFieldOption
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

class WITJC_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class RUOCS_ProjectV2ItemConnection_Field(Generic[ProjectV2ItemConnection]):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class IFPTR_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class DraftIssue(GQLObject):
   assignees: WITJC_UserConnection_Field
   body: str
   bodyHTML: HTML
   bodyText: str
   createdAt: DateTime
   creator: Actor
   id: ID
   projectV2Items: RUOCS_ProjectV2ItemConnection_Field ## Circular Reference for ProjectV2ItemConnection
   projectsV2: IFPTR_ProjectV2Connection_Field
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

class RepositoryCodeowners(GQLObject):
   errors: RepositoryCodeownersError

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

class AREUH_DeploymentStatusConnection_Field(DeploymentStatusConnection):
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
   statuses: AREUH_DeploymentStatusConnection_Field
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

class RAEMU_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class UHPAH_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DiscussionCommentConnectionArgs



class RUSQO_UserContentEditConnection_Field(UserContentEditConnection):
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
   reactions: RAEMU_ReactionConnection_Field
   replies: UHPAH_DiscussionCommentConnection_Field
   replyTo: NewType('DiscussionComment', GQLObject) ## Circular Reference for DiscussionComment
   resourcePath: URI
   updatedAt: DateTime
   upvoteCount: int
   url: URI
   userContentEdits: RUSQO_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanMarkAsAnswer: bool
   viewerCanMinimize: bool
   viewerCanReact: bool
   viewerCanUnmarkAsAnswer: bool
   viewerCanUpdate: bool
   viewerCanUpvote: bool
   viewerCannotUpdateReasons: CommentCannotUpdateReason
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

class LIFCC_IssueConnection_Field(IssueConnection):
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

class EHOAV_PullRequestConnection_Field(Generic[PullRequestConnection]):
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
   issues: LIFCC_IssueConnection_Field
   name: str
   pullRequests: EHOAV_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
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

class RESZZ_DiscussionPollOptionConnection_Field(DiscussionPollOptionConnection):
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
   options: RESZZ_DiscussionPollOptionConnection_Field
   question: str
   totalVoteCount: int
   viewerCanVote: bool
   viewerHasVoted: bool

class OEDUS_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DiscussionCommentConnectionArgs



class FXFVF_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class ZQTED_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class QIFXR_UserContentEditConnection_Field(UserContentEditConnection):
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
   comments: OEDUS_DiscussionCommentConnection_Field
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   labels: FXFVF_LabelConnection_Field
   lastEditedAt: DateTime
   locked: bool
   number: int
   poll: DiscussionPoll
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: ZQTED_ReactionConnection_Field
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   resourcePath: URI
   title: str
   updatedAt: DateTime
   upvoteCount: int
   url: URI
   userContentEdits: QIFXR_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanReact: bool
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

class EOGSZ_DeploymentReviewerConnection_Field(DeploymentReviewerConnection):
   class DeploymentReviewerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewerConnectionArgs



class DeploymentProtectionRule(GQLObject):
   databaseId: int
   reviewers: EOGSZ_DeploymentReviewerConnection_Field
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

class JKIDK_DeploymentProtectionRuleConnection_Field(DeploymentProtectionRuleConnection):
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
   protectionRules: JKIDK_DeploymentProtectionRuleConnection_Field

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

class GRNKN_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class LUUCD_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class SUQJU_ReleaseAssetConnection_Field(ReleaseAssetConnection):
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
   mentions: GRNKN_UserConnection_Field
   name: str
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: LUUCD_ReactionConnection_Field
   releaseAssets: SUQJU_ReleaseAssetConnection_Field
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   resourcePath: URI
   shortDescriptionHTML: VVAIP_HTML_Field
   tag: NewType('Ref', GQLObject) ## Circular Reference for Ref
   tagCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   tagName: str
   updatedAt: DateTime
   url: URI
   viewerCanReact: bool

class License(GQLObject):
   body: str
   conditions: LicenseRule
   description: str
   featured: bool
   hidden: bool
   id: ID
   implementation: str
   key: str
   limitations: LicenseRule
   name: str
   nickname: str
   permissions: LicenseRule
   pseudoLicense: bool
   spdxId: str
   url: URI

class VFUJS_IssueConnection_Field(IssueConnection):
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



class VAPJZ_PullRequestConnection_Field(Generic[PullRequestConnection]):
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
   issues: VFUJS_IssueConnection_Field
   number: int
   progressPercentage: float
   pullRequests: VAPJZ_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   resourcePath: URI
   state: MilestoneState
   title: str
   updatedAt: DateTime
   url: URI

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

class RPFQR_RepositoryConnection_Field(RepositoryConnection):
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



class WUARD_Repository_Field(Generic[Repository]):
   class RepositoryArgs(GQLArgsSet, GQLObject):
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs



class RepositoryOwner(GQLObject):
   avatarUrl: EFOOO_URI_Field
   id: ID
   login: str
   repositories: RPFQR_RepositoryConnection_Field
   repository: WUARD_Repository_Field ## Circular Reference for Repository
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

class WPKGC_PackageFileConnection_Field(PackageFileConnection):
   class PackageFileConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: PackageFileOrder
      after: str
      before: str
      first: int
      last: int

   _args: PackageFileConnectionArgs



class PackageVersion(GQLObject):
   files: WPKGC_PackageFileConnection_Field
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

class DUYCS_PackageVersion_Field(PackageVersion):
   class PackageVersionArgs(GQLArgsSet, GQLObject):
      version: NonNull_str

   _args: PackageVersionArgs



class YYKLU_PackageVersionConnection_Field(PackageVersionConnection):
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
   version: DUYCS_PackageVersion_Field
   versions: YYKLU_PackageVersionConnection_Field

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
   gradientStopColors: str
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

class NUAGK_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: ProjectCardConnectionArgs



class ProjectColumn(GQLObject):
   cards: NUAGK_ProjectCardConnection_Field
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

class BJGVO_Project_Field(Generic[Project]):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class NonNull_ProjectState(GQLObject): pass

class MMTUT_ProjectConnection_Field(ProjectConnection):
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
   project: BJGVO_Project_Field ## Circular Reference for Project
   projects: MMTUT_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   viewerCanCreateProjects: bool

class LRBFK_ProjectColumnConnection_Field(ProjectColumnConnection):
   class ProjectColumnConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectColumnConnectionArgs



class IGITZ_ProjectCardConnection_Field(ProjectCardConnection):
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
   columns: LRBFK_ProjectColumnConnection_Field
   createdAt: DateTime
   creator: Actor
   databaseId: int
   id: ID
   name: str
   number: int
   owner: ProjectOwner
   pendingCards: IGITZ_ProjectCardConnection_Field
   progress: ProjectProgress
   resourcePath: URI
   state: ProjectState
   updatedAt: DateTime
   url: URI
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

class LNPID_Topic_Field(Generic[Topic]):
   class TopicArgs(GQLArgsSet, GQLObject):
      first: int

   _args: TopicArgs



class IDHHW_RepositoryConnection_Field(RepositoryConnection):
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



class SSXHF_StargazerConnection_Field(StargazerConnection):
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
   relatedTopics: LNPID_Topic_Field ## Circular Reference for Topic
   repositories: IDHHW_RepositoryConnection_Field
   stargazerCount: int
   stargazers: SSXHF_StargazerConnection_Field
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

class CIIDD_CWEConnection_Field(CWEConnection):
   class CWEConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CWEConnectionArgs



class NonNull_SecurityAdvisorySeverity(GQLObject): pass

class NonNull_SecurityAdvisoryClassification(GQLObject): pass

class MXINA_SecurityVulnerabilityConnection_Field(SecurityVulnerabilityConnection):
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
   cwes: CIIDD_CWEConnection_Field
   databaseId: int
   description: str
   ghsaId: str
   id: ID
   identifiers: SecurityAdvisoryIdentifier
   notificationsPermalink: URI
   origin: str
   permalink: URI
   publishedAt: DateTime
   references: SecurityAdvisoryReference
   severity: SecurityAdvisorySeverity
   summary: str
   updatedAt: DateTime
   vulnerabilities: MXINA_SecurityVulnerabilityConnection_Field
   withdrawnAt: DateTime

class RepositoryVulnerabilityAlert(GQLObject):
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

class PGJJT_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class TUQEK_BranchProtectionRuleConnection_Field(BranchProtectionRuleConnection):
   class BranchProtectionRuleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BranchProtectionRuleConnectionArgs



class RIJRO_RepositoryCodeowners_Field(RepositoryCodeowners):
   class RepositoryCodeownersArgs(GQLArgsSet, GQLObject):
      refName: str

   _args: RepositoryCodeownersArgs



class VIIED_RepositoryCollaboratorConnection_Field(RepositoryCollaboratorConnection):
   class RepositoryCollaboratorConnectionArgs(GQLArgsSet, GQLObject):
      affiliation: CollaboratorAffiliation
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryCollaboratorConnectionArgs



class KOLAN_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class list_RepositoryContactLink(list, RepositoryContactLink): pass

class YGRIE_DeployKeyConnection_Field(DeployKeyConnection):
   class DeployKeyConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeployKeyConnectionArgs



class QKHPX_DeploymentConnection_Field(DeploymentConnection):
   class DeploymentConnectionArgs(GQLArgsSet, GQLObject):
      environments: list[NonNull_str]
      orderBy: DeploymentOrder
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentConnectionArgs



class EPNUI_Discussion_Field(Discussion):
   class DiscussionArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: DiscussionArgs



class FUSKN_DiscussionCategoryConnection_Field(DiscussionCategoryConnection):
   class DiscussionCategoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      filterByAssignable: bool

   _args: DiscussionCategoryConnectionArgs



class SOWZF_DiscussionCategory_Field(DiscussionCategory):
   class DiscussionCategoryArgs(GQLArgsSet, GQLObject):
      slug: NonNull_str

   _args: DiscussionCategoryArgs



class AZXFP_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      categoryId: ID
      orderBy: DiscussionOrder

   _args: DiscussionConnectionArgs



class KRHEA_Environment_Field(Environment):
   class EnvironmentArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: EnvironmentArgs



class BDKIM_EnvironmentConnection_Field(EnvironmentConnection):
   class EnvironmentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: EnvironmentConnectionArgs



class UMOAT_RepositoryConnection_Field(RepositoryConnection):
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



class YMGHX_Issue_Field(Generic[Issue]):
   class IssueArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: IssueArgs



class ABHVH_IssueOrPullRequest_Field(IssueOrPullRequest):
   class IssueOrPullRequestArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: IssueOrPullRequestArgs



class list_IssueTemplate(list, IssueTemplate): pass

class OXDRW_IssueConnection_Field(IssueConnection):
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



class KMPHG_Label_Field(Label):
   class LabelArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: LabelArgs



class YLRBB_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int
      query: str

   _args: LabelConnectionArgs



class CBJVM_LanguageConnection_Field(LanguageConnection):
   class LanguageConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: LanguageOrder

   _args: LanguageConnectionArgs



class OXWAA_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class CPCCU_Milestone_Field(Milestone):
   class MilestoneArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: MilestoneArgs



class NonNull_MilestoneState(GQLObject): pass

class PGPMI_MilestoneConnection_Field(MilestoneConnection):
   class MilestoneConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      states: list[NonNull_MilestoneState]
      orderBy: MilestoneOrder
      query: str

   _args: MilestoneConnectionArgs



class UWBVP_GitObject_Field(GitObject):
   class GitObjectArgs(GQLArgsSet, GQLObject):
      oid: GitObjectID
      expression: str

   _args: GitObjectArgs



class XCKEE_PackageConnection_Field(PackageConnection):
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



class RWLET_PinnedDiscussionConnection_Field(PinnedDiscussionConnection):
   class PinnedDiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PinnedDiscussionConnectionArgs



class UGFTT_PinnedIssueConnection_Field(PinnedIssueConnection):
   class PinnedIssueConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PinnedIssueConnectionArgs



class SVXNN_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class OTZSD_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class LLXOF_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: ProjectOrder
      search: str
      states: list[NonNull_ProjectState]
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class QJXUK_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: ProjectV2Order

   _args: ProjectV2ConnectionArgs



class HDLMC_PullRequest_Field(Generic[PullRequest]):
   class PullRequestArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: PullRequestArgs



class list_PullRequestTemplate(list, PullRequestTemplate): pass

class NOWVN_PullRequestConnection_Field(Generic[PullRequestConnection]):
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



class KIZQN_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class GHVCI_Ref_Field(Generic[Ref]):
   class RefArgs(GQLArgsSet, GQLObject):
      qualifiedName: NonNull_str

   _args: RefArgs



class OMGGK_RefConnection_Field(RefConnection):
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



class BBYFM_Release_Field(Release):
   class ReleaseArgs(GQLArgsSet, GQLObject):
      tagName: NonNull_str

   _args: ReleaseArgs



class MFVPL_ReleaseConnection_Field(ReleaseConnection):
   class ReleaseConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ReleaseOrder

   _args: ReleaseConnectionArgs



class EQYIH_RepositoryTopicConnection_Field(RepositoryTopicConnection):
   class RepositoryTopicConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryTopicConnectionArgs



class AHPTQ_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class DCLUN_SubmoduleConnection_Field(SubmoduleConnection):
   class SubmoduleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: SubmoduleConnectionArgs



class NonNull_RepositoryVulnerabilityAlertState(GQLObject): pass

class NonNull_RepositoryVulnerabilityAlertDependencyScope(GQLObject): pass

class CANGU_RepositoryVulnerabilityAlertConnection_Field(RepositoryVulnerabilityAlertConnection):
   class RepositoryVulnerabilityAlertConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      states: list[NonNull_RepositoryVulnerabilityAlertState]
      dependencyScopes: list[NonNull_RepositoryVulnerabilityAlertDependencyScope]

   _args: RepositoryVulnerabilityAlertConnectionArgs



class LWCUG_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class Repository(GQLObject):
   allowUpdateBranch: bool
   assignableUsers: PGJJT_UserConnection_Field
   autoMergeAllowed: bool
   branchProtectionRules: TUQEK_BranchProtectionRuleConnection_Field
   codeOfConduct: CodeOfConduct
   codeowners: RIJRO_RepositoryCodeowners_Field
   collaborators: VIIED_RepositoryCollaboratorConnection_Field
   commitComments: KOLAN_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
   contactLinks: list_RepositoryContactLink[RepositoryContactLink]
   createdAt: DateTime
   databaseId: int
   defaultBranchRef: NewType('Ref', GQLObject) ## Circular Reference for Ref
   deleteBranchOnMerge: bool
   deployKeys: YGRIE_DeployKeyConnection_Field
   deployments: QKHPX_DeploymentConnection_Field
   description: str
   descriptionHTML: HTML
   discussion: EPNUI_Discussion_Field
   discussionCategories: FUSKN_DiscussionCategoryConnection_Field
   discussionCategory: SOWZF_DiscussionCategory_Field
   discussions: AZXFP_DiscussionConnection_Field
   diskUsage: int
   environment: KRHEA_Environment_Field
   environments: BDKIM_EnvironmentConnection_Field
   forkCount: int
   forkingAllowed: bool
   forks: UMOAT_RepositoryConnection_Field
   fundingLinks: FundingLink
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
   issue: YMGHX_Issue_Field ## Circular Reference for Issue
   issueOrPullRequest: ABHVH_IssueOrPullRequest_Field
   issueTemplates: list_IssueTemplate[IssueTemplate]
   issues: OXDRW_IssueConnection_Field
   label: KMPHG_Label_Field
   labels: YLRBB_LabelConnection_Field
   languages: CBJVM_LanguageConnection_Field
   latestRelease: Release
   licenseInfo: License
   lockReason: RepositoryLockReason
   mentionableUsers: OXWAA_UserConnection_Field
   mergeCommitAllowed: bool
   mergeCommitMessage: MergeCommitMessage
   mergeCommitTitle: MergeCommitTitle
   milestone: CPCCU_Milestone_Field
   milestones: PGPMI_MilestoneConnection_Field
   mirrorUrl: URI
   name: str
   nameWithOwner: str
   object: UWBVP_GitObject_Field
   openGraphImageUrl: URI
   owner: RepositoryOwner
   packages: XCKEE_PackageConnection_Field
   parent: NewType('Repository', GQLObject) ## Circular Reference for Repository
   pinnedDiscussions: RWLET_PinnedDiscussionConnection_Field
   pinnedIssues: UGFTT_PinnedIssueConnection_Field
   primaryLanguage: Language
   project: SVXNN_Project_Field
   projectV2: OTZSD_ProjectV2_Field ## Circular Reference for ProjectV2
   projects: LLXOF_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   projectsV2: QJXUK_ProjectV2Connection_Field
   pullRequest: HDLMC_PullRequest_Field ## Circular Reference for PullRequest
   pullRequestTemplates: list_PullRequestTemplate[PullRequestTemplate]
   pullRequests: NOWVN_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   pushedAt: DateTime
   rebaseMergeAllowed: bool
   recentProjects: KIZQN_ProjectV2Connection_Field
   ref: GHVCI_Ref_Field ## Circular Reference for Ref
   refs: OMGGK_RefConnection_Field
   release: BBYFM_Release_Field
   releases: MFVPL_ReleaseConnection_Field
   repositoryTopics: EQYIH_RepositoryTopicConnection_Field
   resourcePath: URI
   securityPolicyUrl: URI
   shortDescriptionHTML: JSVHZ_HTML_Field
   squashMergeAllowed: bool
   squashMergeCommitMessage: SquashMergeCommitMessage
   squashMergeCommitTitle: SquashMergeCommitTitle
   sshUrl: GitSSHRemote
   stargazerCount: int
   stargazers: AHPTQ_StargazerConnection_Field
   submodules: DCLUN_SubmoduleConnection_Field
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
   vulnerabilityAlerts: CANGU_RepositoryVulnerabilityAlertConnection_Field
   watchers: LWCUG_UserConnection_Field
   webCommitSignoffRequired: bool

class WFMJA_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class RKBZJ_UserContentEditConnection_Field(UserContentEditConnection):
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
   id: ID
   includesCreatedEdit: bool
   isMinimized: bool
   issue: NewType('Issue', GQLObject) ## Circular Reference for Issue
   lastEditedAt: DateTime
   minimizedReason: str
   publishedAt: DateTime
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: WFMJA_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   updatedAt: DateTime
   url: URI
   userContentEdits: RKBZJ_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanMinimize: bool
   viewerCanReact: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: CommentCannotUpdateReason
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

class Hovercard(GQLObject):
   contexts: HovercardContext

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

class NGMIZ_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class Assignable(GQLObject):
   assignees: NGMIZ_UserConnection_Field

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

class EQCNX_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class Labelable(GQLObject):
   labels: EQCNX_LabelConnection_Field

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

class WFYCH_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class KIHBZ_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class OFVZY_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject):
      includeNotificationContexts: bool

   _args: HovercardArgs



class UXIHV_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class TUIAD_LinkedBranchConnection_Field(LinkedBranchConnection):
   class LinkedBranchConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: LinkedBranchConnectionArgs



class IWUSW_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class ROEMF_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: ProjectCardConnectionArgs



class XTYDD_ProjectV2ItemConnection_Field(Generic[ProjectV2ItemConnection]):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class VSCZH_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class RNQOI_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class IIOXS_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class NonNull_IssueTimelineItemsItemType(GQLObject): pass

class OLVDU_IssueTimelineItemsConnection_Field(IssueTimelineItemsConnection):
   class IssueTimelineItemsConnectionArgs(GQLArgsSet, GQLObject):
      since: DateTime
      skip: int
      itemTypes: list[NonNull_IssueTimelineItemsItemType]
      after: str
      before: str
      first: int
      last: int

   _args: IssueTimelineItemsConnectionArgs



class SSGKH_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class BWTIH_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class AEXVC_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class Issue(GQLObject):
   activeLockReason: LockReason
   assignees: WFYCH_UserConnection_Field
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyResourcePath: URI
   bodyText: str
   bodyUrl: URI
   closed: bool
   closedAt: DateTime
   comments: KIHBZ_IssueCommentConnection_Field
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   hovercard: OFVZY_Hovercard_Field
   id: ID
   includesCreatedEdit: bool
   isPinned: bool
   isReadByViewer: bool
   labels: UXIHV_LabelConnection_Field
   lastEditedAt: DateTime
   linkedBranches: TUIAD_LinkedBranchConnection_Field
   locked: bool
   milestone: Milestone
   number: int
   participants: IWUSW_UserConnection_Field
   projectCards: ROEMF_ProjectCardConnection_Field
   projectItems: XTYDD_ProjectV2ItemConnection_Field ## Circular Reference for ProjectV2ItemConnection
   projectV2: VSCZH_ProjectV2_Field ## Circular Reference for ProjectV2
   projectsV2: RNQOI_ProjectV2Connection_Field
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: IIOXS_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   state: IssueState
   stateReason: IssueStateReason
   timelineItems: OLVDU_IssueTimelineItemsConnection_Field
   title: str
   titleHTML: str
   trackedInIssues: SSGKH_IssueConnection_Field
   trackedIssues: BWTIH_IssueConnection_Field
   trackedIssuesCount: GKPSH_trackedIssuesCount_Field
   updatedAt: DateTime
   url: URI
   userContentEdits: AEXVC_UserContentEditConnection_Field
   viewerCanReact: bool
   viewerCanSubscribe: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: CommentCannotUpdateReason
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

class GLLFX_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class ProjectV2ItemFieldLabelValue(GQLObject):
   field: ProjectV2FieldConfiguration
   labels: GLLFX_LabelConnection_Field

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

class KTIQR_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: PullRequestOrder

   _args: PullRequestConnectionArgs



class ProjectV2ItemFieldPullRequestValue(GQLObject):
   field: ProjectV2FieldConfiguration
   pullRequests: KTIQR_PullRequestConnection_Field ## Circular Reference for PullRequestConnection

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

class CKNHX_RequestedReviewerConnection_Field(RequestedReviewerConnection):
   class RequestedReviewerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: RequestedReviewerConnectionArgs



class ProjectV2ItemFieldReviewerValue(GQLObject):
   field: ProjectV2FieldConfiguration
   reviewers: CKNHX_RequestedReviewerConnection_Field

class ProjectV2ItemFieldSingleSelectValue(GQLObject):
   createdAt: DateTime
   creator: Actor
   databaseId: int
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

class VIQZZ_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class ProjectV2ItemFieldUserValue(GQLObject):
   field: ProjectV2FieldConfiguration
   users: VIQZZ_UserConnection_Field

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

class NYUNT_ProjectV2ItemFieldValue_Field(ProjectV2ItemFieldValue):
   class ProjectV2ItemFieldValueArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: ProjectV2ItemFieldValueArgs



class VMOSM_ProjectV2ItemFieldValueConnection_Field(ProjectV2ItemFieldValueConnection):
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
   fieldValueByName: NYUNT_ProjectV2ItemFieldValue_Field
   fieldValues: VMOSM_ProjectV2ItemFieldValueConnection_Field
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

class BXUMT_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class AOIUB_ProjectV2Connection_Field(ProjectV2Connection):
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
   projectV2: BXUMT_ProjectV2_Field ## Circular Reference for ProjectV2
   projectsV2: AOIUB_ProjectV2Connection_Field

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

class QZZHS_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class ZXGRM_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class VCKYJ_ProjectV2SortByFieldConnection_Field(ProjectV2SortByFieldConnection):
   class ProjectV2SortByFieldConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2SortByFieldConnectionArgs



class QXJDM_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
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
   fields: QZZHS_ProjectV2FieldConfigurationConnection_Field
   filter: str
   groupByFields: ZXGRM_ProjectV2FieldConfigurationConnection_Field
   id: ID
   layout: ProjectV2ViewLayout
   name: str
   number: int
   project: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2
   sortByFields: VCKYJ_ProjectV2SortByFieldConnection_Field
   updatedAt: DateTime
   verticalGroupByFields: QXJDM_ProjectV2FieldConfigurationConnection_Field

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

class LBPGK_ProjectV2FieldConfiguration_Field(ProjectV2FieldConfiguration):
   class ProjectV2FieldConfigurationArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: ProjectV2FieldConfigurationArgs



class ECCCS_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class MHZBW_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ItemOrder

   _args: ProjectV2ItemConnectionArgs



class ZTOYY_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: RepositoryOrder

   _args: RepositoryConnectionArgs



class PJNSO_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: TeamOrder

   _args: TeamConnectionArgs



class SATUE_ProjectV2View_Field(ProjectV2View):
   class ProjectV2ViewArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2ViewArgs



class HCKUP_ProjectV2ViewConnection_Field(ProjectV2ViewConnection):
   class ProjectV2ViewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ViewOrder

   _args: ProjectV2ViewConnectionArgs



class ProjectV2(GQLObject):
   closed: bool
   closedAt: DateTime
   createdAt: DateTime
   creator: Actor
   databaseId: int
   field: LBPGK_ProjectV2FieldConfiguration_Field
   fields: ECCCS_ProjectV2FieldConfigurationConnection_Field
   id: ID
   items: MHZBW_ProjectV2ItemConnection_Field
   number: int
   owner: ProjectV2Owner
   public: bool
   readme: str
   repositories: ZTOYY_RepositoryConnection_Field
   resourcePath: URI
   shortDescription: str
   teams: PJNSO_TeamConnection_Field
   title: str
   updatedAt: DateTime
   url: URI
   view: SATUE_ProjectV2View_Field
   viewerCanUpdate: bool
   views: HCKUP_ProjectV2ViewConnection_Field

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

class JCZTA_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class HBTWT_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: TeamOrder
      userLogins: list[NonNull_str]
      immediateOnly: bool
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class LJYMG_TeamDiscussion_Field(TeamDiscussion):
   class TeamDiscussionArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: TeamDiscussionArgs



class MBMHT_TeamDiscussionConnection_Field(TeamDiscussionConnection):
   class TeamDiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      isPinned: bool
      orderBy: TeamDiscussionOrder

   _args: TeamDiscussionConnectionArgs



class FJKGD_OrganizationInvitationConnection_Field(OrganizationInvitationConnection):
   class OrganizationInvitationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationInvitationConnectionArgs



class DFCFY_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class LOSTL_TeamMemberConnection_Field(TeamMemberConnection):
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



class VSXPE_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class RLUWE_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2Order
      filterBy: ProjectV2Filters
      query: str

   _args: ProjectV2ConnectionArgs



class WDVNZ_TeamRepositoryConnection_Field(TeamRepositoryConnection):
   class TeamRepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: TeamRepositoryOrder

   _args: TeamRepositoryConnectionArgs



class Team(GQLObject):
   ancestors: JCZTA_TeamConnection_Field
   avatarUrl: OGGXC_URI_Field
   childTeams: HBTWT_TeamConnection_Field
   combinedSlug: str
   createdAt: DateTime
   databaseId: int
   description: str
   discussion: LJYMG_TeamDiscussion_Field
   discussions: MBMHT_TeamDiscussionConnection_Field
   discussionsResourcePath: URI
   discussionsUrl: URI
   editTeamResourcePath: URI
   editTeamUrl: URI
   id: ID
   invitations: FJKGD_OrganizationInvitationConnection_Field
   memberStatuses: DFCFY_UserStatusConnection_Field
   members: LOSTL_TeamMemberConnection_Field
   membersResourcePath: URI
   membersUrl: URI
   name: str
   newTeamResourcePath: URI
   newTeamUrl: URI
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   parentTeam: NewType('Team', GQLObject) ## Circular Reference for Team
   privacy: TeamPrivacy
   projectV2: VSXPE_ProjectV2_Field
   projectsV2: RLUWE_ProjectV2Connection_Field
   repositories: WDVNZ_TeamRepositoryConnection_Field
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

class NVGEL_BranchProtectionRuleConflictConnection_Field(BranchProtectionRuleConflictConnection):
   class BranchProtectionRuleConflictConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BranchProtectionRuleConflictConnectionArgs



class SVXWP_BypassForcePushAllowanceConnection_Field(BypassForcePushAllowanceConnection):
   class BypassForcePushAllowanceConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BypassForcePushAllowanceConnectionArgs



class KVJLU_BypassPullRequestAllowanceConnection_Field(BypassPullRequestAllowanceConnection):
   class BypassPullRequestAllowanceConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BypassPullRequestAllowanceConnectionArgs



class LXZBZ_RefConnection_Field(RefConnection):
   class RefConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: RefConnectionArgs



class YOPMH_PushAllowanceConnection_Field(PushAllowanceConnection):
   class PushAllowanceConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PushAllowanceConnectionArgs



class list_RequiredStatusCheckDescription(list, RequiredStatusCheckDescription): pass

class LPQMP_ReviewDismissalAllowanceConnection_Field(ReviewDismissalAllowanceConnection):
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
   branchProtectionRuleConflicts: NVGEL_BranchProtectionRuleConflictConnection_Field
   bypassForcePushAllowances: SVXWP_BypassForcePushAllowanceConnection_Field
   bypassPullRequestAllowances: KVJLU_BypassPullRequestAllowanceConnection_Field
   creator: Actor
   databaseId: int
   dismissesStaleReviews: bool
   id: ID
   isAdminEnforced: bool
   lockAllowsFetchAndMerge: bool
   lockBranch: bool
   matchingRefs: LXZBZ_RefConnection_Field
   pattern: str
   pushAllowances: YOPMH_PushAllowanceConnection_Field
   repository: Repository
   requireLastPushApproval: bool
   requiredApprovingReviewCount: int
   requiredStatusCheckContexts: list[str]
   requiredStatusChecks: list_RequiredStatusCheckDescription[RequiredStatusCheckDescription]
   requiresApprovingReviews: bool
   requiresCodeOwnerReviews: bool
   requiresCommitSignatures: bool
   requiresConversationResolution: bool
   requiresLinearHistory: bool
   requiresStatusChecks: bool
   requiresStrictStatusChecks: bool
   restrictsPushes: bool
   restrictsReviewDismissals: bool
   reviewDismissalAllowances: LPQMP_ReviewDismissalAllowanceConnection_Field

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

class FBWWR_ComparisonCommitConnection_Field(ComparisonCommitConnection):
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
   commits: FBWWR_ComparisonCommitConnection_Field
   headTarget: GitObject
   id: ID
   status: ComparisonStatus

class NUMHH_PullRequestConnection_Field(Generic[PullRequestConnection]):
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



class CFIEI_Comparison_Field(Comparison):
   class ComparisonArgs(GQLArgsSet, GQLObject):
      headRef: NonNull_str

   _args: ComparisonArgs



class Ref(GQLObject):
   associatedPullRequests: NUMHH_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   branchProtectionRule: BranchProtectionRule
   compare: CFIEI_Comparison_Field
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

class BLFIW_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class WFONC_UserContentEditConnection_Field(UserContentEditConnection):
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
   minimizedReason: str
   originalCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   originalPosition: int
   outdated: bool
   path: str
   position: int
   publishedAt: DateTime
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   pullRequestReview: NewType('PullRequestReview', GQLObject) ## Circular Reference for PullRequestReview
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: BLFIW_ReactionConnection_Field
   replyTo: NewType('PullRequestReviewComment', GQLObject) ## Circular Reference for PullRequestReviewComment
   repository: Repository
   resourcePath: URI
   state: PullRequestReviewCommentState
   updatedAt: DateTime
   url: URI
   userContentEdits: WFONC_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanMinimize: bool
   viewerCanReact: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: CommentCannotUpdateReason
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

class CEJXO_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewCommentConnectionArgs



class KKIMB_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class HRSQL_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class DJFMV_UserContentEditConnection_Field(UserContentEditConnection):
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
   comments: CEJXO_PullRequestReviewCommentConnection_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   lastEditedAt: DateTime
   onBehalfOf: KKIMB_TeamConnection_Field
   publishedAt: DateTime
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: HRSQL_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   state: PullRequestReviewState
   submittedAt: DateTime
   updatedAt: DateTime
   url: URI
   userContentEdits: DJFMV_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanReact: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: CommentCannotUpdateReason
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

class NNRLQ_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      skip: int

   _args: PullRequestReviewCommentConnectionArgs



class PullRequestReviewThread(GQLObject):
   comments: NNRLQ_PullRequestReviewCommentConnection_Field
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

class RMGAI_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class CommitCommentThread(GQLObject):
   comments: RMGAI_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
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

class MNGZQ_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class PullRequestCommitCommentThread(GQLObject):
   comments: MNGZQ_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
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

class HCPOK_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class AZBUG_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      userLinkedOnly: bool
      after: str
      before: str
      first: int
      last: int
      orderBy: IssueOrder

   _args: IssueConnectionArgs



class UDFWI_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class ZGRNO_PullRequestCommitConnection_Field(PullRequestCommitConnection):
   class PullRequestCommitConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestCommitConnectionArgs



class LPYPF_PullRequestChangedFileConnection_Field(PullRequestChangedFileConnection):
   class PullRequestChangedFileConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestChangedFileConnectionArgs



class XUBDA_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject):
      includeNotificationContexts: bool

   _args: HovercardArgs



class FCQGH_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class DHJKY_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      writersOnly: bool

   _args: PullRequestReviewConnectionArgs



class VHKTE_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewConnectionArgs



class MUVEP_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class AEGRJ_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: ProjectCardConnectionArgs



class PAIUQ_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class FJFGT_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class YFBGX_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class EWNXU_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class AOLPW_ReviewRequestConnection_Field(ReviewRequestConnection):
   class ReviewRequestConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ReviewRequestConnectionArgs



class JJCUH_PullRequestReviewThreadConnection_Field(PullRequestReviewThreadConnection):
   class PullRequestReviewThreadConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewThreadConnectionArgs



class NonNull_PullRequestReviewState(GQLObject): pass

class WRQHV_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      states: list[NonNull_PullRequestReviewState]
      author: str

   _args: PullRequestReviewConnectionArgs



class NonNull_PullRequestTimelineItemsItemType(GQLObject): pass

class PFNJC_PullRequestTimelineItemsConnection_Field(PullRequestTimelineItemsConnection):
   class PullRequestTimelineItemsConnectionArgs(GQLArgsSet, GQLObject):
      since: DateTime
      skip: int
      itemTypes: list[NonNull_PullRequestTimelineItemsItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestTimelineItemsConnectionArgs



class AKNYQ_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class PullRequest(GQLObject):
   activeLockReason: LockReason
   additions: int
   assignees: HCPOK_UserConnection_Field
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
   closingIssuesReferences: AZBUG_IssueConnection_Field
   comments: UDFWI_IssueCommentConnection_Field
   commits: ZGRNO_PullRequestCommitConnection_Field
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   deletions: int
   editor: Actor
   files: LPYPF_PullRequestChangedFileConnection_Field
   headRef: Ref
   headRefName: str
   headRefOid: GitObjectID
   headRepository: Repository
   headRepositoryOwner: RepositoryOwner
   hovercard: XUBDA_Hovercard_Field
   id: ID
   includesCreatedEdit: bool
   isCrossRepository: bool
   isDraft: bool
   isReadByViewer: bool
   labels: FCQGH_LabelConnection_Field
   lastEditedAt: DateTime
   latestOpinionatedReviews: DHJKY_PullRequestReviewConnection_Field
   latestReviews: VHKTE_PullRequestReviewConnection_Field
   locked: bool
   maintainerCanModify: bool
   mergeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   mergeable: MergeableState
   merged: bool
   mergedAt: DateTime
   mergedBy: Actor
   milestone: Milestone
   number: int
   participants: MUVEP_UserConnection_Field
   permalink: URI
   potentialMergeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   projectCards: AEGRJ_ProjectCardConnection_Field
   projectItems: PAIUQ_ProjectV2ItemConnection_Field
   projectV2: FJFGT_ProjectV2_Field
   projectsV2: YFBGX_ProjectV2Connection_Field
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: EWNXU_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   revertResourcePath: URI
   revertUrl: URI
   reviewDecision: PullRequestReviewDecision
   reviewRequests: AOLPW_ReviewRequestConnection_Field
   reviewThreads: JJCUH_PullRequestReviewThreadConnection_Field
   reviews: WRQHV_PullRequestReviewConnection_Field
   state: PullRequestState
   suggestedReviewers: SuggestedReviewer
   timelineItems: PFNJC_PullRequestTimelineItemsConnection_Field
   title: str
   titleHTML: HTML
   totalCommentsCount: int
   updatedAt: DateTime
   url: URI
   userContentEdits: AKNYQ_UserContentEditConnection_Field
   viewerCanApplySuggestion: bool
   viewerCanDeleteHeadRef: bool
   viewerCanDisableAutoMerge: bool
   viewerCanEditFiles: bool
   viewerCanEnableAutoMerge: bool
   viewerCanMergeAsAdmin: bool
   viewerCanReact: bool
   viewerCanSubscribe: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: CommentCannotUpdateReason
   viewerDidAuthor: bool
   viewerLatestReview: PullRequestReview
   viewerLatestReviewRequest: ReviewRequest
   viewerMergeBodyText: JUTMB_viewerMergeBodyText_Field
   viewerMergeHeadlineText: ZQSSH_viewerMergeHeadlineText_Field
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
   avatarUrl: FDWKE_URI_Field
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

class Blame(GQLObject):
   ranges: BlameRange

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

class CZEAF_DeploymentReviewerConnection_Field(DeploymentReviewerConnection):
   class DeploymentReviewerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewerConnectionArgs



class DeploymentRequest(GQLObject):
   currentUserCanApprove: bool
   environment: Environment
   reviewers: CZEAF_DeploymentReviewerConnection_Field
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

class FWEEE_CheckAnnotationConnection_Field(CheckAnnotationConnection):
   class CheckAnnotationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CheckAnnotationConnectionArgs



class ZDGGO_CheckStepConnection_Field(CheckStepConnection):
   class CheckStepConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      number: int

   _args: CheckStepConnectionArgs



class CheckRun(GQLObject):
   annotations: FWEEE_CheckAnnotationConnection_Field
   checkSuite: NewType('CheckSuite', GQLObject) ## Circular Reference for CheckSuite
   completedAt: DateTime
   conclusion: CheckConclusionState
   databaseId: int
   deployment: Deployment
   detailsUrl: URI
   externalId: str
   id: ID
   isRequired: SDQUK_isRequired_Field
   name: str
   pendingDeploymentRequest: DeploymentRequest
   permalink: URI
   repository: Repository
   resourcePath: URI
   startedAt: DateTime
   status: CheckStatusState
   steps: ZDGGO_CheckStepConnection_Field
   summary: str
   text: str
   title: str
   url: URI

class StatusContext(GQLObject):
   avatarUrl: BGIJX_URI_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   context: str
   createdAt: DateTime
   creator: Actor
   description: str
   id: ID
   isRequired: YIPUF_isRequired_Field
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

class NKXOH_StatusCheckRollupContextConnection_Field(StatusCheckRollupContextConnection):
   class StatusCheckRollupContextConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: StatusCheckRollupContextConnectionArgs



class LFDCG_StatusContext_Field(StatusContext):
   class StatusContextArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: StatusContextArgs



class Status(GQLObject):
   combinedContexts: NKXOH_StatusCheckRollupContextConnection_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   context: LFDCG_StatusContext_Field
   contexts: StatusContext
   id: ID
   state: StatusState

class BBALG_StatusCheckRollupContextConnection_Field(StatusCheckRollupContextConnection):
   class StatusCheckRollupContextConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: StatusCheckRollupContextConnectionArgs



class StatusCheckRollup(GQLObject):
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   contexts: BBALG_StatusCheckRollupContextConnection_Field
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

class QKRYA_PullRequestConnection_Field(PullRequestConnection):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: PullRequestOrder

   _args: PullRequestConnectionArgs



class RTADD_GitActorConnection_Field(GitActorConnection):
   class GitActorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: GitActorConnectionArgs



class TDLPX_Blame_Field(Blame):
   class BlameArgs(GQLArgsSet, GQLObject):
      path: NonNull_str

   _args: BlameArgs



class ZBSTK_CheckSuiteConnection_Field(CheckSuiteConnection):
   class CheckSuiteConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      filterBy: CheckSuiteFilter

   _args: CheckSuiteConnectionArgs



class VQKIN_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class RIZSP_DeploymentConnection_Field(DeploymentConnection):
   class DeploymentConnectionArgs(GQLArgsSet, GQLObject):
      environments: list[NonNull_str]
      orderBy: DeploymentOrder
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentConnectionArgs



class QFFBA_TreeEntry_Field(TreeEntry):
   class TreeEntryArgs(GQLArgsSet, GQLObject):
      path: NonNull_str

   _args: TreeEntryArgs



class WHLAG_CommitHistoryConnection_Field(CommitHistoryConnection):
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



class BMVHK_CommitConnection_Field(CommitConnection):
   class CommitConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitConnectionArgs



class CJWSG_SubmoduleConnection_Field(SubmoduleConnection):
   class SubmoduleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: SubmoduleConnectionArgs



class Commit(GQLObject):
   abbreviatedOid: str
   additions: int
   associatedPullRequests: QKRYA_PullRequestConnection_Field
   author: GitActor
   authoredByCommitter: bool
   authoredDate: DateTime
   authors: RTADD_GitActorConnection_Field
   blame: TDLPX_Blame_Field
   changedFilesIfAvailable: int
   checkSuites: ZBSTK_CheckSuiteConnection_Field
   comments: VQKIN_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
   commitResourcePath: URI
   commitUrl: URI
   committedDate: DateTime
   committedViaWeb: bool
   committer: GitActor
   deletions: int
   deployments: RIZSP_DeploymentConnection_Field
   file: QFFBA_TreeEntry_Field
   history: WHLAG_CommitHistoryConnection_Field
   id: ID
   message: str
   messageBody: str
   messageBodyHTML: HTML
   messageHeadline: str
   messageHeadlineHTML: HTML
   oid: GitObjectID
   onBehalfOf: NewType('Organization', GQLObject) ## Circular Reference for Organization
   parents: BMVHK_CommitConnection_Field
   pushedDate: DateTime
   repository: Repository
   resourcePath: URI
   signature: GitSignature
   status: Status
   statusCheckRollup: StatusCheckRollup
   submodules: CJWSG_SubmoduleConnection_Field
   tarballUrl: URI
   tree: Tree
   treeResourcePath: URI
   treeUrl: URI
   url: URI
   viewerCanSubscribe: bool
   viewerSubscription: SubscriptionState
   zipballUrl: URI

class CJOIA_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class HHGYR_UserContentEditConnection_Field(UserContentEditConnection):
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
   reactions: CJOIA_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   updatedAt: DateTime
   url: URI
   userContentEdits: HHGYR_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanMinimize: bool
   viewerCanReact: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: CommentCannotUpdateReason
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

class LEAHL_CreatedCommitContributionConnection_Field(CreatedCommitContributionConnection):
   class CreatedCommitContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: CommitContributionOrder

   _args: CreatedCommitContributionConnectionArgs



class CommitContributionsByRepository(GQLObject):
   contributions: LEAHL_CreatedCommitContributionConnection_Field
   repository: Repository
   resourcePath: URI
   url: URI

class ContributionCalendarWeek(GQLObject):
   contributionDays: ContributionCalendarDay
   firstDay: Date

class ContributionCalendar(GQLObject):
   colors: str
   isHalloween: bool
   months: ContributionCalendarMonth
   totalContributions: int
   weeks: ContributionCalendarWeek

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

class PWLGA_CreatedIssueContributionConnection_Field(CreatedIssueContributionConnection):
   class CreatedIssueContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedIssueContributionConnectionArgs



class IssueContributionsByRepository(GQLObject):
   contributions: PWLGA_CreatedIssueContributionConnection_Field
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

class EELPE_CreatedPullRequestContributionConnection_Field(CreatedPullRequestContributionConnection):
   class CreatedPullRequestContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestContributionConnectionArgs



class PullRequestContributionsByRepository(GQLObject):
   contributions: EELPE_CreatedPullRequestContributionConnection_Field
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

class CNSCY_CreatedPullRequestReviewContributionConnection_Field(CreatedPullRequestReviewContributionConnection):
   class CreatedPullRequestReviewContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestReviewContributionConnectionArgs



class PullRequestReviewContributionsByRepository(GQLObject):
   contributions: CNSCY_CreatedPullRequestReviewContributionConnection_Field
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

class RTWHN_CommitContributionsByRepository_Field(CommitContributionsByRepository):
   class CommitContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int

   _args: CommitContributionsByRepositoryArgs



class AIBBS_CreatedIssueContributionConnection_Field(CreatedIssueContributionConnection):
   class CreatedIssueContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      excludePopular: bool
      orderBy: ContributionOrder

   _args: CreatedIssueContributionConnectionArgs



class NXNUI_IssueContributionsByRepository_Field(IssueContributionsByRepository):
   class IssueContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int
      excludeFirst: bool
      excludePopular: bool

   _args: IssueContributionsByRepositoryArgs



class TZYCV_CreatedPullRequestContributionConnection_Field(CreatedPullRequestContributionConnection):
   class CreatedPullRequestContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      excludePopular: bool
      orderBy: ContributionOrder

   _args: CreatedPullRequestContributionConnectionArgs



class CNBKS_PullRequestContributionsByRepository_Field(PullRequestContributionsByRepository):
   class PullRequestContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int
      excludeFirst: bool
      excludePopular: bool

   _args: PullRequestContributionsByRepositoryArgs



class CWRWB_CreatedPullRequestReviewContributionConnection_Field(CreatedPullRequestReviewContributionConnection):
   class CreatedPullRequestReviewContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestReviewContributionConnectionArgs



class WPXFW_PullRequestReviewContributionsByRepository_Field(PullRequestReviewContributionsByRepository):
   class PullRequestReviewContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int

   _args: PullRequestReviewContributionsByRepositoryArgs



class JJTNX_CreatedRepositoryContributionConnection_Field(CreatedRepositoryContributionConnection):
   class CreatedRepositoryContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      orderBy: ContributionOrder

   _args: CreatedRepositoryContributionConnectionArgs



class ContributionsCollection(GQLObject):
   commitContributionsByRepository: RTWHN_CommitContributionsByRepository_Field
   contributionCalendar: ContributionCalendar
   contributionYears: int
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
   issueContributions: AIBBS_CreatedIssueContributionConnection_Field
   issueContributionsByRepository: NXNUI_IssueContributionsByRepository_Field
   joinedGitHubContribution: JoinedGitHubContribution
   latestRestrictedContributionDate: Date
   mostRecentCollectionWithActivity: NewType('ContributionsCollection', GQLObject) ## Circular Reference for ContributionsCollection
   mostRecentCollectionWithoutActivity: NewType('ContributionsCollection', GQLObject) ## Circular Reference for ContributionsCollection
   popularIssueContribution: CreatedIssueContribution
   popularPullRequestContribution: CreatedPullRequestContribution
   pullRequestContributions: TZYCV_CreatedPullRequestContributionConnection_Field
   pullRequestContributionsByRepository: CNBKS_PullRequestContributionsByRepository_Field
   pullRequestReviewContributions: CWRWB_CreatedPullRequestReviewContributionConnection_Field
   pullRequestReviewContributionsByRepository: WPXFW_PullRequestReviewContributionsByRepository_Field
   repositoryContributions: JJTNX_CreatedRepositoryContributionConnection_Field
   restrictedContributionsCount: int
   startedAt: DateTime
   totalCommitContributions: int
   totalIssueContributions: PBPMT_totalIssueContributions_Field
   totalPullRequestContributions: FRXSN_totalPullRequestContributions_Field
   totalPullRequestReviewContributions: int
   totalRepositoriesWithContributedCommits: int
   totalRepositoriesWithContributedIssues: ERTLR_totalRepositoriesWithContributedIssues_Field
   totalRepositoriesWithContributedPullRequestReviews: int
   totalRepositoriesWithContributedPullRequests: IRLGS_totalRepositoriesWithContributedPullRequests_Field
   totalRepositoryContributions: LOSNG_totalRepositoryContributions_Field
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

class CSASF_UserContentEditConnection_Field(UserContentEditConnection):
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
   userContentEdits: CSASF_UserContentEditConnection_Field
   viewerCanDelete: bool
   viewerCanMinimize: bool
   viewerCanUpdate: bool
   viewerCannotUpdateReasons: CommentCannotUpdateReason
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
   text: MVXGN_text_Field

class GistEdge(GQLObject):
   cursor: str
   node: NewType('Gist', GQLObject) ## Circular Reference for Gist

class list_GistEdge(list, GistEdge): pass

class GistConnection(GQLObject):
   edges: list_GistEdge[GistEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Gist
   pageInfo: PageInfo
   totalCount: int

class OFFDY_GistCommentConnection_Field(GistCommentConnection):
   class GistCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: GistCommentConnectionArgs



class UJCGC_GistFile_Field(GistFile):
   class GistFileArgs(GQLArgsSet, GQLObject):
      limit: int
      oid: GitObjectID

   _args: GistFileArgs



class list_GistFile(list, GistFile): pass

class HGDEZ_GistConnection_Field(GistConnection):
   class GistConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: GistOrder

   _args: GistConnectionArgs



class MIDTI_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class Gist(GQLObject):
   comments: OFFDY_GistCommentConnection_Field
   createdAt: DateTime
   description: str
   files: UJCGC_GistFile_Field
   forks: HGDEZ_GistConnection_Field
   id: ID
   isFork: bool
   isPublic: bool
   name: str
   owner: RepositoryOwner
   pushedAt: DateTime
   resourcePath: URI
   stargazerCount: int
   stargazers: MIDTI_StargazerConnection_Field
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

class PDRQA_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class ProfileItemShowcase(GQLObject):
   hasPinnedItems: bool
   items: PDRQA_PinnableItemConnection_Field

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

class GZRGR_SponsorsListingFeaturedItem_Field(SponsorsListingFeaturedItem):
   class SponsorsListingFeaturedItemArgs(GQLArgsSet, GQLObject):
      featureableTypes: list[NonNull_SponsorsListingFeaturedItemFeatureableType]

   _args: SponsorsListingFeaturedItemArgs



class RIQNU_SponsorsTierConnection_Field(SponsorsTierConnection):
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
   featuredItems: GZRGR_SponsorsListingFeaturedItem_Field
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
   tiers: RIQNU_SponsorsTierConnection_Field
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

class KAAXS_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class UOJIH_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class NonNull_SponsorsActivityAction(GQLObject): pass

class UWNSJ_SponsorsActivityConnection_Field(Generic[SponsorsActivityConnection]):
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



class ZRJRR_Sponsorship_Field(Generic[Sponsorship]):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class PTBNT_Sponsorship_Field(Generic[Sponsorship]):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class GBTOL_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class QIMIO_SponsorshipConnection_Field(Generic[SponsorshipConnection]):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class KXGEX_SponsorshipConnection_Field(Generic[SponsorshipConnection]):
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
   isSponsoredBy: IDILW_isSponsoredBy_Field
   isSponsoringViewer: bool
   monthlyEstimatedSponsorsIncomeInCents: int
   sponsoring: KAAXS_SponsorConnection_Field
   sponsors: UOJIH_SponsorConnection_Field
   sponsorsActivities: UWNSJ_SponsorsActivityConnection_Field ## Circular Reference for SponsorsActivityConnection
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: ZRJRR_Sponsorship_Field ## Circular Reference for Sponsorship
   sponsorshipForViewerAsSponsorable: PTBNT_Sponsorship_Field ## Circular Reference for Sponsorship
   sponsorshipNewsletters: GBTOL_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: QIMIO_SponsorshipConnection_Field ## Circular Reference for SponsorshipConnection
   sponsorshipsAsSponsor: KXGEX_SponsorshipConnection_Field ## Circular Reference for SponsorshipConnection
   totalSponsorshipAmountAsSponsorInCents: ERAGL_totalSponsorshipAmountAsSponsorInCents_Field
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

class GOEPF_SponsorshipConnection_Field(SponsorshipConnection):
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
   sponsorships: GOEPF_SponsorshipConnection_Field

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

class IQYVN_CommitCommentConnection_Field(CommitCommentConnection):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class BBKOW_ContributionsCollection_Field(ContributionsCollection):
   class ContributionsCollectionArgs(GQLArgsSet, GQLObject):
      organizationID: ID
      from_: DateTime
      to: DateTime

   _args: ContributionsCollectionArgs



class MTOGS_FollowerConnection_Field(FollowerConnection):
   class FollowerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: FollowerConnectionArgs



class TTHKG_FollowingConnection_Field(FollowingConnection):
   class FollowingConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: FollowingConnectionArgs



class QUALE_Gist_Field(Gist):
   class GistArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: GistArgs



class MEZXC_GistCommentConnection_Field(GistCommentConnection):
   class GistCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: GistCommentConnectionArgs



class QXOBC_GistConnection_Field(GistConnection):
   class GistConnectionArgs(GQLArgsSet, GQLObject):
      privacy: GistPrivacy
      orderBy: GistOrder
      after: str
      before: str
      first: int
      last: int

   _args: GistConnectionArgs



class GXURK_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject):
      primarySubjectId: ID

   _args: HovercardArgs



class XTXKT_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class BXFOR_IssueConnection_Field(IssueConnection):
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



class QPIJV_Organization_Field(Generic[Organization]):
   class OrganizationArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: OrganizationArgs



class MKWOJ_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: OrganizationOrder
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class EKZRX_PackageConnection_Field(PackageConnection):
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

class CSMMU_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class ZBLFE_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class BCUFV_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class RTWFN_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class CZRAV_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: ProjectOrder
      search: str
      states: list[NonNull_ProjectState]
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class BUTJB_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class WKYAT_PublicKeyConnection_Field(PublicKeyConnection):
   class PublicKeyConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PublicKeyConnectionArgs



class VSBAR_PullRequestConnection_Field(PullRequestConnection):
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



class IMYYU_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class EUGKM_RepositoryConnection_Field(RepositoryConnection):
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



class HQQQM_RepositoryConnection_Field(RepositoryConnection):
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



class TKBGI_Repository_Field(Repository):
   class RepositoryArgs(GQLArgsSet, GQLObject):
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs



class KVMKB_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class NAEQS_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionOrder
      repositoryId: ID
      answered: bool

   _args: DiscussionConnectionArgs



class NYYLO_SavedReplyConnection_Field(SavedReplyConnection):
   class SavedReplyConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SavedReplyOrder

   _args: SavedReplyConnectionArgs



class CGLBR_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class DBAYO_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class IXYXD_SponsorsActivityConnection_Field(SponsorsActivityConnection):
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



class DQMHZ_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class NQYOW_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class LZOSI_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class JLSYY_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class TFGZD_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipOrder
      maintainerLogins: list[NonNull_str]
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class KVQGV_StarredRepositoryConnection_Field(StarredRepositoryConnection):
   class StarredRepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      ownedByViewer: bool
      orderBy: StarOrder

   _args: StarredRepositoryConnectionArgs



class NonNull_RepositoryOrder(RepositoryOrder): pass

class BSMKP_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: NonNull_RepositoryOrder
      since: DateTime

   _args: RepositoryConnectionArgs



class BKKHV_RepositoryConnection_Field(RepositoryConnection):
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
   anyPinnableItems: FVIRY_anyPinnableItems_Field
   avatarUrl: KNIKP_URI_Field
   bio: str
   bioHTML: HTML
   canReceiveOrganizationEmailsWhenNotificationsRestricted: UPNFZ_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field
   commitComments: IQYVN_CommitCommentConnection_Field
   company: str
   companyHTML: HTML
   contributionsCollection: BBKOW_ContributionsCollection_Field
   createdAt: DateTime
   databaseId: int
   email: str
   estimatedNextSponsorsPayoutInCents: int
   followers: MTOGS_FollowerConnection_Field
   following: TTHKG_FollowingConnection_Field
   gist: QUALE_Gist_Field
   gistComments: MEZXC_GistCommentConnection_Field
   gists: QXOBC_GistConnection_Field
   hasSponsorsListing: bool
   hovercard: GXURK_Hovercard_Field
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
   isSponsoredBy: HJFNL_isSponsoredBy_Field
   isSponsoringViewer: bool
   isViewer: bool
   issueComments: XTXKT_IssueCommentConnection_Field
   issues: BXFOR_IssueConnection_Field
   itemShowcase: ProfileItemShowcase
   location: str
   login: str
   monthlyEstimatedSponsorsIncomeInCents: int
   name: str
   organization: QPIJV_Organization_Field ## Circular Reference for Organization
   organizationVerifiedDomainEmails: NTILC_organizationVerifiedDomainEmails_Field
   organizations: MKWOJ_OrganizationConnection_Field
   packages: EKZRX_PackageConnection_Field
   pinnableItems: CSMMU_PinnableItemConnection_Field
   pinnedItems: ZBLFE_PinnableItemConnection_Field
   pinnedItemsRemaining: int
   project: BCUFV_Project_Field
   projectV2: RTWFN_ProjectV2_Field
   projects: CZRAV_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   projectsV2: BUTJB_ProjectV2Connection_Field
   publicKeys: WKYAT_PublicKeyConnection_Field
   pullRequests: VSBAR_PullRequestConnection_Field
   recentProjects: IMYYU_ProjectV2Connection_Field
   repositories: EUGKM_RepositoryConnection_Field
   repositoriesContributedTo: HQQQM_RepositoryConnection_Field
   repository: TKBGI_Repository_Field
   repositoryDiscussionComments: KVMKB_DiscussionCommentConnection_Field
   repositoryDiscussions: NAEQS_DiscussionConnection_Field
   resourcePath: URI
   savedReplies: NYYLO_SavedReplyConnection_Field
   sponsoring: CGLBR_SponsorConnection_Field
   sponsors: DBAYO_SponsorConnection_Field
   sponsorsActivities: IXYXD_SponsorsActivityConnection_Field
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: DQMHZ_Sponsorship_Field
   sponsorshipForViewerAsSponsorable: NQYOW_Sponsorship_Field
   sponsorshipNewsletters: LZOSI_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: JLSYY_SponsorshipConnection_Field
   sponsorshipsAsSponsor: TFGZD_SponsorshipConnection_Field
   starredRepositories: KVQGV_StarredRepositoryConnection_Field
   status: UserStatus
   topRepositories: BSMKP_RepositoryConnection_Field
   totalSponsorshipAmountAsSponsorInCents: XQMCD_totalSponsorshipAmountAsSponsorInCents_Field
   twitterUsername: str
   updatedAt: DateTime
   url: URI
   viewerCanChangePinnedItems: bool
   viewerCanCreateProjects: bool
   viewerCanFollow: bool
   viewerCanSponsor: bool
   viewerIsFollowing: bool
   viewerIsSponsoring: bool
   watching: BKKHV_RepositoryConnection_Field
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

class list_UserEmailMetadata(list, UserEmailMetadata): pass

class ExternalIdentitySamlAttributes(GQLObject):
   attributes: ExternalIdentityAttribute
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

class UYVBH_ExternalIdentityConnection_Field(ExternalIdentityConnection):
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
   externalIdentities: UYVBH_ExternalIdentityConnection_Field
   id: ID
   idpCertificate: X509Certificate
   issuer: str
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   signatureMethod: URI
   ssoUrl: URI

class UDIQN_OrganizationAuditEntryConnection_Field(OrganizationAuditEntryConnection):
   class OrganizationAuditEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: AuditLogOrder

   _args: OrganizationAuditEntryConnectionArgs



class ULAGM_VerifiableDomainConnection_Field(VerifiableDomainConnection):
   class VerifiableDomainConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      isVerified: bool
      isApproved: bool
      orderBy: VerifiableDomainOrder

   _args: VerifiableDomainConnectionArgs



class LPOUX_OrganizationEnterpriseOwnerConnection_Field(OrganizationEnterpriseOwnerConnection):
   class OrganizationEnterpriseOwnerConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      organizationRole: RoleInOrganization
      orderBy: OrgEnterpriseOwnerOrder
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationEnterpriseOwnerConnectionArgs



class BRJXE_IpAllowListEntryConnection_Field(Generic[IpAllowListEntryConnection]):
   class IpAllowListEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: IpAllowListEntryConnectionArgs



class SCMNT_MannequinConnection_Field(MannequinConnection):
   class MannequinConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: MannequinOrder

   _args: MannequinConnectionArgs



class YCLDV_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class QZKCN_OrganizationMemberConnection_Field(OrganizationMemberConnection):
   class OrganizationMemberConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationMemberConnectionArgs



class LEGFV_PackageConnection_Field(PackageConnection):
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



class YYEWO_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class IQGFP_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class NHFZN_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class ENTLP_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class JJOMQ_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class HBABP_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: ProjectOrder
      search: str
      states: list[NonNull_ProjectState]
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class JQCOF_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class IVDKR_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class AYRJY_RepositoryConnection_Field(RepositoryConnection):
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



class KKADL_Repository_Field(Repository):
   class RepositoryArgs(GQLArgsSet, GQLObject):
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs



class UEMDI_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class PRFXM_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionOrder
      repositoryId: ID
      answered: bool

   _args: DiscussionConnectionArgs



class ANTSK_RepositoryMigrationConnection_Field(RepositoryMigrationConnection):
   class RepositoryMigrationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      state: MigrationState
      repositoryName: str
      orderBy: RepositoryMigrationOrder

   _args: RepositoryMigrationConnectionArgs



class ZVDPU_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class NFTVX_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class ZRACG_SponsorsActivityConnection_Field(SponsorsActivityConnection):
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



class BQPQS_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class CDBVO_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class XODEC_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class ICVSP_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class IGKGG_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipOrder
      maintainerLogins: list[NonNull_str]
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class RZBPU_Team_Field(Team):
   class TeamArgs(GQLArgsSet, GQLObject):
      slug: NonNull_str

   _args: TeamArgs



class WEHNX_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      privacy: TeamPrivacy
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
   anyPinnableItems: HQGVF_anyPinnableItems_Field
   auditLog: UDIQN_OrganizationAuditEntryConnection_Field
   avatarUrl: FDCMQ_URI_Field
   createdAt: DateTime
   databaseId: int
   description: str
   descriptionHTML: str
   domains: ULAGM_VerifiableDomainConnection_Field
   email: str
   enterpriseOwners: LPOUX_OrganizationEnterpriseOwnerConnection_Field
   estimatedNextSponsorsPayoutInCents: int
   hasSponsorsListing: bool
   id: ID
   interactionAbility: RepositoryInteractionAbility
   ipAllowListEnabledSetting: IpAllowListEnabledSettingValue
   ipAllowListEntries: BRJXE_IpAllowListEntryConnection_Field ## Circular Reference for IpAllowListEntryConnection
   ipAllowListForInstalledAppsEnabledSetting: IpAllowListForInstalledAppsEnabledSettingValue
   isSponsoredBy: OVOQQ_isSponsoredBy_Field
   isSponsoringViewer: bool
   isVerified: bool
   itemShowcase: ProfileItemShowcase
   location: str
   login: str
   mannequins: SCMNT_MannequinConnection_Field
   memberStatuses: YCLDV_UserStatusConnection_Field
   membersCanForkPrivateRepositories: bool
   membersWithRole: QZKCN_OrganizationMemberConnection_Field
   monthlyEstimatedSponsorsIncomeInCents: int
   name: str
   newTeamResourcePath: URI
   newTeamUrl: URI
   notificationDeliveryRestrictionEnabledSetting: NotificationRestrictionSettingValue
   organizationBillingEmail: str
   packages: LEGFV_PackageConnection_Field
   pendingMembers: YYEWO_UserConnection_Field
   pinnableItems: IQGFP_PinnableItemConnection_Field
   pinnedItems: NHFZN_PinnableItemConnection_Field
   pinnedItemsRemaining: int
   project: ENTLP_Project_Field
   projectV2: JJOMQ_ProjectV2_Field
   projects: HBABP_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   projectsV2: JQCOF_ProjectV2Connection_Field
   recentProjects: IVDKR_ProjectV2Connection_Field
   repositories: AYRJY_RepositoryConnection_Field
   repository: KKADL_Repository_Field
   repositoryDiscussionComments: UEMDI_DiscussionCommentConnection_Field
   repositoryDiscussions: PRFXM_DiscussionConnection_Field
   repositoryMigrations: ANTSK_RepositoryMigrationConnection_Field
   requiresTwoFactorAuthentication: bool
   resourcePath: URI
   samlIdentityProvider: OrganizationIdentityProvider
   sponsoring: ZVDPU_SponsorConnection_Field
   sponsors: NFTVX_SponsorConnection_Field
   sponsorsActivities: ZRACG_SponsorsActivityConnection_Field
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: BQPQS_Sponsorship_Field
   sponsorshipForViewerAsSponsorable: CDBVO_Sponsorship_Field
   sponsorshipNewsletters: XODEC_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: ICVSP_SponsorshipConnection_Field
   sponsorshipsAsSponsor: IGKGG_SponsorshipConnection_Field
   team: RZBPU_Team_Field
   teams: WEHNX_TeamConnection_Field
   teamsResourcePath: URI
   teamsUrl: URI
   totalSponsorshipAmountAsSponsorInCents: JBWFU_totalSponsorshipAmountAsSponsorInCents_Field
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

class YHVCH_EnterpriseOrganizationMembershipConnection_Field(EnterpriseOrganizationMembershipConnection):
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
   avatarUrl: LHIHH_URI_Field
   createdAt: DateTime
   enterprise: NewType('Enterprise', GQLObject) ## Circular Reference for Enterprise
   id: ID
   login: str
   name: str
   organizations: YHVCH_EnterpriseOrganizationMembershipConnection_Field
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

class CZAWQ_EnterpriseServerUserAccountEmailConnection_Field(EnterpriseServerUserAccountEmailConnection):
   class EnterpriseServerUserAccountEmailConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: EnterpriseServerUserAccountEmailOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerUserAccountEmailConnectionArgs



class EnterpriseServerUserAccount(GQLObject):
   createdAt: DateTime
   emails: CZAWQ_EnterpriseServerUserAccountEmailConnection_Field
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

class KQTIB_EnterpriseServerUserAccountConnection_Field(EnterpriseServerUserAccountConnection):
   class EnterpriseServerUserAccountConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: EnterpriseServerUserAccountOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerUserAccountConnectionArgs



class XVBGC_EnterpriseServerUserAccountsUploadConnection_Field(EnterpriseServerUserAccountsUploadConnection):
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
   userAccounts: KQTIB_EnterpriseServerUserAccountConnection_Field
   userAccountsUploads: XVBGC_EnterpriseServerUserAccountsUploadConnection_Field

class EnterpriseServerInstallationEdge(GQLObject):
   cursor: str
   node: EnterpriseServerInstallation

class list_EnterpriseServerInstallationEdge(list, EnterpriseServerInstallationEdge): pass

class list_EnterpriseServerInstallation(list, EnterpriseServerInstallation): pass

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

class RNCQQ_ExternalIdentityConnection_Field(ExternalIdentityConnection):
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
   externalIdentities: RNCQQ_ExternalIdentityConnection_Field
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

class BEYAI_EnterpriseRepositoryInfoConnection_Field(EnterpriseRepositoryInfoConnection):
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
   repositories: BEYAI_EnterpriseRepositoryInfoConnection_Field

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
   shortDescriptionHTML: BELQK_HTML_Field
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

class PJTIU_ExternalIdentityConnection_Field(ExternalIdentityConnection):
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
   externalIdentities: PJTIU_ExternalIdentityConnection_Field
   id: ID
   idpCertificate: X509Certificate
   issuer: str
   recoveryCodes: list[str]
   signatureMethod: SamlSignatureAlgorithm
   ssoUrl: URI

class NLWHI_EnterpriseAdministratorConnection_Field(EnterpriseAdministratorConnection):
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



class QLPQE_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class GIVUF_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class NonNull_DefaultRepositoryPermissionField(GQLObject): pass

class LEXQF_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_DefaultRepositoryPermissionField
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class QINHM_VerifiableDomainConnection_Field(VerifiableDomainConnection):
   class VerifiableDomainConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      isVerified: bool
      isApproved: bool
      orderBy: VerifiableDomainOrder

   _args: VerifiableDomainConnectionArgs



class GEQUH_EnterpriseServerInstallationConnection_Field(EnterpriseServerInstallationConnection):
   class EnterpriseServerInstallationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      connectedOnly: bool
      orderBy: EnterpriseServerInstallationOrder

   _args: EnterpriseServerInstallationConnectionArgs



class KYKMI_EnterpriseFailedInvitationConnection_Field(EnterpriseFailedInvitationConnection):
   class EnterpriseFailedInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseFailedInvitationConnectionArgs



class UEBGI_IpAllowListEntryConnection_Field(Generic[IpAllowListEntryConnection]):
   class IpAllowListEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: IpAllowListEntryConnectionArgs



class DODEQ_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class NonNull_OrganizationMembersCanCreateRepositoriesSettingValue(GQLObject): pass

class KSVSR_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_OrganizationMembersCanCreateRepositoriesSettingValue
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class OOQZV_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class LSNXQ_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class GCEAN_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class JNTYH_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class BPSZL_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class ENVTJ_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class CXKSH_EnterpriseOutsideCollaboratorConnection_Field(EnterpriseOutsideCollaboratorConnection):
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



class UCSIJ_EnterpriseAdministratorInvitationConnection_Field(EnterpriseAdministratorInvitationConnection):
   class EnterpriseAdministratorInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: EnterpriseAdministratorInvitationOrder
      role: EnterpriseAdministratorRole
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseAdministratorInvitationConnectionArgs



class XCBYK_RepositoryInvitationConnection_Field(RepositoryInvitationConnection):
   class RepositoryInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: RepositoryInvitationOrder
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryInvitationConnectionArgs



class NFGZA_EnterprisePendingMemberInvitationConnection_Field(EnterprisePendingMemberInvitationConnection):
   class EnterprisePendingMemberInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      organizationLogins: list[NonNull_str]
      invitationSource: OrganizationInvitationSource
      after: str
      before: str
      first: int
      last: int

   _args: EnterprisePendingMemberInvitationConnectionArgs



class ENJWV_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class NonNull_IdentityProviderConfigurationState(GQLObject): pass

class ZQDJP_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_IdentityProviderConfigurationState
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class UBKJU_EnterpriseMemberConnection_Field(EnterpriseMemberConnection):
   class EnterpriseMemberConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: EnterpriseMemberOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseMemberConnectionArgs



class VTHYQ_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class CGNRW_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class EnterpriseOwnerInfo(GQLObject):
   admins: NLWHI_EnterpriseAdministratorConnection_Field
   affiliatedUsersWithTwoFactorDisabled: QLPQE_UserConnection_Field
   affiliatedUsersWithTwoFactorDisabledExist: bool
   allowPrivateRepositoryForkingSetting: EnterpriseEnabledDisabledSettingValue
   allowPrivateRepositoryForkingSettingOrganizations: GIVUF_OrganizationConnection_Field
   allowPrivateRepositoryForkingSettingPolicyValue: EnterpriseAllowPrivateRepositoryForkingPolicyValue
   defaultRepositoryPermissionSetting: EnterpriseDefaultRepositoryPermissionSettingValue
   defaultRepositoryPermissionSettingOrganizations: LEXQF_OrganizationConnection_Field
   domains: QINHM_VerifiableDomainConnection_Field
   enterpriseServerInstallations: GEQUH_EnterpriseServerInstallationConnection_Field
   failedInvitations: KYKMI_EnterpriseFailedInvitationConnection_Field
   ipAllowListEnabledSetting: IpAllowListEnabledSettingValue
   ipAllowListEntries: UEBGI_IpAllowListEntryConnection_Field ## Circular Reference for IpAllowListEntryConnection
   ipAllowListForInstalledAppsEnabledSetting: IpAllowListForInstalledAppsEnabledSettingValue
   isUpdatingDefaultRepositoryPermission: bool
   isUpdatingTwoFactorRequirement: bool
   membersCanChangeRepositoryVisibilitySetting: EnterpriseEnabledDisabledSettingValue
   membersCanChangeRepositoryVisibilitySettingOrganizations: DODEQ_OrganizationConnection_Field
   membersCanCreateInternalRepositoriesSetting: bool
   membersCanCreatePrivateRepositoriesSetting: bool
   membersCanCreatePublicRepositoriesSetting: bool
   membersCanCreateRepositoriesSetting: EnterpriseMembersCanCreateRepositoriesSettingValue
   membersCanCreateRepositoriesSettingOrganizations: KSVSR_OrganizationConnection_Field
   membersCanDeleteIssuesSetting: EnterpriseEnabledDisabledSettingValue
   membersCanDeleteIssuesSettingOrganizations: OOQZV_OrganizationConnection_Field
   membersCanDeleteRepositoriesSetting: EnterpriseEnabledDisabledSettingValue
   membersCanDeleteRepositoriesSettingOrganizations: LSNXQ_OrganizationConnection_Field
   membersCanInviteCollaboratorsSetting: EnterpriseEnabledDisabledSettingValue
   membersCanInviteCollaboratorsSettingOrganizations: GCEAN_OrganizationConnection_Field
   membersCanMakePurchasesSetting: EnterpriseMembersCanMakePurchasesSettingValue
   membersCanUpdateProtectedBranchesSetting: EnterpriseEnabledDisabledSettingValue
   membersCanUpdateProtectedBranchesSettingOrganizations: JNTYH_OrganizationConnection_Field
   membersCanViewDependencyInsightsSetting: EnterpriseEnabledDisabledSettingValue
   membersCanViewDependencyInsightsSettingOrganizations: BPSZL_OrganizationConnection_Field
   notificationDeliveryRestrictionEnabledSetting: NotificationRestrictionSettingValue
   oidcProvider: OIDCProvider
   organizationProjectsSetting: EnterpriseEnabledDisabledSettingValue
   organizationProjectsSettingOrganizations: ENVTJ_OrganizationConnection_Field
   outsideCollaborators: CXKSH_EnterpriseOutsideCollaboratorConnection_Field
   pendingAdminInvitations: UCSIJ_EnterpriseAdministratorInvitationConnection_Field
   pendingCollaboratorInvitations: XCBYK_RepositoryInvitationConnection_Field
   pendingMemberInvitations: NFGZA_EnterprisePendingMemberInvitationConnection_Field
   repositoryProjectsSetting: EnterpriseEnabledDisabledSettingValue
   repositoryProjectsSettingOrganizations: ENJWV_OrganizationConnection_Field
   samlIdentityProvider: EnterpriseIdentityProvider
   samlIdentityProviderSettingOrganizations: ZQDJP_OrganizationConnection_Field
   supportEntitlements: UBKJU_EnterpriseMemberConnection_Field
   teamDiscussionsSetting: EnterpriseEnabledDisabledSettingValue
   teamDiscussionsSettingOrganizations: VTHYQ_OrganizationConnection_Field
   twoFactorRequiredSetting: EnterpriseEnabledSettingValue
   twoFactorRequiredSettingOrganizations: CGNRW_OrganizationConnection_Field

class VOADO_EnterpriseMemberConnection_Field(EnterpriseMemberConnection):
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



class PFDDY_OrganizationConnection_Field(OrganizationConnection):
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
   avatarUrl: ODNVG_URI_Field
   billingInfo: EnterpriseBillingInfo
   createdAt: DateTime
   databaseId: int
   description: str
   descriptionHTML: HTML
   id: ID
   location: str
   members: VOADO_EnterpriseMemberConnection_Field
   name: str
   organizations: PFDDY_OrganizationConnection_Field
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

class SASWN_IpAllowListEntryConnection_Field(IpAllowListEntryConnection):
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
   ipAllowListEntries: SASWN_IpAllowListEntryConnection_Field
   logoBackgroundColor: str
   logoUrl: GHGWM_URI_Field
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

class AOCYO_CheckRunConnection_Field(CheckRunConnection):
   class CheckRunConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      filterBy: CheckRunFilter

   _args: CheckRunConnectionArgs



class OKLOB_PullRequestConnection_Field(PullRequestConnection):
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
   checkRuns: AOCYO_CheckRunConnection_Field
   commit: Commit
   conclusion: CheckConclusionState
   createdAt: DateTime
   creator: User
   databaseId: int
   id: ID
   matchingPullRequests: OKLOB_PullRequestConnection_Field
   push: Push
   repository: Repository
   resourcePath: URI
   status: CheckStatusState
   updatedAt: DateTime
   url: URI
   workflowRun: NewType('WorkflowRun', GQLObject) ## Circular Reference for WorkflowRun

class JYTHT_EnvironmentConnection_Field(EnvironmentConnection):
   class EnvironmentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: EnvironmentConnectionArgs



class DeploymentReview(GQLObject):
   comment: str
   databaseId: int
   environments: JYTHT_EnvironmentConnection_Field
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

class NPMFB_WorkflowRunConnection_Field(Generic[WorkflowRunConnection]):
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
   runs: NPMFB_WorkflowRunConnection_Field ## Circular Reference for WorkflowRunConnection
   updatedAt: DateTime

class FDBWK_DeploymentReviewConnection_Field(DeploymentReviewConnection):
   class DeploymentReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewConnectionArgs



class EIUXJ_DeploymentRequestConnection_Field(DeploymentRequestConnection):
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
   deploymentReviews: FDBWK_DeploymentReviewConnection_Field
   id: ID
   pendingDeploymentRequests: EIUXJ_DeploymentRequestConnection_Field
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
   logoUrl: QTTQR_URI_Field
   name: str
   normalizedShortDescription: str
   pricingUrl: URI
   primaryCategory: MarketplaceCategory
   privacyPolicyUrl: URI
   resourcePath: URI
   screenshotUrls: str
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

class TextMatch(GQLObject):
   fragment: str
   highlights: TextMatchHighlight
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

class ASDPC_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      skip: int

   _args: PullRequestReviewCommentConnectionArgs



class PullRequestThread(GQLObject):
   comments: ASDPC_PullRequestReviewCommentConnection_Field
   diffSide: DiffSide
   id: ID
   isCollapsed: bool
   isOutdated: bool
   isResolved: bool
   line: int
   pullRequest: PullRequest
   repository: Repository
   resolvedBy: User
   startDiffSide: DiffSide
   startLine: int
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

class KXFVH_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class GFUIH_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class ProfileOwner(GQLObject):
   anyPinnableItems: QZCCR_anyPinnableItems_Field
   email: str
   id: ID
   itemShowcase: ProfileItemShowcase
   location: str
   login: str
   name: str
   pinnableItems: KXFVH_PinnableItemConnection_Field
   pinnedItems: GFUIH_PinnableItemConnection_Field
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

class VNKES_UserContentEditConnection_Field(UserContentEditConnection):
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
   userContentEdits: VNKES_UserContentEditConnection_Field
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

class TCDRQ_StargazerConnection_Field(StargazerConnection):
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
   stargazers: TCDRQ_StargazerConnection_Field
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

class CreateSponsorsListingPayload(GQLObject):
   clientMutationId: str
   sponsorsListing: SponsorsListing

class CreateSponsorsTierPayload(GQLObject):
   clientMutationId: str
   sponsorsTier: SponsorsTier

class CreateSponsorshipPayload(GQLObject):
   clientMutationId: str
   sponsorship: Sponsorship

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

class DeletePullRequestReviewPayload(GQLObject):
   clientMutationId: str
   pullRequestReview: PullRequestReview

class DeleteVerifiableDomainPayload(GQLObject):
   clientMutationId: str
   owner: VerifiableDomainOwner

class DismissPullRequestReviewPayload(GQLObject):
   clientMutationId: str
   pullRequestReview: PullRequestReview

class DismissRepositoryVulnerabilityAlertPayload(GQLObject):
   clientMutationId: str
   repositoryVulnerabilityAlert: RepositoryVulnerabilityAlert

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

class MDOBM_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class GrantEnterpriseOrganizationsMigratorRolePayload(GQLObject):
   clientMutationId: str
   organizations: MDOBM_OrganizationConnection_Field

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

class MarkPullRequestReadyForReviewPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest

class YRANG_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class MemberStatusable(GQLObject):
   memberStatuses: YRANG_UserStatusConnection_Field

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

class JLQLY_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class OrganizationTeamsHovercardContext(GQLObject):
   message: str
   octicon: str
   relevantTeams: JLQLY_TeamConnection_Field
   teamsResourcePath: URI
   teamsUrl: URI
   totalTeamCount: int

class EVYFY_OrganizationConnection_Field(OrganizationConnection):
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
   relevantOrganizations: EVYFY_OrganizationConnection_Field
   totalOrganizationCount: int

class ETQYV_PackageConnection_Field(PackageConnection):
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
   packages: ETQYV_PackageConnection_Field

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

class SJCNJ_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class ProjectV2Recent(GQLObject):
   recentProjects: SJCNJ_ProjectV2Connection_Field

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

class HLUCT_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionOrder
      repositoryId: ID
      answered: bool

   _args: DiscussionConnectionArgs



class RepositoryDiscussionAuthor(GQLObject):
   repositoryDiscussions: HLUCT_DiscussionConnection_Field

class CCSFI_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class RepositoryDiscussionCommentAuthor(GQLObject):
   repositoryDiscussionComments: CCSFI_DiscussionCommentConnection_Field

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

class OPLRO_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class RevokeEnterpriseOrganizationsMigratorRolePayload(GQLObject):
   clientMutationId: str
   organizations: OPLRO_OrganizationConnection_Field

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

class NonNull_list_CheckSuiteAutoTriggerPreference(list, CheckSuiteAutoTriggerPreference): pass

class UpdateCheckSuitePreferencesInput(GQLObject):
   repositoryId: ID
   autoTriggerPreferences: NonNull_list_CheckSuiteAutoTriggerPreference[CheckSuiteAutoTriggerPreference]
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

class YMHGF_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class UpdateProjectV2ItemPositionPayload(GQLObject):
   clientMutationId: str
   items: YMHGF_ProjectV2ItemConnection_Field

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
