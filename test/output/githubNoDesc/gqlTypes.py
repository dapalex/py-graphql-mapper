from typing import Generic, Union
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gqlTypes import ID
from pygqlmap.src.gqlArguedPrimitives import *
from typing import NewType
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *
from .circularRefs import *

class Votable(GQLObject):
   upvoteCount: int ##NON NULL
   viewerCanUpvote: bool ##NON NULL
   viewerHasUpvoted: bool ##NON NULL

class VerifiableDomainOrder(GQLObject):
   field: VerifiableDomainOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class UserEmailMetadata(GQLObject):
   primary: bool
   type: str
   value: str ##NON NULL

class UpdateTeamsRepositoryInput(GQLObject):
   repositoryId: ID ##NON NULL
   teamIds: list[ID] ##NON NULL
   permission: RepositoryPermission ##NON NULL
   clientMutationId: str

class UpdateTeamDiscussionCommentInput(GQLObject):
   id: ID ##NON NULL
   body: str ##NON NULL
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
   repositoryId: ID ##NON NULL
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
   pullRequestReviewId: ID ##NON NULL
   body: str ##NON NULL
   clientMutationId: str

class UpdatePullRequestInput(GQLObject):
   pullRequestId: ID ##NON NULL
   baseRefName: str
   title: str
   body: str
   state: PullRequestUpdateState
   maintainerCanModify: bool
   assigneeIds: list[ID] ##NON NULL
   milestoneId: ID
   labelIds: list[ID] ##NON NULL
   projectIds: list[ID] ##NON NULL
   clientMutationId: str

class UpdateProjectV2ItemPositionInput(GQLObject):
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   afterId: ID
   clientMutationId: str

class UpdateProjectV2DraftIssueInput(GQLObject):
   draftIssueId: ID ##NON NULL
   title: str
   body: str
   assigneeIds: list[ID] ##NON NULL
   clientMutationId: str

class UpdateProjectNextInput(GQLObject):
   projectId: ID
   title: str
   description: str
   shortDescription: str
   closed: bool
   public: bool
   clientMutationId: str

class UpdateProjectDraftIssueInput(GQLObject):
   draftIssueId: ID ##NON NULL
   title: str
   body: str
   assigneeIds: list[ID] ##NON NULL
   clientMutationId: str

class UpdateProjectCardInput(GQLObject):
   projectCardId: ID ##NON NULL
   isArchived: bool
   note: str
   clientMutationId: str

class UpdateOrganizationAllowPrivateRepositoryForkingSettingInput(GQLObject):
   organizationId: ID ##NON NULL
   forkingEnabled: bool ##NON NULL
   clientMutationId: str

class UpdateIssueInput(GQLObject):
   id: ID ##NON NULL
   title: str
   body: str
   assigneeIds: list[ID] ##NON NULL
   milestoneId: ID
   labelIds: list[ID] ##NON NULL
   state: IssueState
   projectIds: list[ID] ##NON NULL
   clientMutationId: str

class UpdateIpAllowListForInstalledAppsEnabledSettingInput(GQLObject):
   ownerId: ID ##NON NULL
   settingValue: IpAllowListForInstalledAppsEnabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateIpAllowListEnabledSettingInput(GQLObject):
   ownerId: ID ##NON NULL
   settingValue: IpAllowListEnabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseRepositoryProjectsSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseOwnerOrganizationRolePayload(GQLObject):
   clientMutationId: str
   message: str

class UpdateEnterpriseOrganizationProjectsSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanDeleteIssuesSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   policyValue: EnterpriseAllowPrivateRepositoryForkingPolicyValue
   clientMutationId: str

class UpdateEnterpriseAdministratorRoleInput(GQLObject):
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   role: EnterpriseAdministratorRole ##NON NULL
   clientMutationId: str

class UpdateDiscussionCommentInput(GQLObject):
   commentId: ID ##NON NULL
   body: str ##NON NULL
   clientMutationId: str

class Updatable(GQLObject):
   viewerCanUpdate: bool ##NON NULL

class UnpinIssueInput(GQLObject):
   issueId: ID ##NON NULL
   clientMutationId: str

class UnmarkIssueAsDuplicateInput(GQLObject):
   duplicateId: ID ##NON NULL
   canonicalId: ID ##NON NULL
   clientMutationId: str

class UnmarkDiscussionCommentAsAnswerInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class UnlinkRepositoryFromProjectInput(GQLObject):
   projectId: ID ##NON NULL
   repositoryId: ID ##NON NULL
   clientMutationId: str

class UnlinkProjectV2FromRepositoryInput(GQLObject):
   projectId: ID ##NON NULL
   repositoryId: ID ##NON NULL
   clientMutationId: str

class UnfollowUserInput(GQLObject):
   userId: ID ##NON NULL
   clientMutationId: str

class UnarchiveRepositoryInput(GQLObject):
   repositoryId: ID ##NON NULL
   clientMutationId: str

class TransferIssueInput(GQLObject):
   issueId: ID ##NON NULL
   repositoryId: ID ##NON NULL
   createLabelsIfMissing: bool
   clientMutationId: str

class TextMatchHighlight(GQLObject):
   beginIndice: int ##NON NULL
   endIndice: int ##NON NULL
   text: str ##NON NULL

class TeamOrder(GQLObject):
   field: TeamOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class TeamDiscussionOrder(GQLObject):
   field: TeamDiscussionOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class Subscribable(GQLObject):
   id: ID ##NON NULL
   viewerCanSubscribe: bool ##NON NULL
   viewerSubscription: SubscriptionState

class SubmitPullRequestReviewInput(GQLObject):
   pullRequestId: ID
   pullRequestReviewId: ID
   event: PullRequestReviewEvent ##NON NULL
   body: str
   clientMutationId: str

class StartRepositoryMigrationInput(GQLObject):
   sourceId: ID ##NON NULL
   ownerId: ID ##NON NULL
   sourceRepositoryUrl: URI ##NON NULL
   repositoryName: str ##NON NULL
   continueOnError: bool
   gitArchiveUrl: str
   metadataArchiveUrl: str
   accessToken: str ##NON NULL
   githubPat: str
   skipReleases: bool
   targetRepoVisibility: str
   lockSource: bool
   clientMutationId: str

class SponsorshipOrder(GQLObject):
   field: SponsorshipOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorsTierOrder(GQLObject):
   field: SponsorsTierOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorsActivityOrder(GQLObject):
   field: SponsorsActivityOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorOrder(GQLObject):
   field: SponsorOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SetUserInteractionLimitInput(GQLObject):
   userId: ID ##NON NULL
   limit: RepositoryInteractionLimit ##NON NULL
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SetOrganizationInteractionLimitInput(GQLObject):
   organizationId: ID ##NON NULL
   limit: RepositoryInteractionLimit ##NON NULL
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SecurityVulnerabilityOrder(GQLObject):
   field: SecurityVulnerabilityOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SecurityAdvisoryPackageVersion(GQLObject):
   identifier: str ##NON NULL

class SecurityAdvisoryOrder(GQLObject):
   field: SecurityAdvisoryOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SecurityAdvisoryIdentifier(GQLObject):
   type: str ##NON NULL
   value: str ##NON NULL

class RevokeMigratorRolePayload(GQLObject):
   clientMutationId: str
   success: bool

class RevokeEnterpriseOrganizationsMigratorRoleInput(GQLObject):
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class ResolveReviewThreadInput(GQLObject):
   threadId: ID ##NON NULL
   clientMutationId: str

class RequiredStatusCheckInput(GQLObject):
   context: str ##NON NULL
   appId: ID

class RequirableByPullRequest(GQLObject):
   isRequired: isRequiredField ##NON NULL

class RepositoryOrder(GQLObject):
   field: RepositoryOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class RepositoryInvitationOrder(GQLObject):
   field: RepositoryInvitationOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class RepositoryContactLink(GQLObject):
   about: str ##NON NULL
   name: str ##NON NULL
   url: URI ##NON NULL

class ReopenPullRequestInput(GQLObject):
   pullRequestId: ID ##NON NULL
   clientMutationId: str

class RemoveUpvoteInput(GQLObject):
   subjectId: ID ##NON NULL
   clientMutationId: str

class RemoveReactionInput(GQLObject):
   subjectId: ID ##NON NULL
   content: ReactionContent ##NON NULL
   clientMutationId: str

class RemoveLabelsFromLabelableInput(GQLObject):
   labelableId: ID ##NON NULL
   labelIds: list[ID] ##NON NULL
   clientMutationId: str

class RemoveEnterpriseSupportEntitlementInput(GQLObject):
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class RemoveEnterpriseIdentityProviderInput(GQLObject):
   enterpriseId: ID ##NON NULL
   clientMutationId: str

class RemoveAssigneesFromAssignableInput(GQLObject):
   assignableId: ID ##NON NULL
   assigneeIds: list[ID] ##NON NULL
   clientMutationId: str

class RejectDeploymentsInput(GQLObject):
   workflowRunId: ID ##NON NULL
   environmentIds: list[ID] ##NON NULL
   comment: str
   clientMutationId: str

class RegenerateVerifiableDomainTokenInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class RefUpdateRule(GQLObject):
   allowsDeletions: bool ##NON NULL
   allowsForcePushes: bool ##NON NULL
   blocksCreations: bool ##NON NULL
   pattern: str ##NON NULL
   requiredApprovingReviewCount: int
   requiredStatusCheckContexts: list[str]
   requiresCodeOwnerReviews: bool ##NON NULL
   requiresConversationResolution: bool ##NON NULL
   requiresLinearHistory: bool ##NON NULL
   requiresSignatures: bool ##NON NULL
   viewerAllowedToDismissReviews: bool ##NON NULL
   viewerCanPush: bool ##NON NULL

class ReactionOrder(GQLObject):
   field: ReactionOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class PullRequestOrder(GQLObject):
   field: PullRequestOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class PublishSponsorsTierInput(GQLObject):
   tierId: ID ##NON NULL
   clientMutationId: str

class ProjectV2ViewOrder(GQLObject):
   field: ProjectV2ViewOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class ProjectV2Order(GQLObject):
   field: ProjectV2OrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class ProjectV2ItemOrder(GQLObject):
   field: ProjectV2ItemOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class ProjectV2Filters(GQLObject):
   state: ProjectV2State

class ProjectV2FieldOrder(GQLObject):
   field: ProjectV2FieldOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class ProjectOrder(GQLObject):
   field: ProjectOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class PageInfo(GQLObject):
   endCursor: str
   hasNextPage: bool ##NON NULL
   hasPreviousPage: bool ##NON NULL
   startCursor: str

class PackageVersionOrder(GQLObject):
   field: PackageVersionOrderField
   direction: OrderDirection

class PackageOrder(GQLObject):
   field: PackageOrderField
   direction: OrderDirection

class OrganizationOrder(GQLObject):
   field: OrganizationOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class OauthApplicationAuditEntryData(GQLObject):
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI

class MoveProjectColumnInput(GQLObject):
   columnId: ID ##NON NULL
   afterColumnId: ID
   clientMutationId: str

class MinimizeCommentInput(GQLObject):
   subjectId: ID ##NON NULL
   classifier: ReportedContentClassifiers ##NON NULL
   clientMutationId: str

class MilestoneOrder(GQLObject):
   field: MilestoneOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class MergePullRequestInput(GQLObject):
   pullRequestId: ID ##NON NULL
   commitHeadline: str
   commitBody: str
   expectedHeadOid: GitObjectID
   mergeMethod: PullRequestMergeMethod
   authorEmail: str
   clientMutationId: str

class MarketplaceCategory(GQLObject):
   description: str
   howItWorks: str
   id: ID ##NON NULL
   name: str ##NON NULL
   primaryListingCount: int ##NON NULL
   resourcePath: URI ##NON NULL
   secondaryListingCount: int ##NON NULL
   slug: str ##NON NULL
   url: URI ##NON NULL

class MarkFileAsViewedInput(GQLObject):
   pullRequestId: ID ##NON NULL
   path: str ##NON NULL
   clientMutationId: str

class MannequinOrder(GQLObject):
   field: MannequinOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class LockLockableInput(GQLObject):
   lockableId: ID ##NON NULL
   lockReason: LockReason
   clientMutationId: str

class LinkProjectV2ToTeamInput(GQLObject):
   projectId: ID ##NON NULL
   teamId: ID ##NON NULL
   clientMutationId: str

class LicenseRule(GQLObject):
   description: str ##NON NULL
   key: str ##NON NULL
   label: str ##NON NULL

class Language(GQLObject):
   color: str
   id: ID ##NON NULL
   name: str ##NON NULL

class IssueTemplate(GQLObject):
   about: str
   body: str
   filename: str ##NON NULL
   name: str ##NON NULL
   title: str

class IssueFilters(GQLObject):
   assignee: str
   createdBy: str
   labels: list[str] ##NON NULL
   mentioned: str
   milestone: str
   milestoneNumber: str
   since: DateTime
   states: list[IssueState] ##NON NULL
   viewerSubscribed: bool

class IpAllowListEntryOrder(GQLObject):
   field: IpAllowListEntryOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class HovercardContext(GQLObject):
   message: str ##NON NULL
   octicon: str ##NON NULL

class GrantMigratorRoleInput(GQLObject):
   organizationId: ID ##NON NULL
   actor: str ##NON NULL
   actorType: ActorType ##NON NULL
   clientMutationId: str

class GitHubMetadata(GQLObject):
   gitHubServicesSha: GitObjectID ##NON NULL
   gitIpAddresses: list[str]
   hookIpAddresses: list[str]
   importerIpAddresses: list[str]
   isPasswordAuthenticationVerifiable: bool ##NON NULL
   pagesIpAddresses: list[str]

class GenericHovercardContext(GQLObject):
   message: str ##NON NULL
   octicon: str ##NON NULL

class FollowUserInput(GQLObject):
   userId: ID ##NON NULL
   clientMutationId: str

class FileDeletion(GQLObject):
   path: str ##NON NULL

class ExternalIdentityAttribute(GQLObject):
   metadata: str
   name: str ##NON NULL
   value: str ##NON NULL

class EnterpriseServerUserAccountOrder(GQLObject):
   field: EnterpriseServerUserAccountOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseServerInstallationOrder(GQLObject):
   field: EnterpriseServerInstallationOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseMemberOrder(GQLObject):
   field: EnterpriseMemberOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseAuditEntryData(GQLObject):
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI

class EnablePullRequestAutoMergeInput(GQLObject):
   pullRequestId: ID ##NON NULL
   commitHeadline: str
   commitBody: str
   mergeMethod: PullRequestMergeMethod
   authorEmail: str
   clientMutationId: str

class DraftPullRequestReviewComment(GQLObject):
   path: str ##NON NULL
   position: int ##NON NULL
   body: str ##NON NULL

class DismissPullRequestReviewInput(GQLObject):
   pullRequestReviewId: ID ##NON NULL
   message: str ##NON NULL
   clientMutationId: str

class DiscussionOrder(GQLObject):
   field: DiscussionOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class DeploymentOrder(GQLObject):
   field: DeploymentOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class DependabotUpdateError(GQLObject):
   body: str ##NON NULL
   errorType: str ##NON NULL
   title: str ##NON NULL

class DeleteTeamDiscussionPayload(GQLObject):
   clientMutationId: str

class DeleteTeamDiscussionCommentPayload(GQLObject):
   clientMutationId: str

class DeleteRefPayload(GQLObject):
   clientMutationId: str

class DeletePullRequestReviewInput(GQLObject):
   pullRequestReviewId: ID ##NON NULL
   clientMutationId: str

class DeleteProjectV2ItemPayload(GQLObject):
   clientMutationId: str
   deletedItemId: ID

class DeleteProjectNextItemPayload(GQLObject):
   clientMutationId: str

class DeleteProjectInput(GQLObject):
   projectId: ID ##NON NULL
   clientMutationId: str

class DeleteProjectCardInput(GQLObject):
   cardId: ID ##NON NULL
   clientMutationId: str

class DeleteIssueInput(GQLObject):
   issueId: ID ##NON NULL
   clientMutationId: str

class DeleteIssueCommentInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteEnvironmentPayload(GQLObject):
   clientMutationId: str

class DeleteDiscussionInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteDeploymentPayload(GQLObject):
   clientMutationId: str

class DeleteBranchProtectionRulePayload(GQLObject):
   clientMutationId: str

class Deletable(GQLObject):
   viewerCanDelete: bool ##NON NULL

class CreateTeamDiscussionInput(GQLObject):
   teamId: ID ##NON NULL
   title: str ##NON NULL
   body: str ##NON NULL
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
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   oid: GitObjectID ##NON NULL
   clientMutationId: str

class CreateProjectV2Input(GQLObject):
   ownerId: ID ##NON NULL
   title: str ##NON NULL
   repositoryId: ID
   teamId: ID
   clientMutationId: str

class CreateMigrationSourceInput(GQLObject):
   name: str ##NON NULL
   url: str ##NON NULL
   accessToken: str
   type: MigrationSourceType ##NON NULL
   ownerId: ID ##NON NULL
   githubPat: str
   clientMutationId: str

class CreateIssueInput(GQLObject):
   repositoryId: ID ##NON NULL
   title: str ##NON NULL
   body: str
   assigneeIds: list[ID] ##NON NULL
   milestoneId: ID
   labelIds: list[ID] ##NON NULL
   projectIds: list[ID] ##NON NULL
   issueTemplate: str
   clientMutationId: str

class CreateEnvironmentInput(GQLObject):
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   clientMutationId: str

class CreateDiscussionInput(GQLObject):
   repositoryId: ID ##NON NULL
   title: str ##NON NULL
   body: str ##NON NULL
   categoryId: ID ##NON NULL
   clientMutationId: str

class CreateAttributionInvitationInput(GQLObject):
   ownerId: ID ##NON NULL
   sourceId: ID ##NON NULL
   targetId: ID ##NON NULL
   clientMutationId: str

class ConvertProjectCardNoteToIssueInput(GQLObject):
   projectCardId: ID ##NON NULL
   repositoryId: ID ##NON NULL
   title: str
   body: str
   clientMutationId: str

class ContributionCalendarMonth(GQLObject):
   firstDay: Date ##NON NULL
   name: str ##NON NULL
   totalWeeks: int ##NON NULL
   year: int ##NON NULL

class CommittableBranch(GQLObject):
   id: ID
   repositoryNameWithOwner: str
   branchName: str

class CommitContributionOrder(GQLObject):
   field: CommitContributionOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class CodeOfConduct(GQLObject):
   body: str
   id: ID ##NON NULL
   key: str ##NON NULL
   name: str ##NON NULL
   resourcePath: URI
   url: URI

class CloseIssueInput(GQLObject):
   issueId: ID ##NON NULL
   stateReason: IssueClosedStateReason
   clientMutationId: str

class CloneTemplateRepositoryInput(GQLObject):
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   ownerId: ID ##NON NULL
   description: str
   visibility: RepositoryVisibility ##NON NULL
   includeAllBranches: bool
   clientMutationId: str

class ClearProjectV2ItemFieldValueInput(GQLObject):
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   fieldId: ID ##NON NULL
   clientMutationId: str

class CheckSuiteFilter(GQLObject):
   appId: int
   checkName: str

class CheckStep(GQLObject):
   completedAt: DateTime
   conclusion: CheckConclusionState
   externalId: str
   name: str ##NON NULL
   number: int ##NON NULL
   secondsToCompletion: int
   startedAt: DateTime
   status: CheckStatusState ##NON NULL

class CheckRunOutputImage(GQLObject):
   alt: str ##NON NULL
   imageUrl: URI ##NON NULL
   caption: str

class CheckRunAction(GQLObject):
   label: str ##NON NULL
   description: str ##NON NULL
   identifier: str ##NON NULL

class CheckAnnotationPosition(GQLObject):
   column: int
   line: int ##NON NULL

class CancelSponsorshipInput(GQLObject):
   sponsorId: ID
   sponsorLogin: str
   sponsorableId: ID
   sponsorableLogin: str
   clientMutationId: str

class CWE(GQLObject):
   cweId: str ##NON NULL
   description: str ##NON NULL
   id: ID ##NON NULL
   name: str ##NON NULL

class AuditLogOrder(GQLObject):
   field: AuditLogOrderField
   direction: OrderDirection

class ArchiveProjectV2ItemInput(GQLObject):
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   clientMutationId: str

class ApproveDeploymentsInput(GQLObject):
   workflowRunId: ID ##NON NULL
   environmentIds: list[ID] ##NON NULL
   comment: str
   clientMutationId: str

class AddUpvoteInput(GQLObject):
   subjectId: ID ##NON NULL
   clientMutationId: str

class AddReactionInput(GQLObject):
   subjectId: ID ##NON NULL
   content: ReactionContent ##NON NULL
   clientMutationId: str

class AddPullRequestReviewCommentInput(GQLObject):
   pullRequestId: ID
   pullRequestReviewId: ID
   commitOID: GitObjectID
   body: str ##NON NULL
   path: str
   position: int
   inReplyTo: ID
   clientMutationId: str

class AddProjectV2DraftIssueInput(GQLObject):
   projectId: ID ##NON NULL
   title: str ##NON NULL
   body: str
   assigneeIds: list[ID] ##NON NULL
   clientMutationId: str

class AddProjectDraftIssueInput(GQLObject):
   projectId: ID
   title: str
   body: str
   assigneeIds: list[ID] ##NON NULL
   clientMutationId: str

class AddProjectCardInput(GQLObject):
   projectColumnId: ID ##NON NULL
   contentId: ID
   note: str
   clientMutationId: str

class AddEnterpriseSupportEntitlementPayload(GQLObject):
   clientMutationId: str
   message: str

class AddEnterpriseOrganizationMemberInput(GQLObject):
   enterpriseId: ID ##NON NULL
   organizationId: ID ##NON NULL
   userIds: list[ID] ##NON NULL
   role: OrganizationMemberRole
   clientMutationId: str

class AddDiscussionCommentInput(GQLObject):
   discussionId: ID ##NON NULL
   replyToId: ID
   body: str ##NON NULL
   clientMutationId: str

class AddAssigneesToAssignableInput(GQLObject):
   assignableId: ID ##NON NULL
   assigneeIds: list[ID] ##NON NULL
   clientMutationId: str

class Actor(GQLObject):
   avatarUrl: URIField ##NON NULL
   login: str ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class AcceptEnterpriseAdministratorInvitationInput(GQLObject):
   invitationId: ID ##NON NULL
   clientMutationId: str

class AbortQueuedMigrationsInput(GQLObject):
   ownerId: ID ##NON NULL
   clientMutationId: str

class UserEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('User', GQLObject) ## Circular Reference for User

class UserConnection(GQLObject):
   edges: list[UserEdge]
   nodes: list[NewType('User', GQLObject)] ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class AutoMergeRequest(GQLObject):
   authorEmail: str
   commitBody: str
   commitHeadline: str
   enabledAt: DateTime
   enabledBy: Actor
   mergeMethod: PullRequestMergeMethod ##NON NULL
   pullRequest: NewType('PullRequest', GQLObject) ##NON NULL ## Circular Reference for PullRequest

class BranchProtectionRuleConflict(GQLObject):
   branchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   conflictingBranchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   ref: NewType('Ref', GQLObject) ## Circular Reference for Ref

