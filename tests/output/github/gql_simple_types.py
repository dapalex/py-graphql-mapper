from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class IIUPE_anyPinnableItems_Field(ArguedBool):
   """
   IIUPE_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class GIOMU_URI_Field(ArguedStr):
   """
   GIOMU_URI_Field - URL for the listing's logo image.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class PWOWW_URI_Field(ArguedStr):
   """
   PWOWW_URI_Field - A URL pointing to the app's logo.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting image.

      """
      size: int

   _args: URIArgs



class PLGTO_URI_Field(ArguedStr):
   """
   PLGTO_URI_Field - A URL pointing to the enterprise's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class DXFGM_HTML_Field(ArguedStr):
   """
   DXFGM_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class BWRND_URI_Field(ArguedStr):
   """
   BWRND_URI_Field - A URL pointing to the enterprise user account's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class NQEOB_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   NQEOB_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

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



class IEDTD_isSponsoredBy_Field(ArguedBool):
   """
   IEDTD_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class AFLXZ_URI_Field(ArguedStr):
   """
   AFLXZ_URI_Field - A URL pointing to the organization's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class OAWAA_anyPinnableItems_Field(ArguedBool):
   """
   OAWAA_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class CZSIC_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   CZSIC_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

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



class GMPXD_organizationVerifiedDomainEmails_Field(ArguedStr):
   """
   GMPXD_organizationVerifiedDomainEmails_Field - Verified email addresses that match verified domains for a specified organization the user is a member of.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      login - The login of the organization to match verified domains from.

      """
      login: NonNull_str

   _args: strArgs



class YGUAG_isSponsoredBy_Field(ArguedBool):
   """
   YGUAG_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class FLIOJ_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedBool):
   """
   FLIOJ_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field - Could this user receive email notifications, if the organization had notification restrictions enabled?

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      login - The login of the organization to check.

      """
      login: NonNull_str

   _args: boolArgs



class ZAPPC_URI_Field(ArguedStr):
   """
   ZAPPC_URI_Field - A URL pointing to the user's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class PNVQQ_anyPinnableItems_Field(ArguedBool):
   """
   PNVQQ_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class IMEYM_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   IMEYM_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

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



class BJQQY_isSponsoredBy_Field(ArguedBool):
   """
   BJQQY_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class BKGQY_text_Field(ArguedStr):
   """
   BKGQY_text_Field - UTF8 text data or null if the file is binary

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      truncate - Optionally truncate the returned file to this length.

      """
      truncate: int

   _args: strArgs



class SRQMT_totalRepositoryContributions_Field(ArguedInt):
   """
   SRQMT_totalRepositoryContributions_Field - How many repositories the user created.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first repository ever be excluded from this count.

      """
      excludeFirst: bool

   _args: intArgs



