from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class ODBXR_anyPinnableItems_Field(ArguedBool):
   """
   ODBXR_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class SCWND_URI_Field(ArguedStr):
   """
   SCWND_URI_Field - URL for the listing's logo image.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class XTPZA_URI_Field(ArguedStr):
   """
   XTPZA_URI_Field - A URL pointing to the app's logo.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting image.

      """
      size: int

   _args: URIArgs



class CYSMW_URI_Field(ArguedStr):
   """
   CYSMW_URI_Field - A URL pointing to the enterprise's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class VUBLQ_HTML_Field(ArguedStr):
   """
   VUBLQ_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class IFUMS_URI_Field(ArguedStr):
   """
   IFUMS_URI_Field - A URL pointing to the enterprise user account's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class NZMVG_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   NZMVG_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

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



class KIYOL_isSponsoredBy_Field(ArguedBool):
   """
   KIYOL_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class HBYVQ_URI_Field(ArguedStr):
   """
   HBYVQ_URI_Field - A URL pointing to the organization's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class VMKWJ_anyPinnableItems_Field(ArguedBool):
   """
   VMKWJ_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class IHBCR_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   IHBCR_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

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



class FOGWM_organizationVerifiedDomainEmails_Field(ArguedStr):
   """
   FOGWM_organizationVerifiedDomainEmails_Field - Verified email addresses that match verified domains for a specified organization the user is a member of.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      login - The login of the organization to match verified domains from.

      """
      login: NonNull_str

   _args: strArgs



class VKERH_isSponsoredBy_Field(ArguedBool):
   """
   VKERH_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class JWHUW_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedBool):
   """
   JWHUW_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field - Could this user receive email notifications, if the organization had notification restrictions enabled?

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      login - The login of the organization to check.

      """
      login: NonNull_str

   _args: boolArgs



class RTAOK_URI_Field(ArguedStr):
   """
   RTAOK_URI_Field - A URL pointing to the user's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class IPLGW_anyPinnableItems_Field(ArguedBool):
   """
   IPLGW_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class SAMNF_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   SAMNF_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

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



class LAPKE_isSponsoredBy_Field(ArguedBool):
   """
   LAPKE_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class VHAOC_text_Field(ArguedStr):
   """
   VHAOC_text_Field - UTF8 text data or null if the file is binary

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      truncate - Optionally truncate the returned file to this length.

      """
      truncate: int

   _args: strArgs



class JVPAP_totalRepositoryContributions_Field(ArguedInt):
   """
   JVPAP_totalRepositoryContributions_Field - How many repositories the user created.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first repository ever be excluded from this count.

      """
      excludeFirst: bool

   _args: intArgs



class QWHHU_totalRepositoriesWithContributedPullRequests_Field(ArguedInt):
   """
   QWHHU_totalRepositoriesWithContributedPullRequests_Field - How many different repositories the user opened pull requests in.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class PDWSN_totalRepositoriesWithContributedIssues_Field(ArguedInt):
   """
   PDWSN_totalRepositoriesWithContributedIssues_Field - How many different repositories the user opened issues in.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class XEEGR_totalPullRequestContributions_Field(ArguedInt):
   """
   XEEGR_totalPullRequestContributions_Field - How many pull requests the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class SGTYP_totalIssueContributions_Field(ArguedInt):
   """
   SGTYP_totalIssueContributions_Field - How many issues the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class PKCUV_isRequired_Field(ArguedBool):
   """
   PKCUV_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class HAYOW_URI_Field(ArguedStr):
   """
   HAYOW_URI_Field - The avatar of the OAuth application or the user that created the status

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class AEGOW_isRequired_Field(ArguedBool):
   """
   AEGOW_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class UCYLQ_URI_Field(ArguedStr):
   """
   UCYLQ_URI_Field - A URL pointing to the author's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class IXZOF_viewerMergeHeadlineText_Field(ArguedStr):
   """
   IXZOF_viewerMergeHeadlineText_Field - The merge headline text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class ACHOO_viewerMergeBodyText_Field(ArguedStr):
   """
   ACHOO_viewerMergeBodyText_Field - The merge body text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class FRTRH_URI_Field(ArguedStr):
   """
   FRTRH_URI_Field - A URL pointing to the team's avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class ADVTC_trackedIssuesCount_Field(ArguedInt):
   """
   ADVTC_trackedIssuesCount_Field - The number of tracked issues for this issue

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      states - Limit the count to tracked issues with the specified states.

      """
      states: list[TrackedIssueStates]

   _args: intArgs



class QHOFH_HTML_Field(ArguedStr):
   """
   QHOFH_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class PZYRM_URI_Field(ArguedStr):
   """
   PZYRM_URI_Field - A URL pointing to the owner's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class FECCR_HTML_Field(ArguedStr):
   """
   FECCR_HTML_Field - A description of the release, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class UMCLH_URI_Field(ArguedStr):
   """
   UMCLH_URI_Field - A URL pointing to the GitHub App's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class NYOXP_URI_Field(ArguedStr):
   """
   NYOXP_URI_Field - A URL pointing to the actor's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class JEYBZ_isRequired_Field(ArguedBool):
   """
   JEYBZ_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



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
   topicNames: NonNull_list[str]
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

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   expectedHeadOid: GitObjectID
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

class UnmarkIssueAsDuplicateInput(GQLObject):
   """
   UnmarkIssueAsDuplicateInput - Autogenerated input type of UnmarkIssueAsDuplicate

   duplicateId - ID of the issue or pull request currently marked as a duplicate.

   canonicalId - ID of the issue or pull request currently considered canonical/authoritative/original.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   duplicateId: ID
   canonicalId: ID
   clientMutationId: str

