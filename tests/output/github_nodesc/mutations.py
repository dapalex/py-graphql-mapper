from typing import List
from pygqlmap import GQLMutation
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *


NonNull_AbortQueuedMigrationsInput = AbortQueuedMigrationsInput

NonNull_AcceptEnterpriseAdministratorInvitationInput = AcceptEnterpriseAdministratorInvitationInput

NonNull_AcceptTopicSuggestionInput = AcceptTopicSuggestionInput

NonNull_AddAssigneesToAssignableInput = AddAssigneesToAssignableInput

NonNull_AddCommentInput = AddCommentInput

NonNull_AddDiscussionCommentInput = AddDiscussionCommentInput

NonNull_AddDiscussionPollVoteInput = AddDiscussionPollVoteInput

NonNull_AddEnterpriseOrganizationMemberInput = AddEnterpriseOrganizationMemberInput

NonNull_AddEnterpriseSupportEntitlementInput = AddEnterpriseSupportEntitlementInput

NonNull_AddLabelsToLabelableInput = AddLabelsToLabelableInput

NonNull_AddProjectCardInput = AddProjectCardInput

NonNull_AddProjectColumnInput = AddProjectColumnInput

NonNull_AddProjectV2DraftIssueInput = AddProjectV2DraftIssueInput

NonNull_AddProjectV2ItemByIdInput = AddProjectV2ItemByIdInput

NonNull_AddPullRequestReviewInput = AddPullRequestReviewInput

NonNull_AddPullRequestReviewCommentInput = AddPullRequestReviewCommentInput

NonNull_AddPullRequestReviewThreadInput = AddPullRequestReviewThreadInput

NonNull_AddReactionInput = AddReactionInput

NonNull_AddStarInput = AddStarInput

NonNull_AddUpvoteInput = AddUpvoteInput

NonNull_AddVerifiableDomainInput = AddVerifiableDomainInput

NonNull_ApproveDeploymentsInput = ApproveDeploymentsInput

NonNull_ApproveVerifiableDomainInput = ApproveVerifiableDomainInput

NonNull_ArchiveProjectV2ItemInput = ArchiveProjectV2ItemInput

NonNull_ArchiveRepositoryInput = ArchiveRepositoryInput

NonNull_CancelEnterpriseAdminInvitationInput = CancelEnterpriseAdminInvitationInput

NonNull_CancelSponsorshipInput = CancelSponsorshipInput

NonNull_ChangeUserStatusInput = ChangeUserStatusInput

NonNull_ClearLabelsFromLabelableInput = ClearLabelsFromLabelableInput

NonNull_ClearProjectV2ItemFieldValueInput = ClearProjectV2ItemFieldValueInput

NonNull_CloneProjectInput = CloneProjectInput

NonNull_CloneTemplateRepositoryInput = CloneTemplateRepositoryInput

NonNull_CloseIssueInput = CloseIssueInput

NonNull_ClosePullRequestInput = ClosePullRequestInput

NonNull_ConvertProjectCardNoteToIssueInput = ConvertProjectCardNoteToIssueInput

NonNull_ConvertPullRequestToDraftInput = ConvertPullRequestToDraftInput

NonNull_CreateAttributionInvitationInput = CreateAttributionInvitationInput

NonNull_CreateBranchProtectionRuleInput = CreateBranchProtectionRuleInput

NonNull_CreateCheckRunInput = CreateCheckRunInput

NonNull_CreateCheckSuiteInput = CreateCheckSuiteInput

NonNull_CreateCommitOnBranchInput = CreateCommitOnBranchInput

NonNull_CreateDiscussionInput = CreateDiscussionInput

NonNull_CreateEnterpriseOrganizationInput = CreateEnterpriseOrganizationInput

NonNull_CreateEnvironmentInput = CreateEnvironmentInput

NonNull_CreateIpAllowListEntryInput = CreateIpAllowListEntryInput

NonNull_CreateIssueInput = CreateIssueInput

NonNull_CreateLinkedBranchInput = CreateLinkedBranchInput

NonNull_CreateMigrationSourceInput = CreateMigrationSourceInput

NonNull_CreateProjectInput = CreateProjectInput

NonNull_CreateProjectV2Input = CreateProjectV2Input

NonNull_CreatePullRequestInput = CreatePullRequestInput

NonNull_CreateRefInput = CreateRefInput

NonNull_CreateRepositoryInput = CreateRepositoryInput

NonNull_CreateSponsorsListingInput = CreateSponsorsListingInput

NonNull_CreateSponsorsTierInput = CreateSponsorsTierInput

NonNull_CreateSponsorshipInput = CreateSponsorshipInput

NonNull_CreateTeamDiscussionInput = CreateTeamDiscussionInput

NonNull_CreateTeamDiscussionCommentInput = CreateTeamDiscussionCommentInput

NonNull_DeclineTopicSuggestionInput = DeclineTopicSuggestionInput

NonNull_DeleteBranchProtectionRuleInput = DeleteBranchProtectionRuleInput

NonNull_DeleteDeploymentInput = DeleteDeploymentInput

NonNull_DeleteDiscussionInput = DeleteDiscussionInput

NonNull_DeleteDiscussionCommentInput = DeleteDiscussionCommentInput

NonNull_DeleteEnvironmentInput = DeleteEnvironmentInput

NonNull_DeleteIpAllowListEntryInput = DeleteIpAllowListEntryInput

NonNull_DeleteIssueInput = DeleteIssueInput

NonNull_DeleteIssueCommentInput = DeleteIssueCommentInput

NonNull_DeleteLinkedBranchInput = DeleteLinkedBranchInput

NonNull_DeleteProjectInput = DeleteProjectInput

NonNull_DeleteProjectCardInput = DeleteProjectCardInput

NonNull_DeleteProjectColumnInput = DeleteProjectColumnInput

NonNull_DeleteProjectV2ItemInput = DeleteProjectV2ItemInput

NonNull_DeletePullRequestReviewInput = DeletePullRequestReviewInput

NonNull_DeletePullRequestReviewCommentInput = DeletePullRequestReviewCommentInput

NonNull_DeleteRefInput = DeleteRefInput

NonNull_DeleteTeamDiscussionInput = DeleteTeamDiscussionInput

NonNull_DeleteTeamDiscussionCommentInput = DeleteTeamDiscussionCommentInput

NonNull_DeleteVerifiableDomainInput = DeleteVerifiableDomainInput

NonNull_DisablePullRequestAutoMergeInput = DisablePullRequestAutoMergeInput

NonNull_DismissPullRequestReviewInput = DismissPullRequestReviewInput

NonNull_DismissRepositoryVulnerabilityAlertInput = DismissRepositoryVulnerabilityAlertInput

NonNull_EnablePullRequestAutoMergeInput = EnablePullRequestAutoMergeInput

NonNull_FollowOrganizationInput = FollowOrganizationInput

NonNull_FollowUserInput = FollowUserInput

NonNull_GrantEnterpriseOrganizationsMigratorRoleInput = GrantEnterpriseOrganizationsMigratorRoleInput

NonNull_GrantMigratorRoleInput = GrantMigratorRoleInput

NonNull_InviteEnterpriseAdminInput = InviteEnterpriseAdminInput

NonNull_LinkProjectV2ToRepositoryInput = LinkProjectV2ToRepositoryInput

NonNull_LinkProjectV2ToTeamInput = LinkProjectV2ToTeamInput

NonNull_LinkRepositoryToProjectInput = LinkRepositoryToProjectInput

NonNull_LockLockableInput = LockLockableInput

NonNull_MarkDiscussionCommentAsAnswerInput = MarkDiscussionCommentAsAnswerInput

