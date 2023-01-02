from pygqlmap import GQLMutation
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *


class abortQueuedMigrations(GQLMutation):
   """
   abortQueuedMigrations - Clear all of a customer's queued migrations

   """
   class AbortQueuedMigrationsPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AbortQueuedMigrations

      """
      input: AbortQueuedMigrationsInput ##NON NULL

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
      input: AcceptEnterpriseAdministratorInvitationInput ##NON NULL

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
      input: AcceptTopicSuggestionInput ##NON NULL

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
      input: AddAssigneesToAssignableInput ##NON NULL

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
      input: AddCommentInput ##NON NULL

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
      input: AddDiscussionCommentInput ##NON NULL

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
      input: AddDiscussionPollVoteInput ##NON NULL

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
      input: AddEnterpriseOrganizationMemberInput ##NON NULL

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
      input: AddEnterpriseSupportEntitlementInput ##NON NULL

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
      input: AddLabelsToLabelableInput ##NON NULL

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
      input: AddProjectCardInput ##NON NULL

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
      input: AddProjectColumnInput ##NON NULL

   _args: AddProjectColumnPayloadArgs


   type: AddProjectColumnPayload

class addProjectDraftIssue(GQLMutation):
   """
   addProjectDraftIssue - Creates a new draft issue and add it to a Project.

   """
   class AddProjectDraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddProjectDraftIssue

      """
      input: AddProjectDraftIssueInput ##NON NULL

   _args: AddProjectDraftIssuePayloadArgs


   type: AddProjectDraftIssuePayload

class addProjectNextItem(GQLMutation):
   """
   addProjectNextItem - Adds an existing item (Issue or PullRequest) to a Project.

   """
   class AddProjectNextItemPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddProjectNextItem

      """
      input: AddProjectNextItemInput ##NON NULL

   _args: AddProjectNextItemPayloadArgs


   type: AddProjectNextItemPayload

class addProjectV2DraftIssue(GQLMutation):
   """
   addProjectV2DraftIssue - Creates a new draft issue and add it to a Project.

   """
   class AddProjectV2DraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AddProjectV2DraftIssue

      """
      input: AddProjectV2DraftIssueInput ##NON NULL

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
      input: AddProjectV2ItemByIdInput ##NON NULL

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
      input: AddPullRequestReviewInput ##NON NULL

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
      input: AddPullRequestReviewCommentInput ##NON NULL

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
      input: AddPullRequestReviewThreadInput ##NON NULL

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
      input: AddReactionInput ##NON NULL

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
      input: AddStarInput ##NON NULL

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
      input: AddUpvoteInput ##NON NULL

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
      input: AddVerifiableDomainInput ##NON NULL

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
      input: ApproveDeploymentsInput ##NON NULL

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
      input: ApproveVerifiableDomainInput ##NON NULL

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
      input: ArchiveProjectV2ItemInput ##NON NULL

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
      input: ArchiveRepositoryInput ##NON NULL

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
      input: CancelEnterpriseAdminInvitationInput ##NON NULL

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
      input: CancelSponsorshipInput ##NON NULL

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
      input: ChangeUserStatusInput ##NON NULL

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
      input: ClearLabelsFromLabelableInput ##NON NULL

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
      input: ClearProjectV2ItemFieldValueInput ##NON NULL

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
      input: CloneProjectInput ##NON NULL

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
      input: CloneTemplateRepositoryInput ##NON NULL

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
      input: CloseIssueInput ##NON NULL

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
      input: ClosePullRequestInput ##NON NULL

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
      input: ConvertProjectCardNoteToIssueInput ##NON NULL

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
      input: ConvertPullRequestToDraftInput ##NON NULL

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
      input: CreateAttributionInvitationInput ##NON NULL

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
      input: CreateBranchProtectionRuleInput ##NON NULL

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
      input: CreateCheckRunInput ##NON NULL

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
      input: CreateCheckSuiteInput ##NON NULL

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
      input: CreateCommitOnBranchInput ##NON NULL

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
      input: CreateDiscussionInput ##NON NULL

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
      input: CreateEnterpriseOrganizationInput ##NON NULL

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
      input: CreateEnvironmentInput ##NON NULL

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
      input: CreateIpAllowListEntryInput ##NON NULL

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
      input: CreateIssueInput ##NON NULL

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
      input: CreateLinkedBranchInput ##NON NULL

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
      input: CreateMigrationSourceInput ##NON NULL

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
      input: CreateProjectInput ##NON NULL

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
      input: CreateProjectV2Input ##NON NULL

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
      input: CreatePullRequestInput ##NON NULL

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
      input: CreateRefInput ##NON NULL

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
      input: CreateRepositoryInput ##NON NULL

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
      input: CreateSponsorsListingInput ##NON NULL

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
      input: CreateSponsorsTierInput ##NON NULL

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
      input: CreateSponsorshipInput ##NON NULL

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
      input: CreateTeamDiscussionInput ##NON NULL

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
      input: CreateTeamDiscussionCommentInput ##NON NULL

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
      input: DeclineTopicSuggestionInput ##NON NULL

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
      input: DeleteBranchProtectionRuleInput ##NON NULL

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
      input: DeleteDeploymentInput ##NON NULL

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
      input: DeleteDiscussionInput ##NON NULL

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
      input: DeleteDiscussionCommentInput ##NON NULL

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
      input: DeleteEnvironmentInput ##NON NULL

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
      input: DeleteIpAllowListEntryInput ##NON NULL

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
      input: DeleteIssueInput ##NON NULL

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
      input: DeleteIssueCommentInput ##NON NULL

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
      input: DeleteLinkedBranchInput ##NON NULL

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
      input: DeleteProjectInput ##NON NULL

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
      input: DeleteProjectCardInput ##NON NULL

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
      input: DeleteProjectColumnInput ##NON NULL

   _args: DeleteProjectColumnPayloadArgs


   type: DeleteProjectColumnPayload

