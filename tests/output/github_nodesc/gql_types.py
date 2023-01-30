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
   avatarUrl: FKOKY_URI_Field
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
   labelIds: NonNull_list[ID]
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
   avatarUrl: MJJUJ_URI_Field
   login: str
   resourcePath: URI
   url: URI

class AcceptEnterpriseAdministratorInvitationInput(GQLObject):
   invitationId: ID
   clientMutationId: str

class AbortQueuedMigrationsInput(GQLObject):
   ownerId: ID
   clientMutationId: str

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
   avatarUrl: OHFBC_URI_Field
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

class OFRTU_ReactionConnection_Field(ReactionConnection):
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
   reactions: OFRTU_ReactionConnection_Field
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

class HLLTT_ReactorConnection_Field(ReactorConnection):
   class ReactorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ReactorConnectionArgs



class ReactionGroup(GQLObject):
   content: ReactionContent
   createdAt: DateTime
   reactors: HLLTT_ReactorConnection_Field
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

class SLKQS_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class HBACL_UserContentEditConnection_Field(UserContentEditConnection):
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
   reactions: SLKQS_ReactionConnection_Field
   resourcePath: URI
   updatedAt: DateTime
   url: URI
   userContentEdits: HBACL_UserContentEditConnection_Field
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

class PRQQM_TeamDiscussionCommentConnection_Field(TeamDiscussionCommentConnection):
   class TeamDiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: TeamDiscussionCommentOrder
      fromComment: int

   _args: TeamDiscussionCommentConnectionArgs



class TRDYG_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class BMEKM_UserContentEditConnection_Field(UserContentEditConnection):
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
   comments: PRQQM_TeamDiscussionCommentConnection_Field
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
   reactions: TRDYG_ReactionConnection_Field
   resourcePath: URI
   team: NewType('Team', GQLObject) ## Circular Reference for Team
   title: str
   updatedAt: DateTime
   url: URI
   userContentEdits: BMEKM_UserContentEditConnection_Field
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

class IZINN_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class KAOJE_ProjectV2ItemConnection_Field(Generic[ProjectV2ItemConnection]):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class TXLKA_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class DraftIssue(GQLObject):
   assignees: IZINN_UserConnection_Field
   body: str
   bodyHTML: HTML
   bodyText: str
   createdAt: DateTime
   creator: Actor
   id: ID
   projectV2Items: KAOJE_ProjectV2ItemConnection_Field ## Circular Reference for ProjectV2ItemConnection
   projectsV2: TXLKA_ProjectV2Connection_Field
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

class LQYWX_DeploymentStatusConnection_Field(DeploymentStatusConnection):
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
   statuses: LQYWX_DeploymentStatusConnection_Field
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

class EWNEX_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class YJYHF_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DiscussionCommentConnectionArgs



class WHFCM_UserContentEditConnection_Field(UserContentEditConnection):
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
   reactions: EWNEX_ReactionConnection_Field
   replies: YJYHF_DiscussionCommentConnection_Field
   replyTo: NewType('DiscussionComment', GQLObject) ## Circular Reference for DiscussionComment
   resourcePath: URI
   updatedAt: DateTime
   upvoteCount: int
   url: URI
   userContentEdits: WHFCM_UserContentEditConnection_Field
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

class KNSIM_IssueConnection_Field(IssueConnection):
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

class DBFSH_PullRequestConnection_Field(Generic[PullRequestConnection]):
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
   issues: KNSIM_IssueConnection_Field
   name: str
   pullRequests: DBFSH_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
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

class DSYWN_DiscussionPollOptionConnection_Field(DiscussionPollOptionConnection):
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
   options: DSYWN_DiscussionPollOptionConnection_Field
   question: str
   totalVoteCount: int
   viewerCanVote: bool
   viewerHasVoted: bool

class QITAG_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DiscussionCommentConnectionArgs



class OGNZN_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class RLKBM_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class XUWNT_UserContentEditConnection_Field(UserContentEditConnection):
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
   comments: QITAG_DiscussionCommentConnection_Field
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   labels: OGNZN_LabelConnection_Field
   lastEditedAt: DateTime
   locked: bool
   number: int
   poll: DiscussionPoll
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: RLKBM_ReactionConnection_Field
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   resourcePath: URI
   title: str
   updatedAt: DateTime
   upvoteCount: int
   url: URI
   userContentEdits: XUWNT_UserContentEditConnection_Field
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

class NEPFI_DeploymentReviewerConnection_Field(DeploymentReviewerConnection):
   class DeploymentReviewerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewerConnectionArgs



class DeploymentProtectionRule(GQLObject):
   databaseId: int
   reviewers: NEPFI_DeploymentReviewerConnection_Field
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

class ASIVS_DeploymentProtectionRuleConnection_Field(DeploymentProtectionRuleConnection):
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
   protectionRules: ASIVS_DeploymentProtectionRuleConnection_Field

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

class MSUSE_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class YKUEB_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class RNCWW_ReleaseAssetConnection_Field(ReleaseAssetConnection):
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
   mentions: MSUSE_UserConnection_Field
   name: str
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: YKUEB_ReactionConnection_Field
   releaseAssets: RNCWW_ReleaseAssetConnection_Field
   repository: NewType('Repository', GQLObject) ## Circular Reference for Repository
   resourcePath: URI
   shortDescriptionHTML: WQJYH_HTML_Field
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

class SHKKW_IssueConnection_Field(IssueConnection):
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



class KUTFH_PullRequestConnection_Field(Generic[PullRequestConnection]):
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
   issues: SHKKW_IssueConnection_Field
   number: int
   progressPercentage: float
   pullRequests: KUTFH_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
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

class DDCDT_RepositoryConnection_Field(RepositoryConnection):
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



class KNVEY_Repository_Field(Generic[Repository]):
   class RepositoryArgs(GQLArgsSet, GQLObject):
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs



class RepositoryOwner(GQLObject):
   avatarUrl: GCHYR_URI_Field
   id: ID
   login: str
   repositories: DDCDT_RepositoryConnection_Field
   repository: KNVEY_Repository_Field ## Circular Reference for Repository
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

class GCKFH_PackageFileConnection_Field(PackageFileConnection):
   class PackageFileConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: PackageFileOrder
      after: str
      before: str
      first: int
      last: int

   _args: PackageFileConnectionArgs



class PackageVersion(GQLObject):
   files: GCKFH_PackageFileConnection_Field
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

class IYSNU_PackageVersion_Field(PackageVersion):
   class PackageVersionArgs(GQLArgsSet, GQLObject):
      version: NonNull_str

   _args: PackageVersionArgs



class RWCYS_PackageVersionConnection_Field(PackageVersionConnection):
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
   version: IYSNU_PackageVersion_Field
   versions: RWCYS_PackageVersionConnection_Field

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

class WOWCE_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: ProjectCardConnectionArgs



class ProjectColumn(GQLObject):
   cards: WOWCE_ProjectCardConnection_Field
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

class QMCQS_Project_Field(Generic[Project]):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class NonNull_ProjectState(GQLObject): pass

class BHECN_ProjectConnection_Field(ProjectConnection):
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
   project: QMCQS_Project_Field ## Circular Reference for Project
   projects: BHECN_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   viewerCanCreateProjects: bool

class FIFQE_ProjectColumnConnection_Field(ProjectColumnConnection):
   class ProjectColumnConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectColumnConnectionArgs



class UNXFF_ProjectCardConnection_Field(ProjectCardConnection):
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
   columns: FIFQE_ProjectColumnConnection_Field
   createdAt: DateTime
   creator: Actor
   databaseId: int
   id: ID
   name: str
   number: int
   owner: ProjectOwner
   pendingCards: UNXFF_ProjectCardConnection_Field
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

class SWZXB_Topic_Field(Generic[Topic]):
   class TopicArgs(GQLArgsSet, GQLObject):
      first: int

   _args: TopicArgs



class WENPZ_RepositoryConnection_Field(RepositoryConnection):
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



class AIVOP_StargazerConnection_Field(StargazerConnection):
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
   relatedTopics: SWZXB_Topic_Field ## Circular Reference for Topic
   repositories: WENPZ_RepositoryConnection_Field
   stargazerCount: int
   stargazers: AIVOP_StargazerConnection_Field
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

class GCHPR_CWEConnection_Field(CWEConnection):
   class CWEConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CWEConnectionArgs



class NonNull_SecurityAdvisorySeverity(GQLObject): pass

class NonNull_SecurityAdvisoryClassification(GQLObject): pass

class TWZFB_SecurityVulnerabilityConnection_Field(SecurityVulnerabilityConnection):
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
   cwes: GCHPR_CWEConnection_Field
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
   vulnerabilities: TWZFB_SecurityVulnerabilityConnection_Field
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

class ATLLS_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class KXWJQ_BranchProtectionRuleConnection_Field(BranchProtectionRuleConnection):
   class BranchProtectionRuleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BranchProtectionRuleConnectionArgs



class YMGNL_RepositoryCodeowners_Field(RepositoryCodeowners):
   class RepositoryCodeownersArgs(GQLArgsSet, GQLObject):
      refName: str

   _args: RepositoryCodeownersArgs



class ZURLP_RepositoryCollaboratorConnection_Field(RepositoryCollaboratorConnection):
   class RepositoryCollaboratorConnectionArgs(GQLArgsSet, GQLObject):
      affiliation: CollaboratorAffiliation
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryCollaboratorConnectionArgs



class LGPLB_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class list_RepositoryContactLink(list, RepositoryContactLink): pass

class KIAFE_DeployKeyConnection_Field(DeployKeyConnection):
   class DeployKeyConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeployKeyConnectionArgs



class FYCBW_DeploymentConnection_Field(DeploymentConnection):
   class DeploymentConnectionArgs(GQLArgsSet, GQLObject):
      environments: list[NonNull_str]
      orderBy: DeploymentOrder
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentConnectionArgs



class FYVDE_Discussion_Field(Discussion):
   class DiscussionArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: DiscussionArgs



