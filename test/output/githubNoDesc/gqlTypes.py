from typing import Generic, Union
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gqlTypes import ID
from pygqlmap.src.gqlArgBuiltin import *
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
   teamIds: ID ##NON NULL ##LIST
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
   assigneeIds: ID ##NON NULL ##LIST
   milestoneId: ID
   labelIds: ID ##NON NULL ##LIST
   projectIds: ID ##NON NULL ##LIST
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
   assigneeIds: ID ##NON NULL ##LIST
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
   assigneeIds: ID ##NON NULL ##LIST
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
   assigneeIds: ID ##NON NULL ##LIST
   milestoneId: ID
   labelIds: ID ##NON NULL ##LIST
   state: IssueState
   projectIds: ID ##NON NULL ##LIST
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
   isRequired: YLXLJisRequired_isRequired_Field

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
   labelIds: ID ##NON NULL ##LIST
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
   assigneeIds: ID ##NON NULL ##LIST
   clientMutationId: str

class RejectDeploymentsInput(GQLObject):
   workflowRunId: ID ##NON NULL
   environmentIds: ID ##NON NULL ##LIST
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
   requiredStatusCheckContexts: str ##LIST
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
   labels: str ##NON NULL ##LIST
   mentioned: str
   milestone: str
   milestoneNumber: str
   since: DateTime
   states: IssueState ##NON NULL ##LIST
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
   gitIpAddresses: str ##LIST
   hookIpAddresses: str ##LIST
   importerIpAddresses: str ##LIST
   isPasswordAuthenticationVerifiable: bool ##NON NULL
   pagesIpAddresses: str ##LIST

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
   assigneeIds: ID ##NON NULL ##LIST
   milestoneId: ID
   labelIds: ID ##NON NULL ##LIST
   projectIds: ID ##NON NULL ##LIST
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
   environmentIds: ID ##NON NULL ##LIST
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
   assigneeIds: ID ##NON NULL ##LIST
   clientMutationId: str

class AddProjectDraftIssueInput(GQLObject):
   projectId: ID
   title: str
   body: str
   assigneeIds: ID ##NON NULL ##LIST
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
   userIds: ID ##NON NULL ##LIST
   role: OrganizationMemberRole
   clientMutationId: str

class AddDiscussionCommentInput(GQLObject):
   discussionId: ID ##NON NULL
   replyToId: ID
   body: str ##NON NULL
   clientMutationId: str

class AddAssigneesToAssignableInput(GQLObject):
   assignableId: ID ##NON NULL
   assigneeIds: ID ##NON NULL ##LIST
   clientMutationId: str

class AcceptTopicSuggestionInput(GQLObject):
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   clientMutationId: str

class AbortQueuedMigrationsPayload(GQLObject):
   clientMutationId: str
   success: bool

class UserEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('User', GQLObject) ## Circular Reference for User

class UserConnection(GQLObject):
   edges: UserEdge ##LIST
   nodes: NewType('User', GQLObject) ##LIST ## Circular Reference for User
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
   edges: BranchProtectionRuleConflictEdge ##LIST
   nodes: BranchProtectionRuleConflict ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class TeamEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Team', GQLObject) ## Circular Reference for Team

class TeamConnection(GQLObject):
   edges: TeamEdge ##LIST
   nodes: NewType('Team', GQLObject) ##LIST ## Circular Reference for Team
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class Mannequin(GQLObject):
   avatarUrl: EHZCXavatarUrl_URI_Field
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
   edges: ReactorEdge ##LIST
   nodes: Reactor ##LIST
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
   edges: ReactionEdge ##LIST
   nodes: Reaction ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   viewerHasReacted: bool ##NON NULL

class PLJHRreactions_ReactionConnection_Field(ReactionConnection):
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
   id: ID ##NON NULL
   reactionGroups: NewType('ReactionGroup', GQLObject) ##LIST ## Circular Reference for ReactionGroup
   reactions: PLJHRreactions_ReactionConnection_Field
   viewerCanReact: bool ##NON NULL

class ReactingUserEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User
   reactedAt: DateTime ##NON NULL

class ReactingUserConnection(GQLObject):
   edges: ReactingUserEdge ##LIST
   nodes: NewType('User', GQLObject) ##LIST ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class AZWXEreactors_ReactorConnection_Field(ReactorConnection):
   class ReactorConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ReactorConnectionArgs



class ReactionGroup(GQLObject):
   content: ReactionContent ##NON NULL
   createdAt: DateTime
   reactors: AZWXEreactors_ReactorConnection_Field
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
   edges: UserContentEditEdge ##LIST
   nodes: UserContentEdit ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class IPKKQreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class VDPNHuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



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
   reactionGroups: ReactionGroup ##LIST
   reactions: IPKKQreactions_ReactionConnection_Field
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: VDPNHuserContentEdits_UserContentEditConnection_Field
   viewerCanDelete: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL

class TeamDiscussionCommentEdge(GQLObject):
   cursor: str ##NON NULL
   node: TeamDiscussionComment

class TeamDiscussionCommentConnection(GQLObject):
   edges: TeamDiscussionCommentEdge ##LIST
   nodes: TeamDiscussionComment ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class NSSVKcomments_TeamDiscussionCommentConnection_Field(TeamDiscussionCommentConnection):
   class TeamDiscussionCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: TeamDiscussionCommentOrder
      fromComment: int

   _args: TeamDiscussionCommentConnectionArgs



class FKHJPreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class EBRXQuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class TeamDiscussion(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   bodyVersion: str ##NON NULL
   comments: NSSVKcomments_TeamDiscussionCommentConnection_Field
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
   reactionGroups: ReactionGroup ##LIST
   reactions: FKHJPreactions_ReactionConnection_Field
   resourcePath: URI ##NON NULL
   team: NewType('Team', GQLObject) ##NON NULL ## Circular Reference for Team
   title: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: EBRXQuserContentEdits_UserContentEditConnection_Field
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
   edges: TeamDiscussionEdge ##LIST
   nodes: TeamDiscussion ##LIST
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
   edges: OrganizationInvitationEdge ##LIST
   nodes: OrganizationInvitation ##LIST
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
   edges: UserStatusEdge ##LIST
   nodes: UserStatus ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class TeamMemberEdge(GQLObject):
   cursor: str ##NON NULL
   memberAccessResourcePath: URI ##NON NULL
   memberAccessUrl: URI ##NON NULL
   node: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User
   role: TeamMemberRole ##NON NULL

class TeamMemberConnection(GQLObject):
   edges: TeamMemberEdge ##LIST
   nodes: NewType('User', GQLObject) ##LIST ## Circular Reference for User
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
   edges: ProjectV2FieldConfigurationEdge ##LIST
   nodes: ProjectV2FieldConfiguration ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectNextField(GQLObject):
   id: ID ##NON NULL

class ProjectNextFieldEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectNextField

class ProjectNextFieldConnection(GQLObject):
   edges: ProjectNextFieldEdge ##LIST
   nodes: ProjectNextField ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class BranchProtectionRuleEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('BranchProtectionRule', GQLObject) ## Circular Reference for BranchProtectionRule

class BranchProtectionRuleConnection(GQLObject):
   edges: BranchProtectionRuleEdge ##LIST
   nodes: NewType('BranchProtectionRule', GQLObject) ##LIST ## Circular Reference for BranchProtectionRule
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
   permissionSources: PermissionSource ##LIST

class RepositoryCollaboratorConnection(GQLObject):
   edges: RepositoryCollaboratorEdge ##LIST
   nodes: NewType('User', GQLObject) ##LIST ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeployKeyEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeployKey

class DeployKeyConnection(GQLObject):
   edges: DeployKeyEdge ##LIST
   nodes: DeployKey ##LIST
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
   edges: DeploymentStatusEdge ##LIST
   nodes: DeploymentStatus ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DHAVLstatuses_DeploymentStatusConnection_Field(DeploymentStatusConnection):
   class DeploymentStatusConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentStatusConnectionArgs



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
   statuses: DHAVLstatuses_DeploymentStatusConnection_Field
   task: str
   updatedAt: DateTime ##NON NULL

class DeploymentEdge(GQLObject):
   cursor: str ##NON NULL
   node: Deployment

class DeploymentConnection(GQLObject):
   edges: DeploymentEdge ##LIST
   nodes: Deployment ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DiscussionCommentEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('DiscussionComment', GQLObject) ## Circular Reference for DiscussionComment

class DiscussionCommentConnection(GQLObject):
   edges: DiscussionCommentEdge ##LIST
   nodes: NewType('DiscussionComment', GQLObject) ##LIST ## Circular Reference for DiscussionComment
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class TRWRKreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class JJVGDreplies_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: DiscussionCommentConnectionArgs



class IXLTVuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



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
   reactionGroups: ReactionGroup ##LIST
   reactions: TRWRKreactions_ReactionConnection_Field
   replies: JJVGDreplies_DiscussionCommentConnection_Field
   replyTo: NewType('DiscussionComment', GQLObject) ## Circular Reference for DiscussionComment
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   upvoteCount: int ##NON NULL
   url: URI ##NON NULL
   userContentEdits: IXLTVuserContentEdits_UserContentEditConnection_Field
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
   edges: IssueEdge ##LIST
   nodes: NewType('Issue', GQLObject) ##LIST ## Circular Reference for Issue
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class AQJTGissues_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: IssueOrder
      labels: str ##NON NULL ##LIST
      states: IssueState ##NON NULL ##LIST
      filterBy: IssueFilters
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class NYPPVpullRequests_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject): 
      states: PullRequestState ##NON NULL ##LIST
      labels: str ##NON NULL ##LIST
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class Label(GQLObject):
   color: str ##NON NULL
   createdAt: DateTime
   description: str
   id: ID ##NON NULL
   isDefault: bool ##NON NULL
   issues: AQJTGissues_IssueConnection_Field
   name: str ##NON NULL
   pullRequests: NYPPVpullRequests_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository
   resourcePath: URI ##NON NULL
   updatedAt: DateTime
   url: URI ##NON NULL

class LabelEdge(GQLObject):
   cursor: str ##NON NULL
   node: Label

class LabelConnection(GQLObject):
   edges: LabelEdge ##LIST
   nodes: Label ##LIST
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
   edges: DiscussionPollOptionEdge ##LIST
   nodes: DiscussionPollOption ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ZRVYOoptions_DiscussionPollOptionConnection_Field(DiscussionPollOptionConnection):
   class DiscussionPollOptionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionPollOptionOrder

   _args: DiscussionPollOptionConnectionArgs



class DiscussionPoll(GQLObject):
   discussion: NewType('Discussion', GQLObject) ## Circular Reference for Discussion
   id: ID ##NON NULL
   options: ZRVYOoptions_DiscussionPollOptionConnection_Field
   question: str ##NON NULL
   totalVoteCount: int ##NON NULL
   viewerCanVote: bool ##NON NULL
   viewerHasVoted: bool ##NON NULL

class XRMEXcomments_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: DiscussionCommentConnectionArgs



class YVIPGlabels_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class MRSIYreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class JZJAKuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
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
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   category: DiscussionCategory ##NON NULL
   comments: XRMEXcomments_DiscussionCommentConnection_Field
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   labels: YVIPGlabels_LabelConnection_Field
   lastEditedAt: DateTime
   locked: bool ##NON NULL
   number: int ##NON NULL
   poll: DiscussionPoll
   publishedAt: DateTime
   reactionGroups: ReactionGroup ##LIST
   reactions: MRSIYreactions_ReactionConnection_Field
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository
   resourcePath: URI ##NON NULL
   title: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   upvoteCount: int ##NON NULL
   url: URI ##NON NULL
   userContentEdits: JZJAKuserContentEdits_UserContentEditConnection_Field
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
   edges: DiscussionCategoryEdge ##LIST
   nodes: DiscussionCategory ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DiscussionEdge(GQLObject):
   cursor: str ##NON NULL
   node: Discussion

class DiscussionConnection(GQLObject):
   edges: DiscussionEdge ##LIST
   nodes: Discussion ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeploymentReviewer(GQLObject): 
   pass

class DeploymentReviewerEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeploymentReviewer

class DeploymentReviewerConnection(GQLObject):
   edges: DeploymentReviewerEdge ##LIST
   nodes: DeploymentReviewer ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class QSKCRreviewers_DeploymentReviewerConnection_Field(DeploymentReviewerConnection):
   class DeploymentReviewerConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewerConnectionArgs



class DeploymentProtectionRule(GQLObject):
   databaseId: int
   reviewers: QSKCRreviewers_DeploymentReviewerConnection_Field
   timeout: int ##NON NULL
   type: DeploymentProtectionRuleType ##NON NULL

class DeploymentProtectionRuleEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeploymentProtectionRule

class DeploymentProtectionRuleConnection(GQLObject):
   edges: DeploymentProtectionRuleEdge ##LIST
   nodes: DeploymentProtectionRule ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class HZQBCprotectionRules_DeploymentProtectionRuleConnection_Field(DeploymentProtectionRuleConnection):
   class DeploymentProtectionRuleConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentProtectionRuleConnectionArgs



class Environment(GQLObject):
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   protectionRules: HZQBCprotectionRules_DeploymentProtectionRuleConnection_Field

class EnvironmentEdge(GQLObject):
   cursor: str ##NON NULL
   node: Environment

class EnvironmentConnection(GQLObject):
   edges: EnvironmentEdge ##LIST
   nodes: Environment ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class RepositoryEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Repository', GQLObject) ## Circular Reference for Repository

class RepositoryConnection(GQLObject):
   edges: RepositoryEdge ##LIST
   nodes: NewType('Repository', GQLObject) ##LIST ## Circular Reference for Repository
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
   edges: LanguageEdge ##LIST
   nodes: Language ##LIST
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
   edges: ReleaseAssetEdge ##LIST
   nodes: ReleaseAsset ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class AGDKAmentions_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class ETSOTreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class XIICZreleaseAssets_ReleaseAssetConnection_Field(ReleaseAssetConnection):
   class ReleaseAssetConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      name: str

   _args: ReleaseAssetConnectionArgs



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
   mentions: AGDKAmentions_UserConnection_Field
   name: str
   publishedAt: DateTime
   reactionGroups: ReactionGroup ##LIST
   reactions: ETSOTreactions_ReactionConnection_Field
   releaseAssets: XIICZreleaseAssets_ReleaseAssetConnection_Field
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository
   resourcePath: URI ##NON NULL
   shortDescriptionHTML: UCXZTshortDescriptionHTML_HTML_Field
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

class CDRQIissues_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: IssueOrder
      labels: str ##NON NULL ##LIST
      states: IssueState ##NON NULL ##LIST
      filterBy: IssueFilters
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class EBHSMpullRequests_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject): 
      states: PullRequestState ##NON NULL ##LIST
      labels: str ##NON NULL ##LIST
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class Milestone(GQLObject):
   closed: bool ##NON NULL
   closedAt: DateTime
   createdAt: DateTime ##NON NULL
   creator: Actor
   description: str
   dueOn: DateTime
   id: ID ##NON NULL
   issues: CDRQIissues_IssueConnection_Field
   number: int ##NON NULL
   progressPercentage: float ##NON NULL
   pullRequests: EBHSMpullRequests_PullRequestConnection_Field
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
   edges: MilestoneEdge ##LIST
   nodes: Milestone ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class GitObject(GQLObject):
   abbreviatedOid: str ##NON NULL
   commitResourcePath: URI ##NON NULL
   commitUrl: URI ##NON NULL
   id: ID ##NON NULL
   oid: GitObjectID ##NON NULL
   repository: NewType('Repository', GQLObject) ##NON NULL ## Circular Reference for Repository

class DKDBXrepositories_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: RepositoryAffiliation ##LIST
      ownerAffiliations: RepositoryAffiliation ##LIST
      isLocked: bool
      after: str
      before: str
      first: int
      last: int
      isFork: bool

   _args: RepositoryConnectionArgs



class OMWPDrepository_Repository_Field(Generic[Repository]):
   class RepositoryArgs(GQLArgsSet, GQLObject): 
      name: str ##NON NULL
      followRenames: bool

   _args: RepositoryArgs



class RepositoryOwner(GQLObject):
   avatarUrl: SLRSZavatarUrl_URI_Field
   id: ID ##NON NULL
   login: str ##NON NULL
   repositories: DKDBXrepositories_RepositoryConnection_Field
   repository: OMWPDrepository_Repository_Field ## Circular Reference for Repository
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
   edges: PackageFileEdge ##LIST
   nodes: PackageFile ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PMUVTfiles_PackageFileConnection_Field(PackageFileConnection):
   class PackageFileConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: PackageFileOrder
      after: str
      before: str
      first: int
      last: int

   _args: PackageFileConnectionArgs



class PackageVersion(GQLObject):
   files: PMUVTfiles_PackageFileConnection_Field
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
   edges: PackageVersionEdge ##LIST
   nodes: PackageVersion ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class WUCWQversion_PackageVersion_Field(PackageVersion):
   class PackageVersionArgs(GQLArgsSet, GQLObject): 
      version: str ##NON NULL

   _args: PackageVersionArgs



class TXITLversions_PackageVersionConnection_Field(PackageVersionConnection):
   class PackageVersionConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: PackageVersionOrder
      after: str
      before: str
      first: int
      last: int

   _args: PackageVersionConnectionArgs



class Package(GQLObject):
   id: ID ##NON NULL
   latestVersion: PackageVersion
   name: str ##NON NULL
   packageType: PackageType ##NON NULL
   repository: Repository
   statistics: PackageStatistics
   version: WUCWQversion_PackageVersion_Field
   versions: TXITLversions_PackageVersionConnection_Field