class deleteProjectNextItem(GQLMutation):
   """
   deleteProjectNextItem - Deletes an item from a Project.

   """
   class DeleteProjectNextItemPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteProjectNextItem

      """
      input: DeleteProjectNextItemInput ##NON NULL

   _args: DeleteProjectNextItemPayloadArgs


   type: DeleteProjectNextItemPayload

class deleteProjectV2Item(GQLMutation):
   """
   deleteProjectV2Item - Deletes an item from a Project.

   """
   class DeleteProjectV2ItemPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for DeleteProjectV2Item

      """
      input: DeleteProjectV2ItemInput ##NON NULL

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
      input: DeletePullRequestReviewInput ##NON NULL

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
      input: DeletePullRequestReviewCommentInput ##NON NULL

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
      input: DeleteRefInput ##NON NULL

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
      input: DeleteTeamDiscussionInput ##NON NULL

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
      input: DeleteTeamDiscussionCommentInput ##NON NULL

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
      input: DeleteVerifiableDomainInput ##NON NULL

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
      input: DisablePullRequestAutoMergeInput ##NON NULL

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
      input: DismissPullRequestReviewInput ##NON NULL

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
      input: DismissRepositoryVulnerabilityAlertInput ##NON NULL

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
      input: EnablePullRequestAutoMergeInput ##NON NULL

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
      input: FollowOrganizationInput ##NON NULL

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
      input: FollowUserInput ##NON NULL

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
      input: GrantEnterpriseOrganizationsMigratorRoleInput ##NON NULL

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
      input: GrantMigratorRoleInput ##NON NULL

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
      input: InviteEnterpriseAdminInput ##NON NULL

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
      input: LinkProjectV2ToRepositoryInput ##NON NULL

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
      input: LinkProjectV2ToTeamInput ##NON NULL

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
      input: LinkRepositoryToProjectInput ##NON NULL

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
      input: LockLockableInput ##NON NULL

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
      input: MarkDiscussionCommentAsAnswerInput ##NON NULL

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
      input: MarkFileAsViewedInput ##NON NULL

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
      input: MarkPullRequestReadyForReviewInput ##NON NULL

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
      input: MergeBranchInput ##NON NULL

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
      input: MergePullRequestInput ##NON NULL

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
      input: MinimizeCommentInput ##NON NULL

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
      input: MoveProjectCardInput ##NON NULL

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
      input: MoveProjectColumnInput ##NON NULL

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
      input: PinIssueInput ##NON NULL

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
      input: PublishSponsorsTierInput ##NON NULL

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
      input: RegenerateEnterpriseIdentityProviderRecoveryCodesInput ##NON NULL

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
      input: RegenerateVerifiableDomainTokenInput ##NON NULL

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
      input: RejectDeploymentsInput ##NON NULL

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
      input: RemoveAssigneesFromAssignableInput ##NON NULL

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
      input: RemoveEnterpriseAdminInput ##NON NULL

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
      input: RemoveEnterpriseIdentityProviderInput ##NON NULL

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
      input: RemoveEnterpriseOrganizationInput ##NON NULL

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
      input: RemoveEnterpriseSupportEntitlementInput ##NON NULL

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
      input: RemoveLabelsFromLabelableInput ##NON NULL

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
      input: RemoveOutsideCollaboratorInput ##NON NULL

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
      input: RemoveReactionInput ##NON NULL

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
      input: RemoveStarInput ##NON NULL

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
      input: RemoveUpvoteInput ##NON NULL

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
      input: ReopenIssueInput ##NON NULL

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
      input: ReopenPullRequestInput ##NON NULL

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
      input: RequestReviewsInput ##NON NULL

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
      input: RerequestCheckSuiteInput ##NON NULL

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
      input: ResolveReviewThreadInput ##NON NULL

   _args: ResolveReviewThreadPayloadArgs


   type: ResolveReviewThreadPayload

