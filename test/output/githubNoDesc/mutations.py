from pygqlmap import GQLMutation
from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *


class abortQueuedMigrations(GQLMutation):
   class AbortQueuedMigrationsPayloadArgs(GQLArgsSet, GQLObject): 
      input: AbortQueuedMigrationsInput ##NON NULL

   _args: AbortQueuedMigrationsPayloadArgs


   type: AbortQueuedMigrationsPayload

class acceptEnterpriseAdministratorInvitation(GQLMutation):
   class AcceptEnterpriseAdministratorInvitationPayloadArgs(GQLArgsSet, GQLObject): 
      input: AcceptEnterpriseAdministratorInvitationInput ##NON NULL

   _args: AcceptEnterpriseAdministratorInvitationPayloadArgs


   type: AcceptEnterpriseAdministratorInvitationPayload

class acceptTopicSuggestion(GQLMutation):
   class AcceptTopicSuggestionPayloadArgs(GQLArgsSet, GQLObject): 
      input: AcceptTopicSuggestionInput ##NON NULL

   _args: AcceptTopicSuggestionPayloadArgs


   type: AcceptTopicSuggestionPayload

class addAssigneesToAssignable(GQLMutation):
   class AddAssigneesToAssignablePayloadArgs(GQLArgsSet, GQLObject): 
      input: AddAssigneesToAssignableInput ##NON NULL

   _args: AddAssigneesToAssignablePayloadArgs


   type: AddAssigneesToAssignablePayload

class addComment(GQLMutation):
   class AddCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddCommentInput ##NON NULL

   _args: AddCommentPayloadArgs


   type: AddCommentPayload

class addDiscussionComment(GQLMutation):
   class AddDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddDiscussionCommentInput ##NON NULL

   _args: AddDiscussionCommentPayloadArgs


   type: AddDiscussionCommentPayload

class addDiscussionPollVote(GQLMutation):
   class AddDiscussionPollVotePayloadArgs(GQLArgsSet, GQLObject): 
      input: AddDiscussionPollVoteInput ##NON NULL

   _args: AddDiscussionPollVotePayloadArgs


   type: AddDiscussionPollVotePayload

class addEnterpriseOrganizationMember(GQLMutation):
   class AddEnterpriseOrganizationMemberPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddEnterpriseOrganizationMemberInput ##NON NULL

   _args: AddEnterpriseOrganizationMemberPayloadArgs


   type: AddEnterpriseOrganizationMemberPayload

class addEnterpriseSupportEntitlement(GQLMutation):
   class AddEnterpriseSupportEntitlementPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddEnterpriseSupportEntitlementInput ##NON NULL

   _args: AddEnterpriseSupportEntitlementPayloadArgs


   type: AddEnterpriseSupportEntitlementPayload

class addLabelsToLabelable(GQLMutation):
   class AddLabelsToLabelablePayloadArgs(GQLArgsSet, GQLObject): 
      input: AddLabelsToLabelableInput ##NON NULL

   _args: AddLabelsToLabelablePayloadArgs


   type: AddLabelsToLabelablePayload

class addProjectCard(GQLMutation):
   class AddProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddProjectCardInput ##NON NULL

   _args: AddProjectCardPayloadArgs


   type: AddProjectCardPayload

class addProjectColumn(GQLMutation):
   class AddProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddProjectColumnInput ##NON NULL

   _args: AddProjectColumnPayloadArgs


   type: AddProjectColumnPayload

class addProjectDraftIssue(GQLMutation):
   class AddProjectDraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: AddProjectDraftIssueInput ##NON NULL

   _args: AddProjectDraftIssuePayloadArgs


   type: AddProjectDraftIssuePayload

class addProjectNextItem(GQLMutation):
   class AddProjectNextItemPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddProjectNextItemInput ##NON NULL

   _args: AddProjectNextItemPayloadArgs


   type: AddProjectNextItemPayload

class addProjectV2DraftIssue(GQLMutation):
   class AddProjectV2DraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: AddProjectV2DraftIssueInput ##NON NULL

   _args: AddProjectV2DraftIssuePayloadArgs


   type: AddProjectV2DraftIssuePayload

class addProjectV2ItemById(GQLMutation):
   class AddProjectV2ItemByIdPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddProjectV2ItemByIdInput ##NON NULL

   _args: AddProjectV2ItemByIdPayloadArgs


   type: AddProjectV2ItemByIdPayload

class addPullRequestReview(GQLMutation):
   class AddPullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddPullRequestReviewInput ##NON NULL

   _args: AddPullRequestReviewPayloadArgs


   type: AddPullRequestReviewPayload

class addPullRequestReviewComment(GQLMutation):
   class AddPullRequestReviewCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddPullRequestReviewCommentInput ##NON NULL

   _args: AddPullRequestReviewCommentPayloadArgs


   type: AddPullRequestReviewCommentPayload

class addPullRequestReviewThread(GQLMutation):
   class AddPullRequestReviewThreadPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddPullRequestReviewThreadInput ##NON NULL

   _args: AddPullRequestReviewThreadPayloadArgs


   type: AddPullRequestReviewThreadPayload

class addReaction(GQLMutation):
   class AddReactionPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddReactionInput ##NON NULL

   _args: AddReactionPayloadArgs


   type: AddReactionPayload

class addStar(GQLMutation):
   class AddStarPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddStarInput ##NON NULL

   _args: AddStarPayloadArgs


   type: AddStarPayload

class addUpvote(GQLMutation):
   class AddUpvotePayloadArgs(GQLArgsSet, GQLObject): 
      input: AddUpvoteInput ##NON NULL

   _args: AddUpvotePayloadArgs


   type: AddUpvotePayload

class addVerifiableDomain(GQLMutation):
   class AddVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      input: AddVerifiableDomainInput ##NON NULL

   _args: AddVerifiableDomainPayloadArgs


   type: AddVerifiableDomainPayload

class approveDeployments(GQLMutation):
   class ApproveDeploymentsPayloadArgs(GQLArgsSet, GQLObject): 
      input: ApproveDeploymentsInput ##NON NULL

   _args: ApproveDeploymentsPayloadArgs


   type: ApproveDeploymentsPayload

class approveVerifiableDomain(GQLMutation):
   class ApproveVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      input: ApproveVerifiableDomainInput ##NON NULL

   _args: ApproveVerifiableDomainPayloadArgs


   type: ApproveVerifiableDomainPayload

class archiveProjectV2Item(GQLMutation):
   class ArchiveProjectV2ItemPayloadArgs(GQLArgsSet, GQLObject): 
      input: ArchiveProjectV2ItemInput ##NON NULL

   _args: ArchiveProjectV2ItemPayloadArgs


   type: ArchiveProjectV2ItemPayload

class archiveRepository(GQLMutation):
   class ArchiveRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: ArchiveRepositoryInput ##NON NULL

   _args: ArchiveRepositoryPayloadArgs


   type: ArchiveRepositoryPayload

class cancelEnterpriseAdminInvitation(GQLMutation):
   class CancelEnterpriseAdminInvitationPayloadArgs(GQLArgsSet, GQLObject): 
      input: CancelEnterpriseAdminInvitationInput ##NON NULL

   _args: CancelEnterpriseAdminInvitationPayloadArgs


   type: CancelEnterpriseAdminInvitationPayload

class cancelSponsorship(GQLMutation):
   class CancelSponsorshipPayloadArgs(GQLArgsSet, GQLObject): 
      input: CancelSponsorshipInput ##NON NULL

   _args: CancelSponsorshipPayloadArgs


   type: CancelSponsorshipPayload

class changeUserStatus(GQLMutation):
   class ChangeUserStatusPayloadArgs(GQLArgsSet, GQLObject): 
      input: ChangeUserStatusInput ##NON NULL

   _args: ChangeUserStatusPayloadArgs


   type: ChangeUserStatusPayload

