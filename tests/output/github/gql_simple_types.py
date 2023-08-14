from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class LUDLL_anyPinnableItems_Field(ArguedBool):
   """
   LUDLL_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class AXANY_URI_Field(ArguedStr):
   """
   AXANY_URI_Field - URL for the listing's logo image.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class PCKOH_URI_Field(ArguedStr):
   """
   PCKOH_URI_Field - A URL pointing to the app's logo.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting image.

      """
      size: int

   _args: URIArgs



class GZBMK_URI_Field(ArguedStr):
   """
   GZBMK_URI_Field - A URL pointing to the enterprise's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class YSLVF_HTML_Field(ArguedStr):
   """
   YSLVF_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class CMOBU_URI_Field(ArguedStr):
   """
   CMOBU_URI_Field - A URL pointing to the enterprise user account's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class EUBSH_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   EUBSH_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      since - Filter payments to those that occurred on or after this time.

      until - Filter payments to those that occurred before this time.

      sponsorableLogins - Filter payments to those made to the users or organizations with the specified usernames.

      """
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class IVPGA_isSponsoredBy_Field(ArguedBool):
   """
   IVPGA_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class SBBTQ_URI_Field(ArguedStr):
   """
   SBBTQ_URI_Field - A URL pointing to the organization's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class NAOCE_anyPinnableItems_Field(ArguedBool):
   """
   NAOCE_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class USPFE_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   USPFE_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      since - Filter payments to those that occurred on or after this time.

      until - Filter payments to those that occurred before this time.

      sponsorableLogins - Filter payments to those made to the users or organizations with the specified usernames.

      """
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class FXIBK_organizationVerifiedDomainEmails_Field(ArguedStr):
   """
   FXIBK_organizationVerifiedDomainEmails_Field - Verified email addresses that match verified domains for a specified organization the user is a member of.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      login - The login of the organization to match verified domains from.

      """
      login: NonNull_str

   _args: strArgs



class PAZDL_isSponsoredBy_Field(ArguedBool):
   """
   PAZDL_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class CJXXJ_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedBool):
   """
   CJXXJ_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field - Could this user receive email notifications, if the organization had notification restrictions enabled?

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      login - The login of the organization to check.

      """
      login: NonNull_str

   _args: boolArgs



class FJZJD_URI_Field(ArguedStr):
   """
   FJZJD_URI_Field - A URL pointing to the user's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class ALXTR_anyPinnableItems_Field(ArguedBool):
   """
   ALXTR_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class GUWSH_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   GUWSH_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      since - Filter payments to those that occurred on or after this time.

      until - Filter payments to those that occurred before this time.

      sponsorableLogins - Filter payments to those made to the users or organizations with the specified usernames.

      """
      since: DateTime
      until: DateTime
      sponsorableLogins: list[NonNull_str]

   _args: intArgs



class UGLRZ_isSponsoredBy_Field(ArguedBool):
   """
   UGLRZ_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class BXUPV_text_Field(ArguedStr):
   """
   BXUPV_text_Field - UTF8 text data or null if the file is binary

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      truncate - Optionally truncate the returned file to this length.

      """
      truncate: int

   _args: strArgs



class FANME_totalRepositoryContributions_Field(ArguedInt):
   """
   FANME_totalRepositoryContributions_Field - How many repositories the user created.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first repository ever be excluded from this count.

      """
      excludeFirst: bool

   _args: intArgs



class HBFUS_totalRepositoriesWithContributedPullRequests_Field(ArguedInt):
   """
   HBFUS_totalRepositoriesWithContributedPullRequests_Field - How many different repositories the user opened pull requests in.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class FETUI_totalRepositoriesWithContributedIssues_Field(ArguedInt):
   """
   FETUI_totalRepositoriesWithContributedIssues_Field - How many different repositories the user opened issues in.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class SSDQK_totalPullRequestContributions_Field(ArguedInt):
   """
   SSDQK_totalPullRequestContributions_Field - How many pull requests the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class TGGSE_totalIssueContributions_Field(ArguedInt):
   """
   TGGSE_totalIssueContributions_Field - How many issues the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class EPWEP_isRequired_Field(ArguedBool):
   """
   EPWEP_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class KCEXX_URI_Field(ArguedStr):
   """
   KCEXX_URI_Field - The avatar of the OAuth application or the user that created the status

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class HGFDO_isRequired_Field(ArguedBool):
   """
   HGFDO_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class FBRUV_URI_Field(ArguedStr):
   """
   FBRUV_URI_Field - A URL pointing to the author's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class EPWRV_viewerMergeHeadlineText_Field(ArguedStr):
   """
   EPWRV_viewerMergeHeadlineText_Field - The merge headline text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class EAHTS_viewerMergeBodyText_Field(ArguedStr):
   """
   EAHTS_viewerMergeBodyText_Field - The merge body text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class WHPBO_URI_Field(ArguedStr):
   """
   WHPBO_URI_Field - A URL pointing to the team's avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class JLOQM_trackedIssuesCount_Field(ArguedInt):
   """
   JLOQM_trackedIssuesCount_Field - The number of tracked issues for this issue

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      states - Limit the count to tracked issues with the specified states.

      """
      states: list[TrackedIssueStates]

   _args: intArgs



class PJJUQ_HTML_Field(ArguedStr):
   """
   PJJUQ_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class HKLOV_URI_Field(ArguedStr):
   """
   HKLOV_URI_Field - A URL pointing to the owner's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class HMPMH_HTML_Field(ArguedStr):
   """
   HMPMH_HTML_Field - A description of the release, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class VOMNP_URI_Field(ArguedStr):
   """
   VOMNP_URI_Field - A URL pointing to the GitHub App's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class WorkflowRunOrder(GQLObject):
   """
   WorkflowRunOrder - Ways in which lists of workflow runs can be ordered upon return.

   field - The field by which to order workflows.

   direction - The direction in which to order workflow runs by the specified field.

   """
   field: WorkflowRunOrderField
   direction: OrderDirection

class VerifyVerifiableDomainInput(GQLObject):
   """
   VerifyVerifiableDomainInput - Autogenerated input type of VerifyVerifiableDomain

   id - The ID of the verifiable domain to verify.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class UserStatusOrder(GQLObject):
   """
   UserStatusOrder - Ordering options for user status connections.

   field - The field to order user statuses by.

   direction - The ordering direction.

   """
   field: UserStatusOrderField
   direction: OrderDirection

class UpdateTopicsInput(GQLObject):
   """
   UpdateTopicsInput - Autogenerated input type of UpdateTopics

   repositoryId - The Node ID of the repository.

   topicNames - An array of topic names.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   topicNames: list[str]
   clientMutationId: str

class UpdateTeamDiscussionInput(GQLObject):
   """
   UpdateTeamDiscussionInput - Autogenerated input type of UpdateTeamDiscussion

   id - The Node ID of the discussion to modify.

   title - The updated title of the discussion.

   body - The updated text of the discussion.

   bodyVersion - The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server.

   pinned - If provided, sets the pinned state of the updated discussion.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   title: str
   body: str
   bodyVersion: str
   pinned: bool
   clientMutationId: str

class UpdateSubscriptionInput(GQLObject):
   """
   UpdateSubscriptionInput - Autogenerated input type of UpdateSubscription

   subscribableId - The Node ID of the subscribable object to modify.

   state - The new state of the subscription.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subscribableId: ID
   state: SubscriptionState
   clientMutationId: str

class UpdateRepositoryWebCommitSignoffSettingInput(GQLObject):
   """
   UpdateRepositoryWebCommitSignoffSettingInput - Autogenerated input type of UpdateRepositoryWebCommitSignoffSetting

   repositoryId - The ID of the repository to update.

   webCommitSignoffRequired - Indicates if the repository should require signoff on web-based commits.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   webCommitSignoffRequired: bool
   clientMutationId: str

class UpdateRefInput(GQLObject):
   """
   UpdateRefInput - Autogenerated input type of UpdateRef

   refId - The Node ID of the Ref to be updated.

   oid - The GitObjectID that the Ref shall be updated to target.

   force - Permit updates of branch Refs that are not fast-forwards?

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   refId: ID
   oid: GitObjectID
   force: bool
   clientMutationId: str

class UpdatePullRequestReviewCommentInput(GQLObject):
   """
   UpdatePullRequestReviewCommentInput - Autogenerated input type of UpdatePullRequestReviewComment

   pullRequestReviewCommentId - The Node ID of the comment to modify.

   body - The text of the comment.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestReviewCommentId: ID
   body: str
   clientMutationId: str

class UpdatePullRequestBranchInput(GQLObject):
   """
   UpdatePullRequestBranchInput - Autogenerated input type of UpdatePullRequestBranch

   pullRequestId - The Node ID of the pull request.

   expectedHeadOid - The head ref oid for the upstream branch.

   updateMethod - The update branch method to use. If omitted, defaults to 'MERGE'

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   expectedHeadOid: GitObjectID
   updateMethod: PullRequestBranchUpdateMethod
   clientMutationId: str

class UpdateProjectV2Input(GQLObject):
   """
   UpdateProjectV2Input - Autogenerated input type of UpdateProjectV2

   projectId - The ID of the Project to update.

   title - Set the title of the project.

   shortDescription - Set the short description of the project.

   readme - Set the readme description of the project.

   closed - Set the project to closed or open.

   public - Set the project to public or private.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   title: str
   shortDescription: str
   readme: str
   closed: bool
   public: bool
   clientMutationId: str

class UpdateProjectInput(GQLObject):
   """
   UpdateProjectInput - Autogenerated input type of UpdateProject

   projectId - The Project ID to update.

   name - The name of project.

   body - The description of project.

   state - Whether the project is open or closed.

   public - Whether the project is public or not.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   name: str
   body: str
   state: ProjectState
   public: bool
   clientMutationId: str