NonNull_MarkFileAsViewedInput = MarkFileAsViewedInput

NonNull_MarkPullRequestReadyForReviewInput = MarkPullRequestReadyForReviewInput

NonNull_MergeBranchInput = MergeBranchInput

NonNull_MergePullRequestInput = MergePullRequestInput

NonNull_MinimizeCommentInput = MinimizeCommentInput

NonNull_MoveProjectCardInput = MoveProjectCardInput

NonNull_MoveProjectColumnInput = MoveProjectColumnInput

NonNull_PinIssueInput = PinIssueInput

NonNull_PublishSponsorsTierInput = PublishSponsorsTierInput

NonNull_RegenerateEnterpriseIdentityProviderRecoveryCodesInput = RegenerateEnterpriseIdentityProviderRecoveryCodesInput

NonNull_RegenerateVerifiableDomainTokenInput = RegenerateVerifiableDomainTokenInput

NonNull_RejectDeploymentsInput = RejectDeploymentsInput

NonNull_RemoveAssigneesFromAssignableInput = RemoveAssigneesFromAssignableInput

NonNull_RemoveEnterpriseAdminInput = RemoveEnterpriseAdminInput

NonNull_RemoveEnterpriseIdentityProviderInput = RemoveEnterpriseIdentityProviderInput

NonNull_RemoveEnterpriseOrganizationInput = RemoveEnterpriseOrganizationInput

NonNull_RemoveEnterpriseSupportEntitlementInput = RemoveEnterpriseSupportEntitlementInput

NonNull_RemoveLabelsFromLabelableInput = RemoveLabelsFromLabelableInput

NonNull_RemoveOutsideCollaboratorInput = RemoveOutsideCollaboratorInput

NonNull_RemoveReactionInput = RemoveReactionInput

NonNull_RemoveStarInput = RemoveStarInput

NonNull_RemoveUpvoteInput = RemoveUpvoteInput

NonNull_ReopenIssueInput = ReopenIssueInput

NonNull_ReopenPullRequestInput = ReopenPullRequestInput

NonNull_RequestReviewsInput = RequestReviewsInput

NonNull_RerequestCheckSuiteInput = RerequestCheckSuiteInput

NonNull_ResolveReviewThreadInput = ResolveReviewThreadInput

NonNull_RetireSponsorsTierInput = RetireSponsorsTierInput

NonNull_RevokeEnterpriseOrganizationsMigratorRoleInput = RevokeEnterpriseOrganizationsMigratorRoleInput

NonNull_RevokeMigratorRoleInput = RevokeMigratorRoleInput

NonNull_SetEnterpriseIdentityProviderInput = SetEnterpriseIdentityProviderInput

NonNull_SetOrganizationInteractionLimitInput = SetOrganizationInteractionLimitInput

NonNull_SetRepositoryInteractionLimitInput = SetRepositoryInteractionLimitInput

NonNull_SetUserInteractionLimitInput = SetUserInteractionLimitInput

NonNull_StartOrganizationMigrationInput = StartOrganizationMigrationInput

NonNull_StartRepositoryMigrationInput = StartRepositoryMigrationInput

NonNull_SubmitPullRequestReviewInput = SubmitPullRequestReviewInput

NonNull_TransferEnterpriseOrganizationInput = TransferEnterpriseOrganizationInput

NonNull_TransferIssueInput = TransferIssueInput

NonNull_UnarchiveProjectV2ItemInput = UnarchiveProjectV2ItemInput

NonNull_UnarchiveRepositoryInput = UnarchiveRepositoryInput

NonNull_UnfollowOrganizationInput = UnfollowOrganizationInput

NonNull_UnfollowUserInput = UnfollowUserInput

NonNull_UnlinkProjectV2FromRepositoryInput = UnlinkProjectV2FromRepositoryInput

NonNull_UnlinkProjectV2FromTeamInput = UnlinkProjectV2FromTeamInput

NonNull_UnlinkRepositoryFromProjectInput = UnlinkRepositoryFromProjectInput

NonNull_UnlockLockableInput = UnlockLockableInput

NonNull_UnmarkDiscussionCommentAsAnswerInput = UnmarkDiscussionCommentAsAnswerInput

NonNull_UnmarkFileAsViewedInput = UnmarkFileAsViewedInput

NonNull_UnmarkIssueAsDuplicateInput = UnmarkIssueAsDuplicateInput

NonNull_UnminimizeCommentInput = UnminimizeCommentInput

NonNull_UnpinIssueInput = UnpinIssueInput

NonNull_UnresolveReviewThreadInput = UnresolveReviewThreadInput

NonNull_UpdateBranchProtectionRuleInput = UpdateBranchProtectionRuleInput

NonNull_UpdateCheckRunInput = UpdateCheckRunInput

NonNull_UpdateCheckSuitePreferencesInput = UpdateCheckSuitePreferencesInput

NonNull_UpdateDiscussionInput = UpdateDiscussionInput

NonNull_UpdateDiscussionCommentInput = UpdateDiscussionCommentInput

NonNull_UpdateEnterpriseAdministratorRoleInput = UpdateEnterpriseAdministratorRoleInput

NonNull_UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput = UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput

NonNull_UpdateEnterpriseDefaultRepositoryPermissionSettingInput = UpdateEnterpriseDefaultRepositoryPermissionSettingInput

NonNull_UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput = UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput

NonNull_UpdateEnterpriseMembersCanCreateRepositoriesSettingInput = UpdateEnterpriseMembersCanCreateRepositoriesSettingInput

NonNull_UpdateEnterpriseMembersCanDeleteIssuesSettingInput = UpdateEnterpriseMembersCanDeleteIssuesSettingInput

NonNull_UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput = UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput

NonNull_UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput = UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput

NonNull_UpdateEnterpriseMembersCanMakePurchasesSettingInput = UpdateEnterpriseMembersCanMakePurchasesSettingInput

NonNull_UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput = UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput

NonNull_UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput = UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput

NonNull_UpdateEnterpriseOrganizationProjectsSettingInput = UpdateEnterpriseOrganizationProjectsSettingInput

NonNull_UpdateEnterpriseOwnerOrganizationRoleInput = UpdateEnterpriseOwnerOrganizationRoleInput

NonNull_UpdateEnterpriseProfileInput = UpdateEnterpriseProfileInput

NonNull_UpdateEnterpriseRepositoryProjectsSettingInput = UpdateEnterpriseRepositoryProjectsSettingInput

NonNull_UpdateEnterpriseTeamDiscussionsSettingInput = UpdateEnterpriseTeamDiscussionsSettingInput

NonNull_UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput = UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput

NonNull_UpdateEnvironmentInput = UpdateEnvironmentInput

NonNull_UpdateIpAllowListEnabledSettingInput = UpdateIpAllowListEnabledSettingInput

NonNull_UpdateIpAllowListEntryInput = UpdateIpAllowListEntryInput

NonNull_UpdateIpAllowListForInstalledAppsEnabledSettingInput = UpdateIpAllowListForInstalledAppsEnabledSettingInput

NonNull_UpdateIssueInput = UpdateIssueInput

NonNull_UpdateIssueCommentInput = UpdateIssueCommentInput

NonNull_UpdateNotificationRestrictionSettingInput = UpdateNotificationRestrictionSettingInput

NonNull_UpdateOrganizationAllowPrivateRepositoryForkingSettingInput = UpdateOrganizationAllowPrivateRepositoryForkingSettingInput

NonNull_UpdateOrganizationWebCommitSignoffSettingInput = UpdateOrganizationWebCommitSignoffSettingInput

NonNull_UpdateProjectInput = UpdateProjectInput

NonNull_UpdateProjectCardInput = UpdateProjectCardInput

