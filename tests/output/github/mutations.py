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
   """
   abortQueuedMigrations - Clear all of a customer's queued migrations

   """
   class AbortQueuedMigrationsPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AbortQueuedMigrations

      """
      input: NonNull_AbortQueuedMigrationsInput

   _args: AbortQueuedMigrationsPayloadArgs


   type: AbortQueuedMigrationsPayload

class acceptEnterpriseAdministratorInvitation(GQLMutation):
   """
   acceptEnterpriseAdministratorInvitation - Accepts a pending invitation for a user to become an administrator of an enterprise.

   """
   class AcceptEnterpriseAdministratorInvitationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AcceptEnterpriseAdministratorInvitation

      """
      input: NonNull_AcceptEnterpriseAdministratorInvitationInput

   _args: AcceptEnterpriseAdministratorInvitationPayloadArgs


   type: AcceptEnterpriseAdministratorInvitationPayload

class acceptTopicSuggestion(GQLMutation):
   """
   acceptTopicSuggestion - Applies a suggested topic to the repository.

   """
   class AcceptTopicSuggestionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AcceptTopicSuggestion

      """
      input: NonNull_AcceptTopicSuggestionInput

   _args: AcceptTopicSuggestionPayloadArgs


   type: AcceptTopicSuggestionPayload

class addAssigneesToAssignable(GQLMutation):
   """
   addAssigneesToAssignable - Adds assignees to an assignable object.

   """
   class AddAssigneesToAssignablePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddAssigneesToAssignable

      """
      input: NonNull_AddAssigneesToAssignableInput

   _args: AddAssigneesToAssignablePayloadArgs


   type: AddAssigneesToAssignablePayload

class addComment(GQLMutation):
   """
   addComment - Adds a comment to an Issue or Pull Request.

   """
   class AddCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddComment

      """
      input: NonNull_AddCommentInput

   _args: AddCommentPayloadArgs


   type: AddCommentPayload

class addDiscussionComment(GQLMutation):
   """
   addDiscussionComment - Adds a comment to a Discussion, possibly as a reply to another comment.

   """
   class AddDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddDiscussionComment

      """
      input: NonNull_AddDiscussionCommentInput

   _args: AddDiscussionCommentPayloadArgs


   type: AddDiscussionCommentPayload

class addDiscussionPollVote(GQLMutation):
   """
   addDiscussionPollVote - Vote for an option in a discussion poll.

   """
   class AddDiscussionPollVotePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddDiscussionPollVote

      """
      input: NonNull_AddDiscussionPollVoteInput

   _args: AddDiscussionPollVotePayloadArgs


   type: AddDiscussionPollVotePayload

class addEnterpriseOrganizationMember(GQLMutation):
   """
   addEnterpriseOrganizationMember - Adds enterprise members to an organization within the enterprise.

   """
   class AddEnterpriseOrganizationMemberPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddEnterpriseOrganizationMember

      """
      input: NonNull_AddEnterpriseOrganizationMemberInput

   _args: AddEnterpriseOrganizationMemberPayloadArgs


   type: AddEnterpriseOrganizationMemberPayload

class addEnterpriseSupportEntitlement(GQLMutation):
   """
   addEnterpriseSupportEntitlement - Adds a support entitlement to an enterprise member.

   """
   class AddEnterpriseSupportEntitlementPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddEnterpriseSupportEntitlement

      """
      input: NonNull_AddEnterpriseSupportEntitlementInput

   _args: AddEnterpriseSupportEntitlementPayloadArgs


   type: AddEnterpriseSupportEntitlementPayload

class addLabelsToLabelable(GQLMutation):
   """
   addLabelsToLabelable - Adds labels to a labelable object.

   """
   class AddLabelsToLabelablePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddLabelsToLabelable

      """
      input: NonNull_AddLabelsToLabelableInput

   _args: AddLabelsToLabelablePayloadArgs


   type: AddLabelsToLabelablePayload

class addProjectCard(GQLMutation):
   """
   addProjectCard - Adds a card to a ProjectColumn. Either `contentId` or `note` must be provided but **not** both.

   """
   class AddProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddProjectCard

      """
      input: NonNull_AddProjectCardInput

   _args: AddProjectCardPayloadArgs


   type: AddProjectCardPayload

class addProjectColumn(GQLMutation):
   """
   addProjectColumn - Adds a column to a Project.

   """
   class AddProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddProjectColumn

      """
      input: NonNull_AddProjectColumnInput

   _args: AddProjectColumnPayloadArgs


   type: AddProjectColumnPayload

class addProjectV2DraftIssue(GQLMutation):
   """
   addProjectV2DraftIssue - Creates a new draft issue and add it to a Project.

   """
   class AddProjectV2DraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddProjectV2DraftIssue

      """
      input: NonNull_AddProjectV2DraftIssueInput

   _args: AddProjectV2DraftIssuePayloadArgs


   type: AddProjectV2DraftIssuePayload

class addProjectV2ItemById(GQLMutation):
   """
   addProjectV2ItemById - Links an existing content instance to a Project.

   """
   class AddProjectV2ItemByIdPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddProjectV2ItemById

      """
      input: NonNull_AddProjectV2ItemByIdInput

   _args: AddProjectV2ItemByIdPayloadArgs


   type: AddProjectV2ItemByIdPayload

class addPullRequestReview(GQLMutation):
   """
   addPullRequestReview - Adds a review to a Pull Request.

   """
   class AddPullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddPullRequestReview

      """
      input: NonNull_AddPullRequestReviewInput

   _args: AddPullRequestReviewPayloadArgs


   type: AddPullRequestReviewPayload

class addPullRequestReviewComment(GQLMutation):
   """
   addPullRequestReviewComment - Adds a comment to a review.

   """
   class AddPullRequestReviewCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddPullRequestReviewComment

      """
      input: NonNull_AddPullRequestReviewCommentInput

   _args: AddPullRequestReviewCommentPayloadArgs


   type: AddPullRequestReviewCommentPayload

class addPullRequestReviewThread(GQLMutation):
   """
   addPullRequestReviewThread - Adds a new thread to a pending Pull Request Review.

   """
   class AddPullRequestReviewThreadPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddPullRequestReviewThread

      """
      input: NonNull_AddPullRequestReviewThreadInput

   _args: AddPullRequestReviewThreadPayloadArgs


   type: AddPullRequestReviewThreadPayload

class addReaction(GQLMutation):
   """
   addReaction - Adds a reaction to a subject.

   """
   class AddReactionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddReaction

      """
      input: NonNull_AddReactionInput

   _args: AddReactionPayloadArgs


   type: AddReactionPayload

class addStar(GQLMutation):
   """
   addStar - Adds a star to a Starrable.

   """
   class AddStarPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddStar

      """
      input: NonNull_AddStarInput

   _args: AddStarPayloadArgs


   type: AddStarPayload

class addUpvote(GQLMutation):
   """
   addUpvote - Add an upvote to a discussion or discussion comment.

   """
   class AddUpvotePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddUpvote

      """
      input: NonNull_AddUpvoteInput

   _args: AddUpvotePayloadArgs


   type: AddUpvotePayload

class addVerifiableDomain(GQLMutation):
   """
   addVerifiableDomain - Adds a verifiable domain to an owning account.

   """
   class AddVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddVerifiableDomain

      """
      input: NonNull_AddVerifiableDomainInput

   _args: AddVerifiableDomainPayloadArgs


   type: AddVerifiableDomainPayload

class approveDeployments(GQLMutation):
   """
   approveDeployments - Approve all pending deployments under one or more environments

   """
   class ApproveDeploymentsPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ApproveDeployments

      """
      input: NonNull_ApproveDeploymentsInput

   _args: ApproveDeploymentsPayloadArgs


   type: ApproveDeploymentsPayload

class approveVerifiableDomain(GQLMutation):
   """
   approveVerifiableDomain - Approve a verifiable domain for notification delivery.

   """
   class ApproveVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ApproveVerifiableDomain

      """
      input: NonNull_ApproveVerifiableDomainInput

   _args: ApproveVerifiableDomainPayloadArgs


   type: ApproveVerifiableDomainPayload

class archiveProjectV2Item(GQLMutation):
   """
   archiveProjectV2Item - Archives a ProjectV2Item

   """
   class ArchiveProjectV2ItemPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ArchiveProjectV2Item

      """
      input: NonNull_ArchiveProjectV2ItemInput

   _args: ArchiveProjectV2ItemPayloadArgs


   type: ArchiveProjectV2ItemPayload

class archiveRepository(GQLMutation):
   """
   archiveRepository - Marks a repository as archived.

   """
   class ArchiveRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ArchiveRepository

      """
      input: NonNull_ArchiveRepositoryInput

   _args: ArchiveRepositoryPayloadArgs


   type: ArchiveRepositoryPayload

class cancelEnterpriseAdminInvitation(GQLMutation):
   """
   cancelEnterpriseAdminInvitation - Cancels a pending invitation for an administrator to join an enterprise.

   """
   class CancelEnterpriseAdminInvitationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CancelEnterpriseAdminInvitation

      """
      input: NonNull_CancelEnterpriseAdminInvitationInput

   _args: CancelEnterpriseAdminInvitationPayloadArgs


   type: CancelEnterpriseAdminInvitationPayload