class PackageEdge(GQLObject):
   cursor: str ##NON NULL
   node: Package

class PackageConnection(GQLObject):
   edges: PackageEdge ##LIST
   nodes: Package ##LIST
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
   edges: PinnedDiscussionEdge ##LIST
   nodes: PinnedDiscussion ##LIST
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
   edges: PinnedIssueEdge ##LIST
   nodes: PinnedIssue ##LIST
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
   edges: ProjectCardEdge ##LIST
   nodes: ProjectCard ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ZEGEBcards_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      archivedStates: ProjectCardArchivedState ##LIST

   _args: ProjectCardConnectionArgs



class ProjectColumn(GQLObject):
   cards: ZEGEBcards_ProjectCardConnection_Field
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
   edges: ProjectColumnEdge ##LIST
   nodes: ProjectColumn ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Project', GQLObject) ## Circular Reference for Project

class ProjectConnection(GQLObject):
   edges: ProjectEdge ##LIST
   nodes: NewType('Project', GQLObject) ##LIST ## Circular Reference for Project
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class KVPPCproject_Project_Field(Generic[Project]):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectArgs



class QYKYZprojects_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: ProjectOrder
      search: str
      states: ProjectState ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class ProjectOwner(GQLObject):
   id: ID ##NON NULL
   project: KVPPCproject_Project_Field ## Circular Reference for Project
   projects: QYKYZprojects_ProjectConnection_Field
   projectsResourcePath: URI ##NON NULL
   projectsUrl: URI ##NON NULL
   viewerCanCreateProjects: bool ##NON NULL

class PLIMPcolumns_ProjectColumnConnection_Field(ProjectColumnConnection):
   class ProjectColumnConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ProjectColumnConnectionArgs



class OGXGEpendingCards_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      archivedStates: ProjectCardArchivedState ##LIST

   _args: ProjectCardConnectionArgs



class Project(GQLObject):
   body: str
   bodyHTML: HTML ##NON NULL
   closed: bool ##NON NULL
   closedAt: DateTime
   columns: PLIMPcolumns_ProjectColumnConnection_Field
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   number: int ##NON NULL
   owner: ProjectOwner ##NON NULL
   pendingCards: OGXGEpendingCards_ProjectCardConnection_Field
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
   edges: ProjectNextEdge ##LIST
   nodes: NewType('ProjectNext', GQLObject) ##LIST ## Circular Reference for ProjectNext
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2Edge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('ProjectV2', GQLObject) ## Circular Reference for ProjectV2

class ProjectV2Connection(GQLObject):
   edges: ProjectV2Edge ##LIST
   nodes: NewType('ProjectV2', GQLObject) ##LIST ## Circular Reference for ProjectV2
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
   edges: RefEdge ##LIST
   nodes: NewType('Ref', GQLObject) ##LIST ## Circular Reference for Ref
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ReleaseEdge(GQLObject):
   cursor: str ##NON NULL
   node: Release

class ReleaseConnection(GQLObject):
   edges: ReleaseEdge ##LIST
   nodes: Release ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class StargazerEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User
   starredAt: DateTime ##NON NULL

class StargazerConnection(GQLObject):
   edges: StargazerEdge ##LIST
   nodes: NewType('User', GQLObject) ##LIST ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SIEZLrelatedTopics_Topic_Field(Generic[Topic]):
   class TopicArgs(GQLArgsSet, GQLObject): 
      first: int

   _args: TopicArgs



class SNPZMrepositories_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: RepositoryAffiliation ##LIST
      ownerAffiliations: RepositoryAffiliation ##LIST
      isLocked: bool
      after: str
      before: str
      first: int
      last: int
      sponsorableOnly: bool

   _args: RepositoryConnectionArgs



class AZUJRstargazers_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class Topic(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   relatedTopics: SIEZLrelatedTopics_Topic_Field ## Circular Reference for Topic
   repositories: SNPZMrepositories_RepositoryConnection_Field
   stargazerCount: int ##NON NULL
   stargazers: AZUJRstargazers_StargazerConnection_Field
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
   edges: RepositoryTopicEdge ##LIST
   nodes: RepositoryTopic ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SubmoduleEdge(GQLObject):
   cursor: str ##NON NULL
   node: Submodule

class SubmoduleConnection(GQLObject):
   edges: SubmoduleEdge ##LIST
   nodes: Submodule ##LIST
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
   edges: CWEEdge ##LIST
   nodes: CWE ##LIST
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
   edges: SecurityVulnerabilityEdge ##LIST
   nodes: SecurityVulnerability ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class AOYCFcwes_CWEConnection_Field(CWEConnection):
   class CWEConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: CWEConnectionArgs



class DVTAXvulnerabilities_SecurityVulnerabilityConnection_Field(SecurityVulnerabilityConnection):
   class SecurityVulnerabilityConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: SecurityVulnerabilityOrder
      ecosystem: SecurityAdvisoryEcosystem
      package: str
      severities: SecurityAdvisorySeverity ##NON NULL ##LIST
      classifications: SecurityAdvisoryClassification ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: SecurityVulnerabilityConnectionArgs



class SecurityAdvisory(GQLObject):
   classification: SecurityAdvisoryClassification ##NON NULL
   cvss: CVSS ##NON NULL
   cwes: AOYCFcwes_CWEConnection_Field
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
   vulnerabilities: DVTAXvulnerabilities_SecurityVulnerabilityConnection_Field
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
   edges: RepositoryVulnerabilityAlertEdge ##LIST
   nodes: RepositoryVulnerabilityAlert ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class RAGWIassignableUsers_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class VTCFTbranchProtectionRules_BranchProtectionRuleConnection_Field(BranchProtectionRuleConnection):
   class BranchProtectionRuleConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: BranchProtectionRuleConnectionArgs



class OJVQZcodeowners_RepositoryCodeowners_Field(RepositoryCodeowners):
   class RepositoryCodeownersArgs(GQLArgsSet, GQLObject): 
      refName: str

   _args: RepositoryCodeownersArgs



class HGDEYcollaborators_RepositoryCollaboratorConnection_Field(RepositoryCollaboratorConnection):
   class RepositoryCollaboratorConnectionArgs(GQLArgsSet, GQLObject): 
      affiliation: CollaboratorAffiliation
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryCollaboratorConnectionArgs



class QYFRTcommitComments_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class ZGEMRdeployKeys_DeployKeyConnection_Field(DeployKeyConnection):
   class DeployKeyConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: DeployKeyConnectionArgs



class CWTBVdeployments_DeploymentConnection_Field(DeploymentConnection):
   class DeploymentConnectionArgs(GQLArgsSet, GQLObject): 
      environments: str ##NON NULL ##LIST
      orderBy: DeploymentOrder
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentConnectionArgs



class DUOZYdiscussion_Discussion_Field(Discussion):
   class DiscussionArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: DiscussionArgs



class LDALBdiscussionCategories_DiscussionCategoryConnection_Field(DiscussionCategoryConnection):
   class DiscussionCategoryConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      filterByAssignable: bool

   _args: DiscussionCategoryConnectionArgs



class DSPBHdiscussionCategory_DiscussionCategory_Field(DiscussionCategory):
   class DiscussionCategoryArgs(GQLArgsSet, GQLObject): 
      slug: str ##NON NULL

   _args: DiscussionCategoryArgs



class DELEOdiscussions_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      categoryId: ID
      orderBy: DiscussionOrder

   _args: DiscussionConnectionArgs



class DFFWNenvironment_Environment_Field(Environment):
   class EnvironmentArgs(GQLArgsSet, GQLObject): 
      name: str ##NON NULL

   _args: EnvironmentArgs



class QMRVEenvironments_EnvironmentConnection_Field(EnvironmentConnection):
   class EnvironmentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: EnvironmentConnectionArgs



class YVORPforks_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: RepositoryAffiliation ##LIST
      ownerAffiliations: RepositoryAffiliation ##LIST
      isLocked: bool
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryConnectionArgs



class MUXGEissue_Issue_Field(Generic[Issue]):
   class IssueArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: IssueArgs



class IWIIPissueOrPullRequest_IssueOrPullRequest_Field(IssueOrPullRequest):
   class IssueOrPullRequestArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: IssueOrPullRequestArgs



class AVTQRissues_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: IssueOrder
      labels: str ##NON NULL ##LIST
      states: IssueState ##NON NULL ##LIST
      filterBy: IssueFilters
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class CTBOPlabel_Label_Field(Label):
   class LabelArgs(GQLArgsSet, GQLObject): 
      name: str ##NON NULL

   _args: LabelArgs



class JYWEMlabels_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int
      query: str

   _args: LabelConnectionArgs



class RRGGTlanguages_LanguageConnection_Field(LanguageConnection):
   class LanguageConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: LanguageOrder

   _args: LanguageConnectionArgs



class LDIQTmentionableUsers_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class DLMZDmilestone_Milestone_Field(Milestone):
   class MilestoneArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: MilestoneArgs



class JLHMPmilestones_MilestoneConnection_Field(MilestoneConnection):
   class MilestoneConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      states: MilestoneState ##NON NULL ##LIST
      orderBy: MilestoneOrder
      query: str

   _args: MilestoneConnectionArgs



class QLZCOobject_GitObject_Field(GitObject):
   class GitObjectArgs(GQLArgsSet, GQLObject): 
      oid: GitObjectID
      expression: str

   _args: GitObjectArgs



class VFMCBpackages_PackageConnection_Field(PackageConnection):
   class PackageConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      names: str ##LIST
      repositoryId: ID
      packageType: PackageType
      orderBy: PackageOrder

   _args: PackageConnectionArgs



class DNLACpinnedDiscussions_PinnedDiscussionConnection_Field(PinnedDiscussionConnection):
   class PinnedDiscussionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: PinnedDiscussionConnectionArgs



class SWDFRpinnedIssues_PinnedIssueConnection_Field(PinnedIssueConnection):
   class PinnedIssueConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: PinnedIssueConnectionArgs



class SBYVHproject_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectArgs



class PQZEEprojectV2_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectV2Args



class RWMWDprojects_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: ProjectOrder
      search: str
      states: ProjectState ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class QPOBPprojectsV2_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: ProjectV2Order

   _args: ProjectV2ConnectionArgs



class DKTJGpullRequest_PullRequest_Field(Generic[PullRequest]):
   class PullRequestArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: PullRequestArgs



class RTSYBpullRequests_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject): 
      states: PullRequestState ##NON NULL ##LIST
      labels: str ##NON NULL ##LIST
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class FHFOFrecentProjects_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class BALQOref_Ref_Field(Generic[Ref]):
   class RefArgs(GQLArgsSet, GQLObject): 
      qualifiedName: str ##NON NULL

   _args: RefArgs



class DEWUQrefs_RefConnection_Field(RefConnection):
   class RefConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      after: str
      before: str
      first: int
      last: int
      refPrefix: str ##NON NULL
      direction: OrderDirection
      orderBy: RefOrder

   _args: RefConnectionArgs



class TTKVOrelease_Release_Field(Release):
   class ReleaseArgs(GQLArgsSet, GQLObject): 
      tagName: str ##NON NULL

   _args: ReleaseArgs



class ZWOWZreleases_ReleaseConnection_Field(ReleaseConnection):
   class ReleaseConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ReleaseOrder

   _args: ReleaseConnectionArgs



class OQUCVrepositoryTopics_RepositoryTopicConnection_Field(RepositoryTopicConnection):
   class RepositoryTopicConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryTopicConnectionArgs



class GZIXZstargazers_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class SXAXAsubmodules_SubmoduleConnection_Field(SubmoduleConnection):
   class SubmoduleConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: SubmoduleConnectionArgs



class XPJLMvulnerabilityAlerts_RepositoryVulnerabilityAlertConnection_Field(RepositoryVulnerabilityAlertConnection):
   class RepositoryVulnerabilityAlertConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      states: RepositoryVulnerabilityAlertState ##NON NULL ##LIST
      dependencyScopes: RepositoryVulnerabilityAlertDependencyScope ##NON NULL ##LIST

   _args: RepositoryVulnerabilityAlertConnectionArgs



class ENRITwatchers_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class Repository(GQLObject):
   allowUpdateBranch: bool ##NON NULL
   assignableUsers: RAGWIassignableUsers_UserConnection_Field
   autoMergeAllowed: bool ##NON NULL
   branchProtectionRules: VTCFTbranchProtectionRules_BranchProtectionRuleConnection_Field
   codeOfConduct: CodeOfConduct
   codeowners: OJVQZcodeowners_RepositoryCodeowners_Field
   collaborators: HGDEYcollaborators_RepositoryCollaboratorConnection_Field
   commitComments: QYFRTcommitComments_CommitCommentConnection_Field ## Circular Reference for CommitCommentConnection
   contactLinks: RepositoryContactLink ##LIST
   createdAt: DateTime ##NON NULL
   databaseId: int
   defaultBranchRef: NewType('Ref', GQLObject) ## Circular Reference for Ref
   deleteBranchOnMerge: bool ##NON NULL
   deployKeys: ZGEMRdeployKeys_DeployKeyConnection_Field
   deployments: CWTBVdeployments_DeploymentConnection_Field
   description: str
   descriptionHTML: HTML ##NON NULL
   discussion: DUOZYdiscussion_Discussion_Field
   discussionCategories: LDALBdiscussionCategories_DiscussionCategoryConnection_Field
   discussionCategory: DSPBHdiscussionCategory_DiscussionCategory_Field
   discussions: DELEOdiscussions_DiscussionConnection_Field
   diskUsage: int
   environment: DFFWNenvironment_Environment_Field
   environments: QMRVEenvironments_EnvironmentConnection_Field
   forkCount: int ##NON NULL
   forkingAllowed: bool ##NON NULL
   forks: YVORPforks_RepositoryConnection_Field
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
   issue: MUXGEissue_Issue_Field ## Circular Reference for Issue
   issueOrPullRequest: IWIIPissueOrPullRequest_IssueOrPullRequest_Field
   issueTemplates: IssueTemplate ##LIST
   issues: AVTQRissues_IssueConnection_Field
   label: CTBOPlabel_Label_Field
   labels: JYWEMlabels_LabelConnection_Field
   languages: RRGGTlanguages_LanguageConnection_Field
   latestRelease: Release
   licenseInfo: License
   lockReason: RepositoryLockReason
   mentionableUsers: LDIQTmentionableUsers_UserConnection_Field
   mergeCommitAllowed: bool ##NON NULL
   mergeCommitMessage: MergeCommitMessage ##NON NULL
   mergeCommitTitle: MergeCommitTitle ##NON NULL
   milestone: DLMZDmilestone_Milestone_Field
   milestones: JLHMPmilestones_MilestoneConnection_Field
   mirrorUrl: URI
   name: str ##NON NULL
   nameWithOwner: str ##NON NULL
   object: QLZCOobject_GitObject_Field
   openGraphImageUrl: URI ##NON NULL
   owner: RepositoryOwner ##NON NULL
   packages: VFMCBpackages_PackageConnection_Field
   parent: Repository
   pinnedDiscussions: DNLACpinnedDiscussions_PinnedDiscussionConnection_Field
   pinnedIssues: SWDFRpinnedIssues_PinnedIssueConnection_Field
   primaryLanguage: Language
   project: SBYVHproject_Project_Field
   projectV2: PQZEEprojectV2_ProjectV2_Field ## Circular Reference for ProjectV2
   projects: RWMWDprojects_ProjectConnection_Field
   projectsResourcePath: URI ##NON NULL
   projectsUrl: URI ##NON NULL
   projectsV2: QPOBPprojectsV2_ProjectV2Connection_Field
   pullRequest: DKTJGpullRequest_PullRequest_Field ## Circular Reference for PullRequest
   pullRequestTemplates: PullRequestTemplate ##LIST
   pullRequests: RTSYBpullRequests_PullRequestConnection_Field
   pushedAt: DateTime
   rebaseMergeAllowed: bool ##NON NULL
   recentProjects: FHFOFrecentProjects_ProjectV2Connection_Field
   ref: BALQOref_Ref_Field ## Circular Reference for Ref
   refs: DEWUQrefs_RefConnection_Field
   release: TTKVOrelease_Release_Field
   releases: ZWOWZreleases_ReleaseConnection_Field
   repositoryTopics: OQUCVrepositoryTopics_RepositoryTopicConnection_Field
   resourcePath: URI ##NON NULL
   securityPolicyUrl: URI
   shortDescriptionHTML: LSYLJshortDescriptionHTML_HTML_Field
   squashMergeAllowed: bool ##NON NULL
   squashMergeCommitMessage: SquashMergeCommitMessage ##NON NULL
   squashMergeCommitTitle: SquashMergeCommitTitle ##NON NULL
   sshUrl: GitSSHRemote ##NON NULL
   stargazerCount: int ##NON NULL
   stargazers: GZIXZstargazers_StargazerConnection_Field
   submodules: SXAXAsubmodules_SubmoduleConnection_Field
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
   viewerPossibleCommitEmails: str ##LIST
   viewerSubscription: SubscriptionState
   visibility: RepositoryVisibility ##NON NULL
   vulnerabilityAlerts: XPJLMvulnerabilityAlerts_RepositoryVulnerabilityAlertConnection_Field
   watchers: ENRITwatchers_UserConnection_Field
   webCommitSignoffRequired: bool ##NON NULL

class AGQLJreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class XRKNPuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



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
   reactionGroups: ReactionGroup ##LIST
   reactions: AGQLJreactions_ReactionConnection_Field
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: XRKNPuserContentEdits_UserContentEditConnection_Field
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
   edges: IssueCommentEdge ##LIST
   nodes: IssueComment ##LIST
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
   edges: LinkedBranchEdge ##LIST
   nodes: LinkedBranch ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class BBKQUassignees_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class Assignable(GQLObject):
   assignees: BBKQUassignees_UserConnection_Field

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

class PUYBLlabels_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class Labelable(GQLObject):
   labels: PUYBLlabels_LabelConnection_Field

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
   edges: IssueTimelineItemEdge ##LIST
   nodes: IssueTimelineItem ##LIST
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
   edges: IssueTimelineItemsEdge ##LIST
   filteredCount: int ##NON NULL
   nodes: IssueTimelineItems ##LIST
   pageCount: int ##NON NULL
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   updatedAt: DateTime ##NON NULL

class SHVVDassignees_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class VZYAJcomments_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class VCZJEhovercard_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject): 
      includeNotificationContexts: bool

   _args: HovercardArgs



class AMMFVlabels_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class RLKRIlinkedBranches_LinkedBranchConnection_Field(LinkedBranchConnection):
   class LinkedBranchConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: LinkedBranchConnectionArgs



class WQSFCparticipants_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class CPGYAprojectCards_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      archivedStates: ProjectCardArchivedState ##LIST

   _args: ProjectCardConnectionArgs



class SQTJSprojectItems_ProjectV2ItemConnection_Field(Generic[ProjectV2ItemConnection]):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject): 
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class DSIVKprojectNextItems_ProjectNextItemConnection_Field(Generic[ProjectNextItemConnection]):
   class ProjectNextItemConnectionArgs(GQLArgsSet, GQLObject): 
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: ProjectNextItemConnectionArgs



class FBUDXprojectV2_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectV2Args



class ADEZWprojectsV2_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class NCZRQreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class OVUBRtimelineItems_IssueTimelineItemsConnection_Field(IssueTimelineItemsConnection):
   class IssueTimelineItemsConnectionArgs(GQLArgsSet, GQLObject): 
      since: DateTime
      skip: int
      itemTypes: IssueTimelineItemsItemType ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: IssueTimelineItemsConnectionArgs



class KYFXKtrackedInIssues_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class JBQZRtrackedIssues_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class RDMOZuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class Issue(GQLObject):
   activeLockReason: LockReason
   assignees: SHVVDassignees_UserConnection_Field
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyResourcePath: URI ##NON NULL
   bodyText: str ##NON NULL
   bodyUrl: URI ##NON NULL
   closed: bool ##NON NULL
   closedAt: DateTime
   comments: VZYAJcomments_IssueCommentConnection_Field
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   editor: Actor
   hovercard: VCZJEhovercard_Hovercard_Field
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   isPinned: bool
   isReadByViewer: bool
   labels: AMMFVlabels_LabelConnection_Field
   lastEditedAt: DateTime
   linkedBranches: RLKRIlinkedBranches_LinkedBranchConnection_Field
   locked: bool ##NON NULL
   milestone: Milestone
   number: int ##NON NULL
   participants: WQSFCparticipants_UserConnection_Field
   projectCards: CPGYAprojectCards_ProjectCardConnection_Field
   projectItems: SQTJSprojectItems_ProjectV2ItemConnection_Field ## Circular Reference for ProjectV2ItemConnection
   projectNextItems: DSIVKprojectNextItems_ProjectNextItemConnection_Field ## Circular Reference for ProjectNextItemConnection
   projectV2: FBUDXprojectV2_ProjectV2_Field
   projectsV2: ADEZWprojectsV2_ProjectV2Connection_Field
   publishedAt: DateTime
   reactionGroups: ReactionGroup ##LIST
   reactions: NCZRQreactions_ReactionConnection_Field
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   state: IssueState ##NON NULL
   stateReason: IssueStateReason
   timelineItems: OVUBRtimelineItems_IssueTimelineItemsConnection_Field
   title: str ##NON NULL
   titleHTML: str ##NON NULL
   trackedInIssues: KYFXKtrackedInIssues_IssueConnection_Field
   trackedIssues: JBQZRtrackedIssues_IssueConnection_Field
   trackedIssuesCount: MEBIVtrackedIssuesCount_trackedIssuesCount_Field
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: RDMOZuserContentEdits_UserContentEditConnection_Field
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
   edges: ProjectNextItemFieldValueEdge ##LIST
   nodes: ProjectNextItemFieldValue ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectNextItem(GQLObject):
   id: ID ##NON NULL

class ProjectNextItemEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectNextItem

class ProjectNextItemConnection(GQLObject):
   edges: ProjectNextItemEdge ##LIST
   nodes: ProjectNextItem ##LIST
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
   edges: ProjectViewEdge ##LIST
   nodes: ProjectView ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectNext(GQLObject):
   closedAt: DateTime
   id: ID ##NON NULL
   viewerCanUpdate: bool ##NON NULL

class GNXCMassignees_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class XDNNSprojectV2Items_ProjectV2ItemConnection_Field(Generic[ProjectV2ItemConnection]):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class JZXIDprojectsV2_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class DraftIssue(GQLObject):
   assignees: GNXCMassignees_UserConnection_Field
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   createdAt: DateTime ##NON NULL
   creator: Actor
   id: ID ##NON NULL
   project: ProjectNext ##NON NULL
   projectItem: ProjectNextItem ##NON NULL
   projectV2Items: XDNNSprojectV2Items_ProjectV2ItemConnection_Field
   projectsV2: JZXIDprojectsV2_ProjectV2Connection_Field
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

class MQDGIlabels_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class ProjectV2ItemFieldLabelValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   labels: MQDGIlabels_LabelConnection_Field

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

class WNRWApullRequests_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: PullRequestOrder

   _args: PullRequestConnectionArgs



class ProjectV2ItemFieldPullRequestValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   pullRequests: WNRWApullRequests_PullRequestConnection_Field

class ProjectV2ItemFieldRepositoryValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   repository: Repository

class RequestedReviewer(GQLObject): 
   pass

class RequestedReviewerEdge(GQLObject):
   cursor: str ##NON NULL
   node: RequestedReviewer

class RequestedReviewerConnection(GQLObject):
   edges: RequestedReviewerEdge ##LIST
   nodes: RequestedReviewer ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DNNNIreviewers_RequestedReviewerConnection_Field(RequestedReviewerConnection):
   class RequestedReviewerConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: RequestedReviewerConnectionArgs



class ProjectV2ItemFieldReviewerValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   reviewers: DNNNIreviewers_RequestedReviewerConnection_Field

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

class SDRLZusers_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class ProjectV2ItemFieldUserValue(GQLObject):
   field: ProjectV2FieldConfiguration ##NON NULL
   users: SDRLZusers_UserConnection_Field

class ProjectV2ItemFieldValue(GQLObject): 
   pass

class ProjectV2ItemFieldValueEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2ItemFieldValue

class ProjectV2ItemFieldValueConnection(GQLObject):
   edges: ProjectV2ItemFieldValueEdge ##LIST
   nodes: ProjectV2ItemFieldValue ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ZEIHOfieldValueByName_ProjectV2ItemFieldValue_Field(ProjectV2ItemFieldValue):
   class ProjectV2ItemFieldValueArgs(GQLArgsSet, GQLObject): 
      name: str ##NON NULL

   _args: ProjectV2ItemFieldValueArgs



class HTSUYfieldValues_ProjectV2ItemFieldValueConnection_Field(ProjectV2ItemFieldValueConnection):
   class ProjectV2ItemFieldValueConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ItemFieldValueOrder

   _args: ProjectV2ItemFieldValueConnectionArgs



class ProjectV2Item(GQLObject):
   content: ProjectV2ItemContent
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   fieldValueByName: ZEIHOfieldValueByName_ProjectV2ItemFieldValue_Field
   fieldValues: HTSUYfieldValues_ProjectV2ItemFieldValueConnection_Field
   id: ID ##NON NULL
   isArchived: bool ##NON NULL
   project: ProjectV2 ##NON NULL
   type: ProjectV2ItemType ##NON NULL
   updatedAt: DateTime ##NON NULL

class ProjectV2ItemEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2Item

class ProjectV2ItemConnection(GQLObject):
   edges: ProjectV2ItemEdge ##LIST
   nodes: ProjectV2Item ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class JMLYHprojectV2_ProjectV2_Field(Generic[ProjectV2]):
   class ProjectV2Args(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectV2Args



class ERPOGprojectsV2_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class ProjectV2Owner(GQLObject):
   id: ID ##NON NULL
   projectV2: JMLYHprojectV2_ProjectV2_Field
   projectsV2: ERPOGprojectsV2_ProjectV2Connection_Field

class ProjectV2FieldEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2Field

class ProjectV2FieldConnection(GQLObject):
   edges: ProjectV2FieldEdge ##LIST
   nodes: ProjectV2Field ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2SortBy(GQLObject):
   direction: OrderDirection ##NON NULL
   field: ProjectV2Field ##NON NULL

class ProjectV2SortByEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2SortBy

class ProjectV2SortByConnection(GQLObject):
   edges: ProjectV2SortByEdge ##LIST
   nodes: ProjectV2SortBy ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ProjectV2SortByField(GQLObject):
   direction: OrderDirection ##NON NULL
   field: ProjectV2FieldConfiguration ##NON NULL

class ProjectV2SortByFieldEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2SortByField

class ProjectV2SortByFieldConnection(GQLObject):
   edges: ProjectV2SortByFieldEdge ##LIST
   nodes: ProjectV2SortByField ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class FQGGBfields_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class TYSWAgroupByFields_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class YDCFLsortByFields_ProjectV2SortByFieldConnection_Field(ProjectV2SortByFieldConnection):
   class ProjectV2SortByFieldConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2SortByFieldConnectionArgs



class HYKHBverticalGroupByFields_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class ProjectV2View(GQLObject):
   createdAt: DateTime ##NON NULL
   databaseId: int
   fields: FQGGBfields_ProjectV2FieldConfigurationConnection_Field
   filter: str
   groupByFields: TYSWAgroupByFields_ProjectV2FieldConfigurationConnection_Field
   id: ID ##NON NULL
   layout: ProjectV2ViewLayout ##NON NULL
   name: str ##NON NULL
   number: int ##NON NULL
   project: ProjectV2 ##NON NULL
   sortByFields: YDCFLsortByFields_ProjectV2SortByFieldConnection_Field
   updatedAt: DateTime ##NON NULL
   verticalGroupByFields: HYKHBverticalGroupByFields_ProjectV2FieldConfigurationConnection_Field

class ProjectV2ViewEdge(GQLObject):
   cursor: str ##NON NULL
   node: ProjectV2View

class ProjectV2ViewConnection(GQLObject):
   edges: ProjectV2ViewEdge ##LIST
   nodes: ProjectV2View ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class IYJXVfield_ProjectV2FieldConfiguration_Field(ProjectV2FieldConfiguration):
   class ProjectV2FieldConfigurationArgs(GQLArgsSet, GQLObject): 
      name: str ##NON NULL

   _args: ProjectV2FieldConfigurationArgs



class FIPVBfields_ProjectV2FieldConfigurationConnection_Field(ProjectV2FieldConfigurationConnection):
   class ProjectV2FieldConfigurationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2FieldOrder

   _args: ProjectV2FieldConfigurationConnectionArgs



class ADGTAitems_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ItemOrder

   _args: ProjectV2ItemConnectionArgs



class FHPIOrepositories_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: RepositoryOrder

   _args: RepositoryConnectionArgs



class AHKKHteams_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: TeamOrder

   _args: TeamConnectionArgs



class KMIXDview_ProjectV2View_Field(ProjectV2View):
   class ProjectV2ViewArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectV2ViewArgs



class AZGJBviews_ProjectV2ViewConnection_Field(ProjectV2ViewConnection):
   class ProjectV2ViewConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2ViewOrder

   _args: ProjectV2ViewConnectionArgs



class ProjectV2(GQLObject):
   closed: bool ##NON NULL
   closedAt: DateTime
   createdAt: DateTime ##NON NULL
   creator: Actor
   databaseId: int
   field: IYJXVfield_ProjectV2FieldConfiguration_Field
   fields: FIPVBfields_ProjectV2FieldConfigurationConnection_Field
   id: ID ##NON NULL
   items: ADGTAitems_ProjectV2ItemConnection_Field
   number: int ##NON NULL
   owner: ProjectV2Owner ##NON NULL
   public: bool ##NON NULL
   readme: str
   repositories: FHPIOrepositories_RepositoryConnection_Field
   resourcePath: URI ##NON NULL
   shortDescription: str
   teams: AHKKHteams_TeamConnection_Field
   title: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   view: KMIXDview_ProjectV2View_Field
   viewerCanUpdate: bool ##NON NULL
   views: AZGJBviews_ProjectV2ViewConnection_Field

class TeamRepositoryEdge(GQLObject):
   cursor: str ##NON NULL
   node: Repository ##NON NULL
   permission: RepositoryPermission ##NON NULL

class TeamRepositoryConnection(GQLObject):
   edges: TeamRepositoryEdge ##LIST
   nodes: Repository ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SYRVGancestors_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class ZPPPAchildTeams_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: TeamOrder
      userLogins: str ##NON NULL ##LIST
      immediateOnly: bool
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class RMZBQdiscussion_TeamDiscussion_Field(TeamDiscussion):
   class TeamDiscussionArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: TeamDiscussionArgs



class JNWBGdiscussions_TeamDiscussionConnection_Field(TeamDiscussionConnection):
   class TeamDiscussionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      isPinned: bool
      orderBy: TeamDiscussionOrder

   _args: TeamDiscussionConnectionArgs



class FESYBinvitations_OrganizationInvitationConnection_Field(OrganizationInvitationConnection):
   class OrganizationInvitationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationInvitationConnectionArgs



class ZHNBFmemberStatuses_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class TUQHFmembers_TeamMemberConnection_Field(TeamMemberConnection):
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



class CXNPXprojectV2_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectV2Args



class GQDDZprojectsV2_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ProjectV2Order
      filterBy: ProjectV2Filters
      query: str

   _args: ProjectV2ConnectionArgs



class YYFTSrepositories_TeamRepositoryConnection_Field(TeamRepositoryConnection):
   class TeamRepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: TeamRepositoryOrder

   _args: TeamRepositoryConnectionArgs



class Team(GQLObject):
   ancestors: SYRVGancestors_TeamConnection_Field
   avatarUrl: YZFUJavatarUrl_URI_Field
   childTeams: ZPPPAchildTeams_TeamConnection_Field
   combinedSlug: str ##NON NULL
   createdAt: DateTime ##NON NULL
   databaseId: int
   description: str
   discussion: RMZBQdiscussion_TeamDiscussion_Field
   discussions: JNWBGdiscussions_TeamDiscussionConnection_Field
   discussionsResourcePath: URI ##NON NULL
   discussionsUrl: URI ##NON NULL
   editTeamResourcePath: URI ##NON NULL
   editTeamUrl: URI ##NON NULL
   id: ID ##NON NULL
   invitations: FESYBinvitations_OrganizationInvitationConnection_Field
   memberStatuses: ZHNBFmemberStatuses_UserStatusConnection_Field
   members: TUQHFmembers_TeamMemberConnection_Field
   membersResourcePath: URI ##NON NULL
   membersUrl: URI ##NON NULL
   name: str ##NON NULL
   newTeamResourcePath: URI ##NON NULL
   newTeamUrl: URI ##NON NULL
   organization: NewType('Organization', GQLObject) ##NON NULL ## Circular Reference for Organization
   parentTeam: NewType('Team', GQLObject) ## Circular Reference for Team
   privacy: TeamPrivacy ##NON NULL
   projectV2: CXNPXprojectV2_ProjectV2_Field
   projectsV2: GQDDZprojectsV2_ProjectV2Connection_Field
   repositories: YYFTSrepositories_TeamRepositoryConnection_Field
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
   edges: BypassForcePushAllowanceEdge ##LIST
   nodes: BypassForcePushAllowance ##LIST
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
   edges: BypassPullRequestAllowanceEdge ##LIST
   nodes: BypassPullRequestAllowance ##LIST
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
   edges: PushAllowanceEdge ##LIST
   nodes: PushAllowance ##LIST
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
   edges: ReviewDismissalAllowanceEdge ##LIST
   nodes: ReviewDismissalAllowance ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class JZVWXbranchProtectionRuleConflicts_BranchProtectionRuleConflictConnection_Field(BranchProtectionRuleConflictConnection):
   class BranchProtectionRuleConflictConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: BranchProtectionRuleConflictConnectionArgs



class JPHVRbypassForcePushAllowances_BypassForcePushAllowanceConnection_Field(BypassForcePushAllowanceConnection):
   class BypassForcePushAllowanceConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: BypassForcePushAllowanceConnectionArgs



class RHMPVbypassPullRequestAllowances_BypassPullRequestAllowanceConnection_Field(BypassPullRequestAllowanceConnection):
   class BypassPullRequestAllowanceConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: BypassPullRequestAllowanceConnectionArgs



class KFYEFmatchingRefs_RefConnection_Field(RefConnection):
   class RefConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      after: str
      before: str
      first: int
      last: int

   _args: RefConnectionArgs



class JQCTBpushAllowances_PushAllowanceConnection_Field(PushAllowanceConnection):
   class PushAllowanceConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: PushAllowanceConnectionArgs



class OZHYZreviewDismissalAllowances_ReviewDismissalAllowanceConnection_Field(ReviewDismissalAllowanceConnection):
   class ReviewDismissalAllowanceConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ReviewDismissalAllowanceConnectionArgs



class BranchProtectionRule(GQLObject):
   allowsDeletions: bool ##NON NULL
   allowsForcePushes: bool ##NON NULL
   blocksCreations: bool ##NON NULL
   branchProtectionRuleConflicts: JZVWXbranchProtectionRuleConflicts_BranchProtectionRuleConflictConnection_Field
   bypassForcePushAllowances: JPHVRbypassForcePushAllowances_BypassForcePushAllowanceConnection_Field
   bypassPullRequestAllowances: RHMPVbypassPullRequestAllowances_BypassPullRequestAllowanceConnection_Field
   creator: Actor
   databaseId: int
   dismissesStaleReviews: bool ##NON NULL
   id: ID ##NON NULL
   isAdminEnforced: bool ##NON NULL
   lockAllowsFetchAndMerge: bool ##NON NULL
   lockBranch: bool ##NON NULL
   matchingRefs: KFYEFmatchingRefs_RefConnection_Field
   pattern: str ##NON NULL
   pushAllowances: JQCTBpushAllowances_PushAllowanceConnection_Field
   repository: Repository
   requireLastPushApproval: bool ##NON NULL
   requiredApprovingReviewCount: int
   requiredStatusCheckContexts: str ##LIST
   requiredStatusChecks: RequiredStatusCheckDescription ##LIST
   requiresApprovingReviews: bool ##NON NULL
   requiresCodeOwnerReviews: bool ##NON NULL
   requiresCommitSignatures: bool ##NON NULL
   requiresConversationResolution: bool ##NON NULL
   requiresLinearHistory: bool ##NON NULL
   requiresStatusChecks: bool ##NON NULL
   requiresStrictStatusChecks: bool ##NON NULL
   restrictsPushes: bool ##NON NULL
   restrictsReviewDismissals: bool ##NON NULL
   reviewDismissalAllowances: OZHYZreviewDismissalAllowances_ReviewDismissalAllowanceConnection_Field

class CommitEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Commit', GQLObject) ## Circular Reference for Commit

class ComparisonCommitConnection(GQLObject):
   authorCount: int ##NON NULL
   edges: CommitEdge ##LIST
   nodes: NewType('Commit', GQLObject) ##LIST ## Circular Reference for Commit
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SPMKYcommits_ComparisonCommitConnection_Field(ComparisonCommitConnection):
   class ComparisonCommitConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ComparisonCommitConnectionArgs



class Comparison(GQLObject):
   aheadBy: int ##NON NULL
   baseTarget: GitObject ##NON NULL
   behindBy: int ##NON NULL
   commits: SPMKYcommits_ComparisonCommitConnection_Field
   headTarget: GitObject ##NON NULL
   id: ID ##NON NULL
   status: ComparisonStatus ##NON NULL

class SGWMYassociatedPullRequests_PullRequestConnection_Field(Generic[PullRequestConnection]):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject): 
      states: PullRequestState ##NON NULL ##LIST
      labels: str ##NON NULL ##LIST
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class CGVYLcompare_Comparison_Field(Comparison):
   class ComparisonArgs(GQLArgsSet, GQLObject): 
      headRef: str ##NON NULL

   _args: ComparisonArgs