class MOMMP_totalRepositoriesWithContributedPullRequests_Field(ArguedInt):
   """
   MOMMP_totalRepositoriesWithContributedPullRequests_Field - How many different repositories the user opened pull requests in.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class CNFSS_totalRepositoriesWithContributedIssues_Field(ArguedInt):
   """
   CNFSS_totalRepositoriesWithContributedIssues_Field - How many different repositories the user opened issues in.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class AITRO_totalPullRequestContributions_Field(ArguedInt):
   """
   AITRO_totalPullRequestContributions_Field - How many pull requests the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class RSTAH_totalIssueContributions_Field(ArguedInt):
   """
   RSTAH_totalIssueContributions_Field - How many issues the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class CEQHT_isRequired_Field(ArguedBool):
   """
   CEQHT_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class OKVTM_URI_Field(ArguedStr):
   """
   OKVTM_URI_Field - The avatar of the OAuth application or the user that created the status

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class LGVHD_isRequired_Field(ArguedBool):
   """
   LGVHD_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class CBCGA_URI_Field(ArguedStr):
   """
   CBCGA_URI_Field - A URL pointing to the author's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class IPEID_viewerMergeHeadlineText_Field(ArguedStr):
   """
   IPEID_viewerMergeHeadlineText_Field - The merge headline text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class ZZUHH_viewerMergeBodyText_Field(ArguedStr):
   """
   ZZUHH_viewerMergeBodyText_Field - The merge body text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class LWSZC_URI_Field(ArguedStr):
   """
   LWSZC_URI_Field - A URL pointing to the team's avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class XXUWK_trackedIssuesCount_Field(ArguedInt):
   """
   XXUWK_trackedIssuesCount_Field - The number of tracked issues for this issue

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      states - Limit the count to tracked issues with the specified states.

      """
      states: list[TrackedIssueStates]

   _args: intArgs



class YWVQU_HTML_Field(ArguedStr):
   """
   YWVQU_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class ZHCJX_URI_Field(ArguedStr):
   """
   ZHCJX_URI_Field - A URL pointing to the owner's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class MBTHR_HTML_Field(ArguedStr):
   """
   MBTHR_HTML_Field - A description of the release, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class IBHQI_URI_Field(ArguedStr):
   """
   IBHQI_URI_Field - A URL pointing to the GitHub App's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class WJGOX_URI_Field(ArguedStr):
   """
   WJGOX_URI_Field - A URL pointing to the GitHub App's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class HHFTU_isRequired_Field(ArguedBool):
   """
   HHFTU_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

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

class Submodule(GQLObject):
   """
   Submodule - A pointer to a repository at a specific revision embedded inside another repository.

   branch - The branch of the upstream submodule for tracking updates

   gitUrl - The git URL of the submodule repository

   name - The name of the submodule in .gitmodules

   nameRaw - The name of the submodule in .gitmodules (Base64-encoded)

   path - The path in the superproject that this submodule is located in

   pathRaw - The path in the superproject that this submodule is located in (Base64-encoded)

   subprojectCommitOid - The commit revision of the subproject repository being tracked by the submodule

   """
   branch: str
   gitUrl: URI
   name: str
   nameRaw: Base64String
   path: str
   pathRaw: Base64String
   subprojectCommitOid: GitObjectID

class StatusContextStateCount(GQLObject):
   """
   StatusContextStateCount - Represents a count of the state of a status context.

   count - The number of statuses with this state.

   state - The state of a status context.

   """
   count: int
   state: StatusState

class StatusCheckConfiguration(GQLObject):
   """
   StatusCheckConfiguration - Required status check

   context - The status check context name that must be present on the commit.

   integrationId - The optional integration ID that this status check must originate from.

   """
   context: str
   integrationId: int

class StartOrganizationMigrationInput(GQLObject):
   """
   StartOrganizationMigrationInput - Autogenerated input type of StartOrganizationMigration

   sourceOrgUrl - The URL of the organization to migrate.

   targetOrgName - The name of the target organization.

   targetEnterpriseId - The ID of the enterprise the target organization belongs to.

   sourceAccessToken - The migration source access token.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   sourceOrgUrl: URI
   targetOrgName: str
   targetEnterpriseId: ID
   sourceAccessToken: str
   clientMutationId: str

class SponsorshipOrder(GQLObject):
   """
   SponsorshipOrder - Ordering options for sponsorship connections.

   field - The field to order sponsorship by.

   direction - The ordering direction.

   """
   field: SponsorshipOrderField
   direction: OrderDirection

class SponsorsTierOrder(GQLObject):
   """
   SponsorsTierOrder - Ordering options for Sponsors tiers connections.

   field - The field to order tiers by.

   direction - The ordering direction.

   """
   field: SponsorsTierOrderField
   direction: OrderDirection

class SponsorsActivityOrder(GQLObject):
   """
   SponsorsActivityOrder - Ordering options for GitHub Sponsors activity connections.

   field - The field to order activity by.

   direction - The ordering direction.

   """
   field: SponsorsActivityOrderField
   direction: OrderDirection

class SponsorOrder(GQLObject):
   """
   SponsorOrder - Ordering options for connections to get sponsor entities for GitHub Sponsors.

   field - The field to order sponsor entities by.

   direction - The ordering direction.

   """
   field: SponsorOrderField
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

class RequiredDeploymentsParameters(GQLObject):
   """
   RequiredDeploymentsParameters - Choose which environments must be successfully deployed to before branches can be merged into a branch that matches this rule.

   requiredDeploymentEnvironments - The environments that must be successfully deployed to before branches can be merged.

   """
   requiredDeploymentEnvironments: NonNull_list[str]