class clearLabelsFromLabelable(GQLMutation):
   class ClearLabelsFromLabelablePayloadArgs(GQLArgsSet, GQLObject): 
      input: ClearLabelsFromLabelableInput ##NON NULL

   _args: ClearLabelsFromLabelablePayloadArgs


   type: ClearLabelsFromLabelablePayload

class clearProjectV2ItemFieldValue(GQLMutation):
   class ClearProjectV2ItemFieldValuePayloadArgs(GQLArgsSet, GQLObject): 
      input: ClearProjectV2ItemFieldValueInput ##NON NULL

   _args: ClearProjectV2ItemFieldValuePayloadArgs


   type: ClearProjectV2ItemFieldValuePayload

class cloneProject(GQLMutation):
   class CloneProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: CloneProjectInput ##NON NULL

   _args: CloneProjectPayloadArgs


   type: CloneProjectPayload

class cloneTemplateRepository(GQLMutation):
   class CloneTemplateRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: CloneTemplateRepositoryInput ##NON NULL

   _args: CloneTemplateRepositoryPayloadArgs


   type: CloneTemplateRepositoryPayload

class closeIssue(GQLMutation):
   class CloseIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: CloseIssueInput ##NON NULL

   _args: CloseIssuePayloadArgs


   type: CloseIssuePayload

class closePullRequest(GQLMutation):
   class ClosePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      input: ClosePullRequestInput ##NON NULL

   _args: ClosePullRequestPayloadArgs


   type: ClosePullRequestPayload

class convertProjectCardNoteToIssue(GQLMutation):
   class ConvertProjectCardNoteToIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: ConvertProjectCardNoteToIssueInput ##NON NULL

   _args: ConvertProjectCardNoteToIssuePayloadArgs


   type: ConvertProjectCardNoteToIssuePayload

class convertPullRequestToDraft(GQLMutation):
   class ConvertPullRequestToDraftPayloadArgs(GQLArgsSet, GQLObject): 
      input: ConvertPullRequestToDraftInput ##NON NULL

   _args: ConvertPullRequestToDraftPayloadArgs


   type: ConvertPullRequestToDraftPayload

class createAttributionInvitation(GQLMutation):
   class CreateAttributionInvitationPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateAttributionInvitationInput ##NON NULL

   _args: CreateAttributionInvitationPayloadArgs


   type: CreateAttributionInvitationPayload

class createBranchProtectionRule(GQLMutation):
   class CreateBranchProtectionRulePayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateBranchProtectionRuleInput ##NON NULL

   _args: CreateBranchProtectionRulePayloadArgs


   type: CreateBranchProtectionRulePayload

class createCheckRun(GQLMutation):
   class CreateCheckRunPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateCheckRunInput ##NON NULL

   _args: CreateCheckRunPayloadArgs


   type: CreateCheckRunPayload

class createCheckSuite(GQLMutation):
   class CreateCheckSuitePayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateCheckSuiteInput ##NON NULL

   _args: CreateCheckSuitePayloadArgs


   type: CreateCheckSuitePayload

class createCommitOnBranch(GQLMutation):
   class CreateCommitOnBranchPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateCommitOnBranchInput ##NON NULL

   _args: CreateCommitOnBranchPayloadArgs


   type: CreateCommitOnBranchPayload

class createDiscussion(GQLMutation):
   class CreateDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateDiscussionInput ##NON NULL

   _args: CreateDiscussionPayloadArgs


   type: CreateDiscussionPayload

class createEnterpriseOrganization(GQLMutation):
   class CreateEnterpriseOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateEnterpriseOrganizationInput ##NON NULL

   _args: CreateEnterpriseOrganizationPayloadArgs


   type: CreateEnterpriseOrganizationPayload

class createEnvironment(GQLMutation):
   class CreateEnvironmentPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateEnvironmentInput ##NON NULL

   _args: CreateEnvironmentPayloadArgs


   type: CreateEnvironmentPayload

class createIpAllowListEntry(GQLMutation):
   class CreateIpAllowListEntryPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateIpAllowListEntryInput ##NON NULL

   _args: CreateIpAllowListEntryPayloadArgs


   type: CreateIpAllowListEntryPayload

class createIssue(GQLMutation):
   class CreateIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateIssueInput ##NON NULL

   _args: CreateIssuePayloadArgs


   type: CreateIssuePayload

class createLinkedBranch(GQLMutation):
   class CreateLinkedBranchPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateLinkedBranchInput ##NON NULL

   _args: CreateLinkedBranchPayloadArgs


   type: CreateLinkedBranchPayload

class createMigrationSource(GQLMutation):
   class CreateMigrationSourcePayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateMigrationSourceInput ##NON NULL

   _args: CreateMigrationSourcePayloadArgs


   type: CreateMigrationSourcePayload

class createProject(GQLMutation):
   class CreateProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateProjectInput ##NON NULL

   _args: CreateProjectPayloadArgs


   type: CreateProjectPayload

class createProjectV2(GQLMutation):
   class CreateProjectV2PayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateProjectV2Input ##NON NULL

   _args: CreateProjectV2PayloadArgs


   type: CreateProjectV2Payload

class createPullRequest(GQLMutation):
   class CreatePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreatePullRequestInput ##NON NULL

   _args: CreatePullRequestPayloadArgs


   type: CreatePullRequestPayload

class createRef(GQLMutation):
   class CreateRefPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateRefInput ##NON NULL

   _args: CreateRefPayloadArgs


   type: CreateRefPayload

class createRepository(GQLMutation):
   class CreateRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateRepositoryInput ##NON NULL

   _args: CreateRepositoryPayloadArgs


   type: CreateRepositoryPayload

class createSponsorsListing(GQLMutation):
   class CreateSponsorsListingPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateSponsorsListingInput ##NON NULL

   _args: CreateSponsorsListingPayloadArgs


   type: CreateSponsorsListingPayload

class createSponsorsTier(GQLMutation):
   class CreateSponsorsTierPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateSponsorsTierInput ##NON NULL

   _args: CreateSponsorsTierPayloadArgs


   type: CreateSponsorsTierPayload

class createSponsorship(GQLMutation):
   class CreateSponsorshipPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateSponsorshipInput ##NON NULL

   _args: CreateSponsorshipPayloadArgs


   type: CreateSponsorshipPayload

class createTeamDiscussion(GQLMutation):
   class CreateTeamDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateTeamDiscussionInput ##NON NULL

   _args: CreateTeamDiscussionPayloadArgs


   type: CreateTeamDiscussionPayload

class createTeamDiscussionComment(GQLMutation):
   class CreateTeamDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: CreateTeamDiscussionCommentInput ##NON NULL

   _args: CreateTeamDiscussionCommentPayloadArgs


   type: CreateTeamDiscussionCommentPayload

class declineTopicSuggestion(GQLMutation):
   class DeclineTopicSuggestionPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeclineTopicSuggestionInput ##NON NULL

   _args: DeclineTopicSuggestionPayloadArgs


   type: DeclineTopicSuggestionPayload

class deleteBranchProtectionRule(GQLMutation):
   class DeleteBranchProtectionRulePayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteBranchProtectionRuleInput ##NON NULL

   _args: DeleteBranchProtectionRulePayloadArgs


   type: DeleteBranchProtectionRulePayload

class deleteDeployment(GQLMutation):
   class DeleteDeploymentPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteDeploymentInput ##NON NULL

   _args: DeleteDeploymentPayloadArgs


   type: DeleteDeploymentPayload

class deleteDiscussion(GQLMutation):
   class DeleteDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteDiscussionInput ##NON NULL

   _args: DeleteDiscussionPayloadArgs


   type: DeleteDiscussionPayload

class deleteDiscussionComment(GQLMutation):
   class DeleteDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteDiscussionCommentInput ##NON NULL

   _args: DeleteDiscussionCommentPayloadArgs


   type: DeleteDiscussionCommentPayload

class deleteEnvironment(GQLMutation):
   class DeleteEnvironmentPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteEnvironmentInput ##NON NULL

   _args: DeleteEnvironmentPayloadArgs


   type: DeleteEnvironmentPayload