class revokeEnterpriseOrganizationsMigratorRole(GQLMutation):
   """
   revokeEnterpriseOrganizationsMigratorRole - Revoke the migrator role to a user for all organizations under an enterprise account.

   """
   class RevokeEnterpriseOrganizationsMigratorRolePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for RevokeEnterpriseOrganizationsMigratorRole

      """
      input: RevokeEnterpriseOrganizationsMigratorRoleInput ##NON NULL

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
      input: RevokeMigratorRoleInput ##NON NULL

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
      input: SetEnterpriseIdentityProviderInput ##NON NULL

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
      input: SetOrganizationInteractionLimitInput ##NON NULL

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
      input: SetRepositoryInteractionLimitInput ##NON NULL

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
      input: SetUserInteractionLimitInput ##NON NULL

   _args: SetUserInteractionLimitPayloadArgs


   type: SetUserInteractionLimitPayload

class startRepositoryMigration(GQLMutation):
   """
   startRepositoryMigration - Starts a GitHub Enterprise Importer (GEI) repository migration.

   """
   class StartRepositoryMigrationPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for StartRepositoryMigration

      """
      input: StartRepositoryMigrationInput ##NON NULL

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
      input: SubmitPullRequestReviewInput ##NON NULL

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
      input: TransferEnterpriseOrganizationInput ##NON NULL

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
      input: TransferIssueInput ##NON NULL

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
      input: UnarchiveProjectV2ItemInput ##NON NULL

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
      input: UnarchiveRepositoryInput ##NON NULL

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
      input: UnfollowOrganizationInput ##NON NULL

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
      input: UnfollowUserInput ##NON NULL

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
      input: UnlinkProjectV2FromRepositoryInput ##NON NULL

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
      input: UnlinkProjectV2FromTeamInput ##NON NULL

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
      input: UnlinkRepositoryFromProjectInput ##NON NULL

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
      input: UnlockLockableInput ##NON NULL

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
      input: UnmarkDiscussionCommentAsAnswerInput ##NON NULL

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
      input: UnmarkFileAsViewedInput ##NON NULL

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
      input: UnmarkIssueAsDuplicateInput ##NON NULL

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
      input: UnminimizeCommentInput ##NON NULL

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
      input: UnpinIssueInput ##NON NULL

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
      input: UnresolveReviewThreadInput ##NON NULL

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
      input: UpdateBranchProtectionRuleInput ##NON NULL

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
      input: UpdateCheckRunInput ##NON NULL

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
      input: UpdateCheckSuitePreferencesInput ##NON NULL

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
      input: UpdateDiscussionInput ##NON NULL

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
      input: UpdateDiscussionCommentInput ##NON NULL

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
      input: UpdateEnterpriseAdministratorRoleInput ##NON NULL

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
      input: UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput ##NON NULL

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
      input: UpdateEnterpriseDefaultRepositoryPermissionSettingInput ##NON NULL

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
      input: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput ##NON NULL

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
      input: UpdateEnterpriseMembersCanCreateRepositoriesSettingInput ##NON NULL

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
      input: UpdateEnterpriseMembersCanDeleteIssuesSettingInput ##NON NULL

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
      input: UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput ##NON NULL

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
      input: UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput ##NON NULL

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
      input: UpdateEnterpriseMembersCanMakePurchasesSettingInput ##NON NULL

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
      input: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput ##NON NULL

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
      input: UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput ##NON NULL

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
      input: UpdateEnterpriseOrganizationProjectsSettingInput ##NON NULL

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
      input: UpdateEnterpriseOwnerOrganizationRoleInput ##NON NULL

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
      input: UpdateEnterpriseProfileInput ##NON NULL

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
      input: UpdateEnterpriseRepositoryProjectsSettingInput ##NON NULL

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
      input: UpdateEnterpriseTeamDiscussionsSettingInput ##NON NULL

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
      input: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput ##NON NULL

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
      input: UpdateEnvironmentInput ##NON NULL

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
      input: UpdateIpAllowListEnabledSettingInput ##NON NULL

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
      input: UpdateIpAllowListEntryInput ##NON NULL

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
      input: UpdateIpAllowListForInstalledAppsEnabledSettingInput ##NON NULL

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
      input: UpdateIssueInput ##NON NULL

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
      input: UpdateIssueCommentInput ##NON NULL

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
      input: UpdateNotificationRestrictionSettingInput ##NON NULL

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
      input: UpdateOrganizationAllowPrivateRepositoryForkingSettingInput ##NON NULL

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
      input: UpdateOrganizationWebCommitSignoffSettingInput ##NON NULL

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
      input: UpdateProjectInput ##NON NULL

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
      input: UpdateProjectCardInput ##NON NULL

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
      input: UpdateProjectColumnInput ##NON NULL

   _args: UpdateProjectColumnPayloadArgs


   type: UpdateProjectColumnPayload