class RequirableByPullRequest(GQLObject):
   """
   RequirableByPullRequest - Represents a type that can be required by a pull request for merging.

   isRequired - Whether this is required to pass before merging for a specific pull request.

   """
   isRequired: HHFTU_isRequired_Field

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
   exclude: NonNull_list[str]
   include: NonNull_list[str]
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
   repositoryIds: NonNull_list[ID]

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
   assigneeIds: NonNull_list[ID]
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
   environmentIds: NonNull_list[ID]
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
   exclude: NonNull_list[str]
   include: NonNull_list[str]

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

class EnterpriseServerUserAccountsUploadOrder(GQLObject):
   """
   EnterpriseServerUserAccountsUploadOrder - Ordering options for Enterprise Server user accounts upload connections.

   field - The field to order user accounts uploads by.

   direction - The ordering direction.

   """
   field: EnterpriseServerUserAccountsUploadOrderField
   direction: OrderDirection

class EnterpriseServerUserAccountEmailOrder(GQLObject):
   """
   EnterpriseServerUserAccountEmailOrder - Ordering options for Enterprise Server user account email connections.

   field - The field to order emails by.

   direction - The ordering direction.

   """
   field: EnterpriseServerUserAccountEmailOrderField
   direction: OrderDirection

class EnterpriseRepositoryInfo(GQLObject):
   """
   EnterpriseRepositoryInfo - A subset of repository information queryable from an enterprise.

   isPrivate - Identifies if the repository is private or internal.

   name - The repository's name.

   nameWithOwner - The repository's name with owner.

   """
   id: ID
   isPrivate: bool
   name: str
   nameWithOwner: str

class EnterpriseBillingInfo(GQLObject):
   """
   EnterpriseBillingInfo - Enterprise billing information visible to enterprise billing managers and owners.

   allLicensableUsersCount - The number of licenseable users/emails across the enterprise.

   assetPacks - The number of data packs used by all organizations owned by the enterprise.

   bandwidthQuota - The bandwidth quota in GB for all organizations owned by the enterprise.

   bandwidthUsage - The bandwidth usage in GB for all organizations owned by the enterprise.

   bandwidthUsagePercentage - The bandwidth usage as a percentage of the bandwidth quota.

   storageQuota - The storage quota in GB for all organizations owned by the enterprise.

   storageUsage - The storage usage in GB for all organizations owned by the enterprise.

   storageUsagePercentage - The storage usage as a percentage of the storage quota.

   totalAvailableLicenses - The number of available licenses across all owned organizations based on the unique number of billable users.

   totalLicenses - The total number of licenses allocated.

   """
   allLicensableUsersCount: int
   assetPacks: int
   bandwidthQuota: float
   bandwidthUsage: float
   bandwidthUsagePercentage: int
   storageQuota: float
   storageUsage: float
   storageUsagePercentage: int
   totalAvailableLicenses: int
   totalLicenses: int

class EnterpriseAdministratorInvitationOrder(GQLObject):
   """
   EnterpriseAdministratorInvitationOrder - Ordering options for enterprise administrator invitation connections

   field - The field to order enterprise administrator invitations by.

   direction - The ordering direction.

   """
   field: EnterpriseAdministratorInvitationOrderField
   direction: OrderDirection

class EnablePullRequestAutoMergeInput(GQLObject):
   """
   EnablePullRequestAutoMergeInput - Autogenerated input type of EnablePullRequestAutoMerge

   pullRequestId - ID of the pull request to enable auto-merge on.

   commitHeadline - Commit headline to use for the commit when the PR is mergable; if omitted, a default message will be used. NOTE: when merging with a merge queue any input value for commit headline is ignored.

   commitBody - Commit body to use for the commit when the PR is mergable; if omitted, a default message will be used. NOTE: when merging with a merge queue any input value for commit message is ignored.

   mergeMethod - The merge method to use. If omitted, defaults to `MERGE`. NOTE: when merging with a merge queue any input value for merge method is ignored.

   authorEmail - The email address to associate with this merge.

   expectedHeadOid - The expected head OID of the pull request.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   commitHeadline: str
   commitBody: str
   mergeMethod: PullRequestMergeMethod
   authorEmail: str
   expectedHeadOid: GitObjectID
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

class DequeuePullRequestInput(GQLObject):
   """
   DequeuePullRequestInput - Autogenerated input type of DequeuePullRequest

   id - The ID of the pull request to be dequeued.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class DeployKey(GQLObject):
   """
   DeployKey - A repository deploy key.

   createdAt - Identifies the date and time when the object was created.

   key - The deploy key.

   readOnly - Whether or not the deploy key is read only.

   title - The deploy key title.

   verified - Whether or not the deploy key has been verified.

   """
   createdAt: DateTime
   id: ID
   key: str
   readOnly: bool
   title: str
   verified: bool