NonNull_UpdateProjectColumnInput = UpdateProjectColumnInput

NonNull_UpdateProjectV2Input = UpdateProjectV2Input

NonNull_UpdateProjectV2DraftIssueInput = UpdateProjectV2DraftIssueInput

NonNull_UpdateProjectV2ItemFieldValueInput = UpdateProjectV2ItemFieldValueInput

NonNull_UpdateProjectV2ItemPositionInput = UpdateProjectV2ItemPositionInput

NonNull_UpdatePullRequestInput = UpdatePullRequestInput

NonNull_UpdatePullRequestBranchInput = UpdatePullRequestBranchInput

NonNull_UpdatePullRequestReviewInput = UpdatePullRequestReviewInput

NonNull_UpdatePullRequestReviewCommentInput = UpdatePullRequestReviewCommentInput

NonNull_UpdateRefInput = UpdateRefInput

NonNull_UpdateRepositoryInput = UpdateRepositoryInput

NonNull_UpdateRepositoryWebCommitSignoffSettingInput = UpdateRepositoryWebCommitSignoffSettingInput

NonNull_UpdateSponsorshipPreferencesInput = UpdateSponsorshipPreferencesInput

NonNull_UpdateSubscriptionInput = UpdateSubscriptionInput

NonNull_UpdateTeamDiscussionInput = UpdateTeamDiscussionInput

NonNull_UpdateTeamDiscussionCommentInput = UpdateTeamDiscussionCommentInput

NonNull_UpdateTeamsRepositoryInput = UpdateTeamsRepositoryInput

NonNull_UpdateTopicsInput = UpdateTopicsInput

NonNull_VerifyVerifiableDomainInput = VerifyVerifiableDomainInput

class abortQueuedMigrations(GQLMutation):
   class AbortQueuedMigrationsPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AbortQueuedMigrationsInput

   _args: AbortQueuedMigrationsPayloadArgs


   type: AbortQueuedMigrationsPayload

class acceptEnterpriseAdministratorInvitation(GQLMutation):
   class AcceptEnterpriseAdministratorInvitationPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AcceptEnterpriseAdministratorInvitationInput

   _args: AcceptEnterpriseAdministratorInvitationPayloadArgs


   type: AcceptEnterpriseAdministratorInvitationPayload

class acceptTopicSuggestion(GQLMutation):
   class AcceptTopicSuggestionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AcceptTopicSuggestionInput

   _args: AcceptTopicSuggestionPayloadArgs


   type: AcceptTopicSuggestionPayload

class addAssigneesToAssignable(GQLMutation):
   class AddAssigneesToAssignablePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddAssigneesToAssignableInput

   _args: AddAssigneesToAssignablePayloadArgs


   type: AddAssigneesToAssignablePayload

class addComment(GQLMutation):
   class AddCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddCommentInput

   _args: AddCommentPayloadArgs


   type: AddCommentPayload

class addDiscussionComment(GQLMutation):
   class AddDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddDiscussionCommentInput

   _args: AddDiscussionCommentPayloadArgs


   type: AddDiscussionCommentPayload

class addDiscussionPollVote(GQLMutation):
   class AddDiscussionPollVotePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddDiscussionPollVoteInput

   _args: AddDiscussionPollVotePayloadArgs


   type: AddDiscussionPollVotePayload

class addEnterpriseOrganizationMember(GQLMutation):
   class AddEnterpriseOrganizationMemberPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddEnterpriseOrganizationMemberInput

   _args: AddEnterpriseOrganizationMemberPayloadArgs


   type: AddEnterpriseOrganizationMemberPayload

class addEnterpriseSupportEntitlement(GQLMutation):
   class AddEnterpriseSupportEntitlementPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddEnterpriseSupportEntitlementInput

   _args: AddEnterpriseSupportEntitlementPayloadArgs


   type: AddEnterpriseSupportEntitlementPayload

class addLabelsToLabelable(GQLMutation):
   class AddLabelsToLabelablePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddLabelsToLabelableInput

   _args: AddLabelsToLabelablePayloadArgs


   type: AddLabelsToLabelablePayload

class addProjectCard(GQLMutation):
   class AddProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddProjectCardInput

   _args: AddProjectCardPayloadArgs


   type: AddProjectCardPayload

class addProjectColumn(GQLMutation):
   class AddProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddProjectColumnInput

   _args: AddProjectColumnPayloadArgs


   type: AddProjectColumnPayload

class addProjectV2DraftIssue(GQLMutation):
   class AddProjectV2DraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddProjectV2DraftIssueInput

   _args: AddProjectV2DraftIssuePayloadArgs


   type: AddProjectV2DraftIssuePayload

class addProjectV2ItemById(GQLMutation):
   class AddProjectV2ItemByIdPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddProjectV2ItemByIdInput

   _args: AddProjectV2ItemByIdPayloadArgs


   type: AddProjectV2ItemByIdPayload

class addPullRequestReview(GQLMutation):
   class AddPullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddPullRequestReviewInput

   _args: AddPullRequestReviewPayloadArgs


   type: AddPullRequestReviewPayload

class addPullRequestReviewComment(GQLMutation):
   class AddPullRequestReviewCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddPullRequestReviewCommentInput

   _args: AddPullRequestReviewCommentPayloadArgs


   type: AddPullRequestReviewCommentPayload

class addPullRequestReviewThread(GQLMutation):
   class AddPullRequestReviewThreadPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddPullRequestReviewThreadInput

   _args: AddPullRequestReviewThreadPayloadArgs


   type: AddPullRequestReviewThreadPayload

class addReaction(GQLMutation):
   class AddReactionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddReactionInput

   _args: AddReactionPayloadArgs


   type: AddReactionPayload

class addStar(GQLMutation):
   class AddStarPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddStarInput

   _args: AddStarPayloadArgs


   type: AddStarPayload

class addUpvote(GQLMutation):
   class AddUpvotePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddUpvoteInput

   _args: AddUpvotePayloadArgs


   type: AddUpvotePayload

class addVerifiableDomain(GQLMutation):
   class AddVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_AddVerifiableDomainInput

   _args: AddVerifiableDomainPayloadArgs


   type: AddVerifiableDomainPayload

class approveDeployments(GQLMutation):
   class ApproveDeploymentsPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ApproveDeploymentsInput

   _args: ApproveDeploymentsPayloadArgs


   type: ApproveDeploymentsPayload

class approveVerifiableDomain(GQLMutation):
   class ApproveVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ApproveVerifiableDomainInput

   _args: ApproveVerifiableDomainPayloadArgs


   type: ApproveVerifiableDomainPayload

class archiveProjectV2Item(GQLMutation):
   class ArchiveProjectV2ItemPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ArchiveProjectV2ItemInput

   _args: ArchiveProjectV2ItemPayloadArgs


   type: ArchiveProjectV2ItemPayload

class archiveRepository(GQLMutation):
   class ArchiveRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ArchiveRepositoryInput

   _args: ArchiveRepositoryPayloadArgs


   type: ArchiveRepositoryPayload

class cancelEnterpriseAdminInvitation(GQLMutation):
   class CancelEnterpriseAdminInvitationPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CancelEnterpriseAdminInvitationInput

   _args: CancelEnterpriseAdminInvitationPayloadArgs


   type: CancelEnterpriseAdminInvitationPayload

class cancelSponsorship(GQLMutation):
   class CancelSponsorshipPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CancelSponsorshipInput

   _args: CancelSponsorshipPayloadArgs


   type: CancelSponsorshipPayload

