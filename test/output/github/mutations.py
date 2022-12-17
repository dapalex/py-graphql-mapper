from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *


class abortQueuedMigrations(GQLObject):
   """
   abortQueuedMigrations - Clear all of a customer's queued migrations

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AbortQueuedMigrations

      """
      input: AbortQueuedMigrationsInput ##NON NULL

   _args: Args


   type: AbortQueuedMigrationsPayload

class acceptEnterpriseAdministratorInvitation(GQLObject):
   """
   acceptEnterpriseAdministratorInvitation - Accepts a pending invitation for a user to become an administrator of an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AcceptEnterpriseAdministratorInvitation

      """
      input: AcceptEnterpriseAdministratorInvitationInput ##NON NULL

   _args: Args


   type: AcceptEnterpriseAdministratorInvitationPayload

class acceptTopicSuggestion(GQLObject):
   """
   acceptTopicSuggestion - Applies a suggested topic to the repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AcceptTopicSuggestion

      """
      input: AcceptTopicSuggestionInput ##NON NULL

   _args: Args


   type: AcceptTopicSuggestionPayload

class addAssigneesToAssignable(GQLObject):
   """
   addAssigneesToAssignable - Adds assignees to an assignable object.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddAssigneesToAssignable

      """
      input: AddAssigneesToAssignableInput ##NON NULL

   _args: Args


   type: AddAssigneesToAssignablePayload

class addComment(GQLObject):
   """
   addComment - Adds a comment to an Issue or Pull Request.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddComment

      """
      input: AddCommentInput ##NON NULL

   _args: Args


   type: AddCommentPayload

class addDiscussionComment(GQLObject):
   """
   addDiscussionComment - Adds a comment to a Discussion, possibly as a reply to another comment.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddDiscussionComment

      """
      input: AddDiscussionCommentInput ##NON NULL

   _args: Args


   type: AddDiscussionCommentPayload

class addDiscussionPollVote(GQLObject):
   """
   addDiscussionPollVote - Vote for an option in a discussion poll.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddDiscussionPollVote

      """
      input: AddDiscussionPollVoteInput ##NON NULL

   _args: Args


   type: AddDiscussionPollVotePayload

class addEnterpriseOrganizationMember(GQLObject):
   """
   addEnterpriseOrganizationMember - Adds enterprise members to an organization within the enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddEnterpriseOrganizationMember

      """
      input: AddEnterpriseOrganizationMemberInput ##NON NULL

   _args: Args


   type: AddEnterpriseOrganizationMemberPayload

class addEnterpriseSupportEntitlement(GQLObject):
   """
   addEnterpriseSupportEntitlement - Adds a support entitlement to an enterprise member.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddEnterpriseSupportEntitlement

      """
      input: AddEnterpriseSupportEntitlementInput ##NON NULL

   _args: Args


   type: AddEnterpriseSupportEntitlementPayload

class addLabelsToLabelable(GQLObject):
   """
   addLabelsToLabelable - Adds labels to a labelable object.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddLabelsToLabelable

      """
      input: AddLabelsToLabelableInput ##NON NULL

   _args: Args


   type: AddLabelsToLabelablePayload

class addProjectCard(GQLObject):
   """
   addProjectCard - Adds a card to a ProjectColumn. Either `contentId` or `note` must be provided but **not** both.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddProjectCard

      """
      input: AddProjectCardInput ##NON NULL

   _args: Args


   type: AddProjectCardPayload

class addProjectColumn(GQLObject):
   """
   addProjectColumn - Adds a column to a Project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddProjectColumn

      """
      input: AddProjectColumnInput ##NON NULL

   _args: Args


   type: AddProjectColumnPayload

class addProjectDraftIssue(GQLObject):
   """
   addProjectDraftIssue - Creates a new draft issue and add it to a Project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddProjectDraftIssue

      """
      input: AddProjectDraftIssueInput ##NON NULL

   _args: Args


   type: AddProjectDraftIssuePayload

class addProjectNextItem(GQLObject):
   """
   addProjectNextItem - Adds an existing item (Issue or PullRequest) to a Project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddProjectNextItem

      """
      input: AddProjectNextItemInput ##NON NULL

   _args: Args


   type: AddProjectNextItemPayload

class addProjectV2DraftIssue(GQLObject):
   """
   addProjectV2DraftIssue - Creates a new draft issue and add it to a Project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddProjectV2DraftIssue

      """
      input: AddProjectV2DraftIssueInput ##NON NULL

   _args: Args


   type: AddProjectV2DraftIssuePayload

class addProjectV2ItemById(GQLObject):
   """
   addProjectV2ItemById - Links an existing content instance to a Project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddProjectV2ItemById

      """
      input: AddProjectV2ItemByIdInput ##NON NULL

   _args: Args


   type: AddProjectV2ItemByIdPayload

class addPullRequestReview(GQLObject):
   """
   addPullRequestReview - Adds a review to a Pull Request.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddPullRequestReview

      """
      input: AddPullRequestReviewInput ##NON NULL

   _args: Args


   type: AddPullRequestReviewPayload

class addPullRequestReviewComment(GQLObject):
   """
   addPullRequestReviewComment - Adds a comment to a review.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddPullRequestReviewComment

      """
      input: AddPullRequestReviewCommentInput ##NON NULL

   _args: Args


   type: AddPullRequestReviewCommentPayload

class addPullRequestReviewThread(GQLObject):
   """
   addPullRequestReviewThread - Adds a new thread to a pending Pull Request Review.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddPullRequestReviewThread

      """
      input: AddPullRequestReviewThreadInput ##NON NULL

   _args: Args


   type: AddPullRequestReviewThreadPayload

class addReaction(GQLObject):
   """
   addReaction - Adds a reaction to a subject.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddReaction

      """
      input: AddReactionInput ##NON NULL

   _args: Args


   type: AddReactionPayload

class addStar(GQLObject):
   """
   addStar - Adds a star to a Starrable.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddStar

      """
      input: AddStarInput ##NON NULL

   _args: Args


   type: AddStarPayload

class addUpvote(GQLObject):
   """
   addUpvote - Add an upvote to a discussion or discussion comment.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddUpvote

      """
      input: AddUpvoteInput ##NON NULL

   _args: Args


   type: AddUpvotePayload

class addVerifiableDomain(GQLObject):
   """
   addVerifiableDomain - Adds a verifiable domain to an owning account.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for AddVerifiableDomain

      """
      input: AddVerifiableDomainInput ##NON NULL

   _args: Args


   type: AddVerifiableDomainPayload

class approveDeployments(GQLObject):
   """
   approveDeployments - Approve all pending deployments under one or more environments

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ApproveDeployments

      """
      input: ApproveDeploymentsInput ##NON NULL

   _args: Args


   type: ApproveDeploymentsPayload

class approveVerifiableDomain(GQLObject):
   """
   approveVerifiableDomain - Approve a verifiable domain for notification delivery.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ApproveVerifiableDomain

      """
      input: ApproveVerifiableDomainInput ##NON NULL

   _args: Args


   type: ApproveVerifiableDomainPayload