class Ref(GQLObject):
   associatedPullRequests: SGWMYassociatedPullRequests_PullRequestConnection_Field ## Circular Reference for PullRequestConnection
   branchProtectionRule: BranchProtectionRule
   compare: CGVYLcompare_Comparison_Field
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
   edges: PullRequestCommitEdge ##LIST
   nodes: PullRequestCommit ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PullRequestChangedFileEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequestChangedFile

class PullRequestChangedFileConnection(GQLObject):
   edges: PullRequestChangedFileEdge ##LIST
   nodes: PullRequestChangedFile ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class MPKBSreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class NBBAQuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



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
   reactionGroups: ReactionGroup ##LIST
   reactions: MPKBSreactions_ReactionConnection_Field
   replyTo: NewType('PullRequestReviewComment', GQLObject) ## Circular Reference for PullRequestReviewComment
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   state: PullRequestReviewCommentState ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: NBBAQuserContentEdits_UserContentEditConnection_Field
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
   edges: PullRequestReviewCommentEdge ##LIST
   nodes: PullRequestReviewComment ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class GNYQRcomments_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewCommentConnectionArgs



class VXQPAonBehalfOf_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class BTZEGreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class AVOEJuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class PullRequestReview(GQLObject):
   author: Actor
   authorAssociation: CommentAuthorAssociation ##NON NULL
   authorCanPushToRepository: bool ##NON NULL
   body: str ##NON NULL
   bodyHTML: HTML ##NON NULL
   bodyText: str ##NON NULL
   comments: GNYQRcomments_PullRequestReviewCommentConnection_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   editor: Actor
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   lastEditedAt: DateTime
   onBehalfOf: VXQPAonBehalfOf_TeamConnection_Field
   publishedAt: DateTime
   pullRequest: PullRequest ##NON NULL
   reactionGroups: ReactionGroup ##LIST
   reactions: BTZEGreactions_ReactionConnection_Field
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   state: PullRequestReviewState ##NON NULL
   submittedAt: DateTime
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: AVOEJuserContentEdits_UserContentEditConnection_Field
   viewerCanDelete: bool ##NON NULL
   viewerCanReact: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL

class PullRequestReviewEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequestReview

class PullRequestReviewConnection(GQLObject):
   edges: PullRequestReviewEdge ##LIST
   nodes: PullRequestReview ##LIST
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
   edges: ReviewRequestEdge ##LIST
   nodes: ReviewRequest ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class KFTONcomments_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      skip: int

   _args: PullRequestReviewCommentConnectionArgs



class PullRequestReviewThread(GQLObject):
   comments: KFTONcomments_PullRequestReviewCommentConnection_Field
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
   edges: PullRequestReviewThreadEdge ##LIST
   nodes: PullRequestReviewThread ##LIST
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

class RDAILcomments_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class CommitCommentThread(GQLObject):
   comments: RDAILcomments_CommitCommentConnection_Field
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
   edges: PullRequestTimelineItemEdge ##LIST
   nodes: PullRequestTimelineItem ##LIST
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

class ITKDMcomments_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class PullRequestCommitCommentThread(GQLObject):
   comments: ITKDMcomments_CommitCommentConnection_Field
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
   edges: PullRequestTimelineItemsEdge ##LIST
   filteredCount: int ##NON NULL
   nodes: PullRequestTimelineItems ##LIST
   pageCount: int ##NON NULL
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   updatedAt: DateTime ##NON NULL

class BFMVRassignees_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class BOCSRclosingIssuesReferences_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject): 
      userLinkedOnly: bool
      after: str
      before: str
      first: int
      last: int
      orderBy: IssueOrder

   _args: IssueConnectionArgs



class UVLFTcomments_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class AYETYcommits_PullRequestCommitConnection_Field(PullRequestCommitConnection):
   class PullRequestCommitConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestCommitConnectionArgs



class HVRZSfiles_PullRequestChangedFileConnection_Field(PullRequestChangedFileConnection):
   class PullRequestChangedFileConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestChangedFileConnectionArgs



class CTBLWhovercard_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject): 
      includeNotificationContexts: bool

   _args: HovercardArgs



class OUXQWlabels_LabelConnection_Field(LabelConnection):
   class LabelConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: LabelOrder
      after: str
      before: str
      first: int
      last: int

   _args: LabelConnectionArgs



class IAKBRlatestOpinionatedReviews_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      writersOnly: bool

   _args: PullRequestReviewConnectionArgs



class NIETBlatestReviews_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewConnectionArgs



class KLIOQparticipants_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class YUFQHprojectCards_ProjectCardConnection_Field(ProjectCardConnection):
   class ProjectCardConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      archivedStates: ProjectCardArchivedState ##LIST

   _args: ProjectCardConnectionArgs



class MDEODprojectItems_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject): 
      includeArchived: bool
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class TPMYEprojectV2_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectV2Args



class IDEBGprojectsV2_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class VSORRreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class XJXELreviewRequests_ReviewRequestConnection_Field(ReviewRequestConnection):
   class ReviewRequestConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ReviewRequestConnectionArgs



class HTTZHreviewThreads_PullRequestReviewThreadConnection_Field(PullRequestReviewThreadConnection):
   class PullRequestReviewThreadConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestReviewThreadConnectionArgs



class LOIRTreviews_PullRequestReviewConnection_Field(PullRequestReviewConnection):
   class PullRequestReviewConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      states: PullRequestReviewState ##NON NULL ##LIST
      author: str

   _args: PullRequestReviewConnectionArgs



class KQMLBtimelineItems_PullRequestTimelineItemsConnection_Field(PullRequestTimelineItemsConnection):
   class PullRequestTimelineItemsConnectionArgs(GQLArgsSet, GQLObject): 
      since: DateTime
      skip: int
      itemTypes: PullRequestTimelineItemsItemType ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestTimelineItemsConnectionArgs



class SUQUHuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



class PullRequest(GQLObject):
   activeLockReason: LockReason
   additions: int ##NON NULL
   assignees: BFMVRassignees_UserConnection_Field
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
   closingIssuesReferences: BOCSRclosingIssuesReferences_IssueConnection_Field
   comments: UVLFTcomments_IssueCommentConnection_Field
   commits: AYETYcommits_PullRequestCommitConnection_Field
   createdAt: DateTime ##NON NULL
   createdViaEmail: bool ##NON NULL
   databaseId: int
   deletions: int ##NON NULL
   editor: Actor
   files: HVRZSfiles_PullRequestChangedFileConnection_Field
   headRef: Ref
   headRefName: str ##NON NULL
   headRefOid: GitObjectID ##NON NULL
   headRepository: Repository
   headRepositoryOwner: RepositoryOwner
   hovercard: CTBLWhovercard_Hovercard_Field
   id: ID ##NON NULL
   includesCreatedEdit: bool ##NON NULL
   isCrossRepository: bool ##NON NULL
   isDraft: bool ##NON NULL
   isReadByViewer: bool
   labels: OUXQWlabels_LabelConnection_Field
   lastEditedAt: DateTime
   latestOpinionatedReviews: IAKBRlatestOpinionatedReviews_PullRequestReviewConnection_Field
   latestReviews: NIETBlatestReviews_PullRequestReviewConnection_Field
   locked: bool ##NON NULL
   maintainerCanModify: bool ##NON NULL
   mergeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   mergeable: MergeableState ##NON NULL
   merged: bool ##NON NULL
   mergedAt: DateTime
   mergedBy: Actor
   milestone: Milestone
   number: int ##NON NULL
   participants: KLIOQparticipants_UserConnection_Field
   permalink: URI ##NON NULL
   potentialMergeCommit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   projectCards: YUFQHprojectCards_ProjectCardConnection_Field
   projectItems: MDEODprojectItems_ProjectV2ItemConnection_Field
   projectV2: TPMYEprojectV2_ProjectV2_Field
   projectsV2: IDEBGprojectsV2_ProjectV2Connection_Field
   publishedAt: DateTime
   reactionGroups: ReactionGroup ##LIST
   reactions: VSORRreactions_ReactionConnection_Field
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   revertResourcePath: URI ##NON NULL
   revertUrl: URI ##NON NULL
   reviewDecision: PullRequestReviewDecision
   reviewRequests: XJXELreviewRequests_ReviewRequestConnection_Field
   reviewThreads: HTTZHreviewThreads_PullRequestReviewThreadConnection_Field
   reviews: LOIRTreviews_PullRequestReviewConnection_Field
   state: PullRequestState ##NON NULL
   suggestedReviewers: SuggestedReviewer ##NON NULL
   timelineItems: KQMLBtimelineItems_PullRequestTimelineItemsConnection_Field
   title: str ##NON NULL
   titleHTML: HTML ##NON NULL
   totalCommentsCount: int
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: SUQUHuserContentEdits_UserContentEditConnection_Field
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
   viewerMergeBodyText: LZSEYviewerMergeBodyText_viewerMergeBodyText_Field
   viewerMergeHeadlineText: UALRCviewerMergeHeadlineText_viewerMergeHeadlineText_Field
   viewerSubscription: SubscriptionState

class PullRequestEdge(GQLObject):
   cursor: str ##NON NULL
   node: PullRequest

class PullRequestConnection(GQLObject):
   edges: PullRequestEdge ##LIST
   nodes: PullRequest ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class GitActor(GQLObject):
   avatarUrl: YLNTWavatarUrl_URI_Field
   date: GitTimestamp
   email: str
   name: str
   user: NewType('User', GQLObject) ## Circular Reference for User

class GitActorEdge(GQLObject):
   cursor: str ##NON NULL
   node: GitActor

class GitActorConnection(GQLObject):
   edges: GitActorEdge ##LIST
   nodes: GitActor ##LIST
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
   edges: CheckSuiteEdge ##LIST
   nodes: NewType('CheckSuite', GQLObject) ##LIST ## Circular Reference for CheckSuite
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
   edges: CommitEdge ##LIST
   nodes: NewType('Commit', GQLObject) ##LIST ## Circular Reference for Commit
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CommitConnection(GQLObject):
   edges: CommitEdge ##LIST
   nodes: NewType('Commit', GQLObject) ##LIST ## Circular Reference for Commit
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
   edges: CheckAnnotationEdge ##LIST
   nodes: CheckAnnotation ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class CLDKQreviewers_DeploymentReviewerConnection_Field(DeploymentReviewerConnection):
   class DeploymentReviewerConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewerConnectionArgs



class DeploymentRequest(GQLObject):
   currentUserCanApprove: bool ##NON NULL
   environment: Environment ##NON NULL
   reviewers: CLDKQreviewers_DeploymentReviewerConnection_Field
   waitTimer: int ##NON NULL
   waitTimerStartedAt: DateTime

class CheckStepEdge(GQLObject):
   cursor: str ##NON NULL
   node: CheckStep

class CheckStepConnection(GQLObject):
   edges: CheckStepEdge ##LIST
   nodes: CheckStep ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class OOJREannotations_CheckAnnotationConnection_Field(CheckAnnotationConnection):
   class CheckAnnotationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: CheckAnnotationConnectionArgs



class COCRJsteps_CheckStepConnection_Field(CheckStepConnection):
   class CheckStepConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      number: int

   _args: CheckStepConnectionArgs



class CheckRun(GQLObject):
   annotations: OOJREannotations_CheckAnnotationConnection_Field
   checkSuite: NewType('CheckSuite', GQLObject) ##NON NULL ## Circular Reference for CheckSuite
   completedAt: DateTime
   conclusion: CheckConclusionState
   databaseId: int
   deployment: Deployment
   detailsUrl: URI
   externalId: str
   id: ID ##NON NULL
   isRequired: WPLMYisRequired_isRequired_Field
   name: str ##NON NULL
   pendingDeploymentRequest: DeploymentRequest
   permalink: URI ##NON NULL
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   startedAt: DateTime
   status: CheckStatusState ##NON NULL
   steps: COCRJsteps_CheckStepConnection_Field
   summary: str
   text: str
   title: str
   url: URI ##NON NULL

class StatusContext(GQLObject):
   avatarUrl: SLMPZavatarUrl_URI_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   context: str ##NON NULL
   createdAt: DateTime ##NON NULL
   creator: Actor
   description: str
   id: ID ##NON NULL
   isRequired: SYFLBisRequired_isRequired_Field
   state: StatusState ##NON NULL
   targetUrl: URI

class StatusCheckRollupContext(GQLObject): 
   pass

class StatusCheckRollupContextEdge(GQLObject):
   cursor: str ##NON NULL
   node: StatusCheckRollupContext

class StatusCheckRollupContextConnection(GQLObject):
   checkRunCount: int ##NON NULL
   checkRunCountsByState: CheckRunStateCount ##LIST
   edges: StatusCheckRollupContextEdge ##LIST
   nodes: StatusCheckRollupContext ##LIST
   pageInfo: PageInfo ##NON NULL
   statusContextCount: int ##NON NULL
   statusContextCountsByState: StatusContextStateCount ##LIST
   totalCount: int ##NON NULL

class LIXJHcombinedContexts_StatusCheckRollupContextConnection_Field(StatusCheckRollupContextConnection):
   class StatusCheckRollupContextConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: StatusCheckRollupContextConnectionArgs



class HHMSZcontext_StatusContext_Field(StatusContext):
   class StatusContextArgs(GQLArgsSet, GQLObject): 
      name: str ##NON NULL

   _args: StatusContextArgs



class Status(GQLObject):
   combinedContexts: LIXJHcombinedContexts_StatusCheckRollupContextConnection_Field
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   context: HHMSZcontext_StatusContext_Field
   contexts: StatusContext ##NON NULL
   id: ID ##NON NULL
   state: StatusState ##NON NULL

class WSMEXcontexts_StatusCheckRollupContextConnection_Field(StatusCheckRollupContextConnection):
   class StatusCheckRollupContextConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: StatusCheckRollupContextConnectionArgs



class StatusCheckRollup(GQLObject):
   commit: NewType('Commit', GQLObject) ## Circular Reference for Commit
   contexts: WSMEXcontexts_StatusCheckRollupContextConnection_Field
   id: ID ##NON NULL
   state: StatusState ##NON NULL