class changeUserStatus(GQLMutation):
   class ChangeUserStatusPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ChangeUserStatusInput

   _args: ChangeUserStatusPayloadArgs


   type: ChangeUserStatusPayload

class clearLabelsFromLabelable(GQLMutation):
   class ClearLabelsFromLabelablePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ClearLabelsFromLabelableInput

   _args: ClearLabelsFromLabelablePayloadArgs


   type: ClearLabelsFromLabelablePayload

class clearProjectV2ItemFieldValue(GQLMutation):
   class ClearProjectV2ItemFieldValuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ClearProjectV2ItemFieldValueInput

   _args: ClearProjectV2ItemFieldValuePayloadArgs


   type: ClearProjectV2ItemFieldValuePayload

class cloneProject(GQLMutation):
   class CloneProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CloneProjectInput

   _args: CloneProjectPayloadArgs


   type: CloneProjectPayload

class cloneTemplateRepository(GQLMutation):
   class CloneTemplateRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CloneTemplateRepositoryInput

   _args: CloneTemplateRepositoryPayloadArgs


   type: CloneTemplateRepositoryPayload

class closeIssue(GQLMutation):
   class CloseIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CloseIssueInput

   _args: CloseIssuePayloadArgs


   type: CloseIssuePayload

class closePullRequest(GQLMutation):
   class ClosePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ClosePullRequestInput

   _args: ClosePullRequestPayloadArgs


   type: ClosePullRequestPayload

class convertProjectCardNoteToIssue(GQLMutation):
   class ConvertProjectCardNoteToIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ConvertProjectCardNoteToIssueInput

   _args: ConvertProjectCardNoteToIssuePayloadArgs


   type: ConvertProjectCardNoteToIssuePayload

class convertPullRequestToDraft(GQLMutation):
   class ConvertPullRequestToDraftPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ConvertPullRequestToDraftInput

   _args: ConvertPullRequestToDraftPayloadArgs


   type: ConvertPullRequestToDraftPayload

class createAttributionInvitation(GQLMutation):
   class CreateAttributionInvitationPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateAttributionInvitationInput

   _args: CreateAttributionInvitationPayloadArgs


   type: CreateAttributionInvitationPayload

class createBranchProtectionRule(GQLMutation):
   class CreateBranchProtectionRulePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateBranchProtectionRuleInput

   _args: CreateBranchProtectionRulePayloadArgs


   type: CreateBranchProtectionRulePayload

class createCheckRun(GQLMutation):
   class CreateCheckRunPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateCheckRunInput

   _args: CreateCheckRunPayloadArgs


   type: CreateCheckRunPayload

class createCheckSuite(GQLMutation):
   class CreateCheckSuitePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateCheckSuiteInput

   _args: CreateCheckSuitePayloadArgs


   type: CreateCheckSuitePayload

class createCommitOnBranch(GQLMutation):
   class CreateCommitOnBranchPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateCommitOnBranchInput

   _args: CreateCommitOnBranchPayloadArgs


   type: CreateCommitOnBranchPayload

class createDiscussion(GQLMutation):
   class CreateDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateDiscussionInput

   _args: CreateDiscussionPayloadArgs


   type: CreateDiscussionPayload

class createEnterpriseOrganization(GQLMutation):
   class CreateEnterpriseOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateEnterpriseOrganizationInput

   _args: CreateEnterpriseOrganizationPayloadArgs


   type: CreateEnterpriseOrganizationPayload

class createEnvironment(GQLMutation):
   class CreateEnvironmentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateEnvironmentInput

   _args: CreateEnvironmentPayloadArgs


   type: CreateEnvironmentPayload

class createIpAllowListEntry(GQLMutation):
   class CreateIpAllowListEntryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateIpAllowListEntryInput

   _args: CreateIpAllowListEntryPayloadArgs


   type: CreateIpAllowListEntryPayload

class createIssue(GQLMutation):
   class CreateIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateIssueInput

   _args: CreateIssuePayloadArgs


   type: CreateIssuePayload

class createLinkedBranch(GQLMutation):
   class CreateLinkedBranchPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateLinkedBranchInput

   _args: CreateLinkedBranchPayloadArgs


   type: CreateLinkedBranchPayload

class createMigrationSource(GQLMutation):
   class CreateMigrationSourcePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateMigrationSourceInput

   _args: CreateMigrationSourcePayloadArgs


   type: CreateMigrationSourcePayload

class createProject(GQLMutation):
   class CreateProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateProjectInput

   _args: CreateProjectPayloadArgs


   type: CreateProjectPayload

class createProjectV2(GQLMutation):
   class CreateProjectV2PayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateProjectV2Input

   _args: CreateProjectV2PayloadArgs


   type: CreateProjectV2Payload

class createPullRequest(GQLMutation):
   class CreatePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreatePullRequestInput

   _args: CreatePullRequestPayloadArgs


   type: CreatePullRequestPayload

class createRef(GQLMutation):
   class CreateRefPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateRefInput

   _args: CreateRefPayloadArgs


   type: CreateRefPayload

class createRepository(GQLMutation):
   class CreateRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateRepositoryInput

   _args: CreateRepositoryPayloadArgs


   type: CreateRepositoryPayload

class createSponsorsListing(GQLMutation):
   class CreateSponsorsListingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateSponsorsListingInput

   _args: CreateSponsorsListingPayloadArgs


   type: CreateSponsorsListingPayload

class createSponsorsTier(GQLMutation):
   class CreateSponsorsTierPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateSponsorsTierInput

   _args: CreateSponsorsTierPayloadArgs


   type: CreateSponsorsTierPayload

class createSponsorship(GQLMutation):
   class CreateSponsorshipPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateSponsorshipInput

   _args: CreateSponsorshipPayloadArgs


   type: CreateSponsorshipPayload

class createTeamDiscussion(GQLMutation):
   class CreateTeamDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateTeamDiscussionInput

   _args: CreateTeamDiscussionPayloadArgs


   type: CreateTeamDiscussionPayload

class createTeamDiscussionComment(GQLMutation):
   class CreateTeamDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_CreateTeamDiscussionCommentInput

   _args: CreateTeamDiscussionCommentPayloadArgs


   type: CreateTeamDiscussionCommentPayload

class declineTopicSuggestion(GQLMutation):
   class DeclineTopicSuggestionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeclineTopicSuggestionInput

   _args: DeclineTopicSuggestionPayloadArgs


   type: DeclineTopicSuggestionPayload

class deleteBranchProtectionRule(GQLMutation):
   class DeleteBranchProtectionRulePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteBranchProtectionRuleInput

   _args: DeleteBranchProtectionRulePayloadArgs


   type: DeleteBranchProtectionRulePayload

class deleteDeployment(GQLMutation):
   class DeleteDeploymentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteDeploymentInput

   _args: DeleteDeploymentPayloadArgs


   type: DeleteDeploymentPayload

class deleteDiscussion(GQLMutation):
   class DeleteDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteDiscussionInput

   _args: DeleteDiscussionPayloadArgs


   type: DeleteDiscussionPayload

class deleteDiscussionComment(GQLMutation):
   class DeleteDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteDiscussionCommentInput

   _args: DeleteDiscussionCommentPayloadArgs


   type: DeleteDiscussionCommentPayload

class deleteEnvironment(GQLMutation):
   class DeleteEnvironmentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteEnvironmentInput

   _args: DeleteEnvironmentPayloadArgs


   type: DeleteEnvironmentPayload

class deleteIpAllowListEntry(GQLMutation):
   class DeleteIpAllowListEntryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteIpAllowListEntryInput

   _args: DeleteIpAllowListEntryPayloadArgs


   type: DeleteIpAllowListEntryPayload