class UnmarkDiscussionCommentAsAnswerInput(GQLObject):
   """
   UnmarkDiscussionCommentAsAnswerInput - Autogenerated input type of UnmarkDiscussionCommentAsAnswer

   id - The Node ID of the discussion comment to unmark as an answer.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class UnlinkRepositoryFromProjectInput(GQLObject):
   """
   UnlinkRepositoryFromProjectInput - Autogenerated input type of UnlinkRepositoryFromProject

   projectId - The ID of the Project linked to the Repository.

   repositoryId - The ID of the Repository linked to the Project.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   repositoryId: ID
   clientMutationId: str

class UnlinkProjectV2FromRepositoryInput(GQLObject):
   """
   UnlinkProjectV2FromRepositoryInput - Autogenerated input type of UnlinkProjectV2FromRepository

   projectId - The ID of the project to unlink from the repository.

   repositoryId - The ID of the repository to unlink from the project.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   repositoryId: ID
   clientMutationId: str

class UnfollowUserInput(GQLObject):
   """
   UnfollowUserInput - Autogenerated input type of UnfollowUser

   userId - ID of the user to unfollow.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   userId: ID
   clientMutationId: str

class UnarchiveRepositoryInput(GQLObject):
   """
   UnarchiveRepositoryInput - Autogenerated input type of UnarchiveRepository

   repositoryId - The ID of the repository to unarchive.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   clientMutationId: str

class TransferIssueInput(GQLObject):
   """
   TransferIssueInput - Autogenerated input type of TransferIssue

   issueId - The Node ID of the issue to be transferred

   repositoryId - The Node ID of the repository the issue should be transferred to

   createLabelsIfMissing - Whether to create labels if they don't exist in the target repository (matched by name)

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID
   repositoryId: ID
   createLabelsIfMissing: bool
   clientMutationId: str

class TextMatchHighlight(GQLObject):
   """
   TextMatchHighlight - Represents a single highlight in a search result match.

   beginIndice - The indice in the fragment where the matched text begins.

   endIndice - The indice in the fragment where the matched text ends.

   text - The text matched.

   """
   beginIndice: int
   endIndice: int
   text: str

class TeamOrder(GQLObject):
   """
   TeamOrder - Ways in which team connections can be ordered.

   field - The field in which to order nodes by.

   direction - The direction in which to order nodes.

   """
   field: TeamOrderField
   direction: OrderDirection

class TeamDiscussionOrder(GQLObject):
   """
   TeamDiscussionOrder - Ways in which team discussion connections can be ordered.

   field - The field by which to order nodes.

   direction - The direction in which to order nodes.

   """
   field: TeamDiscussionOrderField
   direction: OrderDirection

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

class StartRepositoryMigrationInput(GQLObject):
   """
   StartRepositoryMigrationInput - Autogenerated input type of StartRepositoryMigration

   sourceId - The ID of the migration source.

   ownerId - The ID of the organization that will own the imported repository.

   sourceRepositoryUrl - The URL of the source repository.

   repositoryName - The name of the imported repository.

   continueOnError - Whether to continue the migration on error. Defaults to `false`.

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

class SetUserInteractionLimitInput(GQLObject):
   """
   SetUserInteractionLimitInput - Autogenerated input type of SetUserInteractionLimit

   userId - The ID of the user to set a limit for.

   limit - The limit to set.

   expiry - When this limit should expire.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   userId: ID
   limit: RepositoryInteractionLimit
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SetOrganizationInteractionLimitInput(GQLObject):
   """
   SetOrganizationInteractionLimitInput - Autogenerated input type of SetOrganizationInteractionLimit

   organizationId - The ID of the organization to set a limit for.

   limit - The limit to set.

   expiry - When this limit should expire.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID
   limit: RepositoryInteractionLimit
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SecurityVulnerabilityOrder(GQLObject):
   """
   SecurityVulnerabilityOrder - Ordering options for security vulnerability connections

   field - The field to order security vulnerabilities by.

   direction - The ordering direction.

   """
   field: SecurityVulnerabilityOrderField
   direction: OrderDirection

class SecurityAdvisoryPackageVersion(GQLObject):
   """
   SecurityAdvisoryPackageVersion - An individual package version

   identifier - The package name or version

   """
   identifier: str

class SecurityAdvisoryOrder(GQLObject):
   """
   SecurityAdvisoryOrder - Ordering options for security advisory connections

   field - The field to order security advisories by.

   direction - The ordering direction.

   """
   field: SecurityAdvisoryOrderField
   direction: OrderDirection

class SecurityAdvisoryIdentifier(GQLObject):
   """
   SecurityAdvisoryIdentifier - A GitHub Security Advisory Identifier

   type - The identifier type, e.g. GHSA, CVE

   value - The identifier

   """
   type: str
   value: str

class RevokeMigratorRolePayload(GQLObject):
   """
   RevokeMigratorRolePayload - Autogenerated return type of RevokeMigratorRole

   clientMutationId - A unique identifier for the client performing the mutation.

   success - Did the operation succeed?

   """
   clientMutationId: str
   success: bool

class RevokeEnterpriseOrganizationsMigratorRoleInput(GQLObject):
   """
   RevokeEnterpriseOrganizationsMigratorRoleInput - Autogenerated input type of RevokeEnterpriseOrganizationsMigratorRole

   enterpriseId - The ID of the enterprise to which all organizations managed by it will be granted the migrator role.

   login - The login of the user to revoke the migrator role

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   login: str
   clientMutationId: str