class CKZBX_DiscussionCategoryConnection_Field(DiscussionCategoryConnection):
   class DiscussionCategoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      filterByAssignable: bool

   _args: DiscussionCategoryConnectionArgs



class UJNXV_DiscussionCategory_Field(DiscussionCategory):
   class DiscussionCategoryArgs(GQLArgsSet, GQLObject):
      slug: NonNull_str

   _args: DiscussionCategoryArgs



class YVXKL_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      categoryId: ID
      orderBy: DiscussionOrder

   _args: DiscussionConnectionArgs



class FBQHB_Environment_Field(Environment):
   class EnvironmentArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: EnvironmentArgs



class URDHG_EnvironmentConnection_Field(EnvironmentConnection):
   class EnvironmentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: EnvironmentConnectionArgs



class SVKWE_RepositoryConnection_Field(RepositoryConnection):
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



class FQSAR_Issue_Field(Generic[Issue]):
   class IssueArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: IssueArgs



class CIQHN_IssueOrPullRequest_Field(IssueOrPullRequest):
   class IssueOrPullRequestArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: IssueOrPullRequestArgs



class list_IssueTemplate(list, IssueTemplate): pass

class RXXVR_IssueConnection_Field(IssueConnection):
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



class GCXYO_Label_Field(Label):
   class LabelArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: LabelArgs



class TYCAN_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int
      query: str

   _args: LabelConnectionArgs



class DJNGM_LanguageConnection_Field(LanguageConnection):
   class LanguageConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: LanguageOrder

   _args: LanguageConnectionArgs



class JHBJD_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class MGNMP_Milestone_Field(Milestone):
   class MilestoneArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: MilestoneArgs



class NonNull_MilestoneState(GQLObject): pass

class MFLFB_MilestoneConnection_Field(MilestoneConnection):
   class MilestoneConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      states: list[NonNull_MilestoneState]
      orderBy: MilestoneOrder
      query: str

   _args: MilestoneConnectionArgs



class RWDOJ_GitObject_Field(GitObject):
   class GitObjectArgs(GQLArgsSet, GQLObject):
      oid: GitObjectID
      expression: str

   _args: GitObjectArgs



class NLUDN_PackageConnection_Field(PackageConnection):
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



class GBEQU_PinnedDiscussionConnection_Field(PinnedDiscussionConnection):
   class PinnedDiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PinnedDiscussionConnectionArgs



class XVIQD_PinnedIssueConnection_Field(PinnedIssueConnection):
   class PinnedIssueConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PinnedIssueConnectionArgs



class NGESH_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class FFFAZ_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class NCUJT_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: ProjectOrder
      search: str
      states: list[NonNull_ProjectState]
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class OXWDH_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: ProjectV2Order

   _args: ProjectV2ConnectionArgs



class HMQUB_PullRequest_Field(Generic[PullRequest]):
   class PullRequestArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: PullRequestArgs



class list_PullRequestTemplate(list, PullRequestTemplate): pass

class PFBUV_PullRequestConnection_Field(Generic[PullRequestConnection]):
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



class HKSDH_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class PDUSE_Ref_Field(Generic[Ref]):
   class RefArgs(GQLArgsSet, GQLObject):
      qualifiedName: NonNull_str

   _args: RefArgs



class RCZFW_RefConnection_Field(RefConnection):
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



class KCQQV_Release_Field(Release):
   class ReleaseArgs(GQLArgsSet, GQLObject):
      tagName: NonNull_str

   _args: ReleaseArgs



class HZWUY_ReleaseConnection_Field(ReleaseConnection):
   class ReleaseConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ReleaseOrder

   _args: ReleaseConnectionArgs



class NICKN_RepositoryTopicConnection_Field(RepositoryTopicConnection):
   class RepositoryTopicConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryTopicConnectionArgs



class BHDKK_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class KJJCF_SubmoduleConnection_Field(SubmoduleConnection):
   class SubmoduleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: SubmoduleConnectionArgs



class NonNull_RepositoryVulnerabilityAlertState(GQLObject): pass

class NonNull_RepositoryVulnerabilityAlertDependencyScope(GQLObject): pass

class FYPEO_RepositoryVulnerabilityAlertConnection_Field(RepositoryVulnerabilityAlertConnection):
   class RepositoryVulnerabilityAlertConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      states: list[NonNull_RepositoryVulnerabilityAlertState]
      dependencyScopes: list[NonNull_RepositoryVulnerabilityAlertDependencyScope]

   _args: RepositoryVulnerabilityAlertConnectionArgs



class YMGYF_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class Repository(GQLObject):
   allowUpdateBranch: bool
   assignableUsers: ATLLS_UserConnection_Field
   autoMergeAllowed: bool
   branchProtectionRules: KXWJQ_BranchProtectionRuleConnection_Field
   codeOfConduct: CodeOfConduct
   codeowners: YMGNL_RepositoryCodeowners_Field
   collaborators: ZURLP_RepositoryCollaboratorConnection_Field
   commitComments: LGPLB_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
   contactLinks: list_RepositoryContactLink[RepositoryContactLink]
   createdAt: DateTime
   databaseId: int
   defaultBranchRef: NewType('Ref', GQLObject) ## Circular Reference for Ref
   deleteBranchOnMerge: bool
   deployKeys: KIAFE_DeployKeyConnection_Field
   deployments: FYCBW_DeploymentConnection_Field
   description: str
   descriptionHTML: HTML
   discussion: FYVDE_Discussion_Field
   discussionCategories: CKZBX_DiscussionCategoryConnection_Field
   discussionCategory: UJNXV_DiscussionCategory_Field
   discussions: YVXKL_DiscussionConnection_Field
   diskUsage: int
   environment: FBQHB_Environment_Field
   environments: URDHG_EnvironmentConnection_Field
   forkCount: int
   forkingAllowed: bool
   forks: SVKWE_RepositoryConnection_Field
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
   issue: FQSAR_Issue_Field ## Circular Reference for Issue
   issueOrPullRequest: CIQHN_IssueOrPullRequest_Field
   issueTemplates: list_IssueTemplate[IssueTemplate]
   issues: RXXVR_IssueConnection_Field
   label: GCXYO_Label_Field
   labels: TYCAN_LabelConnection_Field
   languages: DJNGM_LanguageConnection_Field
   latestRelease: Release
   licenseInfo: License
   lockReason: RepositoryLockReason
   mentionableUsers: JHBJD_UserConnection_Field
   mergeCommitAllowed: bool
   mergeCommitMessage: MergeCommitMessage
   mergeCommitTitle: MergeCommitTitle
   milestone: MGNMP_Milestone_Field
   milestones: MFLFB_MilestoneConnection_Field
   mirrorUrl: URI
   name: str
   nameWithOwner: str
   object: RWDOJ_GitObject_Field
   openGraphImageUrl: URI
   owner: RepositoryOwner
   packages: NLUDN_PackageConnection_Field
   parent: NewType('Repository', GQLObject) ## Circular Reference for Repository
   pinnedDiscussions: GBEQU_PinnedDiscussionConnection_Field
   pinnedIssues: XVIQD_PinnedIssueConnection_Field
   primaryLanguage: Language
   project: NGESH_Project_Field
   projectV2: FFFAZ_ProjectV2_Field ## Circular Reference for ProjectV2
   projects: NCUJT_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   projectsV2: OXWDH_ProjectV2Connection_Field
   pullRequest: HMQUB_PullRequest_Field ## Circular Reference for PullRequest
   pullRequestTemplates: list_PullRequestTemplate[PullRequestTemplate]
   pullRequests: PFBUV_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   pushedAt: DateTime
   rebaseMergeAllowed: bool
   recentProjects: HKSDH_ProjectV2Connection_Field
   ref: PDUSE_Ref_Field ## Circular Reference for Ref
   refs: RCZFW_RefConnection_Field
   release: KCQQV_Release_Field
   releases: HZWUY_ReleaseConnection_Field
   repositoryTopics: NICKN_RepositoryTopicConnection_Field
   resourcePath: URI
   securityPolicyUrl: URI
   shortDescriptionHTML: LRQST_HTML_Field
   squashMergeAllowed: bool
   squashMergeCommitMessage: SquashMergeCommitMessage
   squashMergeCommitTitle: SquashMergeCommitTitle
   sshUrl: GitSSHRemote
   stargazerCount: int
   stargazers: BHDKK_StargazerConnection_Field
   submodules: KJJCF_SubmoduleConnection_Field
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
   vulnerabilityAlerts: FYPEO_RepositoryVulnerabilityAlertConnection_Field
   watchers: YMGYF_UserConnection_Field
   webCommitSignoffRequired: bool

class PPNQC_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class PNYAH_UserContentEditConnection_Field(UserContentEditConnection):
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
   reactions: PPNQC_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   updatedAt: DateTime
   url: URI
   userContentEdits: PNYAH_UserContentEditConnection_Field
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

class UVPRP_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class Assignable(GQLObject):
   assignees: UVPRP_UserConnection_Field

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

class IBJMO_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class Labelable(GQLObject):
   labels: IBJMO_LabelConnection_Field

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

class WYOGC_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class EVIIN_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class HTFVM_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject):
      includeNotificationContexts: bool

   _args: HovercardArgs



class LCZIB_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class JDRQU_LinkedBranchConnection_Field(LinkedBranchConnection):
   class LinkedBranchConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: LinkedBranchConnectionArgs



class IRKHL_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class QQEEY_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: ProjectCardConnectionArgs



class LTBLT_ProjectV2ItemConnection_Field(Generic[ProjectV2ItemConnection]):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class HPSHE_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class DNOKX_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class KDQIG_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class NonNull_IssueTimelineItemsItemType(GQLObject): pass

class BREAH_IssueTimelineItemsConnection_Field(IssueTimelineItemsConnection):
   class IssueTimelineItemsConnectionArgs(GQLArgsSet, GQLObject):
      since: DateTime
      skip: int
      itemTypes: list[NonNull_IssueTimelineItemsItemType]
      after: str
      before: str
      first: int
      last: int

   _args: IssueTimelineItemsConnectionArgs