class deleteIssue(GQLMutation):
   class DeleteIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteIssueInput

   _args: DeleteIssuePayloadArgs


   type: DeleteIssuePayload

class deleteIssueComment(GQLMutation):
   class DeleteIssueCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteIssueCommentInput

   _args: DeleteIssueCommentPayloadArgs


   type: DeleteIssueCommentPayload

class deleteLinkedBranch(GQLMutation):
   class DeleteLinkedBranchPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteLinkedBranchInput

   _args: DeleteLinkedBranchPayloadArgs


   type: DeleteLinkedBranchPayload

class deleteProject(GQLMutation):
   class DeleteProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteProjectInput

   _args: DeleteProjectPayloadArgs


   type: DeleteProjectPayload

class deleteProjectCard(GQLMutation):
   class DeleteProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteProjectCardInput

   _args: DeleteProjectCardPayloadArgs


   type: DeleteProjectCardPayload

class deleteProjectColumn(GQLMutation):
   class DeleteProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteProjectColumnInput

   _args: DeleteProjectColumnPayloadArgs


   type: DeleteProjectColumnPayload

class deleteProjectV2Item(GQLMutation):
   class DeleteProjectV2ItemPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteProjectV2ItemInput

   _args: DeleteProjectV2ItemPayloadArgs


   type: DeleteProjectV2ItemPayload

class deletePullRequestReview(GQLMutation):
   class DeletePullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeletePullRequestReviewInput

   _args: DeletePullRequestReviewPayloadArgs


   type: DeletePullRequestReviewPayload

class deletePullRequestReviewComment(GQLMutation):
   class DeletePullRequestReviewCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeletePullRequestReviewCommentInput

   _args: DeletePullRequestReviewCommentPayloadArgs


   type: DeletePullRequestReviewCommentPayload

class deleteRef(GQLMutation):
   class DeleteRefPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteRefInput

   _args: DeleteRefPayloadArgs


   type: DeleteRefPayload

class deleteTeamDiscussion(GQLMutation):
   class DeleteTeamDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteTeamDiscussionInput

   _args: DeleteTeamDiscussionPayloadArgs


   type: DeleteTeamDiscussionPayload

class deleteTeamDiscussionComment(GQLMutation):
   class DeleteTeamDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteTeamDiscussionCommentInput

   _args: DeleteTeamDiscussionCommentPayloadArgs


   type: DeleteTeamDiscussionCommentPayload

class deleteVerifiableDomain(GQLMutation):
   class DeleteVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DeleteVerifiableDomainInput

   _args: DeleteVerifiableDomainPayloadArgs


   type: DeleteVerifiableDomainPayload

class disablePullRequestAutoMerge(GQLMutation):
   class DisablePullRequestAutoMergePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DisablePullRequestAutoMergeInput

   _args: DisablePullRequestAutoMergePayloadArgs


   type: DisablePullRequestAutoMergePayload

class dismissPullRequestReview(GQLMutation):
   class DismissPullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DismissPullRequestReviewInput

   _args: DismissPullRequestReviewPayloadArgs


   type: DismissPullRequestReviewPayload

class dismissRepositoryVulnerabilityAlert(GQLMutation):
   class DismissRepositoryVulnerabilityAlertPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_DismissRepositoryVulnerabilityAlertInput

   _args: DismissRepositoryVulnerabilityAlertPayloadArgs


   type: DismissRepositoryVulnerabilityAlertPayload

class enablePullRequestAutoMerge(GQLMutation):
   class EnablePullRequestAutoMergePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_EnablePullRequestAutoMergeInput

   _args: EnablePullRequestAutoMergePayloadArgs


   type: EnablePullRequestAutoMergePayload

class followOrganization(GQLMutation):
   class FollowOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_FollowOrganizationInput

   _args: FollowOrganizationPayloadArgs


   type: FollowOrganizationPayload

class followUser(GQLMutation):
   class FollowUserPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_FollowUserInput

   _args: FollowUserPayloadArgs


   type: FollowUserPayload

class grantEnterpriseOrganizationsMigratorRole(GQLMutation):
   class GrantEnterpriseOrganizationsMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_GrantEnterpriseOrganizationsMigratorRoleInput

   _args: GrantEnterpriseOrganizationsMigratorRolePayloadArgs


   type: GrantEnterpriseOrganizationsMigratorRolePayload

class grantMigratorRole(GQLMutation):
   class GrantMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_GrantMigratorRoleInput

   _args: GrantMigratorRolePayloadArgs


   type: GrantMigratorRolePayload

class inviteEnterpriseAdmin(GQLMutation):
   class InviteEnterpriseAdminPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_InviteEnterpriseAdminInput

   _args: InviteEnterpriseAdminPayloadArgs


   type: InviteEnterpriseAdminPayload

class linkProjectV2ToRepository(GQLMutation):
   class LinkProjectV2ToRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_LinkProjectV2ToRepositoryInput

   _args: LinkProjectV2ToRepositoryPayloadArgs


   type: LinkProjectV2ToRepositoryPayload

class linkProjectV2ToTeam(GQLMutation):
   class LinkProjectV2ToTeamPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_LinkProjectV2ToTeamInput

   _args: LinkProjectV2ToTeamPayloadArgs


   type: LinkProjectV2ToTeamPayload

class linkRepositoryToProject(GQLMutation):
   class LinkRepositoryToProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_LinkRepositoryToProjectInput

   _args: LinkRepositoryToProjectPayloadArgs


   type: LinkRepositoryToProjectPayload

class lockLockable(GQLMutation):
   class LockLockablePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_LockLockableInput

   _args: LockLockablePayloadArgs


   type: LockLockablePayload

class markDiscussionCommentAsAnswer(GQLMutation):
   class MarkDiscussionCommentAsAnswerPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_MarkDiscussionCommentAsAnswerInput

   _args: MarkDiscussionCommentAsAnswerPayloadArgs


   type: MarkDiscussionCommentAsAnswerPayload

class markFileAsViewed(GQLMutation):
   class MarkFileAsViewedPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_MarkFileAsViewedInput

   _args: MarkFileAsViewedPayloadArgs


   type: MarkFileAsViewedPayload

class markPullRequestReadyForReview(GQLMutation):
   class MarkPullRequestReadyForReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_MarkPullRequestReadyForReviewInput

   _args: MarkPullRequestReadyForReviewPayloadArgs


   type: MarkPullRequestReadyForReviewPayload

class mergeBranch(GQLMutation):
   class MergeBranchPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_MergeBranchInput

   _args: MergeBranchPayloadArgs


   type: MergeBranchPayload

class mergePullRequest(GQLMutation):
   class MergePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_MergePullRequestInput

   _args: MergePullRequestPayloadArgs


   type: MergePullRequestPayload

class minimizeComment(GQLMutation):
   class MinimizeCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_MinimizeCommentInput

   _args: MinimizeCommentPayloadArgs


   type: MinimizeCommentPayload

class moveProjectCard(GQLMutation):
   class MoveProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_MoveProjectCardInput

   _args: MoveProjectCardPayloadArgs


   type: MoveProjectCardPayload

class moveProjectColumn(GQLMutation):
   class MoveProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_MoveProjectColumnInput

   _args: MoveProjectColumnPayloadArgs


   type: MoveProjectColumnPayload

class pinIssue(GQLMutation):
   class PinIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_PinIssueInput

   _args: PinIssuePayloadArgs


   type: PinIssuePayload

class publishSponsorsTier(GQLMutation):
   class PublishSponsorsTierPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_PublishSponsorsTierInput

   _args: PublishSponsorsTierPayloadArgs


   type: PublishSponsorsTierPayload

