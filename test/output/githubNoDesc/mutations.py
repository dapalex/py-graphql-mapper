from pygqlmap import GQLMutation
from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *


class abortQueuedMigrations(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AbortQueuedMigrationsInput ##NON NULL

   _args: Args


   type: AbortQueuedMigrationsPayload

class acceptEnterpriseAdministratorInvitation(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AcceptEnterpriseAdministratorInvitationInput ##NON NULL

   _args: Args


   type: AcceptEnterpriseAdministratorInvitationPayload

class acceptTopicSuggestion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AcceptTopicSuggestionInput ##NON NULL

   _args: Args


   type: AcceptTopicSuggestionPayload

class addAssigneesToAssignable(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddAssigneesToAssignableInput ##NON NULL

   _args: Args


   type: AddAssigneesToAssignablePayload

class addComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddCommentInput ##NON NULL

   _args: Args


   type: AddCommentPayload

class addDiscussionComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddDiscussionCommentInput ##NON NULL

   _args: Args


   type: AddDiscussionCommentPayload

class addDiscussionPollVote(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddDiscussionPollVoteInput ##NON NULL

   _args: Args


   type: AddDiscussionPollVotePayload

class addEnterpriseOrganizationMember(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddEnterpriseOrganizationMemberInput ##NON NULL

   _args: Args


   type: AddEnterpriseOrganizationMemberPayload

class addEnterpriseSupportEntitlement(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddEnterpriseSupportEntitlementInput ##NON NULL

   _args: Args


   type: AddEnterpriseSupportEntitlementPayload

class addLabelsToLabelable(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddLabelsToLabelableInput ##NON NULL

   _args: Args


   type: AddLabelsToLabelablePayload

class addProjectCard(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddProjectCardInput ##NON NULL

   _args: Args


   type: AddProjectCardPayload

class addProjectColumn(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddProjectColumnInput ##NON NULL

   _args: Args


   type: AddProjectColumnPayload

class addProjectDraftIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddProjectDraftIssueInput ##NON NULL

   _args: Args


   type: AddProjectDraftIssuePayload

class addProjectNextItem(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddProjectNextItemInput ##NON NULL

   _args: Args


   type: AddProjectNextItemPayload

class addProjectV2DraftIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddProjectV2DraftIssueInput ##NON NULL

   _args: Args


   type: AddProjectV2DraftIssuePayload

class addProjectV2ItemById(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddProjectV2ItemByIdInput ##NON NULL

   _args: Args


   type: AddProjectV2ItemByIdPayload

class addPullRequestReview(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddPullRequestReviewInput ##NON NULL

   _args: Args


   type: AddPullRequestReviewPayload

class addPullRequestReviewComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddPullRequestReviewCommentInput ##NON NULL

   _args: Args


   type: AddPullRequestReviewCommentPayload

class addPullRequestReviewThread(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddPullRequestReviewThreadInput ##NON NULL

   _args: Args


   type: AddPullRequestReviewThreadPayload

class addReaction(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddReactionInput ##NON NULL

   _args: Args


   type: AddReactionPayload

class addStar(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddStarInput ##NON NULL

   _args: Args


   type: AddStarPayload

class addUpvote(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddUpvoteInput ##NON NULL

   _args: Args


   type: AddUpvotePayload

class addVerifiableDomain(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddVerifiableDomainInput ##NON NULL

   _args: Args


   type: AddVerifiableDomainPayload

class approveDeployments(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ApproveDeploymentsInput ##NON NULL

   _args: Args


   type: ApproveDeploymentsPayload

class approveVerifiableDomain(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ApproveVerifiableDomainInput ##NON NULL

   _args: Args


   type: ApproveVerifiableDomainPayload

class archiveProjectV2Item(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ArchiveProjectV2ItemInput ##NON NULL

   _args: Args


   type: ArchiveProjectV2ItemPayload

class archiveRepository(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ArchiveRepositoryInput ##NON NULL

   _args: Args


   type: ArchiveRepositoryPayload

class cancelEnterpriseAdminInvitation(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CancelEnterpriseAdminInvitationInput ##NON NULL

   _args: Args


   type: CancelEnterpriseAdminInvitationPayload

class cancelSponsorship(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CancelSponsorshipInput ##NON NULL

   _args: Args


   type: CancelSponsorshipPayload

class changeUserStatus(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ChangeUserStatusInput ##NON NULL

   _args: Args


   type: ChangeUserStatusPayload

class clearLabelsFromLabelable(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ClearLabelsFromLabelableInput ##NON NULL

   _args: Args


   type: ClearLabelsFromLabelablePayload

class clearProjectV2ItemFieldValue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ClearProjectV2ItemFieldValueInput ##NON NULL

   _args: Args


   type: ClearProjectV2ItemFieldValuePayload

class cloneProject(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CloneProjectInput ##NON NULL

   _args: Args


   type: CloneProjectPayload

class cloneTemplateRepository(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CloneTemplateRepositoryInput ##NON NULL

   _args: Args


   type: CloneTemplateRepositoryPayload

class closeIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CloseIssueInput ##NON NULL

   _args: Args


   type: CloseIssuePayload

class closePullRequest(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ClosePullRequestInput ##NON NULL

   _args: Args


   type: ClosePullRequestPayload

class convertProjectCardNoteToIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ConvertProjectCardNoteToIssueInput ##NON NULL

   _args: Args


   type: ConvertProjectCardNoteToIssuePayload

class convertPullRequestToDraft(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ConvertPullRequestToDraftInput ##NON NULL

   _args: Args


   type: ConvertPullRequestToDraftPayload

class createAttributionInvitation(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateAttributionInvitationInput ##NON NULL

   _args: Args


   type: CreateAttributionInvitationPayload

class createBranchProtectionRule(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateBranchProtectionRuleInput ##NON NULL

   _args: Args


   type: CreateBranchProtectionRulePayload

class createCheckRun(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateCheckRunInput ##NON NULL

   _args: Args


   type: CreateCheckRunPayload

class createCheckSuite(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateCheckSuiteInput ##NON NULL

   _args: Args


   type: CreateCheckSuitePayload

class createCommitOnBranch(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateCommitOnBranchInput ##NON NULL

   _args: Args


   type: CreateCommitOnBranchPayload

class createDiscussion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateDiscussionInput ##NON NULL

   _args: Args


   type: CreateDiscussionPayload

class createEnterpriseOrganization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateEnterpriseOrganizationInput ##NON NULL

   _args: Args


   type: CreateEnterpriseOrganizationPayload

class createEnvironment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateEnvironmentInput ##NON NULL

   _args: Args


   type: CreateEnvironmentPayload

class createIpAllowListEntry(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateIpAllowListEntryInput ##NON NULL

   _args: Args


   type: CreateIpAllowListEntryPayload

class createIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateIssueInput ##NON NULL

   _args: Args


   type: CreateIssuePayload

class createLinkedBranch(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateLinkedBranchInput ##NON NULL

   _args: Args


   type: CreateLinkedBranchPayload

class createMigrationSource(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateMigrationSourceInput ##NON NULL

   _args: Args


   type: CreateMigrationSourcePayload

class createProject(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateProjectInput ##NON NULL

   _args: Args


   type: CreateProjectPayload

class createProjectV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateProjectV2Input ##NON NULL

   _args: Args


   type: CreateProjectV2Payload

class createPullRequest(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreatePullRequestInput ##NON NULL

   _args: Args


   type: CreatePullRequestPayload

class createRef(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateRefInput ##NON NULL

   _args: Args


   type: CreateRefPayload

class createRepository(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateRepositoryInput ##NON NULL

   _args: Args


   type: CreateRepositoryPayload

class createSponsorsListing(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateSponsorsListingInput ##NON NULL

   _args: Args


   type: CreateSponsorsListingPayload

class createSponsorsTier(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateSponsorsTierInput ##NON NULL

   _args: Args


   type: CreateSponsorsTierPayload

class createSponsorship(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateSponsorshipInput ##NON NULL

   _args: Args


   type: CreateSponsorshipPayload

class createTeamDiscussion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateTeamDiscussionInput ##NON NULL

   _args: Args


   type: CreateTeamDiscussionPayload

class createTeamDiscussionComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateTeamDiscussionCommentInput ##NON NULL

   _args: Args


   type: CreateTeamDiscussionCommentPayload

class declineTopicSuggestion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeclineTopicSuggestionInput ##NON NULL

   _args: Args


   type: DeclineTopicSuggestionPayload

class deleteBranchProtectionRule(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteBranchProtectionRuleInput ##NON NULL

   _args: Args


   type: DeleteBranchProtectionRulePayload

class deleteDeployment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteDeploymentInput ##NON NULL

   _args: Args


   type: DeleteDeploymentPayload

class deleteDiscussion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteDiscussionInput ##NON NULL

   _args: Args


   type: DeleteDiscussionPayload

class deleteDiscussionComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteDiscussionCommentInput ##NON NULL

   _args: Args


   type: DeleteDiscussionCommentPayload

class deleteEnvironment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteEnvironmentInput ##NON NULL

   _args: Args


   type: DeleteEnvironmentPayload

class deleteIpAllowListEntry(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteIpAllowListEntryInput ##NON NULL

   _args: Args


   type: DeleteIpAllowListEntryPayload

class deleteIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteIssueInput ##NON NULL

   _args: Args


   type: DeleteIssuePayload

class deleteIssueComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteIssueCommentInput ##NON NULL

   _args: Args


   type: DeleteIssueCommentPayload

class deleteLinkedBranch(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteLinkedBranchInput ##NON NULL

   _args: Args


   type: DeleteLinkedBranchPayload

class deleteProject(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteProjectInput ##NON NULL

   _args: Args


   type: DeleteProjectPayload

class deleteProjectCard(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteProjectCardInput ##NON NULL

   _args: Args


   type: DeleteProjectCardPayload

class deleteProjectColumn(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteProjectColumnInput ##NON NULL

   _args: Args


   type: DeleteProjectColumnPayload

class deleteProjectNextItem(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteProjectNextItemInput ##NON NULL

   _args: Args


   type: DeleteProjectNextItemPayload

class deleteProjectV2Item(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteProjectV2ItemInput ##NON NULL

   _args: Args


   type: DeleteProjectV2ItemPayload

class deletePullRequestReview(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeletePullRequestReviewInput ##NON NULL

   _args: Args


   type: DeletePullRequestReviewPayload

class deletePullRequestReviewComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeletePullRequestReviewCommentInput ##NON NULL

   _args: Args


   type: DeletePullRequestReviewCommentPayload

class deleteRef(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteRefInput ##NON NULL

   _args: Args


   type: DeleteRefPayload

class deleteTeamDiscussion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteTeamDiscussionInput ##NON NULL

   _args: Args


   type: DeleteTeamDiscussionPayload

class deleteTeamDiscussionComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteTeamDiscussionCommentInput ##NON NULL

   _args: Args


   type: DeleteTeamDiscussionCommentPayload

class deleteVerifiableDomain(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteVerifiableDomainInput ##NON NULL

   _args: Args


   type: DeleteVerifiableDomainPayload

class disablePullRequestAutoMerge(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DisablePullRequestAutoMergeInput ##NON NULL

   _args: Args


   type: DisablePullRequestAutoMergePayload

class dismissPullRequestReview(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DismissPullRequestReviewInput ##NON NULL

   _args: Args


   type: DismissPullRequestReviewPayload

class dismissRepositoryVulnerabilityAlert(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DismissRepositoryVulnerabilityAlertInput ##NON NULL

   _args: Args


   type: DismissRepositoryVulnerabilityAlertPayload

class enablePullRequestAutoMerge(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: EnablePullRequestAutoMergeInput ##NON NULL

   _args: Args


   type: EnablePullRequestAutoMergePayload

class followOrganization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: FollowOrganizationInput ##NON NULL

   _args: Args


   type: FollowOrganizationPayload

class followUser(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: FollowUserInput ##NON NULL

   _args: Args


   type: FollowUserPayload

class grantEnterpriseOrganizationsMigratorRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: GrantEnterpriseOrganizationsMigratorRoleInput ##NON NULL

   _args: Args


   type: GrantEnterpriseOrganizationsMigratorRolePayload

class grantMigratorRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: GrantMigratorRoleInput ##NON NULL

   _args: Args


   type: GrantMigratorRolePayload

class inviteEnterpriseAdmin(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: InviteEnterpriseAdminInput ##NON NULL

   _args: Args


   type: InviteEnterpriseAdminPayload

class linkProjectV2ToRepository(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: LinkProjectV2ToRepositoryInput ##NON NULL

   _args: Args


   type: LinkProjectV2ToRepositoryPayload

class linkProjectV2ToTeam(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: LinkProjectV2ToTeamInput ##NON NULL

   _args: Args


   type: LinkProjectV2ToTeamPayload

class linkRepositoryToProject(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: LinkRepositoryToProjectInput ##NON NULL

   _args: Args


   type: LinkRepositoryToProjectPayload

class lockLockable(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: LockLockableInput ##NON NULL

   _args: Args


   type: LockLockablePayload

class markDiscussionCommentAsAnswer(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MarkDiscussionCommentAsAnswerInput ##NON NULL

   _args: Args


   type: MarkDiscussionCommentAsAnswerPayload

class markFileAsViewed(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MarkFileAsViewedInput ##NON NULL

   _args: Args


   type: MarkFileAsViewedPayload

class markPullRequestReadyForReview(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MarkPullRequestReadyForReviewInput ##NON NULL

   _args: Args


   type: MarkPullRequestReadyForReviewPayload

class mergeBranch(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MergeBranchInput ##NON NULL

   _args: Args


   type: MergeBranchPayload

class mergePullRequest(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MergePullRequestInput ##NON NULL

   _args: Args


   type: MergePullRequestPayload

class minimizeComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MinimizeCommentInput ##NON NULL

   _args: Args


   type: MinimizeCommentPayload

class moveProjectCard(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MoveProjectCardInput ##NON NULL

   _args: Args


   type: MoveProjectCardPayload

class moveProjectColumn(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MoveProjectColumnInput ##NON NULL

   _args: Args


   type: MoveProjectColumnPayload

class pinIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: PinIssueInput ##NON NULL

   _args: Args


   type: PinIssuePayload

class publishSponsorsTier(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: PublishSponsorsTierInput ##NON NULL

   _args: Args


   type: PublishSponsorsTierPayload

class regenerateEnterpriseIdentityProviderRecoveryCodes(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RegenerateEnterpriseIdentityProviderRecoveryCodesInput ##NON NULL

   _args: Args


   type: RegenerateEnterpriseIdentityProviderRecoveryCodesPayload

class regenerateVerifiableDomainToken(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RegenerateVerifiableDomainTokenInput ##NON NULL

   _args: Args


   type: RegenerateVerifiableDomainTokenPayload

class rejectDeployments(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RejectDeploymentsInput ##NON NULL

   _args: Args


   type: RejectDeploymentsPayload

class removeAssigneesFromAssignable(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RemoveAssigneesFromAssignableInput ##NON NULL

   _args: Args


   type: RemoveAssigneesFromAssignablePayload

class removeEnterpriseAdmin(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RemoveEnterpriseAdminInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseAdminPayload

class removeEnterpriseIdentityProvider(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RemoveEnterpriseIdentityProviderInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseIdentityProviderPayload

class removeEnterpriseOrganization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RemoveEnterpriseOrganizationInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseOrganizationPayload

class removeEnterpriseSupportEntitlement(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RemoveEnterpriseSupportEntitlementInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseSupportEntitlementPayload

class removeLabelsFromLabelable(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RemoveLabelsFromLabelableInput ##NON NULL

   _args: Args


   type: RemoveLabelsFromLabelablePayload

class removeOutsideCollaborator(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RemoveOutsideCollaboratorInput ##NON NULL

   _args: Args


   type: RemoveOutsideCollaboratorPayload

class removeReaction(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RemoveReactionInput ##NON NULL

   _args: Args


   type: RemoveReactionPayload

class removeStar(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RemoveStarInput ##NON NULL

   _args: Args


   type: RemoveStarPayload

class removeUpvote(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RemoveUpvoteInput ##NON NULL

   _args: Args


   type: RemoveUpvotePayload

class reopenIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ReopenIssueInput ##NON NULL

   _args: Args


   type: ReopenIssuePayload

class reopenPullRequest(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ReopenPullRequestInput ##NON NULL

   _args: Args


   type: ReopenPullRequestPayload

class requestReviews(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RequestReviewsInput ##NON NULL

   _args: Args


   type: RequestReviewsPayload

class rerequestCheckSuite(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RerequestCheckSuiteInput ##NON NULL

   _args: Args


   type: RerequestCheckSuitePayload

class resolveReviewThread(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ResolveReviewThreadInput ##NON NULL

   _args: Args


   type: ResolveReviewThreadPayload

class revokeEnterpriseOrganizationsMigratorRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RevokeEnterpriseOrganizationsMigratorRoleInput ##NON NULL

   _args: Args


   type: RevokeEnterpriseOrganizationsMigratorRolePayload

class revokeMigratorRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RevokeMigratorRoleInput ##NON NULL

   _args: Args


   type: RevokeMigratorRolePayload

class setEnterpriseIdentityProvider(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: SetEnterpriseIdentityProviderInput ##NON NULL

   _args: Args


   type: SetEnterpriseIdentityProviderPayload

class setOrganizationInteractionLimit(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: SetOrganizationInteractionLimitInput ##NON NULL

   _args: Args


   type: SetOrganizationInteractionLimitPayload

class setRepositoryInteractionLimit(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: SetRepositoryInteractionLimitInput ##NON NULL

   _args: Args


   type: SetRepositoryInteractionLimitPayload

class setUserInteractionLimit(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: SetUserInteractionLimitInput ##NON NULL

   _args: Args


   type: SetUserInteractionLimitPayload

class startRepositoryMigration(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: StartRepositoryMigrationInput ##NON NULL

   _args: Args


   type: StartRepositoryMigrationPayload

class submitPullRequestReview(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: SubmitPullRequestReviewInput ##NON NULL

   _args: Args


   type: SubmitPullRequestReviewPayload

class transferEnterpriseOrganization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: TransferEnterpriseOrganizationInput ##NON NULL

   _args: Args


   type: TransferEnterpriseOrganizationPayload

class transferIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: TransferIssueInput ##NON NULL

   _args: Args


   type: TransferIssuePayload

class unarchiveProjectV2Item(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnarchiveProjectV2ItemInput ##NON NULL

   _args: Args


   type: UnarchiveProjectV2ItemPayload

class unarchiveRepository(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnarchiveRepositoryInput ##NON NULL

   _args: Args


   type: UnarchiveRepositoryPayload

class unfollowOrganization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnfollowOrganizationInput ##NON NULL

   _args: Args


   type: UnfollowOrganizationPayload

class unfollowUser(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnfollowUserInput ##NON NULL

   _args: Args


   type: UnfollowUserPayload

class unlinkProjectV2FromRepository(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnlinkProjectV2FromRepositoryInput ##NON NULL

   _args: Args


   type: UnlinkProjectV2FromRepositoryPayload

class unlinkProjectV2FromTeam(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnlinkProjectV2FromTeamInput ##NON NULL

   _args: Args


   type: UnlinkProjectV2FromTeamPayload

class unlinkRepositoryFromProject(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnlinkRepositoryFromProjectInput ##NON NULL

   _args: Args


   type: UnlinkRepositoryFromProjectPayload

class unlockLockable(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnlockLockableInput ##NON NULL

   _args: Args


   type: UnlockLockablePayload

class unmarkDiscussionCommentAsAnswer(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnmarkDiscussionCommentAsAnswerInput ##NON NULL

   _args: Args


   type: UnmarkDiscussionCommentAsAnswerPayload

class unmarkFileAsViewed(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnmarkFileAsViewedInput ##NON NULL

   _args: Args


   type: UnmarkFileAsViewedPayload

class unmarkIssueAsDuplicate(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnmarkIssueAsDuplicateInput ##NON NULL

   _args: Args


   type: UnmarkIssueAsDuplicatePayload

class unminimizeComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnminimizeCommentInput ##NON NULL

   _args: Args


   type: UnminimizeCommentPayload

class unpinIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnpinIssueInput ##NON NULL

   _args: Args


   type: UnpinIssuePayload

class unresolveReviewThread(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UnresolveReviewThreadInput ##NON NULL

   _args: Args


   type: UnresolveReviewThreadPayload

class updateBranchProtectionRule(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateBranchProtectionRuleInput ##NON NULL

   _args: Args


   type: UpdateBranchProtectionRulePayload

class updateCheckRun(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateCheckRunInput ##NON NULL

   _args: Args


   type: UpdateCheckRunPayload

class updateCheckSuitePreferences(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateCheckSuitePreferencesInput ##NON NULL

   _args: Args


   type: UpdateCheckSuitePreferencesPayload

class updateDiscussion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateDiscussionInput ##NON NULL

   _args: Args


   type: UpdateDiscussionPayload

class updateDiscussionComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateDiscussionCommentInput ##NON NULL

   _args: Args


   type: UpdateDiscussionCommentPayload

class updateEnterpriseAdministratorRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseAdministratorRoleInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseAdministratorRolePayload

class updateEnterpriseAllowPrivateRepositoryForkingSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload

class updateEnterpriseDefaultRepositoryPermissionSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseDefaultRepositoryPermissionSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseDefaultRepositoryPermissionSettingPayload

class updateEnterpriseMembersCanChangeRepositoryVisibilitySetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload

class updateEnterpriseMembersCanCreateRepositoriesSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanCreateRepositoriesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload

class updateEnterpriseMembersCanDeleteIssuesSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanDeleteIssuesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanDeleteIssuesSettingPayload

class updateEnterpriseMembersCanDeleteRepositoriesSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload

class updateEnterpriseMembersCanInviteCollaboratorsSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload

class updateEnterpriseMembersCanMakePurchasesSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanMakePurchasesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanMakePurchasesSettingPayload

class updateEnterpriseMembersCanUpdateProtectedBranchesSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload

class updateEnterpriseMembersCanViewDependencyInsightsSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload

class updateEnterpriseOrganizationProjectsSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseOrganizationProjectsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseOrganizationProjectsSettingPayload

class updateEnterpriseOwnerOrganizationRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseOwnerOrganizationRoleInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseOwnerOrganizationRolePayload

class updateEnterpriseProfile(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseProfileInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseProfilePayload

class updateEnterpriseRepositoryProjectsSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseRepositoryProjectsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseRepositoryProjectsSettingPayload

class updateEnterpriseTeamDiscussionsSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseTeamDiscussionsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseTeamDiscussionsSettingPayload

class updateEnterpriseTwoFactorAuthenticationRequiredSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload

class updateEnvironment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateEnvironmentInput ##NON NULL

   _args: Args


   type: UpdateEnvironmentPayload

class updateIpAllowListEnabledSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateIpAllowListEnabledSettingInput ##NON NULL

   _args: Args


   type: UpdateIpAllowListEnabledSettingPayload

class updateIpAllowListEntry(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateIpAllowListEntryInput ##NON NULL

   _args: Args


   type: UpdateIpAllowListEntryPayload

class updateIpAllowListForInstalledAppsEnabledSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateIpAllowListForInstalledAppsEnabledSettingInput ##NON NULL

   _args: Args


   type: UpdateIpAllowListForInstalledAppsEnabledSettingPayload

class updateIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateIssueInput ##NON NULL

   _args: Args


   type: UpdateIssuePayload

class updateIssueComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateIssueCommentInput ##NON NULL

   _args: Args


   type: UpdateIssueCommentPayload

class updateNotificationRestrictionSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateNotificationRestrictionSettingInput ##NON NULL

   _args: Args


   type: UpdateNotificationRestrictionSettingPayload

class updateOrganizationAllowPrivateRepositoryForkingSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateOrganizationAllowPrivateRepositoryForkingSettingInput ##NON NULL

   _args: Args


   type: UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload

class updateOrganizationWebCommitSignoffSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateOrganizationWebCommitSignoffSettingInput ##NON NULL

   _args: Args


   type: UpdateOrganizationWebCommitSignoffSettingPayload

class updateProject(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateProjectInput ##NON NULL

   _args: Args


   type: UpdateProjectPayload

class updateProjectCard(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateProjectCardInput ##NON NULL

   _args: Args


   type: UpdateProjectCardPayload

class updateProjectColumn(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateProjectColumnInput ##NON NULL

   _args: Args


   type: UpdateProjectColumnPayload

class updateProjectDraftIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateProjectDraftIssueInput ##NON NULL

   _args: Args


   type: UpdateProjectDraftIssuePayload

class updateProjectNext(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateProjectNextInput ##NON NULL

   _args: Args


   type: UpdateProjectNextPayload

class updateProjectNextItemField(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateProjectNextItemFieldInput ##NON NULL

   _args: Args


   type: UpdateProjectNextItemFieldPayload

class updateProjectV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateProjectV2Input ##NON NULL

   _args: Args


   type: UpdateProjectV2Payload

class updateProjectV2DraftIssue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateProjectV2DraftIssueInput ##NON NULL

   _args: Args


   type: UpdateProjectV2DraftIssuePayload

class updateProjectV2ItemFieldValue(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateProjectV2ItemFieldValueInput ##NON NULL

   _args: Args


   type: UpdateProjectV2ItemFieldValuePayload

class updateProjectV2ItemPosition(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateProjectV2ItemPositionInput ##NON NULL

   _args: Args


   type: UpdateProjectV2ItemPositionPayload

class updatePullRequest(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdatePullRequestInput ##NON NULL

   _args: Args


   type: UpdatePullRequestPayload

class updatePullRequestBranch(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdatePullRequestBranchInput ##NON NULL

   _args: Args


   type: UpdatePullRequestBranchPayload

class updatePullRequestReview(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdatePullRequestReviewInput ##NON NULL

   _args: Args


   type: UpdatePullRequestReviewPayload

class updatePullRequestReviewComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdatePullRequestReviewCommentInput ##NON NULL

   _args: Args


   type: UpdatePullRequestReviewCommentPayload

class updateRef(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateRefInput ##NON NULL

   _args: Args


   type: UpdateRefPayload

class updateRepository(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateRepositoryInput ##NON NULL

   _args: Args


   type: UpdateRepositoryPayload

class updateRepositoryWebCommitSignoffSetting(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateRepositoryWebCommitSignoffSettingInput ##NON NULL

   _args: Args


   type: UpdateRepositoryWebCommitSignoffSettingPayload

class updateSponsorshipPreferences(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateSponsorshipPreferencesInput ##NON NULL

   _args: Args


   type: UpdateSponsorshipPreferencesPayload

class updateSubscription(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateSubscriptionInput ##NON NULL

   _args: Args


   type: UpdateSubscriptionPayload

class updateTeamDiscussion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateTeamDiscussionInput ##NON NULL

   _args: Args


   type: UpdateTeamDiscussionPayload

class updateTeamDiscussionComment(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateTeamDiscussionCommentInput ##NON NULL

   _args: Args


   type: UpdateTeamDiscussionCommentPayload

class updateTeamsRepository(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateTeamsRepositoryInput ##NON NULL

   _args: Args


   type: UpdateTeamsRepositoryPayload

class updateTopics(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateTopicsInput ##NON NULL

   _args: Args


   type: UpdateTopicsPayload

class verifyVerifiableDomain(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
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