class archiveProjectV2Item(GQLObject):
   """
   archiveProjectV2Item - Archives a ProjectV2Item

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ArchiveProjectV2Item

      """
      input: ArchiveProjectV2ItemInput ##NON NULL

   _args: Args


   type: ArchiveProjectV2ItemPayload

class archiveRepository(GQLObject):
   """
   archiveRepository - Marks a repository as archived.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ArchiveRepository

      """
      input: ArchiveRepositoryInput ##NON NULL

   _args: Args


   type: ArchiveRepositoryPayload

class cancelEnterpriseAdminInvitation(GQLObject):
   """
   cancelEnterpriseAdminInvitation - Cancels a pending invitation for an administrator to join an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CancelEnterpriseAdminInvitation

      """
      input: CancelEnterpriseAdminInvitationInput ##NON NULL

   _args: Args


   type: CancelEnterpriseAdminInvitationPayload

class cancelSponsorship(GQLObject):
   """
   cancelSponsorship - Cancel an active sponsorship.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CancelSponsorship

      """
      input: CancelSponsorshipInput ##NON NULL

   _args: Args


   type: CancelSponsorshipPayload

class changeUserStatus(GQLObject):
   """
   changeUserStatus - Update your status on GitHub.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ChangeUserStatus

      """
      input: ChangeUserStatusInput ##NON NULL

   _args: Args


   type: ChangeUserStatusPayload

class clearLabelsFromLabelable(GQLObject):
   """
   clearLabelsFromLabelable - Clears all labels from a labelable object.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ClearLabelsFromLabelable

      """
      input: ClearLabelsFromLabelableInput ##NON NULL

   _args: Args


   type: ClearLabelsFromLabelablePayload

class clearProjectV2ItemFieldValue(GQLObject):
   """
   clearProjectV2ItemFieldValue - This mutation clears the value of a field for an item in a Project. Currently only text, number, date, assignees, labels, single-select, iteration and milestone fields are supported.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ClearProjectV2ItemFieldValue

      """
      input: ClearProjectV2ItemFieldValueInput ##NON NULL

   _args: Args


   type: ClearProjectV2ItemFieldValuePayload

class cloneProject(GQLObject):
   """
   cloneProject - Creates a new project by cloning configuration from an existing project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CloneProject

      """
      input: CloneProjectInput ##NON NULL

   _args: Args


   type: CloneProjectPayload

class cloneTemplateRepository(GQLObject):
   """
   cloneTemplateRepository - Create a new repository with the same files and directory structure as a template repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CloneTemplateRepository

      """
      input: CloneTemplateRepositoryInput ##NON NULL

   _args: Args


   type: CloneTemplateRepositoryPayload

class closeIssue(GQLObject):
   """
   closeIssue - Close an issue.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CloseIssue

      """
      input: CloseIssueInput ##NON NULL

   _args: Args


   type: CloseIssuePayload

class closePullRequest(GQLObject):
   """
   closePullRequest - Close a pull request.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ClosePullRequest

      """
      input: ClosePullRequestInput ##NON NULL

   _args: Args


   type: ClosePullRequestPayload

class convertProjectCardNoteToIssue(GQLObject):
   """
   convertProjectCardNoteToIssue - Convert a project note card to one associated with a newly created issue.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ConvertProjectCardNoteToIssue

      """
      input: ConvertProjectCardNoteToIssueInput ##NON NULL

   _args: Args


   type: ConvertProjectCardNoteToIssuePayload

class convertPullRequestToDraft(GQLObject):
   """
   convertPullRequestToDraft - Converts a pull request to draft

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ConvertPullRequestToDraft

      """
      input: ConvertPullRequestToDraftInput ##NON NULL

   _args: Args


   type: ConvertPullRequestToDraftPayload

class createAttributionInvitation(GQLObject):
   """
   createAttributionInvitation - Invites a user to claim reattributable data

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateAttributionInvitation

      """
      input: CreateAttributionInvitationInput ##NON NULL

   _args: Args


   type: CreateAttributionInvitationPayload

class createBranchProtectionRule(GQLObject):
   """
   createBranchProtectionRule - Create a new branch protection rule

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateBranchProtectionRule

      """
      input: CreateBranchProtectionRuleInput ##NON NULL

   _args: Args


   type: CreateBranchProtectionRulePayload

class createCheckRun(GQLObject):
   """
   createCheckRun - Create a check run.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateCheckRun

      """
      input: CreateCheckRunInput ##NON NULL

   _args: Args


   type: CreateCheckRunPayload

class createCheckSuite(GQLObject):
   """
   createCheckSuite - Create a check suite

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateCheckSuite

      """
      input: CreateCheckSuiteInput ##NON NULL

   _args: Args


   type: CreateCheckSuitePayload