class regenerateEnterpriseIdentityProviderRecoveryCodes(GQLMutation):
   class RegenerateEnterpriseIdentityProviderRecoveryCodesPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RegenerateEnterpriseIdentityProviderRecoveryCodesInput

   _args: RegenerateEnterpriseIdentityProviderRecoveryCodesPayloadArgs


   type: RegenerateEnterpriseIdentityProviderRecoveryCodesPayload

class regenerateVerifiableDomainToken(GQLMutation):
   class RegenerateVerifiableDomainTokenPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RegenerateVerifiableDomainTokenInput

   _args: RegenerateVerifiableDomainTokenPayloadArgs


   type: RegenerateVerifiableDomainTokenPayload

class rejectDeployments(GQLMutation):
   class RejectDeploymentsPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RejectDeploymentsInput

   _args: RejectDeploymentsPayloadArgs


   type: RejectDeploymentsPayload

class removeAssigneesFromAssignable(GQLMutation):
   class RemoveAssigneesFromAssignablePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RemoveAssigneesFromAssignableInput

   _args: RemoveAssigneesFromAssignablePayloadArgs


   type: RemoveAssigneesFromAssignablePayload

class removeEnterpriseAdmin(GQLMutation):
   class RemoveEnterpriseAdminPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RemoveEnterpriseAdminInput

   _args: RemoveEnterpriseAdminPayloadArgs


   type: RemoveEnterpriseAdminPayload

class removeEnterpriseIdentityProvider(GQLMutation):
   class RemoveEnterpriseIdentityProviderPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RemoveEnterpriseIdentityProviderInput

   _args: RemoveEnterpriseIdentityProviderPayloadArgs


   type: RemoveEnterpriseIdentityProviderPayload

class removeEnterpriseOrganization(GQLMutation):
   class RemoveEnterpriseOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RemoveEnterpriseOrganizationInput

   _args: RemoveEnterpriseOrganizationPayloadArgs


   type: RemoveEnterpriseOrganizationPayload

class removeEnterpriseSupportEntitlement(GQLMutation):
   class RemoveEnterpriseSupportEntitlementPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RemoveEnterpriseSupportEntitlementInput

   _args: RemoveEnterpriseSupportEntitlementPayloadArgs


   type: RemoveEnterpriseSupportEntitlementPayload

class removeLabelsFromLabelable(GQLMutation):
   class RemoveLabelsFromLabelablePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RemoveLabelsFromLabelableInput

   _args: RemoveLabelsFromLabelablePayloadArgs


   type: RemoveLabelsFromLabelablePayload

class removeOutsideCollaborator(GQLMutation):
   class RemoveOutsideCollaboratorPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RemoveOutsideCollaboratorInput

   _args: RemoveOutsideCollaboratorPayloadArgs


   type: RemoveOutsideCollaboratorPayload

class removeReaction(GQLMutation):
   class RemoveReactionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RemoveReactionInput

   _args: RemoveReactionPayloadArgs


   type: RemoveReactionPayload

class removeStar(GQLMutation):
   class RemoveStarPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RemoveStarInput

   _args: RemoveStarPayloadArgs


   type: RemoveStarPayload

class removeUpvote(GQLMutation):
   class RemoveUpvotePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RemoveUpvoteInput

   _args: RemoveUpvotePayloadArgs


   type: RemoveUpvotePayload

class reopenIssue(GQLMutation):
   class ReopenIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ReopenIssueInput

   _args: ReopenIssuePayloadArgs


   type: ReopenIssuePayload

class reopenPullRequest(GQLMutation):
   class ReopenPullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ReopenPullRequestInput

   _args: ReopenPullRequestPayloadArgs


   type: ReopenPullRequestPayload

class requestReviews(GQLMutation):
   class RequestReviewsPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RequestReviewsInput

   _args: RequestReviewsPayloadArgs


   type: RequestReviewsPayload

class rerequestCheckSuite(GQLMutation):
   class RerequestCheckSuitePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RerequestCheckSuiteInput

   _args: RerequestCheckSuitePayloadArgs


   type: RerequestCheckSuitePayload

class resolveReviewThread(GQLMutation):
   class ResolveReviewThreadPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_ResolveReviewThreadInput

   _args: ResolveReviewThreadPayloadArgs


   type: ResolveReviewThreadPayload

class retireSponsorsTier(GQLMutation):
   class RetireSponsorsTierPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RetireSponsorsTierInput

   _args: RetireSponsorsTierPayloadArgs


   type: RetireSponsorsTierPayload

class revokeEnterpriseOrganizationsMigratorRole(GQLMutation):
   class RevokeEnterpriseOrganizationsMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RevokeEnterpriseOrganizationsMigratorRoleInput

   _args: RevokeEnterpriseOrganizationsMigratorRolePayloadArgs


   type: RevokeEnterpriseOrganizationsMigratorRolePayload

class revokeMigratorRole(GQLMutation):
   class RevokeMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_RevokeMigratorRoleInput

   _args: RevokeMigratorRolePayloadArgs


   type: RevokeMigratorRolePayload

class setEnterpriseIdentityProvider(GQLMutation):
   class SetEnterpriseIdentityProviderPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_SetEnterpriseIdentityProviderInput

   _args: SetEnterpriseIdentityProviderPayloadArgs


   type: SetEnterpriseIdentityProviderPayload

class setOrganizationInteractionLimit(GQLMutation):
   class SetOrganizationInteractionLimitPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_SetOrganizationInteractionLimitInput

   _args: SetOrganizationInteractionLimitPayloadArgs


   type: SetOrganizationInteractionLimitPayload

class setRepositoryInteractionLimit(GQLMutation):
   class SetRepositoryInteractionLimitPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_SetRepositoryInteractionLimitInput

   _args: SetRepositoryInteractionLimitPayloadArgs


   type: SetRepositoryInteractionLimitPayload

class setUserInteractionLimit(GQLMutation):
   class SetUserInteractionLimitPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_SetUserInteractionLimitInput

   _args: SetUserInteractionLimitPayloadArgs


   type: SetUserInteractionLimitPayload

class startOrganizationMigration(GQLMutation):
   class StartOrganizationMigrationPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_StartOrganizationMigrationInput

   _args: StartOrganizationMigrationPayloadArgs


   type: StartOrganizationMigrationPayload

class startRepositoryMigration(GQLMutation):
   class StartRepositoryMigrationPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_StartRepositoryMigrationInput

   _args: StartRepositoryMigrationPayloadArgs


   type: StartRepositoryMigrationPayload

class submitPullRequestReview(GQLMutation):
   class SubmitPullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_SubmitPullRequestReviewInput

   _args: SubmitPullRequestReviewPayloadArgs


   type: SubmitPullRequestReviewPayload

class transferEnterpriseOrganization(GQLMutation):
   class TransferEnterpriseOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_TransferEnterpriseOrganizationInput

   _args: TransferEnterpriseOrganizationPayloadArgs


   type: TransferEnterpriseOrganizationPayload

class transferIssue(GQLMutation):
   class TransferIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_TransferIssueInput

   _args: TransferIssuePayloadArgs


   type: TransferIssuePayload

class unarchiveProjectV2Item(GQLMutation):
   class UnarchiveProjectV2ItemPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnarchiveProjectV2ItemInput

   _args: UnarchiveProjectV2ItemPayloadArgs


   type: UnarchiveProjectV2ItemPayload

class unarchiveRepository(GQLMutation):
   class UnarchiveRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnarchiveRepositoryInput

   _args: UnarchiveRepositoryPayloadArgs


   type: UnarchiveRepositoryPayload