class PRSXU_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class BHALD_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class WYHKN_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class Issue(GQLObject):
   activeLockReason: LockReason
   assignees: WYOGC_UserConnection_Field
   author: Actor
   authorAssociation: CommentAuthorAssociation
   body: str
   bodyHTML: HTML
   bodyResourcePath: URI
   bodyText: str
   bodyUrl: URI
   closed: bool
   closedAt: DateTime
   comments: EVIIN_IssueCommentConnection_Field
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   hovercard: HTFVM_Hovercard_Field
   id: ID
   includesCreatedEdit: bool
   isPinned: bool
   isReadByViewer: bool
   labels: LCZIB_LabelConnection_Field
   lastEditedAt: DateTime
   linkedBranches: JDRQU_LinkedBranchConnection_Field
   locked: bool
   milestone: Milestone
   number: int
   participants: IRKHL_UserConnection_Field
   projectCards: QQEEY_ProjectCardConnection_Field
   projectItems: LTBLT_ProjectV2ItemConnection_Field ## Circular Reference for ProjectV2ItemConnection
   projectV2: HPSHE_ProjectV2_Field ## Circular Reference for ProjectV2
   projectsV2: DNOKX_ProjectV2Connection_Field
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: KDQIG_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   state: IssueState
   stateReason: IssueStateReason
   timelineItems: BREAH_IssueTimelineItemsConnection_Field
   title: str
   titleHTML: str
   trackedInIssues: PRSXU_IssueConnection_Field
   trackedIssues: BHALD_IssueConnection_Field
   trackedIssuesCount: GKNMZ_trackedIssuesCount_Field
   updatedAt: DateTime
   url: URI
   userContentEdits: WYHKN_UserContentEditConnection_Field
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

class UVHDM_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class ProjectV2ItemFieldLabelValue(GQLObject):
   field: ProjectV2FieldConfiguration
   labels: UVHDM_LabelConnection_Field

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

class ACZBB_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: PullRequestOrder

   _args: PullRequestConnectionArgs



class ProjectV2ItemFieldPullRequestValue(GQLObject):
   field: ProjectV2FieldConfiguration
   pullRequests: ACZBB_PullRequestConnection_Field ## Circular Reference for PullRequestConnection

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

class NOCFY_RequestedReviewerConnection_Field(RequestedReviewerConnection):
   class RequestedReviewerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: RequestedReviewerConnectionArgs



class ProjectV2ItemFieldReviewerValue(GQLObject):
   field: ProjectV2FieldConfiguration
   reviewers: NOCFY_RequestedReviewerConnection_Field

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

class OZZRF_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class ProjectV2ItemFieldUserValue(GQLObject):
   field: ProjectV2FieldConfiguration
   users: OZZRF_UserConnection_Field

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

class JAWUI_ProjectV2ItemFieldValue_Field(ProjectV2ItemFieldValue):
   class ProjectV2ItemFieldValueArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: ProjectV2ItemFieldValueArgs



class TYAPM_ProjectV2ItemFieldValueConnection_Field(ProjectV2ItemFieldValueConnection):
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
   fieldValueByName: JAWUI_ProjectV2ItemFieldValue_Field
   fieldValues: TYAPM_ProjectV2ItemFieldValueConnection_Field
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

class YIJUA_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class IDZQI_ProjectV2Connection_Field(ProjectV2Connection):
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
   projectV2: YIJUA_ProjectV2_Field ## Circular Reference for ProjectV2
   projectsV2: IDZQI_ProjectV2Connection_Field

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

class CVLMM_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class SDHAZ_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class JPYBG_ProjectV2SortByFieldConnection_Field(ProjectV2SortByFieldConnection):
   class ProjectV2SortByFieldConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2SortByFieldConnectionArgs



class EPHXZ_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
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
   fields: CVLMM_ProjectV2FieldConfigurationConnection_Field
   filter: str
   groupByFields: SDHAZ_ProjectV2FieldConfigurationConnection_Field
   id: ID
   layout: ProjectV2ViewLayout
   name: str
   number: int
   project: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2
   sortByFields: JPYBG_ProjectV2SortByFieldConnection_Field
   updatedAt: DateTime
   verticalGroupByFields: EPHXZ_ProjectV2FieldConfigurationConnection_Field

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

class GFSHD_ProjectV2FieldConfiguration_Field(ProjectV2FieldConfiguration):
   class ProjectV2FieldConfigurationArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: ProjectV2FieldConfigurationArgs



class MXWOR_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class YMTCA_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ItemOrder

   _args: ProjectV2ItemConnectionArgs



class BCRYO_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: RepositoryOrder

   _args: RepositoryConnectionArgs



class WGOSN_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: TeamOrder

   _args: TeamConnectionArgs



class ZPLAG_ProjectV2View_Field(ProjectV2View):
   class ProjectV2ViewArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2ViewArgs



class VOUKG_ProjectV2ViewConnection_Field(ProjectV2ViewConnection):
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
   field: GFSHD_ProjectV2FieldConfiguration_Field
   fields: MXWOR_ProjectV2FieldConfigurationConnection_Field
   id: ID
   items: YMTCA_ProjectV2ItemConnection_Field
   number: int
   owner: ProjectV2Owner
   public: bool
   readme: str
   repositories: BCRYO_RepositoryConnection_Field
   resourcePath: URI
   shortDescription: str
   teams: WGOSN_TeamConnection_Field
   title: str
   updatedAt: DateTime
   url: URI
   view: ZPLAG_ProjectV2View_Field
   viewerCanUpdate: bool
   views: VOUKG_ProjectV2ViewConnection_Field

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

class NBJVT_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class ORAQX_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: TeamOrder
      userLogins: list[NonNull_str]
      immediateOnly: bool
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class IHBXU_TeamDiscussion_Field(TeamDiscussion):
   class TeamDiscussionArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: TeamDiscussionArgs



class PMJNR_TeamDiscussionConnection_Field(TeamDiscussionConnection):
   class TeamDiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      isPinned: bool
      orderBy: TeamDiscussionOrder

   _args: TeamDiscussionConnectionArgs



class GIVQZ_OrganizationInvitationConnection_Field(OrganizationInvitationConnection):
   class OrganizationInvitationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationInvitationConnectionArgs



class SICSY_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class UZLTU_TeamMemberConnection_Field(TeamMemberConnection):
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



class QKZOG_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class RDBUU_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2Order
      filterBy: ProjectV2Filters
      query: str

   _args: ProjectV2ConnectionArgs



class RFBRP_TeamRepositoryConnection_Field(TeamRepositoryConnection):
   class TeamRepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: TeamRepositoryOrder

   _args: TeamRepositoryConnectionArgs



class Team(GQLObject):
   ancestors: NBJVT_TeamConnection_Field
   avatarUrl: TAJTM_URI_Field
   childTeams: ORAQX_TeamConnection_Field
   combinedSlug: str
   createdAt: DateTime
   databaseId: int
   description: str
   discussion: IHBXU_TeamDiscussion_Field
   discussions: PMJNR_TeamDiscussionConnection_Field
   discussionsResourcePath: URI
   discussionsUrl: URI
   editTeamResourcePath: URI
   editTeamUrl: URI
   id: ID
   invitations: GIVQZ_OrganizationInvitationConnection_Field
   memberStatuses: SICSY_UserStatusConnection_Field
   members: UZLTU_TeamMemberConnection_Field
   membersResourcePath: URI
   membersUrl: URI
   name: str
   newTeamResourcePath: URI
   newTeamUrl: URI
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   parentTeam: NewType('Team', GQLObject) ## Circular Reference for Team
   privacy: TeamPrivacy
   projectV2: QKZOG_ProjectV2_Field
   projectsV2: RDBUU_ProjectV2Connection_Field
   repositories: RFBRP_TeamRepositoryConnection_Field
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

class MOCSQ_BranchProtectionRuleConflictConnection_Field(BranchProtectionRuleConflictConnection):
   class BranchProtectionRuleConflictConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BranchProtectionRuleConflictConnectionArgs



class OXQJF_BypassForcePushAllowanceConnection_Field(BypassForcePushAllowanceConnection):
   class BypassForcePushAllowanceConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BypassForcePushAllowanceConnectionArgs



class TVMSM_BypassPullRequestAllowanceConnection_Field(BypassPullRequestAllowanceConnection):
   class BypassPullRequestAllowanceConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: BypassPullRequestAllowanceConnectionArgs



class WYGOI_RefConnection_Field(RefConnection):
   class RefConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: RefConnectionArgs



class TVDEC_PushAllowanceConnection_Field(PushAllowanceConnection):
   class PushAllowanceConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PushAllowanceConnectionArgs



class list_RequiredStatusCheckDescription(list, RequiredStatusCheckDescription): pass

class TZEEA_ReviewDismissalAllowanceConnection_Field(ReviewDismissalAllowanceConnection):
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
   branchProtectionRuleConflicts: MOCSQ_BranchProtectionRuleConflictConnection_Field
   bypassForcePushAllowances: OXQJF_BypassForcePushAllowanceConnection_Field
   bypassPullRequestAllowances: TVMSM_BypassPullRequestAllowanceConnection_Field
   creator: Actor
   databaseId: int
   dismissesStaleReviews: bool
   id: ID
   isAdminEnforced: bool
   lockAllowsFetchAndMerge: bool
   lockBranch: bool
   matchingRefs: WYGOI_RefConnection_Field
   pattern: str
   pushAllowances: TVDEC_PushAllowanceConnection_Field
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
   reviewDismissalAllowances: TZEEA_ReviewDismissalAllowanceConnection_Field

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

class FCFZW_ComparisonCommitConnection_Field(ComparisonCommitConnection):
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
   commits: FCFZW_ComparisonCommitConnection_Field
   headTarget: GitObject
   id: ID
   status: ComparisonStatus