class UpdateProjectCardInput(GQLObject):
   """
   UpdateProjectCardInput - Autogenerated input type of UpdateProjectCard

   projectCardId - The ProjectCard ID to update.

   isArchived - Whether or not the ProjectCard should be archived

   note - The note of ProjectCard.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectCardId: ID
   isArchived: bool
   note: str
   clientMutationId: str

class UpdateParameters(GQLObject):
   """
   UpdateParameters - Only allow users with bypass permission to update matching refs.

   updateAllowsFetchAndMerge - Branch can pull changes from its upstream repository

   """
   updateAllowsFetchAndMerge: bool

class UpdateOrganizationAllowPrivateRepositoryForkingSettingInput(GQLObject):
   """
   UpdateOrganizationAllowPrivateRepositoryForkingSettingInput - Autogenerated input type of UpdateOrganizationAllowPrivateRepositoryForkingSetting

   organizationId - The ID of the organization on which to set the allow private repository forking setting.

   forkingEnabled - Enable forking of private repositories in the organization?

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID
   forkingEnabled: bool
   clientMutationId: str

class UpdateIssueInput(GQLObject):
   """
   UpdateIssueInput - Autogenerated input type of UpdateIssue

   id - The ID of the Issue to modify.

   title - The title for the issue.

   body - The body for the issue description.

   assigneeIds - An array of Node IDs of users for this issue.

   milestoneId - The Node ID of the milestone for this issue.

   labelIds - An array of Node IDs of labels for this issue.

   state - The desired issue state.

   projectIds - An array of Node IDs for projects associated with this issue.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   title: str
   body: str
   assigneeIds: list[ID]
   milestoneId: ID
   labelIds: list[ID]
   state: IssueState
   projectIds: list[ID]
   clientMutationId: str

class UpdateIpAllowListForInstalledAppsEnabledSettingInput(GQLObject):
   """
   UpdateIpAllowListForInstalledAppsEnabledSettingInput - Autogenerated input type of UpdateIpAllowListForInstalledAppsEnabledSetting

   ownerId - The ID of the owner.

   settingValue - The value for the IP allow list configuration for installed GitHub Apps setting.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID
   settingValue: IpAllowListForInstalledAppsEnabledSettingValue
   clientMutationId: str

class UpdateIpAllowListEnabledSettingInput(GQLObject):
   """
   UpdateIpAllowListEnabledSettingInput - Autogenerated input type of UpdateIpAllowListEnabledSetting

   ownerId - The ID of the owner on which to set the IP allow list enabled setting.

   settingValue - The value for the IP allow list enabled setting.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID
   settingValue: IpAllowListEnabledSettingValue
   clientMutationId: str

class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput(GQLObject):
   """
   UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput - Autogenerated input type of UpdateEnterpriseTwoFactorAuthenticationRequiredSetting

   enterpriseId - The ID of the enterprise on which to set the two factor authentication required setting.

   settingValue - The value for the two factor authentication required setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   settingValue: EnterpriseEnabledSettingValue
   clientMutationId: str

class UpdateEnterpriseRepositoryProjectsSettingInput(GQLObject):
   """
   UpdateEnterpriseRepositoryProjectsSettingInput - Autogenerated input type of UpdateEnterpriseRepositoryProjectsSetting

   enterpriseId - The ID of the enterprise on which to set the repository projects setting.

   settingValue - The value for the repository projects setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseOwnerOrganizationRolePayload(GQLObject):
   """
   UpdateEnterpriseOwnerOrganizationRolePayload - Autogenerated return type of UpdateEnterpriseOwnerOrganizationRole

   clientMutationId - A unique identifier for the client performing the mutation.

   message - A message confirming the result of changing the owner's organization role.

   """
   clientMutationId: str
   message: str

class UpdateEnterpriseOrganizationProjectsSettingInput(GQLObject):
   """
   UpdateEnterpriseOrganizationProjectsSettingInput - Autogenerated input type of UpdateEnterpriseOrganizationProjectsSetting

   enterpriseId - The ID of the enterprise on which to set the organization projects setting.

   settingValue - The value for the organization projects setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput(GQLObject):
   """
   UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput - Autogenerated input type of UpdateEnterpriseMembersCanUpdateProtectedBranchesSetting

   enterpriseId - The ID of the enterprise on which to set the members can update protected branches setting.

   settingValue - The value for the members can update protected branches setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput(GQLObject):
   """
   UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput - Autogenerated input type of UpdateEnterpriseMembersCanInviteCollaboratorsSetting

   enterpriseId - The ID of the enterprise on which to set the members can invite collaborators setting.

   settingValue - The value for the members can invite collaborators setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanDeleteIssuesSettingInput(GQLObject):
   """
   UpdateEnterpriseMembersCanDeleteIssuesSettingInput - Autogenerated input type of UpdateEnterpriseMembersCanDeleteIssuesSetting

   enterpriseId - The ID of the enterprise on which to set the members can delete issues setting.

   settingValue - The value for the members can delete issues setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput(GQLObject):
   """
   UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput - Autogenerated input type of UpdateEnterpriseMembersCanChangeRepositoryVisibilitySetting

   enterpriseId - The ID of the enterprise on which to set the members can change repository visibility setting.

   settingValue - The value for the members can change repository visibility setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   clientMutationId: str

class UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput(GQLObject):
   """
   UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput - Autogenerated input type of UpdateEnterpriseAllowPrivateRepositoryForkingSetting

   enterpriseId - The ID of the enterprise on which to set the allow private repository forking setting.

   settingValue - The value for the allow private repository forking setting on the enterprise.

   policyValue - The value for the allow private repository forking policy on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   settingValue: EnterpriseEnabledDisabledSettingValue
   policyValue: EnterpriseAllowPrivateRepositoryForkingPolicyValue
   clientMutationId: str

class UpdateEnterpriseAdministratorRoleInput(GQLObject):
   """
   UpdateEnterpriseAdministratorRoleInput - Autogenerated input type of UpdateEnterpriseAdministratorRole

   enterpriseId - The ID of the Enterprise which the admin belongs to.

   login - The login of a administrator whose role is being changed.

   role - The new role for the Enterprise administrator.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   login: str
   role: EnterpriseAdministratorRole
   clientMutationId: str

class UpdateDiscussionCommentInput(GQLObject):
   """
   UpdateDiscussionCommentInput - Autogenerated input type of UpdateDiscussionComment

   commentId - The Node ID of the discussion comment to update.

   body - The new contents of the comment body.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   commentId: ID
   body: str
   clientMutationId: str

class Updatable(GQLObject):
   """
   Updatable - Entities that can be updated.

   viewerCanUpdate - Check if the current viewer can update this object.

   """
   viewerCanUpdate: bool

class UnpinIssueInput(GQLObject):
   """
   UnpinIssueInput - Autogenerated input type of UnpinIssue

   issueId - The ID of the issue to be unpinned

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID
   clientMutationId: str

class UnmarkProjectV2AsTemplateInput(GQLObject):
   """
   UnmarkProjectV2AsTemplateInput - Autogenerated input type of UnmarkProjectV2AsTemplate

   projectId - The ID of the Project to unmark as a template.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   clientMutationId: str

class UnmarkFileAsViewedInput(GQLObject):
   """
   UnmarkFileAsViewedInput - Autogenerated input type of UnmarkFileAsViewed

   pullRequestId - The Node ID of the pull request.

   path - The path of the file to mark as unviewed

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   path: str
   clientMutationId: str

class UnlockLockableInput(GQLObject):
   """
   UnlockLockableInput - Autogenerated input type of UnlockLockable

   lockableId - ID of the item to be unlocked.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   lockableId: ID
   clientMutationId: str

class UnlinkProjectV2FromTeamInput(GQLObject):
   """
   UnlinkProjectV2FromTeamInput - Autogenerated input type of UnlinkProjectV2FromTeam

   projectId - The ID of the project to unlink from the team.

   teamId - The ID of the team to unlink from the project.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   teamId: ID
   clientMutationId: str

class UniformResourceLocatable(GQLObject):
   """
   UniformResourceLocatable - Represents a type that can be retrieved by a URL.

   resourcePath - The HTML path to this resource.

   url - The URL to this resource.

   """
   resourcePath: URI
   url: URI

class UnfollowOrganizationInput(GQLObject):
   """
   UnfollowOrganizationInput - Autogenerated input type of UnfollowOrganization

   organizationId - ID of the organization to unfollow.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID
   clientMutationId: str

class UnarchiveProjectV2ItemInput(GQLObject):
   """
   UnarchiveProjectV2ItemInput - Autogenerated input type of UnarchiveProjectV2Item

   projectId - The ID of the Project to archive the item from.

   itemId - The ID of the ProjectV2Item to unarchive.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   itemId: ID
   clientMutationId: str