class Tree(GQLObject):
   abbreviatedOid: str ##NON NULL
   commitResourcePath: URI ##NON NULL
   commitUrl: URI ##NON NULL
   entries: TreeEntry ##LIST
   id: ID ##NON NULL
   oid: GitObjectID ##NON NULL
   repository: Repository ##NON NULL

class SICFAassociatedPullRequests_PullRequestConnection_Field(PullRequestConnection):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: PullRequestOrder

   _args: PullRequestConnectionArgs



class JPAXWauthors_GitActorConnection_Field(GitActorConnection):
   class GitActorConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: GitActorConnectionArgs



class WUHVKblame_Blame_Field(Blame):
   class BlameArgs(GQLArgsSet, GQLObject): 
      path: str ##NON NULL

   _args: BlameArgs



class JSVIGcheckSuites_CheckSuiteConnection_Field(CheckSuiteConnection):
   class CheckSuiteConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      filterBy: CheckSuiteFilter

   _args: CheckSuiteConnectionArgs



class VZWNBcomments_CommitCommentConnection_Field(Generic[CommitCommentConnection]):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class DQKATdeployments_DeploymentConnection_Field(DeploymentConnection):
   class DeploymentConnectionArgs(GQLArgsSet, GQLObject): 
      environments: str ##NON NULL ##LIST
      orderBy: DeploymentOrder
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentConnectionArgs



class ZTMSQfile_TreeEntry_Field(TreeEntry):
   class TreeEntryArgs(GQLArgsSet, GQLObject): 
      path: str ##NON NULL

   _args: TreeEntryArgs



class WNBNOhistory_CommitHistoryConnection_Field(CommitHistoryConnection):
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



class RPRYBparents_CommitConnection_Field(CommitConnection):
   class CommitConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: CommitConnectionArgs



class FZHDJsubmodules_SubmoduleConnection_Field(SubmoduleConnection):
   class SubmoduleConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: SubmoduleConnectionArgs



class Commit(GQLObject):
   abbreviatedOid: str ##NON NULL
   additions: int ##NON NULL
   associatedPullRequests: SICFAassociatedPullRequests_PullRequestConnection_Field
   author: GitActor
   authoredByCommitter: bool ##NON NULL
   authoredDate: DateTime ##NON NULL
   authors: JPAXWauthors_GitActorConnection_Field
   blame: WUHVKblame_Blame_Field
   changedFilesIfAvailable: int
   checkSuites: JSVIGcheckSuites_CheckSuiteConnection_Field
   comments: VZWNBcomments_CommitCommentConnection_Field
   commitResourcePath: URI ##NON NULL
   commitUrl: URI ##NON NULL
   committedDate: DateTime ##NON NULL
   committedViaWeb: bool ##NON NULL
   committer: GitActor
   deletions: int ##NON NULL
   deployments: DQKATdeployments_DeploymentConnection_Field
   file: ZTMSQfile_TreeEntry_Field
   history: WNBNOhistory_CommitHistoryConnection_Field
   id: ID ##NON NULL
   message: str ##NON NULL
   messageBody: str ##NON NULL
   messageBodyHTML: HTML ##NON NULL
   messageHeadline: str ##NON NULL
   messageHeadlineHTML: HTML ##NON NULL
   oid: GitObjectID ##NON NULL
   onBehalfOf: NewType('Organization', GQLObject) ## Circular Reference for Organization
   parents: RPRYBparents_CommitConnection_Field
   pushedDate: DateTime
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   signature: GitSignature
   status: Status
   statusCheckRollup: StatusCheckRollup
   submodules: FZHDJsubmodules_SubmoduleConnection_Field
   tarballUrl: URI ##NON NULL
   tree: Tree ##NON NULL
   treeResourcePath: URI ##NON NULL
   treeUrl: URI ##NON NULL
   url: URI ##NON NULL
   viewerCanSubscribe: bool ##NON NULL
   viewerSubscription: SubscriptionState
   zipballUrl: URI ##NON NULL

class WWYKQreactions_ReactionConnection_Field(ReactionConnection):
   class ReactionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      content: ReactionContent
      orderBy: ReactionOrder

   _args: ReactionConnectionArgs



class MBSIOuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



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
   reactionGroups: ReactionGroup ##LIST
   reactions: WWYKQreactions_ReactionConnection_Field
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   userContentEdits: MBSIOuserContentEdits_UserContentEditConnection_Field
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
   edges: CommitCommentEdge ##LIST
   nodes: CommitComment ##LIST
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
   edges: CreatedCommitContributionEdge ##LIST
   nodes: CreatedCommitContribution ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class FHGACcontributions_CreatedCommitContributionConnection_Field(CreatedCommitContributionConnection):
   class CreatedCommitContributionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: CommitContributionOrder

   _args: CreatedCommitContributionConnectionArgs



class CommitContributionsByRepository(GQLObject):
   contributions: FHGACcontributions_CreatedCommitContributionConnection_Field
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
   edges: CreatedIssueContributionEdge ##LIST
   nodes: CreatedIssueContribution ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class BQOFScontributions_CreatedIssueContributionConnection_Field(CreatedIssueContributionConnection):
   class CreatedIssueContributionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedIssueContributionConnectionArgs



class IssueContributionsByRepository(GQLObject):
   contributions: BQOFScontributions_CreatedIssueContributionConnection_Field
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
   edges: CreatedPullRequestContributionEdge ##LIST
   nodes: CreatedPullRequestContribution ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ZTNRXcontributions_CreatedPullRequestContributionConnection_Field(CreatedPullRequestContributionConnection):
   class CreatedPullRequestContributionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestContributionConnectionArgs



class PullRequestContributionsByRepository(GQLObject):
   contributions: ZTNRXcontributions_CreatedPullRequestContributionConnection_Field
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
   edges: CreatedPullRequestReviewContributionEdge ##LIST
   nodes: CreatedPullRequestReviewContribution ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class HQKLAcontributions_CreatedPullRequestReviewContributionConnection_Field(CreatedPullRequestReviewContributionConnection):
   class CreatedPullRequestReviewContributionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestReviewContributionConnectionArgs



class PullRequestReviewContributionsByRepository(GQLObject):
   contributions: HQKLAcontributions_CreatedPullRequestReviewContributionConnection_Field
   repository: Repository ##NON NULL

class CreatedRepositoryContributionEdge(GQLObject):
   cursor: str ##NON NULL
   node: CreatedRepositoryContribution

class CreatedRepositoryContributionConnection(GQLObject):
   edges: CreatedRepositoryContributionEdge ##LIST
   nodes: CreatedRepositoryContribution ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EEBDTcommitContributionsByRepository_CommitContributionsByRepository_Field(CommitContributionsByRepository):
   class CommitContributionsByRepositoryArgs(GQLArgsSet, GQLObject): 
      maxRepositories: int

   _args: CommitContributionsByRepositoryArgs



class VTMJHissueContributions_CreatedIssueContributionConnection_Field(CreatedIssueContributionConnection):
   class CreatedIssueContributionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      excludePopular: bool
      orderBy: ContributionOrder

   _args: CreatedIssueContributionConnectionArgs



class WKETWissueContributionsByRepository_IssueContributionsByRepository_Field(IssueContributionsByRepository):
   class IssueContributionsByRepositoryArgs(GQLArgsSet, GQLObject): 
      maxRepositories: int
      excludeFirst: bool
      excludePopular: bool

   _args: IssueContributionsByRepositoryArgs



class KEFELpullRequestContributions_CreatedPullRequestContributionConnection_Field(CreatedPullRequestContributionConnection):
   class CreatedPullRequestContributionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      excludePopular: bool
      orderBy: ContributionOrder

   _args: CreatedPullRequestContributionConnectionArgs



class PKSDMpullRequestContributionsByRepository_PullRequestContributionsByRepository_Field(PullRequestContributionsByRepository):
   class PullRequestContributionsByRepositoryArgs(GQLArgsSet, GQLObject): 
      maxRepositories: int
      excludeFirst: bool
      excludePopular: bool

   _args: PullRequestContributionsByRepositoryArgs



class OZJDUpullRequestReviewContributions_CreatedPullRequestReviewContributionConnection_Field(CreatedPullRequestReviewContributionConnection):
   class CreatedPullRequestReviewContributionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: ContributionOrder

   _args: CreatedPullRequestReviewContributionConnectionArgs



class KDGFJpullRequestReviewContributionsByRepository_PullRequestReviewContributionsByRepository_Field(PullRequestReviewContributionsByRepository):
   class PullRequestReviewContributionsByRepositoryArgs(GQLArgsSet, GQLObject): 
      maxRepositories: int

   _args: PullRequestReviewContributionsByRepositoryArgs



class UALOHrepositoryContributions_CreatedRepositoryContributionConnection_Field(CreatedRepositoryContributionConnection):
   class CreatedRepositoryContributionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      excludeFirst: bool
      orderBy: ContributionOrder

   _args: CreatedRepositoryContributionConnectionArgs



class ContributionsCollection(GQLObject):
   commitContributionsByRepository: EEBDTcommitContributionsByRepository_CommitContributionsByRepository_Field
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
   issueContributions: VTMJHissueContributions_CreatedIssueContributionConnection_Field
   issueContributionsByRepository: WKETWissueContributionsByRepository_IssueContributionsByRepository_Field
   joinedGitHubContribution: JoinedGitHubContribution
   latestRestrictedContributionDate: Date
   mostRecentCollectionWithActivity: NewType('ContributionsCollection', GQLObject) ## Circular Reference for ContributionsCollection
   mostRecentCollectionWithoutActivity: NewType('ContributionsCollection', GQLObject) ## Circular Reference for ContributionsCollection
   popularIssueContribution: CreatedIssueContribution
   popularPullRequestContribution: CreatedPullRequestContribution
   pullRequestContributions: KEFELpullRequestContributions_CreatedPullRequestContributionConnection_Field
   pullRequestContributionsByRepository: PKSDMpullRequestContributionsByRepository_PullRequestContributionsByRepository_Field
   pullRequestReviewContributions: OZJDUpullRequestReviewContributions_CreatedPullRequestReviewContributionConnection_Field
   pullRequestReviewContributionsByRepository: KDGFJpullRequestReviewContributionsByRepository_PullRequestReviewContributionsByRepository_Field
   repositoryContributions: UALOHrepositoryContributions_CreatedRepositoryContributionConnection_Field
   restrictedContributionsCount: int ##NON NULL
   startedAt: DateTime ##NON NULL
   totalCommitContributions: int ##NON NULL
   totalIssueContributions: FVWZAtotalIssueContributions_totalIssueContributions_Field
   totalPullRequestContributions: PURNVtotalPullRequestContributions_totalPullRequestContributions_Field
   totalPullRequestReviewContributions: int ##NON NULL
   totalRepositoriesWithContributedCommits: int ##NON NULL
   totalRepositoriesWithContributedIssues: LYJBOtotalRepositoriesWithContributedIssues_totalRepositoriesWithContributedIssues_Field
   totalRepositoriesWithContributedPullRequestReviews: int ##NON NULL
   totalRepositoriesWithContributedPullRequests: KYOCTtotalRepositoriesWithContributedPullRequests_totalRepositoriesWithContributedPullRequests_Field
   totalRepositoryContributions: PWKGRtotalRepositoryContributions_totalRepositoryContributions_Field
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class FollowerConnection(GQLObject):
   edges: UserEdge ##LIST
   nodes: NewType('User', GQLObject) ##LIST ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class FollowingConnection(GQLObject):
   edges: UserEdge ##LIST
   nodes: NewType('User', GQLObject) ##LIST ## Circular Reference for User
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class JFYHMuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



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
   userContentEdits: JFYHMuserContentEdits_UserContentEditConnection_Field
   viewerCanDelete: bool ##NON NULL
   viewerCanMinimize: bool ##NON NULL
   viewerCanUpdate: bool ##NON NULL
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL
   viewerDidAuthor: bool ##NON NULL

class GistCommentEdge(GQLObject):
   cursor: str ##NON NULL
   node: GistComment

class GistCommentConnection(GQLObject):
   edges: GistCommentEdge ##LIST
   nodes: GistComment ##LIST
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
   text: KLNHFtext_text_Field

class GistEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Gist', GQLObject) ## Circular Reference for Gist

class GistConnection(GQLObject):
   edges: GistEdge ##LIST
   nodes: NewType('Gist', GQLObject) ##LIST ## Circular Reference for Gist
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class HEQYZcomments_GistCommentConnection_Field(GistCommentConnection):
   class GistCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: GistCommentConnectionArgs



class NITQCfiles_GistFile_Field(GistFile):
   class GistFileArgs(GQLArgsSet, GQLObject): 
      limit: int
      oid: GitObjectID

   _args: GistFileArgs



class HJTURforks_GistConnection_Field(GistConnection):
   class GistConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: GistOrder

   _args: GistConnectionArgs



class OGXQAstargazers_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class Gist(GQLObject):
   comments: HEQYZcomments_GistCommentConnection_Field
   createdAt: DateTime ##NON NULL
   description: str
   files: NITQCfiles_GistFile_Field
   forks: HJTURforks_GistConnection_Field
   id: ID ##NON NULL
   isFork: bool ##NON NULL
   isPublic: bool ##NON NULL
   name: str ##NON NULL
   owner: RepositoryOwner
   pushedAt: DateTime
   resourcePath: URI ##NON NULL
   stargazerCount: int ##NON NULL
   stargazers: OGXQAstargazers_StargazerConnection_Field
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   viewerHasStarred: bool ##NON NULL

class PinnableItem(GQLObject): 
   pass

class PinnableItemEdge(GQLObject):
   cursor: str ##NON NULL
   node: PinnableItem

class PinnableItemConnection(GQLObject):
   edges: PinnableItemEdge ##LIST
   nodes: PinnableItem ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EMHXEitems_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class ProfileItemShowcase(GQLObject):
   hasPinnedItems: bool ##NON NULL
   items: EMHXEitems_PinnableItemConnection_Field

class OrganizationEdge(GQLObject):
   cursor: str ##NON NULL
   node: NewType('Organization', GQLObject) ## Circular Reference for Organization

class OrganizationConnection(GQLObject):
   edges: OrganizationEdge ##LIST
   nodes: NewType('Organization', GQLObject) ##LIST ## Circular Reference for Organization
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class PublicKeyEdge(GQLObject):
   cursor: str ##NON NULL
   node: PublicKey

class PublicKeyConnection(GQLObject):
   edges: PublicKeyEdge ##LIST
   nodes: PublicKey ##LIST
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
   edges: SavedReplyEdge ##LIST
   nodes: SavedReply ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class Sponsor(GQLObject): 
   pass

class SponsorEdge(GQLObject):
   cursor: str ##NON NULL
   node: Sponsor

class SponsorConnection(GQLObject):
   edges: SponsorEdge ##LIST
   nodes: Sponsor ##LIST
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
   edges: SponsorsTierEdge ##LIST
   nodes: NewType('SponsorsTier', GQLObject) ##LIST ## Circular Reference for SponsorsTier
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class LRJUHfeaturedItems_SponsorsListingFeaturedItem_Field(SponsorsListingFeaturedItem):
   class SponsorsListingFeaturedItemArgs(GQLArgsSet, GQLObject): 
      featureableTypes: SponsorsListingFeaturedItemFeatureableType ##NON NULL ##LIST

   _args: SponsorsListingFeaturedItemArgs



class DEYRBtiers_SponsorsTierConnection_Field(SponsorsTierConnection):
   class SponsorsTierConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorsTierOrder

   _args: SponsorsTierConnectionArgs



class SponsorsListing(GQLObject):
   activeGoal: SponsorsGoal
   billingCountryOrRegion: str
   contactEmailAddress: str
   createdAt: DateTime ##NON NULL
   dashboardResourcePath: URI ##NON NULL
   dashboardUrl: URI ##NON NULL
   featuredItems: LRJUHfeaturedItems_SponsorsListingFeaturedItem_Field
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
   tiers: DEYRBtiers_SponsorsTierConnection_Field
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
   edges: SponsorshipNewsletterEdge ##LIST
   nodes: SponsorshipNewsletter ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DQRZBsponsoring_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class XIYBSsponsors_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class YUNYUsponsorsActivities_SponsorsActivityConnection_Field(Generic[SponsorsActivityConnection]):
   class SponsorsActivityConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      period: SponsorsActivityPeriod
      since: DateTime
      until: DateTime
      orderBy: SponsorsActivityOrder
      actions: SponsorsActivityAction ##NON NULL ##LIST
      includeAsSponsor: bool

   _args: SponsorsActivityConnectionArgs



class FXUNVsponsorshipNewsletters_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class USRTDsponsorshipsAsMaintainer_SponsorshipConnection_Field(Generic[SponsorshipConnection]):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder

   _args: SponsorshipConnectionArgs



class NZNCNsponsorshipsAsSponsor_SponsorshipConnection_Field(Generic[SponsorshipConnection]):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipOrder
      maintainerLogins: str ##NON NULL ##LIST

   _args: SponsorshipConnectionArgs