class RevertPullRequestInput(GQLObject):
   """
   RevertPullRequestInput - Autogenerated input type of RevertPullRequest

   pullRequestId - The ID of the pull request to revert.

   title - The title of the revert pull request.

   body - The description of the revert pull request.

   draft - Indicates whether the revert pull request should be a draft.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   title: str
   body: str
   draft: bool
   clientMutationId: str

class ResolveReviewThreadInput(GQLObject):
   """
   ResolveReviewThreadInput - Autogenerated input type of ResolveReviewThread

   threadId - The ID of the thread to resolve

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   threadId: ID
   clientMutationId: str

class RequiredStatusCheckInput(GQLObject):
   """
   RequiredStatusCheckInput - Specifies the attributes for a new or updated required status check.

   context - Status check context that must pass for commits to be accepted to the matching branch.

   appId - The ID of the App that must set the status in order for it to be accepted. Omit this value to use whichever app has recently been setting this status, or use "any" to allow any app to set the status.

   """
   context: str
   appId: ID

class RequirableByPullRequest(GQLObject):
   """
   RequirableByPullRequest - Represents a type that can be required by a pull request for merging.

   isRequired - Whether this is required to pass before merging for a specific pull request.

   """
   isRequired: JEYBZ_isRequired_Field

class RepositoryOrder(GQLObject):
   """
   RepositoryOrder - Ordering options for repository connections

   field - The field to order repositories by.

   direction - The ordering direction.

   """
   field: RepositoryOrderField
   direction: OrderDirection

class RepositoryInvitationOrder(GQLObject):
   """
   RepositoryInvitationOrder - Ordering options for repository invitation connections.

   field - The field to order repository invitations by.

   direction - The ordering direction.

   """
   field: RepositoryInvitationOrderField
   direction: OrderDirection

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

class RemoveUpvoteInput(GQLObject):
   """
   RemoveUpvoteInput - Autogenerated input type of RemoveUpvote

   subjectId - The Node ID of the discussion or comment to remove upvote.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID
   clientMutationId: str

class RemoveReactionInput(GQLObject):
   """
   RemoveReactionInput - Autogenerated input type of RemoveReaction

   subjectId - The Node ID of the subject to modify.

   content - The name of the emoji reaction to remove.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID
   content: ReactionContent
   clientMutationId: str

class RemoveLabelsFromLabelableInput(GQLObject):
   """
   RemoveLabelsFromLabelableInput - Autogenerated input type of RemoveLabelsFromLabelable

   labelableId - The id of the Labelable to remove labels from.

   labelIds - The ids of labels to remove.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   labelableId: ID
   labelIds: NonNull_list[ID]
   clientMutationId: str

class RemoveEnterpriseSupportEntitlementInput(GQLObject):
   """
   RemoveEnterpriseSupportEntitlementInput - Autogenerated input type of RemoveEnterpriseSupportEntitlement

   enterpriseId - The ID of the Enterprise which the admin belongs to.

   login - The login of a member who will lose the support entitlement.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   login: str
   clientMutationId: str

class RemoveEnterpriseMemberInput(GQLObject):
   """
   RemoveEnterpriseMemberInput - Autogenerated input type of RemoveEnterpriseMember

   enterpriseId - The ID of the enterprise from which the user should be removed.

   userId - The ID of the user to remove from the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   userId: ID
   clientMutationId: str

class RemoveEnterpriseAdminInput(GQLObject):
   """
   RemoveEnterpriseAdminInput - Autogenerated input type of RemoveEnterpriseAdmin

   enterpriseId - The Enterprise ID from which to remove the administrator.

   login - The login of the user to remove as an administrator.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   login: str
   clientMutationId: str

class ReleaseOrder(GQLObject):
   """
   ReleaseOrder - Ways in which lists of releases can be ordered upon return.

   field - The field in which to order releases by.

   direction - The direction in which to order releases by the specified field.

   """
   field: ReleaseOrderField
   direction: OrderDirection

class RegenerateVerifiableDomainTokenPayload(GQLObject):
   """
   RegenerateVerifiableDomainTokenPayload - Autogenerated return type of RegenerateVerifiableDomainToken

   clientMutationId - A unique identifier for the client performing the mutation.

   verificationToken - The verification token that was generated.

   """
   clientMutationId: str
   verificationToken: str