class cancelSponsorship(GQLMutation):
   """
   cancelSponsorship - Cancel an active sponsorship.

   """
   class CancelSponsorshipPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CancelSponsorship

      """
      input: NonNull_CancelSponsorshipInput

   _args: CancelSponsorshipPayloadArgs


   type: CancelSponsorshipPayload

class changeUserStatus(GQLMutation):
   """
   changeUserStatus - Update your status on GitHub.

   """
   class ChangeUserStatusPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ChangeUserStatus

      """
      input: NonNull_ChangeUserStatusInput

   _args: ChangeUserStatusPayloadArgs


   type: ChangeUserStatusPayload

class clearLabelsFromLabelable(GQLMutation):
   """
   clearLabelsFromLabelable - Clears all labels from a labelable object.

   """
   class ClearLabelsFromLabelablePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ClearLabelsFromLabelable

      """
      input: NonNull_ClearLabelsFromLabelableInput

   _args: ClearLabelsFromLabelablePayloadArgs


   type: ClearLabelsFromLabelablePayload

class clearProjectV2ItemFieldValue(GQLMutation):
   """
   clearProjectV2ItemFieldValue - This mutation clears the value of a field for an item in a Project. Currently only text, number, date, assignees, labels, single-select, iteration and milestone fields are supported.

   """
   class ClearProjectV2ItemFieldValuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ClearProjectV2ItemFieldValue

      """
      input: NonNull_ClearProjectV2ItemFieldValueInput

   _args: ClearProjectV2ItemFieldValuePayloadArgs


   type: ClearProjectV2ItemFieldValuePayload

class cloneProject(GQLMutation):
   """
   cloneProject - Creates a new project by cloning configuration from an existing project.

   """
   class CloneProjectPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CloneProject

      """
      input: NonNull_CloneProjectInput

   _args: CloneProjectPayloadArgs


   type: CloneProjectPayload

class cloneTemplateRepository(GQLMutation):
   """
   cloneTemplateRepository - Create a new repository with the same files and directory structure as a template repository.

   """
   class CloneTemplateRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CloneTemplateRepository

      """
      input: NonNull_CloneTemplateRepositoryInput

   _args: CloneTemplateRepositoryPayloadArgs


   type: CloneTemplateRepositoryPayload

class closeIssue(GQLMutation):
   """
   closeIssue - Close an issue.

   """
   class CloseIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CloseIssue

      """
      input: NonNull_CloseIssueInput

   _args: CloseIssuePayloadArgs


   type: CloseIssuePayload

class closePullRequest(GQLMutation):
   """
   closePullRequest - Close a pull request.

   """
   class ClosePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ClosePullRequest

      """
      input: NonNull_ClosePullRequestInput

   _args: ClosePullRequestPayloadArgs


   type: ClosePullRequestPayload

class convertProjectCardNoteToIssue(GQLMutation):
   """
   convertProjectCardNoteToIssue - Convert a project note card to one associated with a newly created issue.

   """
   class ConvertProjectCardNoteToIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ConvertProjectCardNoteToIssue

      """
      input: NonNull_ConvertProjectCardNoteToIssueInput

   _args: ConvertProjectCardNoteToIssuePayloadArgs


   type: ConvertProjectCardNoteToIssuePayload

class convertPullRequestToDraft(GQLMutation):
   """
   convertPullRequestToDraft - Converts a pull request to draft

   """
   class ConvertPullRequestToDraftPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ConvertPullRequestToDraft

      """
      input: NonNull_ConvertPullRequestToDraftInput

   _args: ConvertPullRequestToDraftPayloadArgs


   type: ConvertPullRequestToDraftPayload

class createAttributionInvitation(GQLMutation):
   """
   createAttributionInvitation - Invites a user to claim reattributable data

   """
   class CreateAttributionInvitationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateAttributionInvitation

      """
      input: NonNull_CreateAttributionInvitationInput

   _args: CreateAttributionInvitationPayloadArgs


   type: CreateAttributionInvitationPayload

class createBranchProtectionRule(GQLMutation):
   """
   createBranchProtectionRule - Create a new branch protection rule

   """
   class CreateBranchProtectionRulePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateBranchProtectionRule

      """
      input: NonNull_CreateBranchProtectionRuleInput

   _args: CreateBranchProtectionRulePayloadArgs


   type: CreateBranchProtectionRulePayload

class createCheckRun(GQLMutation):
   """
   createCheckRun - Create a check run.

   """
   class CreateCheckRunPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateCheckRun

      """
      input: NonNull_CreateCheckRunInput

   _args: CreateCheckRunPayloadArgs


   type: CreateCheckRunPayload

class createCheckSuite(GQLMutation):
   """
   createCheckSuite - Create a check suite

   """
   class CreateCheckSuitePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateCheckSuite

      """
      input: NonNull_CreateCheckSuiteInput

   _args: CreateCheckSuitePayloadArgs


   type: CreateCheckSuitePayload

class createCommitOnBranch(GQLMutation):
   """
   createCommitOnBranch - Appends a commit to the given branch as the authenticated user.

This mutation creates a commit whose parent is the HEAD of the provided
branch and also updates that branch to point to the new commit.
It can be thought of as similar to `git commit`.

### Locating a Branch

Commits are appended to a `branch` of type `Ref`.
This must refer to a git branch (i.e.  the fully qualified path must
begin with `refs/heads/`, although including this prefix is optional.

Callers may specify the `branch` to commit to either by its global node
ID or by passing both of `repositoryNameWithOwner` and `refName`.  For
more details see the documentation for `CommittableBranch`.

### Describing Changes

`fileChanges` are specified as a `FilesChanges` object describing
`FileAdditions` and `FileDeletions`.

Please see the documentation for `FileChanges` for more information on
how to use this argument to describe any set of file changes.

### Authorship

Similar to the web commit interface, this mutation does not support
specifying the author or committer of the commit and will not add
support for this in the future.

A commit created by a successful execution of this mutation will be
authored by the owner of the credential which authenticates the API
request.  The committer will be identical to that of commits authored
using the web interface.

If you need full control over author and committer information, please
use the Git Database REST API instead.

### Commit Signing

Commits made using this mutation are automatically signed by GitHub if
supported and will be marked as verified in the user interface.


   """
   class CreateCommitOnBranchPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateCommitOnBranch

      """
      input: NonNull_CreateCommitOnBranchInput

   _args: CreateCommitOnBranchPayloadArgs


   type: CreateCommitOnBranchPayload

class createDiscussion(GQLMutation):
   """
   createDiscussion - Create a discussion.

   """
   class CreateDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateDiscussion

      """
      input: NonNull_CreateDiscussionInput

   _args: CreateDiscussionPayloadArgs


   type: CreateDiscussionPayload

class createEnterpriseOrganization(GQLMutation):
   """
   createEnterpriseOrganization - Creates an organization as part of an enterprise account.

   """
   class CreateEnterpriseOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateEnterpriseOrganization

      """
      input: NonNull_CreateEnterpriseOrganizationInput

   _args: CreateEnterpriseOrganizationPayloadArgs


   type: CreateEnterpriseOrganizationPayload

class createEnvironment(GQLMutation):
   """
   createEnvironment - Creates an environment or simply returns it if already exists.

   """
   class CreateEnvironmentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateEnvironment

      """
      input: NonNull_CreateEnvironmentInput

   _args: CreateEnvironmentPayloadArgs


   type: CreateEnvironmentPayload

class createIpAllowListEntry(GQLMutation):
   """
   createIpAllowListEntry - Creates a new IP allow list entry.

   """
   class CreateIpAllowListEntryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateIpAllowListEntry

      """
      input: NonNull_CreateIpAllowListEntryInput

   _args: CreateIpAllowListEntryPayloadArgs


   type: CreateIpAllowListEntryPayload

class createIssue(GQLMutation):
   """
   createIssue - Creates a new issue.

   """
   class CreateIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateIssue

      """
      input: NonNull_CreateIssueInput

   _args: CreateIssuePayloadArgs


   type: CreateIssuePayload

class createLinkedBranch(GQLMutation):
   """
   createLinkedBranch - Create a branch linked to an issue.

   """
   class CreateLinkedBranchPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateLinkedBranch

      """
      input: NonNull_CreateLinkedBranchInput

   _args: CreateLinkedBranchPayloadArgs


   type: CreateLinkedBranchPayload

class createMigrationSource(GQLMutation):
   """
   createMigrationSource - Creates a GitHub Enterprise Importer (GEI) migration source.

   """
   class CreateMigrationSourcePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateMigrationSource

      """
      input: NonNull_CreateMigrationSourceInput

   _args: CreateMigrationSourcePayloadArgs


   type: CreateMigrationSourcePayload

class createProject(GQLMutation):
   """
   createProject - Creates a new project.

   """
   class CreateProjectPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateProject

      """
      input: NonNull_CreateProjectInput

   _args: CreateProjectPayloadArgs


   type: CreateProjectPayload

class createProjectV2(GQLMutation):
   """
   createProjectV2 - Creates a new project.

   """
   class CreateProjectV2PayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateProjectV2

      """
      input: NonNull_CreateProjectV2Input

   _args: CreateProjectV2PayloadArgs


   type: CreateProjectV2Payload