class Sponsorable(GQLObject):
   estimatedNextSponsorsPayoutInCents: int ##NON NULL
   hasSponsorsListing: bool ##NON NULL
   isSponsoredBy: YGBMEisSponsoredBy_isSponsoredBy_Field
   isSponsoringViewer: bool ##NON NULL
   monthlyEstimatedSponsorsIncomeInCents: int ##NON NULL
   sponsoring: DQRZBsponsoring_SponsorConnection_Field
   sponsors: XIYBSsponsors_SponsorConnection_Field
   sponsorsActivities: YUNYUsponsorsActivities_SponsorsActivityConnection_Field ## Circular Reference for SponsorsActivityConnection
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: NewType('Sponsorship', GQLObject) ## Circular Reference for Sponsorship
   sponsorshipForViewerAsSponsorable: NewType('Sponsorship', GQLObject) ## Circular Reference for Sponsorship
   sponsorshipNewsletters: FXUNVsponsorshipNewsletters_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: USRTDsponsorshipsAsMaintainer_SponsorshipConnection_Field ## Circular Reference for SponsorshipConnection
   sponsorshipsAsSponsor: NZNCNsponsorshipsAsSponsor_SponsorshipConnection_Field ## Circular Reference for SponsorshipConnection
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
   edges: SponsorshipEdge ##LIST
   nodes: Sponsorship ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   totalRecurringMonthlyPriceInCents: int ##NON NULL
   totalRecurringMonthlyPriceInDollars: int ##NON NULL

class EIEFTsponsorships_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder

   _args: SponsorshipConnectionArgs



class SponsorsTierAdminInfo(GQLObject):
   isDraft: bool ##NON NULL
   isPublished: bool ##NON NULL
   isRetired: bool ##NON NULL
   sponsorships: EIEFTsponsorships_SponsorshipConnection_Field

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
   edges: SponsorsActivityEdge ##LIST
   nodes: SponsorsActivity ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class StarredRepositoryEdge(GQLObject):
   cursor: str ##NON NULL
   node: Repository ##NON NULL
   starredAt: DateTime ##NON NULL

class StarredRepositoryConnection(GQLObject):
   edges: StarredRepositoryEdge ##LIST
   isOverLimit: bool ##NON NULL
   nodes: Repository ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class HPXRQcommitComments_CommitCommentConnection_Field(CommitCommentConnection):
   class CommitCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: CommitCommentConnectionArgs



class RTKJRcontributionsCollection_ContributionsCollection_Field(ContributionsCollection):
   class ContributionsCollectionArgs(GQLArgsSet, GQLObject): 
      organizationID: ID
      from_: DateTime
      to: DateTime

   _args: ContributionsCollectionArgs



class ZHOTXfollowers_FollowerConnection_Field(FollowerConnection):
   class FollowerConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: FollowerConnectionArgs



class QUWSAfollowing_FollowingConnection_Field(FollowingConnection):
   class FollowingConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: FollowingConnectionArgs



class GHOJMgist_Gist_Field(Gist):
   class GistArgs(GQLArgsSet, GQLObject): 
      name: str ##NON NULL

   _args: GistArgs



class EIGTTgistComments_GistCommentConnection_Field(GistCommentConnection):
   class GistCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: GistCommentConnectionArgs



class XAKUKgists_GistConnection_Field(GistConnection):
   class GistConnectionArgs(GQLArgsSet, GQLObject): 
      privacy: GistPrivacy
      orderBy: GistOrder
      after: str
      before: str
      first: int
      last: int

   _args: GistConnectionArgs



class HGPHKhovercard_Hovercard_Field(Hovercard):
   class HovercardArgs(GQLArgsSet, GQLObject): 
      primarySubjectId: ID

   _args: HovercardArgs



class VPURHissueComments_IssueCommentConnection_Field(IssueCommentConnection):
   class IssueCommentConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: IssueCommentOrder
      after: str
      before: str
      first: int
      last: int

   _args: IssueCommentConnectionArgs



class TQNVTissues_IssueConnection_Field(IssueConnection):
   class IssueConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: IssueOrder
      labels: str ##NON NULL ##LIST
      states: IssueState ##NON NULL ##LIST
      filterBy: IssueFilters
      after: str
      before: str
      first: int
      last: int

   _args: IssueConnectionArgs



class FAJSLorganization_Organization_Field(Generic[Organization]):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: OrganizationArgs



class IHOORorganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class KXYLKpackages_PackageConnection_Field(PackageConnection):
   class PackageConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      names: str ##LIST
      repositoryId: ID
      packageType: PackageType
      orderBy: PackageOrder

   _args: PackageConnectionArgs



class EHNUUpinnableItems_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject): 
      types: PinnableItemType ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class LJJUMpinnedItems_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject): 
      types: PinnableItemType ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class IPLYQproject_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectArgs



class KGZUUprojectV2_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectV2Args



class RLNVIprojects_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: ProjectOrder
      search: str
      states: ProjectState ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class ZASPYprojectsV2_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class JVIEIpublicKeys_PublicKeyConnection_Field(PublicKeyConnection):
   class PublicKeyConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: PublicKeyConnectionArgs



class MJCYYpullRequests_PullRequestConnection_Field(PullRequestConnection):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject): 
      states: PullRequestState ##NON NULL ##LIST
      labels: str ##NON NULL ##LIST
      headRefName: str
      baseRefName: str
      orderBy: IssueOrder
      after: str
      before: str
      first: int
      last: int

   _args: PullRequestConnectionArgs



class RPVTLrecentProjects_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class TXFYRrepositories_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: RepositoryAffiliation ##LIST
      ownerAffiliations: RepositoryAffiliation ##LIST
      isLocked: bool
      after: str
      before: str
      first: int
      last: int
      isFork: bool

   _args: RepositoryConnectionArgs



class WZTZVrepositoriesContributedTo_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      isLocked: bool
      includeUserRepositories: bool
      contributionTypes: RepositoryContributionType ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryConnectionArgs



class WWUEUrepository_Repository_Field(Repository):
   class RepositoryArgs(GQLArgsSet, GQLObject): 
      name: str ##NON NULL
      followRenames: bool

   _args: RepositoryArgs



class SRBVSrepositoryDiscussionComments_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class MCUFXrepositoryDiscussions_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionOrder
      repositoryId: ID
      answered: bool

   _args: DiscussionConnectionArgs



class IUDZOsavedReplies_SavedReplyConnection_Field(SavedReplyConnection):
   class SavedReplyConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SavedReplyOrder

   _args: SavedReplyConnectionArgs



class DUNDXsponsoring_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class UGLYSsponsors_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class XFZIUsponsorsActivities_SponsorsActivityConnection_Field(SponsorsActivityConnection):
   class SponsorsActivityConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      period: SponsorsActivityPeriod
      since: DateTime
      until: DateTime
      orderBy: SponsorsActivityOrder
      actions: SponsorsActivityAction ##NON NULL ##LIST
      includeAsSponsor: bool

   _args: SponsorsActivityConnectionArgs



class VSGRPsponsorshipNewsletters_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class NHEACsponsorshipsAsMaintainer_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder

   _args: SponsorshipConnectionArgs



class MQUPPsponsorshipsAsSponsor_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipOrder
      maintainerLogins: str ##NON NULL ##LIST

   _args: SponsorshipConnectionArgs



class WYXETstarredRepositories_StarredRepositoryConnection_Field(StarredRepositoryConnection):
   class StarredRepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      ownedByViewer: bool
      orderBy: StarOrder

   _args: StarredRepositoryConnectionArgs



class OGBXDtopRepositories_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: RepositoryOrder ##NON NULL
      since: DateTime

   _args: RepositoryConnectionArgs



class ZBZWPwatching_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: RepositoryAffiliation ##LIST
      ownerAffiliations: RepositoryAffiliation ##LIST
      isLocked: bool
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryConnectionArgs



class User(GQLObject):
   anyPinnableItems: UATYKanyPinnableItems_anyPinnableItems_Field
   avatarUrl: IRWUJavatarUrl_URI_Field
   bio: str
   bioHTML: HTML ##NON NULL
   canReceiveOrganizationEmailsWhenNotificationsRestricted: DQJRFcanReceiveOrganizationEmailsWhenNotificationsRestricted_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field
   commitComments: HPXRQcommitComments_CommitCommentConnection_Field
   company: str
   companyHTML: HTML ##NON NULL
   contributionsCollection: RTKJRcontributionsCollection_ContributionsCollection_Field
   createdAt: DateTime ##NON NULL
   databaseId: int
   email: str ##NON NULL
   estimatedNextSponsorsPayoutInCents: int ##NON NULL
   followers: ZHOTXfollowers_FollowerConnection_Field
   following: QUWSAfollowing_FollowingConnection_Field
   gist: GHOJMgist_Gist_Field
   gistComments: EIGTTgistComments_GistCommentConnection_Field
   gists: XAKUKgists_GistConnection_Field
   hasSponsorsListing: bool ##NON NULL
   hovercard: HGPHKhovercard_Hovercard_Field
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
   isSponsoredBy: OOWDRisSponsoredBy_isSponsoredBy_Field
   isSponsoringViewer: bool ##NON NULL
   isViewer: bool ##NON NULL
   issueComments: VPURHissueComments_IssueCommentConnection_Field
   issues: TQNVTissues_IssueConnection_Field
   itemShowcase: ProfileItemShowcase ##NON NULL
   location: str
   login: str ##NON NULL
   monthlyEstimatedSponsorsIncomeInCents: int ##NON NULL
   name: str
   organization: FAJSLorganization_Organization_Field ## Circular Reference for Organization
   organizationVerifiedDomainEmails: HYZYHorganizationVerifiedDomainEmails_organizationVerifiedDomainEmails_Field
   organizations: IHOORorganizations_OrganizationConnection_Field
   packages: KXYLKpackages_PackageConnection_Field
   pinnableItems: EHNUUpinnableItems_PinnableItemConnection_Field
   pinnedItems: LJJUMpinnedItems_PinnableItemConnection_Field
   pinnedItemsRemaining: int ##NON NULL
   project: IPLYQproject_Project_Field
   projectV2: KGZUUprojectV2_ProjectV2_Field
   projects: RLNVIprojects_ProjectConnection_Field
   projectsResourcePath: URI ##NON NULL
   projectsUrl: URI ##NON NULL
   projectsV2: ZASPYprojectsV2_ProjectV2Connection_Field
   publicKeys: JVIEIpublicKeys_PublicKeyConnection_Field
   pullRequests: MJCYYpullRequests_PullRequestConnection_Field
   recentProjects: RPVTLrecentProjects_ProjectV2Connection_Field
   repositories: TXFYRrepositories_RepositoryConnection_Field
   repositoriesContributedTo: WZTZVrepositoriesContributedTo_RepositoryConnection_Field
   repository: WWUEUrepository_Repository_Field
   repositoryDiscussionComments: SRBVSrepositoryDiscussionComments_DiscussionCommentConnection_Field
   repositoryDiscussions: MCUFXrepositoryDiscussions_DiscussionConnection_Field
   resourcePath: URI ##NON NULL
   savedReplies: IUDZOsavedReplies_SavedReplyConnection_Field
   sponsoring: DUNDXsponsoring_SponsorConnection_Field
   sponsors: UGLYSsponsors_SponsorConnection_Field
   sponsorsActivities: XFZIUsponsorsActivities_SponsorsActivityConnection_Field
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: Sponsorship
   sponsorshipForViewerAsSponsorable: Sponsorship
   sponsorshipNewsletters: VSGRPsponsorshipNewsletters_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: NHEACsponsorshipsAsMaintainer_SponsorshipConnection_Field
   sponsorshipsAsSponsor: MQUPPsponsorshipsAsSponsor_SponsorshipConnection_Field
   starredRepositories: WYXETstarredRepositories_StarredRepositoryConnection_Field
   status: UserStatus
   topRepositories: OGBXDtopRepositories_RepositoryConnection_Field
   twitterUsername: str
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   viewerCanChangePinnedItems: bool ##NON NULL
   viewerCanCreateProjects: bool ##NON NULL
   viewerCanFollow: bool ##NON NULL
   viewerCanSponsor: bool ##NON NULL
   viewerIsFollowing: bool ##NON NULL
   viewerIsSponsoring: bool ##NON NULL
   watching: ZBZWPwatching_RepositoryConnection_Field
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
   membershipTypes: OrgRemoveMemberAuditEntryMembershipType ##LIST
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
   membershipTypes: OrgRemoveOutsideCollaboratorAuditEntryMembershipType ##LIST
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
   restoredMemberships: OrgRestoreMemberAuditEntryMembership ##LIST
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
   edges: OrganizationAuditEntryEdge ##LIST
   nodes: OrganizationAuditEntry ##LIST
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
   edges: VerifiableDomainEdge ##LIST
   nodes: VerifiableDomain ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class OrganizationEnterpriseOwnerEdge(GQLObject):
   cursor: str ##NON NULL
   node: User
   organizationRole: RoleInOrganization ##NON NULL

class OrganizationEnterpriseOwnerConnection(GQLObject):
   edges: OrganizationEnterpriseOwnerEdge ##LIST
   nodes: User ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class MannequinEdge(GQLObject):
   cursor: str ##NON NULL
   node: Mannequin

class MannequinConnection(GQLObject):
   edges: MannequinEdge ##LIST
   nodes: Mannequin ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class OrganizationMemberEdge(GQLObject):
   cursor: str ##NON NULL
   hasTwoFactorEnabled: bool
   node: User
   role: OrganizationMemberRole

class OrganizationMemberConnection(GQLObject):
   edges: OrganizationMemberEdge ##LIST
   nodes: User ##LIST
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
   edges: RepositoryMigrationEdge ##LIST
   nodes: RepositoryMigration ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ExternalIdentitySamlAttributes(GQLObject):
   attributes: ExternalIdentityAttribute ##NON NULL
   emails: UserEmailMetadata ##LIST
   familyName: str
   givenName: str
   groups: str ##LIST
   nameId: str
   username: str

class ExternalIdentityScimAttributes(GQLObject):
   emails: UserEmailMetadata ##LIST
   familyName: str
   givenName: str
   groups: str ##LIST
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
   edges: ExternalIdentityEdge ##LIST
   nodes: ExternalIdentity ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class TVTHHexternalIdentities_ExternalIdentityConnection_Field(ExternalIdentityConnection):
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
   externalIdentities: TVTHHexternalIdentities_ExternalIdentityConnection_Field
   id: ID ##NON NULL
   idpCertificate: X509Certificate
   issuer: str
   organization: Organization
   signatureMethod: URI
   ssoUrl: URI

class FWWWKauditLog_OrganizationAuditEntryConnection_Field(OrganizationAuditEntryConnection):
   class OrganizationAuditEntryConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      query: str
      orderBy: AuditLogOrder

   _args: OrganizationAuditEntryConnectionArgs



class CVHQHdomains_VerifiableDomainConnection_Field(VerifiableDomainConnection):
   class VerifiableDomainConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      isVerified: bool
      isApproved: bool
      orderBy: VerifiableDomainOrder

   _args: VerifiableDomainConnectionArgs



class PNTXOenterpriseOwners_OrganizationEnterpriseOwnerConnection_Field(OrganizationEnterpriseOwnerConnection):
   class OrganizationEnterpriseOwnerConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      organizationRole: RoleInOrganization
      orderBy: OrgEnterpriseOwnerOrder
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationEnterpriseOwnerConnectionArgs



class OVGVSipAllowListEntries_IpAllowListEntryConnection_Field(Generic[IpAllowListEntryConnection]):
   class IpAllowListEntryConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: IpAllowListEntryConnectionArgs



class YEWTWmannequins_MannequinConnection_Field(MannequinConnection):
   class MannequinConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: MannequinOrder

   _args: MannequinConnectionArgs



class VWAHOmemberStatuses_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class QQFIImembersWithRole_OrganizationMemberConnection_Field(OrganizationMemberConnection):
   class OrganizationMemberConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationMemberConnectionArgs



class HPIIMpackages_PackageConnection_Field(PackageConnection):
   class PackageConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      names: str ##LIST
      repositoryId: ID
      packageType: PackageType
      orderBy: PackageOrder

   _args: PackageConnectionArgs



class UGHVZpendingMembers_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class BLNMIpinnableItems_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject): 
      types: PinnableItemType ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class HMZMSpinnedItems_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject): 
      types: PinnableItemType ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class UADVXproject_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectArgs



class NYVUIprojectV2_ProjectV2_Field(ProjectV2):
   class ProjectV2Args(GQLArgsSet, GQLObject): 
      number: int ##NON NULL

   _args: ProjectV2Args



class ORYXCprojects_ProjectConnection_Field(ProjectConnection):
   class ProjectConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: ProjectOrder
      search: str
      states: ProjectState ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: ProjectConnectionArgs



class DWJYHprojectsV2_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      orderBy: ProjectV2Order
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class TFBJNrecentProjects_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class NNFFSrepositories_RepositoryConnection_Field(RepositoryConnection):
   class RepositoryConnectionArgs(GQLArgsSet, GQLObject): 
      privacy: RepositoryPrivacy
      orderBy: RepositoryOrder
      affiliations: RepositoryAffiliation ##LIST
      ownerAffiliations: RepositoryAffiliation ##LIST
      isLocked: bool
      after: str
      before: str
      first: int
      last: int
      isFork: bool

   _args: RepositoryConnectionArgs



class FMKGHrepository_Repository_Field(Repository):
   class RepositoryArgs(GQLArgsSet, GQLObject): 
      name: str ##NON NULL
      followRenames: bool

   _args: RepositoryArgs



class DSZJGrepositoryDiscussionComments_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class QDKEOrepositoryDiscussions_DiscussionConnection_Field(DiscussionConnection):
   class DiscussionConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: DiscussionOrder
      repositoryId: ID
      answered: bool

   _args: DiscussionConnectionArgs



class SBXDBrepositoryMigrations_RepositoryMigrationConnection_Field(RepositoryMigrationConnection):
   class RepositoryMigrationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      state: MigrationState
      repositoryName: str
      orderBy: RepositoryMigrationOrder

   _args: RepositoryMigrationConnectionArgs