class DNMRB_PullRequestConnection_Field(Generic[PullRequestConnection]):
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



class HEKRL_Comparison_Field(Comparison):
   class ComparisonArgs(GQLArgsSet, GQLObject):
      headRef: NonNull_str

   _args: ComparisonArgs



class Ref(GQLObject):
   associatedPullRequests: DNMRB_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   branchProtectionRule: BranchProtectionRule
   compare: HEKRL_Comparison_Field
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

class MNXTI_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class LEDAE_UserContentEditConnection_Field(UserContentEditConnection):
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
   reactions: MNXTI_ReactionConnection_Field
   replyTo: NewType('PullRequestReviewComment', GQLObject) ## Circular Reference for PullRequestReviewComment
   repository: Repository
   resourcePath: URI
   state: PullRequestReviewCommentState
   updatedAt: DateTime
   url: URI
   userContentEdits: LEDAE_UserContentEditConnection_Field
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

class RTOCA_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewCommentConnectionArgs



class KJESP_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class AKGXV_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class OVWNR_UserContentEditConnection_Field(UserContentEditConnection):
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
   comments: RTOCA_PullRequestReviewCommentConnection_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   editor: Actor
   id: ID
   includesCreatedEdit: bool
   lastEditedAt: DateTime
   onBehalfOf: KJESP_TeamConnection_Field
   publishedAt: DateTime
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: AKGXV_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   state: PullRequestReviewState
   submittedAt: DateTime
   updatedAt: DateTime
   url: URI
   userContentEdits: OVWNR_UserContentEditConnection_Field
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

class TARBY_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      skip: int

   _args: PullRequestReviewCommentConnectionArgs



class PullRequestReviewThread(GQLObject):
   comments: TARBY_PullRequestReviewCommentConnection_Field
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

class BLZPC_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class CommitCommentThread(GQLObject):
   comments: BLZPC_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
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

class GDYJX_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class PullRequestCommitCommentThread(GQLObject):
   comments: GDYJX_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
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

class KSVEB_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class RQNWT_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject):
      userLinkedOnly: bool
      after: str
      before: str
      first: int
      last: int
      orderBy: IssueOrder

   _args: IssueConnectionArgs



class GHLWN_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class FTAHL_PullRequestCommitConnection_Field(PullRequestCommitConnection):
   class PullRequestCommitConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestCommitConnectionArgs



class EEYEB_PullRequestChangedFileConnection_Field(PullRequestChangedFileConnection):
   class PullRequestChangedFileConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestChangedFileConnectionArgs



class GYCDI_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject):
      includeNotificationContexts: bool

   _args: HovercardArgs



class QQBMI_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class ZODCZ_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      writersOnly: bool

   _args: PullRequestReviewConnectionArgs



class HJSUE_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewConnectionArgs



class QYTER_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class VFXZW_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: ProjectCardConnectionArgs



class LRRII_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class RIZTB_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class FPOXK_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class JHUGT_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class DYSID_ReviewRequestConnection_Field(ReviewRequestConnection):
   class ReviewRequestConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ReviewRequestConnectionArgs



class IJKNU_PullRequestReviewThreadConnection_Field(PullRequestReviewThreadConnection):
   class PullRequestReviewThreadConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewThreadConnectionArgs



class NonNull_PullRequestReviewState(GQLObject): pass

class JTRJY_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      states: list[NonNull_PullRequestReviewState]
      author: str

   _args: PullRequestReviewConnectionArgs



class NonNull_PullRequestTimelineItemsItemType(GQLObject): pass