class RegenerateEnterpriseIdentityProviderRecoveryCodesInput(GQLObject):
   """
   RegenerateEnterpriseIdentityProviderRecoveryCodesInput - Autogenerated input type of RegenerateEnterpriseIdentityProviderRecoveryCodes

   enterpriseId - The ID of the enterprise on which to set an identity provider.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   clientMutationId: str

class RefOrder(GQLObject):
   """
   RefOrder - Ways in which lists of git refs can be ordered upon return.

   field - The field in which to order refs by.

   direction - The direction in which to order refs by the specified field.

   """
   field: RefOrderField
   direction: OrderDirection

class RateLimit(GQLObject):
   """
   RateLimit - Represents the client's rate limit.

   cost - The point cost for the current query counting against the rate limit.

   limit - The maximum number of points the client is permitted to consume in a 60 minute window.

   nodeCount - The maximum number of nodes this query may return

   remaining - The number of points remaining in the current rate limit window.

   resetAt - The time at which the current rate limit window resets in UTC epoch seconds.

   used - The number of points used in the current rate limit window.

   """
   cost: int
   limit: int
   nodeCount: int
   remaining: int
   resetAt: DateTime
   used: int

class PullRequestChangedFile(GQLObject):
   """
   PullRequestChangedFile - A file changed in a pull request.

   additions - The number of additions to the file.

   changeType - How the file was changed in this PullRequest

   deletions - The number of deletions to the file.

   path - The path of the file.

   viewerViewedState - The state of the file for the viewer.

   """
   additions: int
   changeType: PatchStatus
   deletions: int
   path: str
   viewerViewedState: FileViewedState

class PublicKey(GQLObject):
   """
   PublicKey - A user's public key.

   accessedAt - The last time this authorization was used to perform an action. Values will be null for keys not owned by the user.

   createdAt - Identifies the date and time when the key was created. Keys created before March 5th, 2014 have inaccurate values. Values will be null for keys not owned by the user.

   fingerprint - The fingerprint for this PublicKey.

   isReadOnly - Whether this PublicKey is read-only or not. Values will be null for keys not owned by the user.

   key - The public key string.

   updatedAt - Identifies the date and time when the key was updated. Keys created before March 5th, 2014 may have inaccurate values. Values will be null for keys not owned by the user.

   """
   accessedAt: DateTime
   createdAt: DateTime
   fingerprint: str
   id: ID
   isReadOnly: bool
   key: str
   updatedAt: DateTime

class ProjectV2SingleSelectFieldOption(GQLObject):
   """
   ProjectV2SingleSelectFieldOption - Single select field option for a configuration for a project.

   id - The option's ID.

   name - The option's name.

   nameHTML - The option's html name.

   """
   id: str
   name: str
   nameHTML: str

class ProjectV2IterationFieldIteration(GQLObject):
   """
   ProjectV2IterationFieldIteration - Iteration field iteration settings for a project.

   duration - The iteration's duration in days

   id - The iteration's ID.

   startDate - The iteration's start date

   title - The iteration's title.

   titleHTML - The iteration's html title.

   """
   duration: int
   id: str
   startDate: Date
   title: str
   titleHTML: str

class ProjectV2ItemFieldValueOrder(GQLObject):
   """
   ProjectV2ItemFieldValueOrder - Ordering options for project v2 item field value connections

   field - The field to order the project v2 item field values by.

   direction - The ordering direction.

   """
   field: ProjectV2ItemFieldValueOrderField
   direction: OrderDirection

class ProjectV2FieldValue(GQLObject):
   """
   ProjectV2FieldValue - The values that can be used to update a field of an item inside a Project. Only 1 value can be updated at a time.

   text - The text to set on the field.

   number - The number to set on the field.

   date - The ISO 8601 date to set on the field.

   singleSelectOptionId - The id of the single select option to set on the field.

   iterationId - The id of the iteration to set on the field.

   """
   text: str
   number: float
   date: Date
   singleSelectOptionId: str
   iterationId: str

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

   oauthApplicationName - The name of the OAuth Application.

   oauthApplicationResourcePath - The HTTP path for the OAuth Application

   oauthApplicationUrl - The HTTP URL for the OAuth Application

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

class MergePullRequestInput(GQLObject):
   """
   MergePullRequestInput - Autogenerated input type of MergePullRequest

   pullRequestId - ID of the pull request to be merged.

   commitHeadline - Commit headline to use for the merge commit; if omitted, a default message will be used.

   commitBody - Commit body to use for the merge commit; if omitted, a default message will be used

   expectedHeadOid - OID that the pull request head ref must match to allow merge; if omitted, no check is performed.

   mergeMethod - The merge method to use. If omitted, defaults to 'MERGE'

   authorEmail - The email address to associate with this merge.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   commitHeadline: str
   commitBody: str
   expectedHeadOid: GitObjectID
   mergeMethod: PullRequestMergeMethod
   authorEmail: str
   clientMutationId: str

class MarketplaceCategory(GQLObject):
   """
   MarketplaceCategory - A public description of a Marketplace category.

   description - The category's description.

   howItWorks - The technical description of how apps listed in this category work with GitHub.

   name - The category's name.

   primaryListingCount - How many Marketplace listings have this as their primary category.

   resourcePath - The HTTP path for this Marketplace category.

   secondaryListingCount - How many Marketplace listings have this as their secondary category.

   slug - The short name of the category used in its URL.

   url - The HTTP URL for this Marketplace category.

   """
   description: str
   howItWorks: str
   id: ID
   name: str
   primaryListingCount: int
   resourcePath: URI
   secondaryListingCount: int
   slug: str
   url: URI

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

class IssueTemplate(GQLObject):
   """
   IssueTemplate - A repository issue template.

   about - The template purpose.

   body - The suggested issue body.

   filename - The template filename.

   name - The template name.

   title - The suggested issue title.

   """
   about: str
   body: str
   filename: str
   name: str
   title: str