class TransferEnterpriseOrganizationInput(GQLObject):
   """
   TransferEnterpriseOrganizationInput - Autogenerated input type of TransferEnterpriseOrganization

   organizationId - The ID of the organization to transfer.

   destinationEnterpriseId - The ID of the enterprise where the organization should be transferred.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID
   destinationEnterpriseId: ID
   clientMutationId: str

class TeamRepositoryOrder(GQLObject):
   """
   TeamRepositoryOrder - Ordering options for team repository connections

   field - The field to order repositories by.

   direction - The ordering direction.

   """
   field: TeamRepositoryOrderField
   direction: OrderDirection

class TeamMemberOrder(GQLObject):
   """
   TeamMemberOrder - Ordering options for team member connections

   field - The field to order team members by.

   direction - The ordering direction.

   """
   field: TeamMemberOrderField
   direction: OrderDirection

class TeamDiscussionCommentOrder(GQLObject):
   """
   TeamDiscussionCommentOrder - Ways in which team discussion comment connections can be ordered.

   field - The field by which to order nodes.

   direction - The direction in which to order nodes.

   """
   field: TeamDiscussionCommentOrderField
   direction: OrderDirection

class TagNamePatternParameters(GQLObject):
   """
   TagNamePatternParameters - Parameters to be used for the tag_name_pattern rule

   name - How this rule will appear to users.

   negate - If true, the rule will fail if the pattern matches.

   operator - The operator to use for matching.

   pattern - The pattern to match with.

   """
   name: str
   negate: bool
   operator: str
   pattern: str

class Subscribable(GQLObject):
   """
   Subscribable - Entities that can be subscribed to for web and email notifications.

   viewerCanSubscribe - Check if the viewer is able to change their subscription status for the repository.

   viewerSubscription - Identifies if the viewer is watching, not watching, or ignoring the subscribable entity.

   """
   id: ID
   viewerCanSubscribe: bool
   viewerSubscription: SubscriptionState

class SubmitPullRequestReviewInput(GQLObject):
   """
   SubmitPullRequestReviewInput - Autogenerated input type of SubmitPullRequestReview

   pullRequestId - The Pull Request ID to submit any pending reviews.

   pullRequestReviewId - The Pull Request Review ID to submit.

   event - The event to send to the Pull Request Review.

   body - The text field to set on the Pull Request Review.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   pullRequestReviewId: ID
   event: PullRequestReviewEvent
   body: str
   clientMutationId: str

class StatusCheckConfigurationInput(GQLObject):
   """
   StatusCheckConfigurationInput - Required status check

   context - The status check context name that must be present on the commit.

   integrationId - The optional integration ID that this status check must originate from.

   """
   context: str
   integrationId: int

class StartRepositoryMigrationInput(GQLObject):
   """
   StartRepositoryMigrationInput - Autogenerated input type of StartRepositoryMigration

   sourceId - The ID of the migration source.

   ownerId - The ID of the organization that will own the imported repository.

   sourceRepositoryUrl - The URL of the source repository.

   repositoryName - The name of the imported repository.

   continueOnError - Whether to continue the migration on error. Defaults to `false`. We strongly recommend setting this to `true` for the smoothest migration experience. *This default will change to `true` on September 4, 2023.*

   gitArchiveUrl - The signed URL to access the user-uploaded git archive.

   metadataArchiveUrl - The signed URL to access the user-uploaded metadata archive.

   accessToken - The migration source access token.

   githubPat - The GitHub personal access token of the user importing to the target repository.

   skipReleases - Whether to skip migrating releases for the repository.

   targetRepoVisibility - The visibility of the imported repository.

   lockSource - Whether to lock the source repository.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   sourceId: ID
   ownerId: ID
   sourceRepositoryUrl: URI
   repositoryName: str
   continueOnError: bool
   gitArchiveUrl: str
   metadataArchiveUrl: str
   accessToken: str
   githubPat: str
   skipReleases: bool
   targetRepoVisibility: str
   lockSource: bool
   clientMutationId: str

class StarOrder(GQLObject):
   """
   StarOrder - Ways in which star connections can be ordered.

   field - The field in which to order nodes by.

   direction - The direction in which to order nodes.

   """
   field: StarOrderField
   direction: OrderDirection

class SponsorshipNewsletterOrder(GQLObject):
   """
   SponsorshipNewsletterOrder - Ordering options for sponsorship newsletter connections.

   field - The field to order sponsorship newsletters by.

   direction - The ordering direction.

   """
   field: SponsorshipNewsletterOrderField
   direction: OrderDirection

class SponsorsGoal(GQLObject):
   """
   SponsorsGoal - A goal associated with a GitHub Sponsors listing, representing a target the sponsored maintainer would like to attain.

   description - A description of the goal from the maintainer.

   kind - What the objective of this goal is.

   percentComplete - The percentage representing how complete this goal is, between 0-100.

   targetValue - What the goal amount is. Represents an amount in USD for monthly sponsorship amount goals. Represents a count of unique sponsors for total sponsors count goals.

   title - A brief summary of the kind and target value of this goal.

   """
   description: str
   kind: SponsorsGoalKind
   percentComplete: int
   targetValue: int
   title: str

class SponsorableOrder(GQLObject):
   """
   SponsorableOrder - Ordering options for connections to get sponsorable entities for GitHub Sponsors.

   field - The field to order sponsorable entities by.

   direction - The ordering direction.

   """
   field: SponsorableOrderField
   direction: OrderDirection

class SocialAccount(GQLObject):
   """
   SocialAccount - Social media profile associated with a user.

   displayName - Name of the social media account as it appears on the profile.

   provider - Software or company that hosts the social media account.

   url - URL of the social media account.

   """
   displayName: str
   provider: SocialAccountProvider
   url: URI

class SetRepositoryInteractionLimitInput(GQLObject):
   """
   SetRepositoryInteractionLimitInput - Autogenerated input type of SetRepositoryInteractionLimit

   repositoryId - The ID of the repository to set a limit for.

   limit - The limit to set.

   expiry - When this limit should expire.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   limit: RepositoryInteractionLimit
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SetEnterpriseIdentityProviderInput(GQLObject):
   """
   SetEnterpriseIdentityProviderInput - Autogenerated input type of SetEnterpriseIdentityProvider

   enterpriseId - The ID of the enterprise on which to set an identity provider.

   ssoUrl - The URL endpoint for the identity provider's SAML SSO.

   issuer - The Issuer Entity ID for the SAML identity provider

   idpCertificate - The x509 certificate used by the identity provider to sign assertions and responses.

   signatureMethod - The signature algorithm used to sign SAML requests for the identity provider.

   digestMethod - The digest algorithm used to sign SAML requests for the identity provider.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   ssoUrl: URI
   issuer: str
   idpCertificate: str
   signatureMethod: SamlSignatureAlgorithm
   digestMethod: SamlDigestAlgorithm
   clientMutationId: str

class SecurityAdvisoryReference(GQLObject):
   """
   SecurityAdvisoryReference - A GitHub Security Advisory Reference

   url - A publicly accessible reference

   """
   url: URI

class SecurityAdvisoryPackage(GQLObject):
   """
   SecurityAdvisoryPackage - An individual package

   ecosystem - The ecosystem the package belongs to, e.g. RUBYGEMS, NPM

   name - The package name

   """
   ecosystem: SecurityAdvisoryEcosystem
   name: str

class SecurityAdvisoryIdentifierFilter(GQLObject):
   """
   SecurityAdvisoryIdentifierFilter - An advisory identifier to filter results on.

   type - The identifier type.

   value - The identifier string. Supports exact or partial matching.

   """
   type: SecurityAdvisoryIdentifierType
   value: str

class SavedReplyOrder(GQLObject):
   """
   SavedReplyOrder - Ordering options for saved reply connections.

   field - The field to order saved replies by.

   direction - The ordering direction.

   """
   field: SavedReplyOrderField
   direction: OrderDirection

class RevokeMigratorRoleInput(GQLObject):
   """
   RevokeMigratorRoleInput - Autogenerated input type of RevokeMigratorRole

   organizationId - The ID of the organization that the user/team belongs to.

   actor - The user login or Team slug to revoke the migrator role from.

   actorType - Specifies the type of the actor, can be either USER or TEAM.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID
   actor: str
   actorType: ActorType
   clientMutationId: str

class ReviewStatusHovercardContext(GQLObject):
   """
   ReviewStatusHovercardContext - A hovercard context with a message describing the current code review state of the pull
request.


   message - A string describing this context

   octicon - An octicon to accompany this context

   reviewDecision - The current status of the pull request with respect to code review.

   """
   message: str
   octicon: str
   reviewDecision: PullRequestReviewDecision

class RetireSponsorsTierInput(GQLObject):
   """
   RetireSponsorsTierInput - Autogenerated input type of RetireSponsorsTier

   tierId - The ID of the published tier to retire.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   tierId: ID
   clientMutationId: str

class RerequestCheckSuiteInput(GQLObject):
   """
   RerequestCheckSuiteInput - Autogenerated input type of RerequestCheckSuite

   repositoryId - The Node ID of the repository.

   checkSuiteId - The Node ID of the check suite.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   checkSuiteId: ID
   clientMutationId: str

class RequiredDeploymentsParametersInput(GQLObject):
   """
   RequiredDeploymentsParametersInput - Choose which environments must be successfully deployed to before branches can be merged into a branch that matches this rule.

   requiredDeploymentEnvironments - The environments that must be successfully deployed to before branches can be merged.

   """
   requiredDeploymentEnvironments: list[str]

class OGACT_isRequired_Field(ArguedBool):
   """
   OGACT_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class RequestReviewsInput(GQLObject):
   """
   RequestReviewsInput - Autogenerated input type of RequestReviews

   pullRequestId - The Node ID of the pull request to modify.

   userIds - The Node IDs of the user to request.

   teamIds - The Node IDs of the team to request.

   union - Add users to the set rather than replace.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   userIds: list[ID]
   teamIds: list[ID]
   union: bool
   clientMutationId: str

class RepositoryOrder(GQLObject):
   """
   RepositoryOrder - Ordering options for repository connections

   field - The field to order repositories by.

   direction - The ordering direction.

   """
   field: RepositoryOrderField
   direction: OrderDirection