class createPullRequest(GQLMutation):
   """
   createPullRequest - Create a new pull request

   """
   class CreatePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreatePullRequest

      """
      input: NonNull_CreatePullRequestInput

   _args: CreatePullRequestPayloadArgs


   type: CreatePullRequestPayload

class createRef(GQLMutation):
   """
   createRef - Create a new Git Ref.

   """
   class CreateRefPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateRef

      """
      input: NonNull_CreateRefInput

   _args: CreateRefPayloadArgs


   type: CreateRefPayload

class createRepository(GQLMutation):
   """
   createRepository - Create a new repository.

   """
   class CreateRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateRepository

      """
      input: NonNull_CreateRepositoryInput

   _args: CreateRepositoryPayloadArgs


   type: CreateRepositoryPayload

class createSponsorsListing(GQLMutation):
   """
   createSponsorsListing - Create a GitHub Sponsors profile to allow others to sponsor you or your organization.

   """
   class CreateSponsorsListingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateSponsorsListing

      """
      input: NonNull_CreateSponsorsListingInput

   _args: CreateSponsorsListingPayloadArgs


   type: CreateSponsorsListingPayload

class createSponsorsTier(GQLMutation):
   """
   createSponsorsTier - Create a new payment tier for your GitHub Sponsors profile.

   """
   class CreateSponsorsTierPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateSponsorsTier

      """
      input: NonNull_CreateSponsorsTierInput

   _args: CreateSponsorsTierPayloadArgs


   type: CreateSponsorsTierPayload

class createSponsorship(GQLMutation):
   """
   createSponsorship - Start a new sponsorship of a maintainer in GitHub Sponsors, or reactivate a past sponsorship.

   """
   class CreateSponsorshipPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateSponsorship

      """
      input: NonNull_CreateSponsorshipInput

   _args: CreateSponsorshipPayloadArgs


   type: CreateSponsorshipPayload

class createTeamDiscussion(GQLMutation):
   """
   createTeamDiscussion - Creates a new team discussion.

   """
   class CreateTeamDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateTeamDiscussion

      """
      input: NonNull_CreateTeamDiscussionInput

   _args: CreateTeamDiscussionPayloadArgs


   type: CreateTeamDiscussionPayload

class createTeamDiscussionComment(GQLMutation):
   """
   createTeamDiscussionComment - Creates a new team discussion comment.

   """
   class CreateTeamDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for CreateTeamDiscussionComment

      """
      input: NonNull_CreateTeamDiscussionCommentInput

   _args: CreateTeamDiscussionCommentPayloadArgs


   type: CreateTeamDiscussionCommentPayload

class declineTopicSuggestion(GQLMutation):
   """
   declineTopicSuggestion - Rejects a suggested topic for the repository.

   """
   class DeclineTopicSuggestionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeclineTopicSuggestion

      """
      input: NonNull_DeclineTopicSuggestionInput

   _args: DeclineTopicSuggestionPayloadArgs


   type: DeclineTopicSuggestionPayload

class deleteBranchProtectionRule(GQLMutation):
   """
   deleteBranchProtectionRule - Delete a branch protection rule

   """
   class DeleteBranchProtectionRulePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteBranchProtectionRule

      """
      input: NonNull_DeleteBranchProtectionRuleInput

   _args: DeleteBranchProtectionRulePayloadArgs


   type: DeleteBranchProtectionRulePayload

class deleteDeployment(GQLMutation):
   """
   deleteDeployment - Deletes a deployment.

   """
   class DeleteDeploymentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteDeployment

      """
      input: NonNull_DeleteDeploymentInput

   _args: DeleteDeploymentPayloadArgs


   type: DeleteDeploymentPayload

class deleteDiscussion(GQLMutation):
   """
   deleteDiscussion - Delete a discussion and all of its replies.

   """
   class DeleteDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteDiscussion

      """
      input: NonNull_DeleteDiscussionInput

   _args: DeleteDiscussionPayloadArgs


   type: DeleteDiscussionPayload

class deleteDiscussionComment(GQLMutation):
   """
   deleteDiscussionComment - Delete a discussion comment. If it has replies, wipe it instead.

   """
   class DeleteDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteDiscussionComment

      """
      input: NonNull_DeleteDiscussionCommentInput

   _args: DeleteDiscussionCommentPayloadArgs


   type: DeleteDiscussionCommentPayload

class deleteEnvironment(GQLMutation):
   """
   deleteEnvironment - Deletes an environment

   """
   class DeleteEnvironmentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteEnvironment

      """
      input: NonNull_DeleteEnvironmentInput

   _args: DeleteEnvironmentPayloadArgs


   type: DeleteEnvironmentPayload

class deleteIpAllowListEntry(GQLMutation):
   """
   deleteIpAllowListEntry - Deletes an IP allow list entry.

   """
   class DeleteIpAllowListEntryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteIpAllowListEntry

      """
      input: NonNull_DeleteIpAllowListEntryInput

   _args: DeleteIpAllowListEntryPayloadArgs


   type: DeleteIpAllowListEntryPayload

class deleteIssue(GQLMutation):
   """
   deleteIssue - Deletes an Issue object.

   """
   class DeleteIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteIssue

      """
      input: NonNull_DeleteIssueInput

   _args: DeleteIssuePayloadArgs


   type: DeleteIssuePayload

class deleteIssueComment(GQLMutation):
   """
   deleteIssueComment - Deletes an IssueComment object.

   """
   class DeleteIssueCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteIssueComment

      """
      input: NonNull_DeleteIssueCommentInput

   _args: DeleteIssueCommentPayloadArgs


   type: DeleteIssueCommentPayload

class deleteLinkedBranch(GQLMutation):
   """
   deleteLinkedBranch - Unlink a branch from an issue.

   """
   class DeleteLinkedBranchPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteLinkedBranch

      """
      input: NonNull_DeleteLinkedBranchInput

   _args: DeleteLinkedBranchPayloadArgs


   type: DeleteLinkedBranchPayload

class deleteProject(GQLMutation):
   """
   deleteProject - Deletes a project.

   """
   class DeleteProjectPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteProject

      """
      input: NonNull_DeleteProjectInput

   _args: DeleteProjectPayloadArgs


   type: DeleteProjectPayload

class deleteProjectCard(GQLMutation):
   """
   deleteProjectCard - Deletes a project card.

   """
   class DeleteProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteProjectCard

      """
      input: NonNull_DeleteProjectCardInput

   _args: DeleteProjectCardPayloadArgs


   type: DeleteProjectCardPayload

class deleteProjectColumn(GQLMutation):
   """
   deleteProjectColumn - Deletes a project column.

   """
   class DeleteProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteProjectColumn

      """
      input: NonNull_DeleteProjectColumnInput

   _args: DeleteProjectColumnPayloadArgs


   type: DeleteProjectColumnPayload

class deleteProjectV2Item(GQLMutation):
   """
   deleteProjectV2Item - Deletes an item from a Project.

   """
   class DeleteProjectV2ItemPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteProjectV2Item

      """
      input: NonNull_DeleteProjectV2ItemInput

   _args: DeleteProjectV2ItemPayloadArgs


   type: DeleteProjectV2ItemPayload

class deletePullRequestReview(GQLMutation):
   """
   deletePullRequestReview - Deletes a pull request review.

   """
   class DeletePullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeletePullRequestReview

      """
      input: NonNull_DeletePullRequestReviewInput

   _args: DeletePullRequestReviewPayloadArgs


   type: DeletePullRequestReviewPayload

class deletePullRequestReviewComment(GQLMutation):
   """
   deletePullRequestReviewComment - Deletes a pull request review comment.

   """
   class DeletePullRequestReviewCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeletePullRequestReviewComment

      """
      input: NonNull_DeletePullRequestReviewCommentInput

   _args: DeletePullRequestReviewCommentPayloadArgs


   type: DeletePullRequestReviewCommentPayload

class deleteRef(GQLMutation):
   """
   deleteRef - Delete a Git Ref.

   """
   class DeleteRefPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteRef

      """
      input: NonNull_DeleteRefInput

   _args: DeleteRefPayloadArgs


   type: DeleteRefPayload

class deleteTeamDiscussion(GQLMutation):
   """
   deleteTeamDiscussion - Deletes a team discussion.

   """
   class DeleteTeamDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteTeamDiscussion

      """
      input: NonNull_DeleteTeamDiscussionInput

   _args: DeleteTeamDiscussionPayloadArgs


   type: DeleteTeamDiscussionPayload

class deleteTeamDiscussionComment(GQLMutation):
   """
   deleteTeamDiscussionComment - Deletes a team discussion comment.

   """
   class DeleteTeamDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteTeamDiscussionComment

      """
      input: NonNull_DeleteTeamDiscussionCommentInput

   _args: DeleteTeamDiscussionCommentPayloadArgs


   type: DeleteTeamDiscussionCommentPayload

class deleteVerifiableDomain(GQLMutation):
   """
   deleteVerifiableDomain - Deletes a verifiable domain.

   """
   class DeleteVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteVerifiableDomain

      """
      input: NonNull_DeleteVerifiableDomainInput

   _args: DeleteVerifiableDomainPayloadArgs


   type: DeleteVerifiableDomainPayload