class DeleteVerifiableDomainInput(GQLObject):
   """
   DeleteVerifiableDomainInput - Autogenerated input type of DeleteVerifiableDomain

   id - The ID of the verifiable domain to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class DeleteTeamDiscussionInput(GQLObject):
   """
   DeleteTeamDiscussionInput - Autogenerated input type of DeleteTeamDiscussion

   id - The discussion ID to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class DeleteTeamDiscussionCommentInput(GQLObject):
   """
   DeleteTeamDiscussionCommentInput - Autogenerated input type of DeleteTeamDiscussionComment

   id - The ID of the comment to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class DeleteRepositoryRulesetInput(GQLObject):
   """
   DeleteRepositoryRulesetInput - Autogenerated input type of DeleteRepositoryRuleset

   repositoryRulesetId - The global relay id of the repository ruleset to be deleted.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryRulesetId: ID
   clientMutationId: str

class DeleteRefInput(GQLObject):
   """
   DeleteRefInput - Autogenerated input type of DeleteRef

   refId - The Node ID of the Ref to be deleted.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   refId: ID
   clientMutationId: str

class DeletePullRequestReviewCommentInput(GQLObject):
   """
   DeletePullRequestReviewCommentInput - Autogenerated input type of DeletePullRequestReviewComment

   id - The ID of the comment to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class DeleteProjectV2ItemPayload(GQLObject):
   """
   DeleteProjectV2ItemPayload - Autogenerated return type of DeleteProjectV2Item

   clientMutationId - A unique identifier for the client performing the mutation.

   deletedItemId - The ID of the deleted item.

   """
   clientMutationId: str
   deletedItemId: ID

class DeleteProjectV2Input(GQLObject):
   """
   DeleteProjectV2Input - Autogenerated input type of DeleteProjectV2

   projectId - The ID of the Project to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   clientMutationId: str

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

class ConvertPullRequestToDraftInput(GQLObject):
   """
   ConvertPullRequestToDraftInput - Autogenerated input type of ConvertPullRequestToDraft

   pullRequestId - ID of the pull request to convert to draft

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   clientMutationId: str

class ContributionOrder(GQLObject):
   """
   ContributionOrder - Ordering options for contribution connections.

   direction - The ordering direction.

   """
   direction: OrderDirection

class ContributionCalendarDay(GQLObject):
   """
   ContributionCalendarDay - Represents a single day of contributions on GitHub by a user.

   color - The hex color code that represents how many contributions were made on this day compared to others in the calendar.

   contributionCount - How many contributions were made by the user on this day.

   contributionLevel - Indication of contributions, relative to other days. Can be used to indicate which color to represent this day on a calendar.

   date - The day this square represents.

   weekday - A number representing which day of the week this square represents, e.g., 1 is Monday.

   """
   color: str
   contributionCount: int
   contributionLevel: ContributionLevel
   date: Date
   weekday: int

class CommitterEmailPatternParameters(GQLObject):
   """
   CommitterEmailPatternParameters - Parameters to be used for the committer_email_pattern rule

   name - How this rule will appear to users.

   negate - If true, the rule will fail if the pattern matches.

   operator - The operator to use for matching.

   pattern - The pattern to match with.

   """
   name: str
   negate: bool
   operator: str
   pattern: str

class CommitMessagePatternParametersInput(GQLObject):
   """
   CommitMessagePatternParametersInput - Parameters to be used for the commit_message_pattern rule

   name - How this rule will appear to users.

   negate - If true, the rule will fail if the pattern matches.

   operator - The operator to use for matching.

   pattern - The pattern to match with.

   """
   name: str
   negate: bool
   operator: str
   pattern: str

class CommitMessage(GQLObject):
   """
   CommitMessage - A message to include with a new commit

   headline - The headline of the message.

   body - The body of the message.

   """
   headline: str
   body: str