class deleteIpAllowListEntry(GQLMutation):
   class DeleteIpAllowListEntryPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteIpAllowListEntryInput ##NON NULL

   _args: DeleteIpAllowListEntryPayloadArgs


   type: DeleteIpAllowListEntryPayload

class deleteIssue(GQLMutation):
   class DeleteIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteIssueInput ##NON NULL

   _args: DeleteIssuePayloadArgs


   type: DeleteIssuePayload

class deleteIssueComment(GQLMutation):
   class DeleteIssueCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteIssueCommentInput ##NON NULL

   _args: DeleteIssueCommentPayloadArgs


   type: DeleteIssueCommentPayload

class deleteLinkedBranch(GQLMutation):
   class DeleteLinkedBranchPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteLinkedBranchInput ##NON NULL

   _args: DeleteLinkedBranchPayloadArgs


   type: DeleteLinkedBranchPayload

class deleteProject(GQLMutation):
   class DeleteProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteProjectInput ##NON NULL

   _args: DeleteProjectPayloadArgs


   type: DeleteProjectPayload

class deleteProjectCard(GQLMutation):
   class DeleteProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteProjectCardInput ##NON NULL

   _args: DeleteProjectCardPayloadArgs


   type: DeleteProjectCardPayload

class deleteProjectColumn(GQLMutation):
   class DeleteProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteProjectColumnInput ##NON NULL

   _args: DeleteProjectColumnPayloadArgs


   type: DeleteProjectColumnPayload

class deleteProjectNextItem(GQLMutation):
   class DeleteProjectNextItemPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteProjectNextItemInput ##NON NULL

   _args: DeleteProjectNextItemPayloadArgs


   type: DeleteProjectNextItemPayload

class deleteProjectV2Item(GQLMutation):
   class DeleteProjectV2ItemPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteProjectV2ItemInput ##NON NULL

   _args: DeleteProjectV2ItemPayloadArgs


   type: DeleteProjectV2ItemPayload

class deletePullRequestReview(GQLMutation):
   class DeletePullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeletePullRequestReviewInput ##NON NULL

   _args: DeletePullRequestReviewPayloadArgs


   type: DeletePullRequestReviewPayload

class deletePullRequestReviewComment(GQLMutation):
   class DeletePullRequestReviewCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeletePullRequestReviewCommentInput ##NON NULL

   _args: DeletePullRequestReviewCommentPayloadArgs


   type: DeletePullRequestReviewCommentPayload

class deleteRef(GQLMutation):
   class DeleteRefPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteRefInput ##NON NULL

   _args: DeleteRefPayloadArgs


   type: DeleteRefPayload

class deleteTeamDiscussion(GQLMutation):
   class DeleteTeamDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteTeamDiscussionInput ##NON NULL

   _args: DeleteTeamDiscussionPayloadArgs


   type: DeleteTeamDiscussionPayload

class deleteTeamDiscussionComment(GQLMutation):
   class DeleteTeamDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteTeamDiscussionCommentInput ##NON NULL

   _args: DeleteTeamDiscussionCommentPayloadArgs


   type: DeleteTeamDiscussionCommentPayload

class deleteVerifiableDomain(GQLMutation):
   class DeleteVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      input: DeleteVerifiableDomainInput ##NON NULL

   _args: DeleteVerifiableDomainPayloadArgs


   type: DeleteVerifiableDomainPayload

class disablePullRequestAutoMerge(GQLMutation):
   class DisablePullRequestAutoMergePayloadArgs(GQLArgsSet, GQLObject): 
      input: DisablePullRequestAutoMergeInput ##NON NULL

   _args: DisablePullRequestAutoMergePayloadArgs


   type: DisablePullRequestAutoMergePayload

class dismissPullRequestReview(GQLMutation):
   class DismissPullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: DismissPullRequestReviewInput ##NON NULL

   _args: DismissPullRequestReviewPayloadArgs


   type: DismissPullRequestReviewPayload

class dismissRepositoryVulnerabilityAlert(GQLMutation):
   class DismissRepositoryVulnerabilityAlertPayloadArgs(GQLArgsSet, GQLObject): 
      input: DismissRepositoryVulnerabilityAlertInput ##NON NULL

   _args: DismissRepositoryVulnerabilityAlertPayloadArgs


   type: DismissRepositoryVulnerabilityAlertPayload

class enablePullRequestAutoMerge(GQLMutation):
   class EnablePullRequestAutoMergePayloadArgs(GQLArgsSet, GQLObject): 
      input: EnablePullRequestAutoMergeInput ##NON NULL

   _args: EnablePullRequestAutoMergePayloadArgs


   type: EnablePullRequestAutoMergePayload

class followOrganization(GQLMutation):
   class FollowOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      input: FollowOrganizationInput ##NON NULL

   _args: FollowOrganizationPayloadArgs


   type: FollowOrganizationPayload

class followUser(GQLMutation):
   class FollowUserPayloadArgs(GQLArgsSet, GQLObject): 
      input: FollowUserInput ##NON NULL

   _args: FollowUserPayloadArgs


   type: FollowUserPayload

class grantEnterpriseOrganizationsMigratorRole(GQLMutation):
   class GrantEnterpriseOrganizationsMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: GrantEnterpriseOrganizationsMigratorRoleInput ##NON NULL

   _args: GrantEnterpriseOrganizationsMigratorRolePayloadArgs


   type: GrantEnterpriseOrganizationsMigratorRolePayload

class grantMigratorRole(GQLMutation):
   class GrantMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: GrantMigratorRoleInput ##NON NULL

   _args: GrantMigratorRolePayloadArgs


   type: GrantMigratorRolePayload

class inviteEnterpriseAdmin(GQLMutation):
   class InviteEnterpriseAdminPayloadArgs(GQLArgsSet, GQLObject): 
      input: InviteEnterpriseAdminInput ##NON NULL

   _args: InviteEnterpriseAdminPayloadArgs


   type: InviteEnterpriseAdminPayload

class linkProjectV2ToRepository(GQLMutation):
   class LinkProjectV2ToRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: LinkProjectV2ToRepositoryInput ##NON NULL

   _args: LinkProjectV2ToRepositoryPayloadArgs


   type: LinkProjectV2ToRepositoryPayload

class linkProjectV2ToTeam(GQLMutation):
   class LinkProjectV2ToTeamPayloadArgs(GQLArgsSet, GQLObject): 
      input: LinkProjectV2ToTeamInput ##NON NULL

   _args: LinkProjectV2ToTeamPayloadArgs


   type: LinkProjectV2ToTeamPayload

class linkRepositoryToProject(GQLMutation):
   class LinkRepositoryToProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: LinkRepositoryToProjectInput ##NON NULL

   _args: LinkRepositoryToProjectPayloadArgs


   type: LinkRepositoryToProjectPayload

class lockLockable(GQLMutation):
   class LockLockablePayloadArgs(GQLArgsSet, GQLObject): 
      input: LockLockableInput ##NON NULL

   _args: LockLockablePayloadArgs


   type: LockLockablePayload

class markDiscussionCommentAsAnswer(GQLMutation):
   class MarkDiscussionCommentAsAnswerPayloadArgs(GQLArgsSet, GQLObject): 
      input: MarkDiscussionCommentAsAnswerInput ##NON NULL

   _args: MarkDiscussionCommentAsAnswerPayloadArgs


   type: MarkDiscussionCommentAsAnswerPayload

class markFileAsViewed(GQLMutation):
   class MarkFileAsViewedPayloadArgs(GQLArgsSet, GQLObject): 
      input: MarkFileAsViewedInput ##NON NULL

   _args: MarkFileAsViewedPayloadArgs


   type: MarkFileAsViewedPayload

class markPullRequestReadyForReview(GQLMutation):
   class MarkPullRequestReadyForReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: MarkPullRequestReadyForReviewInput ##NON NULL

   _args: MarkPullRequestReadyForReviewPayloadArgs


   type: MarkPullRequestReadyForReviewPayload