class IssueFilters(GQLObject):
   """
   IssueFilters - Ways in which to filter lists of issues.

   assignee - List issues assigned to given name. Pass in `null` for issues with no assigned user, and `*` for issues assigned to any user.

   createdBy - List issues created by given name.

   labels - List issues where the list of label names exist on the issue.

   mentioned - List issues where the given name is mentioned in the issue.

   milestone - List issues by given milestone argument. If an string representation of an integer is passed, it should refer to a milestone by its database ID. Pass in `null` for issues with no milestone, and `*` for issues that are assigned to any milestone.

   milestoneNumber - List issues by given milestone argument. If an string representation of an integer is passed, it should refer to a milestone by its number field. Pass in `null` for issues with no milestone, and `*` for issues that are assigned to any milestone.

   since - List issues that have been updated at or after the given date.

   states - List issues filtered by the list of states given.

   viewerSubscribed - List issues subscribed to by viewer.

   """
   assignee: str
   createdBy: str
   labels: list[str]
   mentioned: str
   milestone: str
   milestoneNumber: str
   since: DateTime
   states: list[IssueState]
   viewerSubscribed: bool

class IpAllowListEntryOrder(GQLObject):
   """
   IpAllowListEntryOrder - Ordering options for IP allow list entry connections.

   field - The field to order IP allow list entries by.

   direction - The ordering direction.

   """
   field: IpAllowListEntryOrderField
   direction: OrderDirection

class HovercardContext(GQLObject):
   """
   HovercardContext - An individual line of a hovercard

   message - A string describing this context

   octicon - An octicon to accompany this context

   """
   message: str
   octicon: str

class GrantMigratorRoleInput(GQLObject):
   """
   GrantMigratorRoleInput - Autogenerated input type of GrantMigratorRole

   organizationId - The ID of the organization that the user/team belongs to.

   actor - The user login or Team slug to grant the migrator role.

   actorType - Specifies the type of the actor, can be either USER or TEAM.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID
   actor: str
   actorType: ActorType
   clientMutationId: str

class GitHubMetadata(GQLObject):
   """
   GitHubMetadata - Represents information about the GitHub instance.

   gitHubServicesSha - Returns a String that's a SHA of `github-services`

   gitIpAddresses - IP addresses that users connect to for git operations

   hookIpAddresses - IP addresses that service hooks are sent from

   importerIpAddresses - IP addresses that the importer connects from

   isPasswordAuthenticationVerifiable - Whether or not users are verified

   pagesIpAddresses - IP addresses for GitHub Pages' A records

   """
   gitHubServicesSha: GitObjectID
   gitIpAddresses: list[str]
   hookIpAddresses: list[str]
   importerIpAddresses: list[str]
   isPasswordAuthenticationVerifiable: bool
   pagesIpAddresses: list[str]

class GenericHovercardContext(GQLObject):
   """
   GenericHovercardContext - A generic hovercard context with a message and icon

   message - A string describing this context

   octicon - An octicon to accompany this context

   """
   message: str
   octicon: str

class FollowUserInput(GQLObject):
   """
   FollowUserInput - Autogenerated input type of FollowUser

   userId - ID of the user to follow.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   userId: ID
   clientMutationId: str

class FileDeletion(GQLObject):
   """
   FileDeletion - A command to delete the file at the given path as part of a commit.

   path - The path to delete

   """
   path: str

class ExternalIdentityAttribute(GQLObject):
   """
   ExternalIdentityAttribute - An attribute for the External Identity attributes collection

   metadata - The attribute metadata as JSON

   name - The attribute name

   value - The attribute value

   """
   metadata: str
   name: str
   value: str

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

class EnablePullRequestAutoMergeInput(GQLObject):
   """
   EnablePullRequestAutoMergeInput - Autogenerated input type of EnablePullRequestAutoMerge

   pullRequestId - ID of the pull request to enable auto-merge on.

   commitHeadline - Commit headline to use for the commit when the PR is mergable; if omitted, a default message will be used. NOTE: when merging with a merge queue any input value for commit headline is ignored.

   commitBody - Commit body to use for the commit when the PR is mergable; if omitted, a default message will be used. NOTE: when merging with a merge queue any input value for commit message is ignored.

   mergeMethod - The merge method to use. If omitted, defaults to `MERGE`. NOTE: when merging with a merge queue any input value for merge method is ignored.

   authorEmail - The email address to associate with this merge.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   commitHeadline: str
   commitBody: str
   mergeMethod: PullRequestMergeMethod
   authorEmail: str
   clientMutationId: str

class DraftPullRequestReviewComment(GQLObject):
   """
   DraftPullRequestReviewComment - Specifies a review comment to be left with a Pull Request Review.

   path - Path to the file being commented on.

   position - Position in the file to leave a comment on.

   body - Body of the comment to leave.

   """
   path: str
   position: int
   body: str

class DismissPullRequestReviewInput(GQLObject):
   """
   DismissPullRequestReviewInput - Autogenerated input type of DismissPullRequestReview

   pullRequestReviewId - The Node ID of the pull request review to modify.

   message - The contents of the pull request review dismissal message.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestReviewId: ID
   message: str
   clientMutationId: str

class DiscussionOrder(GQLObject):
   """
   DiscussionOrder - Ways in which lists of discussions can be ordered upon return.

   field - The field by which to order discussions.

   direction - The direction in which to order discussions by the specified field.

   """
   field: DiscussionOrderField
   direction: OrderDirection

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

class DeleteProjectV2ItemPayload(GQLObject):
   """
   DeleteProjectV2ItemPayload - Autogenerated return type of DeleteProjectV2Item

   clientMutationId - A unique identifier for the client performing the mutation.

   deletedItemId - The ID of the deleted item.

   """
   clientMutationId: str
   deletedItemId: ID