class BranchProtectionRuleConflictEdge(GQLObject):
   cursor: str ##NON NULL
   node: BranchProtectionRuleConflict

class BranchProtectionRuleConflictConnection(GQLObject):
   edges: list[BranchProtectionRuleConflictEdge]
   nodes: list[BranchProtectionRuleConflict]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class TeamEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Team', GQLObject) ## Circular Reference for Team

class TeamConnection(GQLObject):
   edges: list[TeamEdge]
   nodes: list[NewType('Team', GQLObject)] ## Circular Reference for Team
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class Mannequin(GQLObject):
   avatarUrl: URIField ##NON NULL
   claimant: NewType('User', GQLObject) ## Circular Reference for User
   createdAt: DateTime ##NON NULL
   databaseId: int
   email: str
   id: ID ##NON NULL
   login: str ##NON NULL
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL

class Reactor(GQLObject): 
   pass

class ReactorEdge(GQLObject):
   cursor: str ##NON NULL
   node: Reactor ##NON NULL
   reactedAt: DateTime ##NON NULL

class ReactorConnection(GQLObject):
   edges: list[ReactorEdge]
   nodes: list[Reactor]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class Reaction(GQLObject):
   content: ReactionContent ##NON NULL
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   reactable: NewType('Reactable', GQLObject) ##NON NULL ## Circular Reference for Reactable
   user: NewType('User', GQLObject) ## Circular Reference for User

class ReactionEdge(GQLObject):
   cursor: str ##NON NULL
   node: Reaction

class ReactionConnection(GQLObject):
   edges: list[ReactionEdge]
   nodes: list[Reaction]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   viewerHasReacted: bool ##NON NULL