class disablePullRequestAutoMerge(GQLMutation):
   """
   disablePullRequestAutoMerge - Disable auto merge on the given pull request

   """
   class DisablePullRequestAutoMergePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DisablePullRequestAutoMerge

      """
      input: NonNull_DisablePullRequestAutoMergeInput

   _args: DisablePullRequestAutoMergePayloadArgs


   type: DisablePullRequestAutoMergePayload

class dismissPullRequestReview(GQLMutation):
   """
   dismissPullRequestReview - Dismisses an approved or rejected pull request review.

   """
   class DismissPullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DismissPullRequestReview

      """
      input: NonNull_DismissPullRequestReviewInput

   _args: DismissPullRequestReviewPayloadArgs


   type: DismissPullRequestReviewPayload

class dismissRepositoryVulnerabilityAlert(GQLMutation):
   """
   dismissRepositoryVulnerabilityAlert - Dismisses the Dependabot alert.

   """
   class DismissRepositoryVulnerabilityAlertPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DismissRepositoryVulnerabilityAlert

      """
      input: NonNull_DismissRepositoryVulnerabilityAlertInput

   _args: DismissRepositoryVulnerabilityAlertPayloadArgs


   type: DismissRepositoryVulnerabilityAlertPayload

class enablePullRequestAutoMerge(GQLMutation):
   """
   enablePullRequestAutoMerge - Enable the default auto-merge on a pull request.

   """
   class EnablePullRequestAutoMergePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for EnablePullRequestAutoMerge

      """
      input: NonNull_EnablePullRequestAutoMergeInput

   _args: EnablePullRequestAutoMergePayloadArgs


   type: EnablePullRequestAutoMergePayload

class followOrganization(GQLMutation):
   """
   followOrganization - Follow an organization.

   """
   class FollowOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for FollowOrganization

      """
      input: NonNull_FollowOrganizationInput

   _args: FollowOrganizationPayloadArgs


   type: FollowOrganizationPayload

class followUser(GQLMutation):
   """
   followUser - Follow a user.

   """
   class FollowUserPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for FollowUser

      """
      input: NonNull_FollowUserInput

   _args: FollowUserPayloadArgs


   type: FollowUserPayload

class grantEnterpriseOrganizationsMigratorRole(GQLMutation):
   """
   grantEnterpriseOrganizationsMigratorRole - Grant the migrator role to a user for all organizations under an enterprise account.

   """
   class GrantEnterpriseOrganizationsMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for GrantEnterpriseOrganizationsMigratorRole

      """
      input: NonNull_GrantEnterpriseOrganizationsMigratorRoleInput

   _args: GrantEnterpriseOrganizationsMigratorRolePayloadArgs


   type: GrantEnterpriseOrganizationsMigratorRolePayload

class grantMigratorRole(GQLMutation):
   """
   grantMigratorRole - Grant the migrator role to a user or a team.

   """
   class GrantMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for GrantMigratorRole

      """
      input: NonNull_GrantMigratorRoleInput

   _args: GrantMigratorRolePayloadArgs


   type: GrantMigratorRolePayload

class inviteEnterpriseAdmin(GQLMutation):
   """
   inviteEnterpriseAdmin - Invite someone to become an administrator of the enterprise.

   """
   class InviteEnterpriseAdminPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for InviteEnterpriseAdmin

      """
      input: NonNull_InviteEnterpriseAdminInput

   _args: InviteEnterpriseAdminPayloadArgs


   type: InviteEnterpriseAdminPayload

class linkProjectV2ToRepository(GQLMutation):
   """
   linkProjectV2ToRepository - Links a project to a repository.

   """
   class LinkProjectV2ToRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for LinkProjectV2ToRepository

      """
      input: NonNull_LinkProjectV2ToRepositoryInput

   _args: LinkProjectV2ToRepositoryPayloadArgs


   type: LinkProjectV2ToRepositoryPayload

class linkProjectV2ToTeam(GQLMutation):
   """
   linkProjectV2ToTeam - Links a project to a team.

   """
   class LinkProjectV2ToTeamPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for LinkProjectV2ToTeam

      """
      input: NonNull_LinkProjectV2ToTeamInput

   _args: LinkProjectV2ToTeamPayloadArgs


   type: LinkProjectV2ToTeamPayload

class linkRepositoryToProject(GQLMutation):
   """
   linkRepositoryToProject - Creates a repository link for a project.

   """
   class LinkRepositoryToProjectPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for LinkRepositoryToProject

      """
      input: NonNull_LinkRepositoryToProjectInput

   _args: LinkRepositoryToProjectPayloadArgs


   type: LinkRepositoryToProjectPayload

class lockLockable(GQLMutation):
   """
   lockLockable - Lock a lockable object

   """
   class LockLockablePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for LockLockable

      """
      input: NonNull_LockLockableInput

   _args: LockLockablePayloadArgs


   type: LockLockablePayload

class markDiscussionCommentAsAnswer(GQLMutation):
   """
   markDiscussionCommentAsAnswer - Mark a discussion comment as the chosen answer for discussions in an answerable category.

   """
   class MarkDiscussionCommentAsAnswerPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for MarkDiscussionCommentAsAnswer

      """
      input: NonNull_MarkDiscussionCommentAsAnswerInput

   _args: MarkDiscussionCommentAsAnswerPayloadArgs


   type: MarkDiscussionCommentAsAnswerPayload

class markFileAsViewed(GQLMutation):
   """
   markFileAsViewed - Mark a pull request file as viewed

   """
   class MarkFileAsViewedPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for MarkFileAsViewed

      """
      input: NonNull_MarkFileAsViewedInput

   _args: MarkFileAsViewedPayloadArgs


   type: MarkFileAsViewedPayload

class markPullRequestReadyForReview(GQLMutation):
   """
   markPullRequestReadyForReview - Marks a pull request ready for review.

   """
   class MarkPullRequestReadyForReviewPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for MarkPullRequestReadyForReview

      """
      input: NonNull_MarkPullRequestReadyForReviewInput

   _args: MarkPullRequestReadyForReviewPayloadArgs


   type: MarkPullRequestReadyForReviewPayload

class mergeBranch(GQLMutation):
   """
   mergeBranch - Merge a head into a branch.

   """
   class MergeBranchPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for MergeBranch

      """
      input: NonNull_MergeBranchInput

   _args: MergeBranchPayloadArgs


   type: MergeBranchPayload

class mergePullRequest(GQLMutation):
   """
   mergePullRequest - Merge a pull request.

   """
   class MergePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for MergePullRequest

      """
      input: NonNull_MergePullRequestInput

   _args: MergePullRequestPayloadArgs


   type: MergePullRequestPayload

class minimizeComment(GQLMutation):
   """
   minimizeComment - Minimizes a comment on an Issue, Commit, Pull Request, or Gist

   """
   class MinimizeCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for MinimizeComment

      """
      input: NonNull_MinimizeCommentInput

   _args: MinimizeCommentPayloadArgs


   type: MinimizeCommentPayload

class moveProjectCard(GQLMutation):
   """
   moveProjectCard - Moves a project card to another place.

   """
   class MoveProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for MoveProjectCard

      """
      input: NonNull_MoveProjectCardInput

   _args: MoveProjectCardPayloadArgs


   type: MoveProjectCardPayload

class moveProjectColumn(GQLMutation):
   """
   moveProjectColumn - Moves a project column to another place.

   """
   class MoveProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for MoveProjectColumn

      """
      input: NonNull_MoveProjectColumnInput

   _args: MoveProjectColumnPayloadArgs


   type: MoveProjectColumnPayload

class pinIssue(GQLMutation):
   """
   pinIssue - Pin an issue to a repository

   """
   class PinIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for PinIssue

      """
      input: NonNull_PinIssueInput

   _args: PinIssuePayloadArgs


   type: PinIssuePayload

class publishSponsorsTier(GQLMutation):
   """
   publishSponsorsTier - Publish an existing sponsorship tier that is currently still a draft to a GitHub Sponsors profile.

   """
   class PublishSponsorsTierPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for PublishSponsorsTier

      """
      input: NonNull_PublishSponsorsTierInput

   _args: PublishSponsorsTierPayloadArgs


   type: PublishSponsorsTierPayload

class regenerateEnterpriseIdentityProviderRecoveryCodes(GQLMutation):
   """
   regenerateEnterpriseIdentityProviderRecoveryCodes - Regenerates the identity provider recovery codes for an enterprise

   """
   class RegenerateEnterpriseIdentityProviderRecoveryCodesPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RegenerateEnterpriseIdentityProviderRecoveryCodes

      """
      input: NonNull_RegenerateEnterpriseIdentityProviderRecoveryCodesInput

   _args: RegenerateEnterpriseIdentityProviderRecoveryCodesPayloadArgs


   type: RegenerateEnterpriseIdentityProviderRecoveryCodesPayload