class mergeBranch(GQLMutation):
   class MergeBranchPayloadArgs(GQLArgsSet, GQLObject): 
      input: MergeBranchInput ##NON NULL

   _args: MergeBranchPayloadArgs


   type: MergeBranchPayload

class mergePullRequest(GQLMutation):
   class MergePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      input: MergePullRequestInput ##NON NULL

   _args: MergePullRequestPayloadArgs


   type: MergePullRequestPayload

class minimizeComment(GQLMutation):
   class MinimizeCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: MinimizeCommentInput ##NON NULL

   _args: MinimizeCommentPayloadArgs


   type: MinimizeCommentPayload

class moveProjectCard(GQLMutation):
   class MoveProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      input: MoveProjectCardInput ##NON NULL

   _args: MoveProjectCardPayloadArgs


   type: MoveProjectCardPayload

class moveProjectColumn(GQLMutation):
   class MoveProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      input: MoveProjectColumnInput ##NON NULL

   _args: MoveProjectColumnPayloadArgs


   type: MoveProjectColumnPayload

class pinIssue(GQLMutation):
   class PinIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: PinIssueInput ##NON NULL

   _args: PinIssuePayloadArgs


   type: PinIssuePayload

class publishSponsorsTier(GQLMutation):
   class PublishSponsorsTierPayloadArgs(GQLArgsSet, GQLObject): 
      input: PublishSponsorsTierInput ##NON NULL

   _args: PublishSponsorsTierPayloadArgs


   type: PublishSponsorsTierPayload

class regenerateEnterpriseIdentityProviderRecoveryCodes(GQLMutation):
   class RegenerateEnterpriseIdentityProviderRecoveryCodesPayloadArgs(GQLArgsSet, GQLObject): 
      input: RegenerateEnterpriseIdentityProviderRecoveryCodesInput ##NON NULL

   _args: RegenerateEnterpriseIdentityProviderRecoveryCodesPayloadArgs


   type: RegenerateEnterpriseIdentityProviderRecoveryCodesPayload

class regenerateVerifiableDomainToken(GQLMutation):
   class RegenerateVerifiableDomainTokenPayloadArgs(GQLArgsSet, GQLObject): 
      input: RegenerateVerifiableDomainTokenInput ##NON NULL

   _args: RegenerateVerifiableDomainTokenPayloadArgs


   type: RegenerateVerifiableDomainTokenPayload

class rejectDeployments(GQLMutation):
   class RejectDeploymentsPayloadArgs(GQLArgsSet, GQLObject): 
      input: RejectDeploymentsInput ##NON NULL

   _args: RejectDeploymentsPayloadArgs


   type: RejectDeploymentsPayload

class removeAssigneesFromAssignable(GQLMutation):
   class RemoveAssigneesFromAssignablePayloadArgs(GQLArgsSet, GQLObject): 
      input: RemoveAssigneesFromAssignableInput ##NON NULL

   _args: RemoveAssigneesFromAssignablePayloadArgs


   type: RemoveAssigneesFromAssignablePayload

class removeEnterpriseAdmin(GQLMutation):
   class RemoveEnterpriseAdminPayloadArgs(GQLArgsSet, GQLObject): 
      input: RemoveEnterpriseAdminInput ##NON NULL

   _args: RemoveEnterpriseAdminPayloadArgs


   type: RemoveEnterpriseAdminPayload

class removeEnterpriseIdentityProvider(GQLMutation):
   class RemoveEnterpriseIdentityProviderPayloadArgs(GQLArgsSet, GQLObject): 
      input: RemoveEnterpriseIdentityProviderInput ##NON NULL

   _args: RemoveEnterpriseIdentityProviderPayloadArgs


   type: RemoveEnterpriseIdentityProviderPayload

class removeEnterpriseOrganization(GQLMutation):
   class RemoveEnterpriseOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      input: RemoveEnterpriseOrganizationInput ##NON NULL

   _args: RemoveEnterpriseOrganizationPayloadArgs


   type: RemoveEnterpriseOrganizationPayload

class removeEnterpriseSupportEntitlement(GQLMutation):
   class RemoveEnterpriseSupportEntitlementPayloadArgs(GQLArgsSet, GQLObject): 
      input: RemoveEnterpriseSupportEntitlementInput ##NON NULL

   _args: RemoveEnterpriseSupportEntitlementPayloadArgs


   type: RemoveEnterpriseSupportEntitlementPayload

class removeLabelsFromLabelable(GQLMutation):
   class RemoveLabelsFromLabelablePayloadArgs(GQLArgsSet, GQLObject): 
      input: RemoveLabelsFromLabelableInput ##NON NULL

   _args: RemoveLabelsFromLabelablePayloadArgs


   type: RemoveLabelsFromLabelablePayload

class removeOutsideCollaborator(GQLMutation):
   class RemoveOutsideCollaboratorPayloadArgs(GQLArgsSet, GQLObject): 
      input: RemoveOutsideCollaboratorInput ##NON NULL

   _args: RemoveOutsideCollaboratorPayloadArgs


   type: RemoveOutsideCollaboratorPayload

class removeReaction(GQLMutation):
   class RemoveReactionPayloadArgs(GQLArgsSet, GQLObject): 
      input: RemoveReactionInput ##NON NULL

   _args: RemoveReactionPayloadArgs


   type: RemoveReactionPayload

class removeStar(GQLMutation):
   class RemoveStarPayloadArgs(GQLArgsSet, GQLObject): 
      input: RemoveStarInput ##NON NULL

   _args: RemoveStarPayloadArgs


   type: RemoveStarPayload

class removeUpvote(GQLMutation):
   class RemoveUpvotePayloadArgs(GQLArgsSet, GQLObject): 
      input: RemoveUpvoteInput ##NON NULL

   _args: RemoveUpvotePayloadArgs


   type: RemoveUpvotePayload

class reopenIssue(GQLMutation):
   class ReopenIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: ReopenIssueInput ##NON NULL

   _args: ReopenIssuePayloadArgs


   type: ReopenIssuePayload

class reopenPullRequest(GQLMutation):
   class ReopenPullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      input: ReopenPullRequestInput ##NON NULL

   _args: ReopenPullRequestPayloadArgs


   type: ReopenPullRequestPayload

class requestReviews(GQLMutation):
   class RequestReviewsPayloadArgs(GQLArgsSet, GQLObject): 
      input: RequestReviewsInput ##NON NULL

   _args: RequestReviewsPayloadArgs


   type: RequestReviewsPayload

class rerequestCheckSuite(GQLMutation):
   class RerequestCheckSuitePayloadArgs(GQLArgsSet, GQLObject): 
      input: RerequestCheckSuiteInput ##NON NULL

   _args: RerequestCheckSuitePayloadArgs


   type: RerequestCheckSuitePayload

class resolveReviewThread(GQLMutation):
   class ResolveReviewThreadPayloadArgs(GQLArgsSet, GQLObject): 
      input: ResolveReviewThreadInput ##NON NULL

   _args: ResolveReviewThreadPayloadArgs


   type: ResolveReviewThreadPayload

class revokeEnterpriseOrganizationsMigratorRole(GQLMutation):
   class RevokeEnterpriseOrganizationsMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: RevokeEnterpriseOrganizationsMigratorRoleInput ##NON NULL

   _args: RevokeEnterpriseOrganizationsMigratorRolePayloadArgs


   type: RevokeEnterpriseOrganizationsMigratorRolePayload

class revokeMigratorRole(GQLMutation):
   class RevokeMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: RevokeMigratorRoleInput ##NON NULL

   _args: RevokeMigratorRolePayloadArgs


   type: RevokeMigratorRolePayload

class setEnterpriseIdentityProvider(GQLMutation):
   class SetEnterpriseIdentityProviderPayloadArgs(GQLArgsSet, GQLObject): 
      input: SetEnterpriseIdentityProviderInput ##NON NULL

   _args: SetEnterpriseIdentityProviderPayloadArgs


   type: SetEnterpriseIdentityProviderPayload