class WGSWRsponsoring_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class LBYYIsponsors_SponsorConnection_Field(SponsorConnection):
   class SponsorConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      tierId: ID
      orderBy: SponsorOrder

   _args: SponsorConnectionArgs



class EKEMDsponsorsActivities_SponsorsActivityConnection_Field(SponsorsActivityConnection):
   class SponsorsActivityConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      period: SponsorsActivityPeriod
      since: DateTime
      until: DateTime
      orderBy: SponsorsActivityOrder
      actions: SponsorsActivityAction ##NON NULL ##LIST
      includeAsSponsor: bool

   _args: SponsorsActivityConnectionArgs



class SOUEIsponsorshipNewsletters_SponsorshipNewsletterConnection_Field(SponsorshipNewsletterConnection):
   class SponsorshipNewsletterConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipNewsletterOrder

   _args: SponsorshipNewsletterConnectionArgs



class EZNLXsponsorshipsAsMaintainer_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      includePrivate: bool
      orderBy: SponsorshipOrder

   _args: SponsorshipConnectionArgs



class ROATEsponsorshipsAsSponsor_SponsorshipConnection_Field(SponsorshipConnection):
   class SponsorshipConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: SponsorshipOrder
      maintainerLogins: str ##NON NULL ##LIST

   _args: SponsorshipConnectionArgs



class HWKMRteam_Team_Field(Team):
   class TeamArgs(GQLArgsSet, GQLObject): 
      slug: str ##NON NULL

   _args: TeamArgs



class OQAMZteams_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject): 
      privacy: TeamPrivacy
      role: TeamRole
      query: str
      userLogins: str ##NON NULL ##LIST
      orderBy: TeamOrder
      ldapMapped: bool
      rootTeamsOnly: bool
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class Organization(GQLObject):
   anyPinnableItems: VYWKQanyPinnableItems_anyPinnableItems_Field
   auditLog: FWWWKauditLog_OrganizationAuditEntryConnection_Field
   avatarUrl: JTPXPavatarUrl_URI_Field
   createdAt: DateTime ##NON NULL
   databaseId: int
   description: str
   descriptionHTML: str
   domains: CVHQHdomains_VerifiableDomainConnection_Field
   email: str
   enterpriseOwners: PNTXOenterpriseOwners_OrganizationEnterpriseOwnerConnection_Field
   estimatedNextSponsorsPayoutInCents: int ##NON NULL
   hasSponsorsListing: bool ##NON NULL
   id: ID ##NON NULL
   interactionAbility: RepositoryInteractionAbility
   ipAllowListEnabledSetting: IpAllowListEnabledSettingValue ##NON NULL
   ipAllowListEntries: OVGVSipAllowListEntries_IpAllowListEntryConnection_Field ## Circular Reference for IpAllowListEntryConnection
   ipAllowListForInstalledAppsEnabledSetting: IpAllowListForInstalledAppsEnabledSettingValue ##NON NULL
   isSponsoredBy: XRTILisSponsoredBy_isSponsoredBy_Field
   isSponsoringViewer: bool ##NON NULL
   isVerified: bool ##NON NULL
   itemShowcase: ProfileItemShowcase ##NON NULL
   location: str
   login: str ##NON NULL
   mannequins: YEWTWmannequins_MannequinConnection_Field
   memberStatuses: VWAHOmemberStatuses_UserStatusConnection_Field
   membersCanForkPrivateRepositories: bool ##NON NULL
   membersWithRole: QQFIImembersWithRole_OrganizationMemberConnection_Field
   monthlyEstimatedSponsorsIncomeInCents: int ##NON NULL
   name: str
   newTeamResourcePath: URI ##NON NULL
   newTeamUrl: URI ##NON NULL
   notificationDeliveryRestrictionEnabledSetting: NotificationRestrictionSettingValue ##NON NULL
   organizationBillingEmail: str
   packages: HPIIMpackages_PackageConnection_Field
   pendingMembers: UGHVZpendingMembers_UserConnection_Field
   pinnableItems: BLNMIpinnableItems_PinnableItemConnection_Field
   pinnedItems: HMZMSpinnedItems_PinnableItemConnection_Field
   pinnedItemsRemaining: int ##NON NULL
   project: UADVXproject_Project_Field
   projectV2: NYVUIprojectV2_ProjectV2_Field
   projects: ORYXCprojects_ProjectConnection_Field
   projectsResourcePath: URI ##NON NULL
   projectsUrl: URI ##NON NULL
   projectsV2: DWJYHprojectsV2_ProjectV2Connection_Field
   recentProjects: TFBJNrecentProjects_ProjectV2Connection_Field
   repositories: NNFFSrepositories_RepositoryConnection_Field
   repository: FMKGHrepository_Repository_Field
   repositoryDiscussionComments: DSZJGrepositoryDiscussionComments_DiscussionCommentConnection_Field
   repositoryDiscussions: QDKEOrepositoryDiscussions_DiscussionConnection_Field
   repositoryMigrations: SBXDBrepositoryMigrations_RepositoryMigrationConnection_Field
   requiresTwoFactorAuthentication: bool
   resourcePath: URI ##NON NULL
   samlIdentityProvider: OrganizationIdentityProvider
   sponsoring: WGSWRsponsoring_SponsorConnection_Field
   sponsors: LBYYIsponsors_SponsorConnection_Field
   sponsorsActivities: EKEMDsponsorsActivities_SponsorsActivityConnection_Field
   sponsorsListing: SponsorsListing
   sponsorshipForViewerAsSponsor: Sponsorship
   sponsorshipForViewerAsSponsorable: Sponsorship
   sponsorshipNewsletters: SOUEIsponsorshipNewsletters_SponsorshipNewsletterConnection_Field
   sponsorshipsAsMaintainer: EZNLXsponsorshipsAsMaintainer_SponsorshipConnection_Field
   sponsorshipsAsSponsor: ROATEsponsorshipsAsSponsor_SponsorshipConnection_Field
   team: HWKMRteam_Team_Field
   teams: OQAMZteams_TeamConnection_Field
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
   edges: EnterpriseOrganizationMembershipEdge ##LIST
   nodes: Organization ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ZJIMXorganizations_EnterpriseOrganizationMembershipConnection_Field(EnterpriseOrganizationMembershipConnection):
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
   avatarUrl: EHZADavatarUrl_URI_Field
   createdAt: DateTime ##NON NULL
   enterprise: NewType('Enterprise', GQLObject) ##NON NULL ## Circular Reference for Enterprise
   id: ID ##NON NULL
   login: str ##NON NULL
   name: str
   organizations: ZJIMXorganizations_EnterpriseOrganizationMembershipConnection_Field
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
   edges: EnterpriseMemberEdge ##LIST
   nodes: EnterpriseMember ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterpriseAdministratorEdge(GQLObject):
   cursor: str ##NON NULL
   node: User
   role: EnterpriseAdministratorRole ##NON NULL

class EnterpriseAdministratorConnection(GQLObject):
   edges: EnterpriseAdministratorEdge ##LIST
   nodes: User ##LIST
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
   edges: EnterpriseServerUserAccountEmailEdge ##LIST
   nodes: EnterpriseServerUserAccountEmail ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class QUEOEemails_EnterpriseServerUserAccountEmailConnection_Field(EnterpriseServerUserAccountEmailConnection):
   class EnterpriseServerUserAccountEmailConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: EnterpriseServerUserAccountEmailOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerUserAccountEmailConnectionArgs



class EnterpriseServerUserAccount(GQLObject):
   createdAt: DateTime ##NON NULL
   emails: QUEOEemails_EnterpriseServerUserAccountEmailConnection_Field
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
   edges: EnterpriseServerUserAccountEdge ##LIST
   nodes: EnterpriseServerUserAccount ##LIST
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
   edges: EnterpriseServerUserAccountsUploadEdge ##LIST
   nodes: EnterpriseServerUserAccountsUpload ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class QFGSAuserAccounts_EnterpriseServerUserAccountConnection_Field(EnterpriseServerUserAccountConnection):
   class EnterpriseServerUserAccountConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: EnterpriseServerUserAccountOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerUserAccountConnectionArgs



class BBALGuserAccountsUploads_EnterpriseServerUserAccountsUploadConnection_Field(EnterpriseServerUserAccountsUploadConnection):
   class EnterpriseServerUserAccountsUploadConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: EnterpriseServerUserAccountsUploadOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseServerUserAccountsUploadConnectionArgs



class EnterpriseServerInstallation(GQLObject):
   createdAt: DateTime ##NON NULL
   customerName: str ##NON NULL
   hostName: str ##NON NULL
   id: ID ##NON NULL
   isConnected: bool ##NON NULL
   updatedAt: DateTime ##NON NULL
   userAccounts: QFGSAuserAccounts_EnterpriseServerUserAccountConnection_Field
   userAccountsUploads: BBALGuserAccountsUploads_EnterpriseServerUserAccountsUploadConnection_Field

class EnterpriseServerInstallationEdge(GQLObject):
   cursor: str ##NON NULL
   node: EnterpriseServerInstallation

class EnterpriseServerInstallationConnection(GQLObject):
   edges: EnterpriseServerInstallationEdge ##LIST
   nodes: EnterpriseServerInstallation ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class WAXBDexternalIdentities_ExternalIdentityConnection_Field(ExternalIdentityConnection):
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
   externalIdentities: WAXBDexternalIdentities_ExternalIdentityConnection_Field
   id: ID ##NON NULL
   providerType: OIDCProviderType ##NON NULL
   tenantId: str ##NON NULL

class EnterpriseRepositoryInfoEdge(GQLObject):
   cursor: str ##NON NULL
   node: EnterpriseRepositoryInfo

class EnterpriseRepositoryInfoConnection(GQLObject):
   edges: EnterpriseRepositoryInfoEdge ##LIST
   nodes: EnterpriseRepositoryInfo ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class BTBTArepositories_EnterpriseRepositoryInfoConnection_Field(EnterpriseRepositoryInfoConnection):
   class EnterpriseRepositoryInfoConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: RepositoryOrder

   _args: EnterpriseRepositoryInfoConnectionArgs



class EnterpriseOutsideCollaboratorEdge(GQLObject):
   cursor: str ##NON NULL
   node: User
   repositories: BTBTArepositories_EnterpriseRepositoryInfoConnection_Field

class EnterpriseOutsideCollaboratorConnection(GQLObject):
   edges: EnterpriseOutsideCollaboratorEdge ##LIST
   nodes: User ##LIST
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
   edges: EnterpriseAdministratorInvitationEdge ##LIST
   nodes: EnterpriseAdministratorInvitation ##LIST
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
   shortDescriptionHTML: IUMEBshortDescriptionHTML_HTML_Field
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
   edges: RepositoryInvitationEdge ##LIST
   nodes: RepositoryInvitation ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class EnterprisePendingMemberInvitationEdge(GQLObject):
   cursor: str ##NON NULL
   node: OrganizationInvitation

class EnterprisePendingMemberInvitationConnection(GQLObject):
   edges: EnterprisePendingMemberInvitationEdge ##LIST
   nodes: OrganizationInvitation ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL
   totalUniqueUserCount: int ##NON NULL

class MWUQRexternalIdentities_ExternalIdentityConnection_Field(ExternalIdentityConnection):
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
   externalIdentities: MWUQRexternalIdentities_ExternalIdentityConnection_Field
   id: ID ##NON NULL
   idpCertificate: X509Certificate
   issuer: str
   recoveryCodes: str ##LIST
   signatureMethod: SamlSignatureAlgorithm
   ssoUrl: URI

class NBNWJadmins_EnterpriseAdministratorConnection_Field(EnterpriseAdministratorConnection):
   class EnterpriseAdministratorConnectionArgs(GQLArgsSet, GQLObject): 
      organizationLogins: str ##NON NULL ##LIST
      query: str
      role: EnterpriseAdministratorRole
      orderBy: EnterpriseMemberOrder
      hasTwoFactorEnabled: bool
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseAdministratorConnectionArgs



class JWBBPaffiliatedUsersWithTwoFactorDisabled_UserConnection_Field(UserConnection):
   class UserConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserConnectionArgs



class ZMOVQallowPrivateRepositoryForkingSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class NCFPYdefaultRepositoryPermissionSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: DefaultRepositoryPermissionField ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class HQXWPdomains_VerifiableDomainConnection_Field(VerifiableDomainConnection):
   class VerifiableDomainConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      isVerified: bool
      isApproved: bool
      orderBy: VerifiableDomainOrder

   _args: VerifiableDomainConnectionArgs



class KYLZVenterpriseServerInstallations_EnterpriseServerInstallationConnection_Field(EnterpriseServerInstallationConnection):
   class EnterpriseServerInstallationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      connectedOnly: bool
      orderBy: EnterpriseServerInstallationOrder

   _args: EnterpriseServerInstallationConnectionArgs



class MCPUFipAllowListEntries_IpAllowListEntryConnection_Field(Generic[IpAllowListEntryConnection]):
   class IpAllowListEntryConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: IpAllowListEntryConnectionArgs



class EBGLLmembersCanChangeRepositoryVisibilitySettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class BHXPYmembersCanCreateRepositoriesSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: OrganizationMembersCanCreateRepositoriesSettingValue ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class AEMEYmembersCanDeleteIssuesSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class HALHPmembersCanDeleteRepositoriesSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class HVACMmembersCanInviteCollaboratorsSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class CYVTBmembersCanUpdateProtectedBranchesSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class KQEZKmembersCanViewDependencyInsightsSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class RDGBLorganizationProjectsSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class DOILLoutsideCollaborators_EnterpriseOutsideCollaboratorConnection_Field(EnterpriseOutsideCollaboratorConnection):
   class EnterpriseOutsideCollaboratorConnectionArgs(GQLArgsSet, GQLObject): 
      login: str
      query: str
      orderBy: EnterpriseMemberOrder
      visibility: RepositoryVisibility
      hasTwoFactorEnabled: bool
      organizationLogins: str ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseOutsideCollaboratorConnectionArgs



class DVPFYpendingAdminInvitations_EnterpriseAdministratorInvitationConnection_Field(EnterpriseAdministratorInvitationConnection):
   class EnterpriseAdministratorInvitationConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      orderBy: EnterpriseAdministratorInvitationOrder
      role: EnterpriseAdministratorRole
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseAdministratorInvitationConnectionArgs



class AQCRQpendingCollaboratorInvitations_RepositoryInvitationConnection_Field(RepositoryInvitationConnection):
   class RepositoryInvitationConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      orderBy: RepositoryInvitationOrder
      after: str
      before: str
      first: int
      last: int

   _args: RepositoryInvitationConnectionArgs



class ZSBOCpendingMemberInvitations_EnterprisePendingMemberInvitationConnection_Field(EnterprisePendingMemberInvitationConnection):
   class EnterprisePendingMemberInvitationConnectionArgs(GQLArgsSet, GQLObject): 
      query: str
      organizationLogins: str ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: EnterprisePendingMemberInvitationConnectionArgs



class RUXJHrepositoryProjectsSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class KAMGJsamlIdentityProviderSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: IdentityProviderConfigurationState ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class XYVRVsupportEntitlements_EnterpriseMemberConnection_Field(EnterpriseMemberConnection):
   class EnterpriseMemberConnectionArgs(GQLArgsSet, GQLObject): 
      orderBy: EnterpriseMemberOrder
      after: str
      before: str
      first: int
      last: int

   _args: EnterpriseMemberConnectionArgs



class TQBEAteamDiscussionsSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class KZPXPtwoFactorRequiredSettingOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      value: bool ##NON NULL
      orderBy: OrganizationOrder

   _args: OrganizationConnectionArgs