class regenerateVerifiableDomainToken(GQLMutation):
   """
   regenerateVerifiableDomainToken - Regenerates a verifiable domain's verification token.

   """
   class RegenerateVerifiableDomainTokenPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RegenerateVerifiableDomainToken

      """
      input: NonNull_RegenerateVerifiableDomainTokenInput

   _args: RegenerateVerifiableDomainTokenPayloadArgs


   type: RegenerateVerifiableDomainTokenPayload

class rejectDeployments(GQLMutation):
   """
   rejectDeployments - Reject all pending deployments under one or more environments

   """
   class RejectDeploymentsPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RejectDeployments

      """
      input: NonNull_RejectDeploymentsInput

   _args: RejectDeploymentsPayloadArgs


   type: RejectDeploymentsPayload

class removeAssigneesFromAssignable(GQLMutation):
   """
   removeAssigneesFromAssignable - Removes assignees from an assignable object.

   """
   class RemoveAssigneesFromAssignablePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RemoveAssigneesFromAssignable

      """
      input: NonNull_RemoveAssigneesFromAssignableInput

   _args: RemoveAssigneesFromAssignablePayloadArgs


   type: RemoveAssigneesFromAssignablePayload

class removeEnterpriseAdmin(GQLMutation):
   """
   removeEnterpriseAdmin - Removes an administrator from the enterprise.

   """
   class RemoveEnterpriseAdminPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RemoveEnterpriseAdmin

      """
      input: NonNull_RemoveEnterpriseAdminInput

   _args: RemoveEnterpriseAdminPayloadArgs


   type: RemoveEnterpriseAdminPayload

class removeEnterpriseIdentityProvider(GQLMutation):
   """
   removeEnterpriseIdentityProvider - Removes the identity provider from an enterprise

   """
   class RemoveEnterpriseIdentityProviderPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RemoveEnterpriseIdentityProvider

      """
      input: NonNull_RemoveEnterpriseIdentityProviderInput

   _args: RemoveEnterpriseIdentityProviderPayloadArgs


   type: RemoveEnterpriseIdentityProviderPayload

class removeEnterpriseOrganization(GQLMutation):
   """
   removeEnterpriseOrganization - Removes an organization from the enterprise

   """
   class RemoveEnterpriseOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RemoveEnterpriseOrganization

      """
      input: NonNull_RemoveEnterpriseOrganizationInput

   _args: RemoveEnterpriseOrganizationPayloadArgs


   type: RemoveEnterpriseOrganizationPayload

class removeEnterpriseSupportEntitlement(GQLMutation):
   """
   removeEnterpriseSupportEntitlement - Removes a support entitlement from an enterprise member.

   """
   class RemoveEnterpriseSupportEntitlementPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RemoveEnterpriseSupportEntitlement

      """
      input: NonNull_RemoveEnterpriseSupportEntitlementInput

   _args: RemoveEnterpriseSupportEntitlementPayloadArgs


   type: RemoveEnterpriseSupportEntitlementPayload

class removeLabelsFromLabelable(GQLMutation):
   """
   removeLabelsFromLabelable - Removes labels from a Labelable object.

   """
   class RemoveLabelsFromLabelablePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RemoveLabelsFromLabelable

      """
      input: NonNull_RemoveLabelsFromLabelableInput

   _args: RemoveLabelsFromLabelablePayloadArgs


   type: RemoveLabelsFromLabelablePayload

class removeOutsideCollaborator(GQLMutation):
   """
   removeOutsideCollaborator - Removes outside collaborator from all repositories in an organization.

   """
   class RemoveOutsideCollaboratorPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RemoveOutsideCollaborator

      """
      input: NonNull_RemoveOutsideCollaboratorInput

   _args: RemoveOutsideCollaboratorPayloadArgs


   type: RemoveOutsideCollaboratorPayload

class removeReaction(GQLMutation):
   """
   removeReaction - Removes a reaction from a subject.

   """
   class RemoveReactionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RemoveReaction

      """
      input: NonNull_RemoveReactionInput

   _args: RemoveReactionPayloadArgs


   type: RemoveReactionPayload

class removeStar(GQLMutation):
   """
   removeStar - Removes a star from a Starrable.

   """
   class RemoveStarPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RemoveStar

      """
      input: NonNull_RemoveStarInput

   _args: RemoveStarPayloadArgs


   type: RemoveStarPayload

class removeUpvote(GQLMutation):
   """
   removeUpvote - Remove an upvote to a discussion or discussion comment.

   """
   class RemoveUpvotePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RemoveUpvote

      """
      input: NonNull_RemoveUpvoteInput

   _args: RemoveUpvotePayloadArgs


   type: RemoveUpvotePayload

class reopenIssue(GQLMutation):
   """
   reopenIssue - Reopen a issue.

   """
   class ReopenIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ReopenIssue

      """
      input: NonNull_ReopenIssueInput

   _args: ReopenIssuePayloadArgs


   type: ReopenIssuePayload

class reopenPullRequest(GQLMutation):
   """
   reopenPullRequest - Reopen a pull request.

   """
   class ReopenPullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ReopenPullRequest

      """
      input: NonNull_ReopenPullRequestInput

   _args: ReopenPullRequestPayloadArgs


   type: ReopenPullRequestPayload

class requestReviews(GQLMutation):
   """
   requestReviews - Set review requests on a pull request.

   """
   class RequestReviewsPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RequestReviews

      """
      input: NonNull_RequestReviewsInput

   _args: RequestReviewsPayloadArgs


   type: RequestReviewsPayload

class rerequestCheckSuite(GQLMutation):
   """
   rerequestCheckSuite - Rerequests an existing check suite.

   """
   class RerequestCheckSuitePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RerequestCheckSuite

      """
      input: NonNull_RerequestCheckSuiteInput

   _args: RerequestCheckSuitePayloadArgs


   type: RerequestCheckSuitePayload

class resolveReviewThread(GQLMutation):
   """
   resolveReviewThread - Marks a review thread as resolved.

   """
   class ResolveReviewThreadPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for ResolveReviewThread

      """
      input: NonNull_ResolveReviewThreadInput

   _args: ResolveReviewThreadPayloadArgs


   type: ResolveReviewThreadPayload

class retireSponsorsTier(GQLMutation):
   """
   retireSponsorsTier - Retire a published payment tier from your GitHub Sponsors profile so it cannot be used to start new sponsorships.

   """
   class RetireSponsorsTierPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RetireSponsorsTier

      """
      input: NonNull_RetireSponsorsTierInput

   _args: RetireSponsorsTierPayloadArgs


   type: RetireSponsorsTierPayload

class revokeEnterpriseOrganizationsMigratorRole(GQLMutation):
   """
   revokeEnterpriseOrganizationsMigratorRole - Revoke the migrator role to a user for all organizations under an enterprise account.

   """
   class RevokeEnterpriseOrganizationsMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RevokeEnterpriseOrganizationsMigratorRole

      """
      input: NonNull_RevokeEnterpriseOrganizationsMigratorRoleInput

   _args: RevokeEnterpriseOrganizationsMigratorRolePayloadArgs


   type: RevokeEnterpriseOrganizationsMigratorRolePayload

class revokeMigratorRole(GQLMutation):
   """
   revokeMigratorRole - Revoke the migrator role from a user or a team.

   """
   class RevokeMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RevokeMigratorRole

      """
      input: NonNull_RevokeMigratorRoleInput

   _args: RevokeMigratorRolePayloadArgs


   type: RevokeMigratorRolePayload

class setEnterpriseIdentityProvider(GQLMutation):
   """
   setEnterpriseIdentityProvider - Creates or updates the identity provider for an enterprise.

   """
   class SetEnterpriseIdentityProviderPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for SetEnterpriseIdentityProvider

      """
      input: NonNull_SetEnterpriseIdentityProviderInput

   _args: SetEnterpriseIdentityProviderPayloadArgs


   type: SetEnterpriseIdentityProviderPayload

class setOrganizationInteractionLimit(GQLMutation):
   """
   setOrganizationInteractionLimit - Set an organization level interaction limit for an organization's public repositories.

   """
   class SetOrganizationInteractionLimitPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for SetOrganizationInteractionLimit

      """
      input: NonNull_SetOrganizationInteractionLimitInput

   _args: SetOrganizationInteractionLimitPayloadArgs


   type: SetOrganizationInteractionLimitPayload

class setRepositoryInteractionLimit(GQLMutation):
   """
   setRepositoryInteractionLimit - Sets an interaction limit setting for a repository.

   """
   class SetRepositoryInteractionLimitPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for SetRepositoryInteractionLimit

      """
      input: NonNull_SetRepositoryInteractionLimitInput

   _args: SetRepositoryInteractionLimitPayloadArgs


   type: SetRepositoryInteractionLimitPayload

class setUserInteractionLimit(GQLMutation):
   """
   setUserInteractionLimit - Set a user level interaction limit for an user's public repositories.

   """
   class SetUserInteractionLimitPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for SetUserInteractionLimit

      """
      input: NonNull_SetUserInteractionLimitInput

   _args: SetUserInteractionLimitPayloadArgs


   type: SetUserInteractionLimitPayload

