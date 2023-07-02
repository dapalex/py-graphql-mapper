from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class GKZDE_anyPinnableItems_Field(ArguedBool):
   """
   GKZDE_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class ELUXS_URI_Field(ArguedStr):
   """
   ELUXS_URI_Field - URL for the listing's logo image.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class UAPAG_URI_Field(ArguedStr):
   """
   UAPAG_URI_Field - A URL pointing to the app's logo.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting image.

      """
      size: int

   _args: URIArgs



class XESGW_URI_Field(ArguedStr):
   """
   XESGW_URI_Field - A URL pointing to the enterprise's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class EJRFT_HTML_Field(ArguedStr):
   """
   EJRFT_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class CGBUE_URI_Field(ArguedStr):
   """
   CGBUE_URI_Field - A URL pointing to the enterprise user account's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class WDZVA_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   WDZVA_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

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



class VFXER_isSponsoredBy_Field(ArguedBool):
   """
   VFXER_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class CIARF_URI_Field(ArguedStr):
   """
   CIARF_URI_Field - A URL pointing to the organization's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class GWUDW_anyPinnableItems_Field(ArguedBool):
   """
   GWUDW_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class GCQIJ_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   GCQIJ_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

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



class PQKFK_organizationVerifiedDomainEmails_Field(ArguedStr):
   """
   PQKFK_organizationVerifiedDomainEmails_Field - Verified email addresses that match verified domains for a specified organization the user is a member of.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      login - The login of the organization to match verified domains from.

      """
      login: NonNull_str

   _args: strArgs



class RDZXD_isSponsoredBy_Field(ArguedBool):
   """
   RDZXD_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class CTVCB_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedBool):
   """
   CTVCB_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field - Could this user receive email notifications, if the organization had notification restrictions enabled?

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      login - The login of the organization to check.

      """
      login: NonNull_str

   _args: boolArgs



class TFHJP_URI_Field(ArguedStr):
   """
   TFHJP_URI_Field - A URL pointing to the user's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class GDNVE_anyPinnableItems_Field(ArguedBool):
   """
   GDNVE_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class NAJYE_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   NAJYE_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

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



class HUCUJ_isSponsoredBy_Field(ArguedBool):
   """
   HUCUJ_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      accountLogin - The target account's login.

      """
      accountLogin: NonNull_str

   _args: boolArgs



class GSAOA_text_Field(ArguedStr):
   """
   GSAOA_text_Field - UTF8 text data or null if the file is binary

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      truncate - Optionally truncate the returned file to this length.

      """
      truncate: int

   _args: strArgs



class YJUMT_totalRepositoryContributions_Field(ArguedInt):
   """
   YJUMT_totalRepositoryContributions_Field - How many repositories the user created.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first repository ever be excluded from this count.

      """
      excludeFirst: bool

   _args: intArgs



class VBYDY_totalRepositoriesWithContributedPullRequests_Field(ArguedInt):
   """
   VBYDY_totalRepositoriesWithContributedPullRequests_Field - How many different repositories the user opened pull requests in.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class RUUQM_totalRepositoriesWithContributedIssues_Field(ArguedInt):
   """
   RUUQM_totalRepositoriesWithContributedIssues_Field - How many different repositories the user opened issues in.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class DVBKA_totalPullRequestContributions_Field(ArguedInt):
   """
   DVBKA_totalPullRequestContributions_Field - How many pull requests the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class OTBMU_totalIssueContributions_Field(ArguedInt):
   """
   OTBMU_totalIssueContributions_Field - How many issues the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class WLCXL_isRequired_Field(ArguedBool):
   """
   WLCXL_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class GKGVB_URI_Field(ArguedStr):
   """
   GKGVB_URI_Field - The avatar of the OAuth application or the user that created the status

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class MMXLZ_isRequired_Field(ArguedBool):
   """
   MMXLZ_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject):
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class GBTSP_URI_Field(ArguedStr):
   """
   GBTSP_URI_Field - A URL pointing to the author's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class LZPAU_viewerMergeHeadlineText_Field(ArguedStr):
   """
   LZPAU_viewerMergeHeadlineText_Field - The merge headline text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class XCYNJ_viewerMergeBodyText_Field(ArguedStr):
   """
   XCYNJ_viewerMergeBodyText_Field - The merge body text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject):
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class LOVOZ_URI_Field(ArguedStr):
   """
   LOVOZ_URI_Field - A URL pointing to the team's avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class ERHFD_trackedIssuesCount_Field(ArguedInt):
   """
   ERHFD_trackedIssuesCount_Field - The number of tracked issues for this issue

   """
   class intArgs(GQLArgsSet, GQLObject):
      """
      states - Limit the count to tracked issues with the specified states.

      """
      states: list[TrackedIssueStates]

   _args: intArgs