class setOrganizationInteractionLimit(GQLMutation):
   class SetOrganizationInteractionLimitPayloadArgs(GQLArgsSet, GQLObject): 
      input: SetOrganizationInteractionLimitInput ##NON NULL

   _args: SetOrganizationInteractionLimitPayloadArgs


   type: SetOrganizationInteractionLimitPayload

class setRepositoryInteractionLimit(GQLMutation):
   class SetRepositoryInteractionLimitPayloadArgs(GQLArgsSet, GQLObject): 
      input: SetRepositoryInteractionLimitInput ##NON NULL

   _args: SetRepositoryInteractionLimitPayloadArgs


   type: SetRepositoryInteractionLimitPayload

class setUserInteractionLimit(GQLMutation):
   class SetUserInteractionLimitPayloadArgs(GQLArgsSet, GQLObject): 
      input: SetUserInteractionLimitInput ##NON NULL

   _args: SetUserInteractionLimitPayloadArgs


   type: SetUserInteractionLimitPayload

class startRepositoryMigration(GQLMutation):
   class StartRepositoryMigrationPayloadArgs(GQLArgsSet, GQLObject): 
      input: StartRepositoryMigrationInput ##NON NULL

   _args: StartRepositoryMigrationPayloadArgs


   type: StartRepositoryMigrationPayload

class submitPullRequestReview(GQLMutation):
   class SubmitPullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: SubmitPullRequestReviewInput ##NON NULL

   _args: SubmitPullRequestReviewPayloadArgs


   type: SubmitPullRequestReviewPayload

class transferEnterpriseOrganization(GQLMutation):
   class TransferEnterpriseOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      input: TransferEnterpriseOrganizationInput ##NON NULL

   _args: TransferEnterpriseOrganizationPayloadArgs


   type: TransferEnterpriseOrganizationPayload

class transferIssue(GQLMutation):
   class TransferIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: TransferIssueInput ##NON NULL

   _args: TransferIssuePayloadArgs


   type: TransferIssuePayload

class unarchiveProjectV2Item(GQLMutation):
   class UnarchiveProjectV2ItemPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnarchiveProjectV2ItemInput ##NON NULL

   _args: UnarchiveProjectV2ItemPayloadArgs


   type: UnarchiveProjectV2ItemPayload

class unarchiveRepository(GQLMutation):
   class UnarchiveRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnarchiveRepositoryInput ##NON NULL

   _args: UnarchiveRepositoryPayloadArgs


   type: UnarchiveRepositoryPayload

class unfollowOrganization(GQLMutation):
   class UnfollowOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnfollowOrganizationInput ##NON NULL

   _args: UnfollowOrganizationPayloadArgs


   type: UnfollowOrganizationPayload

class unfollowUser(GQLMutation):
   class UnfollowUserPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnfollowUserInput ##NON NULL

   _args: UnfollowUserPayloadArgs


   type: UnfollowUserPayload

class unlinkProjectV2FromRepository(GQLMutation):
   class UnlinkProjectV2FromRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnlinkProjectV2FromRepositoryInput ##NON NULL

   _args: UnlinkProjectV2FromRepositoryPayloadArgs


   type: UnlinkProjectV2FromRepositoryPayload

class unlinkProjectV2FromTeam(GQLMutation):
   class UnlinkProjectV2FromTeamPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnlinkProjectV2FromTeamInput ##NON NULL

   _args: UnlinkProjectV2FromTeamPayloadArgs


   type: UnlinkProjectV2FromTeamPayload

class unlinkRepositoryFromProject(GQLMutation):
   class UnlinkRepositoryFromProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnlinkRepositoryFromProjectInput ##NON NULL

   _args: UnlinkRepositoryFromProjectPayloadArgs


   type: UnlinkRepositoryFromProjectPayload

class unlockLockable(GQLMutation):
   class UnlockLockablePayloadArgs(GQLArgsSet, GQLObject): 
      input: UnlockLockableInput ##NON NULL

   _args: UnlockLockablePayloadArgs


   type: UnlockLockablePayload

class unmarkDiscussionCommentAsAnswer(GQLMutation):
   class UnmarkDiscussionCommentAsAnswerPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnmarkDiscussionCommentAsAnswerInput ##NON NULL

   _args: UnmarkDiscussionCommentAsAnswerPayloadArgs


   type: UnmarkDiscussionCommentAsAnswerPayload

class unmarkFileAsViewed(GQLMutation):
   class UnmarkFileAsViewedPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnmarkFileAsViewedInput ##NON NULL

   _args: UnmarkFileAsViewedPayloadArgs


   type: UnmarkFileAsViewedPayload

class unmarkIssueAsDuplicate(GQLMutation):
   class UnmarkIssueAsDuplicatePayloadArgs(GQLArgsSet, GQLObject): 
      input: UnmarkIssueAsDuplicateInput ##NON NULL

   _args: UnmarkIssueAsDuplicatePayloadArgs


   type: UnmarkIssueAsDuplicatePayload

class unminimizeComment(GQLMutation):
   class UnminimizeCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnminimizeCommentInput ##NON NULL

   _args: UnminimizeCommentPayloadArgs


   type: UnminimizeCommentPayload

class unpinIssue(GQLMutation):
   class UnpinIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: UnpinIssueInput ##NON NULL

   _args: UnpinIssuePayloadArgs


   type: UnpinIssuePayload

class unresolveReviewThread(GQLMutation):
   class UnresolveReviewThreadPayloadArgs(GQLArgsSet, GQLObject): 
      input: UnresolveReviewThreadInput ##NON NULL

   _args: UnresolveReviewThreadPayloadArgs


   type: UnresolveReviewThreadPayload

class updateBranchProtectionRule(GQLMutation):
   class UpdateBranchProtectionRulePayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateBranchProtectionRuleInput ##NON NULL

   _args: UpdateBranchProtectionRulePayloadArgs


   type: UpdateBranchProtectionRulePayload

class updateCheckRun(GQLMutation):
   class UpdateCheckRunPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateCheckRunInput ##NON NULL

   _args: UpdateCheckRunPayloadArgs


   type: UpdateCheckRunPayload

class updateCheckSuitePreferences(GQLMutation):
   class UpdateCheckSuitePreferencesPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateCheckSuitePreferencesInput ##NON NULL

   _args: UpdateCheckSuitePreferencesPayloadArgs


   type: UpdateCheckSuitePreferencesPayload

class updateDiscussion(GQLMutation):
   class UpdateDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateDiscussionInput ##NON NULL

   _args: UpdateDiscussionPayloadArgs


   type: UpdateDiscussionPayload

class updateDiscussionComment(GQLMutation):
   class UpdateDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateDiscussionCommentInput ##NON NULL

   _args: UpdateDiscussionCommentPayloadArgs


   type: UpdateDiscussionCommentPayload

class updateEnterpriseAdministratorRole(GQLMutation):
   class UpdateEnterpriseAdministratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseAdministratorRoleInput ##NON NULL

   _args: UpdateEnterpriseAdministratorRolePayloadArgs


   type: UpdateEnterpriseAdministratorRolePayload

class updateEnterpriseAllowPrivateRepositoryForkingSetting(GQLMutation):
   class UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput ##NON NULL

   _args: UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayloadArgs


   type: UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload

class updateEnterpriseDefaultRepositoryPermissionSetting(GQLMutation):
   class UpdateEnterpriseDefaultRepositoryPermissionSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseDefaultRepositoryPermissionSettingInput ##NON NULL

   _args: UpdateEnterpriseDefaultRepositoryPermissionSettingPayloadArgs


   type: UpdateEnterpriseDefaultRepositoryPermissionSettingPayload

class updateEnterpriseMembersCanChangeRepositoryVisibilitySetting(GQLMutation):
   class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput ##NON NULL

   _args: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayloadArgs


   type: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload

class updateEnterpriseMembersCanCreateRepositoriesSetting(GQLMutation):
   class UpdateEnterpriseMembersCanCreateRepositoriesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanCreateRepositoriesSettingInput ##NON NULL

   _args: UpdateEnterpriseMembersCanCreateRepositoriesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload

class updateEnterpriseMembersCanDeleteIssuesSetting(GQLMutation):
   class UpdateEnterpriseMembersCanDeleteIssuesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanDeleteIssuesSettingInput ##NON NULL

   _args: UpdateEnterpriseMembersCanDeleteIssuesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanDeleteIssuesSettingPayload

class updateEnterpriseMembersCanDeleteRepositoriesSetting(GQLMutation):
   class UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput ##NON NULL

   _args: UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload

class updateEnterpriseMembersCanInviteCollaboratorsSetting(GQLMutation):
   class UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput ##NON NULL

   _args: UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayloadArgs


   type: UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload

class updateEnterpriseMembersCanMakePurchasesSetting(GQLMutation):
   class UpdateEnterpriseMembersCanMakePurchasesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanMakePurchasesSettingInput ##NON NULL

   _args: UpdateEnterpriseMembersCanMakePurchasesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanMakePurchasesSettingPayload

class updateEnterpriseMembersCanUpdateProtectedBranchesSetting(GQLMutation):
   class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput ##NON NULL

   _args: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload

class updateEnterpriseMembersCanViewDependencyInsightsSetting(GQLMutation):
   class UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput ##NON NULL

   _args: UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayloadArgs


   type: UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload

class updateEnterpriseOrganizationProjectsSetting(GQLMutation):
   class UpdateEnterpriseOrganizationProjectsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseOrganizationProjectsSettingInput ##NON NULL

   _args: UpdateEnterpriseOrganizationProjectsSettingPayloadArgs


   type: UpdateEnterpriseOrganizationProjectsSettingPayload

class updateEnterpriseOwnerOrganizationRole(GQLMutation):
   class UpdateEnterpriseOwnerOrganizationRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseOwnerOrganizationRoleInput ##NON NULL

   _args: UpdateEnterpriseOwnerOrganizationRolePayloadArgs


   type: UpdateEnterpriseOwnerOrganizationRolePayload

class updateEnterpriseProfile(GQLMutation):
   class UpdateEnterpriseProfilePayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseProfileInput ##NON NULL

   _args: UpdateEnterpriseProfilePayloadArgs


   type: UpdateEnterpriseProfilePayload

class updateEnterpriseRepositoryProjectsSetting(GQLMutation):
   class UpdateEnterpriseRepositoryProjectsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseRepositoryProjectsSettingInput ##NON NULL

   _args: UpdateEnterpriseRepositoryProjectsSettingPayloadArgs


   type: UpdateEnterpriseRepositoryProjectsSettingPayload

class updateEnterpriseTeamDiscussionsSetting(GQLMutation):
   class UpdateEnterpriseTeamDiscussionsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseTeamDiscussionsSettingInput ##NON NULL

   _args: UpdateEnterpriseTeamDiscussionsSettingPayloadArgs


   type: UpdateEnterpriseTeamDiscussionsSettingPayload

class updateEnterpriseTwoFactorAuthenticationRequiredSetting(GQLMutation):
   class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput ##NON NULL

   _args: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayloadArgs


   type: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload

class updateEnvironment(GQLMutation):
   class UpdateEnvironmentPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateEnvironmentInput ##NON NULL

   _args: UpdateEnvironmentPayloadArgs


   type: UpdateEnvironmentPayload

class updateIpAllowListEnabledSetting(GQLMutation):
   class UpdateIpAllowListEnabledSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateIpAllowListEnabledSettingInput ##NON NULL

   _args: UpdateIpAllowListEnabledSettingPayloadArgs


   type: UpdateIpAllowListEnabledSettingPayload

class updateIpAllowListEntry(GQLMutation):
   class UpdateIpAllowListEntryPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateIpAllowListEntryInput ##NON NULL

   _args: UpdateIpAllowListEntryPayloadArgs


   type: UpdateIpAllowListEntryPayload

class updateIpAllowListForInstalledAppsEnabledSetting(GQLMutation):
   class UpdateIpAllowListForInstalledAppsEnabledSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateIpAllowListForInstalledAppsEnabledSettingInput ##NON NULL

   _args: UpdateIpAllowListForInstalledAppsEnabledSettingPayloadArgs


   type: UpdateIpAllowListForInstalledAppsEnabledSettingPayload

class updateIssue(GQLMutation):
   class UpdateIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateIssueInput ##NON NULL

   _args: UpdateIssuePayloadArgs


   type: UpdateIssuePayload

class updateIssueComment(GQLMutation):
   class UpdateIssueCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateIssueCommentInput ##NON NULL

   _args: UpdateIssueCommentPayloadArgs


   type: UpdateIssueCommentPayload

class updateNotificationRestrictionSetting(GQLMutation):
   class UpdateNotificationRestrictionSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateNotificationRestrictionSettingInput ##NON NULL

   _args: UpdateNotificationRestrictionSettingPayloadArgs


   type: UpdateNotificationRestrictionSettingPayload

class updateOrganizationAllowPrivateRepositoryForkingSetting(GQLMutation):
   class UpdateOrganizationAllowPrivateRepositoryForkingSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateOrganizationAllowPrivateRepositoryForkingSettingInput ##NON NULL

   _args: UpdateOrganizationAllowPrivateRepositoryForkingSettingPayloadArgs


   type: UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload

class updateOrganizationWebCommitSignoffSetting(GQLMutation):
   class UpdateOrganizationWebCommitSignoffSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateOrganizationWebCommitSignoffSettingInput ##NON NULL

   _args: UpdateOrganizationWebCommitSignoffSettingPayloadArgs


   type: UpdateOrganizationWebCommitSignoffSettingPayload

class updateProject(GQLMutation):
   class UpdateProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateProjectInput ##NON NULL

   _args: UpdateProjectPayloadArgs


   type: UpdateProjectPayload

class updateProjectCard(GQLMutation):
   class UpdateProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateProjectCardInput ##NON NULL

   _args: UpdateProjectCardPayloadArgs


   type: UpdateProjectCardPayload

class updateProjectColumn(GQLMutation):
   class UpdateProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateProjectColumnInput ##NON NULL

   _args: UpdateProjectColumnPayloadArgs


   type: UpdateProjectColumnPayload

class updateProjectDraftIssue(GQLMutation):
   class UpdateProjectDraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateProjectDraftIssueInput ##NON NULL

   _args: UpdateProjectDraftIssuePayloadArgs


   type: UpdateProjectDraftIssuePayload

class updateProjectNext(GQLMutation):
   class UpdateProjectNextPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateProjectNextInput ##NON NULL

   _args: UpdateProjectNextPayloadArgs


   type: UpdateProjectNextPayload

class updateProjectNextItemField(GQLMutation):
   class UpdateProjectNextItemFieldPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateProjectNextItemFieldInput ##NON NULL

   _args: UpdateProjectNextItemFieldPayloadArgs


   type: UpdateProjectNextItemFieldPayload

class updateProjectV2(GQLMutation):
   class UpdateProjectV2PayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateProjectV2Input ##NON NULL

   _args: UpdateProjectV2PayloadArgs


   type: UpdateProjectV2Payload

class updateProjectV2DraftIssue(GQLMutation):
   class UpdateProjectV2DraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateProjectV2DraftIssueInput ##NON NULL

   _args: UpdateProjectV2DraftIssuePayloadArgs


   type: UpdateProjectV2DraftIssuePayload

class updateProjectV2ItemFieldValue(GQLMutation):
   class UpdateProjectV2ItemFieldValuePayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateProjectV2ItemFieldValueInput ##NON NULL

   _args: UpdateProjectV2ItemFieldValuePayloadArgs


   type: UpdateProjectV2ItemFieldValuePayload