class startOrganizationMigration(GQLMutation):
   """
   startOrganizationMigration - Starts a GitHub Enterprise Importer organization migration.

   """
   class StartOrganizationMigrationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for StartOrganizationMigration

      """
      input: NonNull_StartOrganizationMigrationInput

   _args: StartOrganizationMigrationPayloadArgs


   type: StartOrganizationMigrationPayload

class startRepositoryMigration(GQLMutation):
   """
   startRepositoryMigration - Starts a GitHub Enterprise Importer (GEI) repository migration.

   """
   class StartRepositoryMigrationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for StartRepositoryMigration

      """
      input: NonNull_StartRepositoryMigrationInput

   _args: StartRepositoryMigrationPayloadArgs


   type: StartRepositoryMigrationPayload

class submitPullRequestReview(GQLMutation):
   """
   submitPullRequestReview - Submits a pending pull request review.

   """
   class SubmitPullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for SubmitPullRequestReview

      """
      input: NonNull_SubmitPullRequestReviewInput

   _args: SubmitPullRequestReviewPayloadArgs


   type: SubmitPullRequestReviewPayload

class transferEnterpriseOrganization(GQLMutation):
   """
   transferEnterpriseOrganization - Transfer an organization from one enterprise to another enterprise.

   """
   class TransferEnterpriseOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for TransferEnterpriseOrganization

      """
      input: NonNull_TransferEnterpriseOrganizationInput

   _args: TransferEnterpriseOrganizationPayloadArgs


   type: TransferEnterpriseOrganizationPayload

class transferIssue(GQLMutation):
   """
   transferIssue - Transfer an issue to a different repository

   """
   class TransferIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for TransferIssue

      """
      input: NonNull_TransferIssueInput

   _args: TransferIssuePayloadArgs


   type: TransferIssuePayload

class unarchiveProjectV2Item(GQLMutation):
   """
   unarchiveProjectV2Item - Unarchives a ProjectV2Item

   """
   class UnarchiveProjectV2ItemPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnarchiveProjectV2Item

      """
      input: NonNull_UnarchiveProjectV2ItemInput

   _args: UnarchiveProjectV2ItemPayloadArgs


   type: UnarchiveProjectV2ItemPayload

class unarchiveRepository(GQLMutation):
   """
   unarchiveRepository - Unarchives a repository.

   """
   class UnarchiveRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnarchiveRepository

      """
      input: NonNull_UnarchiveRepositoryInput

   _args: UnarchiveRepositoryPayloadArgs


   type: UnarchiveRepositoryPayload

class unfollowOrganization(GQLMutation):
   """
   unfollowOrganization - Unfollow an organization.

   """
   class UnfollowOrganizationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnfollowOrganization

      """
      input: NonNull_UnfollowOrganizationInput

   _args: UnfollowOrganizationPayloadArgs


   type: UnfollowOrganizationPayload

class unfollowUser(GQLMutation):
   """
   unfollowUser - Unfollow a user.

   """
   class UnfollowUserPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnfollowUser

      """
      input: NonNull_UnfollowUserInput

   _args: UnfollowUserPayloadArgs


   type: UnfollowUserPayload

class unlinkProjectV2FromRepository(GQLMutation):
   """
   unlinkProjectV2FromRepository - Unlinks a project from a repository.

   """
   class UnlinkProjectV2FromRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnlinkProjectV2FromRepository

      """
      input: NonNull_UnlinkProjectV2FromRepositoryInput

   _args: UnlinkProjectV2FromRepositoryPayloadArgs


   type: UnlinkProjectV2FromRepositoryPayload

class unlinkProjectV2FromTeam(GQLMutation):
   """
   unlinkProjectV2FromTeam - Unlinks a project to a team.

   """
   class UnlinkProjectV2FromTeamPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnlinkProjectV2FromTeam

      """
      input: NonNull_UnlinkProjectV2FromTeamInput

   _args: UnlinkProjectV2FromTeamPayloadArgs


   type: UnlinkProjectV2FromTeamPayload

class unlinkRepositoryFromProject(GQLMutation):
   """
   unlinkRepositoryFromProject - Deletes a repository link from a project.

   """
   class UnlinkRepositoryFromProjectPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnlinkRepositoryFromProject

      """
      input: NonNull_UnlinkRepositoryFromProjectInput

   _args: UnlinkRepositoryFromProjectPayloadArgs


   type: UnlinkRepositoryFromProjectPayload

class unlockLockable(GQLMutation):
   """
   unlockLockable - Unlock a lockable object

   """
   class UnlockLockablePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnlockLockable

      """
      input: NonNull_UnlockLockableInput

   _args: UnlockLockablePayloadArgs


   type: UnlockLockablePayload

class unmarkDiscussionCommentAsAnswer(GQLMutation):
   """
   unmarkDiscussionCommentAsAnswer - Unmark a discussion comment as the chosen answer for discussions in an answerable category.

   """
   class UnmarkDiscussionCommentAsAnswerPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnmarkDiscussionCommentAsAnswer

      """
      input: NonNull_UnmarkDiscussionCommentAsAnswerInput

   _args: UnmarkDiscussionCommentAsAnswerPayloadArgs


   type: UnmarkDiscussionCommentAsAnswerPayload

class unmarkFileAsViewed(GQLMutation):
   """
   unmarkFileAsViewed - Unmark a pull request file as viewed

   """
   class UnmarkFileAsViewedPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnmarkFileAsViewed

      """
      input: NonNull_UnmarkFileAsViewedInput

   _args: UnmarkFileAsViewedPayloadArgs


   type: UnmarkFileAsViewedPayload

class unmarkIssueAsDuplicate(GQLMutation):
   """
   unmarkIssueAsDuplicate - Unmark an issue as a duplicate of another issue.

   """
   class UnmarkIssueAsDuplicatePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnmarkIssueAsDuplicate

      """
      input: NonNull_UnmarkIssueAsDuplicateInput

   _args: UnmarkIssueAsDuplicatePayloadArgs


   type: UnmarkIssueAsDuplicatePayload

class unminimizeComment(GQLMutation):
   """
   unminimizeComment - Unminimizes a comment on an Issue, Commit, Pull Request, or Gist

   """
   class UnminimizeCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnminimizeComment

      """
      input: NonNull_UnminimizeCommentInput

   _args: UnminimizeCommentPayloadArgs


   type: UnminimizeCommentPayload

class unpinIssue(GQLMutation):
   """
   unpinIssue - Unpin a pinned issue from a repository

   """
   class UnpinIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnpinIssue

      """
      input: NonNull_UnpinIssueInput

   _args: UnpinIssuePayloadArgs


   type: UnpinIssuePayload

class unresolveReviewThread(GQLMutation):
   """
   unresolveReviewThread - Marks a review thread as unresolved.

   """
   class UnresolveReviewThreadPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UnresolveReviewThread

      """
      input: NonNull_UnresolveReviewThreadInput

   _args: UnresolveReviewThreadPayloadArgs


   type: UnresolveReviewThreadPayload

class updateBranchProtectionRule(GQLMutation):
   """
   updateBranchProtectionRule - Update a branch protection rule

   """
   class UpdateBranchProtectionRulePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateBranchProtectionRule

      """
      input: NonNull_UpdateBranchProtectionRuleInput

   _args: UpdateBranchProtectionRulePayloadArgs


   type: UpdateBranchProtectionRulePayload

class updateCheckRun(GQLMutation):
   """
   updateCheckRun - Update a check run

   """
   class UpdateCheckRunPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateCheckRun

      """
      input: NonNull_UpdateCheckRunInput

   _args: UpdateCheckRunPayloadArgs


   type: UpdateCheckRunPayload

class updateCheckSuitePreferences(GQLMutation):
   """
   updateCheckSuitePreferences - Modifies the settings of an existing check suite

   """
   class UpdateCheckSuitePreferencesPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateCheckSuitePreferences

      """
      input: NonNull_UpdateCheckSuitePreferencesInput

   _args: UpdateCheckSuitePreferencesPayloadArgs


   type: UpdateCheckSuitePreferencesPayload

class updateDiscussion(GQLMutation):
   """
   updateDiscussion - Update a discussion

   """
   class UpdateDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateDiscussion

      """
      input: NonNull_UpdateDiscussionInput

   _args: UpdateDiscussionPayloadArgs


   type: UpdateDiscussionPayload

class updateDiscussionComment(GQLMutation):
   """
   updateDiscussionComment - Update the contents of a comment on a Discussion

   """
   class UpdateDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateDiscussionComment

      """
      input: NonNull_UpdateDiscussionCommentInput

   _args: UpdateDiscussionCommentPayloadArgs


   type: UpdateDiscussionCommentPayload

class updateEnterpriseAdministratorRole(GQLMutation):
   """
   updateEnterpriseAdministratorRole - Updates the role of an enterprise administrator.

   """
   class UpdateEnterpriseAdministratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseAdministratorRole

      """
      input: NonNull_UpdateEnterpriseAdministratorRoleInput

   _args: UpdateEnterpriseAdministratorRolePayloadArgs


   type: UpdateEnterpriseAdministratorRolePayload

class updateEnterpriseAllowPrivateRepositoryForkingSetting(GQLMutation):
   """
   updateEnterpriseAllowPrivateRepositoryForkingSetting - Sets whether private repository forks are enabled for an enterprise.

   """
   class UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseAllowPrivateRepositoryForkingSetting

      """
      input: NonNull_UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput

   _args: UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayloadArgs


   type: UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload

class updateEnterpriseDefaultRepositoryPermissionSetting(GQLMutation):
   """
   updateEnterpriseDefaultRepositoryPermissionSetting - Sets the base repository permission for organizations in an enterprise.

   """
   class UpdateEnterpriseDefaultRepositoryPermissionSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseDefaultRepositoryPermissionSetting

      """
      input: NonNull_UpdateEnterpriseDefaultRepositoryPermissionSettingInput

   _args: UpdateEnterpriseDefaultRepositoryPermissionSettingPayloadArgs


   type: UpdateEnterpriseDefaultRepositoryPermissionSettingPayload

class updateEnterpriseMembersCanChangeRepositoryVisibilitySetting(GQLMutation):
   """
   updateEnterpriseMembersCanChangeRepositoryVisibilitySetting - Sets whether organization members with admin permissions on a repository can change repository visibility.

   """
   class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseMembersCanChangeRepositoryVisibilitySetting

      """
      input: NonNull_UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput

   _args: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayloadArgs


   type: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload

class updateEnterpriseMembersCanCreateRepositoriesSetting(GQLMutation):
   """
   updateEnterpriseMembersCanCreateRepositoriesSetting - Sets the members can create repositories setting for an enterprise.

   """
   class UpdateEnterpriseMembersCanCreateRepositoriesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseMembersCanCreateRepositoriesSetting

      """
      input: NonNull_UpdateEnterpriseMembersCanCreateRepositoriesSettingInput

   _args: UpdateEnterpriseMembersCanCreateRepositoriesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload

class updateEnterpriseMembersCanDeleteIssuesSetting(GQLMutation):
   """
   updateEnterpriseMembersCanDeleteIssuesSetting - Sets the members can delete issues setting for an enterprise.

   """
   class UpdateEnterpriseMembersCanDeleteIssuesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseMembersCanDeleteIssuesSetting

      """
      input: NonNull_UpdateEnterpriseMembersCanDeleteIssuesSettingInput

   _args: UpdateEnterpriseMembersCanDeleteIssuesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanDeleteIssuesSettingPayload

class updateEnterpriseMembersCanDeleteRepositoriesSetting(GQLMutation):
   """
   updateEnterpriseMembersCanDeleteRepositoriesSetting - Sets the members can delete repositories setting for an enterprise.

   """
   class UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseMembersCanDeleteRepositoriesSetting

      """
      input: NonNull_UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput

   _args: UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload

class updateEnterpriseMembersCanInviteCollaboratorsSetting(GQLMutation):
   """
   updateEnterpriseMembersCanInviteCollaboratorsSetting - Sets whether members can invite collaborators are enabled for an enterprise.

   """
   class UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseMembersCanInviteCollaboratorsSetting

      """
      input: NonNull_UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput

   _args: UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayloadArgs


   type: UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload

class updateEnterpriseMembersCanMakePurchasesSetting(GQLMutation):
   """
   updateEnterpriseMembersCanMakePurchasesSetting - Sets whether or not an organization admin can make purchases.

   """
   class UpdateEnterpriseMembersCanMakePurchasesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseMembersCanMakePurchasesSetting

      """
      input: NonNull_UpdateEnterpriseMembersCanMakePurchasesSettingInput

   _args: UpdateEnterpriseMembersCanMakePurchasesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanMakePurchasesSettingPayload

class updateEnterpriseMembersCanUpdateProtectedBranchesSetting(GQLMutation):
   """
   updateEnterpriseMembersCanUpdateProtectedBranchesSetting - Sets the members can update protected branches setting for an enterprise.

   """
   class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseMembersCanUpdateProtectedBranchesSetting

      """
      input: NonNull_UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput

   _args: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayloadArgs


   type: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload

class updateEnterpriseMembersCanViewDependencyInsightsSetting(GQLMutation):
   """
   updateEnterpriseMembersCanViewDependencyInsightsSetting - Sets the members can view dependency insights for an enterprise.

   """
   class UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseMembersCanViewDependencyInsightsSetting

      """
      input: NonNull_UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput

   _args: UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayloadArgs


   type: UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload

class updateEnterpriseOrganizationProjectsSetting(GQLMutation):
   """
   updateEnterpriseOrganizationProjectsSetting - Sets whether organization projects are enabled for an enterprise.

   """
   class UpdateEnterpriseOrganizationProjectsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseOrganizationProjectsSetting

      """
      input: NonNull_UpdateEnterpriseOrganizationProjectsSettingInput

   _args: UpdateEnterpriseOrganizationProjectsSettingPayloadArgs


   type: UpdateEnterpriseOrganizationProjectsSettingPayload

class updateEnterpriseOwnerOrganizationRole(GQLMutation):
   """
   updateEnterpriseOwnerOrganizationRole - Updates the role of an enterprise owner with an organization.

   """
   class UpdateEnterpriseOwnerOrganizationRolePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseOwnerOrganizationRole

      """
      input: NonNull_UpdateEnterpriseOwnerOrganizationRoleInput

   _args: UpdateEnterpriseOwnerOrganizationRolePayloadArgs


   type: UpdateEnterpriseOwnerOrganizationRolePayload

class updateEnterpriseProfile(GQLMutation):
   """
   updateEnterpriseProfile - Updates an enterprise's profile.

   """
   class UpdateEnterpriseProfilePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseProfile

      """
      input: NonNull_UpdateEnterpriseProfileInput

   _args: UpdateEnterpriseProfilePayloadArgs


   type: UpdateEnterpriseProfilePayload

class updateEnterpriseRepositoryProjectsSetting(GQLMutation):
   """
   updateEnterpriseRepositoryProjectsSetting - Sets whether repository projects are enabled for a enterprise.

   """
   class UpdateEnterpriseRepositoryProjectsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseRepositoryProjectsSetting

      """
      input: NonNull_UpdateEnterpriseRepositoryProjectsSettingInput

   _args: UpdateEnterpriseRepositoryProjectsSettingPayloadArgs


   type: UpdateEnterpriseRepositoryProjectsSettingPayload

class updateEnterpriseTeamDiscussionsSetting(GQLMutation):
   """
   updateEnterpriseTeamDiscussionsSetting - Sets whether team discussions are enabled for an enterprise.

   """
   class UpdateEnterpriseTeamDiscussionsSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseTeamDiscussionsSetting

      """
      input: NonNull_UpdateEnterpriseTeamDiscussionsSettingInput

   _args: UpdateEnterpriseTeamDiscussionsSettingPayloadArgs


   type: UpdateEnterpriseTeamDiscussionsSettingPayload

class updateEnterpriseTwoFactorAuthenticationRequiredSetting(GQLMutation):
   """
   updateEnterpriseTwoFactorAuthenticationRequiredSetting - Sets whether two factor authentication is required for all users in an enterprise.

   """
   class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnterpriseTwoFactorAuthenticationRequiredSetting

      """
      input: NonNull_UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput

   _args: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayloadArgs


   type: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload

class updateEnvironment(GQLMutation):
   """
   updateEnvironment - Updates an environment.

   """
   class UpdateEnvironmentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateEnvironment

      """
      input: NonNull_UpdateEnvironmentInput

   _args: UpdateEnvironmentPayloadArgs


   type: UpdateEnvironmentPayload

class updateIpAllowListEnabledSetting(GQLMutation):
   """
   updateIpAllowListEnabledSetting - Sets whether an IP allow list is enabled on an owner.

   """
   class UpdateIpAllowListEnabledSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateIpAllowListEnabledSetting

      """
      input: NonNull_UpdateIpAllowListEnabledSettingInput

   _args: UpdateIpAllowListEnabledSettingPayloadArgs


   type: UpdateIpAllowListEnabledSettingPayload

class updateIpAllowListEntry(GQLMutation):
   """
   updateIpAllowListEntry - Updates an IP allow list entry.

   """
   class UpdateIpAllowListEntryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateIpAllowListEntry

      """
      input: NonNull_UpdateIpAllowListEntryInput

   _args: UpdateIpAllowListEntryPayloadArgs


   type: UpdateIpAllowListEntryPayload

class updateIpAllowListForInstalledAppsEnabledSetting(GQLMutation):
   """
   updateIpAllowListForInstalledAppsEnabledSetting - Sets whether IP allow list configuration for installed GitHub Apps is enabled on an owner.

   """
   class UpdateIpAllowListForInstalledAppsEnabledSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateIpAllowListForInstalledAppsEnabledSetting

      """
      input: NonNull_UpdateIpAllowListForInstalledAppsEnabledSettingInput

   _args: UpdateIpAllowListForInstalledAppsEnabledSettingPayloadArgs


   type: UpdateIpAllowListForInstalledAppsEnabledSettingPayload

class updateIssue(GQLMutation):
   """
   updateIssue - Updates an Issue.

   """
   class UpdateIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateIssue

      """
      input: NonNull_UpdateIssueInput

   _args: UpdateIssuePayloadArgs


   type: UpdateIssuePayload