class ReactionConnectionField(ReactionConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: Args



class Reactable(GQLObject):
   databaseId: int
   id: ID ##NON NULL
   reactionGroups: list[NewType('ReactionGroup', GQLObject)] ## Circular Reference for ReactionGroup
   reactions: ReactionConnectionField ##NON NULL
   viewerCanReact: bool ##NON NULL

class ReactingUserEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User
   reactedAt: DateTime ##NON NULL

class ReactingUserConnection(GQLObject):
   edges: list[ReactingUserEdge]
   nodes: list[NewType('User', GQLObject)] ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ReactorConnectionField(ReactorConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class ReactionGroup(GQLObject):
   content: ReactionContent ##NON NULL
   createdAt: DateTime
   reactors: ReactorConnectionField ##NON NULL
   subject: Reactable ##NON NULL
   viewerHasReacted: bool ##NON NULL

class UserContentEdit(GQLObject):
   createdAt: DateTime ##NON NULL
   deletedAt: DateTime
   deletedBy: Actor
   diff: str
   editedAt: DateTime ##NON NULL
   editor: Actor
   id: ID ##NON NULL
   updatedAt: DateTime ##NON NULL

class UserContentEditEdge(GQLObject):
   cursor: str ##NON NULL
   node: UserContentEdit

class UserContentEditConnection(GQLObject):
   edges: list[UserContentEditEdge]
   nodes: list[UserContentEdit]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class UserContentEditConnectionField(UserContentEditConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class TeamDiscussionComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   bodyVersion: str ##NON NULL
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   discussion: NewType('TeamDiscussion', GQLObject) ##NON NULL ## Circular Reference for TeamDiscussion
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   lastEditedAt: DateTime
   number: int ##NON NULL
   publishedAt: DateTime
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanDelete: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL

class TeamDiscussionCommentEdge(GQLObject):
   cursor: str ##NON NULL
   node: TeamDiscussionComment

class TeamDiscussionCommentConnection(GQLObject):
   edges: list[TeamDiscussionCommentEdge]
   nodes: list[TeamDiscussionComment]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class TeamDiscussionCommentConnectionField(TeamDiscussionCommentConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: TeamDiscussionCommentOrder
      fromComment: int

   _args: Args



class TeamDiscussion(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   bodyVersion: str ##NON NULL
   comments: TeamDiscussionCommentConnectionField ##NON NULL
   commentsResourcePath: URI ##NON NULL
   commentsUrl: URI ##NON NULL
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   isPinned: bool ##NON NULL
   isPrivate: bool ##NON NULL
   lastEditedAt: DateTime
   number: int ##NON NULL
   publishedAt: DateTime
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   resourcePath: URI ##NON NULL
   team: NewType('Team', GQLObject) ##NON NULL ## Circular Reference for Team
   title: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanDelete: bool ##NON NULL
   viewerCanPin: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanSubscribe: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL
   viewerSubscription: SubscriptionState

class TeamDiscussionEdge(GQLObject):
   cursor: str ##NON NULL
   node: TeamDiscussion

class TeamDiscussionConnection(GQLObject):
   edges: list[TeamDiscussionEdge]
   nodes: list[TeamDiscussion]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class OrganizationInvitation(GQLObject):
   createdAt: DateTime ##NON NULL
   email: str
   id: ID ##NON NULL
   invitationType: OrganizationInvitationType ##NON NULL
   invitee: NewType('User', GQLObject) ## Circular Reference for User
   inviter: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User
   organization: NewType('Organization', GQLObject) ##NON NULL ## Circular Reference for Organization
   role: OrganizationInvitationRole ##NON NULL

class OrganizationInvitationEdge(GQLObject):
   cursor: str ##NON NULL
   node: OrganizationInvitation

class OrganizationInvitationConnection(GQLObject):
   edges: list[OrganizationInvitationEdge]
   nodes: list[OrganizationInvitation]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class UserStatus(GQLObject):
   createdAt: DateTime ##NON NULL
   emoji: str
   emojiHTML: HTML
   expiresAt: DateTime
   id: ID ##NON NULL
   indicatesLimitedAvailability: bool ##NON NULL
   message: str
   organization: NewType('Organization', GQLObject) ## Circular Reference for Organization
   updatedAt: DateTime ##NON NULL
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class UserStatusEdge(GQLObject):
   cursor: str ##NON NULL
   node: UserStatus

class UserStatusConnection(GQLObject):
   edges: list[UserStatusEdge]
   nodes: list[UserStatus]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class TeamMemberEdge(GQLObject):
   cursor: str ##NON NULL
   memberAccessResourcePath: URI ##NON NULL
   memberAccessUrl: URI ##NON NULL
   node: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User
   role: TeamMemberRole ##NON NULL

class TeamMemberConnection(GQLObject):
   edges: list[TeamMemberEdge]
   nodes: list[NewType('User', GQLObject)] ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2Field(GQLObject):
   createdAt: DateTime ##NON NULL
   dataType: ProjectV2FieldType ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   project: NewType('ProjectV2', GQLObject) ##NON NULL ## Circular Reference for ProjectV2
   updatedAt: DateTime ##NON NULL

class ProjectV2IterationFieldConfiguration(GQLObject):
   completedIterations: ProjectV2IterationFieldIteration ##NON NULL
   duration: int ##NON NULL
   iterations: ProjectV2IterationFieldIteration ##NON NULL
   startDay: int ##NON NULL

class ProjectV2IterationField(GQLObject):
   configuration: ProjectV2IterationFieldConfiguration ##NON NULL
   createdAt: DateTime ##NON NULL
   dataType: ProjectV2FieldType ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   project: NewType('ProjectV2', GQLObject) ##NON NULL ## Circular Reference for ProjectV2
   updatedAt: DateTime ##NON NULL

class ProjectV2SingleSelectField(GQLObject):
   createdAt: DateTime ##NON NULL
   dataType: ProjectV2FieldType ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   options: ProjectV2SingleSelectFieldOption ##NON NULL
   project: NewType('ProjectV2', GQLObject) ##NON NULL ## Circular Reference for ProjectV2
   updatedAt: DateTime ##NON NULL

class ProjectV2FieldConfiguration(GQLObject): 
   pass

class ProjectV2FieldConfigurationEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2FieldConfiguration

class ProjectV2FieldConfigurationConnection(GQLObject):
   edges: list[ProjectV2FieldConfigurationEdge]
   nodes: list[ProjectV2FieldConfiguration]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectNextField(GQLObject):
   id: ID ##NON NULL

class ProjectNextFieldEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectNextField

class ProjectNextFieldConnection(GQLObject):
   edges: list[ProjectNextFieldEdge]
   nodes: list[ProjectNextField]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class BranchProtectionRuleEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule

class BranchProtectionRuleConnection(GQLObject):
   edges: list[BranchProtectionRuleEdge]
   nodes: list[NewType('BranchProtectionRule', GQLObject)] ## Circular Reference for BranchProtectionRule
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class RepositoryCodeowners(GQLObject):
   errors: RepositoryCodeownersError ##NON NULL

class PermissionGranter(GQLObject): 
   pass

class PermissionSource(GQLObject):
   organization: NewType('Organization', GQLObject) ##NON NULL ## Circular Reference for Organization
   permission: DefaultRepositoryPermissionField ##NON NULL
   source: PermissionGranter ##NON NULL

class RepositoryCollaboratorEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User
   permission: RepositoryPermission ##NON NULL
   permissionSources: list[PermissionSource]

class RepositoryCollaboratorConnection(GQLObject):
   edges: list[RepositoryCollaboratorEdge]
   nodes: list[NewType('User', GQLObject)] ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeployKeyEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeployKey

class DeployKeyConnection(GQLObject):
   edges: list[DeployKeyEdge]
   nodes: list[DeployKey]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeploymentStatus(GQLObject):
   createdAt: DateTime ##NON NULL
   creator: Actor ##NON NULL
   deployment: NewType('Deployment', GQLObject) ##NON NULL ## Circular Reference for Deployment
   description: str
   environmentUrl: URI
   id: ID ##NON NULL
   logUrl: URI
   state: DeploymentStatusState ##NON NULL
   updatedAt: DateTime ##NON NULL

class DeploymentStatusEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeploymentStatus

class DeploymentStatusConnection(GQLObject):
   edges: list[DeploymentStatusEdge]
   nodes: list[DeploymentStatus]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeploymentStatusConnectionField(DeploymentStatusConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class Deployment(GQLObject):
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   commitOid: str ##NON NULL
   createdAt: DateTime ##NON NULL
   creator: Actor ##NON NULL
   databaseId: int
   description: str
   environment: str
   id: ID ##NON NULL
   latestEnvironment: str
   latestStatus: DeploymentStatus
   originalEnvironment: str
   payload: str
   ref: NewType('Ref', GQLObject) ## Circular Reference for Ref
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository
   state: DeploymentState
   statuses: DeploymentStatusConnectionField
   task: str
   updatedAt: DateTime ##NON NULL

class DeploymentEdge(GQLObject):
   cursor: str ##NON NULL
   node: Deployment

class DeploymentConnection(GQLObject):
   edges: list[DeploymentEdge]
   nodes: list[Deployment]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DiscussionCommentEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('DiscussionComment', GQLObject) ## Circular Reference for DiscussionComment

class DiscussionCommentConnection(GQLObject):
   edges: list[DiscussionCommentEdge]
   nodes: list[NewType('DiscussionComment', GQLObject)] ## Circular Reference for DiscussionComment
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DiscussionCommentConnectionField(DiscussionCommentConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class DiscussionComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   deletedAt: DateTime
   discussion: NewType('Discussion', GQLObject) ## Circular Reference for Discussion
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   isAnswer: bool ##NON NULL
   isMinimized: bool ##NON NULL
   lastEditedAt: DateTime
   minimizedReason: str
   publishedAt: DateTime
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   replies: DiscussionCommentConnectionField ##NON NULL
   replyTo: NewType('DiscussionComment', GQLObject) ## Circular Reference for DiscussionComment
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   upvoteCount: int ##NON NULL
   url: URI ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanDelete: bool ##NON NULL
   viewerCanMarkAsAnswer: bool ##NON NULL
   viewerCanMinimize: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanUnmarkAsAnswer: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCanUpvote: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL
   viewerHasUpvoted: bool ##NON NULL

class DiscussionCategory(GQLObject):
   createdAt: DateTime ##NON NULL
   description: str
   emoji: str ##NON NULL
   emojiHTML: HTML ##NON NULL
   id: ID ##NON NULL
   isAnswerable: bool ##NON NULL
   name: str ##NON NULL
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository
   slug: str ##NON NULL
   updatedAt: DateTime ##NON NULL

class IssueEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Issue', GQLObject) ## Circular Reference for Issue

class IssueConnection(GQLObject):
   edges: list[IssueEdge]
   nodes: list[NewType('Issue', GQLObject)] ## Circular Reference for Issue
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class IssueConnectionField(IssueConnection):
   class Args(GQLArgsSet): 
      orderBy: IssueOrder
      labels: list[str] ##NON NULL
      states: list[IssueState] ##NON NULL
      filterBy: IssueFilters
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PullRequestConnectionField(Generic[PullRequestConnection]):
   class Args(GQLArgsSet): 
      states: list[PullRequestState] ##NON NULL
      labels: list[str] ##NON NULL
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class Label(GQLObject):
   color: str ##NON NULL
   createdAt: DateTime
   description: str
   id: ID ##NON NULL
   isDefault: bool ##NON NULL
   issues: IssueConnectionField ##NON NULL
   name: str ##NON NULL
   pullRequests: PullRequestConnectionField ##NON NULL ## Circular Reference for PullRequestConnection
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository
   resourcePath: URI ##NON NULL
   updatedAt: DateTime
   url: URI ##NON NULL

class LabelEdge(GQLObject):
   cursor: str ##NON NULL
   node: Label

class LabelConnection(GQLObject):
   edges: list[LabelEdge]
   nodes: list[Label]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DiscussionPollOption(GQLObject):
   id: ID ##NON NULL
   option: str ##NON NULL
   poll: NewType('DiscussionPoll', GQLObject) ## Circular Reference for DiscussionPoll
   totalVoteCount: int ##NON NULL
   viewerHasVoted: bool ##NON NULL

class DiscussionPollOptionEdge(GQLObject):
   cursor: str ##NON NULL
   node: DiscussionPollOption

class DiscussionPollOptionConnection(GQLObject):
   edges: list[DiscussionPollOptionEdge]
   nodes: list[DiscussionPollOption]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DiscussionPollOptionConnectionField(DiscussionPollOptionConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionPollOptionOrder

   _args: Args



class DiscussionPoll(GQLObject):
   discussion: NewType('Discussion', GQLObject) ## Circular Reference for Discussion
   id: ID ##NON NULL
   options: DiscussionPollOptionConnectionField
   question: str ##NON NULL
   totalVoteCount: int ##NON NULL
   viewerCanVote: bool ##NON NULL
   viewerHasVoted: bool ##NON NULL

class LabelConnectionField(LabelConnection):
   class Args(GQLArgsSet): 
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class Discussion(GQLObject):
   activeLockReason: LockReason
   answer: DiscussionComment
   answerChosenAt: DateTime
   answerChosenBy: Actor
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   category: DiscussionCategory ##NON NULL
   comments: DiscussionCommentConnectionField ##NON NULL
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   labels: LabelConnectionField
   lastEditedAt: DateTime
   locked: bool ##NON NULL
   number: int ##NON NULL
   poll: DiscussionPoll
   publishedAt: DateTime
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository
   resourcePath: URI ##NON NULL
   title: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   upvoteCount: int ##NON NULL
   url: URI ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanDelete: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanSubscribe: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCanUpvote: bool ##NON NULL
   viewerDidAuthor: bool ##NON NULL
   viewerHasUpvoted: bool ##NON NULL
   viewerSubscription: SubscriptionState

class DiscussionCategoryEdge(GQLObject):
   cursor: str ##NON NULL
   node: DiscussionCategory

class DiscussionCategoryConnection(GQLObject):
   edges: list[DiscussionCategoryEdge]
   nodes: list[DiscussionCategory]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DiscussionEdge(GQLObject):
   cursor: str ##NON NULL
   node: Discussion

class DiscussionConnection(GQLObject):
   edges: list[DiscussionEdge]
   nodes: list[Discussion]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeploymentReviewer(GQLObject): 
   pass

class DeploymentReviewerEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeploymentReviewer

class DeploymentReviewerConnection(GQLObject):
   edges: list[DeploymentReviewerEdge]
   nodes: list[DeploymentReviewer]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeploymentReviewerConnectionField(DeploymentReviewerConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class DeploymentProtectionRule(GQLObject):
   databaseId: int
   reviewers: DeploymentReviewerConnectionField ##NON NULL
   timeout: int ##NON NULL
   type: DeploymentProtectionRuleType ##NON NULL

class DeploymentProtectionRuleEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeploymentProtectionRule

class DeploymentProtectionRuleConnection(GQLObject):
   edges: list[DeploymentProtectionRuleEdge]
   nodes: list[DeploymentProtectionRule]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeploymentProtectionRuleConnectionField(DeploymentProtectionRuleConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class Environment(GQLObject):
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   protectionRules: DeploymentProtectionRuleConnectionField ##NON NULL

class EnvironmentEdge(GQLObject):
   cursor: str ##NON NULL
   node: Environment

class EnvironmentConnection(GQLObject):
   edges: list[EnvironmentEdge]
   nodes: list[Environment]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class RepositoryEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Repository', GQLObject) ## Circular Reference for Repository

class RepositoryConnection(GQLObject):
   edges: list[RepositoryEdge]
   nodes: list[NewType('Repository', GQLObject)] ## Circular Reference for Repository
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   totalDiskUsage: int ##NON NULL

class IssueOrPullRequest(GQLObject): 
   pass

class LanguageEdge(GQLObject):
   cursor: str ##NON NULL
   node: Language ##NON NULL
   size: int ##NON NULL

class LanguageConnection(GQLObject):
   edges: list[LanguageEdge]
   nodes: list[Language]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   totalSize: int ##NON NULL

class ReleaseAsset(GQLObject):
   contentType: str ##NON NULL
   createdAt: DateTime ##NON NULL
   downloadCount: int ##NON NULL
   downloadUrl: URI ##NON NULL
   id: ID ##NON NULL
   name: str ##NON NULL
   release: NewType('Release', GQLObject) ## Circular Reference for Release
   size: int ##NON NULL
   updatedAt: DateTime ##NON NULL
   uploadedBy: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User
   url: URI ##NON NULL

class ReleaseAssetEdge(GQLObject):
   cursor: str ##NON NULL
   node: ReleaseAsset

class ReleaseAssetConnection(GQLObject):
   edges: list[ReleaseAssetEdge]
   nodes: list[ReleaseAsset]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class UserConnectionField(UserConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class ReleaseAssetConnectionField(ReleaseAssetConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      name: str

   _args: Args



class Release(GQLObject):
   author: NewType('User', GQLObject) ## Circular Reference for User
   createdAt: DateTime ##NON NULL
   databaseId: int
   description: str
   descriptionHTML: HTML
   id: ID ##NON NULL
   isDraft: bool ##NON NULL
   isLatest: bool ##NON NULL
   isPrerelease: bool ##NON NULL
   mentions: UserConnectionField
   name: str
   publishedAt: DateTime
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   releaseAssets: ReleaseAssetConnectionField ##NON NULL
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository
   resourcePath: URI ##NON NULL
   shortDescriptionHTML: HTMLField
   tag: NewType('Ref', GQLObject) ## Circular Reference for Ref
   tagCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   tagName: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   viewerCanReact: bool ##NON NULL

class License(GQLObject):
   body: str ##NON NULL
   conditions: LicenseRule ##NON NULL
   description: str
   featured: bool ##NON NULL
   hidden: bool ##NON NULL
   id: ID ##NON NULL
   implementation: str
   key: str ##NON NULL
   limitations: LicenseRule ##NON NULL
   name: str ##NON NULL
   nickname: str
   permissions: LicenseRule ##NON NULL
   pseudoLicense: bool ##NON NULL
   spdxId: str
   url: URI

class Milestone(GQLObject):
   closed: bool ##NON NULL
   closedAt: DateTime
   createdAt: DateTime ##NON NULL
   creator: Actor
   description: str
   dueOn: DateTime
   id: ID ##NON NULL
   issues: IssueConnectionField ##NON NULL
   number: int ##NON NULL
   progressPercentage: float ##NON NULL
   pullRequests: PullRequestConnectionField ##NON NULL
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository
   resourcePath: URI ##NON NULL
   state: MilestoneState ##NON NULL
   title: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL

class MilestoneEdge(GQLObject):
   cursor: str ##NON NULL
   node: Milestone

class MilestoneConnection(GQLObject):
   edges: list[MilestoneEdge]
   nodes: list[Milestone]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class GitObject(GQLObject):
   abbreviatedOid: str ##NON NULL
   commitResourcePath: URI ##NON NULL
   commitUrl: URI ##NON NULL
   id: ID ##NON NULL
   oid: GitObjectID ##NON NULL
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository

class RepositoryConnectionField(RepositoryConnection):
   class Args(GQLArgsSet): 
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

   _args: Args



class RepositoryField(Generic[Repository]):
   class Args(GQLArgsSet): 
      name: str ##NON NULL
      followRenames: bool

   _args: Args



class RepositoryOwner(GQLObject):
   avatarUrl: URIField ##NON NULL
   id: ID ##NON NULL
   login: str ##NON NULL
   repositories: RepositoryConnectionField ##NON NULL
   repository: RepositoryField ## Circular Reference for Repository
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class PackageFile(GQLObject):
   id: ID ##NON NULL
   md5: str
   name: str ##NON NULL
   packageVersion: NewType('PackageVersion', GQLObject) ## Circular Reference for PackageVersion
   sha1: str
   sha256: str
   size: int
   updatedAt: DateTime ##NON NULL
   url: URI

class PackageFileEdge(GQLObject):
   cursor: str ##NON NULL
   node: PackageFile

class PackageFileConnection(GQLObject):
   edges: list[PackageFileEdge]
   nodes: list[PackageFile]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PackageFileConnectionField(PackageFileConnection):
   class Args(GQLArgsSet): 
      orderBy: PackageFileOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PackageVersion(GQLObject):
   files: PackageFileConnectionField ##NON NULL
   id: ID ##NON NULL
   package: NewType('Package', GQLObject) ## Circular Reference for Package
   platform: str
   preRelease: bool ##NON NULL
   readme: str
   release: Release
   statistics: PackageVersionStatistics
   summary: str
   version: str ##NON NULL

class PackageVersionEdge(GQLObject):
   cursor: str ##NON NULL
   node: PackageVersion

class PackageVersionConnection(GQLObject):
   edges: list[PackageVersionEdge]
   nodes: list[PackageVersion]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PackageVersionField(PackageVersion):
   class Args(GQLArgsSet): 
      version: str ##NON NULL

   _args: Args



class PackageVersionConnectionField(PackageVersionConnection):
   class Args(GQLArgsSet): 
      orderBy: PackageVersionOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class Package(GQLObject):
   id: ID ##NON NULL
   latestVersion: PackageVersion
   name: str ##NON NULL
   packageType: PackageType ##NON NULL
   repository: Repository
   statistics: PackageStatistics
   version: PackageVersionField
   versions: PackageVersionConnectionField ##NON NULL

class PackageEdge(GQLObject):
   cursor: str ##NON NULL
   node: Package

class PackageConnection(GQLObject):
   edges: list[PackageEdge]
   nodes: list[Package]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PinnedDiscussion(GQLObject):
   createdAt: DateTime ##NON NULL
   databaseId: int
   discussion: Discussion ##NON NULL
   gradientStopColors: str ##NON NULL
   id: ID ##NON NULL
   pattern: PinnedDiscussionPattern ##NON NULL
   pinnedBy: Actor ##NON NULL
   preconfiguredGradient: PinnedDiscussionGradient
   repository: Repository ##NON NULL
   updatedAt: DateTime ##NON NULL

class PinnedDiscussionEdge(GQLObject):
   cursor: str ##NON NULL
   node: PinnedDiscussion

class PinnedDiscussionConnection(GQLObject):
   edges: list[PinnedDiscussionEdge]
   nodes: list[PinnedDiscussion]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PinnedIssue(GQLObject):
   databaseId: int
   id: ID ##NON NULL
   issue: NewType('Issue', GQLObject) ##NON NULL ## Circular Reference for Issue
   pinnedBy: Actor ##NON NULL
   repository: Repository ##NON NULL

class PinnedIssueEdge(GQLObject):
   cursor: str ##NON NULL
   node: PinnedIssue

class PinnedIssueConnection(GQLObject):
   edges: list[PinnedIssueEdge]
   nodes: list[PinnedIssue]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectCardItem(GQLObject): 
   pass

class ProjectCard(GQLObject):
   column: NewType('ProjectColumn', GQLObject) ## Circular Reference for ProjectColumn
   content: ProjectCardItem
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   id: ID ##NON NULL
   isArchived: bool ##NON NULL
   note: str
   project: NewType('Project', GQLObject) ##NON NULL ## Circular Reference for Project
   resourcePath: URI ##NON NULL
   state: ProjectCardState
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL

class ProjectCardEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectCard

class ProjectCardConnection(GQLObject):
   edges: list[ProjectCardEdge]
   nodes: list[ProjectCard]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectCardConnectionField(ProjectCardConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      archivedStates: list[ProjectCardArchivedState]

   _args: Args



class ProjectColumn(GQLObject):
   cards: ProjectCardConnectionField ##NON NULL
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   project: NewType('Project', GQLObject) ##NON NULL ## Circular Reference for Project
   purpose: ProjectColumnPurpose
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL

class ProjectColumnEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectColumn

class ProjectColumnConnection(GQLObject):
   edges: list[ProjectColumnEdge]
   nodes: list[ProjectColumn]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Project', GQLObject) ## Circular Reference for Project

class ProjectConnection(GQLObject):
   edges: list[ProjectEdge]
   nodes: list[NewType('Project', GQLObject)] ## Circular Reference for Project
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectField(Generic[Project]):
   class Args(GQLArgsSet): 
      number: int ##NON NULL

   _args: Args



class ProjectConnectionField(ProjectConnection):
   class Args(GQLArgsSet): 
      orderBy: ProjectOrder
      search: str
      states: list[ProjectState] ##NON NULL
      after: str
      before: str
      first: int
      last: int

   _args: Args



class ProjectOwner(GQLObject):
   id: ID ##NON NULL
   project: ProjectField ## Circular Reference for Project
   projects: ProjectConnectionField ##NON NULL
   projectsResourcePath: URI ##NON NULL
   projectsUrl: URI ##NON NULL
   viewerCanCreateProjects: bool ##NON NULL

class ProjectColumnConnectionField(ProjectColumnConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class Project(GQLObject):
   body: str
   bodyHTML: HTML ##NON NULL
   closed: bool ##NON NULL
   closedAt: DateTime
   columns: ProjectColumnConnectionField ##NON NULL
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   number: int ##NON NULL
   owner: ProjectOwner ##NON NULL
   pendingCards: ProjectCardConnectionField ##NON NULL
   progress: ProjectProgress ##NON NULL
   resourcePath: URI ##NON NULL
   state: ProjectState ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   viewerCanUpdate: bool ##NON NULL

class ProjectNextEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('ProjectNext', GQLObject) ## Circular Reference for ProjectNext

class ProjectNextConnection(GQLObject):
   edges: list[ProjectNextEdge]
   nodes: list[NewType('ProjectNext', GQLObject)] ## Circular Reference for ProjectNext
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2Edge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2

class ProjectV2Connection(GQLObject):
   edges: list[ProjectV2Edge]
   nodes: list[NewType('ProjectV2', GQLObject)] ## Circular Reference for ProjectV2
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PullRequestTemplate(GQLObject):
   body: str
   filename: str
   repository: Repository ##NON NULL

class RefEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Ref', GQLObject) ## Circular Reference for Ref

class RefConnection(GQLObject):
   edges: list[RefEdge]
   nodes: list[NewType('Ref', GQLObject)] ## Circular Reference for Ref
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ReleaseEdge(GQLObject):
   cursor: str ##NON NULL
   node: Release

class ReleaseConnection(GQLObject):
   edges: list[ReleaseEdge]
   nodes: list[Release]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class StargazerEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User
   starredAt: DateTime ##NON NULL

class StargazerConnection(GQLObject):
   edges: list[StargazerEdge]
   nodes: list[NewType('User', GQLObject)] ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class TopicField(Generic[Topic]):
   class Args(GQLArgsSet): 
      first: int

   _args: Args



class StargazerConnectionField(StargazerConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: Args



class Topic(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   relatedTopics: TopicField ##NON NULL ## Circular Reference for Topic
   repositories: RepositoryConnectionField ##NON NULL
   stargazerCount: int ##NON NULL
   stargazers: StargazerConnectionField ##NON NULL
   viewerHasStarred: bool ##NON NULL

class RepositoryTopic(GQLObject):
   id: ID ##NON NULL
   resourcePath: URI ##NON NULL
   topic: Topic ##NON NULL
   url: URI ##NON NULL

class RepositoryTopicEdge(GQLObject):
   cursor: str ##NON NULL
   node: RepositoryTopic

class RepositoryTopicConnection(GQLObject):
   edges: list[RepositoryTopicEdge]
   nodes: list[RepositoryTopic]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SubmoduleEdge(GQLObject):
   cursor: str ##NON NULL
   node: Submodule

class SubmoduleConnection(GQLObject):
   edges: list[SubmoduleEdge]
   nodes: list[Submodule]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DependabotUpdate(GQLObject):
   error: DependabotUpdateError
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   repository: Repository ##NON NULL

class CWEEdge(GQLObject):
   cursor: str ##NON NULL
   node: CWE

class CWEConnection(GQLObject):
   edges: list[CWEEdge]
   nodes: list[CWE]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SecurityVulnerability(GQLObject):
   advisory: NewType('SecurityAdvisory', GQLObject) ##NON NULL ## Circular Reference for SecurityAdvisory
   firstPatchedVersion: SecurityAdvisoryPackageVersion
   package: SecurityAdvisoryPackage ##NON NULL
   severity: SecurityAdvisorySeverity ##NON NULL
   updatedAt: DateTime ##NON NULL
   vulnerableVersionRange: str ##NON NULL

class SecurityVulnerabilityEdge(GQLObject):
   cursor: str ##NON NULL
   node: SecurityVulnerability

class SecurityVulnerabilityConnection(GQLObject):
   edges: list[SecurityVulnerabilityEdge]
   nodes: list[SecurityVulnerability]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CWEConnectionField(CWEConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class SecurityVulnerabilityConnectionField(SecurityVulnerabilityConnection):
   class Args(GQLArgsSet): 
      orderBy: SecurityVulnerabilityOrder
      ecosystem: SecurityAdvisoryEcosystem
      package: str
      severities: list[SecurityAdvisorySeverity] ##NON NULL
      classifications: list[SecurityAdvisoryClassification] ##NON NULL
      after: str
      before: str
      first: int
      last: int

   _args: Args



class SecurityAdvisory(GQLObject):
   classification: SecurityAdvisoryClassification ##NON NULL
   cvss: CVSS ##NON NULL
   cwes: CWEConnectionField ##NON NULL
   databaseId: int
   description: str ##NON NULL
   ghsaId: str ##NON NULL
   id: ID ##NON NULL
   identifiers: SecurityAdvisoryIdentifier ##NON NULL
   notificationsPermalink: URI
   origin: str ##NON NULL
   permalink: URI
   publishedAt: DateTime ##NON NULL
   references: SecurityAdvisoryReference ##NON NULL
   severity: SecurityAdvisorySeverity ##NON NULL
   summary: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   vulnerabilities: SecurityVulnerabilityConnectionField ##NON NULL
   withdrawnAt: DateTime

class RepositoryVulnerabilityAlert(GQLObject):
   createdAt: DateTime ##NON NULL
   dependabotUpdate: DependabotUpdate
   dependencyScope: RepositoryVulnerabilityAlertDependencyScope
   dismissComment: str
   dismissReason: str
   dismissedAt: DateTime
   dismisser: NewType('User', GQLObject) ## Circular Reference for User
   fixedAt: DateTime
   id: ID ##NON NULL
   number: int ##NON NULL
   repository: Repository ##NON NULL
   securityAdvisory: SecurityAdvisory
   securityVulnerability: SecurityVulnerability
   state: RepositoryVulnerabilityAlertState ##NON NULL
   vulnerableManifestFilename: str ##NON NULL
   vulnerableManifestPath: str ##NON NULL
   vulnerableRequirements: str

class RepositoryVulnerabilityAlertEdge(GQLObject):
   cursor: str ##NON NULL
   node: RepositoryVulnerabilityAlert

class RepositoryVulnerabilityAlertConnection(GQLObject):
   edges: list[RepositoryVulnerabilityAlertEdge]
   nodes: list[RepositoryVulnerabilityAlert]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class BranchProtectionRuleConnectionField(BranchProtectionRuleConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class RepositoryCodeownersField(RepositoryCodeowners):
   class Args(GQLArgsSet): 
      refName: str

   _args: Args



class RepositoryCollaboratorConnectionField(RepositoryCollaboratorConnection):
   class Args(GQLArgsSet): 
      affiliation: CollaboratorAffiliation
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: Args



class CommitCommentConnectionField(Generic[CommitCommentConnection]):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class DeployKeyConnectionField(DeployKeyConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class DeploymentConnectionField(DeploymentConnection):
   class Args(GQLArgsSet): 
      environments: list[str] ##NON NULL
      orderBy: DeploymentOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class DiscussionField(Discussion):
   class Args(GQLArgsSet): 
      number: int ##NON NULL

   _args: Args



class DiscussionCategoryConnectionField(DiscussionCategoryConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      filterByAssignable: bool

   _args: Args



class DiscussionCategoryField(DiscussionCategory):
   class Args(GQLArgsSet): 
      slug: str ##NON NULL

   _args: Args



class DiscussionConnectionField(DiscussionConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      categoryId: ID
      orderBy: DiscussionOrder

   _args: Args



class EnvironmentField(Environment):
   class Args(GQLArgsSet): 
      name: str ##NON NULL

   _args: Args



class EnvironmentConnectionField(EnvironmentConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class IssueField(Generic[Issue]):
   class Args(GQLArgsSet): 
      number: int ##NON NULL

   _args: Args



class IssueOrPullRequestField(IssueOrPullRequest):
   class Args(GQLArgsSet): 
      number: int ##NON NULL

   _args: Args



class LabelField(Label):
   class Args(GQLArgsSet): 
      name: str ##NON NULL

   _args: Args



class LanguageConnectionField(LanguageConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: LanguageOrder

   _args: Args



class MilestoneField(Milestone):
   class Args(GQLArgsSet): 
      number: int ##NON NULL

   _args: Args



class MilestoneConnectionField(MilestoneConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      states: list[MilestoneState] ##NON NULL
      orderBy: MilestoneOrder
      query: str

   _args: Args



class GitObjectField(GitObject):
   class Args(GQLArgsSet): 
      oid: GitObjectID
      expression: str

   _args: Args



class PackageConnectionField(PackageConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      names: list[str]
      repositoryId: ID
      packageType: PackageType
      orderBy: PackageOrder

   _args: Args



class PinnedDiscussionConnectionField(PinnedDiscussionConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PinnedIssueConnectionField(PinnedIssueConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class ProjectV2ConnectionField(ProjectV2Connection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: ProjectV2Order

   _args: Args



class PullRequestField(Generic[PullRequest]):
   class Args(GQLArgsSet): 
      number: int ##NON NULL

   _args: Args



class RefField(Generic[Ref]):
   class Args(GQLArgsSet): 
      qualifiedName: str ##NON NULL

   _args: Args



class RefConnectionField(RefConnection):
   class Args(GQLArgsSet): 
      query: str
      after: str
      before: str
      first: int
      last: int
      refPrefix: str ##NON NULL
      direction: OrderDirection
      orderBy: RefOrder

   _args: Args



class ReleaseField(Release):
   class Args(GQLArgsSet): 
      tagName: str ##NON NULL

   _args: Args



class ReleaseConnectionField(ReleaseConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ReleaseOrder

   _args: Args



class RepositoryTopicConnectionField(RepositoryTopicConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class SubmoduleConnectionField(SubmoduleConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class RepositoryVulnerabilityAlertConnectionField(RepositoryVulnerabilityAlertConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      states: list[RepositoryVulnerabilityAlertState] ##NON NULL
      dependencyScopes: list[RepositoryVulnerabilityAlertDependencyScope] ##NON NULL

   _args: Args



class Repository(GQLObject):
   allowUpdateBranch: bool ##NON NULL
   assignableUsers: UserConnectionField ##NON NULL
   autoMergeAllowed: bool ##NON NULL
   branchProtectionRules: BranchProtectionRuleConnectionField ##NON NULL
   codeOfConduct: CodeOfConduct
   codeowners: RepositoryCodeownersField
   collaborators: RepositoryCollaboratorConnectionField
   commitComments: CommitCommentConnectionField ##NON NULL ## Circular Reference for CommitCommentConnection
   contactLinks: list[RepositoryContactLink]
   createdAt: DateTime ##NON NULL
   databaseId: int
   defaultBranchRef: NewType('Ref', GQLObject) ## Circular Reference for Ref
   deleteBranchOnMerge: bool ##NON NULL
   deployKeys: DeployKeyConnectionField ##NON NULL
   deployments: DeploymentConnectionField ##NON NULL
   description: str
   descriptionHTML: HTML ##NON NULL
   discussion: DiscussionField
   discussionCategories: DiscussionCategoryConnectionField ##NON NULL
   discussionCategory: DiscussionCategoryField
   discussions: DiscussionConnectionField ##NON NULL
   diskUsage: int
   environment: EnvironmentField
   environments: EnvironmentConnectionField ##NON NULL
   forkCount: int ##NON NULL
   forkingAllowed: bool ##NON NULL
   forks: RepositoryConnectionField ##NON NULL
   fundingLinks: FundingLink ##NON NULL
   hasDiscussionsEnabled: bool ##NON NULL
   hasIssuesEnabled: bool ##NON NULL
   hasProjectsEnabled: bool ##NON NULL
   hasVulnerabilityAlertsEnabled: bool ##NON NULL
   hasWikiEnabled: bool ##NON NULL
   homepageUrl: URI
   id: ID ##NON NULL
   interactionAbility: RepositoryInteractionAbility
   isArchived: bool ##NON NULL
   isBlankIssuesEnabled: bool ##NON NULL
   isDisabled: bool ##NON NULL
   isEmpty: bool ##NON NULL
   isFork: bool ##NON NULL
   isInOrganization: bool ##NON NULL
   isLocked: bool ##NON NULL
   isMirror: bool ##NON NULL
   isPrivate: bool ##NON NULL
   isSecurityPolicyEnabled: bool
   isTemplate: bool ##NON NULL
   isUserConfigurationRepository: bool ##NON NULL
   issue: IssueField ## Circular Reference for Issue
   issueOrPullRequest: IssueOrPullRequestField
   issueTemplates: list[IssueTemplate]
   issues: IssueConnectionField ##NON NULL
   label: LabelField
   labels: LabelConnectionField
   languages: LanguageConnectionField
   latestRelease: Release
   licenseInfo: License
   lockReason: RepositoryLockReason
   mentionableUsers: UserConnectionField ##NON NULL
   mergeCommitAllowed: bool ##NON NULL
   mergeCommitMessage: MergeCommitMessage ##NON NULL
   mergeCommitTitle: MergeCommitTitle ##NON NULL
   milestone: MilestoneField
   milestones: MilestoneConnectionField
   mirrorUrl: URI
   name: str ##NON NULL
   nameWithOwner: str ##NON NULL
   object: GitObjectField
   openGraphImageUrl: URI ##NON NULL
   owner: RepositoryOwner ##NON NULL
   packages: PackageConnectionField ##NON NULL
   parent: Repository
   pinnedDiscussions: PinnedDiscussionConnectionField ##NON NULL
   pinnedIssues: PinnedIssueConnectionField
   primaryLanguage: Language
   project: ProjectField
   projectV2: ProjectV2Field ## Circular Reference for ProjectV2
   projects: ProjectConnectionField ##NON NULL
   projectsResourcePath: URI ##NON NULL
   projectsUrl: URI ##NON NULL
   projectsV2: ProjectV2ConnectionField ##NON NULL
   pullRequest: PullRequestField ## Circular Reference for PullRequest
   pullRequestTemplates: list[PullRequestTemplate]
   pullRequests: PullRequestConnectionField ##NON NULL
   pushedAt: DateTime
   rebaseMergeAllowed: bool ##NON NULL
   recentProjects: ProjectV2ConnectionField ##NON NULL
   ref: RefField ## Circular Reference for Ref
   refs: RefConnectionField
   release: ReleaseField
   releases: ReleaseConnectionField ##NON NULL
   repositoryTopics: RepositoryTopicConnectionField ##NON NULL
   resourcePath: URI ##NON NULL
   securityPolicyUrl: URI
   shortDescriptionHTML: HTMLField ##NON NULL
   squashMergeAllowed: bool ##NON NULL
   squashMergeCommitMessage: SquashMergeCommitMessage ##NON NULL
   squashMergeCommitTitle: SquashMergeCommitTitle ##NON NULL
   sshUrl: GitSSHRemote ##NON NULL
   stargazerCount: int ##NON NULL
   stargazers: StargazerConnectionField ##NON NULL
   submodules: SubmoduleConnectionField ##NON NULL
   tempCloneToken: str
   templateRepository: Repository
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   usesCustomOpenGraphImage: bool ##NON NULL
   viewerCanAdminister: bool ##NON NULL
   viewerCanCreateProjects: bool ##NON NULL
   viewerCanSubscribe: bool ##NON NULL
   viewerCanUpdateTopics: bool ##NON NULL
   viewerDefaultCommitEmail: str
   viewerDefaultMergeMethod: PullRequestMergeMethod ##NON NULL
   viewerHasStarred: bool ##NON NULL
   viewerPermission: RepositoryPermission
   viewerPossibleCommitEmails: list[str]
   viewerSubscription: SubscriptionState
   visibility: RepositoryVisibility ##NON NULL
   vulnerabilityAlerts: RepositoryVulnerabilityAlertConnectionField
   watchers: UserConnectionField ##NON NULL
   webCommitSignoffRequired: bool ##NON NULL

class IssueComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   isMinimized: bool ##NON NULL
   issue: NewType('Issue', GQLObject) ##NON NULL ## Circular Reference for Issue
   lastEditedAt: DateTime
   minimizedReason: str
   publishedAt: DateTime
   pullRequest: NewType('PullRequest', GQLObject) ## Circular Reference for PullRequest
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanDelete: bool ##NON NULL
   viewerCanMinimize: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL

class IssueCommentEdge(GQLObject):
   cursor: str ##NON NULL
   node: IssueComment

class IssueCommentConnection(GQLObject):
   edges: list[IssueCommentEdge]
   nodes: list[IssueComment]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class Hovercard(GQLObject):
   contexts: HovercardContext ##NON NULL

class LinkedBranch(GQLObject):
   id: ID ##NON NULL
   ref: Ref

class LinkedBranchEdge(GQLObject):
   cursor: str ##NON NULL
   node: LinkedBranch

class LinkedBranchConnection(GQLObject):
   edges: list[LinkedBranchEdge]
   nodes: list[LinkedBranch]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class Assignable(GQLObject):
   assignees: UserConnectionField ##NON NULL

class Assignee(GQLObject): 
   pass

class AssignedEvent(GQLObject):
   actor: Actor
   assignable: Assignable ##NON NULL
   assignee: Assignee
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL

class Closer(GQLObject): 
   pass

class ClosedEvent(GQLObject):
   actor: Actor
   closable: Closable ##NON NULL
   closer: Closer
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   resourcePath: URI ##NON NULL
   stateReason: IssueStateReason
   url: URI ##NON NULL

class ReferencedSubject(GQLObject): 
   pass

class CrossReferencedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   isCrossRepository: bool ##NON NULL
   referencedAt: DateTime ##NON NULL
   resourcePath: URI ##NON NULL
   source: ReferencedSubject ##NON NULL
   target: ReferencedSubject ##NON NULL
   url: URI ##NON NULL
   willCloseTarget: bool ##NON NULL

class MilestoneItem(GQLObject): 
   pass

class DemilestonedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   milestoneTitle: str ##NON NULL
   subject: MilestoneItem ##NON NULL

class Labelable(GQLObject):
   labels: LabelConnectionField

class LabeledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   label: Label ##NON NULL
   labelable: Labelable ##NON NULL

class LockedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   lockReason: LockReason
   lockable: Lockable ##NON NULL

class MilestonedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   milestoneTitle: str ##NON NULL
   subject: MilestoneItem ##NON NULL

class ReferencedEvent(GQLObject):
   actor: Actor
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   commitRepository: Repository ##NON NULL
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   isCrossRepository: bool ##NON NULL
   isDirectReference: bool ##NON NULL
   subject: ReferencedSubject ##NON NULL

class RenamedTitleSubject(GQLObject): 
   pass

class RenamedTitleEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   currentTitle: str ##NON NULL
   id: ID ##NON NULL
   previousTitle: str ##NON NULL
   subject: RenamedTitleSubject ##NON NULL

class ReopenedEvent(GQLObject):
   actor: Actor
   closable: Closable ##NON NULL
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   stateReason: IssueStateReason

class SubscribedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   subscribable: Subscribable ##NON NULL

class TransferredEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   fromRepository: Repository
   id: ID ##NON NULL
   issue: Issue ##NON NULL

class UnassignedEvent(GQLObject):
   actor: Actor
   assignable: Assignable ##NON NULL
   assignee: Assignee
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL

class UnlabeledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   label: Label ##NON NULL
   labelable: Labelable ##NON NULL

class UnlockedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   lockable: Lockable ##NON NULL

class UnsubscribedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   subscribable: Subscribable ##NON NULL

class UserBlockedEvent(GQLObject):
   actor: Actor
   blockDuration: UserBlockDuration ##NON NULL
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   subject: NewType('User', GQLObject) ## Circular Reference for User

class IssueTimelineItem(GQLObject): 
   pass

class IssueTimelineItemEdge(GQLObject):
   cursor: str ##NON NULL
   node: IssueTimelineItem

class IssueTimelineConnection(GQLObject):
   edges: list[IssueTimelineItemEdge]
   nodes: list[IssueTimelineItem]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class AddedToProjectEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL

class CommentDeletedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   databaseId: int
   deletedCommentAuthor: Actor
   id: ID ##NON NULL

class ConnectedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   isCrossRepository: bool ##NON NULL
   source: ReferencedSubject ##NON NULL
   subject: ReferencedSubject ##NON NULL

class ConvertedNoteToIssueEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL

class ConvertedToDiscussionEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   discussion: Discussion
   id: ID ##NON NULL

class DisconnectedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   isCrossRepository: bool ##NON NULL
   source: ReferencedSubject ##NON NULL
   subject: ReferencedSubject ##NON NULL

class MarkedAsDuplicateEvent(GQLObject):
   actor: Actor
   canonical: IssueOrPullRequest
   createdAt: DateTime ##NON NULL
   duplicate: IssueOrPullRequest
   id: ID ##NON NULL
   isCrossRepository: bool ##NON NULL

class MentionedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL

class MovedColumnsInProjectEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL

class PinnedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   issue: Issue ##NON NULL

class RemovedFromProjectEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL

class UnmarkedAsDuplicateEvent(GQLObject):
   actor: Actor
   canonical: IssueOrPullRequest
   createdAt: DateTime ##NON NULL
   duplicate: IssueOrPullRequest
   id: ID ##NON NULL
   isCrossRepository: bool ##NON NULL

class UnpinnedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   issue: Issue ##NON NULL

class IssueTimelineItems(GQLObject): 
   pass

class IssueTimelineItemsEdge(GQLObject):
   cursor: str ##NON NULL
   node: IssueTimelineItems

class IssueTimelineItemsConnection(GQLObject):
   edges: list[IssueTimelineItemsEdge]
   filteredCount: int ##NON NULL
   nodes: list[IssueTimelineItems]
   pageCount: int ##NON NULL
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   updatedAt: DateTime ##NON NULL

class IssueCommentConnectionField(IssueCommentConnection):
   class Args(GQLArgsSet): 
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class HovercardField(Hovercard):
   class Args(GQLArgsSet): 
      includeNotificationContexts: bool

   _args: Args



class LinkedBranchConnectionField(LinkedBranchConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class ProjectV2ItemConnectionField(Generic[ProjectV2ItemConnection]):
   class Args(GQLArgsSet): 
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: Args



class ProjectNextItemConnectionField(Generic[ProjectNextItemConnection]):
   class Args(GQLArgsSet): 
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: Args



class IssueTimelineItemsConnectionField(IssueTimelineItemsConnection):
   class Args(GQLArgsSet): 
      since: DateTime
      skip: int
      itemTypes: list[IssueTimelineItemsItemType] ##NON NULL
      after: str
      before: str
      first: int
      last: int

   _args: Args



class Issue(GQLObject):
   activeLockReason: LockReason
   assignees: UserConnectionField ##NON NULL
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyResourcePath: URI ##NON NULL
   bodyText: str ##NON NULL
   bodyUrl: URI ##NON NULL
   closed: bool ##NON NULL
   closedAt: DateTime
   comments: IssueCommentConnectionField ##NON NULL
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   editor: Actor
   hovercard: HovercardField ##NON NULL
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   isPinned: bool
   isReadByViewer: bool
   labels: LabelConnectionField
   lastEditedAt: DateTime
   linkedBranches: LinkedBranchConnectionField ##NON NULL
   locked: bool ##NON NULL
   milestone: Milestone
   number: int ##NON NULL
   participants: UserConnectionField ##NON NULL
   projectCards: ProjectCardConnectionField ##NON NULL
   projectItems: ProjectV2ItemConnectionField ##NON NULL ## Circular Reference for ProjectV2ItemConnection
   projectNextItems: ProjectNextItemConnectionField ##NON NULL ## Circular Reference for ProjectNextItemConnection
   projectV2: ProjectV2Field ## Circular Reference for ProjectV2
   projectsV2: ProjectV2ConnectionField ##NON NULL
   publishedAt: DateTime
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   state: IssueState ##NON NULL
   stateReason: IssueStateReason
   timelineItems: IssueTimelineItemsConnectionField ##NON NULL
   title: str ##NON NULL
   titleHTML: str ##NON NULL
   trackedInIssues: IssueConnectionField ##NON NULL
   trackedIssues: IssueConnectionField ##NON NULL
   trackedIssuesCount: trackedIssuesCountField ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanReact: bool ##NON NULL
   viewerCanSubscribe: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL
   viewerSubscription: SubscriptionState

class ProjectNextItemContent(GQLObject): 
   pass

class ProjectNextItemFieldValue(GQLObject):
   id: ID ##NON NULL

class ProjectNextItemFieldValueEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectNextItemFieldValue

class ProjectNextItemFieldValueConnection(GQLObject):
   edges: list[ProjectNextItemFieldValueEdge]
   nodes: list[ProjectNextItemFieldValue]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectNextItem(GQLObject):
   id: ID ##NON NULL

class ProjectNextItemEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectNextItem

class ProjectNextItemConnection(GQLObject):
   edges: list[ProjectNextItemEdge]
   nodes: list[ProjectNextItem]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectNextOwner(GQLObject):
   id: ID ##NON NULL

class ProjectView(GQLObject):
   id: ID ##NON NULL

class ProjectViewEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectView

class ProjectViewConnection(GQLObject):
   edges: list[ProjectViewEdge]
   nodes: list[ProjectView]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectNext(GQLObject):
   closedAt: DateTime
   id: ID ##NON NULL
   viewerCanUpdate: bool ##NON NULL

class DraftIssue(GQLObject):
   assignees: UserConnectionField ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   createdAt: DateTime ##NON NULL
   creator: Actor
   id: ID ##NON NULL
   project: ProjectNext ##NON NULL
   projectItem: ProjectNextItem ##NON NULL
   projectV2Items: ProjectV2ItemConnectionField ##NON NULL
   projectsV2: ProjectV2ConnectionField ##NON NULL
   title: str ##NON NULL
   updatedAt: DateTime ##NON NULL

class ProjectV2ItemContent(GQLObject): 
   pass

class ProjectV2ItemFieldDateValue(GQLObject):
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   date: Date
   field: ProjectV2FieldConfiguration ##NON NULL
   id: ID ##NON NULL
   item: NewType('ProjectV2Item', GQLObject) ##NON NULL ## Circular Reference for ProjectV2Item
   updatedAt: DateTime ##NON NULL

class ProjectV2ItemFieldIterationValue(GQLObject):
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   duration: int ##NON NULL
   field: ProjectV2FieldConfiguration ##NON NULL
   id: ID ##NON NULL
   item: NewType('ProjectV2Item', GQLObject) ##NON NULL ## Circular Reference for ProjectV2Item
   iterationId: str ##NON NULL
   startDate: Date ##NON NULL
   title: str ##NON NULL
   titleHTML: str ##NON NULL
   updatedAt: DateTime ##NON NULL

class ProjectV2ItemFieldLabelValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   labels: LabelConnectionField

class ProjectV2ItemFieldMilestoneValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   milestone: Milestone

class ProjectV2ItemFieldNumberValue(GQLObject):
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   field: ProjectV2FieldConfiguration ##NON NULL
   id: ID ##NON NULL
   item: NewType('ProjectV2Item', GQLObject) ##NON NULL ## Circular Reference for ProjectV2Item
   number: float
   updatedAt: DateTime ##NON NULL

class ProjectV2ItemFieldPullRequestValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   pullRequests: PullRequestConnectionField

class ProjectV2ItemFieldRepositoryValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   repository: Repository

class RequestedReviewer(GQLObject): 
   pass

class RequestedReviewerEdge(GQLObject):
   cursor: str ##NON NULL
   node: RequestedReviewer

class RequestedReviewerConnection(GQLObject):
   edges: list[RequestedReviewerEdge]
   nodes: list[RequestedReviewer]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class RequestedReviewerConnectionField(RequestedReviewerConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class ProjectV2ItemFieldReviewerValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   reviewers: RequestedReviewerConnectionField

class ProjectV2ItemFieldSingleSelectValue(GQLObject):
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   field: ProjectV2FieldConfiguration ##NON NULL
   id: ID ##NON NULL
   item: NewType('ProjectV2Item', GQLObject) ##NON NULL ## Circular Reference for ProjectV2Item
   name: str
   nameHTML: str
   optionId: str
   updatedAt: DateTime ##NON NULL

class ProjectV2ItemFieldTextValue(GQLObject):
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   field: ProjectV2FieldConfiguration ##NON NULL
   id: ID ##NON NULL
   item: NewType('ProjectV2Item', GQLObject) ##NON NULL ## Circular Reference for ProjectV2Item
   text: str
   updatedAt: DateTime ##NON NULL

class ProjectV2ItemFieldUserValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   users: UserConnectionField

class ProjectV2ItemFieldValue(GQLObject): 
   pass

class ProjectV2ItemFieldValueEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2ItemFieldValue

class ProjectV2ItemFieldValueConnection(GQLObject):
   edges: list[ProjectV2ItemFieldValueEdge]
   nodes: list[ProjectV2ItemFieldValue]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2ItemFieldValueField(ProjectV2ItemFieldValue):
   class Args(GQLArgsSet): 
      name: str ##NON NULL

   _args: Args



class ProjectV2ItemFieldValueConnectionField(ProjectV2ItemFieldValueConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ItemFieldValueOrder

   _args: Args



class ProjectV2Item(GQLObject):
   content: ProjectV2ItemContent
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   fieldValueByName: ProjectV2ItemFieldValueField
   fieldValues: ProjectV2ItemFieldValueConnectionField ##NON NULL
   id: ID ##NON NULL
   isArchived: bool ##NON NULL
   project: NewType('ProjectV2', GQLObject) ##NON NULL ## Circular Reference for ProjectV2
   type: ProjectV2ItemType ##NON NULL
   updatedAt: DateTime ##NON NULL

class ProjectV2ItemEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2Item

class ProjectV2ItemConnection(GQLObject):
   edges: list[ProjectV2ItemEdge]
   nodes: list[ProjectV2Item]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2Owner(GQLObject):
   id: ID ##NON NULL
   projectV2: ProjectV2Field ## Circular Reference for ProjectV2
   projectsV2: ProjectV2ConnectionField ##NON NULL

class ProjectV2FieldEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2Field

class ProjectV2FieldConnection(GQLObject):
   edges: list[ProjectV2FieldEdge]
   nodes: list[ProjectV2Field]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2SortBy(GQLObject):
   direction: OrderDirection ##NON NULL
   field: ProjectV2Field ##NON NULL

class ProjectV2SortByEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2SortBy

class ProjectV2SortByConnection(GQLObject):
   edges: list[ProjectV2SortByEdge]
   nodes: list[ProjectV2SortBy]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2SortByField(GQLObject):
   direction: OrderDirection ##NON NULL
   field: ProjectV2FieldConfiguration ##NON NULL

class ProjectV2SortByFieldEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2SortByField

class ProjectV2SortByFieldConnection(GQLObject):
   edges: list[ProjectV2SortByFieldEdge]
   nodes: list[ProjectV2SortByField]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2FieldConfigurationConnectionField(ProjectV2FieldConfigurationConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: Args



class ProjectV2SortByFieldConnectionField(ProjectV2SortByFieldConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class ProjectV2View(GQLObject):
   createdAt: DateTime ##NON NULL
   databaseId: int
   fields: ProjectV2FieldConfigurationConnectionField
   filter: str
   groupByFields: ProjectV2FieldConfigurationConnectionField
   id: ID ##NON NULL
   layout: ProjectV2ViewLayout ##NON NULL
   name: str ##NON NULL
   number: int ##NON NULL
   project: NewType('ProjectV2', GQLObject) ##NON NULL ## Circular Reference for ProjectV2
   sortByFields: ProjectV2SortByFieldConnectionField
   updatedAt: DateTime ##NON NULL
   verticalGroupByFields: ProjectV2FieldConfigurationConnectionField

class ProjectV2ViewEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2View

class ProjectV2ViewConnection(GQLObject):
   edges: list[ProjectV2ViewEdge]
   nodes: list[ProjectV2View]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2FieldConfigurationField(ProjectV2FieldConfiguration):
   class Args(GQLArgsSet): 
      name: str ##NON NULL

   _args: Args



class TeamConnectionField(TeamConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: TeamOrder

   _args: Args



class ProjectV2ViewField(ProjectV2View):
   class Args(GQLArgsSet): 
      number: int ##NON NULL

   _args: Args



class ProjectV2ViewConnectionField(ProjectV2ViewConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ViewOrder

   _args: Args



class ProjectV2(GQLObject):
   closed: bool ##NON NULL
   closedAt: DateTime
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   field: ProjectV2FieldConfigurationField
   fields: ProjectV2FieldConfigurationConnectionField ##NON NULL
   id: ID ##NON NULL
   items: ProjectV2ItemConnectionField ##NON NULL
   number: int ##NON NULL
   owner: ProjectV2Owner ##NON NULL
   public: bool ##NON NULL
   readme: str
   repositories: RepositoryConnectionField ##NON NULL
   resourcePath: URI ##NON NULL
   shortDescription: str
   teams: TeamConnectionField ##NON NULL
   title: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   view: ProjectV2ViewField
   viewerCanUpdate: bool ##NON NULL
   views: ProjectV2ViewConnectionField ##NON NULL

class TeamRepositoryEdge(GQLObject):
   cursor: str ##NON NULL
   node: Repository ##NON NULL
   permission: RepositoryPermission ##NON NULL

class TeamRepositoryConnection(GQLObject):
   edges: list[TeamRepositoryEdge]
   nodes: list[Repository]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class TeamDiscussionField(TeamDiscussion):
   class Args(GQLArgsSet): 
      number: int ##NON NULL

   _args: Args



class TeamDiscussionConnectionField(TeamDiscussionConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      isPinned: bool
      orderBy: TeamDiscussionOrder

   _args: Args



class OrganizationInvitationConnectionField(OrganizationInvitationConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class UserStatusConnectionField(UserStatusConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: Args



class TeamMemberConnectionField(TeamMemberConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      query: str
      membership: TeamMembershipType
      role: TeamMemberRole
      orderBy: TeamMemberOrder

   _args: Args



class TeamRepositoryConnectionField(TeamRepositoryConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: TeamRepositoryOrder

   _args: Args



class Team(GQLObject):
   ancestors: TeamConnectionField ##NON NULL
   avatarUrl: URIField
   childTeams: TeamConnectionField ##NON NULL
   combinedSlug: str ##NON NULL
   createdAt: DateTime ##NON NULL
   databaseId: int
   description: str
   discussion: TeamDiscussionField
   discussions: TeamDiscussionConnectionField ##NON NULL
   discussionsResourcePath: URI ##NON NULL
   discussionsUrl: URI ##NON NULL
   editTeamResourcePath: URI ##NON NULL
   editTeamUrl: URI ##NON NULL
   id: ID ##NON NULL
   invitations: OrganizationInvitationConnectionField
   memberStatuses: UserStatusConnectionField ##NON NULL
   members: TeamMemberConnectionField ##NON NULL
   membersResourcePath: URI ##NON NULL
   membersUrl: URI ##NON NULL
   name: str ##NON NULL
   newTeamResourcePath: URI ##NON NULL
   newTeamUrl: URI ##NON NULL
   organization: NewType('Organization', GQLObject) ##NON NULL ## Circular Reference for Organization
   parentTeam: NewType('Team', GQLObject) ## Circular Reference for Team
   privacy: TeamPrivacy ##NON NULL
   projectV2: ProjectV2Field
   projectsV2: ProjectV2ConnectionField ##NON NULL
   repositories: TeamRepositoryConnectionField ##NON NULL
   repositoriesResourcePath: URI ##NON NULL
   repositoriesUrl: URI ##NON NULL
   resourcePath: URI ##NON NULL
   slug: str ##NON NULL
   teamsResourcePath: URI ##NON NULL
   teamsUrl: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   viewerCanAdminister: bool ##NON NULL
   viewerCanSubscribe: bool ##NON NULL
   viewerSubscription: SubscriptionState

class BranchActorAllowanceActor(GQLObject): 
   pass

class BypassForcePushAllowance(GQLObject):
   actor: BranchActorAllowanceActor
   branchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   id: ID ##NON NULL

class BypassForcePushAllowanceEdge(GQLObject):
   cursor: str ##NON NULL
   node: BypassForcePushAllowance

class BypassForcePushAllowanceConnection(GQLObject):
   edges: list[BypassForcePushAllowanceEdge]
   nodes: list[BypassForcePushAllowance]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class BypassPullRequestAllowance(GQLObject):
   actor: BranchActorAllowanceActor
   branchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   id: ID ##NON NULL

class BypassPullRequestAllowanceEdge(GQLObject):
   cursor: str ##NON NULL
   node: BypassPullRequestAllowance

class BypassPullRequestAllowanceConnection(GQLObject):
   edges: list[BypassPullRequestAllowanceEdge]
   nodes: list[BypassPullRequestAllowance]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PushAllowanceActor(GQLObject): 
   pass

class PushAllowance(GQLObject):
   actor: PushAllowanceActor
   branchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   id: ID ##NON NULL

class PushAllowanceEdge(GQLObject):
   cursor: str ##NON NULL
   node: PushAllowance

class PushAllowanceConnection(GQLObject):
   edges: list[PushAllowanceEdge]
   nodes: list[PushAllowance]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class RequiredStatusCheckDescription(GQLObject):
   app: NewType('App', GQLObject) ## Circular Reference for App
   context: str ##NON NULL

class ReviewDismissalAllowanceActor(GQLObject): 
   pass

class ReviewDismissalAllowance(GQLObject):
   actor: ReviewDismissalAllowanceActor
   branchProtectionRule: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule
   id: ID ##NON NULL

class ReviewDismissalAllowanceEdge(GQLObject):
   cursor: str ##NON NULL
   node: ReviewDismissalAllowance

class ReviewDismissalAllowanceConnection(GQLObject):
   edges: list[ReviewDismissalAllowanceEdge]
   nodes: list[ReviewDismissalAllowance]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class BranchProtectionRuleConflictConnectionField(BranchProtectionRuleConflictConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class BypassForcePushAllowanceConnectionField(BypassForcePushAllowanceConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class BypassPullRequestAllowanceConnectionField(BypassPullRequestAllowanceConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PushAllowanceConnectionField(PushAllowanceConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class ReviewDismissalAllowanceConnectionField(ReviewDismissalAllowanceConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class BranchProtectionRule(GQLObject):
   allowsDeletions: bool ##NON NULL
   allowsForcePushes: bool ##NON NULL
   blocksCreations: bool ##NON NULL
   branchProtectionRuleConflicts: BranchProtectionRuleConflictConnectionField ##NON NULL
   bypassForcePushAllowances: BypassForcePushAllowanceConnectionField ##NON NULL
   bypassPullRequestAllowances: BypassPullRequestAllowanceConnectionField ##NON NULL
   creator: Actor
   databaseId: int
   dismissesStaleReviews: bool ##NON NULL
   id: ID ##NON NULL
   isAdminEnforced: bool ##NON NULL
   lockAllowsFetchAndMerge: bool ##NON NULL
   lockBranch: bool ##NON NULL
   matchingRefs: RefConnectionField ##NON NULL
   pattern: str ##NON NULL
   pushAllowances: PushAllowanceConnectionField ##NON NULL
   repository: Repository
   requireLastPushApproval: bool ##NON NULL
   requiredApprovingReviewCount: int
   requiredStatusCheckContexts: list[str]
   requiredStatusChecks: list[RequiredStatusCheckDescription]
   requiresApprovingReviews: bool ##NON NULL
   requiresCodeOwnerReviews: bool ##NON NULL
   requiresCommitSignatures: bool ##NON NULL
   requiresConversationResolution: bool ##NON NULL
   requiresLinearHistory: bool ##NON NULL
   requiresStatusChecks: bool ##NON NULL
   requiresStrictStatusChecks: bool ##NON NULL
   restrictsPushes: bool ##NON NULL
   restrictsReviewDismissals: bool ##NON NULL
   reviewDismissalAllowances: ReviewDismissalAllowanceConnectionField ##NON NULL

class CommitEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Commit', GQLObject) ## Circular Reference for Commit

class ComparisonCommitConnection(GQLObject):
   authorCount: int ##NON NULL
   edges: list[CommitEdge]
   nodes: list[NewType('Commit', GQLObject)] ## Circular Reference for Commit
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ComparisonCommitConnectionField(ComparisonCommitConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class Comparison(GQLObject):
   aheadBy: int ##NON NULL
   baseTarget: GitObject ##NON NULL
   behindBy: int ##NON NULL
   commits: ComparisonCommitConnectionField ##NON NULL
   headTarget: GitObject ##NON NULL
   id: ID ##NON NULL
   status: ComparisonStatus ##NON NULL

class ComparisonField(Comparison):
   class Args(GQLArgsSet): 
      headRef: str ##NON NULL

   _args: Args



class Ref(GQLObject):
   associatedPullRequests: PullRequestConnectionField ##NON NULL ## Circular Reference for PullRequestConnection
   branchProtectionRule: BranchProtectionRule
   compare: ComparisonField
   id: ID ##NON NULL
   name: str ##NON NULL
   prefix: str ##NON NULL
   refUpdateRule: RefUpdateRule
   repository: Repository ##NON NULL
   target: GitObject

class PullRequestCommit(GQLObject):
   commit: NewType('Commit', GQLObject) ##NON NULL ## Circular Reference for Commit
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class PullRequestCommitEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequestCommit

class PullRequestCommitConnection(GQLObject):
   edges: list[PullRequestCommitEdge]
   nodes: list[PullRequestCommit]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PullRequestChangedFileEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequestChangedFile

class PullRequestChangedFileConnection(GQLObject):
   edges: list[PullRequestChangedFileEdge]
   nodes: list[PullRequestChangedFile]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PullRequestReviewComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   diffHunk: str ##NON NULL
   draftedAt: DateTime ##NON NULL
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   isMinimized: bool ##NON NULL
   lastEditedAt: DateTime
   minimizedReason: str
   originalCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   originalPosition: int ##NON NULL
   outdated: bool ##NON NULL
   path: str ##NON NULL
   position: int
   publishedAt: DateTime
   pullRequest: PullRequest ##NON NULL
   pullRequestReview: NewType('PullRequestReview', GQLObject) ## Circular Reference for PullRequestReview
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   replyTo: NewType('PullRequestReviewComment', GQLObject) ## Circular Reference for PullRequestReviewComment
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   state: PullRequestReviewCommentState ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanDelete: bool ##NON NULL
   viewerCanMinimize: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL

class PullRequestReviewCommentEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequestReviewComment

class PullRequestReviewCommentConnection(GQLObject):
   edges: list[PullRequestReviewCommentEdge]
   nodes: list[PullRequestReviewComment]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PullRequestReviewCommentConnectionField(PullRequestReviewCommentConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PullRequestReview(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   authorCanPushToRepository: bool ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   comments: PullRequestReviewCommentConnectionField ##NON NULL
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   lastEditedAt: DateTime
   onBehalfOf: TeamConnectionField ##NON NULL
   publishedAt: DateTime
   pullRequest: PullRequest ##NON NULL
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   state: PullRequestReviewState ##NON NULL
   submittedAt: DateTime
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanDelete: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL

class PullRequestReviewEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequestReview

class PullRequestReviewConnection(GQLObject):
   edges: list[PullRequestReviewEdge]
   nodes: list[PullRequestReview]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ReviewRequest(GQLObject):
   asCodeOwner: bool ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL
   requestedReviewer: RequestedReviewer

class ReviewRequestEdge(GQLObject):
   cursor: str ##NON NULL
   node: ReviewRequest

class ReviewRequestConnection(GQLObject):
   edges: list[ReviewRequestEdge]
   nodes: list[ReviewRequest]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PullRequestReviewThread(GQLObject):
   comments: PullRequestReviewCommentConnectionField ##NON NULL
   diffSide: DiffSide ##NON NULL
   id: ID ##NON NULL
   isCollapsed: bool ##NON NULL
   isOutdated: bool ##NON NULL
   isResolved: bool ##NON NULL
   line: int
   originalLine: int
   originalStartLine: int
   path: str ##NON NULL
   pullRequest: PullRequest ##NON NULL
   repository: Repository ##NON NULL
   resolvedBy: NewType('User', GQLObject) ## Circular Reference for User
   startDiffSide: DiffSide
   startLine: int
   viewerCanReply: bool ##NON NULL
   viewerCanResolve: bool ##NON NULL
   viewerCanUnresolve: bool ##NON NULL

class PullRequestReviewThreadEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequestReviewThread

class PullRequestReviewThreadConnection(GQLObject):
   edges: list[PullRequestReviewThreadEdge]
   nodes: list[PullRequestReviewThread]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SuggestedReviewer(GQLObject):
   isAuthor: bool ##NON NULL
   isCommenter: bool ##NON NULL
   reviewer: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class BaseRefDeletedEvent(GQLObject):
   actor: Actor
   baseRefName: str
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest

class BaseRefForcePushedEvent(GQLObject):
   actor: Actor
   afterCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   beforeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL
   ref: Ref

class CommitCommentThread(GQLObject):
   comments: CommitCommentConnectionField ##NON NULL
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   id: ID ##NON NULL
   path: str
   position: int
   repository: Repository ##NON NULL

class DeployedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   databaseId: int
   deployment: Deployment ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL
   ref: Ref

class DeploymentEnvironmentChangedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   deploymentStatus: DeploymentStatus ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL

class HeadRefDeletedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   headRef: Ref
   headRefName: str ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL

class HeadRefForcePushedEvent(GQLObject):
   actor: Actor
   afterCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   beforeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL
   ref: Ref

class HeadRefRestoredEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL

class MergedEvent(GQLObject):
   actor: Actor
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   mergeRef: Ref
   mergeRefName: str ##NON NULL
   pullRequest: PullRequest ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class ReviewDismissedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   databaseId: int
   dismissalMessage: str
   dismissalMessageHTML: str
   id: ID ##NON NULL
   previousReviewState: PullRequestReviewState ##NON NULL
   pullRequest: PullRequest ##NON NULL
   pullRequestCommit: PullRequestCommit
   resourcePath: URI ##NON NULL
   review: PullRequestReview
   url: URI ##NON NULL

class ReviewRequestRemovedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL
   requestedReviewer: RequestedReviewer

class ReviewRequestedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL
   requestedReviewer: RequestedReviewer

class PullRequestTimelineItem(GQLObject): 
   pass

class PullRequestTimelineItemEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequestTimelineItem

class PullRequestTimelineConnection(GQLObject):
   edges: list[PullRequestTimelineItemEdge]
   nodes: list[PullRequestTimelineItem]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class AutoMergeDisabledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   disabler: NewType('User', GQLObject) ## Circular Reference for User
   id: ID ##NON NULL
   pullRequest: PullRequest
   reason: str
   reasonCode: str

class AutoMergeEnabledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   enabler: NewType('User', GQLObject) ## Circular Reference for User
   id: ID ##NON NULL
   pullRequest: PullRequest

class AutoRebaseEnabledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   enabler: NewType('User', GQLObject) ## Circular Reference for User
   id: ID ##NON NULL
   pullRequest: PullRequest

class AutoSquashEnabledEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   enabler: NewType('User', GQLObject) ## Circular Reference for User
   id: ID ##NON NULL
   pullRequest: PullRequest

class AutomaticBaseChangeFailedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   newBase: str ##NON NULL
   oldBase: str ##NON NULL
   pullRequest: PullRequest ##NON NULL

class AutomaticBaseChangeSucceededEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   newBase: str ##NON NULL
   oldBase: str ##NON NULL
   pullRequest: PullRequest ##NON NULL

class BaseRefChangedEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   currentRefName: str ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   previousRefName: str ##NON NULL
   pullRequest: PullRequest ##NON NULL

class ConvertToDraftEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class PullRequestCommitCommentThread(GQLObject):
   comments: CommitCommentConnectionField ##NON NULL
   commit: NewType('Commit', GQLObject) ##NON NULL ## Circular Reference for Commit
   id: ID ##NON NULL
   path: str
   position: int
   pullRequest: PullRequest ##NON NULL
   repository: Repository ##NON NULL

class PullRequestRevisionMarker(GQLObject):
   createdAt: DateTime ##NON NULL
   lastSeenCommit: NewType('Commit', GQLObject) ##NON NULL ## Circular Reference for Commit
   pullRequest: PullRequest ##NON NULL

class ReadyForReviewEvent(GQLObject):
   actor: Actor
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   pullRequest: PullRequest ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class PullRequestTimelineItems(GQLObject): 
   pass

class PullRequestTimelineItemsEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequestTimelineItems

class PullRequestTimelineItemsConnection(GQLObject):
   edges: list[PullRequestTimelineItemsEdge]
   filteredCount: int ##NON NULL
   nodes: list[PullRequestTimelineItems]
   pageCount: int ##NON NULL
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   updatedAt: DateTime ##NON NULL

class PullRequestCommitConnectionField(PullRequestCommitConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PullRequestChangedFileConnectionField(PullRequestChangedFileConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PullRequestReviewConnectionField(PullRequestReviewConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      writersOnly: bool

   _args: Args



class ReviewRequestConnectionField(ReviewRequestConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PullRequestReviewThreadConnectionField(PullRequestReviewThreadConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PullRequestTimelineItemsConnectionField(PullRequestTimelineItemsConnection):
   class Args(GQLArgsSet): 
      since: DateTime
      skip: int
      itemTypes: list[PullRequestTimelineItemsItemType] ##NON NULL
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PullRequest(GQLObject):
   activeLockReason: LockReason
   additions: int ##NON NULL
   assignees: UserConnectionField ##NON NULL
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   autoMergeRequest: AutoMergeRequest
   baseRef: Ref
   baseRefName: str ##NON NULL
   baseRefOid: GitObjectID ##NON NULL
   baseRepository: Repository
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   changedFiles: int ##NON NULL
   checksResourcePath: URI ##NON NULL
   checksUrl: URI ##NON NULL
   closed: bool ##NON NULL
   closedAt: DateTime
   closingIssuesReferences: IssueConnectionField
   comments: IssueCommentConnectionField ##NON NULL
   commits: PullRequestCommitConnectionField ##NON NULL
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   deletions: int ##NON NULL
   editor: Actor
   files: PullRequestChangedFileConnectionField
   headRef: Ref
   headRefName: str ##NON NULL
   headRefOid: GitObjectID ##NON NULL
   headRepository: Repository
   headRepositoryOwner: RepositoryOwner
   hovercard: HovercardField ##NON NULL
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   isCrossRepository: bool ##NON NULL
   isDraft: bool ##NON NULL
   isReadByViewer: bool
   labels: LabelConnectionField
   lastEditedAt: DateTime
   latestOpinionatedReviews: PullRequestReviewConnectionField
   latestReviews: PullRequestReviewConnectionField
   locked: bool ##NON NULL
   maintainerCanModify: bool ##NON NULL
   mergeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   mergeable: MergeableState ##NON NULL
   merged: bool ##NON NULL
   mergedAt: DateTime
   mergedBy: Actor
   milestone: Milestone
   number: int ##NON NULL
   participants: UserConnectionField ##NON NULL
   permalink: URI ##NON NULL
   potentialMergeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   projectCards: ProjectCardConnectionField ##NON NULL
   projectItems: ProjectV2ItemConnectionField ##NON NULL
   projectV2: ProjectV2Field
   projectsV2: ProjectV2ConnectionField ##NON NULL
   publishedAt: DateTime
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   revertResourcePath: URI ##NON NULL
   revertUrl: URI ##NON NULL
   reviewDecision: PullRequestReviewDecision
   reviewRequests: ReviewRequestConnectionField
   reviewThreads: PullRequestReviewThreadConnectionField ##NON NULL
   reviews: PullRequestReviewConnectionField
   state: PullRequestState ##NON NULL
   suggestedReviewers: SuggestedReviewer ##NON NULL
   timelineItems: PullRequestTimelineItemsConnectionField ##NON NULL
   title: str ##NON NULL
   titleHTML: HTML ##NON NULL
   totalCommentsCount: int
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanApplySuggestion: bool ##NON NULL
   viewerCanDeleteHeadRef: bool ##NON NULL
   viewerCanDisableAutoMerge: bool ##NON NULL
   viewerCanEditFiles: bool ##NON NULL
   viewerCanEnableAutoMerge: bool ##NON NULL
   viewerCanMergeAsAdmin: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanSubscribe: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL
   viewerLatestReview: PullRequestReview
   viewerLatestReviewRequest: ReviewRequest
   viewerMergeBodyText: viewerMergeBodyTextField ##NON NULL
   viewerMergeHeadlineText: viewerMergeHeadlineTextField ##NON NULL
   viewerSubscription: SubscriptionState

class PullRequestEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequest

class PullRequestConnection(GQLObject):
   edges: list[PullRequestEdge]
   nodes: list[PullRequest]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class GitActor(GQLObject):
   avatarUrl: URIField ##NON NULL
   date: GitTimestamp
   email: str
   name: str
   user: NewType('User', GQLObject) ## Circular Reference for User

class GitActorEdge(GQLObject):
   cursor: str ##NON NULL
   node: GitActor

class GitActorConnection(GQLObject):
   edges: list[GitActorEdge]
   nodes: list[GitActor]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class BlameRange(GQLObject):
   age: int ##NON NULL
   commit: NewType('Commit', GQLObject) ##NON NULL ## Circular Reference for Commit
   endingLine: int ##NON NULL
   startingLine: int ##NON NULL

class Blame(GQLObject):
   ranges: BlameRange ##NON NULL

class CheckSuiteEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('CheckSuite', GQLObject) ## Circular Reference for CheckSuite

class CheckSuiteConnection(GQLObject):
   edges: list[CheckSuiteEdge]
   nodes: list[NewType('CheckSuite', GQLObject)] ## Circular Reference for CheckSuite
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class TreeEntry(GQLObject):
   extension: str
   isGenerated: bool ##NON NULL
   language: Language
   lineCount: int
   mode: int ##NON NULL
   name: str ##NON NULL
   nameRaw: Base64String ##NON NULL
   object: GitObject
   oid: GitObjectID ##NON NULL
   path: str
   pathRaw: Base64String
   repository: Repository ##NON NULL
   size: int ##NON NULL
   submodule: Submodule
   type: str ##NON NULL

class CommitHistoryConnection(GQLObject):
   edges: list[CommitEdge]
   nodes: list[NewType('Commit', GQLObject)] ## Circular Reference for Commit
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CommitConnection(GQLObject):
   edges: list[CommitEdge]
   nodes: list[NewType('Commit', GQLObject)] ## Circular Reference for Commit
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class GitSignature(GQLObject):
   email: str ##NON NULL
   isValid: bool ##NON NULL
   payload: str ##NON NULL
   signature: str ##NON NULL
   signer: NewType('User', GQLObject) ## Circular Reference for User
   state: GitSignatureState ##NON NULL
   wasSignedByGitHub: bool ##NON NULL

class CheckAnnotationSpan(GQLObject):
   end: CheckAnnotationPosition ##NON NULL
   start: CheckAnnotationPosition ##NON NULL

class CheckAnnotation(GQLObject):
   annotationLevel: CheckAnnotationLevel
   blobUrl: URI ##NON NULL
   databaseId: int
   location: CheckAnnotationSpan ##NON NULL
   message: str ##NON NULL
   path: str ##NON NULL
   rawDetails: str
   title: str

class CheckAnnotationEdge(GQLObject):
   cursor: str ##NON NULL
   node: CheckAnnotation

class CheckAnnotationConnection(GQLObject):
   edges: list[CheckAnnotationEdge]
   nodes: list[CheckAnnotation]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeploymentRequest(GQLObject):
   currentUserCanApprove: bool ##NON NULL
   environment: Environment ##NON NULL
   reviewers: DeploymentReviewerConnectionField ##NON NULL
   waitTimer: int ##NON NULL
   waitTimerStartedAt: DateTime

class CheckStepEdge(GQLObject):
   cursor: str ##NON NULL
   node: CheckStep

class CheckStepConnection(GQLObject):
   edges: list[CheckStepEdge]
   nodes: list[CheckStep]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CheckAnnotationConnectionField(CheckAnnotationConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class CheckStepConnectionField(CheckStepConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      number: int

   _args: Args



class CheckRun(GQLObject):
   annotations: CheckAnnotationConnectionField
   checkSuite: NewType('CheckSuite', GQLObject) ##NON NULL ## Circular Reference for CheckSuite
   completedAt: DateTime
   conclusion: CheckConclusionState
   databaseId: int
   deployment: Deployment
   detailsUrl: URI
   externalId: str
   id: ID ##NON NULL
   isRequired: isRequiredField ##NON NULL
   name: str ##NON NULL
   pendingDeploymentRequest: DeploymentRequest
   permalink: URI ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   startedAt: DateTime
   status: CheckStatusState ##NON NULL
   steps: CheckStepConnectionField
   summary: str
   text: str
   title: str
   url: URI ##NON NULL

class StatusContext(GQLObject):
   avatarUrl: URIField
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   context: str ##NON NULL
   createdAt: DateTime ##NON NULL
   creator: Actor
   description: str
   id: ID ##NON NULL
   isRequired: isRequiredField ##NON NULL
   state: StatusState ##NON NULL
   targetUrl: URI

class StatusCheckRollupContext(GQLObject): 
   pass

class StatusCheckRollupContextEdge(GQLObject):
   cursor: str ##NON NULL
   node: StatusCheckRollupContext

class StatusCheckRollupContextConnection(GQLObject):
   checkRunCount: int ##NON NULL
   checkRunCountsByState: list[CheckRunStateCount]
   edges: list[StatusCheckRollupContextEdge]
   nodes: list[StatusCheckRollupContext]
   pageInfo: PageInfo ##NON NULL
   statusContextCount: int ##NON NULL
   statusContextCountsByState: list[StatusContextStateCount]
   totalCount: int ##NON NULL

class StatusCheckRollupContextConnectionField(StatusCheckRollupContextConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class StatusContextField(StatusContext):
   class Args(GQLArgsSet): 
      name: str ##NON NULL

   _args: Args



class Status(GQLObject):
   combinedContexts: StatusCheckRollupContextConnectionField ##NON NULL
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   context: StatusContextField
   contexts: StatusContext ##NON NULL
   id: ID ##NON NULL
   state: StatusState ##NON NULL

class StatusCheckRollup(GQLObject):
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   contexts: StatusCheckRollupContextConnectionField ##NON NULL
   id: ID ##NON NULL
   state: StatusState ##NON NULL

class Tree(GQLObject):
   abbreviatedOid: str ##NON NULL
   commitResourcePath: URI ##NON NULL
   commitUrl: URI ##NON NULL
   entries: list[TreeEntry]
   id: ID ##NON NULL
   oid: GitObjectID ##NON NULL
   repository: Repository ##NON NULL

class GitActorConnectionField(GitActorConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class BlameField(Blame):
   class Args(GQLArgsSet): 
      path: str ##NON NULL

   _args: Args



class CheckSuiteConnectionField(CheckSuiteConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      filterBy: CheckSuiteFilter

   _args: Args



class TreeEntryField(TreeEntry):
   class Args(GQLArgsSet): 
      path: str ##NON NULL

   _args: Args



class CommitHistoryConnectionField(CommitHistoryConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      path: str
      author: CommitAuthor
      since: GitTimestamp
      until: GitTimestamp

   _args: Args



class CommitConnectionField(CommitConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class Commit(GQLObject):
   abbreviatedOid: str ##NON NULL
   additions: int ##NON NULL
   associatedPullRequests: PullRequestConnectionField
   author: GitActor
   authoredByCommitter: bool ##NON NULL
   authoredDate: DateTime ##NON NULL
   authors: GitActorConnectionField ##NON NULL
   blame: BlameField ##NON NULL
   changedFilesIfAvailable: int
   checkSuites: CheckSuiteConnectionField
   comments: CommitCommentConnectionField ##NON NULL
   commitResourcePath: URI ##NON NULL
   commitUrl: URI ##NON NULL
   committedDate: DateTime ##NON NULL
   committedViaWeb: bool ##NON NULL
   committer: GitActor
   deletions: int ##NON NULL
   deployments: DeploymentConnectionField
   file: TreeEntryField
   history: CommitHistoryConnectionField ##NON NULL
   id: ID ##NON NULL
   message: str ##NON NULL
   messageBody: str ##NON NULL
   messageBodyHTML: HTML ##NON NULL
   messageHeadline: str ##NON NULL
   messageHeadlineHTML: HTML ##NON NULL
   oid: GitObjectID ##NON NULL
   onBehalfOf: NewType('Organization', GQLObject) ## Circular Reference for Organization
   parents: CommitConnectionField ##NON NULL
   pushedDate: DateTime
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   signature: GitSignature
   status: Status
   statusCheckRollup: StatusCheckRollup
   submodules: SubmoduleConnectionField ##NON NULL
   tarballUrl: URI ##NON NULL
   tree: Tree ##NON NULL
   treeResourcePath: URI ##NON NULL
   treeUrl: URI ##NON NULL
   url: URI ##NON NULL
   viewerCanSubscribe: bool ##NON NULL
   viewerSubscription: SubscriptionState
   zipballUrl: URI ##NON NULL

class CommitComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   commit: Commit
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   isMinimized: bool ##NON NULL
   lastEditedAt: DateTime
   minimizedReason: str
   path: str
   position: int
   publishedAt: DateTime
   reactionGroups: list[ReactionGroup]
   reactions: ReactionConnectionField ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanDelete: bool ##NON NULL
   viewerCanMinimize: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL

class CommitCommentEdge(GQLObject):
   cursor: str ##NON NULL
   node: CommitComment

class CommitCommentConnection(GQLObject):
   edges: list[CommitCommentEdge]
   nodes: list[CommitComment]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CreatedCommitContribution(GQLObject):
   commitCount: int ##NON NULL
   isRestricted: bool ##NON NULL
   occurredAt: DateTime ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class CreatedCommitContributionEdge(GQLObject):
   cursor: str ##NON NULL
   node: CreatedCommitContribution

class CreatedCommitContributionConnection(GQLObject):
   edges: list[CreatedCommitContributionEdge]
   nodes: list[CreatedCommitContribution]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CreatedCommitContributionConnectionField(CreatedCommitContributionConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: CommitContributionOrder

   _args: Args



class CommitContributionsByRepository(GQLObject):
   contributions: CreatedCommitContributionConnectionField ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class ContributionCalendarWeek(GQLObject):
   contributionDays: ContributionCalendarDay ##NON NULL
   firstDay: Date ##NON NULL

class ContributionCalendar(GQLObject):
   colors: str ##NON NULL
   isHalloween: bool ##NON NULL
   months: ContributionCalendarMonth ##NON NULL
   totalContributions: int ##NON NULL
   weeks: ContributionCalendarWeek ##NON NULL

class CreatedIssueContribution(GQLObject):
   isRestricted: bool ##NON NULL
   issue: Issue ##NON NULL
   occurredAt: DateTime ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class RestrictedContribution(GQLObject):
   isRestricted: bool ##NON NULL
   occurredAt: DateTime ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class CreatedIssueOrRestrictedContribution(GQLObject): 
   pass

class CreatedPullRequestContribution(GQLObject):
   isRestricted: bool ##NON NULL
   occurredAt: DateTime ##NON NULL
   pullRequest: PullRequest ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class CreatedPullRequestOrRestrictedContribution(GQLObject): 
   pass

class CreatedRepositoryContribution(GQLObject):
   isRestricted: bool ##NON NULL
   occurredAt: DateTime ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class CreatedRepositoryOrRestrictedContribution(GQLObject): 
   pass

class CreatedIssueContributionEdge(GQLObject):
   cursor: str ##NON NULL
   node: CreatedIssueContribution

class CreatedIssueContributionConnection(GQLObject):
   edges: list[CreatedIssueContributionEdge]
   nodes: list[CreatedIssueContribution]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CreatedIssueContributionConnectionField(CreatedIssueContributionConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: Args



class IssueContributionsByRepository(GQLObject):
   contributions: CreatedIssueContributionConnectionField ##NON NULL
   repository: Repository ##NON NULL

class JoinedGitHubContribution(GQLObject):
   isRestricted: bool ##NON NULL
   occurredAt: DateTime ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class CreatedPullRequestContributionEdge(GQLObject):
   cursor: str ##NON NULL
   node: CreatedPullRequestContribution

class CreatedPullRequestContributionConnection(GQLObject):
   edges: list[CreatedPullRequestContributionEdge]
   nodes: list[CreatedPullRequestContribution]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CreatedPullRequestContributionConnectionField(CreatedPullRequestContributionConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: Args



class PullRequestContributionsByRepository(GQLObject):
   contributions: CreatedPullRequestContributionConnectionField ##NON NULL
   repository: Repository ##NON NULL

class CreatedPullRequestReviewContribution(GQLObject):
   isRestricted: bool ##NON NULL
   occurredAt: DateTime ##NON NULL
   pullRequest: PullRequest ##NON NULL
   pullRequestReview: PullRequestReview ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class CreatedPullRequestReviewContributionEdge(GQLObject):
   cursor: str ##NON NULL
   node: CreatedPullRequestReviewContribution

class CreatedPullRequestReviewContributionConnection(GQLObject):
   edges: list[CreatedPullRequestReviewContributionEdge]
   nodes: list[CreatedPullRequestReviewContribution]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CreatedPullRequestReviewContributionConnectionField(CreatedPullRequestReviewContributionConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: Args



class PullRequestReviewContributionsByRepository(GQLObject):
   contributions: CreatedPullRequestReviewContributionConnectionField ##NON NULL
   repository: Repository ##NON NULL

class CreatedRepositoryContributionEdge(GQLObject):
   cursor: str ##NON NULL
   node: CreatedRepositoryContribution

class CreatedRepositoryContributionConnection(GQLObject):
   edges: list[CreatedRepositoryContributionEdge]
   nodes: list[CreatedRepositoryContribution]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CommitContributionsByRepositoryField(CommitContributionsByRepository):
   class Args(GQLArgsSet): 
      maxRepositories: int

   _args: Args



class IssueContributionsByRepositoryField(IssueContributionsByRepository):
   class Args(GQLArgsSet): 
      maxRepositories: int
      excludeFirst: bool
      excludePopular: bool

   _args: Args



class PullRequestContributionsByRepositoryField(PullRequestContributionsByRepository):
   class Args(GQLArgsSet): 
      maxRepositories: int
      excludeFirst: bool
      excludePopular: bool

   _args: Args



class PullRequestReviewContributionsByRepositoryField(PullRequestReviewContributionsByRepository):
   class Args(GQLArgsSet): 
      maxRepositories: int

   _args: Args



class CreatedRepositoryContributionConnectionField(CreatedRepositoryContributionConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      orderBy: ContributionOrder

   _args: Args



class ContributionsCollection(GQLObject):
   commitContributionsByRepository: CommitContributionsByRepositoryField ##NON NULL
   contributionCalendar: ContributionCalendar ##NON NULL
   contributionYears: int ##NON NULL
   doesEndInCurrentMonth: bool ##NON NULL
   earliestRestrictedContributionDate: Date
   endedAt: DateTime ##NON NULL
   firstIssueContribution: CreatedIssueOrRestrictedContribution
   firstPullRequestContribution: CreatedPullRequestOrRestrictedContribution
   firstRepositoryContribution: CreatedRepositoryOrRestrictedContribution
   hasActivityInThePast: bool ##NON NULL
   hasAnyContributions: bool ##NON NULL
   hasAnyRestrictedContributions: bool ##NON NULL
   isSingleDay: bool ##NON NULL
   issueContributions: CreatedIssueContributionConnectionField ##NON NULL
   issueContributionsByRepository: IssueContributionsByRepositoryField ##NON NULL
   joinedGitHubContribution: JoinedGitHubContribution
   latestRestrictedContributionDate: Date
   mostRecentCollectionWithActivity: NewType('ContributionsCollection', GQLObject) ## Circular Reference for ContributionsCollection
   mostRecentCollectionWithoutActivity: NewType('ContributionsCollection', GQLObject) ## Circular Reference for ContributionsCollection
   popularIssueContribution: CreatedIssueContribution
   popularPullRequestContribution: CreatedPullRequestContribution
   pullRequestContributions: CreatedPullRequestContributionConnectionField ##NON NULL
   pullRequestContributionsByRepository: PullRequestContributionsByRepositoryField ##NON NULL
   pullRequestReviewContributions: CreatedPullRequestReviewContributionConnectionField ##NON NULL
   pullRequestReviewContributionsByRepository: PullRequestReviewContributionsByRepositoryField ##NON NULL
   repositoryContributions: CreatedRepositoryContributionConnectionField ##NON NULL
   restrictedContributionsCount: int ##NON NULL
   startedAt: DateTime ##NON NULL
   totalCommitContributions: int ##NON NULL
   totalIssueContributions: totalIssueContributionsField ##NON NULL
   totalPullRequestContributions: totalPullRequestContributionsField ##NON NULL
   totalPullRequestReviewContributions: int ##NON NULL
   totalRepositoriesWithContributedCommits: int ##NON NULL
   totalRepositoriesWithContributedIssues: totalRepositoriesWithContributedIssuesField ##NON NULL
   totalRepositoriesWithContributedPullRequestReviews: int ##NON NULL
   totalRepositoriesWithContributedPullRequests: totalRepositoriesWithContributedPullRequestsField ##NON NULL
   totalRepositoryContributions: totalRepositoryContributionsField ##NON NULL
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class FollowerConnection(GQLObject):
   edges: list[UserEdge]
   nodes: list[NewType('User', GQLObject)] ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class FollowingConnection(GQLObject):
   edges: list[UserEdge]
   nodes: list[NewType('User', GQLObject)] ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class GistComment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   editor: Actor
   gist: NewType('Gist', GQLObject) ##NON NULL ## Circular Reference for Gist
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   isMinimized: bool ##NON NULL
   lastEditedAt: DateTime
   minimizedReason: str
   publishedAt: DateTime
   updatedAt: DateTime ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerCanDelete: bool ##NON NULL
   viewerCanMinimize: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL

class GistCommentEdge(GQLObject):
   cursor: str ##NON NULL
   node: GistComment

class GistCommentConnection(GQLObject):
   edges: list[GistCommentEdge]
   nodes: list[GistComment]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class GistFile(GQLObject):
   encodedName: str
   encoding: str
   extension: str
   isImage: bool ##NON NULL
   isTruncated: bool ##NON NULL
   language: Language
   name: str
   size: int
   text: textField

class GistEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Gist', GQLObject) ## Circular Reference for Gist

class GistConnection(GQLObject):
   edges: list[GistEdge]
   nodes: list[NewType('Gist', GQLObject)] ## Circular Reference for Gist
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class GistCommentConnectionField(GistCommentConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class GistFileField(GistFile):
   class Args(GQLArgsSet): 
      limit: int
      oid: GitObjectID

   _args: Args



class GistConnectionField(GistConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: GistOrder

   _args: Args



class Gist(GQLObject):
   comments: GistCommentConnectionField ##NON NULL
   createdAt: DateTime ##NON NULL
   description: str
   files: list[GistFileField]
   forks: GistConnectionField ##NON NULL
   id: ID ##NON NULL
   isFork: bool ##NON NULL
   isPublic: bool ##NON NULL
   name: str ##NON NULL
   owner: RepositoryOwner
   pushedAt: DateTime
   resourcePath: URI ##NON NULL
   stargazerCount: int ##NON NULL
   stargazers: StargazerConnectionField ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   viewerHasStarred: bool ##NON NULL

class PinnableItem(GQLObject): 
   pass

class PinnableItemEdge(GQLObject):
   cursor: str ##NON NULL
   node: PinnableItem

class PinnableItemConnection(GQLObject):
   edges: list[PinnableItemEdge]
   nodes: list[PinnableItem]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PinnableItemConnectionField(PinnableItemConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class ProfileItemShowcase(GQLObject):
   hasPinnedItems: bool ##NON NULL
   items: PinnableItemConnectionField ##NON NULL

class OrganizationEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Organization', GQLObject) ## Circular Reference for Organization

class OrganizationConnection(GQLObject):
   edges: list[OrganizationEdge]
   nodes: list[NewType('Organization', GQLObject)] ## Circular Reference for Organization
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PublicKeyEdge(GQLObject):
   cursor: str ##NON NULL
   node: PublicKey

class PublicKeyConnection(GQLObject):
   edges: list[PublicKeyEdge]
   nodes: list[PublicKey]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SavedReply(GQLObject):
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   title: str ##NON NULL
   user: Actor

class SavedReplyEdge(GQLObject):
   cursor: str ##NON NULL
   node: SavedReply

class SavedReplyConnection(GQLObject):
   edges: list[SavedReplyEdge]
   nodes: list[SavedReply]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class Sponsor(GQLObject): 
   pass

class SponsorEdge(GQLObject):
   cursor: str ##NON NULL
   node: Sponsor

class SponsorConnection(GQLObject):
   edges: list[SponsorEdge]
   nodes: list[Sponsor]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SponsorsListingFeatureableItem(GQLObject): 
   pass

class SponsorsListingFeaturedItem(GQLObject):
   createdAt: DateTime ##NON NULL
   description: str
   featureable: SponsorsListingFeatureableItem ##NON NULL
   id: ID ##NON NULL
   position: int ##NON NULL
   sponsorsListing: NewType('SponsorsListing', GQLObject) ##NON NULL ## Circular Reference for SponsorsListing
   updatedAt: DateTime ##NON NULL

class SponsorsTierEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('SponsorsTier', GQLObject) ## Circular Reference for SponsorsTier

class SponsorsTierConnection(GQLObject):
   edges: list[SponsorsTierEdge]
   nodes: list[NewType('SponsorsTier', GQLObject)] ## Circular Reference for SponsorsTier
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SponsorsListingFeaturedItemField(SponsorsListingFeaturedItem):
   class Args(GQLArgsSet): 
      featureableTypes: list[SponsorsListingFeaturedItemFeatureableType] ##NON NULL

   _args: Args



class SponsorsTierConnectionField(SponsorsTierConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorsTierOrder

   _args: Args



class SponsorsListing(GQLObject):
   activeGoal: SponsorsGoal
   billingCountryOrRegion: str
   contactEmailAddress: str
   createdAt: DateTime ##NON NULL
   dashboardResourcePath: URI ##NON NULL
   dashboardUrl: URI ##NON NULL
   featuredItems: SponsorsListingFeaturedItemField ##NON NULL
   fiscalHost: NewType('Organization', GQLObject) ## Circular Reference for Organization
   fullDescription: str ##NON NULL
   fullDescriptionHTML: HTML ##NON NULL
   id: ID ##NON NULL
   isPublic: bool ##NON NULL
   name: str ##NON NULL
   nextPayoutDate: Date
   residenceCountryOrRegion: str
   resourcePath: URI ##NON NULL
   shortDescription: str ##NON NULL
   slug: str ##NON NULL
   sponsorable: NewType('Sponsorable', GQLObject) ##NON NULL ## Circular Reference for Sponsorable
   tiers: SponsorsTierConnectionField
   url: URI ##NON NULL

class SponsorshipNewsletter(GQLObject):
   body: str ##NON NULL
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   isPublished: bool ##NON NULL
   sponsorable: NewType('Sponsorable', GQLObject) ##NON NULL ## Circular Reference for Sponsorable
   subject: str ##NON NULL
   updatedAt: DateTime ##NON NULL

class SponsorshipNewsletterEdge(GQLObject):
   cursor: str ##NON NULL
   node: SponsorshipNewsletter

class SponsorshipNewsletterConnection(GQLObject):
   edges: list[SponsorshipNewsletterEdge]
   nodes: list[SponsorshipNewsletter]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SponsorConnectionField(SponsorConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: Args



class SponsorsActivityConnectionField(Generic[SponsorsActivityConnection]):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      period: SponsorsActivityPeriod
      since: DateTime
      until: DateTime
      orderBy: SponsorsActivityOrder
      actions: list[SponsorsActivityAction] ##NON NULL
      includeAsSponsor: bool

   _args: Args



class SponsorshipNewsletterConnectionField(SponsorshipNewsletterConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: Args



class SponsorshipConnectionField(Generic[SponsorshipConnection]):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder

   _args: Args



class Sponsorable(GQLObject):
   estimatedNextSponsorsPayoutInCents: int ##NON NULL
   hasSponsorsListing: bool ##NON NULL
   isSponsoredBy: isSponsoredByField ##NON NULL
   isSponsoringViewer: bool ##NON NULL
   monthlyEstimatedSponsorsIncomeInCents: int ##NON NULL
   sponsoring: SponsorConnectionField ##NON NULL
   sponsors: SponsorConnectionField ##NON NULL
   sponsorsActivities: SponsorsActivityConnectionField ##NON NULL ## Circular Reference for SponsorsActivityConnection
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: NewType('Sponsorship', GQLObject) ## Circular Reference for Sponsorship
   sponsorshipForViewerAsSponsorable: NewType('Sponsorship', GQLObject) ## Circular Reference for Sponsorship
   sponsorshipNewsletters: SponsorshipNewsletterConnectionField ##NON NULL
   sponsorshipsAsMaintainer: SponsorshipConnectionField ##NON NULL ## Circular Reference for SponsorshipConnection
   sponsorshipsAsSponsor: SponsorshipConnectionField ##NON NULL ## Circular Reference for SponsorshipConnection
   viewerCanSponsor: bool ##NON NULL
   viewerIsSponsoring: bool ##NON NULL

class Sponsorship(GQLObject):
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   isOneTimePayment: bool ##NON NULL
   isSponsorOptedIntoEmail: bool
   privacyLevel: SponsorshipPrivacy ##NON NULL
   sponsorEntity: Sponsor
   sponsorable: Sponsorable ##NON NULL
   tier: NewType('SponsorsTier', GQLObject) ## Circular Reference for SponsorsTier
   tierSelectedAt: DateTime

class SponsorshipEdge(GQLObject):
   cursor: str ##NON NULL
   node: Sponsorship

class SponsorshipConnection(GQLObject):
   edges: list[SponsorshipEdge]
   nodes: list[Sponsorship]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   totalRecurringMonthlyPriceInCents: int ##NON NULL
   totalRecurringMonthlyPriceInDollars: int ##NON NULL

class SponsorsTierAdminInfo(GQLObject):
   isDraft: bool ##NON NULL
   isPublished: bool ##NON NULL
   isRetired: bool ##NON NULL
   sponsorships: SponsorshipConnectionField ##NON NULL

class SponsorsTier(GQLObject):
   adminInfo: SponsorsTierAdminInfo
   closestLesserValueTier: NewType('SponsorsTier', GQLObject) ## Circular Reference for SponsorsTier
   createdAt: DateTime ##NON NULL
   description: str ##NON NULL
   descriptionHTML: HTML ##NON NULL
   id: ID ##NON NULL
   isCustomAmount: bool ##NON NULL
   isOneTime: bool ##NON NULL
   monthlyPriceInCents: int ##NON NULL
   monthlyPriceInDollars: int ##NON NULL
   name: str ##NON NULL
   sponsorsListing: SponsorsListing ##NON NULL
   updatedAt: DateTime ##NON NULL

class SponsorsActivity(GQLObject):
   action: SponsorsActivityAction ##NON NULL
   id: ID ##NON NULL
   previousSponsorsTier: SponsorsTier
   sponsor: Sponsor
   sponsorable: Sponsorable ##NON NULL
   sponsorsTier: SponsorsTier
   timestamp: DateTime

class SponsorsActivityEdge(GQLObject):
   cursor: str ##NON NULL
   node: SponsorsActivity

class SponsorsActivityConnection(GQLObject):
   edges: list[SponsorsActivityEdge]
   nodes: list[SponsorsActivity]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class StarredRepositoryEdge(GQLObject):
   cursor: str ##NON NULL
   node: Repository ##NON NULL
   starredAt: DateTime ##NON NULL

class StarredRepositoryConnection(GQLObject):
   edges: list[StarredRepositoryEdge]
   isOverLimit: bool ##NON NULL
   nodes: list[Repository]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ContributionsCollectionField(ContributionsCollection):
   class Args(GQLArgsSet): 
      organizationID: ID
      from_: DateTime
      to: DateTime

   _args: Args



class FollowerConnectionField(FollowerConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class FollowingConnectionField(FollowingConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class GistField(Gist):
   class Args(GQLArgsSet): 
      name: str ##NON NULL

   _args: Args



class OrganizationField(Generic[Organization]):
   class Args(GQLArgsSet): 
      login: str ##NON NULL

   _args: Args



class OrganizationConnectionField(OrganizationConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class PublicKeyConnectionField(PublicKeyConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class SavedReplyConnectionField(SavedReplyConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SavedReplyOrder

   _args: Args



class StarredRepositoryConnectionField(StarredRepositoryConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      ownedByViewer: bool
      orderBy: StarOrder

   _args: Args



class User(GQLObject):
   anyPinnableItems: anyPinnableItemsField ##NON NULL
   avatarUrl: URIField ##NON NULL
   bio: str
   bioHTML: HTML ##NON NULL
   canReceiveOrganizationEmailsWhenNotificationsRestricted: canReceiveOrganizationEmailsWhenNotificationsRestrictedField ##NON NULL
   commitComments: CommitCommentConnectionField ##NON NULL
   company: str
   companyHTML: HTML ##NON NULL
   contributionsCollection: ContributionsCollectionField ##NON NULL
   createdAt: DateTime ##NON NULL
   databaseId: int
   email: str ##NON NULL
   estimatedNextSponsorsPayoutInCents: int ##NON NULL
   followers: FollowerConnectionField ##NON NULL
   following: FollowingConnectionField ##NON NULL
   gist: GistField
   gistComments: GistCommentConnectionField ##NON NULL
   gists: GistConnectionField ##NON NULL
   hasSponsorsListing: bool ##NON NULL
   hovercard: HovercardField ##NON NULL
   id: ID ##NON NULL
   interactionAbility: RepositoryInteractionAbility
   isBountyHunter: bool ##NON NULL
   isCampusExpert: bool ##NON NULL
   isDeveloperProgramMember: bool ##NON NULL
   isEmployee: bool ##NON NULL
   isFollowingViewer: bool ##NON NULL
   isGitHubStar: bool ##NON NULL
   isHireable: bool ##NON NULL
   isSiteAdmin: bool ##NON NULL
   isSponsoredBy: isSponsoredByField ##NON NULL
   isSponsoringViewer: bool ##NON NULL
   isViewer: bool ##NON NULL
   issueComments: IssueCommentConnectionField ##NON NULL
   issues: IssueConnectionField ##NON NULL
   itemShowcase: ProfileItemShowcase ##NON NULL
   location: str
   login: str ##NON NULL
   monthlyEstimatedSponsorsIncomeInCents: int ##NON NULL
   name: str
   organization: OrganizationField ## Circular Reference for Organization
   organizationVerifiedDomainEmails: organizationVerifiedDomainEmailsField ##NON NULL
   organizations: OrganizationConnectionField ##NON NULL
   packages: PackageConnectionField ##NON NULL
   pinnableItems: PinnableItemConnectionField ##NON NULL
   pinnedItems: PinnableItemConnectionField ##NON NULL
   pinnedItemsRemaining: int ##NON NULL
   project: ProjectField
   projectV2: ProjectV2Field
   projects: ProjectConnectionField ##NON NULL
   projectsResourcePath: URI ##NON NULL
   projectsUrl: URI ##NON NULL
   projectsV2: ProjectV2ConnectionField ##NON NULL
   publicKeys: PublicKeyConnectionField ##NON NULL
   pullRequests: PullRequestConnectionField ##NON NULL
   recentProjects: ProjectV2ConnectionField ##NON NULL
   repositories: RepositoryConnectionField ##NON NULL
   repositoriesContributedTo: RepositoryConnectionField ##NON NULL
   repository: RepositoryField
   repositoryDiscussionComments: DiscussionCommentConnectionField ##NON NULL
   repositoryDiscussions: DiscussionConnectionField ##NON NULL
   resourcePath: URI ##NON NULL
   savedReplies: SavedReplyConnectionField
   sponsoring: SponsorConnectionField ##NON NULL
   sponsors: SponsorConnectionField ##NON NULL
   sponsorsActivities: SponsorsActivityConnectionField ##NON NULL
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: Sponsorship
   sponsorshipForViewerAsSponsorable: Sponsorship
   sponsorshipNewsletters: SponsorshipNewsletterConnectionField ##NON NULL
   sponsorshipsAsMaintainer: SponsorshipConnectionField ##NON NULL
   sponsorshipsAsSponsor: SponsorshipConnectionField ##NON NULL
   starredRepositories: StarredRepositoryConnectionField ##NON NULL
   status: UserStatus
   topRepositories: RepositoryConnectionField ##NON NULL
   twitterUsername: str
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   viewerCanChangePinnedItems: bool ##NON NULL
   viewerCanCreateProjects: bool ##NON NULL
   viewerCanFollow: bool ##NON NULL
   viewerCanSponsor: bool ##NON NULL
   viewerIsFollowing: bool ##NON NULL
   viewerIsSponsoring: bool ##NON NULL
   watching: RepositoryConnectionField ##NON NULL
   websiteUrl: URI

class AuditEntryActor(GQLObject): 
   pass

class MembersCanDeleteReposClearAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class MembersCanDeleteReposDisableAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class MembersCanDeleteReposEnableAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OauthApplicationCreateAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   applicationUrl: URI
   callbackUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   invitationEmail: str
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgAddMemberAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   permission: OrgAddMemberAuditEntryPermission
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgBlockUserAuditEntry(GQLObject):
   action: str ##NON NULL
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
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgConfigDisableCollaboratorsOnlyAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgConfigEnableCollaboratorsOnlyAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgCreateAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   billingPlan: OrgCreateAuditEntryBillingPlan
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgDisableOauthAppRestrictionsAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgDisableSamlAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   digestMethodUrl: URI
   id: ID ##NON NULL
   issuerUrl: URI
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgEnableOauthAppRestrictionsAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgEnableSamlAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   digestMethodUrl: URI
   id: ID ##NON NULL
   issuerUrl: URI
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgInviteMemberAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   email: str
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationInvitation: OrganizationInvitation
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgInviteToBusinessAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgOauthAppAccessApprovedAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgOauthAppAccessDeniedAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgOauthAppAccessRequestedAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgRemoveBillingManagerAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   reason: OrgRemoveBillingManagerAuditEntryReason
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgRemoveMemberAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   membershipTypes: list[OrgRemoveMemberAuditEntryMembershipType]
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   reason: OrgRemoveMemberAuditEntryReason
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgRemoveOutsideCollaboratorAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   membershipTypes: list[OrgRemoveOutsideCollaboratorAuditEntryMembershipType]
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   reason: OrgRemoveOutsideCollaboratorAuditEntryReason
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgRestoreMemberMembershipOrganizationAuditEntryData(GQLObject):
   organization: Organization
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

class OrgRestoreMemberAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   restoredCustomEmailRoutingsCount: int
   restoredIssueAssignmentsCount: int
   restoredMemberships: list[OrgRestoreMemberAuditEntryMembership]
   restoredMembershipsCount: int
   restoredRepositoriesCount: int
   restoredRepositoryStarsCount: int
   restoredRepositoryWatchesCount: int
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgUnblockUserAuditEntry(GQLObject):
   action: str ##NON NULL
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
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class OrgUpdateDefaultRepositoryPermissionAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   canCreateRepositories: bool
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI
   visibility: OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility

class OrgUpdateMemberRepositoryInvitationPermissionAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   canInviteOutsideCollaboratorsToRepositories: bool
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class PrivateRepositoryForkingDisableAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   isEnabled: bool
   mergeType: RepoChangeMergeSettingAuditEntryMergeType
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   forkParentName: str
   forkSourceName: str
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class RepositoryVisibilityChangeEnableAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI
   id: ID ##NON NULL
   operationType: OperationType
   organization: Organization
   organizationName: str
   organizationResourcePath: URI
   organizationUrl: URI
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class TeamAddMemberAuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   isLdapMapped: bool
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   isLdapMapped: bool
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   isLdapMapped: bool
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   isLdapMapped: bool
   operationType: OperationType
   organization: Organization
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
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   id: ID ##NON NULL
   isLdapMapped: bool
   operationType: OperationType
   organization: Organization
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
   cursor: str ##NON NULL
   node: OrganizationAuditEntry

class OrganizationAuditEntryConnection(GQLObject):
   edges: list[OrganizationAuditEntryEdge]
   nodes: list[OrganizationAuditEntry]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class VerifiableDomainOwner(GQLObject): 
   pass

class VerifiableDomain(GQLObject):
   createdAt: DateTime ##NON NULL
   databaseId: int
   dnsHostName: URI
   domain: URI ##NON NULL
   hasFoundHostName: bool ##NON NULL
   hasFoundVerificationToken: bool ##NON NULL
   id: ID ##NON NULL
   isApproved: bool ##NON NULL
   isRequiredForPolicyEnforcement: bool ##NON NULL
   isVerified: bool ##NON NULL
   owner: VerifiableDomainOwner ##NON NULL
   punycodeEncodedDomain: URI ##NON NULL
   tokenExpirationTime: DateTime
   updatedAt: DateTime ##NON NULL
   verificationToken: str

class VerifiableDomainEdge(GQLObject):
   cursor: str ##NON NULL
   node: VerifiableDomain

class VerifiableDomainConnection(GQLObject):
   edges: list[VerifiableDomainEdge]
   nodes: list[VerifiableDomain]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class OrganizationEnterpriseOwnerEdge(GQLObject):
   cursor: str ##NON NULL
   node: User
   organizationRole: RoleInOrganization ##NON NULL

class OrganizationEnterpriseOwnerConnection(GQLObject):
   edges: list[OrganizationEnterpriseOwnerEdge]
   nodes: list[User]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class MannequinEdge(GQLObject):
   cursor: str ##NON NULL
   node: Mannequin

class MannequinConnection(GQLObject):
   edges: list[MannequinEdge]
   nodes: list[Mannequin]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class OrganizationMemberEdge(GQLObject):
   cursor: str ##NON NULL
   hasTwoFactorEnabled: bool
   node: User
   role: OrganizationMemberRole

class OrganizationMemberConnection(GQLObject):
   edges: list[OrganizationMemberEdge]
   nodes: list[User]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class RepositoryMigration(GQLObject):
   continueOnError: bool ##NON NULL
   createdAt: DateTime ##NON NULL
   databaseId: str
   failureReason: str
   id: ID ##NON NULL
   migrationLogUrl: URI
   migrationSource: MigrationSource ##NON NULL
   repositoryName: str ##NON NULL
   sourceUrl: URI ##NON NULL
   state: MigrationState ##NON NULL

class RepositoryMigrationEdge(GQLObject):
   cursor: str ##NON NULL
   node: RepositoryMigration

class RepositoryMigrationConnection(GQLObject):
   edges: list[RepositoryMigrationEdge]
   nodes: list[RepositoryMigration]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ExternalIdentitySamlAttributes(GQLObject):
   attributes: ExternalIdentityAttribute ##NON NULL
   emails: list[UserEmailMetadata]
   familyName: str
   givenName: str
   groups: list[str]
   nameId: str
   username: str

class ExternalIdentityScimAttributes(GQLObject):
   emails: list[UserEmailMetadata]
   familyName: str
   givenName: str
   groups: list[str]
   username: str

class ExternalIdentity(GQLObject):
   guid: str ##NON NULL
   id: ID ##NON NULL
   organizationInvitation: OrganizationInvitation
   samlIdentity: ExternalIdentitySamlAttributes
   scimIdentity: ExternalIdentityScimAttributes
   user: User

class ExternalIdentityEdge(GQLObject):
   cursor: str ##NON NULL
   node: ExternalIdentity

class ExternalIdentityConnection(GQLObject):
   edges: list[ExternalIdentityEdge]
   nodes: list[ExternalIdentity]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ExternalIdentityConnectionField(ExternalIdentityConnection):
   class Args(GQLArgsSet): 
      membersOnly: bool
      login: str
      userName: str
      after: str
      before: str
      first: int
      last: int

   _args: Args



class OrganizationIdentityProvider(GQLObject):
   digestMethod: URI
   externalIdentities: ExternalIdentityConnectionField ##NON NULL
   id: ID ##NON NULL
   idpCertificate: X509Certificate
   issuer: str
   organization: Organization
   signatureMethod: URI
   ssoUrl: URI

class OrganizationAuditEntryConnectionField(OrganizationAuditEntryConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: AuditLogOrder

   _args: Args



class VerifiableDomainConnectionField(VerifiableDomainConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      isVerified: bool
      isApproved: bool
      orderBy: VerifiableDomainOrder

   _args: Args



class OrganizationEnterpriseOwnerConnectionField(OrganizationEnterpriseOwnerConnection):
   class Args(GQLArgsSet): 
      query: str
      organizationRole: RoleInOrganization
      orderBy: OrgEnterpriseOwnerOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class IpAllowListEntryConnectionField(Generic[IpAllowListEntryConnection]):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: Args



class MannequinConnectionField(MannequinConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: MannequinOrder

   _args: Args



class OrganizationMemberConnectionField(OrganizationMemberConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class RepositoryMigrationConnectionField(RepositoryMigrationConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      state: MigrationState
      repositoryName: str
      orderBy: RepositoryMigrationOrder

   _args: Args



class TeamField(Team):
   class Args(GQLArgsSet): 
      slug: str ##NON NULL

   _args: Args



class Organization(GQLObject):
   anyPinnableItems: anyPinnableItemsField ##NON NULL
   auditLog: OrganizationAuditEntryConnectionField ##NON NULL
   avatarUrl: URIField ##NON NULL
   createdAt: DateTime ##NON NULL
   databaseId: int
   description: str
   descriptionHTML: str
   domains: VerifiableDomainConnectionField
   email: str
   enterpriseOwners: OrganizationEnterpriseOwnerConnectionField ##NON NULL
   estimatedNextSponsorsPayoutInCents: int ##NON NULL
   hasSponsorsListing: bool ##NON NULL
   id: ID ##NON NULL
   interactionAbility: RepositoryInteractionAbility
   ipAllowListEnabledSetting: IpAllowListEnabledSettingValue ##NON NULL
   ipAllowListEntries: IpAllowListEntryConnectionField ##NON NULL ## Circular Reference for IpAllowListEntryConnection
   ipAllowListForInstalledAppsEnabledSetting: IpAllowListForInstalledAppsEnabledSettingValue ##NON NULL
   isSponsoredBy: isSponsoredByField ##NON NULL
   isSponsoringViewer: bool ##NON NULL
   isVerified: bool ##NON NULL
   itemShowcase: ProfileItemShowcase ##NON NULL
   location: str
   login: str ##NON NULL
   mannequins: MannequinConnectionField ##NON NULL
   memberStatuses: UserStatusConnectionField ##NON NULL
   membersCanForkPrivateRepositories: bool ##NON NULL
   membersWithRole: OrganizationMemberConnectionField ##NON NULL
   monthlyEstimatedSponsorsIncomeInCents: int ##NON NULL
   name: str
   newTeamResourcePath: URI ##NON NULL
   newTeamUrl: URI ##NON NULL
   notificationDeliveryRestrictionEnabledSetting: NotificationRestrictionSettingValue ##NON NULL
   organizationBillingEmail: str
   packages: PackageConnectionField ##NON NULL
   pendingMembers: UserConnectionField ##NON NULL
   pinnableItems: PinnableItemConnectionField ##NON NULL
   pinnedItems: PinnableItemConnectionField ##NON NULL
   pinnedItemsRemaining: int ##NON NULL
   project: ProjectField
   projectV2: ProjectV2Field
   projects: ProjectConnectionField ##NON NULL
   projectsResourcePath: URI ##NON NULL
   projectsUrl: URI ##NON NULL
   projectsV2: ProjectV2ConnectionField ##NON NULL
   recentProjects: ProjectV2ConnectionField ##NON NULL
   repositories: RepositoryConnectionField ##NON NULL
   repository: RepositoryField
   repositoryDiscussionComments: DiscussionCommentConnectionField ##NON NULL
   repositoryDiscussions: DiscussionConnectionField ##NON NULL
   repositoryMigrations: RepositoryMigrationConnectionField ##NON NULL
   requiresTwoFactorAuthentication: bool
   resourcePath: URI ##NON NULL
   samlIdentityProvider: OrganizationIdentityProvider
   sponsoring: SponsorConnectionField ##NON NULL
   sponsors: SponsorConnectionField ##NON NULL
   sponsorsActivities: SponsorsActivityConnectionField ##NON NULL
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: Sponsorship
   sponsorshipForViewerAsSponsorable: Sponsorship
   sponsorshipNewsletters: SponsorshipNewsletterConnectionField ##NON NULL
   sponsorshipsAsMaintainer: SponsorshipConnectionField ##NON NULL
   sponsorshipsAsSponsor: SponsorshipConnectionField ##NON NULL
   team: TeamField
   teams: TeamConnectionField ##NON NULL
   teamsResourcePath: URI ##NON NULL
   teamsUrl: URI ##NON NULL
   twitterUsername: str
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   viewerCanAdminister: bool ##NON NULL
   viewerCanChangePinnedItems: bool ##NON NULL
   viewerCanCreateProjects: bool ##NON NULL
   viewerCanCreateRepositories: bool ##NON NULL
   viewerCanCreateTeams: bool ##NON NULL
   viewerCanSponsor: bool ##NON NULL
   viewerIsAMember: bool ##NON NULL
   viewerIsFollowing: bool ##NON NULL
   viewerIsSponsoring: bool ##NON NULL
   webCommitSignoffRequired: bool ##NON NULL
   websiteUrl: URI

class EnterpriseOrganizationMembershipEdge(GQLObject):
   cursor: str ##NON NULL
   node: Organization
   role: EnterpriseUserAccountMembershipRole ##NON NULL

class EnterpriseOrganizationMembershipConnection(GQLObject):
   edges: list[EnterpriseOrganizationMembershipEdge]
   nodes: list[Organization]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterpriseOrganizationMembershipConnectionField(EnterpriseOrganizationMembershipConnection):
   class Args(GQLArgsSet): 
      query: str
      orderBy: OrganizationOrder
      role: EnterpriseUserAccountMembershipRole
      after: str
      before: str
      first: int
      last: int

   _args: Args



class EnterpriseUserAccount(GQLObject):
   avatarUrl: URIField ##NON NULL
   createdAt: DateTime ##NON NULL
   enterprise: NewType('Enterprise', GQLObject) ##NON NULL ## Circular Reference for Enterprise
   id: ID ##NON NULL
   login: str ##NON NULL
   name: str
   organizations: EnterpriseOrganizationMembershipConnectionField ##NON NULL
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   user: User

class EnterpriseMember(GQLObject): 
   pass

class EnterpriseMemberEdge(GQLObject):
   cursor: str ##NON NULL
   node: EnterpriseMember

class EnterpriseMemberConnection(GQLObject):
   edges: list[EnterpriseMemberEdge]
   nodes: list[EnterpriseMember]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterpriseAdministratorEdge(GQLObject):
   cursor: str ##NON NULL
   node: User
   role: EnterpriseAdministratorRole ##NON NULL

class EnterpriseAdministratorConnection(GQLObject):
   edges: list[EnterpriseAdministratorEdge]
   nodes: list[User]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterpriseServerUserAccountEmail(GQLObject):
   createdAt: DateTime ##NON NULL
   email: str ##NON NULL
   id: ID ##NON NULL
   isPrimary: bool ##NON NULL
   updatedAt: DateTime ##NON NULL
   userAccount: NewType('EnterpriseServerUserAccount', GQLObject) ##NON NULL ## Circular Reference for EnterpriseServerUserAccount

class EnterpriseServerUserAccountEmailEdge(GQLObject):
   cursor: str ##NON NULL
   node: EnterpriseServerUserAccountEmail

class EnterpriseServerUserAccountEmailConnection(GQLObject):
   edges: list[EnterpriseServerUserAccountEmailEdge]
   nodes: list[EnterpriseServerUserAccountEmail]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterpriseServerUserAccountEmailConnectionField(EnterpriseServerUserAccountEmailConnection):
   class Args(GQLArgsSet): 
      orderBy: EnterpriseServerUserAccountEmailOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class EnterpriseServerUserAccount(GQLObject):
   createdAt: DateTime ##NON NULL
   emails: EnterpriseServerUserAccountEmailConnectionField ##NON NULL
   enterpriseServerInstallation: NewType('EnterpriseServerInstallation', GQLObject) ##NON NULL ## Circular Reference for EnterpriseServerInstallation
   id: ID ##NON NULL
   isSiteAdmin: bool ##NON NULL
   login: str ##NON NULL
   profileName: str
   remoteCreatedAt: DateTime ##NON NULL
   remoteUserId: int ##NON NULL
   updatedAt: DateTime ##NON NULL

class EnterpriseServerUserAccountEdge(GQLObject):
   cursor: str ##NON NULL
   node: EnterpriseServerUserAccount

class EnterpriseServerUserAccountConnection(GQLObject):
   edges: list[EnterpriseServerUserAccountEdge]
   nodes: list[EnterpriseServerUserAccount]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterpriseServerUserAccountsUpload(GQLObject):
   createdAt: DateTime ##NON NULL
   enterprise: NewType('Enterprise', GQLObject) ##NON NULL ## Circular Reference for Enterprise
   enterpriseServerInstallation: NewType('EnterpriseServerInstallation', GQLObject) ##NON NULL ## Circular Reference for EnterpriseServerInstallation
   id: ID ##NON NULL
   name: str ##NON NULL
   syncState: EnterpriseServerUserAccountsUploadSyncState ##NON NULL
   updatedAt: DateTime ##NON NULL

class EnterpriseServerUserAccountsUploadEdge(GQLObject):
   cursor: str ##NON NULL
   node: EnterpriseServerUserAccountsUpload

class EnterpriseServerUserAccountsUploadConnection(GQLObject):
   edges: list[EnterpriseServerUserAccountsUploadEdge]
   nodes: list[EnterpriseServerUserAccountsUpload]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterpriseServerUserAccountConnectionField(EnterpriseServerUserAccountConnection):
   class Args(GQLArgsSet): 
      orderBy: EnterpriseServerUserAccountOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class EnterpriseServerUserAccountsUploadConnectionField(EnterpriseServerUserAccountsUploadConnection):
   class Args(GQLArgsSet): 
      orderBy: EnterpriseServerUserAccountsUploadOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class EnterpriseServerInstallation(GQLObject):
   createdAt: DateTime ##NON NULL
   customerName: str ##NON NULL
   hostName: str ##NON NULL
   id: ID ##NON NULL
   isConnected: bool ##NON NULL
   updatedAt: DateTime ##NON NULL
   userAccounts: EnterpriseServerUserAccountConnectionField ##NON NULL
   userAccountsUploads: EnterpriseServerUserAccountsUploadConnectionField ##NON NULL

class EnterpriseServerInstallationEdge(GQLObject):
   cursor: str ##NON NULL
   node: EnterpriseServerInstallation

class EnterpriseServerInstallationConnection(GQLObject):
   edges: list[EnterpriseServerInstallationEdge]
   nodes: list[EnterpriseServerInstallation]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class OIDCProvider(GQLObject):
   enterprise: NewType('Enterprise', GQLObject) ## Circular Reference for Enterprise
   externalIdentities: ExternalIdentityConnectionField ##NON NULL
   id: ID ##NON NULL
   providerType: OIDCProviderType ##NON NULL
   tenantId: str ##NON NULL

class EnterpriseRepositoryInfoEdge(GQLObject):
   cursor: str ##NON NULL
   node: EnterpriseRepositoryInfo

class EnterpriseRepositoryInfoConnection(GQLObject):
   edges: list[EnterpriseRepositoryInfoEdge]
   nodes: list[EnterpriseRepositoryInfo]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterpriseRepositoryInfoConnectionField(EnterpriseRepositoryInfoConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: RepositoryOrder

   _args: Args



class EnterpriseOutsideCollaboratorEdge(GQLObject):
   cursor: str ##NON NULL
   node: User
   repositories: EnterpriseRepositoryInfoConnectionField ##NON NULL

class EnterpriseOutsideCollaboratorConnection(GQLObject):
   edges: list[EnterpriseOutsideCollaboratorEdge]
   nodes: list[User]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterpriseAdministratorInvitation(GQLObject):
   createdAt: DateTime ##NON NULL
   email: str
   enterprise: NewType('Enterprise', GQLObject) ##NON NULL ## Circular Reference for Enterprise
   id: ID ##NON NULL
   invitee: User
   inviter: User
   role: EnterpriseAdministratorRole ##NON NULL

class EnterpriseAdministratorInvitationEdge(GQLObject):
   cursor: str ##NON NULL
   node: EnterpriseAdministratorInvitation

class EnterpriseAdministratorInvitationConnection(GQLObject):
   edges: list[EnterpriseAdministratorInvitationEdge]
   nodes: list[EnterpriseAdministratorInvitation]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class RepositoryInfo(GQLObject):
   createdAt: DateTime ##NON NULL
   description: str
   descriptionHTML: HTML ##NON NULL
   forkCount: int ##NON NULL
   hasDiscussionsEnabled: bool ##NON NULL
   hasIssuesEnabled: bool ##NON NULL
   hasProjectsEnabled: bool ##NON NULL
   hasWikiEnabled: bool ##NON NULL
   homepageUrl: URI
   isArchived: bool ##NON NULL
   isFork: bool ##NON NULL
   isInOrganization: bool ##NON NULL
   isLocked: bool ##NON NULL
   isMirror: bool ##NON NULL
   isPrivate: bool ##NON NULL
   isTemplate: bool ##NON NULL
   licenseInfo: License
   lockReason: RepositoryLockReason
   mirrorUrl: URI
   name: str ##NON NULL
   nameWithOwner: str ##NON NULL
   openGraphImageUrl: URI ##NON NULL
   owner: RepositoryOwner ##NON NULL
   pushedAt: DateTime
   resourcePath: URI ##NON NULL
   shortDescriptionHTML: HTMLField ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   usesCustomOpenGraphImage: bool ##NON NULL
   visibility: RepositoryVisibility ##NON NULL

class RepositoryInvitation(GQLObject):
   email: str
   id: ID ##NON NULL
   invitee: User
   inviter: User ##NON NULL
   permalink: URI ##NON NULL
   permission: RepositoryPermission ##NON NULL
   repository: RepositoryInfo

class RepositoryInvitationEdge(GQLObject):
   cursor: str ##NON NULL
   node: RepositoryInvitation

class RepositoryInvitationConnection(GQLObject):
   edges: list[RepositoryInvitationEdge]
   nodes: list[RepositoryInvitation]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterprisePendingMemberInvitationEdge(GQLObject):
   cursor: str ##NON NULL
   node: OrganizationInvitation

class EnterprisePendingMemberInvitationConnection(GQLObject):
   edges: list[EnterprisePendingMemberInvitationEdge]
   nodes: list[OrganizationInvitation]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   totalUniqueUserCount: int ##NON NULL

class EnterpriseIdentityProvider(GQLObject):
   digestMethod: SamlDigestAlgorithm
   enterprise: NewType('Enterprise', GQLObject) ## Circular Reference for Enterprise
   externalIdentities: ExternalIdentityConnectionField ##NON NULL
   id: ID ##NON NULL
   idpCertificate: X509Certificate
   issuer: str
   recoveryCodes: list[str]
   signatureMethod: SamlSignatureAlgorithm
   ssoUrl: URI

class EnterpriseAdministratorConnectionField(EnterpriseAdministratorConnection):
   class Args(GQLArgsSet): 
      organizationLogins: list[str] ##NON NULL
      query: str
      role: EnterpriseAdministratorRole
      orderBy: EnterpriseMemberOrder
      hasTwoFactorEnabled: bool
      after: str
      before: str
      first: int
      last: int

   _args: Args



class EnterpriseServerInstallationConnectionField(EnterpriseServerInstallationConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      connectedOnly: bool
      orderBy: EnterpriseServerInstallationOrder

   _args: Args



class EnterpriseOutsideCollaboratorConnectionField(EnterpriseOutsideCollaboratorConnection):
   class Args(GQLArgsSet): 
      login: str
      query: str
      orderBy: EnterpriseMemberOrder
      visibility: RepositoryVisibility
      hasTwoFactorEnabled: bool
      organizationLogins: list[str] ##NON NULL
      after: str
      before: str
      first: int
      last: int

   _args: Args



class EnterpriseAdministratorInvitationConnectionField(EnterpriseAdministratorInvitationConnection):
   class Args(GQLArgsSet): 
      query: str
      orderBy: EnterpriseAdministratorInvitationOrder
      role: EnterpriseAdministratorRole
      after: str
      before: str
      first: int
      last: int

   _args: Args



class RepositoryInvitationConnectionField(RepositoryInvitationConnection):
   class Args(GQLArgsSet): 
      query: str
      orderBy: RepositoryInvitationOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class EnterprisePendingMemberInvitationConnectionField(EnterprisePendingMemberInvitationConnection):
   class Args(GQLArgsSet): 
      query: str
      organizationLogins: list[str] ##NON NULL
      after: str
      before: str
      first: int
      last: int

   _args: Args



class EnterpriseMemberConnectionField(EnterpriseMemberConnection):
   class Args(GQLArgsSet): 
      orderBy: EnterpriseMemberOrder
      after: str
      before: str
      first: int
      last: int

   _args: Args



class EnterpriseOwnerInfo(GQLObject):
   admins: EnterpriseAdministratorConnectionField ##NON NULL
   affiliatedUsersWithTwoFactorDisabled: UserConnectionField ##NON NULL
   affiliatedUsersWithTwoFactorDisabledExist: bool ##NON NULL
   allowPrivateRepositoryForkingSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   allowPrivateRepositoryForkingSettingOrganizations: OrganizationConnectionField ##NON NULL
   allowPrivateRepositoryForkingSettingPolicyValue: EnterpriseAllowPrivateRepositoryForkingPolicyValue
   defaultRepositoryPermissionSetting: EnterpriseDefaultRepositoryPermissionSettingValue ##NON NULL
   defaultRepositoryPermissionSettingOrganizations: OrganizationConnectionField ##NON NULL
   domains: VerifiableDomainConnectionField ##NON NULL
   enterpriseServerInstallations: EnterpriseServerInstallationConnectionField ##NON NULL
   ipAllowListEnabledSetting: IpAllowListEnabledSettingValue ##NON NULL
   ipAllowListEntries: IpAllowListEntryConnectionField ##NON NULL
   ipAllowListForInstalledAppsEnabledSetting: IpAllowListForInstalledAppsEnabledSettingValue ##NON NULL
   isUpdatingDefaultRepositoryPermission: bool ##NON NULL
   isUpdatingTwoFactorRequirement: bool ##NON NULL
   membersCanChangeRepositoryVisibilitySetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanChangeRepositoryVisibilitySettingOrganizations: OrganizationConnectionField ##NON NULL
   membersCanCreateInternalRepositoriesSetting: bool
   membersCanCreatePrivateRepositoriesSetting: bool
   membersCanCreatePublicRepositoriesSetting: bool
   membersCanCreateRepositoriesSetting: EnterpriseMembersCanCreateRepositoriesSettingValue
   membersCanCreateRepositoriesSettingOrganizations: OrganizationConnectionField ##NON NULL
   membersCanDeleteIssuesSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanDeleteIssuesSettingOrganizations: OrganizationConnectionField ##NON NULL
   membersCanDeleteRepositoriesSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanDeleteRepositoriesSettingOrganizations: OrganizationConnectionField ##NON NULL
   membersCanInviteCollaboratorsSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanInviteCollaboratorsSettingOrganizations: OrganizationConnectionField ##NON NULL
   membersCanMakePurchasesSetting: EnterpriseMembersCanMakePurchasesSettingValue ##NON NULL
   membersCanUpdateProtectedBranchesSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanUpdateProtectedBranchesSettingOrganizations: OrganizationConnectionField ##NON NULL
   membersCanViewDependencyInsightsSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanViewDependencyInsightsSettingOrganizations: OrganizationConnectionField ##NON NULL
   notificationDeliveryRestrictionEnabledSetting: NotificationRestrictionSettingValue ##NON NULL
   oidcProvider: OIDCProvider
   organizationProjectsSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   organizationProjectsSettingOrganizations: OrganizationConnectionField ##NON NULL
   outsideCollaborators: EnterpriseOutsideCollaboratorConnectionField ##NON NULL
   pendingAdminInvitations: EnterpriseAdministratorInvitationConnectionField ##NON NULL
   pendingCollaboratorInvitations: RepositoryInvitationConnectionField ##NON NULL
   pendingMemberInvitations: EnterprisePendingMemberInvitationConnectionField ##NON NULL
   repositoryProjectsSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   repositoryProjectsSettingOrganizations: OrganizationConnectionField ##NON NULL
   samlIdentityProvider: EnterpriseIdentityProvider
   samlIdentityProviderSettingOrganizations: OrganizationConnectionField ##NON NULL
   supportEntitlements: EnterpriseMemberConnectionField ##NON NULL
   teamDiscussionsSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   teamDiscussionsSettingOrganizations: OrganizationConnectionField ##NON NULL
   twoFactorRequiredSetting: EnterpriseEnabledSettingValue ##NON NULL
   twoFactorRequiredSettingOrganizations: OrganizationConnectionField ##NON NULL

class Enterprise(GQLObject):
   avatarUrl: URIField ##NON NULL
   billingInfo: EnterpriseBillingInfo
   createdAt: DateTime ##NON NULL
   databaseId: int
   description: str
   descriptionHTML: HTML ##NON NULL
   id: ID ##NON NULL
   location: str
   members: EnterpriseMemberConnectionField ##NON NULL
   name: str ##NON NULL
   organizations: OrganizationConnectionField ##NON NULL
   ownerInfo: EnterpriseOwnerInfo
   resourcePath: URI ##NON NULL
   slug: str ##NON NULL
   url: URI ##NON NULL
   viewerIsAdmin: bool ##NON NULL
   websiteUrl: URI

class IpAllowListOwner(GQLObject): 
   pass

class IpAllowListEntry(GQLObject):
   allowListValue: str ##NON NULL
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   isActive: bool ##NON NULL
   name: str
   owner: IpAllowListOwner ##NON NULL
   updatedAt: DateTime ##NON NULL

class IpAllowListEntryEdge(GQLObject):
   cursor: str ##NON NULL
   node: IpAllowListEntry

class IpAllowListEntryConnection(GQLObject):
   edges: list[IpAllowListEntryEdge]
   nodes: list[IpAllowListEntry]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class App(GQLObject):
   createdAt: DateTime ##NON NULL
   databaseId: int
   description: str
   id: ID ##NON NULL
   ipAllowListEntries: IpAllowListEntryConnectionField ##NON NULL
   logoBackgroundColor: str ##NON NULL
   logoUrl: URIField ##NON NULL
   name: str ##NON NULL
   slug: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL

class CheckRunEdge(GQLObject):
   cursor: str ##NON NULL
   node: CheckRun

class CheckRunConnection(GQLObject):
   edges: list[CheckRunEdge]
   nodes: list[CheckRun]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class Push(GQLObject):
   id: ID ##NON NULL
   nextSha: GitObjectID
   permalink: URI ##NON NULL
   previousSha: GitObjectID
   pusher: Actor ##NON NULL
   repository: Repository ##NON NULL

class CheckRunConnectionField(CheckRunConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      filterBy: CheckRunFilter

   _args: Args



class CheckSuite(GQLObject):
   app: App
   branch: Ref
   checkRuns: CheckRunConnectionField
   commit: Commit ##NON NULL
   conclusion: CheckConclusionState
   createdAt: DateTime ##NON NULL
   creator: User
   databaseId: int
   id: ID ##NON NULL
   matchingPullRequests: PullRequestConnectionField
   push: Push
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   status: CheckStatusState ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   workflowRun: NewType('WorkflowRun', GQLObject) ## Circular Reference for WorkflowRun

class DeploymentReview(GQLObject):
   comment: str ##NON NULL
   databaseId: int
   environments: EnvironmentConnectionField ##NON NULL
   id: ID ##NON NULL
   state: DeploymentReviewState ##NON NULL
   user: User ##NON NULL

class DeploymentReviewEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeploymentReview

class DeploymentReviewConnection(GQLObject):
   edges: list[DeploymentReviewEdge]
   nodes: list[DeploymentReview]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeploymentRequestEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeploymentRequest

class DeploymentRequestConnection(GQLObject):
   edges: list[DeploymentRequestEdge]
   nodes: list[DeploymentRequest]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class WorkflowRunConnectionField(Generic[WorkflowRunConnection]):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int
      orderBy: WorkflowRunOrder

   _args: Args



class Workflow(GQLObject):
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   runs: WorkflowRunConnectionField ##NON NULL ## Circular Reference for WorkflowRunConnection
   updatedAt: DateTime ##NON NULL

class DeploymentReviewConnectionField(DeploymentReviewConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class DeploymentRequestConnectionField(DeploymentRequestConnection):
   class Args(GQLArgsSet): 
      after: str
      before: str
      first: int
      last: int

   _args: Args



class WorkflowRun(GQLObject):
   checkSuite: CheckSuite ##NON NULL
   createdAt: DateTime ##NON NULL
   databaseId: int
   deploymentReviews: DeploymentReviewConnectionField ##NON NULL
   id: ID ##NON NULL
   pendingDeploymentRequests: DeploymentRequestConnectionField ##NON NULL
   resourcePath: URI ##NON NULL
   runNumber: int ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   workflow: Workflow ##NON NULL

class WorkflowRunEdge(GQLObject):
   cursor: str ##NON NULL
   node: WorkflowRun

class WorkflowRunConnection(GQLObject):
   edges: list[WorkflowRunEdge]
   nodes: list[WorkflowRun]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class UpdateTeamsRepositoryPayload(GQLObject):
   clientMutationId: str
   repository: Repository
   teams: list[Team]

class UpdatePullRequestPayload(GQLObject):
   actor: Actor
   clientMutationId: str
   pullRequest: PullRequest

class UpdateIssuePayload(GQLObject):
   actor: Actor
   clientMutationId: str
   issue: Issue

class CheckAnnotationData(GQLObject):
   path: str ##NON NULL
   location: CheckAnnotationRange ##NON NULL
   annotationLevel: CheckAnnotationLevel ##NON NULL
   message: str ##NON NULL
   title: str
   rawDetails: str

class CheckRunOutput(GQLObject):
   title: str ##NON NULL
   summary: str ##NON NULL
   text: str
   annotations: list[CheckAnnotationData] ##NON NULL
   images: list[CheckRunOutputImage] ##NON NULL

class UpdateCheckRunInput(GQLObject):
   repositoryId: ID ##NON NULL
   checkRunId: ID ##NON NULL
   name: str
   detailsUrl: URI
   externalId: str
   status: RequestableCheckStatusState
   startedAt: DateTime
   conclusion: CheckConclusionState
   completedAt: DateTime
   output: CheckRunOutput
   actions: list[CheckRunAction] ##NON NULL
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
   abbreviatedOid: str ##NON NULL
   commitResourcePath: URI ##NON NULL
   commitUrl: URI ##NON NULL
   id: ID ##NON NULL
   message: str
   name: str ##NON NULL
   oid: GitObjectID ##NON NULL
   repository: Repository ##NON NULL
   tagger: GitActor
   target: GitObject ##NON NULL

class SponsorableItem(GQLObject): 
   pass

class SponsorableItemEdge(GQLObject):
   cursor: str ##NON NULL
   node: SponsorableItem

class SponsorableItemConnection(GQLObject):
   edges: list[SponsorableItemEdge]
   nodes: list[SponsorableItem]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SecurityAdvisoryEdge(GQLObject):
   cursor: str ##NON NULL
   node: SecurityAdvisory

class SecurityAdvisoryConnection(GQLObject):
   edges: list[SecurityAdvisoryEdge]
   nodes: list[SecurityAdvisory]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class MarketplaceListing(GQLObject):
   app: App
   companyUrl: URI
   configurationResourcePath: URI ##NON NULL
   configurationUrl: URI ##NON NULL
   documentationUrl: URI
   extendedDescription: str
   extendedDescriptionHTML: HTML ##NON NULL
   fullDescription: str ##NON NULL
   fullDescriptionHTML: HTML ##NON NULL
   hasPublishedFreeTrialPlans: bool ##NON NULL
   hasTermsOfService: bool ##NON NULL
   hasVerifiedOwner: bool ##NON NULL
   howItWorks: str
   howItWorksHTML: HTML ##NON NULL
   id: ID ##NON NULL
   installationUrl: URI
   installedForViewer: bool ##NON NULL
   isArchived: bool ##NON NULL
   isDraft: bool ##NON NULL
   isPaid: bool ##NON NULL
   isPublic: bool ##NON NULL
   isRejected: bool ##NON NULL
   isUnverified: bool ##NON NULL
   isUnverifiedPending: bool ##NON NULL
   isVerificationPendingFromDraft: bool ##NON NULL
   isVerificationPendingFromUnverified: bool ##NON NULL
   isVerified: bool ##NON NULL
   logoBackgroundColor: str ##NON NULL
   logoUrl: URIField
   name: str ##NON NULL
   normalizedShortDescription: str ##NON NULL
   pricingUrl: URI
   primaryCategory: MarketplaceCategory ##NON NULL
   privacyPolicyUrl: URI ##NON NULL
   resourcePath: URI ##NON NULL
   screenshotUrls: str ##NON NULL
   secondaryCategory: MarketplaceCategory
   shortDescription: str ##NON NULL
   slug: str ##NON NULL
   statusUrl: URI
   supportEmail: str
   supportUrl: URI ##NON NULL
   termsOfServiceUrl: URI
   url: URI ##NON NULL
   viewerCanAddPlans: bool ##NON NULL
   viewerCanApprove: bool ##NON NULL
   viewerCanDelist: bool ##NON NULL
   viewerCanEdit: bool ##NON NULL
   viewerCanEditCategories: bool ##NON NULL
   viewerCanEditPlans: bool ##NON NULL
   viewerCanRedraft: bool ##NON NULL
   viewerCanReject: bool ##NON NULL
   viewerCanRequestApproval: bool ##NON NULL
   viewerHasPurchased: bool ##NON NULL
   viewerHasPurchasedForAllOrganizations: bool ##NON NULL
   viewerIsListingAdmin: bool ##NON NULL

class SearchResultItem(GQLObject): 
   pass

class TextMatch(GQLObject):
   fragment: str ##NON NULL
   highlights: TextMatchHighlight ##NON NULL
   property: str ##NON NULL

class SearchResultItemEdge(GQLObject):
   cursor: str ##NON NULL
   node: SearchResultItem
   textMatches: list[TextMatch]

class SearchResultItemConnection(GQLObject):
   codeCount: int ##NON NULL
   discussionCount: int ##NON NULL
   edges: list[SearchResultItemEdge]
   issueCount: int ##NON NULL
   nodes: list[SearchResultItem]
   pageInfo: PageInfo ##NON NULL
   repositoryCount: int ##NON NULL
   userCount: int ##NON NULL
   wikiCount: int ##NON NULL

class RequestReviewsPayload(GQLObject):
   actor: Actor
   clientMutationId: str
   pullRequest: PullRequest
   requestedReviewersEdge: UserEdge

class RemoveReactionPayload(GQLObject):
   clientMutationId: str
   reaction: Reaction
   subject: Reactable

class RemoveEnterpriseOrganizationPayload(GQLObject):
   clientMutationId: str
   enterprise: Enterprise
   organization: Organization
   viewer: User

class RemoveEnterpriseAdminPayload(GQLObject):
   admin: User
   clientMutationId: str
   enterprise: Enterprise
   message: str
   viewer: User

class PullRequestThread(GQLObject):
   comments: PullRequestReviewCommentConnectionField ##NON NULL
   diffSide: DiffSide ##NON NULL
   id: ID ##NON NULL
   isCollapsed: bool ##NON NULL
   isOutdated: bool ##NON NULL
   isResolved: bool ##NON NULL
   line: int
   pullRequest: PullRequest ##NON NULL
   repository: Repository ##NON NULL
   resolvedBy: User
   startDiffSide: DiffSide
   startLine: int
   viewerCanReply: bool ##NON NULL
   viewerCanResolve: bool ##NON NULL
   viewerCanUnresolve: bool ##NON NULL

class ProjectV2ItemFieldValueCommon(GQLObject):
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   field: ProjectV2FieldConfiguration ##NON NULL
   id: ID ##NON NULL
   item: ProjectV2Item ##NON NULL
   updatedAt: DateTime ##NON NULL

class ProfileOwner(GQLObject):
   anyPinnableItems: anyPinnableItemsField ##NON NULL
   email: str
   id: ID ##NON NULL
   itemShowcase: ProfileItemShowcase ##NON NULL
   location: str
   login: str ##NON NULL
   name: str
   pinnableItems: PinnableItemConnectionField ##NON NULL
   pinnedItems: PinnableItemConnectionField ##NON NULL
   pinnedItemsRemaining: int ##NON NULL
   viewerCanChangePinnedItems: bool ##NON NULL
   websiteUrl: URI

class OrganizationOrUser(GQLObject): 
   pass

class MergePullRequestPayload(GQLObject):
   actor: Actor
   clientMutationId: str
   pullRequest: PullRequest

class MarketplaceListingEdge(GQLObject):
   cursor: str ##NON NULL
   node: MarketplaceListing

class MarketplaceListingConnection(GQLObject):
   edges: list[MarketplaceListingEdge]
   nodes: list[MarketplaceListing]
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class LockLockablePayload(GQLObject):
   actor: Actor
   clientMutationId: str
   lockedRecord: Lockable

class LinkRepositoryToProjectPayload(GQLObject):
   clientMutationId: str
   project: Project
   repository: Repository

class FileChanges(GQLObject):
   deletions: list[FileDeletion] ##NON NULL
   additions: list[FileAddition] ##NON NULL

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
   branch: CommittableBranch ##NON NULL
   fileChanges: FileChanges
   message: CommitMessage ##NON NULL
   expectedHeadOid: GitObjectID ##NON NULL
   clientMutationId: str

class CreateCheckRunInput(GQLObject):
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   headSha: GitObjectID ##NON NULL
   detailsUrl: URI
   externalId: str
   status: RequestableCheckStatusState
   startedAt: DateTime
   conclusion: CheckConclusionState
   completedAt: DateTime
   output: CheckRunOutput
   actions: list[CheckRunAction] ##NON NULL
   clientMutationId: str

class Claimable(GQLObject): 
   pass

class CreateAttributionInvitationPayload(GQLObject):
   clientMutationId: str
   owner: Organization
   source: Claimable
   target: Claimable

class Comment(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   lastEditedAt: DateTime
   publishedAt: DateTime
   updatedAt: DateTime ##NON NULL
   userContentEdits: UserContentEditConnectionField
   viewerDidAuthor: bool ##NON NULL

class AuditEntry(GQLObject):
   action: str ##NON NULL
   actor: AuditEntryActor
   actorIp: str
   actorLocation: ActorLocation
   actorLogin: str
   actorResourcePath: URI
   actorUrl: URI
   createdAt: PreciseDateTime ##NON NULL
   operationType: OperationType
   user: User
   userLogin: str
   userResourcePath: URI
   userUrl: URI

class AddReactionPayload(GQLObject):
   clientMutationId: str
   reaction: Reaction
   subject: Reactable

class AddPullRequestReviewPayload(GQLObject):
   clientMutationId: str
   pullRequestReview: PullRequestReview
   reviewEdge: PullRequestReviewEdge

class AddPullRequestReviewInput(GQLObject):
   pullRequestId: ID ##NON NULL
   commitOID: GitObjectID
   body: str
   event: PullRequestReviewEvent
   comments: list[DraftPullRequestReviewComment]
   threads: list[DraftPullRequestReviewThread]
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
   users: list[User]

class AddLabelsToLabelablePayload(GQLObject):
   clientMutationId: str
   labelable: Labelable

class AddProjectDraftIssuePayload(GQLObject):
   clientMutationId: str

class AddProjectNextItemPayload(GQLObject):
   clientMutationId: str

class AddProjectV2DraftIssuePayload(GQLObject):
   clientMutationId: str
   projectItem: ProjectV2Item

class AddProjectV2ItemByIdPayload(GQLObject):
   clientMutationId: str
   item: ProjectV2Item

class AddPullRequestReviewThreadPayload(GQLObject):
   clientMutationId: str
   thread: PullRequestReviewThread

class Starrable(GQLObject):
   id: ID ##NON NULL
   stargazerCount: int ##NON NULL
   stargazers: StargazerConnectionField ##NON NULL
   viewerHasStarred: bool ##NON NULL

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
   deployments: list[Deployment]

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
   abbreviatedOid: str ##NON NULL
   byteSize: int ##NON NULL
   commitResourcePath: URI ##NON NULL
   commitUrl: URI ##NON NULL
   id: ID ##NON NULL
   isBinary: bool
   isTruncated: bool ##NON NULL
   oid: GitObjectID ##NON NULL
   repository: Repository ##NON NULL
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
   isRestricted: bool ##NON NULL
   occurredAt: DateTime ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL
   user: User ##NON NULL

class ConvertProjectCardNoteToIssuePayload(GQLObject):
   clientMutationId: str
   projectCard: ProjectCard

class ConvertPullRequestToDraftPayload(GQLObject):
   clientMutationId: str
   pullRequest: PullRequest

class CreateBranchProtectionRuleInput(GQLObject):
   repositoryId: ID ##NON NULL
   pattern: str ##NON NULL
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
   reviewDismissalActorIds: list[ID] ##NON NULL
   bypassPullRequestActorIds: list[ID] ##NON NULL
   bypassForcePushActorIds: list[ID] ##NON NULL
   restrictsPushes: bool
   pushActorIds: list[ID] ##NON NULL
   requiredStatusCheckContexts: list[str] ##NON NULL
   requiredStatusChecks: list[RequiredStatusCheckInput] ##NON NULL
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
   email: str ##NON NULL
   isValid: bool ##NON NULL
   keyId: str
   payload: str ##NON NULL
   signature: str ##NON NULL
   signer: User
   state: GitSignatureState ##NON NULL
   wasSignedByGitHub: bool ##NON NULL

class GrantEnterpriseOrganizationsMigratorRolePayload(GQLObject):
   clientMutationId: str
   organizations: OrganizationConnectionField

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

class MemberStatusable(GQLObject):
   memberStatuses: UserStatusConnectionField ##NON NULL

class MergeBranchPayload(GQLObject):
   clientMutationId: str
   mergeCommit: Commit

class Migration(GQLObject):
   continueOnError: bool ##NON NULL
   createdAt: DateTime ##NON NULL
   databaseId: str
   failureReason: str
   id: ID ##NON NULL
   migrationLogUrl: URI
   migrationSource: MigrationSource ##NON NULL
   repositoryName: str ##NON NULL
   sourceUrl: URI ##NON NULL
   state: MigrationState ##NON NULL

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

class OrganizationTeamsHovercardContext(GQLObject):
   message: str ##NON NULL
   octicon: str ##NON NULL
   relevantTeams: TeamConnectionField ##NON NULL
   teamsResourcePath: URI ##NON NULL
   teamsUrl: URI ##NON NULL
   totalTeamCount: int ##NON NULL

class OrganizationsHovercardContext(GQLObject):
   message: str ##NON NULL
   octicon: str ##NON NULL
   relevantOrganizations: OrganizationConnectionField ##NON NULL
   totalOrganizationCount: int ##NON NULL

class PackageOwner(GQLObject):
   id: ID ##NON NULL
   packages: PackageConnectionField ##NON NULL

class PackageTag(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   version: PackageVersion

class PinIssuePayload(GQLObject):
   clientMutationId: str
   issue: Issue

class ProjectV2FieldCommon(GQLObject):
   createdAt: DateTime ##NON NULL
   dataType: ProjectV2FieldType ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   project: ProjectV2 ##NON NULL
   updatedAt: DateTime ##NON NULL

class ProjectV2Recent(GQLObject):
   recentProjects: ProjectV2ConnectionField ##NON NULL

class PublishSponsorsTierPayload(GQLObject):
   clientMutationId: str
   sponsorsTier: SponsorsTier

class RegenerateEnterpriseIdentityProviderRecoveryCodesPayload(GQLObject):
   clientMutationId: str
   identityProvider: EnterpriseIdentityProvider

class RejectDeploymentsPayload(GQLObject):
   clientMutationId: str
   deployments: list[Deployment]

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

class RepositoryDiscussionAuthor(GQLObject):
   repositoryDiscussions: DiscussionConnectionField ##NON NULL

class RepositoryDiscussionCommentAuthor(GQLObject):
   repositoryDiscussionComments: DiscussionCommentConnectionField ##NON NULL

class RepositoryNode(GQLObject):
   repository: Repository ##NON NULL

class RerequestCheckSuitePayload(GQLObject):
   checkSuite: CheckSuite
   clientMutationId: str

class ResolveReviewThreadPayload(GQLObject):
   clientMutationId: str
   thread: PullRequestReviewThread

class RevokeEnterpriseOrganizationsMigratorRolePayload(GQLObject):
   clientMutationId: str
   organizations: OrganizationConnectionField

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
   email: str ##NON NULL
   isValid: bool ##NON NULL
   payload: str ##NON NULL
   signature: str ##NON NULL
   signer: User
   state: GitSignatureState ##NON NULL
   wasSignedByGitHub: bool ##NON NULL

class SshSignature(GQLObject):
   email: str ##NON NULL
   isValid: bool ##NON NULL
   keyFingerprint: str
   payload: str ##NON NULL
   signature: str ##NON NULL
   signer: User
   state: GitSignatureState ##NON NULL
   wasSignedByGitHub: bool ##NON NULL

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
   email: str ##NON NULL
   isValid: bool ##NON NULL
   payload: str ##NON NULL
   signature: str ##NON NULL
   signer: User
   state: GitSignatureState ##NON NULL
   wasSignedByGitHub: bool ##NON NULL

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
   branchProtectionRuleId: ID ##NON NULL
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
   reviewDismissalActorIds: list[ID] ##NON NULL
   bypassPullRequestActorIds: list[ID] ##NON NULL
   bypassForcePushActorIds: list[ID] ##NON NULL
   restrictsPushes: bool
   pushActorIds: list[ID] ##NON NULL
   requiredStatusCheckContexts: list[str] ##NON NULL
   requiredStatusChecks: list[RequiredStatusCheckInput] ##NON NULL
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

class UpdateCheckSuitePreferencesInput(GQLObject):
   repositoryId: ID ##NON NULL
   autoTriggerPreferences: list[CheckSuiteAutoTriggerPreference] ##NON NULL
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

class UpdateProjectDraftIssuePayload(GQLObject):
   clientMutationId: str
   draftIssue: DraftIssue

class UpdateProjectNextItemFieldPayload(GQLObject):
   clientMutationId: str

class UpdateProjectNextPayload(GQLObject):
   clientMutationId: str

class UpdateProjectPayload(GQLObject):
   clientMutationId: str
   project: Project

class UpdateProjectV2DraftIssuePayload(GQLObject):
   clientMutationId: str
   draftIssue: DraftIssue

class UpdateProjectV2ItemFieldValueInput(GQLObject):
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   fieldId: ID ##NON NULL
   value: ProjectV2FieldValue ##NON NULL
   clientMutationId: str

class UpdateProjectV2ItemFieldValuePayload(GQLObject):
   clientMutationId: str
   projectV2Item: ProjectV2Item

class UpdateProjectV2ItemPositionPayload(GQLObject):
   clientMutationId: str
   items: ProjectV2ItemConnectionField

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
   message: str ##NON NULL
   octicon: str ##NON NULL
   viewer: User ##NON NULL