class RepositoryNameConditionTarget(GQLObject):
   """
   RepositoryNameConditionTarget - Parameters to be used for the repository_name condition

   exclude - Array of repository names or patterns to exclude. The condition will not pass if any of these patterns match.

   include - Array of repository names or patterns to include. One of these patterns must match for the condition to pass. Also accepts `~ALL` to include all repositories.

   protected - Target changes that match these patterns will be prevented except by those with bypass permissions.

   """
   exclude: list[str]
   include: list[str]
   protected: bool

class RepositoryInvitationOrder(GQLObject):
   """
   RepositoryInvitationOrder - Ordering options for repository invitation connections.

   field - The field to order repository invitations by.

   direction - The ordering direction.

   """
   field: RepositoryInvitationOrderField
   direction: OrderDirection

class RepositoryIdConditionTargetInput(GQLObject):
   """
   RepositoryIdConditionTargetInput - Parameters to be used for the repository_id condition

   repositoryIds - One of these repo IDs must match the repo.

   """
   repositoryIds: list[ID]

class RepositoryContactLink(GQLObject):
   """
   RepositoryContactLink - A repository contact link.

   about - The contact link purpose.

   name - The contact link name.

   url - The contact link URL.

   """
   about: str
   name: str
   url: URI

class ReopenPullRequestInput(GQLObject):
   """
   ReopenPullRequestInput - Autogenerated input type of ReopenPullRequest

   pullRequestId - ID of the pull request to be reopened.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   clientMutationId: str

class ReopenDiscussionInput(GQLObject):
   """
   ReopenDiscussionInput - Autogenerated input type of ReopenDiscussion

   discussionId - ID of the discussion to be reopened.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   discussionId: ID
   clientMutationId: str

class RemoveStarInput(GQLObject):
   """
   RemoveStarInput - Autogenerated input type of RemoveStar

   starrableId - The Starrable ID to unstar.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   starrableId: ID
   clientMutationId: str

class RemoveOutsideCollaboratorInput(GQLObject):
   """
   RemoveOutsideCollaboratorInput - Autogenerated input type of RemoveOutsideCollaborator

   userId - The ID of the outside collaborator to remove.

   organizationId - The ID of the organization to remove the outside collaborator from.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   userId: ID
   organizationId: ID
   clientMutationId: str

class RemoveEnterpriseSupportEntitlementPayload(GQLObject):
   """
   RemoveEnterpriseSupportEntitlementPayload - Autogenerated return type of RemoveEnterpriseSupportEntitlement

   clientMutationId - A unique identifier for the client performing the mutation.

   message - A message confirming the result of removing the support entitlement.

   """
   clientMutationId: str
   message: str

class RemoveEnterpriseOrganizationInput(GQLObject):
   """
   RemoveEnterpriseOrganizationInput - Autogenerated input type of RemoveEnterpriseOrganization

   enterpriseId - The ID of the enterprise from which the organization should be removed.

   organizationId - The ID of the organization to remove from the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   organizationId: ID
   clientMutationId: str

class RemoveEnterpriseIdentityProviderInput(GQLObject):
   """
   RemoveEnterpriseIdentityProviderInput - Autogenerated input type of RemoveEnterpriseIdentityProvider

   enterpriseId - The ID of the enterprise from which to remove the identity provider.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   clientMutationId: str

class RemoveAssigneesFromAssignableInput(GQLObject):
   """
   RemoveAssigneesFromAssignableInput - Autogenerated input type of RemoveAssigneesFromAssignable

   assignableId - The id of the assignable object to remove assignees from.

   assigneeIds - The id of users to remove as assignees.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   assignableId: ID
   assigneeIds: list[ID]
   clientMutationId: str

class RejectDeploymentsInput(GQLObject):
   """
   RejectDeploymentsInput - Autogenerated input type of RejectDeployments

   workflowRunId - The node ID of the workflow run containing the pending deployments.

   environmentIds - The ids of environments to reject deployments

   comment - Optional comment for rejecting deployments

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   workflowRunId: ID
   environmentIds: list[ID]
   comment: str
   clientMutationId: str

class RegenerateVerifiableDomainTokenInput(GQLObject):
   """
   RegenerateVerifiableDomainTokenInput - Autogenerated input type of RegenerateVerifiableDomainToken

   id - The ID of the verifiable domain to regenerate the verification token of.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class RefUpdateRule(GQLObject):
   """
   RefUpdateRule - A ref update rules for a viewer.

   allowsDeletions - Can this branch be deleted.

   allowsForcePushes - Are force pushes allowed on this branch.

   blocksCreations - Can matching branches be created.

   pattern - Identifies the protection rule pattern.

   requiredApprovingReviewCount - Number of approving reviews required to update matching branches.

   requiredStatusCheckContexts - List of required status check contexts that must pass for commits to be accepted to matching branches.

   requiresCodeOwnerReviews - Are reviews from code owners required to update matching branches.

   requiresConversationResolution - Are conversations required to be resolved before merging.

   requiresLinearHistory - Are merge commits prohibited from being pushed to this branch.

   requiresSignatures - Are commits required to be signed.

   viewerAllowedToDismissReviews - Is the viewer allowed to dismiss reviews.

   viewerCanPush - Can the viewer push to the branch

   """
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

class RefNameConditionTargetInput(GQLObject):
   """
   RefNameConditionTargetInput - Parameters to be used for the ref_name condition

   exclude - Array of ref names or patterns to exclude. The condition will not pass if any of these patterns match.

   include - Array of ref names or patterns to include. One of these patterns must match for the condition to pass. Also accepts `~DEFAULT_BRANCH` to include the default branch or `~ALL` to include all branches.

   """
   exclude: list[str]
   include: list[str]

class ReactionOrder(GQLObject):
   """
   ReactionOrder - Ways in which lists of reactions can be ordered upon return.

   field - The field in which to order reactions by.

   direction - The direction in which to order reactions by the specified field.

   """
   field: ReactionOrderField
   direction: OrderDirection

class PullRequestParametersInput(GQLObject):
   """
   PullRequestParametersInput - Require all commits be made to a non-target branch and submitted via a pull request before they can be merged.

   dismissStaleReviewsOnPush - New, reviewable commits pushed will dismiss previous pull request review approvals.

   requireCodeOwnerReview - Require an approving review in pull requests that modify files that have a designated code owner.

   requireLastPushApproval - Whether the most recent reviewable push must be approved by someone other than the person who pushed it.

   requiredApprovingReviewCount - The number of approving reviews that are required before a pull request can be merged.

   requiredReviewThreadResolution - All conversations on code must be resolved before a pull request can be merged.

   """
   dismissStaleReviewsOnPush: bool
   requireCodeOwnerReview: bool
   requireLastPushApproval: bool
   requiredApprovingReviewCount: int
   requiredReviewThreadResolution: bool

class PullRequestOrder(GQLObject):
   """
   PullRequestOrder - Ways in which lists of issues can be ordered upon return.

   field - The field in which to order pull requests by.

   direction - The direction in which to order pull requests by the specified field.

   """
   field: PullRequestOrderField
   direction: OrderDirection

class PublishSponsorsTierInput(GQLObject):
   """
   PublishSponsorsTierInput - Autogenerated input type of PublishSponsorsTier

   tierId - The ID of the draft tier to publish.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   tierId: ID
   clientMutationId: str

class ProjectV2WorkflowOrder(GQLObject):
   """
   ProjectV2WorkflowOrder - Ordering options for project v2 workflows connections

   field - The field to order the project v2 workflows by.

   direction - The ordering direction.

   """
   field: ProjectV2WorkflowsOrderField
   direction: OrderDirection

class ProjectV2SingleSelectFieldOptionInput(GQLObject):
   """
   ProjectV2SingleSelectFieldOptionInput - Represents a single select field option

   name - The name of the option

   color - The display color of the option

   description - The description text of the option

   """
   name: str
   color: ProjectV2SingleSelectFieldOptionColor
   description: str

class ProjectV2Order(GQLObject):
   """
   ProjectV2Order - Ways in which lists of projects can be ordered upon return.

   field - The field in which to order projects by.

   direction - The direction in which to order projects by the specified field.

   """
   field: ProjectV2OrderField
   direction: OrderDirection

class ProjectV2ItemOrder(GQLObject):
   """
   ProjectV2ItemOrder - Ordering options for project v2 item connections

   field - The field to order the project v2 items by.

   direction - The ordering direction.

   """
   field: ProjectV2ItemOrderField
   direction: OrderDirection

class ProjectV2Filters(GQLObject):
   """
   ProjectV2Filters - Ways in which to filter lists of projects.

   state - List project v2 filtered by the state given.

   """
   state: ProjectV2State

class ProjectV2FieldOrder(GQLObject):
   """
   ProjectV2FieldOrder - Ordering options for project v2 field connections

   field - The field to order the project v2 fields by.

   direction - The ordering direction.

   """
   field: ProjectV2FieldOrderField
   direction: OrderDirection

class ProjectProgress(GQLObject):
   """
   ProjectProgress - Project progress stats.

   doneCount - The number of done cards.

   donePercentage - The percentage of done cards.

   enabled - Whether progress tracking is enabled and cards with purpose exist for this project

   inProgressCount - The number of in-progress cards.

   inProgressPercentage - The percentage of in-progress cards.

   todoCount - The number of to do cards.

   todoPercentage - The percentage of to do cards.

   """
   doneCount: int
   donePercentage: float
   enabled: bool
   inProgressCount: int
   inProgressPercentage: float
   todoCount: int
   todoPercentage: float