class SMDTK_HTML_Field(ArguedStr):
   """
   SMDTK_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class OSBRE_URI_Field(ArguedStr):
   """
   OSBRE_URI_Field - A URL pointing to the owner's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class XWDQC_HTML_Field(ArguedStr):
   """
   XWDQC_HTML_Field - A description of the release, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject):
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class GWXQC_URI_Field(ArguedStr):
   """
   GWXQC_URI_Field - A URL pointing to the GitHub App's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class JYIAS_URI_Field(ArguedStr):
   """
   JYIAS_URI_Field - A URL pointing to the actor's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject):
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class MGRFS_isRequired_Field(ArguedBool):
   """
   MGRFS_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

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
   requiredDeploymentEnvironments: list[str]

class RequirableByPullRequest(GQLObject):
   """
   RequirableByPullRequest - Represents a type that can be required by a pull request for merging.

   isRequired - Whether this is required to pass before merging for a specific pull request.

   """
   isRequired: MGRFS_isRequired_Field

class RepositoryRulesetBypassActorInput(GQLObject):
   """
   RepositoryRulesetBypassActorInput - Specifies the attributes for a new or updated ruleset bypass actor. Only one of `actor_id`, `repository_role_database_id`, or `organization_admin` should be specified.

   actorId - For Team and Integration bypasses, the Team or Integration ID

   repositoryRoleDatabaseId - For role bypasses, the role database ID

   organizationAdmin - For org admin bupasses, true

   bypassMode - The bypass mode for this actor.

   """
   actorId: ID
   repositoryRoleDatabaseId: int
   organizationAdmin: bool
   bypassMode: RepositoryRulesetBypassActorBypassMode

class RepositoryNameConditionTargetInput(GQLObject):
   """
   RepositoryNameConditionTargetInput - Parameters to be used for the repository_name condition

   exclude - Array of repository names or patterns to exclude. The condition will not pass if any of these patterns match.

   include - Array of repository names or patterns to include. One of these patterns must match for the condition to pass. Also accepts `~ALL` to include all repositories.

   protected - Target changes that match these patterns will be prevented except by those with bypass permissions.

   """
   exclude: list[str]
   include: list[str]
   protected: bool

class RepositoryMigrationOrder(GQLObject):
   """
   RepositoryMigrationOrder - Ordering options for repository migrations.

   field - The field to order repository migrations by.

   direction - The ordering direction.

   """
   field: RepositoryMigrationOrderField
   direction: RepositoryMigrationOrderDirection

class RepositoryInteractionAbility(GQLObject):
   """
   RepositoryInteractionAbility - Repository interaction limit that applies to this object.

   expiresAt - The time the currently active limit expires.

   limit - The current limit that is enabled on this object.

   origin - The origin of the currently active interaction limit.

   """
   expiresAt: DateTime
   limit: RepositoryInteractionLimit
   origin: RepositoryInteractionLimitOrigin

class RepositoryIdConditionTarget(GQLObject):
   """
   RepositoryIdConditionTarget - Parameters to be used for the repository_id condition

   repositoryIds - One of these repo IDs must match the repo.

   """
   repositoryIds: list[ID]

class RepositoryCodeownersError(GQLObject):
   """
   RepositoryCodeownersError - An error in a `CODEOWNERS` file.

   column - The column number where the error occurs.

   kind - A short string describing the type of error.

   line - The line number where the error occurs.

   message - A complete description of the error, combining information from other fields.

   path - The path to the file when the error occurs.

   source - The content of the line where the error occurs.

   suggestion - A suggestion of how to fix the error.

   """
   column: int
   kind: str
   line: int
   message: str
   path: str
   source: str
   suggestion: str