class EnterpriseOwnerInfo(GQLObject):
   admins: NBNWJadmins_EnterpriseAdministratorConnection_Field
   affiliatedUsersWithTwoFactorDisabled: JWBBPaffiliatedUsersWithTwoFactorDisabled_UserConnection_Field
   affiliatedUsersWithTwoFactorDisabledExist: bool ##NON NULL
   allowPrivateRepositoryForkingSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   allowPrivateRepositoryForkingSettingOrganizations: ZMOVQallowPrivateRepositoryForkingSettingOrganizations_OrganizationConnection_Field
   allowPrivateRepositoryForkingSettingPolicyValue: EnterpriseAllowPrivateRepositoryForkingPolicyValue
   defaultRepositoryPermissionSetting: EnterpriseDefaultRepositoryPermissionSettingValue ##NON NULL
   defaultRepositoryPermissionSettingOrganizations: NCFPYdefaultRepositoryPermissionSettingOrganizations_OrganizationConnection_Field
   domains: HQXWPdomains_VerifiableDomainConnection_Field
   enterpriseServerInstallations: KYLZVenterpriseServerInstallations_EnterpriseServerInstallationConnection_Field
   ipAllowListEnabledSetting: IpAllowListEnabledSettingValue ##NON NULL
   ipAllowListEntries: MCPUFipAllowListEntries_IpAllowListEntryConnection_Field
   ipAllowListForInstalledAppsEnabledSetting: IpAllowListForInstalledAppsEnabledSettingValue ##NON NULL
   isUpdatingDefaultRepositoryPermission: bool ##NON NULL
   isUpdatingTwoFactorRequirement: bool ##NON NULL
   membersCanChangeRepositoryVisibilitySetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanChangeRepositoryVisibilitySettingOrganizations: EBGLLmembersCanChangeRepositoryVisibilitySettingOrganizations_OrganizationConnection_Field
   membersCanCreateInternalRepositoriesSetting: bool
   membersCanCreatePrivateRepositoriesSetting: bool
   membersCanCreatePublicRepositoriesSetting: bool
   membersCanCreateRepositoriesSetting: EnterpriseMembersCanCreateRepositoriesSettingValue
   membersCanCreateRepositoriesSettingOrganizations: BHXPYmembersCanCreateRepositoriesSettingOrganizations_OrganizationConnection_Field
   membersCanDeleteIssuesSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanDeleteIssuesSettingOrganizations: AEMEYmembersCanDeleteIssuesSettingOrganizations_OrganizationConnection_Field
   membersCanDeleteRepositoriesSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanDeleteRepositoriesSettingOrganizations: HALHPmembersCanDeleteRepositoriesSettingOrganizations_OrganizationConnection_Field
   membersCanInviteCollaboratorsSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanInviteCollaboratorsSettingOrganizations: HVACMmembersCanInviteCollaboratorsSettingOrganizations_OrganizationConnection_Field
   membersCanMakePurchasesSetting: EnterpriseMembersCanMakePurchasesSettingValue ##NON NULL
   membersCanUpdateProtectedBranchesSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanUpdateProtectedBranchesSettingOrganizations: CYVTBmembersCanUpdateProtectedBranchesSettingOrganizations_OrganizationConnection_Field
   membersCanViewDependencyInsightsSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   membersCanViewDependencyInsightsSettingOrganizations: KQEZKmembersCanViewDependencyInsightsSettingOrganizations_OrganizationConnection_Field
   notificationDeliveryRestrictionEnabledSetting: NotificationRestrictionSettingValue ##NON NULL
   oidcProvider: OIDCProvider
   organizationProjectsSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   organizationProjectsSettingOrganizations: RDGBLorganizationProjectsSettingOrganizations_OrganizationConnection_Field
   outsideCollaborators: DOILLoutsideCollaborators_EnterpriseOutsideCollaboratorConnection_Field
   pendingAdminInvitations: DVPFYpendingAdminInvitations_EnterpriseAdministratorInvitationConnection_Field
   pendingCollaboratorInvitations: AQCRQpendingCollaboratorInvitations_RepositoryInvitationConnection_Field
   pendingMemberInvitations: ZSBOCpendingMemberInvitations_EnterprisePendingMemberInvitationConnection_Field
   repositoryProjectsSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   repositoryProjectsSettingOrganizations: RUXJHrepositoryProjectsSettingOrganizations_OrganizationConnection_Field
   samlIdentityProvider: EnterpriseIdentityProvider
   samlIdentityProviderSettingOrganizations: KAMGJsamlIdentityProviderSettingOrganizations_OrganizationConnection_Field
   supportEntitlements: XYVRVsupportEntitlements_EnterpriseMemberConnection_Field
   teamDiscussionsSetting: EnterpriseEnabledDisabledSettingValue ##NON NULL
   teamDiscussionsSettingOrganizations: TQBEAteamDiscussionsSettingOrganizations_OrganizationConnection_Field
   twoFactorRequiredSetting: EnterpriseEnabledSettingValue ##NON NULL
   twoFactorRequiredSettingOrganizations: KZPXPtwoFactorRequiredSettingOrganizations_OrganizationConnection_Field

class ULMKYmembers_EnterpriseMemberConnection_Field(EnterpriseMemberConnection):
   class EnterpriseMemberConnectionArgs(GQLArgsSet, GQLObject): 
      organizationLogins: str ##NON NULL ##LIST
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



class VHPVHorganizations_OrganizationConnection_Field(OrganizationConnection):
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
   avatarUrl: OVNBXavatarUrl_URI_Field
   billingInfo: EnterpriseBillingInfo
   createdAt: DateTime ##NON NULL
   databaseId: int
   description: str
   descriptionHTML: HTML ##NON NULL
   id: ID ##NON NULL
   location: str
   members: ULMKYmembers_EnterpriseMemberConnection_Field
   name: str ##NON NULL
   organizations: VHPVHorganizations_OrganizationConnection_Field
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
   edges: IpAllowListEntryEdge ##LIST
   nodes: IpAllowListEntry ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class LIBNZipAllowListEntries_IpAllowListEntryConnection_Field(IpAllowListEntryConnection):
   class IpAllowListEntryConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: IpAllowListEntryOrder

   _args: IpAllowListEntryConnectionArgs



class App(GQLObject):
   createdAt: DateTime ##NON NULL
   databaseId: int
   description: str
   id: ID ##NON NULL
   ipAllowListEntries: LIBNZipAllowListEntries_IpAllowListEntryConnection_Field
   logoBackgroundColor: str ##NON NULL
   logoUrl: EPCLClogoUrl_URI_Field
   name: str ##NON NULL
   slug: str ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL

class CheckRunEdge(GQLObject):
   cursor: str ##NON NULL
   node: CheckRun

class CheckRunConnection(GQLObject):
   edges: CheckRunEdge ##LIST
   nodes: CheckRun ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class Push(GQLObject):
   id: ID ##NON NULL
   nextSha: GitObjectID
   permalink: URI ##NON NULL
   previousSha: GitObjectID
   pusher: Actor ##NON NULL
   repository: Repository ##NON NULL

class GFIEZcheckRuns_CheckRunConnection_Field(CheckRunConnection):
   class CheckRunConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      filterBy: CheckRunFilter

   _args: CheckRunConnectionArgs



class STMEOmatchingPullRequests_PullRequestConnection_Field(PullRequestConnection):
   class PullRequestConnectionArgs(GQLArgsSet, GQLObject): 
      states: PullRequestState ##NON NULL ##LIST
      labels: str ##NON NULL ##LIST
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
   checkRuns: GFIEZcheckRuns_CheckRunConnection_Field
   commit: Commit ##NON NULL
   conclusion: CheckConclusionState
   createdAt: DateTime ##NON NULL
   creator: User
   databaseId: int
   id: ID ##NON NULL
   matchingPullRequests: STMEOmatchingPullRequests_PullRequestConnection_Field
   push: Push
   repository: Repository ##NON NULL
   resourcePath: URI ##NON NULL
   status: CheckStatusState ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   workflowRun: NewType('WorkflowRun', GQLObject) ## Circular Reference for WorkflowRun

class ZMEIFenvironments_EnvironmentConnection_Field(EnvironmentConnection):
   class EnvironmentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: EnvironmentConnectionArgs



class DeploymentReview(GQLObject):
   comment: str ##NON NULL
   databaseId: int
   environments: ZMEIFenvironments_EnvironmentConnection_Field
   id: ID ##NON NULL
   state: DeploymentReviewState ##NON NULL
   user: User ##NON NULL

class DeploymentReviewEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeploymentReview

class DeploymentReviewConnection(GQLObject):
   edges: DeploymentReviewEdge ##LIST
   nodes: DeploymentReview ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class DeploymentRequestEdge(GQLObject):
   cursor: str ##NON NULL
   node: DeploymentRequest

class DeploymentRequestConnection(GQLObject):
   edges: DeploymentRequestEdge ##LIST
   nodes: DeploymentRequest ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class NRAXIruns_WorkflowRunConnection_Field(Generic[WorkflowRunConnection]):
   class WorkflowRunConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: WorkflowRunOrder

   _args: WorkflowRunConnectionArgs



class Workflow(GQLObject):
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   name: str ##NON NULL
   runs: NRAXIruns_WorkflowRunConnection_Field ## Circular Reference for WorkflowRunConnection
   updatedAt: DateTime ##NON NULL

class KWPEYdeploymentReviews_DeploymentReviewConnection_Field(DeploymentReviewConnection):
   class DeploymentReviewConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentReviewConnectionArgs



class ASSNYpendingDeploymentRequests_DeploymentRequestConnection_Field(DeploymentRequestConnection):
   class DeploymentRequestConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: DeploymentRequestConnectionArgs



class WorkflowRun(GQLObject):
   checkSuite: CheckSuite ##NON NULL
   createdAt: DateTime ##NON NULL
   databaseId: int
   deploymentReviews: KWPEYdeploymentReviews_DeploymentReviewConnection_Field
   id: ID ##NON NULL
   pendingDeploymentRequests: ASSNYpendingDeploymentRequests_DeploymentRequestConnection_Field
   resourcePath: URI ##NON NULL
   runNumber: int ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL
   workflow: Workflow ##NON NULL

class WorkflowRunEdge(GQLObject):
   cursor: str ##NON NULL
   node: WorkflowRun

class WorkflowRunConnection(GQLObject):
   edges: WorkflowRunEdge ##LIST
   nodes: WorkflowRun ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class UpdateTeamsRepositoryPayload(GQLObject):
   clientMutationId: str
   repository: Repository
   teams: Team ##LIST

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
   annotations: CheckAnnotationData ##NON NULL ##LIST
   images: CheckRunOutputImage ##NON NULL ##LIST

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
   actions: CheckRunAction ##NON NULL ##LIST
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
   edges: SponsorableItemEdge ##LIST
   nodes: SponsorableItem ##LIST
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class SecurityAdvisoryEdge(GQLObject):
   cursor: str ##NON NULL
   node: SecurityAdvisory

class SecurityAdvisoryConnection(GQLObject):
   edges: SecurityAdvisoryEdge ##LIST
   nodes: SecurityAdvisory ##LIST
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
   logoUrl: CWFDLlogoUrl_URI_Field
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
   textMatches: TextMatch ##LIST

class SearchResultItemConnection(GQLObject):
   codeCount: int ##NON NULL
   discussionCount: int ##NON NULL
   edges: SearchResultItemEdge ##LIST
   issueCount: int ##NON NULL
   nodes: SearchResultItem ##LIST
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
   reactionGroups: ReactionGroup ##LIST
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

class ZXENQcomments_PullRequestReviewCommentConnection_Field(PullRequestReviewCommentConnection):
   class PullRequestReviewCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      skip: int

   _args: PullRequestReviewCommentConnectionArgs



class PullRequestThread(GQLObject):
   comments: ZXENQcomments_PullRequestReviewCommentConnection_Field
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

class AUMUDpinnableItems_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject): 
      types: PinnableItemType ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class WIMMGpinnedItems_PinnableItemConnection_Field(PinnableItemConnection):
   class PinnableItemConnectionArgs(GQLArgsSet, GQLObject): 
      types: PinnableItemType ##NON NULL ##LIST
      after: str
      before: str
      first: int
      last: int

   _args: PinnableItemConnectionArgs



class ProfileOwner(GQLObject):
   anyPinnableItems: CGFDDanyPinnableItems_anyPinnableItems_Field
   email: str
   id: ID ##NON NULL
   itemShowcase: ProfileItemShowcase ##NON NULL
   location: str
   login: str ##NON NULL
   name: str
   pinnableItems: AUMUDpinnableItems_PinnableItemConnection_Field
   pinnedItems: WIMMGpinnedItems_PinnableItemConnection_Field
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
   edges: MarketplaceListingEdge ##LIST
   nodes: MarketplaceListing ##LIST
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
   deletions: FileDeletion ##NON NULL ##LIST
   additions: FileAddition ##NON NULL ##LIST

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
   actions: CheckRunAction ##NON NULL ##LIST
   clientMutationId: str

class Claimable(GQLObject): 
   pass

class CreateAttributionInvitationPayload(GQLObject):
   clientMutationId: str
   owner: Organization
   source: Claimable
   target: Claimable

class UAWLJuserContentEdits_UserContentEditConnection_Field(UserContentEditConnection):
   class UserContentEditConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: UserContentEditConnectionArgs



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
   userContentEdits: UAWLJuserContentEdits_UserContentEditConnection_Field
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
   reactionGroups: ReactionGroup ##LIST
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
   comments: DraftPullRequestReviewComment ##LIST
   threads: DraftPullRequestReviewThread ##LIST
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
   users: User ##LIST

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

class XQXUCstargazers_StargazerConnection_Field(StargazerConnection):
   class StargazerConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: StarOrder

   _args: StargazerConnectionArgs



class Starrable(GQLObject):
   id: ID ##NON NULL
   stargazerCount: int ##NON NULL
   stargazers: XQXUCstargazers_StargazerConnection_Field
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
   deployments: Deployment ##LIST

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
   reviewDismissalActorIds: ID ##NON NULL ##LIST
   bypassPullRequestActorIds: ID ##NON NULL ##LIST
   bypassForcePushActorIds: ID ##NON NULL ##LIST
   restrictsPushes: bool
   pushActorIds: ID ##NON NULL ##LIST
   requiredStatusCheckContexts: str ##NON NULL ##LIST
   requiredStatusChecks: RequiredStatusCheckInput ##NON NULL ##LIST
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

class HVQSWorganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class GrantEnterpriseOrganizationsMigratorRolePayload(GQLObject):
   clientMutationId: str
   organizations: HVQSWorganizations_OrganizationConnection_Field

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

class GTCPEmemberStatuses_UserStatusConnection_Field(UserStatusConnection):
   class UserStatusConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      orderBy: UserStatusOrder

   _args: UserStatusConnectionArgs



class MemberStatusable(GQLObject):
   memberStatuses: GTCPEmemberStatuses_UserStatusConnection_Field

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

class KFDDLrelevantTeams_TeamConnection_Field(TeamConnection):
   class TeamConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: TeamConnectionArgs



class OrganizationTeamsHovercardContext(GQLObject):
   message: str ##NON NULL
   octicon: str ##NON NULL
   relevantTeams: KFDDLrelevantTeams_TeamConnection_Field
   teamsResourcePath: URI ##NON NULL
   teamsUrl: URI ##NON NULL
   totalTeamCount: int ##NON NULL

class KOCVJrelevantOrganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class OrganizationsHovercardContext(GQLObject):
   message: str ##NON NULL
   octicon: str ##NON NULL
   relevantOrganizations: KOCVJrelevantOrganizations_OrganizationConnection_Field
   totalOrganizationCount: int ##NON NULL

class GQSSXpackages_PackageConnection_Field(PackageConnection):
   class PackageConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      names: str ##LIST
      repositoryId: ID
      packageType: PackageType
      orderBy: PackageOrder

   _args: PackageConnectionArgs



class PackageOwner(GQLObject):
   id: ID ##NON NULL
   packages: GQSSXpackages_PackageConnection_Field

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

class YMEWQrecentProjects_ProjectV2Connection_Field(ProjectV2Connection):
   class ProjectV2ConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ConnectionArgs



class ProjectV2Recent(GQLObject):
   recentProjects: YMEWQrecentProjects_ProjectV2Connection_Field

class PublishSponsorsTierPayload(GQLObject):
   clientMutationId: str
   sponsorsTier: SponsorsTier

class RegenerateEnterpriseIdentityProviderRecoveryCodesPayload(GQLObject):
   clientMutationId: str
   identityProvider: EnterpriseIdentityProvider

class RejectDeploymentsPayload(GQLObject):
   clientMutationId: str
   deployments: Deployment ##LIST

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

class ALFGLrepositoryDiscussions_DiscussionConnection_Field(DiscussionConnection):
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
   repositoryDiscussions: ALFGLrepositoryDiscussions_DiscussionConnection_Field

class TMNAUrepositoryDiscussionComments_DiscussionCommentConnection_Field(DiscussionCommentConnection):
   class DiscussionCommentConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int
      repositoryId: ID
      onlyAnswers: bool

   _args: DiscussionCommentConnectionArgs



class RepositoryDiscussionCommentAuthor(GQLObject):
   repositoryDiscussionComments: TMNAUrepositoryDiscussionComments_DiscussionCommentConnection_Field

class RepositoryNode(GQLObject):
   repository: Repository ##NON NULL

class RerequestCheckSuitePayload(GQLObject):
   checkSuite: CheckSuite
   clientMutationId: str

class ResolveReviewThreadPayload(GQLObject):
   clientMutationId: str
   thread: PullRequestReviewThread

class RNWETorganizations_OrganizationConnection_Field(OrganizationConnection):
   class OrganizationConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: OrganizationConnectionArgs



class RevokeEnterpriseOrganizationsMigratorRolePayload(GQLObject):
   clientMutationId: str
   organizations: RNWETorganizations_OrganizationConnection_Field

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
   reviewDismissalActorIds: ID ##NON NULL ##LIST
   bypassPullRequestActorIds: ID ##NON NULL ##LIST
   bypassForcePushActorIds: ID ##NON NULL ##LIST
   restrictsPushes: bool
   pushActorIds: ID ##NON NULL ##LIST
   requiredStatusCheckContexts: str ##NON NULL ##LIST
   requiredStatusChecks: RequiredStatusCheckInput ##NON NULL ##LIST
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
   autoTriggerPreferences: CheckSuiteAutoTriggerPreference ##NON NULL ##LIST
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

class TMKWKitems_ProjectV2ItemConnection_Field(ProjectV2ItemConnection):
   class ProjectV2ItemConnectionArgs(GQLArgsSet, GQLObject): 
      after: str
      before: str
      first: int
      last: int

   _args: ProjectV2ItemConnectionArgs



class UpdateProjectV2ItemPositionPayload(GQLObject):
   clientMutationId: str
   items: TMKWKitems_ProjectV2ItemConnection_Field

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
   invalidTopicNames: str ##LIST
   repository: Repository

class VerifyVerifiableDomainPayload(GQLObject):
   clientMutationId: str
   domain: VerifiableDomain

class ViewerHovercardContext(GQLObject):
   message: str ##NON NULL
   octicon: str ##NON NULL
   viewer: User ##NON NULL