class PinIssueInput(GQLObject):
   """
   PinIssueInput - Autogenerated input type of PinIssue

   issueId - The ID of the issue to be pinned

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID
   clientMutationId: str

class PackageVersionStatistics(GQLObject):
   """
   PackageVersionStatistics - Represents a object that contains package version activity statistics such as downloads.

   downloadsTotalCount - Number of times the package was downloaded since it was created.

   """
   downloadsTotalCount: int

class PackageStatistics(GQLObject):
   """
   PackageStatistics - Represents a object that contains package activity statistics such as downloads.

   downloadsTotalCount - Number of times the package was downloaded since it was created.

   """
   downloadsTotalCount: int

class PackageFileOrder(GQLObject):
   """
   PackageFileOrder - Ways in which lists of package files can be ordered upon return.

   field - The field in which to order package files by.

   direction - The direction in which to order package files by the specified field.

   """
   field: PackageFileOrderField
   direction: OrderDirection

class OrganizationMigration(GQLObject):
   """
   OrganizationMigration - A GitHub Enterprise Importer (GEI) organization migration.

   createdAt - Identifies the date and time when the object was created.

   databaseId - Identifies the primary key from the database.

   failureReason - The reason the organization migration failed.

   remainingRepositoriesCount - The remaining amount of repos to be migrated.

   sourceOrgName - The name of the source organization to be migrated.

   sourceOrgUrl - The URL of the source organization to migrate.

   state - The migration state.

   targetOrgName - The name of the target organization.

   totalRepositoriesCount - The total amount of repositories to be migrated.

   """
   createdAt: DateTime
   databaseId: str
   failureReason: str
   id: ID
   remainingRepositoriesCount: int
   sourceOrgName: str
   sourceOrgUrl: URI
   state: OrganizationMigrationState
   targetOrgName: str
   totalRepositoriesCount: int

class OauthApplicationAuditEntryData(GQLObject):
   """
   OauthApplicationAuditEntryData - Metadata for an audit entry with action oauth_application.*

   oauthApplicationName - The name of the OAuth application.

   oauthApplicationResourcePath - The HTTP path for the OAuth application

   oauthApplicationUrl - The HTTP URL for the OAuth application

   """
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI

class MoveProjectColumnInput(GQLObject):
   """
   MoveProjectColumnInput - Autogenerated input type of MoveProjectColumn

   columnId - The id of the column to move.

   afterColumnId - Place the new column after the column with this id. Pass null to place it at the front.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   columnId: ID
   afterColumnId: ID
   clientMutationId: str

class MinimizeCommentInput(GQLObject):
   """
   MinimizeCommentInput - Autogenerated input type of MinimizeComment

   subjectId - The Node ID of the subject to modify.

   classifier - The classification of comment

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID
   classifier: ReportedContentClassifiers
   clientMutationId: str

class MilestoneOrder(GQLObject):
   """
   MilestoneOrder - Ordering options for milestone connections.

   field - The field to order milestones by.

   direction - The ordering direction.

   """
   field: MilestoneOrderField
   direction: OrderDirection

class MergeQueueConfiguration(GQLObject):
   """
   MergeQueueConfiguration - Configuration for a MergeQueue

   checkResponseTimeout - The amount of time in minutes to wait for a check response before considering it a failure.

   maximumEntriesToBuild - The maximum number of entries to build at once.

   maximumEntriesToMerge - The maximum number of entries to merge at once.

   mergeMethod - The merge method to use for this queue.

   mergingStrategy - The strategy to use when merging entries.

   minimumEntriesToMerge - The minimum number of entries required to merge at once.

   minimumEntriesToMergeWaitTime - The amount of time in minutes to wait before ignoring the minumum number of entries in the queue requirement and merging a collection of entries

   """
   checkResponseTimeout: int
   maximumEntriesToBuild: int
   maximumEntriesToMerge: int
   mergeMethod: PullRequestMergeMethod
   mergingStrategy: MergeQueueMergingStrategy
   minimumEntriesToMerge: int
   minimumEntriesToMergeWaitTime: int

class MergeBranchInput(GQLObject):
   """
   MergeBranchInput - Autogenerated input type of MergeBranch

   repositoryId - The Node ID of the Repository containing the base branch that will be modified.

   base - The name of the base branch that the provided head will be merged into.

   head - The head to merge into the base branch. This can be a branch name or a commit GitObjectID.

   commitMessage - Message to use for the merge commit. If omitted, a default will be used.

   authorEmail - The email address to associate with this commit.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   base: str
   head: str
   commitMessage: str
   authorEmail: str
   clientMutationId: str

class MarkPullRequestReadyForReviewInput(GQLObject):
   """
   MarkPullRequestReadyForReviewInput - Autogenerated input type of MarkPullRequestReadyForReview

   pullRequestId - ID of the pull request to be marked as ready for review.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   clientMutationId: str

class MarkFileAsViewedInput(GQLObject):
   """
   MarkFileAsViewedInput - Autogenerated input type of MarkFileAsViewed

   pullRequestId - The Node ID of the pull request.

   path - The path of the file to mark as viewed

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   path: str
   clientMutationId: str

class MannequinOrder(GQLObject):
   """
   MannequinOrder - Ordering options for mannequins.

   field - The field to order mannequins by.

   direction - The ordering direction.

   """
   field: MannequinOrderField
   direction: OrderDirection

class LockLockableInput(GQLObject):
   """
   LockLockableInput - Autogenerated input type of LockLockable

   lockableId - ID of the item to be locked.

   lockReason - A reason for why the item will be locked.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   lockableId: ID
   lockReason: LockReason
   clientMutationId: str

class LinkProjectV2ToTeamInput(GQLObject):
   """
   LinkProjectV2ToTeamInput - Autogenerated input type of LinkProjectV2ToTeam

   projectId - The ID of the project to link to the team.

   teamId - The ID of the team to link to the project.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   teamId: ID
   clientMutationId: str

class LicenseRule(GQLObject):
   """
   LicenseRule - Describes a License's conditions, permissions, and limitations

   description - A description of the rule

   key - The machine-readable rule key

   label - The human-readable rule label

   """
   description: str
   key: str
   label: str

class Language(GQLObject):
   """
   Language - Represents a given language found in repositories.

   color - The color defined for the current language.

   name - The name of the current language.

   """
   color: str
   id: ID
   name: str

class IssueOrder(GQLObject):
   """
   IssueOrder - Ways in which lists of issues can be ordered upon return.

   field - The field in which to order issues by.

   direction - The direction in which to order issues by the specified field.

   """
   field: IssueOrderField
   direction: OrderDirection

class IssueCommentOrder(GQLObject):
   """
   IssueCommentOrder - Ways in which lists of issue comments can be ordered upon return.

   field - The field in which to order issue comments by.

   direction - The direction in which to order issue comments by the specified field.

   """
   field: IssueCommentOrderField
   direction: OrderDirection

class InviteEnterpriseAdminInput(GQLObject):
   """
   InviteEnterpriseAdminInput - Autogenerated input type of InviteEnterpriseAdmin

   enterpriseId - The ID of the enterprise to which you want to invite an administrator.

   invitee - The login of a user to invite as an administrator.

   email - The email of the person to invite as an administrator.

   role - The role of the administrator.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   invitee: str
   email: str
   role: EnterpriseAdministratorRole
   clientMutationId: str

class GrantMigratorRolePayload(GQLObject):
   """
   GrantMigratorRolePayload - Autogenerated return type of GrantMigratorRole

   clientMutationId - A unique identifier for the client performing the mutation.

   success - Did the operation succeed?

   """
   clientMutationId: str
   success: bool

class GrantEnterpriseOrganizationsMigratorRoleInput(GQLObject):
   """
   GrantEnterpriseOrganizationsMigratorRoleInput - Autogenerated input type of GrantEnterpriseOrganizationsMigratorRole

   enterpriseId - The ID of the enterprise to which all organizations managed by it will be granted the migrator role.

   login - The login of the user to grant the migrator role

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   login: str
   clientMutationId: str

class GistOrder(GQLObject):
   """
   GistOrder - Ordering options for gist connections

   field - The field to order repositories by.

   direction - The ordering direction.

   """
   field: GistOrderField
   direction: OrderDirection

class FundingLink(GQLObject):
   """
   FundingLink - A funding platform link for a repository.

   platform - The funding platform this link is for.

   url - The configured URL for this funding link.

   """
   platform: FundingPlatform
   url: URI

class FollowOrganizationInput(GQLObject):
   """
   FollowOrganizationInput - Autogenerated input type of FollowOrganization

   organizationId - ID of the organization to follow.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID
   clientMutationId: str

class FileAddition(GQLObject):
   """
   FileAddition - A command to add a file at the given path with the given contents as part of a commit.  Any existing file at that that path will be replaced.

   path - The path in the repository where the file will be located

   contents - The base64 encoded contents of the file

   """
   path: str
   contents: Base64String

class Environments(GQLObject):
   """
   Environments - Ordering options for environments

   field - The field to order environments by.

   direction - The direction in which to order environments by the specified field.

   """
   field: EnvironmentOrderField
   direction: OrderDirection

class EnterpriseServerUserAccountOrder(GQLObject):
   """
   EnterpriseServerUserAccountOrder - Ordering options for Enterprise Server user account connections.

   field - The field to order user accounts by.

   direction - The ordering direction.

   """
   field: EnterpriseServerUserAccountOrderField
   direction: OrderDirection

class EnterpriseServerInstallationOrder(GQLObject):
   """
   EnterpriseServerInstallationOrder - Ordering options for Enterprise Server installation connections.

   field - The field to order Enterprise Server installations by.

   direction - The ordering direction.

   """
   field: EnterpriseServerInstallationOrderField
   direction: OrderDirection

class EnterpriseMemberOrder(GQLObject):
   """
   EnterpriseMemberOrder - Ordering options for enterprise member connections.

   field - The field to order enterprise members by.

   direction - The ordering direction.

   """
   field: EnterpriseMemberOrderField
   direction: OrderDirection

class EnterpriseAuditEntryData(GQLObject):
   """
   EnterpriseAuditEntryData - Metadata for an audit entry containing enterprise account information.

   enterpriseResourcePath - The HTTP path for this enterprise.

   enterpriseSlug - The slug of the enterprise.

   enterpriseUrl - The HTTP URL for this enterprise.

   """
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI

class EnqueuePullRequestInput(GQLObject):
   """
   EnqueuePullRequestInput - Autogenerated input type of EnqueuePullRequest

   pullRequestId - The ID of the pull request to enqueue.

   jump - Add the pull request to the front of the queue.

   expectedHeadOid - The expected head OID of the pull request.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   jump: bool
   expectedHeadOid: GitObjectID
   clientMutationId: str