class OJHKV_PullRequestTimelineItemsConnection_Field(PullRequestTimelineItemsConnection):
   class PullRequestTimelineItemsConnectionArgs(GQLArgsSet, GQLObject):
      since: DateTime
      skip: int
      itemTypes: list[NonNull_PullRequestTimelineItemsItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestTimelineItemsConnectionArgs



class KTQFL_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class PullRequest(GQLObject):
   activeLockReason: LockReason
   additions: int
   assignees: KSVEB_UserConnection_Field
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
   closingIssuesReferences: RQNWT_IssueConnection_Field
   comments: GHLWN_IssueCommentConnection_Field
   commits: FTAHL_PullRequestCommitConnection_Field
   createdAt: DateTime
   createdViaEmail: bool
   databaseId: int
   deletions: int
   editor: Actor
   files: EEYEB_PullRequestChangedFileConnection_Field
   headRef: Ref
   headRefName: str
   headRefOid: GitObjectID
   headRepository: Repository
   headRepositoryOwner: RepositoryOwner
   hovercard: GYCDI_Hovercard_Field
   id: ID
   includesCreatedEdit: bool
   isCrossRepository: bool
   isDraft: bool
   isReadByViewer: bool
   labels: QQBMI_LabelConnection_Field
   lastEditedAt: DateTime
   latestOpinionatedReviews: ZODCZ_PullRequestReviewConnection_Field
   latestReviews: HJSUE_PullRequestReviewConnection_Field
   locked: bool
   maintainerCanModify: bool
   mergeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   mergeable: MergeableState
   merged: bool
   mergedAt: DateTime
   mergedBy: Actor
   milestone: Milestone
   number: int
   participants: QYTER_UserConnection_Field
   permalink: URI
   potentialMergeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   projectCards: VFXZW_ProjectCardConnection_Field
   projectItems: LRRII_ProjectV2ItemConnection_Field
   projectV2: RIZTB_ProjectV2_Field
   projectsV2: FPOXK_ProjectV2Connection_Field
   publishedAt: DateTime
   reactionGroups: list_ReactionGroup[ReactionGroup]
   reactions: JHUGT_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   revertResourcePath: URI
   revertUrl: URI
   reviewDecision: PullRequestReviewDecision
   reviewRequests: DYSID_ReviewRequestConnection_Field
   reviewThreads: IJKNU_PullRequestReviewThreadConnection_Field
   reviews: JTRJY_PullRequestReviewConnection_Field
   state: PullRequestState
   suggestedReviewers: SuggestedReviewer
   timelineItems: OJHKV_PullRequestTimelineItemsConnection_Field
   title: str
   titleHTML: HTML
   totalCommentsCount: int
   updatedAt: DateTime
   url: URI
   userContentEdits: KTQFL_UserContentEditConnection_Field
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
   viewerMergeBodyText: ULLSC_viewerMergeBodyText_Field
   viewerMergeHeadlineText: QNEME_viewerMergeHeadlineText_Field
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
   avatarUrl: LHKDV_URI_Field
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

class HHUJB_DeploymentReviewerConnection_Field(DeploymentReviewerConnection):
   class DeploymentReviewerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewerConnectionArgs



class DeploymentRequest(GQLObject):
   currentUserCanApprove: bool
   environment: Environment
   reviewers: HHUJB_DeploymentReviewerConnection_Field
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

class CVMMT_CheckAnnotationConnection_Field(CheckAnnotationConnection):
   class CheckAnnotationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CheckAnnotationConnectionArgs



class DIUDG_CheckStepConnection_Field(CheckStepConnection):
   class CheckStepConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      number: int

   _args: CheckStepConnectionArgs



class CheckRun(GQLObject):
   annotations: CVMMT_CheckAnnotationConnection_Field
   checkSuite: NewType('CheckSuite', GQLObject) ## Circular Reference for CheckSuite
   completedAt: DateTime
   conclusion: CheckConclusionState
   databaseId: int
   deployment: Deployment
   detailsUrl: URI
   externalId: str
   id: ID
   isRequired: QBHRC_isRequired_Field
   name: str
   pendingDeploymentRequest: DeploymentRequest
   permalink: URI
   repository: Repository
   resourcePath: URI
   startedAt: DateTime
   status: CheckStatusState
   steps: DIUDG_CheckStepConnection_Field
   summary: str
   text: str
   title: str
   url: URI

class StatusContext(GQLObject):
   avatarUrl: LNEYZ_URI_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   context: str
   createdAt: DateTime
   creator: Actor
   description: str
   id: ID
   isRequired: JVVIJ_isRequired_Field
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

class WXXRA_StatusCheckRollupContextConnection_Field(StatusCheckRollupContextConnection):
   class StatusCheckRollupContextConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: StatusCheckRollupContextConnectionArgs



class DLDBD_StatusContext_Field(StatusContext):
   class StatusContextArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: StatusContextArgs



class Status(GQLObject):
   combinedContexts: WXXRA_StatusCheckRollupContextConnection_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   context: DLDBD_StatusContext_Field
   contexts: StatusContext
   id: ID
   state: StatusState

class IKXML_StatusCheckRollupContextConnection_Field(StatusCheckRollupContextConnection):
   class StatusCheckRollupContextConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: StatusCheckRollupContextConnectionArgs



class StatusCheckRollup(GQLObject):
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   contexts: IKXML_StatusCheckRollupContextConnection_Field
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

class KNSJI_PullRequestConnection_Field(PullRequestConnection):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: PullRequestOrder

   _args: PullRequestConnectionArgs



class ERAPK_GitActorConnection_Field(GitActorConnection):
   class GitActorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: GitActorConnectionArgs



class YVQTR_Blame_Field(Blame):
   class BlameArgs(GQLArgsSet, GQLObject):
      path: NonNull_str

   _args: BlameArgs



class QWKCQ_CheckSuiteConnection_Field(CheckSuiteConnection):
   class CheckSuiteConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      filterBy: CheckSuiteFilter

   _args: CheckSuiteConnectionArgs



class IFFLO_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class CIRXU_DeploymentConnection_Field(DeploymentConnection):
   class DeploymentConnectionArgs(GQLArgsSet, GQLObject):
      environments: list[NonNull_str]
      orderBy: DeploymentOrder
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentConnectionArgs



class HBSRF_TreeEntry_Field(TreeEntry):
   class TreeEntryArgs(GQLArgsSet, GQLObject):
      path: NonNull_str

   _args: TreeEntryArgs



class JKZWE_CommitHistoryConnection_Field(CommitHistoryConnection):
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



class EXEZT_CommitConnection_Field(CommitConnection):
   class CommitConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitConnectionArgs



class UXESY_SubmoduleConnection_Field(SubmoduleConnection):
   class SubmoduleConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: SubmoduleConnectionArgs



class Commit(GQLObject):
   abbreviatedOid: str
   additions: int
   associatedPullRequests: KNSJI_PullRequestConnection_Field
   author: GitActor
   authoredByCommitter: bool
   authoredDate: DateTime
   authors: ERAPK_GitActorConnection_Field
   blame: YVQTR_Blame_Field
   changedFilesIfAvailable: int
   checkSuites: QWKCQ_CheckSuiteConnection_Field
   comments: IFFLO_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
   commitResourcePath: URI
   commitUrl: URI
   committedDate: DateTime
   committedViaWeb: bool
   committer: GitActor
   deletions: int
   deployments: CIRXU_DeploymentConnection_Field
   file: HBSRF_TreeEntry_Field
   history: JKZWE_CommitHistoryConnection_Field
   id: ID
   message: str
   messageBody: str
   messageBodyHTML: HTML
   messageHeadline: str
   messageHeadlineHTML: HTML
   oid: GitObjectID
   onBehalfOf: NewType('Organization', GQLObject) ## Circular Reference for Organization
   parents: EXEZT_CommitConnection_Field
   pushedDate: DateTime
   repository: Repository
   resourcePath: URI
   signature: GitSignature
   status: Status
   statusCheckRollup: StatusCheckRollup
   submodules: UXESY_SubmoduleConnection_Field
   tarballUrl: URI
   tree: Tree
   treeResourcePath: URI
   treeUrl: URI
   url: URI
   viewerCanSubscribe: bool
   viewerSubscription: SubscriptionState
   zipballUrl: URI

class FMMQT_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class RVFYB_UserContentEditConnection_Field(UserContentEditConnection):
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
   reactions: FMMQT_ReactionConnection_Field
   repository: Repository
   resourcePath: URI
   updatedAt: DateTime
   url: URI
   userContentEdits: RVFYB_UserContentEditConnection_Field
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

class DVQQS_CreatedCommitContributionConnection_Field(CreatedCommitContributionConnection):
   class CreatedCommitContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: CommitContributionOrder

   _args: CreatedCommitContributionConnectionArgs



class CommitContributionsByRepository(GQLObject):
   contributions: DVQQS_CreatedCommitContributionConnection_Field
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

class QEAVJ_CreatedIssueContributionConnection_Field(CreatedIssueContributionConnection):
   class CreatedIssueContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedIssueContributionConnectionArgs



class IssueContributionsByRepository(GQLObject):
   contributions: QEAVJ_CreatedIssueContributionConnection_Field
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

class GCZFY_CreatedPullRequestContributionConnection_Field(CreatedPullRequestContributionConnection):
   class CreatedPullRequestContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestContributionConnectionArgs



class PullRequestContributionsByRepository(GQLObject):
   contributions: GCZFY_CreatedPullRequestContributionConnection_Field
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

class JUFCH_CreatedPullRequestReviewContributionConnection_Field(CreatedPullRequestReviewContributionConnection):
   class CreatedPullRequestReviewContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestReviewContributionConnectionArgs



class PullRequestReviewContributionsByRepository(GQLObject):
   contributions: JUFCH_CreatedPullRequestReviewContributionConnection_Field
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

class DOYDD_CommitContributionsByRepository_Field(CommitContributionsByRepository):
   class CommitContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int

   _args: CommitContributionsByRepositoryArgs



class DYAKT_CreatedIssueContributionConnection_Field(CreatedIssueContributionConnection):
   class CreatedIssueContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      excludePopular: bool
      orderBy: ContributionOrder

   _args: CreatedIssueContributionConnectionArgs



class SMQRI_IssueContributionsByRepository_Field(IssueContributionsByRepository):
   class IssueContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int
      excludeFirst: bool
      excludePopular: bool

   _args: IssueContributionsByRepositoryArgs



class HKRXA_CreatedPullRequestContributionConnection_Field(CreatedPullRequestContributionConnection):
   class CreatedPullRequestContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      excludePopular: bool
      orderBy: ContributionOrder

   _args: CreatedPullRequestContributionConnectionArgs



class CXWBS_PullRequestContributionsByRepository_Field(PullRequestContributionsByRepository):
   class PullRequestContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int
      excludeFirst: bool
      excludePopular: bool

   _args: PullRequestContributionsByRepositoryArgs



class WUPKP_CreatedPullRequestReviewContributionConnection_Field(CreatedPullRequestReviewContributionConnection):
   class CreatedPullRequestReviewContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestReviewContributionConnectionArgs



class QHPNM_PullRequestReviewContributionsByRepository_Field(PullRequestReviewContributionsByRepository):
   class PullRequestReviewContributionsByRepositoryArgs(GQLArgsSet, GQLObject):
      maxRepositories: int

   _args: PullRequestReviewContributionsByRepositoryArgs



class NLCMY_CreatedRepositoryContributionConnection_Field(CreatedRepositoryContributionConnection):
   class CreatedRepositoryContributionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      orderBy: ContributionOrder

   _args: CreatedRepositoryContributionConnectionArgs



class ContributionsCollection(GQLObject):
   commitContributionsByRepository: DOYDD_CommitContributionsByRepository_Field
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
   issueContributions: DYAKT_CreatedIssueContributionConnection_Field
   issueContributionsByRepository: SMQRI_IssueContributionsByRepository_Field
   joinedGitHubContribution: JoinedGitHubContribution
   latestRestrictedContributionDate: Date
   mostRecentCollectionWithActivity: NewType('ContributionsCollection', GQLObject) ## Circular Reference for ContributionsCollection
   mostRecentCollectionWithoutActivity: NewType('ContributionsCollection', GQLObject) ## Circular Reference for ContributionsCollection
   popularIssueContribution: CreatedIssueContribution
   popularPullRequestContribution: CreatedPullRequestContribution
   pullRequestContributions: HKRXA_CreatedPullRequestContributionConnection_Field
   pullRequestContributionsByRepository: CXWBS_PullRequestContributionsByRepository_Field
   pullRequestReviewContributions: WUPKP_CreatedPullRequestReviewContributionConnection_Field
   pullRequestReviewContributionsByRepository: QHPNM_PullRequestReviewContributionsByRepository_Field
   repositoryContributions: NLCMY_CreatedRepositoryContributionConnection_Field
   restrictedContributionsCount: int
   startedAt: DateTime
   totalCommitContributions: int
   totalIssueContributions: TTIHZ_totalIssueContributions_Field
   totalPullRequestContributions: GNBHJ_totalPullRequestContributions_Field
   totalPullRequestReviewContributions: int
   totalRepositoriesWithContributedCommits: int
   totalRepositoriesWithContributedIssues: UALFL_totalRepositoriesWithContributedIssues_Field
   totalRepositoriesWithContributedPullRequestReviews: int
   totalRepositoriesWithContributedPullRequests: RMZIL_totalRepositoriesWithContributedPullRequests_Field
   totalRepositoryContributions: TOYEM_totalRepositoryContributions_Field
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

class CFOZE_UserContentEditConnection_Field(UserContentEditConnection):
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
   userContentEdits: CFOZE_UserContentEditConnection_Field
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
   text: KTKXF_text_Field

class GistEdge(GQLObject):
   cursor: str
   node: NewType('Gist', GQLObject) ## Circular Reference for Gist

class list_GistEdge(list, GistEdge): pass

class GistConnection(GQLObject):
   edges: list_GistEdge[GistEdge]
   nodes: list_GQLObject[GQLObject] ## Circular Reference for Gist
   pageInfo: PageInfo
   totalCount: int

class ZPCSC_GistCommentConnection_Field(GistCommentConnection):
   class GistCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: GistCommentConnectionArgs



class BWWTR_GistFile_Field(GistFile):
   class GistFileArgs(GQLArgsSet, GQLObject):
      limit: int
      oid: GitObjectID

   _args: GistFileArgs



class list_GistFile(list, GistFile): pass

class UQRVZ_GistConnection_Field(GistConnection):
   class GistConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: GistOrder

   _args: GistConnectionArgs



class RIOEL_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class Gist(GQLObject):
   comments: ZPCSC_GistCommentConnection_Field
   createdAt: DateTime
   description: str
   files: BWWTR_GistFile_Field
   forks: UQRVZ_GistConnection_Field
   id: ID
   isFork: bool
   isPublic: bool
   name: str
   owner: RepositoryOwner
   pushedAt: DateTime
   resourcePath: URI
   stargazerCount: int
   stargazers: RIOEL_StargazerConnection_Field
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

class NYJDR_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class ProfileItemShowcase(GQLObject):
   hasPinnedItems: bool
   items: NYJDR_PinnableItemConnection_Field

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

class NNBYT_SponsorsListingFeaturedItem_Field(SponsorsListingFeaturedItem):
   class SponsorsListingFeaturedItemArgs(GQLArgsSet, GQLObject):
      featureableTypes: list[NonNull_SponsorsListingFeaturedItemFeatureableType]

   _args: SponsorsListingFeaturedItemArgs



class BBVCL_SponsorsTierConnection_Field(SponsorsTierConnection):
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
   featuredItems: NNBYT_SponsorsListingFeaturedItem_Field
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
   tiers: BBVCL_SponsorsTierConnection_Field
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

class QFNUI_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class WBAFS_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class NonNull_SponsorsActivityAction(GQLObject): pass

class LQHJH_SponsorsActivityConnection_Field(Generic[SponsorsActivityConnection]):
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



class NQLGS_Sponsorship_Field(Generic[Sponsorship]):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class PWNEQ_Sponsorship_Field(Generic[Sponsorship]):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class ZKHOG_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class HIBUL_SponsorshipConnection_Field(Generic[SponsorshipConnection]):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class JPIBT_SponsorshipConnection_Field(Generic[SponsorshipConnection]):
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
   isSponsoredBy: KXELZ_isSponsoredBy_Field
   isSponsoringViewer: bool
   monthlyEstimatedSponsorsIncomeInCents: int
   sponsoring: QFNUI_SponsorConnection_Field
   sponsors: WBAFS_SponsorConnection_Field
   sponsorsActivities: LQHJH_SponsorsActivityConnection_Field ## Circular Reference for SponsorsActivityConnection
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: NQLGS_Sponsorship_Field ## Circular Reference for Sponsorship
   sponsorshipForViewerAsSponsorable: PWNEQ_Sponsorship_Field ## Circular Reference for Sponsorship
   sponsorshipNewsletters: ZKHOG_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: HIBUL_SponsorshipConnection_Field ## Circular Reference for SponsorshipConnection
   sponsorshipsAsSponsor: JPIBT_SponsorshipConnection_Field ## Circular Reference for SponsorshipConnection
   totalSponsorshipAmountAsSponsorInCents: TKSSF_totalSponsorshipAmountAsSponsorInCents_Field
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

class FHMWM_SponsorshipConnection_Field(SponsorshipConnection):
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
   sponsorships: FHMWM_SponsorshipConnection_Field

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

class CYYMB_CommitCommentConnection_Field(CommitCommentConnection):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class EQUKB_ContributionsCollection_Field(ContributionsCollection):
   class ContributionsCollectionArgs(GQLArgsSet, GQLObject):
      organizationID: ID
      from_: DateTime
      to: DateTime

   _args: ContributionsCollectionArgs



class PJQKP_FollowerConnection_Field(FollowerConnection):
   class FollowerConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: FollowerConnectionArgs



class PLRJH_FollowingConnection_Field(FollowingConnection):
   class FollowingConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: FollowingConnectionArgs



class ADGZY_Gist_Field(Gist):
   class GistArgs(GQLArgsSet, GQLObject):
      name: NonNull_str

   _args: GistArgs



class VVIMW_GistCommentConnection_Field(GistCommentConnection):
   class GistCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: GistCommentConnectionArgs



class OQBBT_GistConnection_Field(GistConnection):
   class GistConnectionArgs(GQLArgsSet, GQLObject):
      privacy: GistPrivacy
      orderBy: GistOrder
      after: str
      before: str
      first: int
      last: int

   _args: GistConnectionArgs



class NHDNX_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject):
      primarySubjectId: ID

   _args: HovercardArgs



