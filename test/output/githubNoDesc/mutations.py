from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *


class abortQueuedMigrations(GQLObject):
   class Args(GQLOperationArgs): 
      input: AbortQueuedMigrationsInput ##NON NULL

   _args: Args


   type: AbortQueuedMigrationsPayload

class acceptEnterpriseAdministratorInvitation(GQLObject):
   class Args(GQLOperationArgs): 
      input: AcceptEnterpriseAdministratorInvitationInput ##NON NULL

   _args: Args


   type: AcceptEnterpriseAdministratorInvitationPayload

class acceptTopicSuggestion(GQLObject):
   class Args(GQLOperationArgs): 
      input: AcceptTopicSuggestionInput ##NON NULL

   _args: Args


   type: AcceptTopicSuggestionPayload

class addAssigneesToAssignable(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddAssigneesToAssignableInput ##NON NULL

   _args: Args


   type: AddAssigneesToAssignablePayload

class addComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddCommentInput ##NON NULL

   _args: Args


   type: AddCommentPayload

class addDiscussionComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddDiscussionCommentInput ##NON NULL

   _args: Args


   type: AddDiscussionCommentPayload

class addDiscussionPollVote(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddDiscussionPollVoteInput ##NON NULL

   _args: Args


   type: AddDiscussionPollVotePayload

class addEnterpriseOrganizationMember(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddEnterpriseOrganizationMemberInput ##NON NULL

   _args: Args


   type: AddEnterpriseOrganizationMemberPayload

class addEnterpriseSupportEntitlement(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddEnterpriseSupportEntitlementInput ##NON NULL

   _args: Args


   type: AddEnterpriseSupportEntitlementPayload

class addLabelsToLabelable(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddLabelsToLabelableInput ##NON NULL

   _args: Args


   type: AddLabelsToLabelablePayload

class addProjectCard(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddProjectCardInput ##NON NULL

   _args: Args


   type: AddProjectCardPayload

class addProjectColumn(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddProjectColumnInput ##NON NULL

   _args: Args


   type: AddProjectColumnPayload

class addProjectDraftIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddProjectDraftIssueInput ##NON NULL

   _args: Args


   type: AddProjectDraftIssuePayload

class addProjectNextItem(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddProjectNextItemInput ##NON NULL

   _args: Args


   type: AddProjectNextItemPayload

class addProjectV2DraftIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddProjectV2DraftIssueInput ##NON NULL

   _args: Args


   type: AddProjectV2DraftIssuePayload

class addProjectV2ItemById(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddProjectV2ItemByIdInput ##NON NULL

   _args: Args


   type: AddProjectV2ItemByIdPayload

class addPullRequestReview(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddPullRequestReviewInput ##NON NULL

   _args: Args


   type: AddPullRequestReviewPayload

class addPullRequestReviewComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddPullRequestReviewCommentInput ##NON NULL

   _args: Args


   type: AddPullRequestReviewCommentPayload

class addPullRequestReviewThread(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddPullRequestReviewThreadInput ##NON NULL

   _args: Args


   type: AddPullRequestReviewThreadPayload

class addReaction(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddReactionInput ##NON NULL

   _args: Args


   type: AddReactionPayload

class addStar(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddStarInput ##NON NULL

   _args: Args


   type: AddStarPayload

class addUpvote(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddUpvoteInput ##NON NULL

   _args: Args


   type: AddUpvotePayload

class addVerifiableDomain(GQLObject):
   class Args(GQLOperationArgs): 
      input: AddVerifiableDomainInput ##NON NULL

   _args: Args


   type: AddVerifiableDomainPayload

class approveDeployments(GQLObject):
   class Args(GQLOperationArgs): 
      input: ApproveDeploymentsInput ##NON NULL

   _args: Args


   type: ApproveDeploymentsPayload

class approveVerifiableDomain(GQLObject):
   class Args(GQLOperationArgs): 
      input: ApproveVerifiableDomainInput ##NON NULL

   _args: Args


   type: ApproveVerifiableDomainPayload

class archiveProjectV2Item(GQLObject):
   class Args(GQLOperationArgs): 
      input: ArchiveProjectV2ItemInput ##NON NULL

   _args: Args


   type: ArchiveProjectV2ItemPayload

class archiveRepository(GQLObject):
   class Args(GQLOperationArgs): 
      input: ArchiveRepositoryInput ##NON NULL

   _args: Args


   type: ArchiveRepositoryPayload

class cancelEnterpriseAdminInvitation(GQLObject):
   class Args(GQLOperationArgs): 
      input: CancelEnterpriseAdminInvitationInput ##NON NULL

   _args: Args


   type: CancelEnterpriseAdminInvitationPayload

class cancelSponsorship(GQLObject):
   class Args(GQLOperationArgs): 
      input: CancelSponsorshipInput ##NON NULL

   _args: Args


   type: CancelSponsorshipPayload

class changeUserStatus(GQLObject):
   class Args(GQLOperationArgs): 
      input: ChangeUserStatusInput ##NON NULL

   _args: Args


   type: ChangeUserStatusPayload

class clearLabelsFromLabelable(GQLObject):
   class Args(GQLOperationArgs): 
      input: ClearLabelsFromLabelableInput ##NON NULL

   _args: Args


   type: ClearLabelsFromLabelablePayload

class clearProjectV2ItemFieldValue(GQLObject):
   class Args(GQLOperationArgs): 
      input: ClearProjectV2ItemFieldValueInput ##NON NULL

   _args: Args


   type: ClearProjectV2ItemFieldValuePayload

class cloneProject(GQLObject):
   class Args(GQLOperationArgs): 
      input: CloneProjectInput ##NON NULL

   _args: Args


   type: CloneProjectPayload

class cloneTemplateRepository(GQLObject):
   class Args(GQLOperationArgs): 
      input: CloneTemplateRepositoryInput ##NON NULL

   _args: Args


   type: CloneTemplateRepositoryPayload

class closeIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: CloseIssueInput ##NON NULL

   _args: Args


   type: CloseIssuePayload

class closePullRequest(GQLObject):
   class Args(GQLOperationArgs): 
      input: ClosePullRequestInput ##NON NULL

   _args: Args


   type: ClosePullRequestPayload

class convertProjectCardNoteToIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: ConvertProjectCardNoteToIssueInput ##NON NULL

   _args: Args


   type: ConvertProjectCardNoteToIssuePayload

class convertPullRequestToDraft(GQLObject):
   class Args(GQLOperationArgs): 
      input: ConvertPullRequestToDraftInput ##NON NULL

   _args: Args


   type: ConvertPullRequestToDraftPayload

class createAttributionInvitation(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateAttributionInvitationInput ##NON NULL

   _args: Args


   type: CreateAttributionInvitationPayload

class createBranchProtectionRule(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateBranchProtectionRuleInput ##NON NULL

   _args: Args


   type: CreateBranchProtectionRulePayload

class createCheckRun(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateCheckRunInput ##NON NULL

   _args: Args


   type: CreateCheckRunPayload

class createCheckSuite(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateCheckSuiteInput ##NON NULL

   _args: Args


   type: CreateCheckSuitePayload

class createCommitOnBranch(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateCommitOnBranchInput ##NON NULL

   _args: Args


   type: CreateCommitOnBranchPayload

class createDiscussion(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateDiscussionInput ##NON NULL

   _args: Args


   type: CreateDiscussionPayload

class createEnterpriseOrganization(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateEnterpriseOrganizationInput ##NON NULL

   _args: Args


   type: CreateEnterpriseOrganizationPayload

class createEnvironment(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateEnvironmentInput ##NON NULL

   _args: Args


   type: CreateEnvironmentPayload

class createIpAllowListEntry(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateIpAllowListEntryInput ##NON NULL

   _args: Args


   type: CreateIpAllowListEntryPayload

class createIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateIssueInput ##NON NULL

   _args: Args


   type: CreateIssuePayload

class createLinkedBranch(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateLinkedBranchInput ##NON NULL

   _args: Args


   type: CreateLinkedBranchPayload

class createMigrationSource(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateMigrationSourceInput ##NON NULL

   _args: Args


   type: CreateMigrationSourcePayload

class createProject(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateProjectInput ##NON NULL

   _args: Args


   type: CreateProjectPayload

class createProjectV2(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateProjectV2Input ##NON NULL

   _args: Args


   type: CreateProjectV2Payload

class createPullRequest(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreatePullRequestInput ##NON NULL

   _args: Args


   type: CreatePullRequestPayload

class createRef(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateRefInput ##NON NULL

   _args: Args


   type: CreateRefPayload

class createRepository(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateRepositoryInput ##NON NULL

   _args: Args


   type: CreateRepositoryPayload

class createSponsorsListing(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateSponsorsListingInput ##NON NULL

   _args: Args


   type: CreateSponsorsListingPayload

class createSponsorsTier(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateSponsorsTierInput ##NON NULL

   _args: Args


   type: CreateSponsorsTierPayload

class createSponsorship(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateSponsorshipInput ##NON NULL

   _args: Args


   type: CreateSponsorshipPayload

class createTeamDiscussion(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateTeamDiscussionInput ##NON NULL

   _args: Args


   type: CreateTeamDiscussionPayload

class createTeamDiscussionComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateTeamDiscussionCommentInput ##NON NULL

   _args: Args


   type: CreateTeamDiscussionCommentPayload

class declineTopicSuggestion(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeclineTopicSuggestionInput ##NON NULL

   _args: Args


   type: DeclineTopicSuggestionPayload

class deleteBranchProtectionRule(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteBranchProtectionRuleInput ##NON NULL

   _args: Args


   type: DeleteBranchProtectionRulePayload

class deleteDeployment(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteDeploymentInput ##NON NULL

   _args: Args


   type: DeleteDeploymentPayload

class deleteDiscussion(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteDiscussionInput ##NON NULL

   _args: Args


   type: DeleteDiscussionPayload

class deleteDiscussionComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteDiscussionCommentInput ##NON NULL

   _args: Args


   type: DeleteDiscussionCommentPayload

class deleteEnvironment(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteEnvironmentInput ##NON NULL

   _args: Args


   type: DeleteEnvironmentPayload

class deleteIpAllowListEntry(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteIpAllowListEntryInput ##NON NULL

   _args: Args


   type: DeleteIpAllowListEntryPayload

class deleteIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteIssueInput ##NON NULL

   _args: Args


   type: DeleteIssuePayload

class deleteIssueComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteIssueCommentInput ##NON NULL

   _args: Args


   type: DeleteIssueCommentPayload

class deleteLinkedBranch(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteLinkedBranchInput ##NON NULL

   _args: Args


   type: DeleteLinkedBranchPayload

class deleteProject(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteProjectInput ##NON NULL

   _args: Args


   type: DeleteProjectPayload

class deleteProjectCard(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteProjectCardInput ##NON NULL

   _args: Args


   type: DeleteProjectCardPayload

class deleteProjectColumn(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteProjectColumnInput ##NON NULL

   _args: Args


   type: DeleteProjectColumnPayload

class deleteProjectNextItem(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteProjectNextItemInput ##NON NULL

   _args: Args


   type: DeleteProjectNextItemPayload

class deleteProjectV2Item(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteProjectV2ItemInput ##NON NULL

   _args: Args


   type: DeleteProjectV2ItemPayload

class deletePullRequestReview(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeletePullRequestReviewInput ##NON NULL

   _args: Args


   type: DeletePullRequestReviewPayload

class deletePullRequestReviewComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeletePullRequestReviewCommentInput ##NON NULL

   _args: Args


   type: DeletePullRequestReviewCommentPayload

class deleteRef(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteRefInput ##NON NULL

   _args: Args


   type: DeleteRefPayload

class deleteTeamDiscussion(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteTeamDiscussionInput ##NON NULL

   _args: Args


   type: DeleteTeamDiscussionPayload

class deleteTeamDiscussionComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteTeamDiscussionCommentInput ##NON NULL

   _args: Args


   type: DeleteTeamDiscussionCommentPayload

class deleteVerifiableDomain(GQLObject):
   class Args(GQLOperationArgs): 
      input: DeleteVerifiableDomainInput ##NON NULL

   _args: Args


   type: DeleteVerifiableDomainPayload

class disablePullRequestAutoMerge(GQLObject):
   class Args(GQLOperationArgs): 
      input: DisablePullRequestAutoMergeInput ##NON NULL

   _args: Args


   type: DisablePullRequestAutoMergePayload

class dismissPullRequestReview(GQLObject):
   class Args(GQLOperationArgs): 
      input: DismissPullRequestReviewInput ##NON NULL

   _args: Args


   type: DismissPullRequestReviewPayload

class dismissRepositoryVulnerabilityAlert(GQLObject):
   class Args(GQLOperationArgs): 
      input: DismissRepositoryVulnerabilityAlertInput ##NON NULL

   _args: Args


   type: DismissRepositoryVulnerabilityAlertPayload

class enablePullRequestAutoMerge(GQLObject):
   class Args(GQLOperationArgs): 
      input: EnablePullRequestAutoMergeInput ##NON NULL

   _args: Args


   type: EnablePullRequestAutoMergePayload

class followOrganization(GQLObject):
   class Args(GQLOperationArgs): 
      input: FollowOrganizationInput ##NON NULL

   _args: Args


   type: FollowOrganizationPayload

class followUser(GQLObject):
   class Args(GQLOperationArgs): 
      input: FollowUserInput ##NON NULL

   _args: Args


   type: FollowUserPayload

class grantEnterpriseOrganizationsMigratorRole(GQLObject):
   class Args(GQLOperationArgs): 
      input: GrantEnterpriseOrganizationsMigratorRoleInput ##NON NULL

   _args: Args


   type: GrantEnterpriseOrganizationsMigratorRolePayload

class grantMigratorRole(GQLObject):
   class Args(GQLOperationArgs): 
      input: GrantMigratorRoleInput ##NON NULL

   _args: Args


   type: GrantMigratorRolePayload

class inviteEnterpriseAdmin(GQLObject):
   class Args(GQLOperationArgs): 
      input: InviteEnterpriseAdminInput ##NON NULL

   _args: Args


   type: InviteEnterpriseAdminPayload

class linkProjectV2ToRepository(GQLObject):
   class Args(GQLOperationArgs): 
      input: LinkProjectV2ToRepositoryInput ##NON NULL

   _args: Args


   type: LinkProjectV2ToRepositoryPayload

class linkProjectV2ToTeam(GQLObject):
   class Args(GQLOperationArgs): 
      input: LinkProjectV2ToTeamInput ##NON NULL

   _args: Args


   type: LinkProjectV2ToTeamPayload

class linkRepositoryToProject(GQLObject):
   class Args(GQLOperationArgs): 
      input: LinkRepositoryToProjectInput ##NON NULL

   _args: Args


   type: LinkRepositoryToProjectPayload

class lockLockable(GQLObject):
   class Args(GQLOperationArgs): 
      input: LockLockableInput ##NON NULL

   _args: Args


   type: LockLockablePayload

class markDiscussionCommentAsAnswer(GQLObject):
   class Args(GQLOperationArgs): 
      input: MarkDiscussionCommentAsAnswerInput ##NON NULL

   _args: Args


   type: MarkDiscussionCommentAsAnswerPayload

class markFileAsViewed(GQLObject):
   class Args(GQLOperationArgs): 
      input: MarkFileAsViewedInput ##NON NULL

   _args: Args


   type: MarkFileAsViewedPayload

class markPullRequestReadyForReview(GQLObject):
   class Args(GQLOperationArgs): 
      input: MarkPullRequestReadyForReviewInput ##NON NULL

   _args: Args


   type: MarkPullRequestReadyForReviewPayload

class mergeBranch(GQLObject):
   class Args(GQLOperationArgs): 
      input: MergeBranchInput ##NON NULL

   _args: Args


   type: MergeBranchPayload

class mergePullRequest(GQLObject):
   class Args(GQLOperationArgs): 
      input: MergePullRequestInput ##NON NULL

   _args: Args


   type: MergePullRequestPayload

class minimizeComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: MinimizeCommentInput ##NON NULL

   _args: Args


   type: MinimizeCommentPayload

class moveProjectCard(GQLObject):
   class Args(GQLOperationArgs): 
      input: MoveProjectCardInput ##NON NULL

   _args: Args


   type: MoveProjectCardPayload

class moveProjectColumn(GQLObject):
   class Args(GQLOperationArgs): 
      input: MoveProjectColumnInput ##NON NULL

   _args: Args


   type: MoveProjectColumnPayload

class pinIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: PinIssueInput ##NON NULL

   _args: Args


   type: PinIssuePayload

class publishSponsorsTier(GQLObject):
   class Args(GQLOperationArgs): 
      input: PublishSponsorsTierInput ##NON NULL

   _args: Args


   type: PublishSponsorsTierPayload

class regenerateEnterpriseIdentityProviderRecoveryCodes(GQLObject):
   class Args(GQLOperationArgs): 
      input: RegenerateEnterpriseIdentityProviderRecoveryCodesInput ##NON NULL

   _args: Args


   type: RegenerateEnterpriseIdentityProviderRecoveryCodesPayload

class regenerateVerifiableDomainToken(GQLObject):
   class Args(GQLOperationArgs): 
      input: RegenerateVerifiableDomainTokenInput ##NON NULL

   _args: Args


   type: RegenerateVerifiableDomainTokenPayload

class rejectDeployments(GQLObject):
   class Args(GQLOperationArgs): 
      input: RejectDeploymentsInput ##NON NULL

   _args: Args


   type: RejectDeploymentsPayload

class removeAssigneesFromAssignable(GQLObject):
   class Args(GQLOperationArgs): 
      input: RemoveAssigneesFromAssignableInput ##NON NULL

   _args: Args


   type: RemoveAssigneesFromAssignablePayload

class removeEnterpriseAdmin(GQLObject):
   class Args(GQLOperationArgs): 
      input: RemoveEnterpriseAdminInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseAdminPayload

class removeEnterpriseIdentityProvider(GQLObject):
   class Args(GQLOperationArgs): 
      input: RemoveEnterpriseIdentityProviderInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseIdentityProviderPayload

class removeEnterpriseOrganization(GQLObject):
   class Args(GQLOperationArgs): 
      input: RemoveEnterpriseOrganizationInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseOrganizationPayload

class removeEnterpriseSupportEntitlement(GQLObject):
   class Args(GQLOperationArgs): 
      input: RemoveEnterpriseSupportEntitlementInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseSupportEntitlementPayload

class removeLabelsFromLabelable(GQLObject):
   class Args(GQLOperationArgs): 
      input: RemoveLabelsFromLabelableInput ##NON NULL

   _args: Args


   type: RemoveLabelsFromLabelablePayload

class removeOutsideCollaborator(GQLObject):
   class Args(GQLOperationArgs): 
      input: RemoveOutsideCollaboratorInput ##NON NULL

   _args: Args


   type: RemoveOutsideCollaboratorPayload

class removeReaction(GQLObject):
   class Args(GQLOperationArgs): 
      input: RemoveReactionInput ##NON NULL

   _args: Args


   type: RemoveReactionPayload

class removeStar(GQLObject):
   class Args(GQLOperationArgs): 
      input: RemoveStarInput ##NON NULL

   _args: Args


   type: RemoveStarPayload

class removeUpvote(GQLObject):
   class Args(GQLOperationArgs): 
      input: RemoveUpvoteInput ##NON NULL

   _args: Args


   type: RemoveUpvotePayload

class reopenIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: ReopenIssueInput ##NON NULL

   _args: Args


   type: ReopenIssuePayload

class reopenPullRequest(GQLObject):
   class Args(GQLOperationArgs): 
      input: ReopenPullRequestInput ##NON NULL

   _args: Args


   type: ReopenPullRequestPayload

class requestReviews(GQLObject):
   class Args(GQLOperationArgs): 
      input: RequestReviewsInput ##NON NULL

   _args: Args


   type: RequestReviewsPayload

class rerequestCheckSuite(GQLObject):
   class Args(GQLOperationArgs): 
      input: RerequestCheckSuiteInput ##NON NULL

   _args: Args


   type: RerequestCheckSuitePayload

class resolveReviewThread(GQLObject):
   class Args(GQLOperationArgs): 
      input: ResolveReviewThreadInput ##NON NULL

   _args: Args


   type: ResolveReviewThreadPayload

class revokeEnterpriseOrganizationsMigratorRole(GQLObject):
   class Args(GQLOperationArgs): 
      input: RevokeEnterpriseOrganizationsMigratorRoleInput ##NON NULL

   _args: Args


   type: RevokeEnterpriseOrganizationsMigratorRolePayload

class revokeMigratorRole(GQLObject):
   class Args(GQLOperationArgs): 
      input: RevokeMigratorRoleInput ##NON NULL

   _args: Args


   type: RevokeMigratorRolePayload

class setEnterpriseIdentityProvider(GQLObject):
   class Args(GQLOperationArgs): 
      input: SetEnterpriseIdentityProviderInput ##NON NULL

   _args: Args


   type: SetEnterpriseIdentityProviderPayload

class setOrganizationInteractionLimit(GQLObject):
   class Args(GQLOperationArgs): 
      input: SetOrganizationInteractionLimitInput ##NON NULL

   _args: Args


   type: SetOrganizationInteractionLimitPayload

class setRepositoryInteractionLimit(GQLObject):
   class Args(GQLOperationArgs): 
      input: SetRepositoryInteractionLimitInput ##NON NULL

   _args: Args


   type: SetRepositoryInteractionLimitPayload

class setUserInteractionLimit(GQLObject):
   class Args(GQLOperationArgs): 
      input: SetUserInteractionLimitInput ##NON NULL

   _args: Args


   type: SetUserInteractionLimitPayload

class startRepositoryMigration(GQLObject):
   class Args(GQLOperationArgs): 
      input: StartRepositoryMigrationInput ##NON NULL

   _args: Args


   type: StartRepositoryMigrationPayload

class submitPullRequestReview(GQLObject):
   class Args(GQLOperationArgs): 
      input: SubmitPullRequestReviewInput ##NON NULL

   _args: Args


   type: SubmitPullRequestReviewPayload

class transferEnterpriseOrganization(GQLObject):
   class Args(GQLOperationArgs): 
      input: TransferEnterpriseOrganizationInput ##NON NULL

   _args: Args


   type: TransferEnterpriseOrganizationPayload

class transferIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: TransferIssueInput ##NON NULL

   _args: Args


   type: TransferIssuePayload

class unarchiveProjectV2Item(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnarchiveProjectV2ItemInput ##NON NULL

   _args: Args


   type: UnarchiveProjectV2ItemPayload

class unarchiveRepository(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnarchiveRepositoryInput ##NON NULL

   _args: Args


   type: UnarchiveRepositoryPayload

class unfollowOrganization(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnfollowOrganizationInput ##NON NULL

   _args: Args


   type: UnfollowOrganizationPayload

class unfollowUser(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnfollowUserInput ##NON NULL

   _args: Args


   type: UnfollowUserPayload

class unlinkProjectV2FromRepository(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnlinkProjectV2FromRepositoryInput ##NON NULL

   _args: Args


   type: UnlinkProjectV2FromRepositoryPayload

class unlinkProjectV2FromTeam(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnlinkProjectV2FromTeamInput ##NON NULL

   _args: Args


   type: UnlinkProjectV2FromTeamPayload

class unlinkRepositoryFromProject(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnlinkRepositoryFromProjectInput ##NON NULL

   _args: Args


   type: UnlinkRepositoryFromProjectPayload

class unlockLockable(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnlockLockableInput ##NON NULL

   _args: Args


   type: UnlockLockablePayload

class unmarkDiscussionCommentAsAnswer(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnmarkDiscussionCommentAsAnswerInput ##NON NULL

   _args: Args


   type: UnmarkDiscussionCommentAsAnswerPayload

class unmarkFileAsViewed(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnmarkFileAsViewedInput ##NON NULL

   _args: Args


   type: UnmarkFileAsViewedPayload

class unmarkIssueAsDuplicate(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnmarkIssueAsDuplicateInput ##NON NULL

   _args: Args


   type: UnmarkIssueAsDuplicatePayload

class unminimizeComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnminimizeCommentInput ##NON NULL

   _args: Args


   type: UnminimizeCommentPayload

class unpinIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnpinIssueInput ##NON NULL

   _args: Args


   type: UnpinIssuePayload

class unresolveReviewThread(GQLObject):
   class Args(GQLOperationArgs): 
      input: UnresolveReviewThreadInput ##NON NULL

   _args: Args


   type: UnresolveReviewThreadPayload

class updateBranchProtectionRule(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateBranchProtectionRuleInput ##NON NULL

   _args: Args


   type: UpdateBranchProtectionRulePayload

class updateCheckRun(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateCheckRunInput ##NON NULL

   _args: Args


   type: UpdateCheckRunPayload

class updateCheckSuitePreferences(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateCheckSuitePreferencesInput ##NON NULL

   _args: Args


   type: UpdateCheckSuitePreferencesPayload

class updateDiscussion(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateDiscussionInput ##NON NULL

   _args: Args


   type: UpdateDiscussionPayload

class updateDiscussionComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateDiscussionCommentInput ##NON NULL

   _args: Args


   type: UpdateDiscussionCommentPayload

class updateEnterpriseAdministratorRole(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseAdministratorRoleInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseAdministratorRolePayload

class updateEnterpriseAllowPrivateRepositoryForkingSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload

class updateEnterpriseDefaultRepositoryPermissionSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseDefaultRepositoryPermissionSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseDefaultRepositoryPermissionSettingPayload

class updateEnterpriseMembersCanChangeRepositoryVisibilitySetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload

class updateEnterpriseMembersCanCreateRepositoriesSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseMembersCanCreateRepositoriesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload

class updateEnterpriseMembersCanDeleteIssuesSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseMembersCanDeleteIssuesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanDeleteIssuesSettingPayload

class updateEnterpriseMembersCanDeleteRepositoriesSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload

class updateEnterpriseMembersCanInviteCollaboratorsSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload

class updateEnterpriseMembersCanMakePurchasesSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseMembersCanMakePurchasesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanMakePurchasesSettingPayload

class updateEnterpriseMembersCanUpdateProtectedBranchesSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload

class updateEnterpriseMembersCanViewDependencyInsightsSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload

class updateEnterpriseOrganizationProjectsSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseOrganizationProjectsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseOrganizationProjectsSettingPayload

class updateEnterpriseOwnerOrganizationRole(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseOwnerOrganizationRoleInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseOwnerOrganizationRolePayload

class updateEnterpriseProfile(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseProfileInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseProfilePayload

class updateEnterpriseRepositoryProjectsSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseRepositoryProjectsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseRepositoryProjectsSettingPayload

class updateEnterpriseTeamDiscussionsSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseTeamDiscussionsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseTeamDiscussionsSettingPayload

class updateEnterpriseTwoFactorAuthenticationRequiredSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload

class updateEnvironment(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateEnvironmentInput ##NON NULL

   _args: Args


   type: UpdateEnvironmentPayload

class updateIpAllowListEnabledSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateIpAllowListEnabledSettingInput ##NON NULL

   _args: Args


   type: UpdateIpAllowListEnabledSettingPayload

class updateIpAllowListEntry(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateIpAllowListEntryInput ##NON NULL

   _args: Args


   type: UpdateIpAllowListEntryPayload

class updateIpAllowListForInstalledAppsEnabledSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateIpAllowListForInstalledAppsEnabledSettingInput ##NON NULL

   _args: Args


   type: UpdateIpAllowListForInstalledAppsEnabledSettingPayload

class updateIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateIssueInput ##NON NULL

   _args: Args


   type: UpdateIssuePayload

class updateIssueComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateIssueCommentInput ##NON NULL

   _args: Args


   type: UpdateIssueCommentPayload

class updateNotificationRestrictionSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateNotificationRestrictionSettingInput ##NON NULL

   _args: Args


   type: UpdateNotificationRestrictionSettingPayload

class updateOrganizationAllowPrivateRepositoryForkingSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateOrganizationAllowPrivateRepositoryForkingSettingInput ##NON NULL

   _args: Args


   type: UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload

class updateOrganizationWebCommitSignoffSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateOrganizationWebCommitSignoffSettingInput ##NON NULL

   _args: Args


   type: UpdateOrganizationWebCommitSignoffSettingPayload

class updateProject(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateProjectInput ##NON NULL

   _args: Args


   type: UpdateProjectPayload

class updateProjectCard(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateProjectCardInput ##NON NULL

   _args: Args


   type: UpdateProjectCardPayload

class updateProjectColumn(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateProjectColumnInput ##NON NULL

   _args: Args


   type: UpdateProjectColumnPayload

class updateProjectDraftIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateProjectDraftIssueInput ##NON NULL

   _args: Args


   type: UpdateProjectDraftIssuePayload

class updateProjectNext(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateProjectNextInput ##NON NULL

   _args: Args


   type: UpdateProjectNextPayload

class updateProjectNextItemField(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateProjectNextItemFieldInput ##NON NULL

   _args: Args


   type: UpdateProjectNextItemFieldPayload

class updateProjectV2(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateProjectV2Input ##NON NULL

   _args: Args


   type: UpdateProjectV2Payload

class updateProjectV2DraftIssue(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateProjectV2DraftIssueInput ##NON NULL

   _args: Args


   type: UpdateProjectV2DraftIssuePayload

class updateProjectV2ItemFieldValue(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateProjectV2ItemFieldValueInput ##NON NULL

   _args: Args


   type: UpdateProjectV2ItemFieldValuePayload

class updateProjectV2ItemPosition(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateProjectV2ItemPositionInput ##NON NULL

   _args: Args


   type: UpdateProjectV2ItemPositionPayload

class updatePullRequest(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdatePullRequestInput ##NON NULL

   _args: Args


   type: UpdatePullRequestPayload

class updatePullRequestBranch(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdatePullRequestBranchInput ##NON NULL

   _args: Args


   type: UpdatePullRequestBranchPayload

class updatePullRequestReview(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdatePullRequestReviewInput ##NON NULL

   _args: Args


   type: UpdatePullRequestReviewPayload

class updatePullRequestReviewComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdatePullRequestReviewCommentInput ##NON NULL

   _args: Args


   type: UpdatePullRequestReviewCommentPayload

class updateRef(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateRefInput ##NON NULL

   _args: Args


   type: UpdateRefPayload

class updateRepository(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateRepositoryInput ##NON NULL

   _args: Args


   type: UpdateRepositoryPayload

class updateRepositoryWebCommitSignoffSetting(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateRepositoryWebCommitSignoffSettingInput ##NON NULL

   _args: Args


   type: UpdateRepositoryWebCommitSignoffSettingPayload

class updateSponsorshipPreferences(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateSponsorshipPreferencesInput ##NON NULL

   _args: Args


   type: UpdateSponsorshipPreferencesPayload

class updateSubscription(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateSubscriptionInput ##NON NULL

   _args: Args


   type: UpdateSubscriptionPayload

class updateTeamDiscussion(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateTeamDiscussionInput ##NON NULL

   _args: Args


   type: UpdateTeamDiscussionPayload

class updateTeamDiscussionComment(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateTeamDiscussionCommentInput ##NON NULL

   _args: Args


   type: UpdateTeamDiscussionCommentPayload

class updateTeamsRepository(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateTeamsRepositoryInput ##NON NULL

   _args: Args


   type: UpdateTeamsRepositoryPayload

class updateTopics(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateTopicsInput ##NON NULL

   _args: Args


   type: UpdateTopicsPayload

class verifyVerifiableDomain(GQLObject):
   class Args(GQLOperationArgs): 
      input: VerifyVerifiableDomainInput ##NON NULL

   _args: Args


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