class DraftPullRequestReviewThread(GQLObject):
   """
   DraftPullRequestReviewThread - Specifies a review comment thread to be left with a Pull Request Review.

   path - Path to the file being commented on.

   line - The line of the blob to which the thread refers. The end of the line range for multi-line comments.

   side - The side of the diff on which the line resides. For multi-line comments, this is the side for the end of the line range.

   startLine - The first line of the range to which the comment refers.

   startSide - The side of the diff on which the start line resides.

   body - Body of the comment to leave.

   """
   path: str
   line: int
   side: DiffSide
   startLine: int
   startSide: DiffSide
   body: str

class DismissRepositoryVulnerabilityAlertInput(GQLObject):
   """
   DismissRepositoryVulnerabilityAlertInput - Autogenerated input type of DismissRepositoryVulnerabilityAlert

   repositoryVulnerabilityAlertId - The Dependabot alert ID to dismiss.

   dismissReason - The reason the Dependabot alert is being dismissed.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryVulnerabilityAlertId: ID
   dismissReason: DismissReason
   clientMutationId: str

class DiscussionPollOptionOrder(GQLObject):
   """
   DiscussionPollOptionOrder - Ordering options for discussion poll option connections.

   field - The field to order poll options by.

   direction - The ordering direction.

   """
   field: DiscussionPollOptionOrderField
   direction: OrderDirection

class DisablePullRequestAutoMergeInput(GQLObject):
   """
   DisablePullRequestAutoMergeInput - Autogenerated input type of DisablePullRequestAutoMerge

   pullRequestId - ID of the pull request to disable auto merge on.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   clientMutationId: str

class DeploymentOrder(GQLObject):
   """
   DeploymentOrder - Ordering options for deployment connections

   field - The field to order deployments by.

   direction - The ordering direction.

   """
   field: DeploymentOrderField
   direction: OrderDirection

class DependabotUpdateError(GQLObject):
   """
   DependabotUpdateError - An error produced from a Dependabot Update

   body - The body of the error

   errorType - The error code

   title - The title of the error

   """
   body: str
   errorType: str
   title: str

class DeleteTeamDiscussionPayload(GQLObject):
   """
   DeleteTeamDiscussionPayload - Autogenerated return type of DeleteTeamDiscussion

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   clientMutationId: str

class DeleteTeamDiscussionCommentPayload(GQLObject):
   """
   DeleteTeamDiscussionCommentPayload - Autogenerated return type of DeleteTeamDiscussionComment

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   clientMutationId: str

class DeleteRepositoryRulesetPayload(GQLObject):
   """
   DeleteRepositoryRulesetPayload - Autogenerated return type of DeleteRepositoryRuleset

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   clientMutationId: str

class DeleteRefPayload(GQLObject):
   """
   DeleteRefPayload - Autogenerated return type of DeleteRef

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   clientMutationId: str

class DeletePullRequestReviewInput(GQLObject):
   """
   DeletePullRequestReviewInput - Autogenerated input type of DeletePullRequestReview

   pullRequestReviewId - The Node ID of the pull request review to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestReviewId: ID
   clientMutationId: str

class DeleteProjectV2WorkflowInput(GQLObject):
   """
   DeleteProjectV2WorkflowInput - Autogenerated input type of DeleteProjectV2Workflow

   workflowId - The ID of the workflow to be removed.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   workflowId: ID
   clientMutationId: str

class DeleteProjectV2ItemInput(GQLObject):
   """
   DeleteProjectV2ItemInput - Autogenerated input type of DeleteProjectV2Item

   projectId - The ID of the Project from which the item should be removed.

   itemId - The ID of the item to be removed.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   itemId: ID
   clientMutationId: str

class DeleteProjectV2FieldInput(GQLObject):
   """
   DeleteProjectV2FieldInput - Autogenerated input type of DeleteProjectV2Field

   fieldId - The ID of the field to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   fieldId: ID
   clientMutationId: str

class DeleteProjectColumnInput(GQLObject):
   """
   DeleteProjectColumnInput - Autogenerated input type of DeleteProjectColumn

   columnId - The id of the column to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   columnId: ID
   clientMutationId: str

class DeleteLinkedBranchInput(GQLObject):
   """
   DeleteLinkedBranchInput - Autogenerated input type of DeleteLinkedBranch

   linkedBranchId - The ID of the linked branch

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   linkedBranchId: ID
   clientMutationId: str

class DeleteIssueCommentPayload(GQLObject):
   """
   DeleteIssueCommentPayload - Autogenerated return type of DeleteIssueComment

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   clientMutationId: str

class DeleteIpAllowListEntryInput(GQLObject):
   """
   DeleteIpAllowListEntryInput - Autogenerated input type of DeleteIpAllowListEntry

   ipAllowListEntryId - The ID of the IP allow list entry to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ipAllowListEntryId: ID
   clientMutationId: str

class DeleteEnvironmentInput(GQLObject):
   """
   DeleteEnvironmentInput - Autogenerated input type of DeleteEnvironment

   id - The Node ID of the environment to be deleted.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class DeleteDiscussionCommentInput(GQLObject):
   """
   DeleteDiscussionCommentInput - Autogenerated input type of DeleteDiscussionComment

   id - The Node id of the discussion comment to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class DeleteDeploymentInput(GQLObject):
   """
   DeleteDeploymentInput - Autogenerated input type of DeleteDeployment

   id - The Node ID of the deployment to be deleted.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class DeleteBranchProtectionRuleInput(GQLObject):
   """
   DeleteBranchProtectionRuleInput - Autogenerated input type of DeleteBranchProtectionRule

   branchProtectionRuleId - The global relay id of the branch protection rule to be deleted.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   branchProtectionRuleId: ID
   clientMutationId: str

class DeclineTopicSuggestionInput(GQLObject):
   """
   DeclineTopicSuggestionInput - Autogenerated input type of DeclineTopicSuggestion

   repositoryId - The Node ID of the repository.

   name - The name of the suggested topic.

   reason - The reason why the suggested topic is declined.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   name: str
   reason: TopicSuggestionDeclineReason
   clientMutationId: str

class CreateTeamDiscussionCommentInput(GQLObject):
   """
   CreateTeamDiscussionCommentInput - Autogenerated input type of CreateTeamDiscussionComment

   discussionId - The ID of the discussion to which the comment belongs. This field is required.

**Upcoming Change on 2024-07-01 UTC**
**Description:** `discussionId` will be removed. Follow the guide at https://github.blog/changelog/2023-02-08-sunset-notice-team-discussions/ to find a suitable replacement.
**Reason:** The Team Discussions feature is deprecated in favor of Organization Discussions.


   body - The content of the comment. This field is required.

**Upcoming Change on 2024-07-01 UTC**
**Description:** `body` will be removed. Follow the guide at https://github.blog/changelog/2023-02-08-sunset-notice-team-discussions/ to find a suitable replacement.
**Reason:** The Team Discussions feature is deprecated in favor of Organization Discussions.


   clientMutationId - A unique identifier for the client performing the mutation.

   """
   discussionId: ID
   body: str
   clientMutationId: str

class CreateSponsorsTierInput(GQLObject):
   """
   CreateSponsorsTierInput - Autogenerated input type of CreateSponsorsTier

   sponsorableId - The ID of the user or organization who owns the GitHub Sponsors profile. Defaults to the current user if omitted and sponsorableLogin is not given.

   sponsorableLogin - The username of the user or organization who owns the GitHub Sponsors profile. Defaults to the current user if omitted and sponsorableId is not given.

   amount - The value of the new tier in US dollars. Valid values: 1-12000.

   isRecurring - Whether sponsorships using this tier should happen monthly/yearly or just once.

   repositoryId - Optional ID of the private repository that sponsors at this tier should gain read-only access to. Must be owned by an organization.

   repositoryOwnerLogin - Optional login of the organization owner of the private repository that sponsors at this tier should gain read-only access to. Necessary if repositoryName is given. Will be ignored if repositoryId is given.

   repositoryName - Optional name of the private repository that sponsors at this tier should gain read-only access to. Must be owned by an organization. Necessary if repositoryOwnerLogin is given. Will be ignored if repositoryId is given.

   welcomeMessage - Optional message new sponsors at this tier will receive.

   description - A description of what this tier is, what perks sponsors might receive, what a sponsorship at this tier means for you, etc.

   publish - Whether to make the tier available immediately for sponsors to choose. Defaults to creating a draft tier that will not be publicly visible.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
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
   """
   CreateRepositoryInput - Autogenerated input type of CreateRepository

   name - The name of the new repository.

   ownerId - The ID of the owner for the new repository.

   description - A short description of the new repository.

   visibility - Indicates the repository's visibility level.

   template - Whether this repository should be marked as a template such that anyone who can access it can create new repositories with the same files and directory structure.

   homepageUrl - The URL for a web page about this repository.

   hasWikiEnabled - Indicates if the repository should have the wiki feature enabled.

   hasIssuesEnabled - Indicates if the repository should have the issues feature enabled.

   teamId - When an organization is specified as the owner, this ID identifies the team that should be granted access to the new repository.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
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
   """
   CreatePullRequestInput - Autogenerated input type of CreatePullRequest

   repositoryId - The Node ID of the repository.

   baseRefName - The name of the branch you want your changes pulled into. This should be an existing branch