class CommitAuthorEmailPatternParametersInput(GQLObject):
   """
   CommitAuthorEmailPatternParametersInput - Parameters to be used for the commit_author_email_pattern rule

   name - How this rule will appear to users.

   negate - If true, the rule will fail if the pattern matches.

   operator - The operator to use for matching.

   pattern - The pattern to match with.

   """
   name: str
   negate: bool
   operator: str
   pattern: str

class CommitAuthor(GQLObject):
   """
   CommitAuthor - Specifies an author for filtering Git commits.

   id - ID of a User to filter by. If non-null, only commits authored by this user will be returned. This field takes precedence over emails.

   emails - Email addresses to filter by. Commits authored by any of the specified email addresses will be returned.

   """
   id: ID
   emails: list[str]

class ClosePullRequestInput(GQLObject):
   """
   ClosePullRequestInput - Autogenerated input type of ClosePullRequest

   pullRequestId - ID of the pull request to be closed.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   clientMutationId: str

class CloseDiscussionInput(GQLObject):
   """
   CloseDiscussionInput - Autogenerated input type of CloseDiscussion

   discussionId - ID of the discussion to be closed.

   reason - The reason why the discussion is being closed.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   discussionId: ID
   reason: DiscussionCloseReason
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

class BulkSponsorship(GQLObject):
   """
   BulkSponsorship - Information about a sponsorship to make for a user or organization with a GitHub Sponsors profile, as part of sponsoring many users or organizations at once.

   sponsorableId - The ID of the user or organization who is receiving the sponsorship. Required if sponsorableLogin is not given.

   sponsorableLogin - The username of the user or organization who is receiving the sponsorship. Required if sponsorableId is not given.

   amount - The amount to pay to the sponsorable in US dollars. Valid values: 1-12000.

   """
   sponsorableId: ID
   sponsorableLogin: str
   amount: int

class BranchNamePatternParameters(GQLObject):
   """
   BranchNamePatternParameters - Parameters to be used for the branch_name_pattern rule

   name - How this rule will appear to users.

   negate - If true, the rule will fail if the pattern matches.

   operator - The operator to use for matching.

   pattern - The pattern to match with.

   """
   name: str
   negate: bool
   operator: str
   pattern: str

class Bot(GQLObject):
   """
   Bot - A special type of user which takes actions on behalf of GitHub Apps.

   avatarUrl - A URL pointing to the GitHub App's public avatar.

   createdAt - Identifies the date and time when the object was created.

   databaseId - Identifies the primary key from the database.

   login - The username of the actor.

   resourcePath - The HTTP path for this bot

   updatedAt - Identifies the date and time when the object was last updated.

   url - The HTTP URL for this bot

   """
   avatarUrl: WJGOX_URI_Field
   createdAt: DateTime
   databaseId: int
   id: ID
   login: str
   resourcePath: URI
   updatedAt: DateTime
   url: URI

class ArchiveRepositoryInput(GQLObject):
   """
   ArchiveRepositoryInput - Autogenerated input type of ArchiveRepository

   repositoryId - The ID of the repository to mark as archived.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID
   clientMutationId: str

class ApproveVerifiableDomainInput(GQLObject):
   """
   ApproveVerifiableDomainInput - Autogenerated input type of ApproveVerifiableDomain

   id - The ID of the verifiable domain to approve.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class AnnouncementBanner(GQLObject):
   """
   AnnouncementBanner - Represents an announcement banner.

   announcement - The text of the announcement

   announcementExpiresAt - The expiration date of the announcement, if any

   announcementUserDismissible - Whether the announcement can be dismissed by the user

   """
   announcement: str
   announcementExpiresAt: DateTime
   announcementUserDismissible: bool

class AddUpvoteInput(GQLObject):
   """
   AddUpvoteInput - Autogenerated input type of AddUpvote

   subjectId - The Node ID of the discussion or comment to upvote.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID
   clientMutationId: str

class AddReactionInput(GQLObject):
   """
   AddReactionInput - Autogenerated input type of AddReaction

   subjectId - The Node ID of the subject to modify.

   content - The name of the emoji to react with.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID
   content: ReactionContent
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
   userIds: NonNull_list[ID]
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
   assigneeIds: NonNull_list[ID]
   clientMutationId: str

class BERYZ_URI_Field(ArguedStr):
   """
   BERYZ_URI_Field - A URL pointing to the actor's public avatar.

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