class createCommitOnBranch(GQLObject):
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
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateCommitOnBranch

      """
      input: CreateCommitOnBranchInput ##NON NULL

   _args: Args


   type: CreateCommitOnBranchPayload

class createDiscussion(GQLObject):
   """
   createDiscussion - Create a discussion.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateDiscussion

      """
      input: CreateDiscussionInput ##NON NULL

   _args: Args


   type: CreateDiscussionPayload

class createEnterpriseOrganization(GQLObject):
   """
   createEnterpriseOrganization - Creates an organization as part of an enterprise account.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateEnterpriseOrganization

      """
      input: CreateEnterpriseOrganizationInput ##NON NULL

   _args: Args


   type: CreateEnterpriseOrganizationPayload

class createEnvironment(GQLObject):
   """
   createEnvironment - Creates an environment or simply returns it if already exists.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateEnvironment

      """
      input: CreateEnvironmentInput ##NON NULL

   _args: Args


   type: CreateEnvironmentPayload

class createIpAllowListEntry(GQLObject):
   """
   createIpAllowListEntry - Creates a new IP allow list entry.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateIpAllowListEntry

      """
      input: CreateIpAllowListEntryInput ##NON NULL

   _args: Args


   type: CreateIpAllowListEntryPayload

class createIssue(GQLObject):
   """
   createIssue - Creates a new issue.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateIssue

      """
      input: CreateIssueInput ##NON NULL

   _args: Args


   type: CreateIssuePayload

class createLinkedBranch(GQLObject):
   """
   createLinkedBranch - Create a branch linked to an issue.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateLinkedBranch

      """
      input: CreateLinkedBranchInput ##NON NULL

   _args: Args


   type: CreateLinkedBranchPayload

class createMigrationSource(GQLObject):
   """
   createMigrationSource - Creates a GitHub Enterprise Importer (GEI) migration source.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateMigrationSource

      """
      input: CreateMigrationSourceInput ##NON NULL

   _args: Args


   type: CreateMigrationSourcePayload

class createProject(GQLObject):
   """
   createProject - Creates a new project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateProject

      """
      input: CreateProjectInput ##NON NULL

   _args: Args


   type: CreateProjectPayload

class createProjectV2(GQLObject):
   """
   createProjectV2 - Creates a new project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateProjectV2

      """
      input: CreateProjectV2Input ##NON NULL

   _args: Args


   type: CreateProjectV2Payload

class createPullRequest(GQLObject):
   """
   createPullRequest - Create a new pull request

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreatePullRequest

      """
      input: CreatePullRequestInput ##NON NULL

   _args: Args


   type: CreatePullRequestPayload

class createRef(GQLObject):
   """
   createRef - Create a new Git Ref.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateRef

      """
      input: CreateRefInput ##NON NULL

   _args: Args


   type: CreateRefPayload

class createRepository(GQLObject):
   """
   createRepository - Create a new repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateRepository

      """
      input: CreateRepositoryInput ##NON NULL

   _args: Args


   type: CreateRepositoryPayload

class createSponsorsListing(GQLObject):
   """
   createSponsorsListing - Create a GitHub Sponsors profile to allow others to sponsor you or your organization.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateSponsorsListing

      """
      input: CreateSponsorsListingInput ##NON NULL

   _args: Args


   type: CreateSponsorsListingPayload

class createSponsorsTier(GQLObject):
   """
   createSponsorsTier - Create a new payment tier for your GitHub Sponsors profile.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateSponsorsTier

      """
      input: CreateSponsorsTierInput ##NON NULL

   _args: Args


   type: CreateSponsorsTierPayload

class createSponsorship(GQLObject):
   """
   createSponsorship - Start a new sponsorship of a maintainer in GitHub Sponsors, or reactivate a past sponsorship.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateSponsorship

      """
      input: CreateSponsorshipInput ##NON NULL

   _args: Args


   type: CreateSponsorshipPayload

class createTeamDiscussion(GQLObject):
   """
   createTeamDiscussion - Creates a new team discussion.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateTeamDiscussion

      """
      input: CreateTeamDiscussionInput ##NON NULL

   _args: Args


   type: CreateTeamDiscussionPayload

class createTeamDiscussionComment(GQLObject):
   """
   createTeamDiscussionComment - Creates a new team discussion comment.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for CreateTeamDiscussionComment

      """
      input: CreateTeamDiscussionCommentInput ##NON NULL

   _args: Args


   type: CreateTeamDiscussionCommentPayload

class declineTopicSuggestion(GQLObject):
   """
   declineTopicSuggestion - Rejects a suggested topic for the repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeclineTopicSuggestion

      """
      input: DeclineTopicSuggestionInput ##NON NULL

   _args: Args


   type: DeclineTopicSuggestionPayload

class deleteBranchProtectionRule(GQLObject):
   """
   deleteBranchProtectionRule - Delete a branch protection rule

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteBranchProtectionRule

      """
      input: DeleteBranchProtectionRuleInput ##NON NULL

   _args: Args


   type: DeleteBranchProtectionRulePayload

class deleteDeployment(GQLObject):
   """
   deleteDeployment - Deletes a deployment.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteDeployment

      """
      input: DeleteDeploymentInput ##NON NULL

   _args: Args


   type: DeleteDeploymentPayload

class deleteDiscussion(GQLObject):
   """
   deleteDiscussion - Delete a discussion and all of its replies.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteDiscussion

      """
      input: DeleteDiscussionInput ##NON NULL

   _args: Args


   type: DeleteDiscussionPayload

class deleteDiscussionComment(GQLObject):
   """
   deleteDiscussionComment - Delete a discussion comment. If it has replies, wipe it instead.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteDiscussionComment

      """
      input: DeleteDiscussionCommentInput ##NON NULL

   _args: Args


   type: DeleteDiscussionCommentPayload

class deleteEnvironment(GQLObject):
   """
   deleteEnvironment - Deletes an environment

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteEnvironment

      """
      input: DeleteEnvironmentInput ##NON NULL

   _args: Args


   type: DeleteEnvironmentPayload

class deleteIpAllowListEntry(GQLObject):
   """
   deleteIpAllowListEntry - Deletes an IP allow list entry.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteIpAllowListEntry

      """
      input: DeleteIpAllowListEntryInput ##NON NULL

   _args: Args


   type: DeleteIpAllowListEntryPayload

class deleteIssue(GQLObject):
   """
   deleteIssue - Deletes an Issue object.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteIssue

      """
      input: DeleteIssueInput ##NON NULL

   _args: Args


   type: DeleteIssuePayload

class deleteIssueComment(GQLObject):
   """
   deleteIssueComment - Deletes an IssueComment object.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteIssueComment

      """
      input: DeleteIssueCommentInput ##NON NULL

   _args: Args


   type: DeleteIssueCommentPayload

class deleteLinkedBranch(GQLObject):
   """
   deleteLinkedBranch - Unlink a branch from an issue.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteLinkedBranch

      """
      input: DeleteLinkedBranchInput ##NON NULL

   _args: Args


   type: DeleteLinkedBranchPayload

class deleteProject(GQLObject):
   """
   deleteProject - Deletes a project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteProject

      """
      input: DeleteProjectInput ##NON NULL

   _args: Args


   type: DeleteProjectPayload

class deleteProjectCard(GQLObject):
   """
   deleteProjectCard - Deletes a project card.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteProjectCard

      """
      input: DeleteProjectCardInput ##NON NULL

   _args: Args


   type: DeleteProjectCardPayload

class deleteProjectColumn(GQLObject):
   """
   deleteProjectColumn - Deletes a project column.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteProjectColumn

      """
      input: DeleteProjectColumnInput ##NON NULL

   _args: Args


   type: DeleteProjectColumnPayload

class deleteProjectNextItem(GQLObject):
   """
   deleteProjectNextItem - Deletes an item from a Project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteProjectNextItem

      """
      input: DeleteProjectNextItemInput ##NON NULL

   _args: Args


   type: DeleteProjectNextItemPayload

class deleteProjectV2Item(GQLObject):
   """
   deleteProjectV2Item - Deletes an item from a Project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteProjectV2Item

      """
      input: DeleteProjectV2ItemInput ##NON NULL

   _args: Args


   type: DeleteProjectV2ItemPayload

class deletePullRequestReview(GQLObject):
   """
   deletePullRequestReview - Deletes a pull request review.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeletePullRequestReview

      """
      input: DeletePullRequestReviewInput ##NON NULL

   _args: Args


   type: DeletePullRequestReviewPayload

class deletePullRequestReviewComment(GQLObject):
   """
   deletePullRequestReviewComment - Deletes a pull request review comment.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeletePullRequestReviewComment

      """
      input: DeletePullRequestReviewCommentInput ##NON NULL

   _args: Args


   type: DeletePullRequestReviewCommentPayload

class deleteRef(GQLObject):
   """
   deleteRef - Delete a Git Ref.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteRef

      """
      input: DeleteRefInput ##NON NULL

   _args: Args


   type: DeleteRefPayload

class deleteTeamDiscussion(GQLObject):
   """
   deleteTeamDiscussion - Deletes a team discussion.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteTeamDiscussion

      """
      input: DeleteTeamDiscussionInput ##NON NULL

   _args: Args


   type: DeleteTeamDiscussionPayload

class deleteTeamDiscussionComment(GQLObject):
   """
   deleteTeamDiscussionComment - Deletes a team discussion comment.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteTeamDiscussionComment

      """
      input: DeleteTeamDiscussionCommentInput ##NON NULL

   _args: Args


   type: DeleteTeamDiscussionCommentPayload

class deleteVerifiableDomain(GQLObject):
   """
   deleteVerifiableDomain - Deletes a verifiable domain.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DeleteVerifiableDomain

      """
      input: DeleteVerifiableDomainInput ##NON NULL

   _args: Args


   type: DeleteVerifiableDomainPayload

class disablePullRequestAutoMerge(GQLObject):
   """
   disablePullRequestAutoMerge - Disable auto merge on the given pull request

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DisablePullRequestAutoMerge

      """
      input: DisablePullRequestAutoMergeInput ##NON NULL

   _args: Args


   type: DisablePullRequestAutoMergePayload

class dismissPullRequestReview(GQLObject):
   """
   dismissPullRequestReview - Dismisses an approved or rejected pull request review.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DismissPullRequestReview

      """
      input: DismissPullRequestReviewInput ##NON NULL

   _args: Args


   type: DismissPullRequestReviewPayload

class dismissRepositoryVulnerabilityAlert(GQLObject):
   """
   dismissRepositoryVulnerabilityAlert - Dismisses the Dependabot alert.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for DismissRepositoryVulnerabilityAlert

      """
      input: DismissRepositoryVulnerabilityAlertInput ##NON NULL

   _args: Args


   type: DismissRepositoryVulnerabilityAlertPayload

class enablePullRequestAutoMerge(GQLObject):
   """
   enablePullRequestAutoMerge - Enable the default auto-merge on a pull request.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for EnablePullRequestAutoMerge

      """
      input: EnablePullRequestAutoMergeInput ##NON NULL

   _args: Args


   type: EnablePullRequestAutoMergePayload

class followOrganization(GQLObject):
   """
   followOrganization - Follow an organization.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for FollowOrganization

      """
      input: FollowOrganizationInput ##NON NULL

   _args: Args


   type: FollowOrganizationPayload

class followUser(GQLObject):
   """
   followUser - Follow a user.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for FollowUser

      """
      input: FollowUserInput ##NON NULL

   _args: Args


   type: FollowUserPayload

class grantEnterpriseOrganizationsMigratorRole(GQLObject):
   """
   grantEnterpriseOrganizationsMigratorRole - Grant the migrator role to a user for all organizations under an enterprise account.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for GrantEnterpriseOrganizationsMigratorRole

      """
      input: GrantEnterpriseOrganizationsMigratorRoleInput ##NON NULL

   _args: Args


   type: GrantEnterpriseOrganizationsMigratorRolePayload

class grantMigratorRole(GQLObject):
   """
   grantMigratorRole - Grant the migrator role to a user or a team.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for GrantMigratorRole

      """
      input: GrantMigratorRoleInput ##NON NULL

   _args: Args


   type: GrantMigratorRolePayload

class inviteEnterpriseAdmin(GQLObject):
   """
   inviteEnterpriseAdmin - Invite someone to become an administrator of the enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for InviteEnterpriseAdmin

      """
      input: InviteEnterpriseAdminInput ##NON NULL

   _args: Args


   type: InviteEnterpriseAdminPayload

class linkProjectV2ToRepository(GQLObject):
   """
   linkProjectV2ToRepository - Links a project to a repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for LinkProjectV2ToRepository

      """
      input: LinkProjectV2ToRepositoryInput ##NON NULL

   _args: Args


   type: LinkProjectV2ToRepositoryPayload

class linkProjectV2ToTeam(GQLObject):
   """
   linkProjectV2ToTeam - Links a project to a team.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for LinkProjectV2ToTeam

      """
      input: LinkProjectV2ToTeamInput ##NON NULL

   _args: Args


   type: LinkProjectV2ToTeamPayload

class linkRepositoryToProject(GQLObject):
   """
   linkRepositoryToProject - Creates a repository link for a project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for LinkRepositoryToProject

      """
      input: LinkRepositoryToProjectInput ##NON NULL

   _args: Args


   type: LinkRepositoryToProjectPayload

class lockLockable(GQLObject):
   """
   lockLockable - Lock a lockable object

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for LockLockable

      """
      input: LockLockableInput ##NON NULL

   _args: Args


   type: LockLockablePayload

class markDiscussionCommentAsAnswer(GQLObject):
   """
   markDiscussionCommentAsAnswer - Mark a discussion comment as the chosen answer for discussions in an answerable category.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for MarkDiscussionCommentAsAnswer

      """
      input: MarkDiscussionCommentAsAnswerInput ##NON NULL

   _args: Args


   type: MarkDiscussionCommentAsAnswerPayload

class markFileAsViewed(GQLObject):
   """
   markFileAsViewed - Mark a pull request file as viewed

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for MarkFileAsViewed

      """
      input: MarkFileAsViewedInput ##NON NULL

   _args: Args


   type: MarkFileAsViewedPayload

class markPullRequestReadyForReview(GQLObject):
   """
   markPullRequestReadyForReview - Marks a pull request ready for review.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for MarkPullRequestReadyForReview

      """
      input: MarkPullRequestReadyForReviewInput ##NON NULL

   _args: Args


   type: MarkPullRequestReadyForReviewPayload

class mergeBranch(GQLObject):
   """
   mergeBranch - Merge a head into a branch.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for MergeBranch

      """
      input: MergeBranchInput ##NON NULL

   _args: Args


   type: MergeBranchPayload

class mergePullRequest(GQLObject):
   """
   mergePullRequest - Merge a pull request.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for MergePullRequest

      """
      input: MergePullRequestInput ##NON NULL

   _args: Args


   type: MergePullRequestPayload

class minimizeComment(GQLObject):
   """
   minimizeComment - Minimizes a comment on an Issue, Commit, Pull Request, or Gist

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for MinimizeComment

      """
      input: MinimizeCommentInput ##NON NULL

   _args: Args


   type: MinimizeCommentPayload

class moveProjectCard(GQLObject):
   """
   moveProjectCard - Moves a project card to another place.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for MoveProjectCard

      """
      input: MoveProjectCardInput ##NON NULL

   _args: Args


   type: MoveProjectCardPayload

class moveProjectColumn(GQLObject):
   """
   moveProjectColumn - Moves a project column to another place.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for MoveProjectColumn

      """
      input: MoveProjectColumnInput ##NON NULL

   _args: Args


   type: MoveProjectColumnPayload

class pinIssue(GQLObject):
   """
   pinIssue - Pin an issue to a repository

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for PinIssue

      """
      input: PinIssueInput ##NON NULL

   _args: Args


   type: PinIssuePayload

class publishSponsorsTier(GQLObject):
   """
   publishSponsorsTier - Publish an existing sponsorship tier that is currently still a draft to a GitHub Sponsors profile.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for PublishSponsorsTier

      """
      input: PublishSponsorsTierInput ##NON NULL

   _args: Args


   type: PublishSponsorsTierPayload

class regenerateEnterpriseIdentityProviderRecoveryCodes(GQLObject):
   """
   regenerateEnterpriseIdentityProviderRecoveryCodes - Regenerates the identity provider recovery codes for an enterprise

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RegenerateEnterpriseIdentityProviderRecoveryCodes

      """
      input: RegenerateEnterpriseIdentityProviderRecoveryCodesInput ##NON NULL

   _args: Args


   type: RegenerateEnterpriseIdentityProviderRecoveryCodesPayload

class regenerateVerifiableDomainToken(GQLObject):
   """
   regenerateVerifiableDomainToken - Regenerates a verifiable domain's verification token.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RegenerateVerifiableDomainToken

      """
      input: RegenerateVerifiableDomainTokenInput ##NON NULL

   _args: Args


   type: RegenerateVerifiableDomainTokenPayload

class rejectDeployments(GQLObject):
   """
   rejectDeployments - Reject all pending deployments under one or more environments

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RejectDeployments

      """
      input: RejectDeploymentsInput ##NON NULL

   _args: Args


   type: RejectDeploymentsPayload

class removeAssigneesFromAssignable(GQLObject):
   """
   removeAssigneesFromAssignable - Removes assignees from an assignable object.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RemoveAssigneesFromAssignable

      """
      input: RemoveAssigneesFromAssignableInput ##NON NULL

   _args: Args


   type: RemoveAssigneesFromAssignablePayload

class removeEnterpriseAdmin(GQLObject):
   """
   removeEnterpriseAdmin - Removes an administrator from the enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RemoveEnterpriseAdmin

      """
      input: RemoveEnterpriseAdminInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseAdminPayload

class removeEnterpriseIdentityProvider(GQLObject):
   """
   removeEnterpriseIdentityProvider - Removes the identity provider from an enterprise

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RemoveEnterpriseIdentityProvider

      """
      input: RemoveEnterpriseIdentityProviderInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseIdentityProviderPayload

class removeEnterpriseOrganization(GQLObject):
   """
   removeEnterpriseOrganization - Removes an organization from the enterprise

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RemoveEnterpriseOrganization

      """
      input: RemoveEnterpriseOrganizationInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseOrganizationPayload

class removeEnterpriseSupportEntitlement(GQLObject):
   """
   removeEnterpriseSupportEntitlement - Removes a support entitlement from an enterprise member.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RemoveEnterpriseSupportEntitlement

      """
      input: RemoveEnterpriseSupportEntitlementInput ##NON NULL

   _args: Args


   type: RemoveEnterpriseSupportEntitlementPayload

class removeLabelsFromLabelable(GQLObject):
   """
   removeLabelsFromLabelable - Removes labels from a Labelable object.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RemoveLabelsFromLabelable

      """
      input: RemoveLabelsFromLabelableInput ##NON NULL

   _args: Args


   type: RemoveLabelsFromLabelablePayload

class removeOutsideCollaborator(GQLObject):
   """
   removeOutsideCollaborator - Removes outside collaborator from all repositories in an organization.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RemoveOutsideCollaborator

      """
      input: RemoveOutsideCollaboratorInput ##NON NULL

   _args: Args


   type: RemoveOutsideCollaboratorPayload

class removeReaction(GQLObject):
   """
   removeReaction - Removes a reaction from a subject.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RemoveReaction

      """
      input: RemoveReactionInput ##NON NULL

   _args: Args


   type: RemoveReactionPayload

class removeStar(GQLObject):
   """
   removeStar - Removes a star from a Starrable.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RemoveStar

      """
      input: RemoveStarInput ##NON NULL

   _args: Args


   type: RemoveStarPayload

class removeUpvote(GQLObject):
   """
   removeUpvote - Remove an upvote to a discussion or discussion comment.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RemoveUpvote

      """
      input: RemoveUpvoteInput ##NON NULL

   _args: Args


   type: RemoveUpvotePayload

class reopenIssue(GQLObject):
   """
   reopenIssue - Reopen a issue.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ReopenIssue

      """
      input: ReopenIssueInput ##NON NULL

   _args: Args


   type: ReopenIssuePayload

class reopenPullRequest(GQLObject):
   """
   reopenPullRequest - Reopen a pull request.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ReopenPullRequest

      """
      input: ReopenPullRequestInput ##NON NULL

   _args: Args


   type: ReopenPullRequestPayload

class requestReviews(GQLObject):
   """
   requestReviews - Set review requests on a pull request.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RequestReviews

      """
      input: RequestReviewsInput ##NON NULL

   _args: Args


   type: RequestReviewsPayload

class rerequestCheckSuite(GQLObject):
   """
   rerequestCheckSuite - Rerequests an existing check suite.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RerequestCheckSuite

      """
      input: RerequestCheckSuiteInput ##NON NULL

   _args: Args


   type: RerequestCheckSuitePayload

class resolveReviewThread(GQLObject):
   """
   resolveReviewThread - Marks a review thread as resolved.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for ResolveReviewThread

      """
      input: ResolveReviewThreadInput ##NON NULL

   _args: Args


   type: ResolveReviewThreadPayload

class revokeEnterpriseOrganizationsMigratorRole(GQLObject):
   """
   revokeEnterpriseOrganizationsMigratorRole - Revoke the migrator role to a user for all organizations under an enterprise account.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RevokeEnterpriseOrganizationsMigratorRole

      """
      input: RevokeEnterpriseOrganizationsMigratorRoleInput ##NON NULL

   _args: Args


   type: RevokeEnterpriseOrganizationsMigratorRolePayload

class revokeMigratorRole(GQLObject):
   """
   revokeMigratorRole - Revoke the migrator role from a user or a team.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for RevokeMigratorRole

      """
      input: RevokeMigratorRoleInput ##NON NULL

   _args: Args


   type: RevokeMigratorRolePayload

class setEnterpriseIdentityProvider(GQLObject):
   """
   setEnterpriseIdentityProvider - Creates or updates the identity provider for an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for SetEnterpriseIdentityProvider

      """
      input: SetEnterpriseIdentityProviderInput ##NON NULL

   _args: Args


   type: SetEnterpriseIdentityProviderPayload

class setOrganizationInteractionLimit(GQLObject):
   """
   setOrganizationInteractionLimit - Set an organization level interaction limit for an organization's public repositories.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for SetOrganizationInteractionLimit

      """
      input: SetOrganizationInteractionLimitInput ##NON NULL

   _args: Args


   type: SetOrganizationInteractionLimitPayload

class setRepositoryInteractionLimit(GQLObject):
   """
   setRepositoryInteractionLimit - Sets an interaction limit setting for a repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for SetRepositoryInteractionLimit

      """
      input: SetRepositoryInteractionLimitInput ##NON NULL

   _args: Args


   type: SetRepositoryInteractionLimitPayload

class setUserInteractionLimit(GQLObject):
   """
   setUserInteractionLimit - Set a user level interaction limit for an user's public repositories.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for SetUserInteractionLimit

      """
      input: SetUserInteractionLimitInput ##NON NULL

   _args: Args


   type: SetUserInteractionLimitPayload

class startRepositoryMigration(GQLObject):
   """
   startRepositoryMigration - Starts a GitHub Enterprise Importer (GEI) repository migration.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for StartRepositoryMigration

      """
      input: StartRepositoryMigrationInput ##NON NULL

   _args: Args


   type: StartRepositoryMigrationPayload

class submitPullRequestReview(GQLObject):
   """
   submitPullRequestReview - Submits a pending pull request review.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for SubmitPullRequestReview

      """
      input: SubmitPullRequestReviewInput ##NON NULL

   _args: Args


   type: SubmitPullRequestReviewPayload

class transferEnterpriseOrganization(GQLObject):
   """
   transferEnterpriseOrganization - Transfer an organization from one enterprise to another enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for TransferEnterpriseOrganization

      """
      input: TransferEnterpriseOrganizationInput ##NON NULL

   _args: Args


   type: TransferEnterpriseOrganizationPayload

class transferIssue(GQLObject):
   """
   transferIssue - Transfer an issue to a different repository

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for TransferIssue

      """
      input: TransferIssueInput ##NON NULL

   _args: Args


   type: TransferIssuePayload

class unarchiveProjectV2Item(GQLObject):
   """
   unarchiveProjectV2Item - Unarchives a ProjectV2Item

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnarchiveProjectV2Item

      """
      input: UnarchiveProjectV2ItemInput ##NON NULL

   _args: Args


   type: UnarchiveProjectV2ItemPayload

class unarchiveRepository(GQLObject):
   """
   unarchiveRepository - Unarchives a repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnarchiveRepository

      """
      input: UnarchiveRepositoryInput ##NON NULL

   _args: Args


   type: UnarchiveRepositoryPayload

class unfollowOrganization(GQLObject):
   """
   unfollowOrganization - Unfollow an organization.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnfollowOrganization

      """
      input: UnfollowOrganizationInput ##NON NULL

   _args: Args


   type: UnfollowOrganizationPayload

class unfollowUser(GQLObject):
   """
   unfollowUser - Unfollow a user.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnfollowUser

      """
      input: UnfollowUserInput ##NON NULL

   _args: Args


   type: UnfollowUserPayload

class unlinkProjectV2FromRepository(GQLObject):
   """
   unlinkProjectV2FromRepository - Unlinks a project from a repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnlinkProjectV2FromRepository

      """
      input: UnlinkProjectV2FromRepositoryInput ##NON NULL

   _args: Args


   type: UnlinkProjectV2FromRepositoryPayload

class unlinkProjectV2FromTeam(GQLObject):
   """
   unlinkProjectV2FromTeam - Unlinks a project to a team.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnlinkProjectV2FromTeam

      """
      input: UnlinkProjectV2FromTeamInput ##NON NULL

   _args: Args


   type: UnlinkProjectV2FromTeamPayload

class unlinkRepositoryFromProject(GQLObject):
   """
   unlinkRepositoryFromProject - Deletes a repository link from a project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnlinkRepositoryFromProject

      """
      input: UnlinkRepositoryFromProjectInput ##NON NULL

   _args: Args


   type: UnlinkRepositoryFromProjectPayload

class unlockLockable(GQLObject):
   """
   unlockLockable - Unlock a lockable object

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnlockLockable

      """
      input: UnlockLockableInput ##NON NULL

   _args: Args


   type: UnlockLockablePayload

class unmarkDiscussionCommentAsAnswer(GQLObject):
   """
   unmarkDiscussionCommentAsAnswer - Unmark a discussion comment as the chosen answer for discussions in an answerable category.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnmarkDiscussionCommentAsAnswer

      """
      input: UnmarkDiscussionCommentAsAnswerInput ##NON NULL

   _args: Args


   type: UnmarkDiscussionCommentAsAnswerPayload

class unmarkFileAsViewed(GQLObject):
   """
   unmarkFileAsViewed - Unmark a pull request file as viewed

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnmarkFileAsViewed

      """
      input: UnmarkFileAsViewedInput ##NON NULL

   _args: Args


   type: UnmarkFileAsViewedPayload

class unmarkIssueAsDuplicate(GQLObject):
   """
   unmarkIssueAsDuplicate - Unmark an issue as a duplicate of another issue.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnmarkIssueAsDuplicate

      """
      input: UnmarkIssueAsDuplicateInput ##NON NULL

   _args: Args


   type: UnmarkIssueAsDuplicatePayload

class unminimizeComment(GQLObject):
   """
   unminimizeComment - Unminimizes a comment on an Issue, Commit, Pull Request, or Gist

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnminimizeComment

      """
      input: UnminimizeCommentInput ##NON NULL

   _args: Args


   type: UnminimizeCommentPayload

class unpinIssue(GQLObject):
   """
   unpinIssue - Unpin a pinned issue from a repository

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnpinIssue

      """
      input: UnpinIssueInput ##NON NULL

   _args: Args


   type: UnpinIssuePayload

class unresolveReviewThread(GQLObject):
   """
   unresolveReviewThread - Marks a review thread as unresolved.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UnresolveReviewThread

      """
      input: UnresolveReviewThreadInput ##NON NULL

   _args: Args


   type: UnresolveReviewThreadPayload

class updateBranchProtectionRule(GQLObject):
   """
   updateBranchProtectionRule - Update a branch protection rule

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateBranchProtectionRule

      """
      input: UpdateBranchProtectionRuleInput ##NON NULL

   _args: Args


   type: UpdateBranchProtectionRulePayload

class updateCheckRun(GQLObject):
   """
   updateCheckRun - Update a check run

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateCheckRun

      """
      input: UpdateCheckRunInput ##NON NULL

   _args: Args


   type: UpdateCheckRunPayload

class updateCheckSuitePreferences(GQLObject):
   """
   updateCheckSuitePreferences - Modifies the settings of an existing check suite

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateCheckSuitePreferences

      """
      input: UpdateCheckSuitePreferencesInput ##NON NULL

   _args: Args


   type: UpdateCheckSuitePreferencesPayload

class updateDiscussion(GQLObject):
   """
   updateDiscussion - Update a discussion

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateDiscussion

      """
      input: UpdateDiscussionInput ##NON NULL

   _args: Args


   type: UpdateDiscussionPayload

class updateDiscussionComment(GQLObject):
   """
   updateDiscussionComment - Update the contents of a comment on a Discussion

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateDiscussionComment

      """
      input: UpdateDiscussionCommentInput ##NON NULL

   _args: Args


   type: UpdateDiscussionCommentPayload

class updateEnterpriseAdministratorRole(GQLObject):
   """
   updateEnterpriseAdministratorRole - Updates the role of an enterprise administrator.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseAdministratorRole

      """
      input: UpdateEnterpriseAdministratorRoleInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseAdministratorRolePayload

class updateEnterpriseAllowPrivateRepositoryForkingSetting(GQLObject):
   """
   updateEnterpriseAllowPrivateRepositoryForkingSetting - Sets whether private repository forks are enabled for an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseAllowPrivateRepositoryForkingSetting

      """
      input: UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload

class updateEnterpriseDefaultRepositoryPermissionSetting(GQLObject):
   """
   updateEnterpriseDefaultRepositoryPermissionSetting - Sets the base repository permission for organizations in an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseDefaultRepositoryPermissionSetting

      """
      input: UpdateEnterpriseDefaultRepositoryPermissionSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseDefaultRepositoryPermissionSettingPayload

class updateEnterpriseMembersCanChangeRepositoryVisibilitySetting(GQLObject):
   """
   updateEnterpriseMembersCanChangeRepositoryVisibilitySetting - Sets whether organization members with admin permissions on a repository can change repository visibility.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseMembersCanChangeRepositoryVisibilitySetting

      """
      input: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload

class updateEnterpriseMembersCanCreateRepositoriesSetting(GQLObject):
   """
   updateEnterpriseMembersCanCreateRepositoriesSetting - Sets the members can create repositories setting for an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseMembersCanCreateRepositoriesSetting

      """
      input: UpdateEnterpriseMembersCanCreateRepositoriesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload

class updateEnterpriseMembersCanDeleteIssuesSetting(GQLObject):
   """
   updateEnterpriseMembersCanDeleteIssuesSetting - Sets the members can delete issues setting for an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseMembersCanDeleteIssuesSetting

      """
      input: UpdateEnterpriseMembersCanDeleteIssuesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanDeleteIssuesSettingPayload

class updateEnterpriseMembersCanDeleteRepositoriesSetting(GQLObject):
   """
   updateEnterpriseMembersCanDeleteRepositoriesSetting - Sets the members can delete repositories setting for an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseMembersCanDeleteRepositoriesSetting

      """
      input: UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload

class updateEnterpriseMembersCanInviteCollaboratorsSetting(GQLObject):
   """
   updateEnterpriseMembersCanInviteCollaboratorsSetting - Sets whether members can invite collaborators are enabled for an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseMembersCanInviteCollaboratorsSetting

      """
      input: UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload

class updateEnterpriseMembersCanMakePurchasesSetting(GQLObject):
   """
   updateEnterpriseMembersCanMakePurchasesSetting - Sets whether or not an organization admin can make purchases.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseMembersCanMakePurchasesSetting

      """
      input: UpdateEnterpriseMembersCanMakePurchasesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanMakePurchasesSettingPayload

class updateEnterpriseMembersCanUpdateProtectedBranchesSetting(GQLObject):
   """
   updateEnterpriseMembersCanUpdateProtectedBranchesSetting - Sets the members can update protected branches setting for an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseMembersCanUpdateProtectedBranchesSetting

      """
      input: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload

class updateEnterpriseMembersCanViewDependencyInsightsSetting(GQLObject):
   """
   updateEnterpriseMembersCanViewDependencyInsightsSetting - Sets the members can view dependency insights for an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseMembersCanViewDependencyInsightsSetting

      """
      input: UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload

class updateEnterpriseOrganizationProjectsSetting(GQLObject):
   """
   updateEnterpriseOrganizationProjectsSetting - Sets whether organization projects are enabled for an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseOrganizationProjectsSetting

      """
      input: UpdateEnterpriseOrganizationProjectsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseOrganizationProjectsSettingPayload

class updateEnterpriseOwnerOrganizationRole(GQLObject):
   """
   updateEnterpriseOwnerOrganizationRole - Updates the role of an enterprise owner with an organization.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseOwnerOrganizationRole

      """
      input: UpdateEnterpriseOwnerOrganizationRoleInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseOwnerOrganizationRolePayload

class updateEnterpriseProfile(GQLObject):
   """
   updateEnterpriseProfile - Updates an enterprise's profile.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseProfile

      """
      input: UpdateEnterpriseProfileInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseProfilePayload

class updateEnterpriseRepositoryProjectsSetting(GQLObject):
   """
   updateEnterpriseRepositoryProjectsSetting - Sets whether repository projects are enabled for a enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseRepositoryProjectsSetting

      """
      input: UpdateEnterpriseRepositoryProjectsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseRepositoryProjectsSettingPayload

class updateEnterpriseTeamDiscussionsSetting(GQLObject):
   """
   updateEnterpriseTeamDiscussionsSetting - Sets whether team discussions are enabled for an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseTeamDiscussionsSetting

      """
      input: UpdateEnterpriseTeamDiscussionsSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseTeamDiscussionsSettingPayload

class updateEnterpriseTwoFactorAuthenticationRequiredSetting(GQLObject):
   """
   updateEnterpriseTwoFactorAuthenticationRequiredSetting - Sets whether two factor authentication is required for all users in an enterprise.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnterpriseTwoFactorAuthenticationRequiredSetting

      """
      input: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput ##NON NULL

   _args: Args


   type: UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload

class updateEnvironment(GQLObject):
   """
   updateEnvironment - Updates an environment.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateEnvironment

      """
      input: UpdateEnvironmentInput ##NON NULL

   _args: Args


   type: UpdateEnvironmentPayload

class updateIpAllowListEnabledSetting(GQLObject):
   """
   updateIpAllowListEnabledSetting - Sets whether an IP allow list is enabled on an owner.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateIpAllowListEnabledSetting

      """
      input: UpdateIpAllowListEnabledSettingInput ##NON NULL

   _args: Args


   type: UpdateIpAllowListEnabledSettingPayload

class updateIpAllowListEntry(GQLObject):
   """
   updateIpAllowListEntry - Updates an IP allow list entry.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateIpAllowListEntry

      """
      input: UpdateIpAllowListEntryInput ##NON NULL

   _args: Args


   type: UpdateIpAllowListEntryPayload

class updateIpAllowListForInstalledAppsEnabledSetting(GQLObject):
   """
   updateIpAllowListForInstalledAppsEnabledSetting - Sets whether IP allow list configuration for installed GitHub Apps is enabled on an owner.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateIpAllowListForInstalledAppsEnabledSetting

      """
      input: UpdateIpAllowListForInstalledAppsEnabledSettingInput ##NON NULL

   _args: Args


   type: UpdateIpAllowListForInstalledAppsEnabledSettingPayload

class updateIssue(GQLObject):
   """
   updateIssue - Updates an Issue.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateIssue

      """
      input: UpdateIssueInput ##NON NULL

   _args: Args


   type: UpdateIssuePayload

class updateIssueComment(GQLObject):
   """
   updateIssueComment - Updates an IssueComment object.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateIssueComment

      """
      input: UpdateIssueCommentInput ##NON NULL

   _args: Args


   type: UpdateIssueCommentPayload

class updateNotificationRestrictionSetting(GQLObject):
   """
   updateNotificationRestrictionSetting - Update the setting to restrict notifications to only verified or approved domains available to an owner.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateNotificationRestrictionSetting

      """
      input: UpdateNotificationRestrictionSettingInput ##NON NULL

   _args: Args


   type: UpdateNotificationRestrictionSettingPayload

class updateOrganizationAllowPrivateRepositoryForkingSetting(GQLObject):
   """
   updateOrganizationAllowPrivateRepositoryForkingSetting - Sets whether private repository forks are enabled for an organization.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateOrganizationAllowPrivateRepositoryForkingSetting

      """
      input: UpdateOrganizationAllowPrivateRepositoryForkingSettingInput ##NON NULL

   _args: Args


   type: UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload

class updateOrganizationWebCommitSignoffSetting(GQLObject):
   """
   updateOrganizationWebCommitSignoffSetting - Sets whether contributors are required to sign off on web-based commits for repositories in an organization.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateOrganizationWebCommitSignoffSetting

      """
      input: UpdateOrganizationWebCommitSignoffSettingInput ##NON NULL

   _args: Args


   type: UpdateOrganizationWebCommitSignoffSettingPayload

class updateProject(GQLObject):
   """
   updateProject - Updates an existing project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateProject

      """
      input: UpdateProjectInput ##NON NULL

   _args: Args


   type: UpdateProjectPayload

class updateProjectCard(GQLObject):
   """
   updateProjectCard - Updates an existing project card.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateProjectCard

      """
      input: UpdateProjectCardInput ##NON NULL

   _args: Args


   type: UpdateProjectCardPayload

class updateProjectColumn(GQLObject):
   """
   updateProjectColumn - Updates an existing project column.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateProjectColumn

      """
      input: UpdateProjectColumnInput ##NON NULL

   _args: Args


   type: UpdateProjectColumnPayload

class updateProjectDraftIssue(GQLObject):
   """
   updateProjectDraftIssue - Updates a draft issue within a Project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateProjectDraftIssue

      """
      input: UpdateProjectDraftIssueInput ##NON NULL

   _args: Args


   type: UpdateProjectDraftIssuePayload

class updateProjectNext(GQLObject):
   """
   updateProjectNext - Updates an existing project (beta).

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateProjectNext

      """
      input: UpdateProjectNextInput ##NON NULL

   _args: Args


   type: UpdateProjectNextPayload

class updateProjectNextItemField(GQLObject):
   """
   updateProjectNextItemField - Updates a field of an item from a Project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateProjectNextItemField

      """
      input: UpdateProjectNextItemFieldInput ##NON NULL

   _args: Args


   type: UpdateProjectNextItemFieldPayload

class updateProjectV2(GQLObject):
   """
   updateProjectV2 - Updates an existing project (beta).

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateProjectV2

      """
      input: UpdateProjectV2Input ##NON NULL

   _args: Args


   type: UpdateProjectV2Payload

class updateProjectV2DraftIssue(GQLObject):
   """
   updateProjectV2DraftIssue - Updates a draft issue within a Project.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateProjectV2DraftIssue

      """
      input: UpdateProjectV2DraftIssueInput ##NON NULL

   _args: Args


   type: UpdateProjectV2DraftIssuePayload

class updateProjectV2ItemFieldValue(GQLObject):
   """
   updateProjectV2ItemFieldValue - This mutation updates the value of a field for an item in a Project. Currently only single-select, text, number, date, and iteration fields are supported.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateProjectV2ItemFieldValue

      """
      input: UpdateProjectV2ItemFieldValueInput ##NON NULL

   _args: Args


   type: UpdateProjectV2ItemFieldValuePayload

class updateProjectV2ItemPosition(GQLObject):
   """
   updateProjectV2ItemPosition - This mutation updates the position of the item in the project, where the position represents the priority of an item.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateProjectV2ItemPosition

      """
      input: UpdateProjectV2ItemPositionInput ##NON NULL

   _args: Args


   type: UpdateProjectV2ItemPositionPayload

class updatePullRequest(GQLObject):
   """
   updatePullRequest - Update a pull request

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdatePullRequest

      """
      input: UpdatePullRequestInput ##NON NULL

   _args: Args


   type: UpdatePullRequestPayload

class updatePullRequestBranch(GQLObject):
   """
   updatePullRequestBranch - Merge or Rebase HEAD from upstream branch into pull request branch

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdatePullRequestBranch

      """
      input: UpdatePullRequestBranchInput ##NON NULL

   _args: Args


   type: UpdatePullRequestBranchPayload

class updatePullRequestReview(GQLObject):
   """
   updatePullRequestReview - Updates the body of a pull request review.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdatePullRequestReview

      """
      input: UpdatePullRequestReviewInput ##NON NULL

   _args: Args


   type: UpdatePullRequestReviewPayload

class updatePullRequestReviewComment(GQLObject):
   """
   updatePullRequestReviewComment - Updates a pull request review comment.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdatePullRequestReviewComment

      """
      input: UpdatePullRequestReviewCommentInput ##NON NULL

   _args: Args


   type: UpdatePullRequestReviewCommentPayload

class updateRef(GQLObject):
   """
   updateRef - Update a Git Ref.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateRef

      """
      input: UpdateRefInput ##NON NULL

   _args: Args


   type: UpdateRefPayload

class updateRepository(GQLObject):
   """
   updateRepository - Update information about a repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateRepository

      """
      input: UpdateRepositoryInput ##NON NULL

   _args: Args


   type: UpdateRepositoryPayload

class updateRepositoryWebCommitSignoffSetting(GQLObject):
   """
   updateRepositoryWebCommitSignoffSetting - Sets whether contributors are required to sign off on web-based commits for a repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateRepositoryWebCommitSignoffSetting

      """
      input: UpdateRepositoryWebCommitSignoffSettingInput ##NON NULL

   _args: Args


   type: UpdateRepositoryWebCommitSignoffSettingPayload

class updateSponsorshipPreferences(GQLObject):
   """
   updateSponsorshipPreferences - Change visibility of your sponsorship and opt in or out of email updates from the maintainer.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateSponsorshipPreferences

      """
      input: UpdateSponsorshipPreferencesInput ##NON NULL

   _args: Args


   type: UpdateSponsorshipPreferencesPayload

class updateSubscription(GQLObject):
   """
   updateSubscription - Updates the state for subscribable subjects.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateSubscription

      """
      input: UpdateSubscriptionInput ##NON NULL

   _args: Args


   type: UpdateSubscriptionPayload

class updateTeamDiscussion(GQLObject):
   """
   updateTeamDiscussion - Updates a team discussion.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateTeamDiscussion

      """
      input: UpdateTeamDiscussionInput ##NON NULL

   _args: Args


   type: UpdateTeamDiscussionPayload

class updateTeamDiscussionComment(GQLObject):
   """
   updateTeamDiscussionComment - Updates a discussion comment.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateTeamDiscussionComment

      """
      input: UpdateTeamDiscussionCommentInput ##NON NULL

   _args: Args


   type: UpdateTeamDiscussionCommentPayload

class updateTeamsRepository(GQLObject):
   """
   updateTeamsRepository - Update team repository.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateTeamsRepository

      """
      input: UpdateTeamsRepositoryInput ##NON NULL

   _args: Args


   type: UpdateTeamsRepositoryPayload

class updateTopics(GQLObject):
   """
   updateTopics - Replaces the repository's topics with the given topics.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for UpdateTopics

      """
      input: UpdateTopicsInput ##NON NULL

   _args: Args


   type: UpdateTopicsPayload

class verifyVerifiableDomain(GQLObject):
   """
   verifyVerifiableDomain - Verify that a verifiable domain has the expected DNS record.

   """
   class Args(GQLOperationArgs): 
      """
      input - Parameters for VerifyVerifiableDomain

      """
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