class TECFA_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class MFFZH_IssueConnection_Field(IssueConnection):
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



class MWWEN_Organization_Field(Generic[Organization]):
   class OrganizationArgs(GQLArgsSet, GQLObject):
      login: NonNull_str

   _args: OrganizationArgs



class YPDCP_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: OrganizationOrder
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class NJWWL_PackageConnection_Field(PackageConnection):
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

class GFHRN_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class OAOYC_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class QVGQV_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class WCPWR_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class QUAPZ_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: ProjectOrder
      search: str
      states: list[NonNull_ProjectState]
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class PSUFM_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class EFBWB_PublicKeyConnection_Field(PublicKeyConnection):
   class PublicKeyConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: PublicKeyConnectionArgs



class VLMSM_PullRequestConnection_Field(PullRequestConnection):
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



class VINKK_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class GNBAY_RepositoryConnection_Field(RepositoryConnection):
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



class CHYRV_RepositoryConnection_Field(RepositoryConnection):
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



class FRSJU_Repository_Field(Repository):
   class RepositoryArgs(GQLArgsSet, GQLObject):
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs



class WWUKF_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class TBPWK_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionOrder
      repositoryId: ID
      answered: bool

   _args: DiscussionConnectionArgs



class WRDED_SavedReplyConnection_Field(SavedReplyConnection):
   class SavedReplyConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SavedReplyOrder

   _args: SavedReplyConnectionArgs



class UMCQW_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class WHDTA_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class YFQKK_SponsorsActivityConnection_Field(SponsorsActivityConnection):
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



class MSWVA_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class IUPNO_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class MZXRN_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class GGXKZ_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class UWEXP_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipOrder
      maintainerLogins: list[NonNull_str]
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class DPEUJ_StarredRepositoryConnection_Field(StarredRepositoryConnection):
   class StarredRepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      ownedByViewer: bool
      orderBy: StarOrder

   _args: StarredRepositoryConnectionArgs



class NonNull_RepositoryOrder(RepositoryOrder): pass

class BLEJV_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: NonNull_RepositoryOrder
      since: DateTime

   _args: RepositoryConnectionArgs



class XNGMU_RepositoryConnection_Field(RepositoryConnection):
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
   anyPinnableItems: OZZSE_anyPinnableItems_Field
   avatarUrl: MLBIQ_URI_Field
   bio: str
   bioHTML: HTML
   canReceiveOrganizationEmailsWhenNotificationsRestricted: GROVZ_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field
   commitComments: CYYMB_CommitCommentConnection_Field
   company: str
   companyHTML: HTML
   contributionsCollection: EQUKB_ContributionsCollection_Field
   createdAt: DateTime
   databaseId: int
   email: str
   estimatedNextSponsorsPayoutInCents: int
   followers: PJQKP_FollowerConnection_Field
   following: PLRJH_FollowingConnection_Field
   gist: ADGZY_Gist_Field
   gistComments: VVIMW_GistCommentConnection_Field
   gists: OQBBT_GistConnection_Field
   hasSponsorsListing: bool
   hovercard: NHDNX_Hovercard_Field
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
   isSponsoredBy: VFQRL_isSponsoredBy_Field
   isSponsoringViewer: bool
   isViewer: bool
   issueComments: TECFA_IssueCommentConnection_Field
   issues: MFFZH_IssueConnection_Field
   itemShowcase: ProfileItemShowcase
   location: str
   login: str
   monthlyEstimatedSponsorsIncomeInCents: int
   name: str
   organization: MWWEN_Organization_Field ## Circular Reference for Organization
   organizationVerifiedDomainEmails: AGOCV_organizationVerifiedDomainEmails_Field
   organizations: YPDCP_OrganizationConnection_Field
   packages: NJWWL_PackageConnection_Field
   pinnableItems: GFHRN_PinnableItemConnection_Field
   pinnedItems: OAOYC_PinnableItemConnection_Field
   pinnedItemsRemaining: int
   project: QVGQV_Project_Field
   projectV2: WCPWR_ProjectV2_Field
   projects: QUAPZ_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   projectsV2: PSUFM_ProjectV2Connection_Field
   publicKeys: EFBWB_PublicKeyConnection_Field
   pullRequests: VLMSM_PullRequestConnection_Field
   recentProjects: VINKK_ProjectV2Connection_Field
   repositories: GNBAY_RepositoryConnection_Field
   repositoriesContributedTo: CHYRV_RepositoryConnection_Field
   repository: FRSJU_Repository_Field
   repositoryDiscussionComments: WWUKF_DiscussionCommentConnection_Field
   repositoryDiscussions: TBPWK_DiscussionConnection_Field
   resourcePath: URI
   savedReplies: WRDED_SavedReplyConnection_Field
   sponsoring: UMCQW_SponsorConnection_Field
   sponsors: WHDTA_SponsorConnection_Field
   sponsorsActivities: YFQKK_SponsorsActivityConnection_Field
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: MSWVA_Sponsorship_Field
   sponsorshipForViewerAsSponsorable: IUPNO_Sponsorship_Field
   sponsorshipNewsletters: MZXRN_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: GGXKZ_SponsorshipConnection_Field
   sponsorshipsAsSponsor: UWEXP_SponsorshipConnection_Field
   starredRepositories: DPEUJ_StarredRepositoryConnection_Field
   status: UserStatus
   topRepositories: BLEJV_RepositoryConnection_Field
   totalSponsorshipAmountAsSponsorInCents: VQVKQ_totalSponsorshipAmountAsSponsorInCents_Field
   twitterUsername: str
   updatedAt: DateTime
   url: URI
   viewerCanChangePinnedItems: bool
   viewerCanCreateProjects: bool
   viewerCanFollow: bool
   viewerCanSponsor: bool
   viewerIsFollowing: bool
   viewerIsSponsoring: bool
   watching: XNGMU_RepositoryConnection_Field
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

class OQVXJ_ExternalIdentityConnection_Field(ExternalIdentityConnection):
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
   externalIdentities: OQVXJ_ExternalIdentityConnection_Field
   id: ID
   idpCertificate: X509Certificate
   issuer: str
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   signatureMethod: URI
   ssoUrl: URI

class AIQZP_OrganizationAuditEntryConnection_Field(OrganizationAuditEntryConnection):
   class OrganizationAuditEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: AuditLogOrder

   _args: OrganizationAuditEntryConnectionArgs



class AFDKQ_VerifiableDomainConnection_Field(VerifiableDomainConnection):
   class VerifiableDomainConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      isVerified: bool
      isApproved: bool
      orderBy: VerifiableDomainOrder

   _args: VerifiableDomainConnectionArgs



class EDBAM_OrganizationEnterpriseOwnerConnection_Field(OrganizationEnterpriseOwnerConnection):
   class OrganizationEnterpriseOwnerConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      organizationRole: RoleInOrganization
      orderBy: OrgEnterpriseOwnerOrder
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationEnterpriseOwnerConnectionArgs



class AEBND_IpAllowListEntryConnection_Field(Generic[IpAllowListEntryConnection]):
   class IpAllowListEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: IpAllowListEntryConnectionArgs



class RDJEI_MannequinConnection_Field(MannequinConnection):
   class MannequinConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: MannequinOrder

   _args: MannequinConnectionArgs



class AUBRS_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class CHBEX_OrganizationMemberConnection_Field(OrganizationMemberConnection):
   class OrganizationMemberConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationMemberConnectionArgs



class NYDPE_PackageConnection_Field(PackageConnection):
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



class XXCOZ_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class JYCNF_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class THMUJ_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class NKJBZ_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectArgs



class WUVOP_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject):
      number: NonNull_int

   _args: ProjectV2Args



class AUUFE_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: ProjectOrder
      search: str
      states: list[NonNull_ProjectState]
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class JXHUF_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class ZLUGU_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class NBJNJ_RepositoryConnection_Field(RepositoryConnection):
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



class GYFCG_Repository_Field(Repository):
   class RepositoryArgs(GQLArgsSet, GQLObject):
      name: NonNull_str
      followRenames: bool

   _args: RepositoryArgs



class RULLK_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class RRKLB_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionOrder
      repositoryId: ID
      answered: bool

   _args: DiscussionConnectionArgs



class IEWAF_RepositoryMigrationConnection_Field(RepositoryMigrationConnection):
   class RepositoryMigrationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      state: MigrationState
      repositoryName: str
      orderBy: RepositoryMigrationOrder

   _args: RepositoryMigrationConnectionArgs



class KWULK_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class NOPVL_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class WNGBY_SponsorsActivityConnection_Field(SponsorsActivityConnection):
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



class VYADG_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class XFXNT_Sponsorship_Field(Sponsorship):
   class SponsorshipArgs(GQLArgsSet, GQLObject):
      activeOnly: bool

   _args: SponsorshipArgs



class WLKIP_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class VXGDY_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class GXYCU_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipOrder
      maintainerLogins: list[NonNull_str]
      activeOnly: bool

   _args: SponsorshipConnectionArgs



class YBBUQ_Team_Field(Team):
   class TeamArgs(GQLArgsSet, GQLObject):
      slug: NonNull_str

   _args: TeamArgs



class KWJKA_TeamConnection_Field(TeamConnection):
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
   anyPinnableItems: LQXXH_anyPinnableItems_Field
   auditLog: AIQZP_OrganizationAuditEntryConnection_Field
   avatarUrl: CTCAJ_URI_Field
   createdAt: DateTime
   databaseId: int
   description: str
   descriptionHTML: str
   domains: AFDKQ_VerifiableDomainConnection_Field
   email: str
   enterpriseOwners: EDBAM_OrganizationEnterpriseOwnerConnection_Field
   estimatedNextSponsorsPayoutInCents: int
   hasSponsorsListing: bool
   id: ID
   interactionAbility: RepositoryInteractionAbility
   ipAllowListEnabledSetting: IpAllowListEnabledSettingValue
   ipAllowListEntries: AEBND_IpAllowListEntryConnection_Field ## Circular Reference for IpAllowListEntryConnection
   ipAllowListForInstalledAppsEnabledSetting: IpAllowListForInstalledAppsEnabledSettingValue
   isSponsoredBy: DVNDG_isSponsoredBy_Field
   isSponsoringViewer: bool
   isVerified: bool
   itemShowcase: ProfileItemShowcase
   location: str
   login: str
   mannequins: RDJEI_MannequinConnection_Field
   memberStatuses: AUBRS_UserStatusConnection_Field
   membersCanForkPrivateRepositories: bool
   membersWithRole: CHBEX_OrganizationMemberConnection_Field
   monthlyEstimatedSponsorsIncomeInCents: int
   name: str
   newTeamResourcePath: URI
   newTeamUrl: URI
   notificationDeliveryRestrictionEnabledSetting: NotificationRestrictionSettingValue
   organizationBillingEmail: str
   packages: NYDPE_PackageConnection_Field
   pendingMembers: XXCOZ_UserConnection_Field
   pinnableItems: JYCNF_PinnableItemConnection_Field
   pinnedItems: THMUJ_PinnableItemConnection_Field
   pinnedItemsRemaining: int
   project: NKJBZ_Project_Field
   projectV2: WUVOP_ProjectV2_Field
   projects: AUUFE_ProjectConnection_Field
   projectsResourcePath: URI
   projectsUrl: URI
   projectsV2: JXHUF_ProjectV2Connection_Field
   recentProjects: ZLUGU_ProjectV2Connection_Field
   repositories: NBJNJ_RepositoryConnection_Field
   repository: GYFCG_Repository_Field
   repositoryDiscussionComments: RULLK_DiscussionCommentConnection_Field
   repositoryDiscussions: RRKLB_DiscussionConnection_Field
   repositoryMigrations: IEWAF_RepositoryMigrationConnection_Field
   requiresTwoFactorAuthentication: bool
   resourcePath: URI
   samlIdentityProvider: OrganizationIdentityProvider
   sponsoring: KWULK_SponsorConnection_Field
   sponsors: NOPVL_SponsorConnection_Field
   sponsorsActivities: WNGBY_SponsorsActivityConnection_Field
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: VYADG_Sponsorship_Field
   sponsorshipForViewerAsSponsorable: XFXNT_Sponsorship_Field
   sponsorshipNewsletters: WLKIP_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: VXGDY_SponsorshipConnection_Field
   sponsorshipsAsSponsor: GXYCU_SponsorshipConnection_Field
   team: YBBUQ_Team_Field
   teams: KWJKA_TeamConnection_Field
   teamsResourcePath: URI
   teamsUrl: URI
   totalSponsorshipAmountAsSponsorInCents: CTFUG_totalSponsorshipAmountAsSponsorInCents_Field
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

class SBBGV_EnterpriseOrganizationMembershipConnection_Field(EnterpriseOrganizationMembershipConnection):
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
   avatarUrl: ARSHS_URI_Field
   createdAt: DateTime
   enterprise: NewType('Enterprise', GQLObject) ## Circular Reference for Enterprise
   id: ID
   login: str
   name: str
   organizations: SBBGV_EnterpriseOrganizationMembershipConnection_Field
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

class LJPEB_EnterpriseServerUserAccountEmailConnection_Field(EnterpriseServerUserAccountEmailConnection):
   class EnterpriseServerUserAccountEmailConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: EnterpriseServerUserAccountEmailOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerUserAccountEmailConnectionArgs



class EnterpriseServerUserAccount(GQLObject):
   createdAt: DateTime
   emails: LJPEB_EnterpriseServerUserAccountEmailConnection_Field
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

class QXMMA_EnterpriseServerUserAccountConnection_Field(EnterpriseServerUserAccountConnection):
   class EnterpriseServerUserAccountConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: EnterpriseServerUserAccountOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerUserAccountConnectionArgs



class QHFTJ_EnterpriseServerUserAccountsUploadConnection_Field(EnterpriseServerUserAccountsUploadConnection):
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
   userAccounts: QXMMA_EnterpriseServerUserAccountConnection_Field
   userAccountsUploads: QHFTJ_EnterpriseServerUserAccountsUploadConnection_Field

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

class KDEFW_ExternalIdentityConnection_Field(ExternalIdentityConnection):
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
   externalIdentities: KDEFW_ExternalIdentityConnection_Field
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

class JQRKS_EnterpriseRepositoryInfoConnection_Field(EnterpriseRepositoryInfoConnection):
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
   repositories: JQRKS_EnterpriseRepositoryInfoConnection_Field

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
   shortDescriptionHTML: BHHDH_HTML_Field
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

class MOVNU_ExternalIdentityConnection_Field(ExternalIdentityConnection):
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
   externalIdentities: MOVNU_ExternalIdentityConnection_Field
   id: ID
   idpCertificate: X509Certificate
   issuer: str
   recoveryCodes: list[str]
   signatureMethod: SamlSignatureAlgorithm
   ssoUrl: URI

class OMMNB_EnterpriseAdministratorConnection_Field(EnterpriseAdministratorConnection):
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



class HUHKI_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class SGMLG_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class NonNull_DefaultRepositoryPermissionField(GQLObject): pass

class DLXIM_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_DefaultRepositoryPermissionField
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class ESXUM_VerifiableDomainConnection_Field(VerifiableDomainConnection):
   class VerifiableDomainConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      isVerified: bool
      isApproved: bool
      orderBy: VerifiableDomainOrder

   _args: VerifiableDomainConnectionArgs



class BBNOZ_EnterpriseServerInstallationConnection_Field(EnterpriseServerInstallationConnection):
   class EnterpriseServerInstallationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      connectedOnly: bool
      orderBy: EnterpriseServerInstallationOrder

   _args: EnterpriseServerInstallationConnectionArgs



class FWNTF_IpAllowListEntryConnection_Field(Generic[IpAllowListEntryConnection]):
   class IpAllowListEntryConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: IpAllowListEntryConnectionArgs



class PZLGA_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class NonNull_OrganizationMembersCanCreateRepositoriesSettingValue(GQLObject): pass

class HKMYN_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_OrganizationMembersCanCreateRepositoriesSettingValue
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class JRBJT_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class IHLVK_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class KRTWZ_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class YDKMZ_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class OJPWN_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class PHAZP_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class LVOND_EnterpriseOutsideCollaboratorConnection_Field(EnterpriseOutsideCollaboratorConnection):
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



class AOCRJ_EnterpriseAdministratorInvitationConnection_Field(EnterpriseAdministratorInvitationConnection):
   class EnterpriseAdministratorInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: EnterpriseAdministratorInvitationOrder
      role: EnterpriseAdministratorRole
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseAdministratorInvitationConnectionArgs



class HSSOL_RepositoryInvitationConnection_Field(RepositoryInvitationConnection):
   class RepositoryInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      orderBy: RepositoryInvitationOrder
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryInvitationConnectionArgs



class LDLPG_EnterprisePendingMemberInvitationConnection_Field(EnterprisePendingMemberInvitationConnection):
   class EnterprisePendingMemberInvitationConnectionArgs(GQLArgsSet, GQLObject):
      query: str
      organizationLogins: list[NonNull_str]
      after: str
      before: str
      first: int
      last: int

   _args: EnterprisePendingMemberInvitationConnectionArgs



class QKQYD_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class NonNull_IdentityProviderConfigurationState(GQLObject): pass