class updateProjectDraftIssue(GQLMutation):
   """
   updateProjectDraftIssue - Updates a draft issue within a Project.

   """
   class UpdateProjectDraftIssuePayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProjectDraftIssue

      """
      input: UpdateProjectDraftIssueInput ##NON NULL

   _args: UpdateProjectDraftIssuePayloadArgs


   type: UpdateProjectDraftIssuePayload

class updateProjectNext(GQLMutation):
   """
   updateProjectNext - Updates an existing project (beta).

   """
   class UpdateProjectNextPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProjectNext

      """
      input: UpdateProjectNextInput ##NON NULL

   _args: UpdateProjectNextPayloadArgs


   type: UpdateProjectNextPayload

class updateProjectNextItemField(GQLMutation):
   """
   updateProjectNextItemField - Updates a field of an item from a Project.

   """
   class UpdateProjectNextItemFieldPayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProjectNextItemField

      """
      input: UpdateProjectNextItemFieldInput ##NON NULL

   _args: UpdateProjectNextItemFieldPayloadArgs


   type: UpdateProjectNextItemFieldPayload

class updateProjectV2(GQLMutation):
   """
   updateProjectV2 - Updates an existing project (beta).

   """
   class UpdateProjectV2PayloadArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for UpdateProjectV2

      """
      input: UpdateProjectV2Input ##NON NULL

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
      input: UpdateProjectV2DraftIssueInput ##NON NULL

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
      input: UpdateProjectV2ItemFieldValueInput ##NON NULL

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
      input: UpdateProjectV2ItemPositionInput ##NON NULL

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
      input: UpdatePullRequestInput ##NON NULL

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
      input: UpdatePullRequestBranchInput ##NON NULL

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
      input: UpdatePullRequestReviewInput ##NON NULL

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
      input: UpdatePullRequestReviewCommentInput ##NON NULL

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
      input: UpdateRefInput ##NON NULL

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
      input: UpdateRepositoryInput ##NON NULL

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
      input: UpdateRepositoryWebCommitSignoffSettingInput ##NON NULL

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
      input: UpdateSponsorshipPreferencesInput ##NON NULL

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
      input: UpdateSubscriptionInput ##NON NULL

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
      input: UpdateTeamDiscussionInput ##NON NULL

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
      input: UpdateTeamDiscussionCommentInput ##NON NULL

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
      input: UpdateTeamsRepositoryInput ##NON NULL

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
      input: UpdateTopicsInput ##NON NULL

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