class updateProjectV2ItemPosition(GQLMutation):
   class UpdateProjectV2ItemPositionPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateProjectV2ItemPositionInput ##NON NULL

   _args: UpdateProjectV2ItemPositionPayloadArgs


   type: UpdateProjectV2ItemPositionPayload

class updatePullRequest(GQLMutation):
   class UpdatePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdatePullRequestInput ##NON NULL

   _args: UpdatePullRequestPayloadArgs


   type: UpdatePullRequestPayload

class updatePullRequestBranch(GQLMutation):
   class UpdatePullRequestBranchPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdatePullRequestBranchInput ##NON NULL

   _args: UpdatePullRequestBranchPayloadArgs


   type: UpdatePullRequestBranchPayload

class updatePullRequestReview(GQLMutation):
   class UpdatePullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdatePullRequestReviewInput ##NON NULL

   _args: UpdatePullRequestReviewPayloadArgs


   type: UpdatePullRequestReviewPayload

class updatePullRequestReviewComment(GQLMutation):
   class UpdatePullRequestReviewCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdatePullRequestReviewCommentInput ##NON NULL

   _args: UpdatePullRequestReviewCommentPayloadArgs


   type: UpdatePullRequestReviewCommentPayload

class updateRef(GQLMutation):
   class UpdateRefPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateRefInput ##NON NULL

   _args: UpdateRefPayloadArgs


   type: UpdateRefPayload

class updateRepository(GQLMutation):
   class UpdateRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateRepositoryInput ##NON NULL

   _args: UpdateRepositoryPayloadArgs


   type: UpdateRepositoryPayload

class updateRepositoryWebCommitSignoffSetting(GQLMutation):
   class UpdateRepositoryWebCommitSignoffSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateRepositoryWebCommitSignoffSettingInput ##NON NULL

   _args: UpdateRepositoryWebCommitSignoffSettingPayloadArgs


   type: UpdateRepositoryWebCommitSignoffSettingPayload

class updateSponsorshipPreferences(GQLMutation):
   class UpdateSponsorshipPreferencesPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateSponsorshipPreferencesInput ##NON NULL

   _args: UpdateSponsorshipPreferencesPayloadArgs


   type: UpdateSponsorshipPreferencesPayload

class updateSubscription(GQLMutation):
   class UpdateSubscriptionPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateSubscriptionInput ##NON NULL

   _args: UpdateSubscriptionPayloadArgs


   type: UpdateSubscriptionPayload

class updateTeamDiscussion(GQLMutation):
   class UpdateTeamDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateTeamDiscussionInput ##NON NULL

   _args: UpdateTeamDiscussionPayloadArgs


   type: UpdateTeamDiscussionPayload

class updateTeamDiscussionComment(GQLMutation):
   class UpdateTeamDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateTeamDiscussionCommentInput ##NON NULL

   _args: UpdateTeamDiscussionCommentPayloadArgs


   type: UpdateTeamDiscussionCommentPayload

class updateTeamsRepository(GQLMutation):
   class UpdateTeamsRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateTeamsRepositoryInput ##NON NULL

   _args: UpdateTeamsRepositoryPayloadArgs


   type: UpdateTeamsRepositoryPayload

class updateTopics(GQLMutation):
   class UpdateTopicsPayloadArgs(GQLArgsSet, GQLObject): 
      input: UpdateTopicsInput ##NON NULL

   _args: UpdateTopicsPayloadArgs


   type: UpdateTopicsPayload

class verifyVerifiableDomain(GQLMutation):
   class VerifyVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      input: VerifyVerifiableDomainInput ##NON NULL

   _args: VerifyVerifiableDomainPayloadArgs


   type: VerifyVerifiableDomainPayload