class ARVAH_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_IdentityProviderConfigurationState
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class INNEP_EnterpriseMemberConnection_Field(EnterpriseMemberConnection):
   class EnterpriseMemberConnectionArgs(GQLArgsSet, GQLObject):
      orderBy: EnterpriseMemberOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseMemberConnectionArgs



class WKDGW_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class ZBGDK_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      value: NonNull_bool
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class EnterpriseOwnerInfo(GQLObject):
   admins: OMMNB_EnterpriseAdministratorConnection_Field
   affiliatedUsersWithTwoFactorDisabled: HUHKI_UserConnection_Field
   affiliatedUsersWithTwoFactorDisabledExist: bool
   allowPrivateRepositoryForkingSetting: EnterpriseEnabledDisabledSettingValue
   allowPrivateRepositoryForkingSettingOrganizations: SGMLG_OrganizationConnection_Field
   allowPrivateRepositoryForkingSettingPolicyValue: EnterpriseAllowPrivateRepositoryForkingPolicyValue
   defaultRepositoryPermissionSetting: EnterpriseDefaultRepositoryPermissionSettingValue
   defaultRepositoryPermissionSettingOrganizations: DLXIM_OrganizationConnection_Field
   domains: ESXUM_VerifiableDomainConnection_Field
   enterpriseServerInstallations: BBNOZ_EnterpriseServerInstallationConnection_Field
   ipAllowListEnabledSetting: IpAllowListEnabledSettingValue
   ipAllowListEntries: FWNTF_IpAllowListEntryConnection_Field ## Circular Reference for IpAllowListEntryConnection
   ipAllowListForInstalledAppsEnabledSetting: IpAllowListForInstalledAppsEnabledSettingValue
   isUpdatingDefaultRepositoryPermission: bool
   isUpdatingTwoFactorRequirement: bool
   membersCanChangeRepositoryVisibilitySetting: EnterpriseEnabledDisabledSettingValue
   membersCanChangeRepositoryVisibilitySettingOrganizations: PZLGA_OrganizationConnection_Field
   membersCanCreateInternalRepositoriesSetting: bool
   membersCanCreatePrivateRepositoriesSetting: bool
   membersCanCreatePublicRepositoriesSetting: bool
   membersCanCreateRepositoriesSetting: EnterpriseMembersCanCreateRepositoriesSettingValue
   membersCanCreateRepositoriesSettingOrganizations: HKMYN_OrganizationConnection_Field
   membersCanDeleteIssuesSetting: EnterpriseEnabledDisabledSettingValue
   membersCanDeleteIssuesSettingOrganizations: JRBJT_OrganizationConnection_Field
   membersCanDeleteRepositoriesSetting: EnterpriseEnabledDisabledSettingValue
   membersCanDeleteRepositoriesSettingOrganizations: IHLVK_OrganizationConnection_Field
   membersCanInviteCollaboratorsSetting: EnterpriseEnabledDisabledSettingValue
   membersCanInviteCollaboratorsSettingOrganizations: KRTWZ_OrganizationConnection_Field
   membersCanMakePurchasesSetting: EnterpriseMembersCanMakePurchasesSettingValue
   membersCanUpdateProtectedBranchesSetting: EnterpriseEnabledDisabledSettingValue
   membersCanUpdateProtectedBranchesSettingOrganizations: YDKMZ_OrganizationConnection_Field
   membersCanViewDependencyInsightsSetting: EnterpriseEnabledDisabledSettingValue
   membersCanViewDependencyInsightsSettingOrganizations: OJPWN_OrganizationConnection_Field
   notificationDeliveryRestrictionEnabledSetting: NotificationRestrictionSettingValue
   oidcProvider: OIDCProvider
   organizationProjectsSetting: EnterpriseEnabledDisabledSettingValue
   organizationProjectsSettingOrganizations: PHAZP_OrganizationConnection_Field
   outsideCollaborators: LVOND_EnterpriseOutsideCollaboratorConnection_Field
   pendingAdminInvitations: AOCRJ_EnterpriseAdministratorInvitationConnection_Field
   pendingCollaboratorInvitations: HSSOL_RepositoryInvitationConnection_Field
   pendingMemberInvitations: LDLPG_EnterprisePendingMemberInvitationConnection_Field
   repositoryProjectsSetting: EnterpriseEnabledDisabledSettingValue
   repositoryProjectsSettingOrganizations: QKQYD_OrganizationConnection_Field
   samlIdentityProvider: EnterpriseIdentityProvider
   samlIdentityProviderSettingOrganizations: ARVAH_OrganizationConnection_Field
   supportEntitlements: INNEP_EnterpriseMemberConnection_Field
   teamDiscussionsSetting: EnterpriseEnabledDisabledSettingValue
   teamDiscussionsSettingOrganizations: WKDGW_OrganizationConnection_Field
   twoFactorRequiredSetting: EnterpriseEnabledSettingValue
   twoFactorRequiredSettingOrganizations: ZBGDK_OrganizationConnection_Field

class NKXGF_EnterpriseMemberConnection_Field(EnterpriseMemberConnection):
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



class KYEAH_OrganizationConnection_Field(OrganizationConnection):
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
   avatarUrl: SILSD_URI_Field
   billingInfo: EnterpriseBillingInfo
   createdAt: DateTime
   databaseId: int
   description: str
   descriptionHTML: HTML
   id: ID
   location: str
   members: NKXGF_EnterpriseMemberConnection_Field
   name: str
   organizations: KYEAH_OrganizationConnection_Field
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

class FAXGI_IpAllowListEntryConnection_Field(IpAllowListEntryConnection):
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
   ipAllowListEntries: FAXGI_IpAllowListEntryConnection_Field
   logoBackgroundColor: str
   logoUrl: OCZPK_URI_Field
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

class AQRPU_CheckRunConnection_Field(CheckRunConnection):
   class CheckRunConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      filterBy: CheckRunFilter

   _args: CheckRunConnectionArgs



class UPQAJ_PullRequestConnection_Field(PullRequestConnection):
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
   checkRuns: AQRPU_CheckRunConnection_Field
   commit: Commit
   conclusion: CheckConclusionState
   createdAt: DateTime
   creator: User
   databaseId: int
   id: ID
   matchingPullRequests: UPQAJ_PullRequestConnection_Field
   push: Push
   repository: Repository
   resourcePath: URI
   status: CheckStatusState
   updatedAt: DateTime
   url: URI
   workflowRun: NewType('WorkflowRun', GQLObject) ## Circular Reference for WorkflowRun

class WSESE_EnvironmentConnection_Field(EnvironmentConnection):
   class EnvironmentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: EnvironmentConnectionArgs



class DeploymentReview(GQLObject):
   comment: str
   databaseId: int
   environments: WSESE_EnvironmentConnection_Field
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

class XQDSL_WorkflowRunConnection_Field(Generic[WorkflowRunConnection]):
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
   runs: XQDSL_WorkflowRunConnection_Field ## Circular Reference for WorkflowRunConnection
   updatedAt: DateTime

class EPPOD_DeploymentReviewConnection_Field(DeploymentReviewConnection):
   class DeploymentReviewConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewConnectionArgs



class SDRSS_DeploymentRequestConnection_Field(DeploymentRequestConnection):
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
   deploymentReviews: EPPOD_DeploymentReviewConnection_Field
   id: ID
   pendingDeploymentRequests: SDRSS_DeploymentRequestConnection_Field
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
   logoUrl: KKNZP_URI_Field
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

class GDHIB_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      skip: int

   _args: PullRequestReviewCommentConnectionArgs



class PullRequestThread(GQLObject):
   comments: GDHIB_PullRequestReviewCommentConnection_Field
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

class GXUAL_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class TYVZY_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject):
      types: list[NonNull_PinnableItemType]
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class ProfileOwner(GQLObject):
   anyPinnableItems: OXMQI_anyPinnableItems_Field
   email: str
   id: ID
   itemShowcase: ProfileItemShowcase
   location: str
   login: str
   name: str
   pinnableItems: GXUAL_PinnableItemConnection_Field
   pinnedItems: TYVZY_PinnableItemConnection_Field
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

class ZYZAQ_UserContentEditConnection_Field(UserContentEditConnection):
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
   userContentEdits: ZYZAQ_UserContentEditConnection_Field
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

class CZQRO_StargazerConnection_Field(StargazerConnection):
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
   stargazers: CZQRO_StargazerConnection_Field
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

class YAUXV_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class GrantEnterpriseOrganizationsMigratorRolePayload(GQLObject):
   clientMutationId: str
   organizations: YAUXV_OrganizationConnection_Field

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

class LQVBP_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class MemberStatusable(GQLObject):
   memberStatuses: LQVBP_UserStatusConnection_Field

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

class BJYAY_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class OrganizationTeamsHovercardContext(GQLObject):
   message: str
   octicon: str
   relevantTeams: BJYAY_TeamConnection_Field
   teamsResourcePath: URI
   teamsUrl: URI
   totalTeamCount: int

class TBICW_OrganizationConnection_Field(OrganizationConnection):
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
   relevantOrganizations: TBICW_OrganizationConnection_Field
   totalOrganizationCount: int

class YIRIR_PackageConnection_Field(PackageConnection):
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
   packages: YIRIR_PackageConnection_Field

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

class XCIUJ_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class ProjectV2Recent(GQLObject):
   recentProjects: XCIUJ_ProjectV2Connection_Field

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

class SUTVN_DiscussionConnection_Field(DiscussionConnection):
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
   repositoryDiscussions: SUTVN_DiscussionConnection_Field

class OKHXT_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class RepositoryDiscussionCommentAuthor(GQLObject):
   repositoryDiscussionComments: OKHXT_DiscussionCommentConnection_Field

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

class SEWTU_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class RevokeEnterpriseOrganizationsMigratorRolePayload(GQLObject):
   clientMutationId: str
   organizations: SEWTU_OrganizationConnection_Field

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

class EZTHQ_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject):
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class UpdateProjectV2ItemPositionPayload(GQLObject):
   clientMutationId: str
   items: EZTHQ_ProjectV2ItemConnection_Field

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