on the current repository. You cannot update the base branch on a pull request to point
to another repository.


   headRefName - The name of the branch where your changes are implemented. For cross-repository pull requests
in the same network, namespace `head_ref_name` with a user like this: `username:branch`.


   headRepositoryId - The Node ID of the head repository.

   title - The title of the pull request.

   body - The contents of the pull request.

   maintainerCanModify - Indicates whether maintainers can modify the pull request.

   draft - Indicates whether this pull request should be a draft.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
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
   """
   CreateProjectInput - Autogenerated input type of CreateProject

   ownerId - The owner ID to create the project under.

   name - The name of project.

   body - The description of project.

   template - The name of the GitHub-provided template.

   repositoryIds - A list of repository IDs to create as linked repositories for the project

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID
   name: str
   body: str
   template: ProjectTemplate
   repositoryIds: list[ID]
   clientMutationId: str

class CreateLinkedBranchInput(GQLObject):
   """
   CreateLinkedBranchInput - Autogenerated input type of CreateLinkedBranch

   issueId - ID of the issue to link to.

   oid - The commit SHA to base the new branch on.

   name - The name of the new branch. Defaults to issue number and title.

   repositoryId - ID of the repository to create the branch in. Defaults to the issue repository.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID
   oid: GitObjectID
   name: str
   repositoryId: ID
   clientMutationId: str

class CreateIpAllowListEntryInput(GQLObject):
   """
   CreateIpAllowListEntryInput - Autogenerated input type of CreateIpAllowListEntry

   ownerId - The ID of the owner for which to create the new IP allow list entry.

   allowListValue - An IP address or range of addresses in CIDR notation.

   name - An optional name for the IP allow list entry.

   isActive - Whether the IP allow list entry is active when an IP allow list is enabled.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID
   allowListValue: str
   name: str
   isActive: bool
   clientMutationId: str

class CreateEnterpriseOrganizationInput(GQLObject):
   """
   CreateEnterpriseOrganizationInput - Autogenerated input type of CreateEnterpriseOrganization

   enterpriseId - The ID of the enterprise owning the new organization.

   login - The login of the new organization.

   profileName - The profile name of the new organization.

   billingEmail - The email used for sending billing receipts.

   adminLogins - The logins for the administrators of the new organization.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   login: str
   profileName: str
   billingEmail: str
   adminLogins: list[str]
   clientMutationId: str

class CreateCheckSuiteInput(GQLObject):
   """
   CreateCheckSuiteInput - Autogenerated input type of CreateCheckSuite

   repositoryId - The Node ID of the repository.

   headSha - The SHA of the head commit.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   headSha: GitObjectID
   clientMutationId: str

class CopyProjectV2Input(GQLObject):
   """
   CopyProjectV2Input - Autogenerated input type of CopyProjectV2

   projectId - The ID of the source Project to copy.

   ownerId - The owner ID of the new project.

   title - The title of the project.

   includeDraftIssues - Include draft issues in the new project

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   ownerId: ID
   title: str
   includeDraftIssues: bool
   clientMutationId: str

class ConvertProjectCardNoteToIssueInput(GQLObject):
   """
   ConvertProjectCardNoteToIssueInput - Autogenerated input type of ConvertProjectCardNoteToIssue

   projectCardId - The ProjectCard ID to convert.

   repositoryId - The ID of the repository to create the issue in.

   title - The title of the newly created issue. Defaults to the card's note text.

   body - The body of the newly created issue.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectCardId: ID
   repositoryId: ID
   title: str
   body: str
   clientMutationId: str

class ContributionCalendarMonth(GQLObject):
   """
   ContributionCalendarMonth - A month of contributions in a user's contribution graph.

   firstDay - The date of the first day of this month.

   name - The name of the month.

   totalWeeks - How many weeks started in this month.

   year - The year the month occurred in.

   """
   firstDay: Date
   name: str
   totalWeeks: int
   year: int

class CommitterEmailPatternParametersInput(GQLObject):
   """
   CommitterEmailPatternParametersInput - Parameters to be used for the committer_email_pattern rule

   name - How this rule will appear to users.

   negate - If true, the rule will fail if the pattern matches.

   operator - The operator to use for matching.

   pattern - The pattern to match with.

   """
   name: str
   negate: bool
   operator: str
   pattern: str

class CommittableBranch(GQLObject):
   """
   CommittableBranch - A git ref for a commit to be appended to.

The ref must be a branch, i.e. its fully qualified name must start
with `refs/heads/` (although the input is not required to be fully
qualified).

The Ref may be specified by its global node ID or by the
`repositoryNameWithOwner` and `branchName`.

### Examples

Specify a branch using a global node ID:

    { "id": "MDM6UmVmMTpyZWZzL2hlYWRzL21haW4=" }

Specify a branch using `repositoryNameWithOwner` and `branchName`:

    {
      "repositoryNameWithOwner": "github/graphql-client",
      "branchName": "main"
    }



   id - The Node ID of the Ref to be updated.

   repositoryNameWithOwner - The nameWithOwner of the repository to commit to.

   branchName - The unqualified name of the branch to append the commit to.

   """
   id: ID
   repositoryNameWithOwner: str
   branchName: str

class CommitMessagePatternParameters(GQLObject):
   """
   CommitMessagePatternParameters - Parameters to be used for the commit_message_pattern rule

   name - How this rule will appear to users.

   negate - If true, the rule will fail if the pattern matches.

   operator - The operator to use for matching.

   pattern - The pattern to match with.

   """
   name: str
   negate: bool
   operator: str
   pattern: str

class CommitContributionOrder(GQLObject):
   """
   CommitContributionOrder - Ordering options for commit contribution connections.

   field - The field by which to order commit contributions.

   direction - The ordering direction.

   """
   field: CommitContributionOrderField
   direction: OrderDirection

class CommitAuthorEmailPatternParameters(GQLObject):
   """
   CommitAuthorEmailPatternParameters - Parameters to be used for the commit_author_email_pattern rule

   name - How this rule will appear to users.

   negate - If true, the rule will fail if the pattern matches.

   operator - The operator to use for matching.

   pattern - The pattern to match with.

   """
   name: str
   negate: bool
   operator: str
   pattern: str

class CodeOfConduct(GQLObject):
   """
   CodeOfConduct - The Code of Conduct for a repository

   body - The body of the Code of Conduct

   key - The key for the Code of Conduct

   name - The formal name of the Code of Conduct

   resourcePath - The HTTP path for this Code of Conduct

   url - The HTTP URL for this Code of Conduct

   """
   body: str
   id: ID
   key: str
   name: str
   resourcePath: URI
   url: URI

class CloseIssueInput(GQLObject):
   """
   CloseIssueInput - Autogenerated input type of CloseIssue

   issueId - ID of the issue to be closed.

   stateReason - The reason the issue is to be closed.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID
   stateReason: IssueClosedStateReason
   clientMutationId: str

class Closable(GQLObject):
   """
   Closable - An object that can be closed

   closed - Indicates if the object is closed (definition of closed may depend on type)

   closedAt - Identifies the date and time when the object was closed.

   viewerCanClose - Indicates if the object can be closed by the viewer.

   viewerCanReopen - Indicates if the object can be reopened by the viewer.

   """
   closed: bool
   closedAt: DateTime
   viewerCanClose: bool
   viewerCanReopen: bool

class CloneProjectInput(GQLObject):
   """
   CloneProjectInput - Autogenerated input type of CloneProject

   targetOwnerId - The owner ID to create the project under.

   sourceId - The source project to clone.

   includeWorkflows - Whether or not to clone the source project's workflows.

   name - The name of the project.

   body - The description of the project.

   public - The visibility of the project, defaults to false (private).

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   targetOwnerId: ID
   sourceId: ID
   includeWorkflows: bool
   name: str
   body: str
   public: bool
   clientMutationId: str

class ClearLabelsFromLabelableInput(GQLObject):
   """
   ClearLabelsFromLabelableInput - Autogenerated input type of ClearLabelsFromLabelable

   labelableId - The id of the labelable object to clear the labels from.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   labelableId: ID
   clientMutationId: str

class CheckSuiteAutoTriggerPreference(GQLObject):
   """
   CheckSuiteAutoTriggerPreference - The auto-trigger preferences that are available for check suites.

   appId - The node ID of the application that owns the check suite.

   setting - Set to `true` to enable automatic creation of CheckSuite events upon pushes to the repository.

   """
   appId: ID
   setting: bool

class CheckRunStateCount(GQLObject):
   """
   CheckRunStateCount - Represents a count of the state of a check run.

   count - The number of check runs with this state.

   state - The state of a check run.

   """
   count: int
   state: CheckRunState

class CheckRunFilter(GQLObject):
   """
   CheckRunFilter - The filters that are available when fetching check runs.

   checkType - Filters the check runs by this type.

   appId - Filters the check runs created by this application ID.

   checkName - Filters the check runs by this name.

   status - Filters the check runs by this status. Superceded by statuses.

   statuses - Filters the check runs by this status. Overrides status.

   conclusions - Filters the check runs by these conclusions.

   """
   checkType: CheckRunType
   appId: int
   checkName: str
   status: CheckStatusState
   statuses: list[CheckStatusState]
   conclusions: list[CheckConclusionState]