class DeleteProjectInput(GQLObject):
   """
   DeleteProjectInput - Autogenerated input type of DeleteProject

   projectId - The Project ID to update.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   clientMutationId: str

class DeleteProjectCardInput(GQLObject):
   """
   DeleteProjectCardInput - Autogenerated input type of DeleteProjectCard

   cardId - The id of the card to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   cardId: ID
   clientMutationId: str

class DeleteIssueInput(GQLObject):
   """
   DeleteIssueInput - Autogenerated input type of DeleteIssue

   issueId - The ID of the issue to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID
   clientMutationId: str

class DeleteIssueCommentInput(GQLObject):
   """
   DeleteIssueCommentInput - Autogenerated input type of DeleteIssueComment

   id - The ID of the comment to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class DeleteEnvironmentPayload(GQLObject):
   """
   DeleteEnvironmentPayload - Autogenerated return type of DeleteEnvironment

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   clientMutationId: str

class DeleteDiscussionInput(GQLObject):
   """
   DeleteDiscussionInput - Autogenerated input type of DeleteDiscussion

   id - The id of the discussion to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class DeleteDeploymentPayload(GQLObject):
   """
   DeleteDeploymentPayload - Autogenerated return type of DeleteDeployment

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   clientMutationId: str

class DeleteBranchProtectionRulePayload(GQLObject):
   """
   DeleteBranchProtectionRulePayload - Autogenerated return type of DeleteBranchProtectionRule

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   clientMutationId: str

class Deletable(GQLObject):
   """
   Deletable - Entities that can be deleted.

   viewerCanDelete - Check if the current viewer can delete this object.

   """
   viewerCanDelete: bool

class CreateTeamDiscussionInput(GQLObject):
   """
   CreateTeamDiscussionInput - Autogenerated input type of CreateTeamDiscussion

   teamId - The ID of the team to which the discussion belongs.

   title - The title of the discussion.

   body - The content of the discussion.

   private - If true, restricts the visibility of this discussion to team members and organization admins. If false or not specified, allows any organization member to view this discussion.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   teamId: ID
   title: str
   body: str
   private: bool
   clientMutationId: str

class CreateSponsorshipInput(GQLObject):
   """
   CreateSponsorshipInput - Autogenerated input type of CreateSponsorship

   sponsorId - The ID of the user or organization who is acting as the sponsor, paying for the sponsorship. Required if sponsorLogin is not given.

   sponsorLogin - The username of the user or organization who is acting as the sponsor, paying for the sponsorship. Required if sponsorId is not given.

   sponsorableId - The ID of the user or organization who is receiving the sponsorship. Required if sponsorableLogin is not given.

   sponsorableLogin - The username of the user or organization who is receiving the sponsorship. Required if sponsorableId is not given.

   tierId - The ID of one of sponsorable's existing tiers to sponsor at. Required if amount is not specified.

   amount - The amount to pay to the sponsorable in US dollars. Required if a tierId is not specified. Valid values: 1-12000.

   isRecurring - Whether the sponsorship should happen monthly/yearly or just this one time. Required if a tierId is not specified.

   receiveEmails - Whether the sponsor should receive email updates from the sponsorable.

   privacyLevel - Specify whether others should be able to see that the sponsor is sponsoring the sponsorable. Public visibility still does not reveal which tier is used.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
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
   """
   CreateSponsorsListingInput - Autogenerated input type of CreateSponsorsListing

   sponsorableLogin - The username of the organization to create a GitHub Sponsors profile for, if desired. Defaults to creating a GitHub Sponsors profile for the authenticated user if omitted.

   fiscalHostLogin - The username of the supported fiscal host's GitHub organization, if you want to receive sponsorship payouts through a fiscal host rather than directly to a bank account. For example, 'Open-Source-Collective' for Open Source Collective or 'numfocus' for numFOCUS. Case insensitive. See https://docs.github.com/sponsors/receiving-sponsorships-through-github-sponsors/using-a-fiscal-host-to-receive-github-sponsors-payouts for more information.

   fiscallyHostedProjectProfileUrl - The URL for your profile page on the fiscal host's website, e.g., https://opencollective.com/babel or https://numfocus.org/project/bokeh. Required if fiscalHostLogin is specified.

   billingCountryOrRegionCode - The country or region where the sponsorable's bank account is located. Required if fiscalHostLogin is not specified, ignored when fiscalHostLogin is specified.

   residenceCountryOrRegionCode - The country or region where the sponsorable resides. This is for tax purposes. Required if the sponsorable is yourself, ignored when sponsorableLogin specifies an organization.

   contactEmail - The email address we should use to contact you about the GitHub Sponsors profile being created. This will not be shared publicly. Must be a verified email address already on your GitHub account. Only relevant when the sponsorable is yourself. Defaults to your primary email address on file if omitted.

   fullDescription - Provide an introduction to serve as the main focus that appears on your GitHub Sponsors profile. It's a great opportunity to help potential sponsors learn more about you, your work, and why their sponsorship is important to you. GitHub-flavored Markdown is supported.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   sponsorableLogin: str
   fiscalHostLogin: str
   fiscallyHostedProjectProfileUrl: str
   billingCountryOrRegionCode: SponsorsCountryOrRegionCode
   residenceCountryOrRegionCode: SponsorsCountryOrRegionCode
   contactEmail: str
   fullDescription: str
   clientMutationId: str

class CreateRefInput(GQLObject):
   """
   CreateRefInput - Autogenerated input type of CreateRef

   repositoryId - The Node ID of the Repository to create the Ref in.

   name - The fully qualified name of the new Ref (ie: `refs/heads/my_new_branch`).

   oid - The GitObjectID that the new Ref shall target. Must point to a commit.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   name: str
   oid: GitObjectID
   clientMutationId: str