class ReopenIssueInput(GQLObject):
   """
   ReopenIssueInput - Autogenerated input type of ReopenIssue

   issueId - ID of the issue to be opened.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID
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
   labelIds: list[ID]
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

class RefNameConditionTarget(GQLObject):
   """
   RefNameConditionTarget - Parameters to be used for the ref_name condition

   exclude - Array of ref names or patterns to exclude. The condition will not pass if any of these patterns match.

   include - Array of ref names or patterns to include. One of these patterns must match for the condition to pass. Also accepts `~DEFAULT_BRANCH` to include the default branch or `~ALL` to include all branches.

   """
   exclude: list[str]
   include: list[str]

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

class PullRequestParameters(GQLObject):
   """
   PullRequestParameters - Require all commits be made to a non-target branch and submitted via a pull request before they can be merged.

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

class ProjectV2ViewOrder(GQLObject):
   """
   ProjectV2ViewOrder - Ordering options for project v2 view connections

   field - The field to order the project v2 views by.

   direction - The ordering direction.

   """
   field: ProjectV2ViewOrderField
   direction: OrderDirection

class ProjectV2SingleSelectFieldOption(GQLObject):
   """
   ProjectV2SingleSelectFieldOption - Single select field option for a configuration for a project.

   color - The option's display color.

   description - The option's plain-text description.

   descriptionHTML - The option's description, possibly containing HTML.

   id - The option's ID.

   name - The option's name.

   nameHTML - The option's html name.

   """
   color: ProjectV2SingleSelectFieldOptionColor
   description: str
   descriptionHTML: str
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

class ProjectV2Collaborator(GQLObject):
   """
   ProjectV2Collaborator - A collaborator to update on a project. Only one of the userId or teamId should be provided.

   userId - The ID of the user as a collaborator.

   teamId - The ID of the team as a collaborator.

   role - The role to grant the collaborator

   """
   userId: ID
   teamId: ID
   role: ProjectV2Roles

class ProjectOrder(GQLObject):
   """
   ProjectOrder - Ways in which lists of projects can be ordered upon return.

   field - The field in which to order projects by.

   direction - The direction in which to order projects by the specified field.

   """
   field: ProjectOrderField
   direction: OrderDirection

class PageInfo(GQLObject):
   """
   PageInfo - Information about pagination in a connection.

   endCursor - When paginating forwards, the cursor to continue.

   hasNextPage - When paginating forwards, are there more items?

   hasPreviousPage - When paginating backwards, are there more items?

   startCursor - When paginating backwards, the cursor to continue.

   """
   endCursor: str
   hasNextPage: bool
   hasPreviousPage: bool
   startCursor: str

class PackageVersionOrder(GQLObject):
   """
   PackageVersionOrder - Ways in which lists of package versions can be ordered upon return.

   field - The field in which to order package versions by.

   direction - The direction in which to order package versions by the specified field.

   """
   field: PackageVersionOrderField
   direction: OrderDirection

class PackageOrder(GQLObject):
   """
   PackageOrder - Ways in which lists of packages can be ordered upon return.

   field - The field in which to order packages by.

   direction - The direction in which to order packages by the specified field.

   """
   field: PackageOrderField
   direction: OrderDirection

class OrganizationOrder(GQLObject):
   """
   OrganizationOrder - Ordering options for organization connections.

   field - The field to order organizations by.

   direction - The ordering direction.

   """
   field: OrganizationOrderField
   direction: OrderDirection

class OrgEnterpriseOwnerOrder(GQLObject):
   """
   OrgEnterpriseOwnerOrder - Ordering options for an organization's enterprise owner connections.

   field - The field to order enterprise owners by.

   direction - The ordering direction.

   """
   field: OrgEnterpriseOwnerOrderField
   direction: OrderDirection

class Node(GQLObject):
   """
   Node - An object with an ID.

   id - ID of the object.

   """
   id: ID