class unfollowOrganization(GQLMutation):
   class UnfollowOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnfollowOrganizationInput

   _args: UnfollowOrganizationPayloadArgs


   type: UnfollowOrganizationPayload

class unfollowUser(GQLMutation):
   class UnfollowUserPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnfollowUserInput

   _args: UnfollowUserPayloadArgs


   type: UnfollowUserPayload

class unlinkProjectV2FromRepository(GQLMutation):
   class UnlinkProjectV2FromRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnlinkProjectV2FromRepositoryInput

   _args: UnlinkProjectV2FromRepositoryPayloadArgs


   type: UnlinkProjectV2FromRepositoryPayload

class unlinkProjectV2FromTeam(GQLMutation):
   class UnlinkProjectV2FromTeamPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnlinkProjectV2FromTeamInput

   _args: UnlinkProjectV2FromTeamPayloadArgs


   type: UnlinkProjectV2FromTeamPayload

class unlinkRepositoryFromProject(GQLMutation):
   class UnlinkRepositoryFromProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnlinkRepositoryFromProjectInput

   _args: UnlinkRepositoryFromProjectPayloadArgs


   type: UnlinkRepositoryFromProjectPayload

class unlockLockable(GQLMutation):
   class UnlockLockablePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnlockLockableInput

   _args: UnlockLockablePayloadArgs


   type: UnlockLockablePayload

class unmarkDiscussionCommentAsAnswer(GQLMutation):
   class UnmarkDiscussionCommentAsAnswerPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnmarkDiscussionCommentAsAnswerInput

   _args: UnmarkDiscussionCommentAsAnswerPayloadArgs


   type: UnmarkDiscussionCommentAsAnswerPayload

class unmarkFileAsViewed(GQLMutation):
   class UnmarkFileAsViewedPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnmarkFileAsViewedInput

   _args: UnmarkFileAsViewedPayloadArgs


   type: UnmarkFileAsViewedPayload

class unmarkIssueAsDuplicate(GQLMutation):
   class UnmarkIssueAsDuplicatePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnmarkIssueAsDuplicateInput

   _args: UnmarkIssueAsDuplicatePayloadArgs


   type: UnmarkIssueAsDuplicatePayload

class unminimizeComment(GQLMutation):
   class UnminimizeCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnminimizeCommentInput

   _args: UnminimizeCommentPayloadArgs


   type: UnminimizeCommentPayload

class unpinIssue(GQLMutation):
   class UnpinIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnpinIssueInput

   _args: UnpinIssuePayloadArgs


   type: UnpinIssuePayload

class unresolveReviewThread(GQLMutation):
   class UnresolveReviewThreadPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UnresolveReviewThreadInput

   _args: UnresolveReviewThreadPayloadArgs


   type: UnresolveReviewThreadPayload

class updateBranchProtectionRule(GQLMutation):
   class UpdateBranchProtectionRulePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateBranchProtectionRuleInput

   _args: UpdateBranchProtectionRulePayloadArgs


   type: UpdateBranchProtectionRulePayload

class updateCheckRun(GQLMutation):
   class UpdateCheckRunPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateCheckRunInput

   _args: UpdateCheckRunPayloadArgs


   type: UpdateCheckRunPayload

class updateCheckSuitePreferences(GQLMutation):
   class UpdateCheckSuitePreferencesPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateCheckSuitePreferencesInput

   _args: UpdateCheckSuitePreferencesPayloadArgs


   type: UpdateCheckSuitePreferencesPayload

class updateDiscussion(GQLMutation):
   class UpdateDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateDiscussionInput

   _args: UpdateDiscussionPayloadArgs


   type: UpdateDiscussionPayload

class updateDiscussionComment(GQLMutation):
   class UpdateDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateDiscussionCommentInput

   _args: UpdateDiscussionCommentPayloadArgs


   type: UpdateDiscussionCommentPayload

class updateEnterpriseAdministratorRole(GQLMutation):
   class UpdateEnterpriseAdministratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseAdministratorRoleInput

   _args: UpdateEnterpriseAdministratorRolePayloadArgs


   type: UpdateEnterpriseAdministratorRolePayload

class updateEnterpriseAllowPrivateRepositoryForkingSetting(GQLMutation):
   class UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput

   _args: UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayloadArgs


   type: UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload

class updateEnterpriseDefaultRepositoryPermissionSetting(GQLMutation):
   class UpdateEnterpriseDefaultRepositoryPermissionSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseDefaultRepositoryPermissionSettingInput

   _args: UpdateEnterpriseDefaultRepositoryPermissionSettingPayloadArgs


   type: UpdateEnterpriseDefaultRepositoryPermissionSettingPayload

class updateEnterpriseMembersCanChangeRepositoryVisibilitySetting(GQLMutation):
   class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput

   _args: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayloadArgs


   type: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload

class updateEnterpriseMembersCanCreateRepositoriesSetting(GQLMutation):
   class UpdateEnterpriseMembersCanCreateRepositoriesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseMembersCanCreateRepositoriesSettingInput

   _args: UpdateEnterpriseMembersCanCreateRepositoriesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload

class updateEnterpriseMembersCanDeleteIssuesSetting(GQLMutation):
   class UpdateEnterpriseMembersCanDeleteIssuesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseMembersCanDeleteIssuesSettingInput

   _args: UpdateEnterpriseMembersCanDeleteIssuesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanDeleteIssuesSettingPayload

class updateEnterpriseMembersCanDeleteRepositoriesSetting(GQLMutation):
   class UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput

   _args: UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload

class updateEnterpriseMembersCanInviteCollaboratorsSetting(GQLMutation):
   class UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput

   _args: UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayloadArgs


   type: UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload

class updateEnterpriseMembersCanMakePurchasesSetting(GQLMutation):
   class UpdateEnterpriseMembersCanMakePurchasesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseMembersCanMakePurchasesSettingInput

   _args: UpdateEnterpriseMembersCanMakePurchasesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanMakePurchasesSettingPayload

class updateEnterpriseMembersCanUpdateProtectedBranchesSetting(GQLMutation):
   class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput

   _args: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload

class updateEnterpriseMembersCanViewDependencyInsightsSetting(GQLMutation):
   class UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput

   _args: UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayloadArgs


   type: UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload

class updateEnterpriseOrganizationProjectsSetting(GQLMutation):
   class UpdateEnterpriseOrganizationProjectsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseOrganizationProjectsSettingInput

   _args: UpdateEnterpriseOrganizationProjectsSettingPayloadArgs


   type: UpdateEnterpriseOrganizationProjectsSettingPayload

class updateEnterpriseOwnerOrganizationRole(GQLMutation):
   class UpdateEnterpriseOwnerOrganizationRolePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseOwnerOrganizationRoleInput

   _args: UpdateEnterpriseOwnerOrganizationRolePayloadArgs


   type: UpdateEnterpriseOwnerOrganizationRolePayload

class updateEnterpriseProfile(GQLMutation):
   class UpdateEnterpriseProfilePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseProfileInput

   _args: UpdateEnterpriseProfilePayloadArgs


   type: UpdateEnterpriseProfilePayload

class updateEnterpriseRepositoryProjectsSetting(GQLMutation):
   class UpdateEnterpriseRepositoryProjectsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseRepositoryProjectsSettingInput

   _args: UpdateEnterpriseRepositoryProjectsSettingPayloadArgs


   type: UpdateEnterpriseRepositoryProjectsSettingPayload

class updateEnterpriseTeamDiscussionsSetting(GQLMutation):
   class UpdateEnterpriseTeamDiscussionsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseTeamDiscussionsSettingInput

   _args: UpdateEnterpriseTeamDiscussionsSettingPayloadArgs


   type: UpdateEnterpriseTeamDiscussionsSettingPayload