class CreateProjectV2Input(GQLObject):
   """
   CreateProjectV2Input - Autogenerated input type of CreateProjectV2

   ownerId - The owner ID to create the project under.

   title - The title of the project.

   repositoryId - The repository to link the project to.

   teamId - The team to link the project to. The team will be granted read permissions.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID
   title: str
   repositoryId: ID
   teamId: ID
   clientMutationId: str

class CreateMigrationSourceInput(GQLObject):
   """
   CreateMigrationSourceInput - Autogenerated input type of CreateMigrationSource

   name - The migration source name.

   url - The migration source URL, for example `https://github.com` or `https://monalisa.ghe.com`.

   accessToken - The migration source access token.

   type - The migration source type.

   ownerId - The ID of the organization that will own the migration source.

   githubPat - The GitHub personal access token of the user importing to the target repository.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   name: str
   url: str
   accessToken: str
   type: MigrationSourceType
   ownerId: ID
   githubPat: str
   clientMutationId: str

class CreateIssueInput(GQLObject):
   """
   CreateIssueInput - Autogenerated input type of CreateIssue

   repositoryId - The Node ID of the repository.

   title - The title for the issue.

   body - The body for the issue description.

   assigneeIds - The Node ID for the user assignee for this issue.

   milestoneId - The Node ID of the milestone for this issue.

   labelIds - An array of Node IDs of labels for this issue.

   projectIds - An array of Node IDs for projects associated with this issue.

   issueTemplate - The name of an issue template in the repository, assigns labels and assignees from the template to the issue

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   title: str
   body: str
   assigneeIds: list[ID]
   milestoneId: ID
   labelIds: list[ID]
   projectIds: list[ID]
   issueTemplate: str
   clientMutationId: str

class CreateEnvironmentInput(GQLObject):
   """
   CreateEnvironmentInput - Autogenerated input type of CreateEnvironment

   repositoryId - The node ID of the repository.

   name - The name of the environment.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   name: str
   clientMutationId: str

class CreateDiscussionInput(GQLObject):
   """
   CreateDiscussionInput - Autogenerated input type of CreateDiscussion

   repositoryId - The id of the repository on which to create the discussion.

   title - The title of the discussion.

   body - The body of the discussion.

   categoryId - The id of the discussion category to associate with this discussion.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   title: str
   body: str
   categoryId: ID
   clientMutationId: str

class CreateAttributionInvitationInput(GQLObject):
   """
   CreateAttributionInvitationInput - Autogenerated input type of CreateAttributionInvitation

   ownerId - The Node ID of the owner scoping the reattributable data.

   sourceId - The Node ID of the account owning the data to reattribute.

   targetId - The Node ID of the account which may claim the data.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID
   sourceId: ID
   targetId: ID
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

class CommitContributionOrder(GQLObject):
   """
   CommitContributionOrder - Ordering options for commit contribution connections.

   field - The field by which to order commit contributions.

   direction - The ordering direction.

   """
   field: CommitContributionOrderField
   direction: OrderDirection

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

class CloneTemplateRepositoryInput(GQLObject):
   """
   CloneTemplateRepositoryInput - Autogenerated input type of CloneTemplateRepository

   repositoryId - The Node ID of the template repository.

   name - The name of the new repository.

   ownerId - The ID of the owner for the new repository.

   description - A short description of the new repository.

   visibility - Indicates the repository's visibility level.

   includeAllBranches - Whether to copy all branches from the template to the new repository. Defaults to copying only the default branch of the template.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   name: str
   ownerId: ID
   description: str
   visibility: RepositoryVisibility
   includeAllBranches: bool
   clientMutationId: str

class ClearProjectV2ItemFieldValueInput(GQLObject):
   """
   ClearProjectV2ItemFieldValueInput - Autogenerated input type of ClearProjectV2ItemFieldValue

   projectId - The ID of the Project.

   itemId - The ID of the item to be cleared.

   fieldId - The ID of the field to be cleared.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   itemId: ID
   fieldId: ID
   clientMutationId: str

class CheckSuiteFilter(GQLObject):
   """
   CheckSuiteFilter - The filters that are available when fetching check suites.

   appId - Filters the check suites created by this application ID.

   checkName - Filters the check suites by this name.

   """
   appId: int
   checkName: str

class CheckStep(GQLObject):
   """
   CheckStep - A single check step.

   completedAt - Identifies the date and time when the check step was completed.

   conclusion - The conclusion of the check step.

   externalId - A reference for the check step on the integrator's system.

   name - The step's name.

   number - The index of the step in the list of steps of the parent check run.

   secondsToCompletion - Number of seconds to completion.

   startedAt - Identifies the date and time when the check step was started.

   status - The current status of the check step.

   """
   completedAt: DateTime
   conclusion: CheckConclusionState
   externalId: str
   name: str
   number: int
   secondsToCompletion: int
   startedAt: DateTime
   status: CheckStatusState

class CheckRunOutputImage(GQLObject):
   """
   CheckRunOutputImage - Images attached to the check run output displayed in the GitHub pull request UI.

   alt - The alternative text for the image.

   imageUrl - The full URL of the image.

   caption - A short image description.

   """
   alt: str
   imageUrl: URI
   caption: str