class updateIssueComment(GQLMutation):
   """
   updateIssueComment - Updates an IssueComment object.

   """
   class UpdateIssueCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateIssueComment

      """
      input: NonNull_UpdateIssueCommentInput

   _args: UpdateIssueCommentPayloadArgs


   type: UpdateIssueCommentPayload

class updateNotificationRestrictionSetting(GQLMutation):
   """
   updateNotificationRestrictionSetting - Update the setting to restrict notifications to only verified or approved domains available to an owner.

   """
   class UpdateNotificationRestrictionSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateNotificationRestrictionSetting

      """
      input: NonNull_UpdateNotificationRestrictionSettingInput

   _args: UpdateNotificationRestrictionSettingPayloadArgs


   type: UpdateNotificationRestrictionSettingPayload

class updateOrganizationAllowPrivateRepositoryForkingSetting(GQLMutation):
   """
   updateOrganizationAllowPrivateRepositoryForkingSetting - Sets whether private repository forks are enabled for an organization.

   """
   class UpdateOrganizationAllowPrivateRepositoryForkingSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateOrganizationAllowPrivateRepositoryForkingSetting

      """
      input: NonNull_UpdateOrganizationAllowPrivateRepositoryForkingSettingInput

   _args: UpdateOrganizationAllowPrivateRepositoryForkingSettingPayloadArgs


   type: UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload

class updateOrganizationWebCommitSignoffSetting(GQLMutation):
   """
   updateOrganizationWebCommitSignoffSetting - Sets whether contributors are required to sign off on web-based commits for repositories in an organization.

   """
   class UpdateOrganizationWebCommitSignoffSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateOrganizationWebCommitSignoffSetting

      """
      input: NonNull_UpdateOrganizationWebCommitSignoffSettingInput

   _args: UpdateOrganizationWebCommitSignoffSettingPayloadArgs


   type: UpdateOrganizationWebCommitSignoffSettingPayload

class updateProject(GQLMutation):
   """
   updateProject - Updates an existing project.

   """
   class UpdateProjectPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProject

      """
      input: NonNull_UpdateProjectInput

   _args: UpdateProjectPayloadArgs


   type: UpdateProjectPayload

class updateProjectCard(GQLMutation):
   """
   updateProjectCard - Updates an existing project card.

   """
   class UpdateProjectCardPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProjectCard

      """
      input: NonNull_UpdateProjectCardInput

   _args: UpdateProjectCardPayloadArgs


   type: UpdateProjectCardPayload

class updateProjectColumn(GQLMutation):
   """
   updateProjectColumn - Updates an existing project column.

   """
   class UpdateProjectColumnPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProjectColumn

      """
      input: NonNull_UpdateProjectColumnInput

   _args: UpdateProjectColumnPayloadArgs


   type: UpdateProjectColumnPayload

class updateProjectV2(GQLMutation):
   """
   updateProjectV2 - Updates an existing project (beta).

   """
   class UpdateProjectV2PayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProjectV2

      """
      input: NonNull_UpdateProjectV2Input

   _args: UpdateProjectV2PayloadArgs


   type: UpdateProjectV2Payload

class updateProjectV2DraftIssue(GQLMutation):
   """
   updateProjectV2DraftIssue - Updates a draft issue within a Project.

   """
   class UpdateProjectV2DraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProjectV2DraftIssue

      """
      input: NonNull_UpdateProjectV2DraftIssueInput

   _args: UpdateProjectV2DraftIssuePayloadArgs


   type: UpdateProjectV2DraftIssuePayload

class updateProjectV2ItemFieldValue(GQLMutation):
   """
   updateProjectV2ItemFieldValue - This mutation updates the value of a field for an item in a Project. Currently only single-select, text, number, date, and iteration fields are supported.

   """
   class UpdateProjectV2ItemFieldValuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProjectV2ItemFieldValue

      """
      input: NonNull_UpdateProjectV2ItemFieldValueInput

   _args: UpdateProjectV2ItemFieldValuePayloadArgs


   type: UpdateProjectV2ItemFieldValuePayload

class updateProjectV2ItemPosition(GQLMutation):
   """
   updateProjectV2ItemPosition - This mutation updates the position of the item in the project, where the position represents the priority of an item.

   """
   class UpdateProjectV2ItemPositionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProjectV2ItemPosition

      """
      input: NonNull_UpdateProjectV2ItemPositionInput

   _args: UpdateProjectV2ItemPositionPayloadArgs


   type: UpdateProjectV2ItemPositionPayload

class updatePullRequest(GQLMutation):
   """
   updatePullRequest - Update a pull request

   """
   class UpdatePullRequestPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdatePullRequest

      """
      input: NonNull_UpdatePullRequestInput

   _args: UpdatePullRequestPayloadArgs


   type: UpdatePullRequestPayload

class updatePullRequestBranch(GQLMutation):
   """
   updatePullRequestBranch - Merge or Rebase HEAD from upstream branch into pull request branch

   """
   class UpdatePullRequestBranchPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdatePullRequestBranch

      """
      input: NonNull_UpdatePullRequestBranchInput

   _args: UpdatePullRequestBranchPayloadArgs


   type: UpdatePullRequestBranchPayload

class updatePullRequestReview(GQLMutation):
   """
   updatePullRequestReview - Updates the body of a pull request review.

   """
   class UpdatePullRequestReviewPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdatePullRequestReview

      """
      input: NonNull_UpdatePullRequestReviewInput

   _args: UpdatePullRequestReviewPayloadArgs


   type: UpdatePullRequestReviewPayload

class updatePullRequestReviewComment(GQLMutation):
   """
   updatePullRequestReviewComment - Updates a pull request review comment.

   """
   class UpdatePullRequestReviewCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdatePullRequestReviewComment

      """
      input: NonNull_UpdatePullRequestReviewCommentInput

   _args: UpdatePullRequestReviewCommentPayloadArgs


   type: UpdatePullRequestReviewCommentPayload

class updateRef(GQLMutation):
   """
   updateRef - Update a Git Ref.

   """
   class UpdateRefPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateRef

      """
      input: NonNull_UpdateRefInput

   _args: UpdateRefPayloadArgs


   type: UpdateRefPayload

class updateRepository(GQLMutation):
   """
   updateRepository - Update information about a repository.

   """
   class UpdateRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateRepository

      """
      input: NonNull_UpdateRepositoryInput

   _args: UpdateRepositoryPayloadArgs


   type: UpdateRepositoryPayload

class updateRepositoryWebCommitSignoffSetting(GQLMutation):
   """
   updateRepositoryWebCommitSignoffSetting - Sets whether contributors are required to sign off on web-based commits for a repository.

   """
   class UpdateRepositoryWebCommitSignoffSettingPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateRepositoryWebCommitSignoffSetting

      """
      input: NonNull_UpdateRepositoryWebCommitSignoffSettingInput

   _args: UpdateRepositoryWebCommitSignoffSettingPayloadArgs


   type: UpdateRepositoryWebCommitSignoffSettingPayload

class updateSponsorshipPreferences(GQLMutation):
   """
   updateSponsorshipPreferences - Change visibility of your sponsorship and opt in or out of email updates from the maintainer.

   """
   class UpdateSponsorshipPreferencesPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateSponsorshipPreferences

      """
      input: NonNull_UpdateSponsorshipPreferencesInput

   _args: UpdateSponsorshipPreferencesPayloadArgs


   type: UpdateSponsorshipPreferencesPayload

class updateSubscription(GQLMutation):
   """
   updateSubscription - Updates the state for subscribable subjects.

   """
   class UpdateSubscriptionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateSubscription

      """
      input: NonNull_UpdateSubscriptionInput

   _args: UpdateSubscriptionPayloadArgs


   type: UpdateSubscriptionPayload

class updateTeamDiscussion(GQLMutation):
   """
   updateTeamDiscussion - Updates a team discussion.

   """
   class UpdateTeamDiscussionPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateTeamDiscussion

      """
      input: NonNull_UpdateTeamDiscussionInput

   _args: UpdateTeamDiscussionPayloadArgs


   type: UpdateTeamDiscussionPayload

class updateTeamDiscussionComment(GQLMutation):
   """
   updateTeamDiscussionComment - Updates a discussion comment.

   """
   class UpdateTeamDiscussionCommentPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateTeamDiscussionComment

      """
      input: NonNull_UpdateTeamDiscussionCommentInput

   _args: UpdateTeamDiscussionCommentPayloadArgs


   type: UpdateTeamDiscussionCommentPayload

class updateTeamsRepository(GQLMutation):
   """
   updateTeamsRepository - Update team repository.

   """
   class UpdateTeamsRepositoryPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateTeamsRepository

      """
      input: NonNull_UpdateTeamsRepositoryInput

   _args: UpdateTeamsRepositoryPayloadArgs


   type: UpdateTeamsRepositoryPayload

class updateTopics(GQLMutation):
   """
   updateTopics - Replaces the repository's topics with the given topics.

   """
   class UpdateTopicsPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateTopics

      """
      input: NonNull_UpdateTopicsInput

   _args: UpdateTopicsPayloadArgs


   type: UpdateTopicsPayload

class verifyVerifiableDomain(GQLMutation):
   """
   verifyVerifiableDomain - Verify that a verifiable domain has the expected DNS record.

   """
   class VerifyVerifiableDomainPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for VerifyVerifiableDomain

      """
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