class updateEnterpriseTwoFactorAuthenticationRequiredSetting(GQLMutation):
   class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput

   _args: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayloadArgs


   type: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload

class updateEnvironment(GQLMutation):
   class UpdateEnvironmentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateEnvironmentInput

   _args: UpdateEnvironmentPayloadArgs


   type: UpdateEnvironmentPayload

class updateIpAllowListEnabledSetting(GQLMutation):
   class UpdateIpAllowListEnabledSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateIpAllowListEnabledSettingInput

   _args: UpdateIpAllowListEnabledSettingPayloadArgs


   type: UpdateIpAllowListEnabledSettingPayload

class updateIpAllowListEntry(GQLMutation):
   class UpdateIpAllowListEntryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateIpAllowListEntryInput

   _args: UpdateIpAllowListEntryPayloadArgs


   type: UpdateIpAllowListEntryPayload

class updateIpAllowListForInstalledAppsEnabledSetting(GQLMutation):
   class UpdateIpAllowListForInstalledAppsEnabledSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateIpAllowListForInstalledAppsEnabledSettingInput

   _args: UpdateIpAllowListForInstalledAppsEnabledSettingPayloadArgs


   type: UpdateIpAllowListForInstalledAppsEnabledSettingPayload

class updateIssue(GQLMutation):
   class UpdateIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateIssueInput

   _args: UpdateIssuePayloadArgs


   type: UpdateIssuePayload

class updateIssueComment(GQLMutation):
   class UpdateIssueCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateIssueCommentInput

   _args: UpdateIssueCommentPayloadArgs


   type: UpdateIssueCommentPayload

class updateNotificationRestrictionSetting(GQLMutation):
   class UpdateNotificationRestrictionSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateNotificationRestrictionSettingInput

   _args: UpdateNotificationRestrictionSettingPayloadArgs


   type: UpdateNotificationRestrictionSettingPayload

class updateOrganizationAllowPrivateRepositoryForkingSetting(GQLMutation):
   class UpdateOrganizationAllowPrivateRepositoryForkingSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateOrganizationAllowPrivateRepositoryForkingSettingInput

   _args: UpdateOrganizationAllowPrivateRepositoryForkingSettingPayloadArgs


   type: UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload

class updateOrganizationWebCommitSignoffSetting(GQLMutation):
   class UpdateOrganizationWebCommitSignoffSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateOrganizationWebCommitSignoffSettingInput

   _args: UpdateOrganizationWebCommitSignoffSettingPayloadArgs


   type: UpdateOrganizationWebCommitSignoffSettingPayload

class updateProject(GQLMutation):
   class UpdateProjectPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateProjectInput

   _args: UpdateProjectPayloadArgs


   type: UpdateProjectPayload

class updateProjectCard(GQLMutation):
   class UpdateProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateProjectCardInput

   _args: UpdateProjectCardPayloadArgs


   type: UpdateProjectCardPayload

class updateProjectColumn(GQLMutation):
   class UpdateProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateProjectColumnInput

   _args: UpdateProjectColumnPayloadArgs


   type: UpdateProjectColumnPayload

class updateProjectV2(GQLMutation):
   class UpdateProjectV2PayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateProjectV2Input

   _args: UpdateProjectV2PayloadArgs


   type: UpdateProjectV2Payload

class updateProjectV2DraftIssue(GQLMutation):
   class UpdateProjectV2DraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateProjectV2DraftIssueInput

   _args: UpdateProjectV2DraftIssuePayloadArgs


   type: UpdateProjectV2DraftIssuePayload

class updateProjectV2ItemFieldValue(GQLMutation):
   class UpdateProjectV2ItemFieldValuePayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateProjectV2ItemFieldValueInput

   _args: UpdateProjectV2ItemFieldValuePayloadArgs


   type: UpdateProjectV2ItemFieldValuePayload

class updateProjectV2ItemPosition(GQLMutation):
   class UpdateProjectV2ItemPositionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateProjectV2ItemPositionInput

   _args: UpdateProjectV2ItemPositionPayloadArgs


   type: UpdateProjectV2ItemPositionPayload

class updatePullRequest(GQLMutation):
   class UpdatePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdatePullRequestInput

   _args: UpdatePullRequestPayloadArgs


   type: UpdatePullRequestPayload

class updatePullRequestBranch(GQLMutation):
   class UpdatePullRequestBranchPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdatePullRequestBranchInput

   _args: UpdatePullRequestBranchPayloadArgs


   type: UpdatePullRequestBranchPayload

class updatePullRequestReview(GQLMutation):
   class UpdatePullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdatePullRequestReviewInput

   _args: UpdatePullRequestReviewPayloadArgs


   type: UpdatePullRequestReviewPayload

class updatePullRequestReviewComment(GQLMutation):
   class UpdatePullRequestReviewCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdatePullRequestReviewCommentInput

   _args: UpdatePullRequestReviewCommentPayloadArgs


   type: UpdatePullRequestReviewCommentPayload

class updateRef(GQLMutation):
   class UpdateRefPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateRefInput

   _args: UpdateRefPayloadArgs


   type: UpdateRefPayload

class updateRepository(GQLMutation):
   class UpdateRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateRepositoryInput

   _args: UpdateRepositoryPayloadArgs


   type: UpdateRepositoryPayload

class updateRepositoryWebCommitSignoffSetting(GQLMutation):
   class UpdateRepositoryWebCommitSignoffSettingPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateRepositoryWebCommitSignoffSettingInput

   _args: UpdateRepositoryWebCommitSignoffSettingPayloadArgs


   type: UpdateRepositoryWebCommitSignoffSettingPayload

class updateSponsorshipPreferences(GQLMutation):
   class UpdateSponsorshipPreferencesPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateSponsorshipPreferencesInput

   _args: UpdateSponsorshipPreferencesPayloadArgs


   type: UpdateSponsorshipPreferencesPayload

class updateSubscription(GQLMutation):
   class UpdateSubscriptionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateSubscriptionInput

   _args: UpdateSubscriptionPayloadArgs


   type: UpdateSubscriptionPayload

class updateTeamDiscussion(GQLMutation):
   class UpdateTeamDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateTeamDiscussionInput

   _args: UpdateTeamDiscussionPayloadArgs


   type: UpdateTeamDiscussionPayload

class updateTeamDiscussionComment(GQLMutation):
   class UpdateTeamDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateTeamDiscussionCommentInput

   _args: UpdateTeamDiscussionCommentPayloadArgs


   type: UpdateTeamDiscussionCommentPayload

class updateTeamsRepository(GQLMutation):
   class UpdateTeamsRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateTeamsRepositoryInput

   _args: UpdateTeamsRepositoryPayloadArgs


   type: UpdateTeamsRepositoryPayload

class updateTopics(GQLMutation):
   class UpdateTopicsPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_UpdateTopicsInput

   _args: UpdateTopicsPayloadArgs


   type: UpdateTopicsPayload

class verifyVerifiableDomain(GQLMutation):
   class VerifyVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      input: NonNull_VerifyVerifiableDomainInput

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
   retireSponsorsTier = retireSponsorsTier
   revokeEnterpriseOrganizationsMigratorRole = revokeEnterpriseOrganizationsMigratorRole
   revokeMigratorRole = revokeMigratorRole
   setEnterpriseIdentityProvider = setEnterpriseIdentityProvider
   setOrganizationInteractionLimit = setOrganizationInteractionLimit
   setRepositoryInteractionLimit = setRepositoryInteractionLimit
   setUserInteractionLimit = setUserInteractionLimit
   startOrganizationMigration = startOrganizationMigration
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