class MoveProjectCardInput(GQLObject):
   """
   MoveProjectCardInput - Autogenerated input type of MoveProjectCard

   cardId - The id of the card to move.

   columnId - The id of the column to move it into.

   afterCardId - Place the new card after the card with this id. Pass null to place it at the top.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   cardId: ID
   columnId: ID
   afterCardId: ID
   clientMutationId: str

class Minimizable(GQLObject):
   """
   Minimizable - Entities that can be minimized.

   isMinimized - Returns whether or not a comment has been minimized.

   minimizedReason - Returns why the comment was minimized. One of `abuse`, `off-topic`, `outdated`, `resolved`, `duplicate` and `spam`. Note that the case and formatting of these values differs from the inputs to the `MinimizeComment` mutation.

   viewerCanMinimize - Check if the current viewer can minimize this object.

   """
   isMinimized: bool
   minimizedReason: str
   viewerCanMinimize: bool

class MigrationSource(GQLObject):
   """
   MigrationSource - A GitHub Enterprise Importer (GEI) migration source.

   name - The migration source name.

   type - The migration source type.

   url - The migration source URL, for example `https://github.com` or `https://monalisa.ghe.com`.

   """
   id: ID
   name: str
   type: MigrationSourceType
   url: URI

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

class MarkProjectV2AsTemplateInput(GQLObject):
   """
   MarkProjectV2AsTemplateInput - Autogenerated input type of MarkProjectV2AsTemplate

   projectId - The ID of the Project to mark as a template.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   clientMutationId: str

class MarkDiscussionCommentAsAnswerInput(GQLObject):
   """
   MarkDiscussionCommentAsAnswerInput - Autogenerated input type of MarkDiscussionCommentAsAnswer

   id - The Node ID of the discussion comment to mark as an answer.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID
   clientMutationId: str

class Lockable(GQLObject):
   """
   Lockable - An object that can be locked.

   activeLockReason - Reason that the conversation was locked.

   locked - `true` if the object is locked

   """
   activeLockReason: LockReason
   locked: bool

class LinkRepositoryToProjectInput(GQLObject):
   """
   LinkRepositoryToProjectInput - Autogenerated input type of LinkRepositoryToProject

   projectId - The ID of the Project to link to a Repository

   repositoryId - The ID of the Repository to link to a Project.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   repositoryId: ID
   clientMutationId: str

class LinkProjectV2ToRepositoryInput(GQLObject):
   """
   LinkProjectV2ToRepositoryInput - Autogenerated input type of LinkProjectV2ToRepository

   projectId - The ID of the project to link to the repository.

   repositoryId - The ID of the repository to link to the project.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   repositoryId: ID
   clientMutationId: str

class LanguageOrder(GQLObject):
   """
   LanguageOrder - Ordering options for language connections.

   field - The field to order languages by.

   direction - The ordering direction.

   """
   field: LanguageOrderField
   direction: OrderDirection

class LabelOrder(GQLObject):
   """
   LabelOrder - Ways in which lists of labels can be ordered upon return.

   field - The field in which to order labels by.

   direction - The direction in which to order labels by the specified field.

   """
   field: LabelOrderField
   direction: OrderDirection

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

   discussionId - The ID of the discussion to which the comment belongs.

   body - The content of the comment.

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

class CGAIP_URI_Field(ArguedStr):
   """
   CGAIP_URI_Field - A URL pointing to the GitHub App's public avatar.

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

class AddPullRequestReviewThreadInput(GQLObject):
   """
   AddPullRequestReviewThreadInput - Autogenerated input type of AddPullRequestReviewThread

   path - Path to the file being commented on.

   body - Body of the thread's first comment.

   pullRequestId - The node ID of the pull request reviewing

   pullRequestReviewId - The Node ID of the review to modify.

   line - The line of the blob to which the thread refers, required for line-level threads. The end of the line range for multi-line comments.

   side - The side of the diff on which the line resides. For multi-line comments, this is the side for the end of the line range.

   startLine - The first line of the range to which the comment refers.

   startSide - The side of the diff on which the start line resides.

   subjectType - The level at which the comments in the corresponding thread are targeted, can be a diff line or a file

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
   subjectType: PullRequestReviewThreadSubjectType
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
   labelIds: list[ID]
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
   avatarUrl: JYIAS_URI_Field
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