class CheckAnnotationRange(GQLObject):
   """
   CheckAnnotationRange - Information from a check run analysis to specific lines of code.

   startLine - The starting line of the range.

   startColumn - The starting column of the range.

   endLine - The ending line of the range.

   endColumn - The ending column of the range.

   """
   startLine: int
   startColumn: int
   endLine: int
   endColumn: int

class ChangeUserStatusInput(GQLObject):
   """
   ChangeUserStatusInput - Autogenerated input type of ChangeUserStatus

   emoji - The emoji to represent your status. Can either be a native Unicode emoji or an emoji name with colons, e.g., :grinning:.

   message - A short description of your current status.

   organizationId - The ID of the organization whose members will be allowed to see the status. If omitted, the status will be publicly visible.

   limitedAvailability - Whether this status should indicate you are not fully available on GitHub, e.g., you are away.

   expiresAt - If set, the user status will not be shown after this date.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   emoji: str
   message: str
   organizationId: ID
   limitedAvailability: bool
   expiresAt: DateTime
   clientMutationId: str

class CancelEnterpriseAdminInvitationInput(GQLObject):
   """
   CancelEnterpriseAdminInvitationInput - Autogenerated input type of CancelEnterpriseAdminInvitation

   invitationId - The Node ID of the pending enterprise administrator invitation.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   invitationId: ID
   clientMutationId: str

class CVSS(GQLObject):
   """
   CVSS - The Common Vulnerability Scoring System

   score - The CVSS score associated with this advisory

   vectorString - The CVSS vector string associated with this advisory

   """
   score: float
   vectorString: str

class BranchNamePatternParametersInput(GQLObject):
   """
   BranchNamePatternParametersInput - Parameters to be used for the branch_name_pattern rule

   name - How this rule will appear to users.

   negate - If true, the rule will fail if the pattern matches.

   operator - The operator to use for matching.

   pattern - The pattern to match with.

   """
   name: str
   negate: bool
   operator: str
   pattern: str

class WVUEE_URI_Field(ArguedStr):
   """
   WVUEE_URI_Field - A URL pointing to the GitHub App's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class AuditLogOrder(GQLObject):
   """
   AuditLogOrder - Ordering options for Audit Log connections.

   field - The field to order Audit Logs by.

   direction - The ordering direction.

   """
   field: AuditLogOrderField
   direction: OrderDirection

class ArchiveProjectV2ItemInput(GQLObject):
   """
   ArchiveProjectV2ItemInput - Autogenerated input type of ArchiveProjectV2Item

   projectId - The ID of the Project to archive the item from.

   itemId - The ID of the ProjectV2Item to archive.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   itemId: ID
   clientMutationId: str

class ApproveDeploymentsInput(GQLObject):
   """
   ApproveDeploymentsInput - Autogenerated input type of ApproveDeployments

   workflowRunId - The node ID of the workflow run containing the pending deployments.

   environmentIds - The ids of environments to reject deployments

   comment - Optional comment for approving deployments

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   workflowRunId: ID
   environmentIds: list[ID]
   comment: str
   clientMutationId: str

class AddVerifiableDomainInput(GQLObject):
   """
   AddVerifiableDomainInput - Autogenerated input type of AddVerifiableDomain

   ownerId - The ID of the owner to add the domain to

   domain - The URL of the domain

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID
   domain: URI
   clientMutationId: str

class AddStarInput(GQLObject):
   """
   AddStarInput - Autogenerated input type of AddStar

   starrableId - The Starrable ID to star.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   starrableId: ID
   clientMutationId: str

class AddPullRequestReviewThreadReplyInput(GQLObject):
   """
   AddPullRequestReviewThreadReplyInput - Autogenerated input type of AddPullRequestReviewThreadReply

   pullRequestReviewId - The Node ID of the pending review to which the reply will belong.

   pullRequestReviewThreadId - The Node ID of the thread to which this reply is being written.

   body - The text of the reply.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestReviewId: ID
   pullRequestReviewThreadId: ID
   body: str
   clientMutationId: str

class AddPullRequestReviewCommentInput(GQLObject):
   """
   AddPullRequestReviewCommentInput - Autogenerated input type of AddPullRequestReviewComment

   pullRequestId - The node ID of the pull request reviewing

**Upcoming Change on 2023-10-01 UTC**
**Description:** `pullRequestId` will be removed. use addPullRequestReviewThread or addPullRequestReviewThreadReply instead
**Reason:** We are deprecating the addPullRequestReviewComment mutation


   pullRequestReviewId - The Node ID of the review to modify.

**Upcoming Change on 2023-10-01 UTC**
**Description:** `pullRequestReviewId` will be removed. use addPullRequestReviewThread or addPullRequestReviewThreadReply instead
**Reason:** We are deprecating the addPullRequestReviewComment mutation


   commitOID - The SHA of the commit to comment on.

**Upcoming Change on 2023-10-01 UTC**
**Description:** `commitOID` will be removed. use addPullRequestReviewThread or addPullRequestReviewThreadReply instead
**Reason:** We are deprecating the addPullRequestReviewComment mutation


   body - The text of the comment. This field is required

**Upcoming Change on 2023-10-01 UTC**
**Description:** `body` will be removed. use addPullRequestReviewThread or addPullRequestReviewThreadReply instead
**Reason:** We are deprecating the addPullRequestReviewComment mutation


   path - The relative path of the file to comment on.

**Upcoming Change on 2023-10-01 UTC**
**Description:** `path` will be removed. use addPullRequestReviewThread or addPullRequestReviewThreadReply instead
**Reason:** We are deprecating the addPullRequestReviewComment mutation


   position - The line index in the diff to comment on.

**Upcoming Change on 2023-10-01 UTC**
**Description:** `position` will be removed. use addPullRequestReviewThread or addPullRequestReviewThreadReply instead
**Reason:** We are deprecating the addPullRequestReviewComment mutation


   inReplyTo - The comment id to reply to.

**Upcoming Change on 2023-10-01 UTC**
**Description:** `inReplyTo` will be removed. use addPullRequestReviewThread or addPullRequestReviewThreadReply instead
**Reason:** We are deprecating the addPullRequestReviewComment mutation


   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   pullRequestReviewId: ID
   commitOID: GitObjectID
   body: str
   path: str
   position: int
   inReplyTo: ID
   clientMutationId: str

class AddProjectV2DraftIssueInput(GQLObject):
   """
   AddProjectV2DraftIssueInput - Autogenerated input type of AddProjectV2DraftIssue

   projectId - The ID of the Project to add the draft issue to.

   title - The title of the draft issue. A project item can also be created by providing the URL of an Issue or Pull Request if you have access.

   body - The body of the draft issue.

   assigneeIds - The IDs of the assignees of the draft issue.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   title: str
   body: str
   assigneeIds: list[ID]
   clientMutationId: str

class AddProjectCardInput(GQLObject):
   """
   AddProjectCardInput - Autogenerated input type of AddProjectCard

   projectColumnId - The Node ID of the ProjectColumn.

   contentId - The content of the card. Must be a member of the ProjectCardItem union

   note - The note on the card.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectColumnId: ID
   contentId: ID
   note: str
   clientMutationId: str

class AddEnterpriseSupportEntitlementPayload(GQLObject):
   """
   AddEnterpriseSupportEntitlementPayload - Autogenerated return type of AddEnterpriseSupportEntitlement

   clientMutationId - A unique identifier for the client performing the mutation.

   message - A message confirming the result of adding the support entitlement.

   """
   clientMutationId: str
   message: str

class AddEnterpriseOrganizationMemberInput(GQLObject):
   """
   AddEnterpriseOrganizationMemberInput - Autogenerated input type of AddEnterpriseOrganizationMember

   enterpriseId - The ID of the enterprise which owns the organization.

   organizationId - The ID of the organization the users will be added to.

   userIds - The IDs of the enterprise members to add.

   role - The role to assign the users in the organization

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   organizationId: ID
   userIds: list[ID]
   role: OrganizationMemberRole
   clientMutationId: str

class AddDiscussionCommentInput(GQLObject):
   """
   AddDiscussionCommentInput - Autogenerated input type of AddDiscussionComment

   discussionId - The Node ID of the discussion to comment on.

   replyToId - The Node ID of the discussion comment within this discussion to reply to.

   body - The contents of the comment.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   discussionId: ID
   replyToId: ID
   body: str
   clientMutationId: str

class AddAssigneesToAssignableInput(GQLObject):
   """
   AddAssigneesToAssignableInput - Autogenerated input type of AddAssigneesToAssignable

   assignableId - The id of the assignable object to add assignees to.

   assigneeIds - The id of users to add as assignees.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   assignableId: ID
   assigneeIds: list[ID]
   clientMutationId: str

class YBFIV_URI_Field(ArguedStr):
   """
   YBFIV_URI_Field - A URL pointing to the actor's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class AcceptTopicSuggestionInput(GQLObject):
   """
   AcceptTopicSuggestionInput - Autogenerated input type of AcceptTopicSuggestion

   repositoryId - The Node ID of the repository.

   name - The name of the suggested topic.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   name: str
   clientMutationId: str

class AbortQueuedMigrationsPayload(GQLObject):
   """
   AbortQueuedMigrationsPayload - Autogenerated return type of AbortQueuedMigrations

   clientMutationId - A unique identifier for the client performing the mutation.

   success - Did the operation succeed?

   """
   clientMutationId: str
   success: bool