class CheckRunAction(GQLObject):
   """
   CheckRunAction - Possible further actions the integrator can perform.

   label - The text to be displayed on a button in the web UI.

   description - A short explanation of what this action would do.

   identifier - A reference for the action on the integrator's system. 

   """
   label: str
   description: str
   identifier: str

class CheckAnnotationPosition(GQLObject):
   """
   CheckAnnotationPosition - A character position in a check annotation.

   column - Column number (1 indexed).

   line - Line number (1 indexed).

   """
   column: int
   line: int

class CancelSponsorshipInput(GQLObject):
   """
   CancelSponsorshipInput - Autogenerated input type of CancelSponsorship

   sponsorId - The ID of the user or organization who is acting as the sponsor, paying for the sponsorship. Required if sponsorLogin is not given.

   sponsorLogin - The username of the user or organization who is acting as the sponsor, paying for the sponsorship. Required if sponsorId is not given.

   sponsorableId - The ID of the user or organization who is receiving the sponsorship. Required if sponsorableLogin is not given.

   sponsorableLogin - The username of the user or organization who is receiving the sponsorship. Required if sponsorableId is not given.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   sponsorId: ID
   sponsorLogin: str
   sponsorableId: ID
   sponsorableLogin: str
   clientMutationId: str

class CWE(GQLObject):
   """
   CWE - A common weakness enumeration

   cweId - The id of the CWE

   description - A detailed description of this CWE

   name - The name of this CWE

   """
   cweId: str
   description: str
   id: ID
   name: str

class CDIHG_URI_Field(ArguedStr):
   """
   CDIHG_URI_Field - A URL pointing to the GitHub App's public avatar.

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
   environmentIds: NonNull_list[ID]
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

class AddPullRequestReviewThreadInput(GQLObject):
   """
   AddPullRequestReviewThreadInput - Autogenerated input type of AddPullRequestReviewThread

   path - Path to the file being commented on.

   body - Body of the thread's first comment.

   pullRequestId - The node ID of the pull request reviewing

   pullRequestReviewId - The Node ID of the review to modify.

   line - The line of the blob to which the thread refers. The end of the line range for multi-line comments.

   side - The side of the diff on which the line resides. For multi-line comments, this is the side for the end of the line range.

   startLine - The first line of the range to which the comment refers.

   startSide - The side of the diff on which the start line resides.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   path: str
   body: str
   pullRequestId: ID
   pullRequestReviewId: ID
   line: int
   side: DiffSide
   startLine: int
   startSide: DiffSide
   clientMutationId: str

class AddProjectV2ItemByIdInput(GQLObject):
   """
   AddProjectV2ItemByIdInput - Autogenerated input type of AddProjectV2ItemById

   projectId - The ID of the Project to add the item to.

   contentId - The id of the Issue or Pull Request to add.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   contentId: ID
   clientMutationId: str

class AddProjectColumnInput(GQLObject):
   """
   AddProjectColumnInput - Autogenerated input type of AddProjectColumn

   projectId - The Node ID of the project.

   name - The name of the column.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   name: str
   clientMutationId: str

class AddLabelsToLabelableInput(GQLObject):
   """
   AddLabelsToLabelableInput - Autogenerated input type of AddLabelsToLabelable

   labelableId - The id of the labelable object to add labels to.

   labelIds - The ids of the labels to add.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   labelableId: ID
   labelIds: NonNull_list[ID]
   clientMutationId: str

class AddEnterpriseSupportEntitlementInput(GQLObject):
   """
   AddEnterpriseSupportEntitlementInput - Autogenerated input type of AddEnterpriseSupportEntitlement

   enterpriseId - The ID of the Enterprise which the admin belongs to.

   login - The login of a member who will receive the support entitlement.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID
   login: str
   clientMutationId: str

class AddDiscussionPollVoteInput(GQLObject):
   """
   AddDiscussionPollVoteInput - Autogenerated input type of AddDiscussionPollVote

   pollOptionId - The Node ID of the discussion poll option to vote for.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pollOptionId: ID
   clientMutationId: str

class AddCommentInput(GQLObject):
   """
   AddCommentInput - Autogenerated input type of AddComment

   subjectId - The Node ID of the subject to modify.

   body - The contents of the comment.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID
   body: str
   clientMutationId: str

class ActorLocation(GQLObject):
   """
   ActorLocation - Location information for an actor

   city - City

   country - Country name

   countryCode - Country code

   region - Region name

   regionCode - Region or state code

   """
   city: str
   country: str
   countryCode: str
   region: str
   regionCode: str

class Actor(GQLObject):
   """
   Actor - Represents an object which can take actions on GitHub. Typically a User or Bot.

   avatarUrl - A URL pointing to the actor's public avatar.

   login - The username of the actor.

   resourcePath - The HTTP path for this actor.

   url - The HTTP URL for this actor.

   """
   avatarUrl: NYOXP_URI_Field
   login: str
   resourcePath: URI
   url: URI

class AcceptEnterpriseAdministratorInvitationInput(GQLObject):
   """
   AcceptEnterpriseAdministratorInvitationInput - Autogenerated input type of AcceptEnterpriseAdministratorInvitation

   invitationId - The id of the invitation being accepted

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   invitationId: ID
   clientMutationId: str

class AbortQueuedMigrationsInput(GQLObject):
   """
   AbortQueuedMigrationsInput - Autogenerated input type of AbortQueuedMigrations

   ownerId - The ID of the organization that is running the migrations.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID
   clientMutationId: str