class Mutations(Enum):
   abortQueuedMigrations = abortQueuedMigrations
   acceptEnterpriseAdministratorInvitation = acceptEnterpriseAdministratorInvitation
   acceptTopicSuggestion = acceptTopicSuggestion
   addAssigneesToAssignable = addAssigneesToAssignable
   addComment = addComment
   addDiscussionComment = addDiscussionComment
   addDiscussionPollVote = addDiscussionPollVote
   addEnterpriseOrganizationMember = addEnterpriseOrganizationMember
   addEnterpriseSupportEntitlement = addEnterpriseSupportEntitlement
   addLabelsToLabelable = addLabelsToLabelable
   addProjectCard = addProjectCard
   addProjectColumn = addProjectColumn
   addProjectDraftIssue = addProjectDraftIssue
   addProjectNextItem = addProjectNextItem
   addProjectV2DraftIssue = addProjectV2DraftIssue
   addProjectV2ItemById = addProjectV2ItemById
   addPullRequestReview = addPullRequestReview
   addPullRequestReviewComment = addPullRequestReviewComment
   addPullRequestReviewThread = addPullRequestReviewThread
   addReaction = addReaction
   addStar = addStar
   addUpvote = addUpvote
   addVerifiableDomain = addVerifiableDomain
   approveDeployments = approveDeployments
   approveVerifiableDomain = approveVerifiableDomain
   archiveProjectV2Item = archiveProjectV2Item
   archiveRepository = archiveRepository
   cancelEnterpriseAdminInvitation = cancelEnterpriseAdminInvitation
   cancelSponsorship = cancelSponsorship
   changeUserStatus = changeUserStatus
   clearLabelsFromLabelable = clearLabelsFromLabelable
   clearProjectV2ItemFieldValue = clearProjectV2ItemFieldValue
   cloneProject = cloneProject
   cloneTemplateRepository = cloneTemplateRepository
   closeIssue = closeIssue
   closePullRequest = closePullRequest
   convertProjectCardNoteToIssue = convertProjectCardNoteToIssue
   convertPullRequestToDraft = convertPullRequestToDraft
   createAttributionInvitation = createAttributionInvitation
   createBranchProtectionRule = createBranchProtectionRule
   createCheckRun = createCheckRun
   createCheckSuite = createCheckSuite
   createCommitOnBranch = createCommitOnBranch
   createDiscussion = createDiscussion
   createEnterpriseOrganization = createEnterpriseOrganization
   createEnvironment = createEnvironment
   createIpAllowListEntry = createIpAllowListEntry
   createIssue = createIssue
   createLinkedBranch = createLinkedBranch
   createMigrationSource = createMigrationSource
   createProject = createProject
   createProjectV2 = createProjectV2
   createPullRequest = createPullRequest
   createRef = createRef
   createRepository = createRepository
   createSponsorsListing = createSponsorsListing
   createSponsorsTier = createSponsorsTier
   createSponsorship = createSponsorship
   createTeamDiscussion = createTeamDiscussion
   createTeamDiscussionComment = createTeamDiscussionComment
   declineTopicSuggestion = declineTopicSuggestion
   deleteBranchProtectionRule = deleteBranchProtectionRule
   deleteDeployment = deleteDeployment
   deleteDiscussion = deleteDiscussion
   deleteDiscussionComment = deleteDiscussionComment
   deleteEnvironment = deleteEnvironment
   deleteIpAllowListEntry = deleteIpAllowListEntry
   deleteIssue = deleteIssue
   deleteIssueComment = deleteIssueComment
   deleteLinkedBranch = deleteLinkedBranch
   deleteProject = deleteProject
   deleteProjectCard = deleteProjectCard
   deleteProjectColumn = deleteProjectColumn
   deleteProjectNextItem = deleteProjectNextItem
   deleteProjectV2Item = deleteProjectV2Item
   deletePullRequestReview = deletePullRequestReview
   deletePullRequestReviewComment = deletePullRequestReviewComment
   deleteRef = deleteRef
   deleteTeamDiscussion = deleteTeamDiscussion
   deleteTeamDiscussionComment = deleteTeamDiscussionComment
   deleteVerifiableDomain = deleteVerifiableDomain
   disablePullRequestAutoMerge = disablePullRequestAutoMerge
   dismissPullRequestReview = dismissPullRequestReview
   dismissRepositoryVulnerabilityAlert = dismissRepositoryVulnerabilityAlert
   enablePullRequestAutoMerge = enablePullRequestAutoMerge
   followOrganization = followOrganization
   followUser = followUser
   grantEnterpriseOrganizationsMigratorRole = grantEnterpriseOrganizationsMigratorRole
   grantMigratorRole = grantMigratorRole
   inviteEnterpriseAdmin = inviteEnterpriseAdmin
   linkProjectV2ToRepository = linkProjectV2ToRepository
   linkProjectV2ToTeam = linkProjectV2ToTeam
   linkRepositoryToProject = linkRepositoryToProject
   lockLockable = lockLockable
   markDiscussionCommentAsAnswer = markDiscussionCommentAsAnswer
   markFileAsViewed = markFileAsViewed
   markPullRequestReadyForReview = markPullRequestReadyForReview
   mergeBranch = mergeBranch
   mergePullRequest = mergePullRequest
   minimizeComment = minimizeComment
   moveProjectCard = moveProjectCard
   moveProjectColumn = moveProjectColumn
   pinIssue = pinIssue
   publishSponsorsTier = publishSponsorsTier
   regenerateEnterpriseIdentityProviderRecoveryCodes = regenerateEnterpriseIdentityProviderRecoveryCodes
   regenerateVerifiableDomainToken = regenerateVerifiableDomainToken
   rejectDeployments = rejectDeployments
   removeAssigneesFromAssignable = removeAssigneesFromAssignable
   removeEnterpriseAdmin = removeEnterpriseAdmin
   removeEnterpriseIdentityProvider = removeEnterpriseIdentityProvider
   removeEnterpriseOrganization = removeEnterpriseOrganization
   removeEnterpriseSupportEntitlement = removeEnterpriseSupportEntitlement
   removeLabelsFromLabelable = removeLabelsFromLabelable
   removeOutsideCollaborator = removeOutsideCollaborator
   removeReaction = removeReaction
   removeStar = removeStar
   removeUpvote = removeUpvote
   reopenIssue = reopenIssue
   reopenPullRequest = reopenPullRequest
   requestReviews = requestReviews
   rerequestCheckSuite = rerequestCheckSuite
   resolveReviewThread = resolveReviewThread
   revokeEnterpriseOrganizationsMigratorRole = revokeEnterpriseOrganizationsMigratorRole
   revokeMigratorRole = revokeMigratorRole
   setEnterpriseIdentityProvider = setEnterpriseIdentityProvider
   setOrganizationInteractionLimit = setOrganizationInteractionLimit
   setRepositoryInteractionLimit = setRepositoryInteractionLimit
   setUserInteractionLimit = setUserInteractionLimit
   startRepositoryMigration = startRepositoryMigration
   submitPullRequestReview = submitPullRequestReview
   transferEnterpriseOrganization = transferEnterpriseOrganization
   transferIssue = transferIssue
   unarchiveProjectV2Item = unarchiveProjectV2Item
   unarchiveRepository = unarchiveRepository
   unfollowOrganization = unfollowOrganization
   unfollowUser = unfollowUser
   unlinkProjectV2FromRepository = unlinkProjectV2FromRepository
   unlinkProjectV2FromTeam = unlinkProjectV2FromTeam
   unlinkRepositoryFromProject = unlinkRepositoryFromProject
   unlockLockable = unlockLockable
   unmarkDiscussionCommentAsAnswer = unmarkDiscussionCommentAsAnswer
   unmarkFileAsViewed = unmarkFileAsViewed
   unmarkIssueAsDuplicate = unmarkIssueAsDuplicate
   unminimizeComment = unminimizeComment
   unpinIssue = unpinIssue
   unresolveReviewThread = unresolveReviewThread
   updateBranchProtectionRule = updateBranchProtectionRule
   updateCheckRun = updateCheckRun
   updateCheckSuitePreferences = updateCheckSuitePreferences
   updateDiscussion = updateDiscussion
   updateDiscussionComment = updateDiscussionComment
   updateEnterpriseAdministratorRole = updateEnterpriseAdministratorRole
   updateEnterpriseAllowPrivateRepositoryForkingSetting = updateEnterpriseAllowPrivateRepositoryForkingSetting
   updateEnterpriseDefaultRepositoryPermissionSetting = updateEnterpriseDefaultRepositoryPermissionSetting
   updateEnterpriseMembersCanChangeRepositoryVisibilitySetting = updateEnterpriseMembersCanChangeRepositoryVisibilitySetting
   updateEnterpriseMembersCanCreateRepositoriesSetting = updateEnterpriseMembersCanCreateRepositoriesSetting
   updateEnterpriseMembersCanDeleteIssuesSetting = updateEnterpriseMembersCanDeleteIssuesSetting
   updateEnterpriseMembersCanDeleteRepositoriesSetting = updateEnterpriseMembersCanDeleteRepositoriesSetting
   updateEnterpriseMembersCanInviteCollaboratorsSetting = updateEnterpriseMembersCanInviteCollaboratorsSetting
   updateEnterpriseMembersCanMakePurchasesSetting = updateEnterpriseMembersCanMakePurchasesSetting
   updateEnterpriseMembersCanUpdateProtectedBranchesSetting = updateEnterpriseMembersCanUpdateProtectedBranchesSetting
   updateEnterpriseMembersCanViewDependencyInsightsSetting = updateEnterpriseMembersCanViewDependencyInsightsSetting
   updateEnterpriseOrganizationProjectsSetting = updateEnterpriseOrganizationProjectsSetting
   updateEnterpriseOwnerOrganizationRole = updateEnterpriseOwnerOrganizationRole
   updateEnterpriseProfile = updateEnterpriseProfile
   updateEnterpriseRepositoryProjectsSetting = updateEnterpriseRepositoryProjectsSetting
   updateEnterpriseTeamDiscussionsSetting = updateEnterpriseTeamDiscussionsSetting
   updateEnterpriseTwoFactorAuthenticationRequiredSetting = updateEnterpriseTwoFactorAuthenticationRequiredSetting
   updateEnvironment = updateEnvironment
   updateIpAllowListEnabledSetting = updateIpAllowListEnabledSetting
   updateIpAllowListEntry = updateIpAllowListEntry
   updateIpAllowListForInstalledAppsEnabledSetting = updateIpAllowListForInstalledAppsEnabledSetting
   updateIssue = updateIssue
   updateIssueComment = updateIssueComment
   updateNotificationRestrictionSetting = updateNotificationRestrictionSetting
   updateOrganizationAllowPrivateRepositoryForkingSetting = updateOrganizationAllowPrivateRepositoryForkingSetting
   updateOrganizationWebCommitSignoffSetting = updateOrganizationWebCommitSignoffSetting
   updateProject = updateProject
   updateProjectCard = updateProjectCard
   updateProjectColumn = updateProjectColumn
   updateProjectDraftIssue = updateProjectDraftIssue
   updateProjectNext = updateProjectNext
   updateProjectNextItemField = updateProjectNextItemField
   updateProjectV2 = updateProjectV2
   updateProjectV2DraftIssue = updateProjectV2DraftIssue
   updateProjectV2ItemFieldValue = updateProjectV2ItemFieldValue
   updateProjectV2ItemPosition = updateProjectV2ItemPosition
   updatePullRequest = updatePullRequest
   updatePullRequestBranch = updatePullRequestBranch
   updatePullRequestReview = updatePullRequestReview
   updatePullRequestReviewComment = updatePullRequestReviewComment
   updateRef = updateRef
   updateRepository = updateRepository
   updateRepositoryWebCommitSignoffSetting = updateRepositoryWebCommitSignoffSetting
   updateSponsorshipPreferences = updateSponsorshipPreferences
   updateSubscription = updateSubscription
   updateTeamDiscussion = updateTeamDiscussion
   updateTeamDiscussionComment = updateTeamDiscussionComment
   updateTeamsRepository = updateTeamsRepository
   updateTopics = updateTopics
   verifyVerifiableDomain = verifyVerifiableDomain
