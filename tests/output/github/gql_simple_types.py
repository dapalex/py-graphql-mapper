from typing import Generic
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import ID
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *

class UXJAB_anyPinnableItems_Field(ArguedStr):
   """
   UXJAB_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class ALODJ_URI_Field(ArguedStr):
   """
   ALODJ_URI_Field - URL for the listing's logo image.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class DYGLW_URI_Field(ArguedStr):
   """
   DYGLW_URI_Field - A URL pointing to the app's logo.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting image.

      """
      size: int

   _args: URIArgs



class VOLFL_URI_Field(ArguedStr):
   """
   VOLFL_URI_Field - A URL pointing to the enterprise's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class UNYTI_HTML_Field(ArguedStr):
   """
   UNYTI_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject): 
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class MTNOK_URI_Field(ArguedStr):
   """
   MTNOK_URI_Field - A URL pointing to the enterprise user account's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class EUXHN_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   EUXHN_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      since - Filter payments to those that occurred on or after this time.

      until - Filter payments to those that occurred before this time.

      sponsorableLogins - Filter payments to those made to the users or organizations with the specified usernames.

      """
      since: DateTime
      until: DateTime
      sponsorableLogins: str ##NON NULL ##LIST

   _args: intArgs



class TTPUG_isSponsoredBy_Field(ArguedStr):
   """
   TTPUG_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      accountLogin - The target account's login.

      """
      accountLogin: str ##NON NULL

   _args: boolArgs



class WHEVD_URI_Field(ArguedStr):
   """
   WHEVD_URI_Field - A URL pointing to the organization's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class XZHWE_anyPinnableItems_Field(ArguedStr):
   """
   XZHWE_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class UUKAP_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   UUKAP_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      since - Filter payments to those that occurred on or after this time.

      until - Filter payments to those that occurred before this time.

      sponsorableLogins - Filter payments to those made to the users or organizations with the specified usernames.

      """
      since: DateTime
      until: DateTime
      sponsorableLogins: str ##NON NULL ##LIST

   _args: intArgs



class ENEBF_organizationVerifiedDomainEmails_Field(ArguedStr):
   """
   ENEBF_organizationVerifiedDomainEmails_Field - Verified email addresses that match verified domains for a specified organization the user is a member of.

   """
   class strArgs(GQLArgsSet, GQLObject): 
      """
      login - The login of the organization to match verified domains from.

      """
      login: str ##NON NULL

   _args: strArgs



class YHNJR_isSponsoredBy_Field(ArguedStr):
   """
   YHNJR_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      accountLogin - The target account's login.

      """
      accountLogin: str ##NON NULL

   _args: boolArgs



class YXVRA_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedStr):
   """
   YXVRA_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field - Could this user receive email notifications, if the organization had notification restrictions enabled?

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      login - The login of the organization to check.

      """
      login: str ##NON NULL

   _args: boolArgs



class AGGPK_URI_Field(ArguedStr):
   """
   AGGPK_URI_Field - A URL pointing to the user's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class SVOHV_anyPinnableItems_Field(ArguedStr):
   """
   SVOHV_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class CWCIG_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   """
   CWCIG_totalSponsorshipAmountAsSponsorInCents_Field - The amount in United States cents (e.g., 500 = $5.00 USD) that this entity has spent on GitHub to fund sponsorships. Only returns a value when viewed by the user themselves or by a user who can manage sponsorships for the requested organization.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      since - Filter payments to those that occurred on or after this time.

      until - Filter payments to those that occurred before this time.

      sponsorableLogins - Filter payments to those made to the users or organizations with the specified usernames.

      """
      since: DateTime
      until: DateTime
      sponsorableLogins: str ##NON NULL ##LIST

   _args: intArgs



class AGHTX_isSponsoredBy_Field(ArguedStr):
   """
   AGHTX_isSponsoredBy_Field - Whether the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      accountLogin - The target account's login.

      """
      accountLogin: str ##NON NULL

   _args: boolArgs



class XJEXO_text_Field(ArguedStr):
   """
   XJEXO_text_Field - UTF8 text data or null if the file is binary

   """
   class strArgs(GQLArgsSet, GQLObject): 
      """
      truncate - Optionally truncate the returned file to this length.

      """
      truncate: int

   _args: strArgs



class BKRKE_totalRepositoryContributions_Field(ArguedStr):
   """
   BKRKE_totalRepositoryContributions_Field - How many repositories the user created.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      excludeFirst - Should the user's first repository ever be excluded from this count.

      """
      excludeFirst: bool

   _args: intArgs



class UMCSI_totalRepositoriesWithContributedPullRequests_Field(ArguedStr):
   """
   UMCSI_totalRepositoriesWithContributedPullRequests_Field - How many different repositories the user opened pull requests in.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class RYNDA_totalRepositoriesWithContributedIssues_Field(ArguedStr):
   """
   RYNDA_totalRepositoriesWithContributedIssues_Field - How many different repositories the user opened issues in.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class QNSMI_totalPullRequestContributions_Field(ArguedStr):
   """
   QNSMI_totalPullRequestContributions_Field - How many pull requests the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class FAFSY_totalIssueContributions_Field(ArguedStr):
   """
   FAFSY_totalIssueContributions_Field - How many issues the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class LVRNI_isRequired_Field(ArguedStr):
   """
   LVRNI_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class AECPA_URI_Field(ArguedStr):
   """
   AECPA_URI_Field - The avatar of the OAuth application or the user that created the status

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class ZBYJX_isRequired_Field(ArguedStr):
   """
   ZBYJX_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class BMGAY_URI_Field(ArguedStr):
   """
   BMGAY_URI_Field - A URL pointing to the author's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class SVTRG_viewerMergeHeadlineText_Field(ArguedStr):
   """
   SVTRG_viewerMergeHeadlineText_Field - The merge headline text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject): 
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class HZYCN_viewerMergeBodyText_Field(ArguedStr):
   """
   HZYCN_viewerMergeBodyText_Field - The merge body text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject): 
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class BQDHX_URI_Field(ArguedStr):
   """
   BQDHX_URI_Field - A URL pointing to the team's avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class DVAQR_trackedIssuesCount_Field(ArguedStr):
   """
   DVAQR_trackedIssuesCount_Field - The number of tracked issues for this issue

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      states - Limit the count to tracked issues with the specified states.

      """
      states: TrackedIssueStates ##LIST

   _args: intArgs



class PBLBV_HTML_Field(ArguedStr):
   """
   PBLBV_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject): 
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class RKTPS_URI_Field(ArguedStr):
   """
   RKTPS_URI_Field - A URL pointing to the owner's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class RIFOU_HTML_Field(ArguedStr):
   """
   RIFOU_HTML_Field - A description of the release, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject): 
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class ZMYLJ_URI_Field(ArguedStr):
   """
   ZMYLJ_URI_Field - A URL pointing to the GitHub App's public avatar.

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
   field: WorkflowRunOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class VerifyVerifiableDomainInput(GQLObject):
   """
   VerifyVerifiableDomainInput - Autogenerated input type of VerifyVerifiableDomain

   id - The ID of the verifiable domain to verify.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   clientMutationId: str

class UserStatusOrder(GQLObject):
   """
   UserStatusOrder - Ordering options for user status connections.

   field - The field to order user statuses by.

   direction - The ordering direction.

   """
   field: UserStatusOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class UpdateTopicsInput(GQLObject):
   """
   UpdateTopicsInput - Autogenerated input type of UpdateTopics

   repositoryId - The Node ID of the repository.

   topicNames - An array of topic names.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID ##NON NULL
   topicNames: str ##NON NULL ##LIST
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
   id: ID ##NON NULL
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
   subscribableId: ID ##NON NULL
   state: SubscriptionState ##NON NULL
   clientMutationId: str

class UpdateRepositoryWebCommitSignoffSettingInput(GQLObject):
   """
   UpdateRepositoryWebCommitSignoffSettingInput - Autogenerated input type of UpdateRepositoryWebCommitSignoffSetting

   repositoryId - The ID of the repository to update.

   webCommitSignoffRequired - Indicates if the repository should require signoff on web-based commits.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID ##NON NULL
   webCommitSignoffRequired: bool ##NON NULL
   clientMutationId: str

class UpdateRefInput(GQLObject):
   """
   UpdateRefInput - Autogenerated input type of UpdateRef

   refId - The Node ID of the Ref to be updated.

   oid - The GitObjectID that the Ref shall be updated to target.

   force - Permit updates of branch Refs that are not fast-forwards?

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   refId: ID ##NON NULL
   oid: GitObjectID ##NON NULL
   force: bool
   clientMutationId: str

class UpdatePullRequestReviewCommentInput(GQLObject):
   """
   UpdatePullRequestReviewCommentInput - Autogenerated input type of UpdatePullRequestReviewComment

   pullRequestReviewCommentId - The Node ID of the comment to modify.

   body - The text of the comment.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestReviewCommentId: ID ##NON NULL
   body: str ##NON NULL
   clientMutationId: str

class UpdatePullRequestBranchInput(GQLObject):
   """
   UpdatePullRequestBranchInput - Autogenerated input type of UpdatePullRequestBranch

   pullRequestId - The Node ID of the pull request.

   expectedHeadOid - The head ref oid for the upstream branch.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID ##NON NULL
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
   projectId: ID ##NON NULL
   title: str
   shortDescription: str
   readme: str
   closed: bool
   public: bool
   clientMutationId: str

class UpdateProjectNextItemFieldInput(GQLObject):
   """
   UpdateProjectNextItemFieldInput - Autogenerated input type of UpdateProjectNextItemField

   projectId - The ID of the Project. This field is required.

   itemId - The id of the item to be updated. This field is required.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `itemId` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   fieldId - The id of the field to be updated.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `fieldId` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   fieldWithSettingId - The id of the field to be updated. Only supports custom fields and status for now.

**Upcoming Change on 2022-10-01 UTC**
**Description:** `fieldWithSettingId` will be removed. Use `fieldConstraintId` instead
**Reason:** Renamed to fieldConstraintId to improve naming consistency.


   fieldConstraintId - The id of the field to be updated. Only supports custom fields and status for now.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `fieldConstraintId` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   value - The value which will be set on the field. This field is required.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `value` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   itemId: ID
   fieldId: ID
   fieldWithSettingId: ID
   fieldConstraintId: ID
   value: str
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
   projectId: ID ##NON NULL
   name: str
   body: str
   state: ProjectState
   public: bool
   clientMutationId: str

class UpdateProjectColumnInput(GQLObject):
   """
   UpdateProjectColumnInput - Autogenerated input type of UpdateProjectColumn

   projectColumnId - The ProjectColumn ID to update.

   name - The name of project column.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectColumnId: ID ##NON NULL
   name: str ##NON NULL
   clientMutationId: str

class UpdateOrganizationWebCommitSignoffSettingInput(GQLObject):
   """
   UpdateOrganizationWebCommitSignoffSettingInput - Autogenerated input type of UpdateOrganizationWebCommitSignoffSetting

   organizationId - The ID of the organization on which to set the web commit signoff setting.

   webCommitSignoffRequired - Enable signoff on web-based commits for repositories in the organization?

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID ##NON NULL
   webCommitSignoffRequired: bool ##NON NULL
   clientMutationId: str

class UpdateNotificationRestrictionSettingInput(GQLObject):
   """
   UpdateNotificationRestrictionSettingInput - Autogenerated input type of UpdateNotificationRestrictionSetting

   ownerId - The ID of the owner on which to set the restrict notifications setting.

   settingValue - The value for the restrict notifications setting.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID ##NON NULL
   settingValue: NotificationRestrictionSettingValue ##NON NULL
   clientMutationId: str

class UpdateIssueCommentInput(GQLObject):
   """
   UpdateIssueCommentInput - Autogenerated input type of UpdateIssueComment

   id - The ID of the IssueComment to modify.

   body - The updated text of the comment.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   body: str ##NON NULL
   clientMutationId: str

class UpdateIpAllowListEntryInput(GQLObject):
   """
   UpdateIpAllowListEntryInput - Autogenerated input type of UpdateIpAllowListEntry

   ipAllowListEntryId - The ID of the IP allow list entry to update.

   allowListValue - An IP address or range of addresses in CIDR notation.

   name - An optional name for the IP allow list entry.

   isActive - Whether the IP allow list entry is active when an IP allow list is enabled.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ipAllowListEntryId: ID ##NON NULL
   allowListValue: str ##NON NULL
   name: str
   isActive: bool ##NON NULL
   clientMutationId: str

class UpdateEnvironmentInput(GQLObject):
   """
   UpdateEnvironmentInput - Autogenerated input type of UpdateEnvironment

   environmentId - The node ID of the environment.

   waitTimer - The wait timer in minutes.

   reviewers - The ids of users or teams that can approve deployments to this environment

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   environmentId: ID ##NON NULL
   waitTimer: int
   reviewers: ID ##NON NULL ##LIST
   clientMutationId: str

class UpdateEnterpriseTeamDiscussionsSettingInput(GQLObject):
   """
   UpdateEnterpriseTeamDiscussionsSettingInput - Autogenerated input type of UpdateEnterpriseTeamDiscussionsSetting

   enterpriseId - The ID of the enterprise on which to set the team discussions setting.

   settingValue - The value for the team discussions setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseProfileInput(GQLObject):
   """
   UpdateEnterpriseProfileInput - Autogenerated input type of UpdateEnterpriseProfile

   enterpriseId - The Enterprise ID to update.

   name - The name of the enterprise.

   description - The description of the enterprise.

   websiteUrl - The URL of the enterprise's website.

   location - The location of the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
   name: str
   description: str
   websiteUrl: str
   location: str
   clientMutationId: str

class UpdateEnterpriseOwnerOrganizationRoleInput(GQLObject):
   """
   UpdateEnterpriseOwnerOrganizationRoleInput - Autogenerated input type of UpdateEnterpriseOwnerOrganizationRole

   enterpriseId - The ID of the Enterprise which the owner belongs to.

   organizationId - The ID of the organization for membership change.

   organizationRole - The role to assume in the organization.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
   organizationId: ID ##NON NULL
   organizationRole: RoleInOrganization ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput(GQLObject):
   """
   UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput - Autogenerated input type of UpdateEnterpriseMembersCanViewDependencyInsightsSetting

   enterpriseId - The ID of the enterprise on which to set the members can view dependency insights setting.

   settingValue - The value for the members can view dependency insights setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanMakePurchasesSettingInput(GQLObject):
   """
   UpdateEnterpriseMembersCanMakePurchasesSettingInput - Autogenerated input type of UpdateEnterpriseMembersCanMakePurchasesSetting

   enterpriseId - The ID of the enterprise on which to set the members can make purchases setting.

   settingValue - The value for the members can make purchases setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseMembersCanMakePurchasesSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput(GQLObject):
   """
   UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput - Autogenerated input type of UpdateEnterpriseMembersCanDeleteRepositoriesSetting

   enterpriseId - The ID of the enterprise on which to set the members can delete repositories setting.

   settingValue - The value for the members can delete repositories setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanCreateRepositoriesSettingInput(GQLObject):
   """
   UpdateEnterpriseMembersCanCreateRepositoriesSettingInput - Autogenerated input type of UpdateEnterpriseMembersCanCreateRepositoriesSetting

   enterpriseId - The ID of the enterprise on which to set the members can create repositories setting.

   settingValue - Value for the members can create repositories setting on the enterprise. This or the granular public/private/internal allowed fields (but not both) must be provided.

   membersCanCreateRepositoriesPolicyEnabled - When false, allow member organizations to set their own repository creation member privileges.

   membersCanCreatePublicRepositories - Allow members to create public repositories. Defaults to current value.

   membersCanCreatePrivateRepositories - Allow members to create private repositories. Defaults to current value.

   membersCanCreateInternalRepositories - Allow members to create internal repositories. Defaults to current value.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseMembersCanCreateRepositoriesSettingValue
   membersCanCreateRepositoriesPolicyEnabled: bool
   membersCanCreatePublicRepositories: bool
   membersCanCreatePrivateRepositories: bool
   membersCanCreateInternalRepositories: bool
   clientMutationId: str

class UpdateEnterpriseDefaultRepositoryPermissionSettingInput(GQLObject):
   """
   UpdateEnterpriseDefaultRepositoryPermissionSettingInput - Autogenerated input type of UpdateEnterpriseDefaultRepositoryPermissionSetting

   enterpriseId - The ID of the enterprise on which to set the base repository permission setting.

   settingValue - The value for the base repository permission setting on the enterprise.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseDefaultRepositoryPermissionSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseAdministratorRolePayload(GQLObject):
   """
   UpdateEnterpriseAdministratorRolePayload - Autogenerated return type of UpdateEnterpriseAdministratorRole

   clientMutationId - A unique identifier for the client performing the mutation.

   message - A message confirming the result of changing the administrator's role.

   """
   clientMutationId: str
   message: str

class UpdateDiscussionInput(GQLObject):
   """
   UpdateDiscussionInput - Autogenerated input type of UpdateDiscussion

   discussionId - The Node ID of the discussion to update.

   title - The new discussion title.

   body - The new contents of the discussion body.

   categoryId - The Node ID of a discussion category within the same repository to change this discussion to.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   discussionId: ID ##NON NULL
   title: str
   body: str
   categoryId: ID
   clientMutationId: str

class UpdatableComment(GQLObject):
   """
   UpdatableComment - Comments that can be updated.

   viewerCannotUpdateReasons - Reasons why the current viewer can not update this comment.

   """
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL

class UnresolveReviewThreadInput(GQLObject):
   """
   UnresolveReviewThreadInput - Autogenerated input type of UnresolveReviewThread

   threadId - The ID of the thread to unresolve

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   threadId: ID ##NON NULL
   clientMutationId: str

class UnminimizeCommentInput(GQLObject):
   """
   UnminimizeCommentInput - Autogenerated input type of UnminimizeComment

   subjectId - The Node ID of the subject to modify.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID ##NON NULL
   clientMutationId: str

class UnmarkFileAsViewedInput(GQLObject):
   """
   UnmarkFileAsViewedInput - Autogenerated input type of UnmarkFileAsViewed

   pullRequestId - The Node ID of the pull request.

   path - The path of the file to mark as unviewed

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID ##NON NULL
   path: str ##NON NULL
   clientMutationId: str

class UnlockLockableInput(GQLObject):
   """
   UnlockLockableInput - Autogenerated input type of UnlockLockable

   lockableId - ID of the item to be unlocked.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   lockableId: ID ##NON NULL
   clientMutationId: str

class UnlinkProjectV2FromTeamInput(GQLObject):
   """
   UnlinkProjectV2FromTeamInput - Autogenerated input type of UnlinkProjectV2FromTeam

   projectId - The ID of the project to unlink from the team.

   teamId - The ID of the team to unlink from the project.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID ##NON NULL
   teamId: ID ##NON NULL
   clientMutationId: str

class UniformResourceLocatable(GQLObject):
   """
   UniformResourceLocatable - Represents a type that can be retrieved by a URL.

   resourcePath - The HTML path to this resource.

   url - The URL to this resource.

   """
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class UnfollowOrganizationInput(GQLObject):
   """
   UnfollowOrganizationInput - Autogenerated input type of UnfollowOrganization

   organizationId - ID of the organization to unfollow.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID ##NON NULL
   clientMutationId: str

class UnarchiveProjectV2ItemInput(GQLObject):
   """
   UnarchiveProjectV2ItemInput - Autogenerated input type of UnarchiveProjectV2Item

   projectId - The ID of the Project to archive the item from.

   itemId - The ID of the ProjectV2Item to unarchive.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   clientMutationId: str

class TransferEnterpriseOrganizationInput(GQLObject):
   """
   TransferEnterpriseOrganizationInput - Autogenerated input type of TransferEnterpriseOrganization

   organizationId - The ID of the organization to transfer.

   destinationEnterpriseId - The ID of the enterprise where the organization should be transferred.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID ##NON NULL
   destinationEnterpriseId: ID ##NON NULL
   clientMutationId: str

class TeamRepositoryOrder(GQLObject):
   """
   TeamRepositoryOrder - Ordering options for team repository connections

   field - The field to order repositories by.

   direction - The ordering direction.

   """
   field: TeamRepositoryOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class TeamMemberOrder(GQLObject):
   """
   TeamMemberOrder - Ordering options for team member connections

   field - The field to order team members by.

   direction - The ordering direction.

   """
   field: TeamMemberOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class TeamDiscussionCommentOrder(GQLObject):
   """
   TeamDiscussionCommentOrder - Ways in which team discussion comment connections can be ordered.

   field - The field by which to order nodes.

   direction - The direction in which to order nodes.

   """
   field: TeamDiscussionCommentOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

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
   gitUrl: URI ##NON NULL
   name: str ##NON NULL
   nameRaw: Base64String ##NON NULL
   path: str ##NON NULL
   pathRaw: Base64String ##NON NULL
   subprojectCommitOid: GitObjectID

class StatusContextStateCount(GQLObject):
   """
   StatusContextStateCount - Represents a count of the state of a status context.

   count - The number of statuses with this state.

   state - The state of a status context.

   """
   count: int ##NON NULL
   state: StatusState ##NON NULL

class StartOrganizationMigrationInput(GQLObject):
   """
   StartOrganizationMigrationInput - Autogenerated input type of StartOrganizationMigration

   sourceOrgUrl - The URL of the organization to migrate.

   targetOrgName - The name of the target organization.

   targetEnterpriseId - The ID of the enterprise the target organization belongs to.

   sourceAccessToken - The migration source access token.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   sourceOrgUrl: URI ##NON NULL
   targetOrgName: str ##NON NULL
   targetEnterpriseId: ID ##NON NULL
   sourceAccessToken: str ##NON NULL
   clientMutationId: str

class SponsorshipOrder(GQLObject):
   """
   SponsorshipOrder - Ordering options for sponsorship connections.

   field - The field to order sponsorship by.

   direction - The ordering direction.

   """
   field: SponsorshipOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorsTierOrder(GQLObject):
   """
   SponsorsTierOrder - Ordering options for Sponsors tiers connections.

   field - The field to order tiers by.

   direction - The ordering direction.

   """
   field: SponsorsTierOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorsActivityOrder(GQLObject):
   """
   SponsorsActivityOrder - Ordering options for GitHub Sponsors activity connections.

   field - The field to order activity by.

   direction - The ordering direction.

   """
   field: SponsorsActivityOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorOrder(GQLObject):
   """
   SponsorOrder - Ordering options for connections to get sponsor entities for GitHub Sponsors.

   field - The field to order sponsor entities by.

   direction - The ordering direction.

   """
   field: SponsorOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SetUserInteractionLimitInput(GQLObject):
   """
   SetUserInteractionLimitInput - Autogenerated input type of SetUserInteractionLimit

   userId - The ID of the user to set a limit for.

   limit - The limit to set.

   expiry - When this limit should expire.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   userId: ID ##NON NULL
   limit: RepositoryInteractionLimit ##NON NULL
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
   organizationId: ID ##NON NULL
   limit: RepositoryInteractionLimit ##NON NULL
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SecurityVulnerabilityOrder(GQLObject):
   """
   SecurityVulnerabilityOrder - Ordering options for security vulnerability connections

   field - The field to order security vulnerabilities by.

   direction - The ordering direction.

   """
   field: SecurityVulnerabilityOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SecurityAdvisoryPackageVersion(GQLObject):
   """
   SecurityAdvisoryPackageVersion - An individual package version

   identifier - The package name or version

   """
   identifier: str ##NON NULL

class SecurityAdvisoryOrder(GQLObject):
   """
   SecurityAdvisoryOrder - Ordering options for security advisory connections

   field - The field to order security advisories by.

   direction - The ordering direction.

   """
   field: SecurityAdvisoryOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SecurityAdvisoryIdentifier(GQLObject):
   """
   SecurityAdvisoryIdentifier - A GitHub Security Advisory Identifier

   type - The identifier type, e.g. GHSA, CVE

   value - The identifier

   """
   type: str ##NON NULL
   value: str ##NON NULL

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
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class RetireSponsorsTierInput(GQLObject):
   """
   RetireSponsorsTierInput - Autogenerated input type of RetireSponsorsTier

   tierId - The ID of the published tier to retire.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   tierId: ID ##NON NULL
   clientMutationId: str

class RerequestCheckSuiteInput(GQLObject):
   """
   RerequestCheckSuiteInput - Autogenerated input type of RerequestCheckSuite

   repositoryId - The Node ID of the repository.

   checkSuiteId - The Node ID of the check suite.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID ##NON NULL
   checkSuiteId: ID ##NON NULL
   clientMutationId: str

class FNQDY_isRequired_Field(ArguedStr):
   """
   FNQDY_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

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
   pullRequestId: ID ##NON NULL
   userIds: ID ##NON NULL ##LIST
   teamIds: ID ##NON NULL ##LIST
   union: bool
   clientMutationId: str

class RepositoryMigrationOrder(GQLObject):
   """
   RepositoryMigrationOrder - Ordering options for repository migrations.

   field - The field to order repository migrations by.

   direction - The ordering direction.

   """
   field: RepositoryMigrationOrderField ##NON NULL
   direction: RepositoryMigrationOrderDirection ##NON NULL

class RepositoryInteractionAbility(GQLObject):
   """
   RepositoryInteractionAbility - Repository interaction limit that applies to this object.

   expiresAt - The time the currently active limit expires.

   limit - The current limit that is enabled on this object.

   origin - The origin of the currently active interaction limit.

   """
   expiresAt: DateTime
   limit: RepositoryInteractionLimit ##NON NULL
   origin: RepositoryInteractionLimitOrigin ##NON NULL

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
   column: int ##NON NULL
   kind: str ##NON NULL
   line: int ##NON NULL
   message: str ##NON NULL
   path: str ##NON NULL
   source: str ##NON NULL
   suggestion: str

class ReopenIssueInput(GQLObject):
   """
   ReopenIssueInput - Autogenerated input type of ReopenIssue

   issueId - ID of the issue to be opened.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID ##NON NULL
   clientMutationId: str

class RemoveStarInput(GQLObject):
   """
   RemoveStarInput - Autogenerated input type of RemoveStar

   starrableId - The Starrable ID to unstar.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   starrableId: ID ##NON NULL
   clientMutationId: str

class RemoveOutsideCollaboratorInput(GQLObject):
   """
   RemoveOutsideCollaboratorInput - Autogenerated input type of RemoveOutsideCollaborator

   userId - The ID of the outside collaborator to remove.

   organizationId - The ID of the organization to remove the outside collaborator from.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   userId: ID ##NON NULL
   organizationId: ID ##NON NULL
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
   enterpriseId: ID ##NON NULL
   organizationId: ID ##NON NULL
   clientMutationId: str

class RemoveEnterpriseAdminInput(GQLObject):
   """
   RemoveEnterpriseAdminInput - Autogenerated input type of RemoveEnterpriseAdmin

   enterpriseId - The Enterprise ID from which to remove the administrator.

   login - The login of the user to remove as an administrator.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class ReleaseOrder(GQLObject):
   """
   ReleaseOrder - Ways in which lists of releases can be ordered upon return.

   field - The field in which to order releases by.

   direction - The direction in which to order releases by the specified field.

   """
   field: ReleaseOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

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
   enterpriseId: ID ##NON NULL
   clientMutationId: str

class RefOrder(GQLObject):
   """
   RefOrder - Ways in which lists of git refs can be ordered upon return.

   field - The field in which to order refs by.

   direction - The direction in which to order refs by the specified field.

   """
   field: RefOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

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
   cost: int ##NON NULL
   limit: int ##NON NULL
   nodeCount: int ##NON NULL
   remaining: int ##NON NULL
   resetAt: DateTime ##NON NULL
   used: int ##NON NULL

class PullRequestChangedFile(GQLObject):
   """
   PullRequestChangedFile - A file changed in a pull request.

   additions - The number of additions to the file.

   changeType - How the file was changed in this PullRequest

   deletions - The number of deletions to the file.

   path - The path of the file.

   viewerViewedState - The state of the file for the viewer.

   """
   additions: int ##NON NULL
   changeType: PatchStatus ##NON NULL
   deletions: int ##NON NULL
   path: str ##NON NULL
   viewerViewedState: FileViewedState ##NON NULL

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
   fingerprint: str ##NON NULL
   id: ID ##NON NULL
   isReadOnly: bool
   key: str ##NON NULL
   updatedAt: DateTime

class ProjectV2SingleSelectFieldOption(GQLObject):
   """
   ProjectV2SingleSelectFieldOption - Single select field option for a configuration for a project.

   id - The option's ID.

   name - The option's name.

   nameHTML - The option's html name.

   """
   id: str ##NON NULL
   name: str ##NON NULL
   nameHTML: str ##NON NULL

class ProjectV2IterationFieldIteration(GQLObject):
   """
   ProjectV2IterationFieldIteration - Iteration field iteration settings for a project.

   duration - The iteration's duration in days

   id - The iteration's ID.

   startDate - The iteration's start date

   title - The iteration's title.

   titleHTML - The iteration's html title.

   """
   duration: int ##NON NULL
   id: str ##NON NULL
   startDate: Date ##NON NULL
   title: str ##NON NULL
   titleHTML: str ##NON NULL

class ProjectV2ItemFieldValueOrder(GQLObject):
   """
   ProjectV2ItemFieldValueOrder - Ordering options for project v2 item field value connections

   field - The field to order the project v2 item field values by.

   direction - The ordering direction.

   """
   field: ProjectV2ItemFieldValueOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

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
   doneCount: int ##NON NULL
   donePercentage: float ##NON NULL
   enabled: bool ##NON NULL
   inProgressCount: int ##NON NULL
   inProgressPercentage: float ##NON NULL
   todoCount: int ##NON NULL
   todoPercentage: float ##NON NULL

class PinIssueInput(GQLObject):
   """
   PinIssueInput - Autogenerated input type of PinIssue

   issueId - The ID of the issue to be pinned

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID ##NON NULL
   clientMutationId: str

class PackageVersionStatistics(GQLObject):
   """
   PackageVersionStatistics - Represents a object that contains package version activity statistics such as downloads.

   downloadsTotalCount - Number of times the package was downloaded since it was created.

   """
   downloadsTotalCount: int ##NON NULL

class PackageStatistics(GQLObject):
   """
   PackageStatistics - Represents a object that contains package activity statistics such as downloads.

   downloadsTotalCount - Number of times the package was downloaded since it was created.

   """
   downloadsTotalCount: int ##NON NULL

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
   createdAt: DateTime ##NON NULL
   databaseId: str
   failureReason: str
   id: ID ##NON NULL
   remainingRepositoriesCount: int
   sourceOrgName: str ##NON NULL
   sourceOrgUrl: URI ##NON NULL
   state: OrganizationMigrationState ##NON NULL
   targetOrgName: str ##NON NULL
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
   columnId: ID ##NON NULL
   afterColumnId: ID
   clientMutationId: str

class MinimizeCommentInput(GQLObject):
   """
   MinimizeCommentInput - Autogenerated input type of MinimizeComment

   subjectId - The Node ID of the subject to modify.

   classifier - The classification of comment

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID ##NON NULL
   classifier: ReportedContentClassifiers ##NON NULL
   clientMutationId: str

class MilestoneOrder(GQLObject):
   """
   MilestoneOrder - Ordering options for milestone connections.

   field - The field to order milestones by.

   direction - The ordering direction.

   """
   field: MilestoneOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

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
   pullRequestId: ID ##NON NULL
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
   id: ID ##NON NULL
   name: str ##NON NULL
   primaryListingCount: int ##NON NULL
   resourcePath: URI ##NON NULL
   secondaryListingCount: int ##NON NULL
   slug: str ##NON NULL
   url: URI ##NON NULL

class MarkFileAsViewedInput(GQLObject):
   """
   MarkFileAsViewedInput - Autogenerated input type of MarkFileAsViewed

   pullRequestId - The Node ID of the pull request.

   path - The path of the file to mark as viewed

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID ##NON NULL
   path: str ##NON NULL
   clientMutationId: str

class MannequinOrder(GQLObject):
   """
   MannequinOrder - Ordering options for mannequins.

   field - The field to order mannequins by.

   direction - The ordering direction.

   """
   field: MannequinOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class LockLockableInput(GQLObject):
   """
   LockLockableInput - Autogenerated input type of LockLockable

   lockableId - ID of the item to be locked.

   lockReason - A reason for why the item will be locked.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   lockableId: ID ##NON NULL
   lockReason: LockReason
   clientMutationId: str

class LinkProjectV2ToTeamInput(GQLObject):
   """
   LinkProjectV2ToTeamInput - Autogenerated input type of LinkProjectV2ToTeam

   projectId - The ID of the project to link to the team.

   teamId - The ID of the team to link to the project.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID ##NON NULL
   teamId: ID ##NON NULL
   clientMutationId: str

class LicenseRule(GQLObject):
   """
   LicenseRule - Describes a License's conditions, permissions, and limitations

   description - A description of the rule

   key - The machine-readable rule key

   label - The human-readable rule label

   """
   description: str ##NON NULL
   key: str ##NON NULL
   label: str ##NON NULL

class Language(GQLObject):
   """
   Language - Represents a given language found in repositories.

   color - The color defined for the current language.

   name - The name of the current language.

   """
   color: str
   id: ID ##NON NULL
   name: str ##NON NULL

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
   filename: str ##NON NULL
   name: str ##NON NULL
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
   labels: str ##NON NULL ##LIST
   mentioned: str
   milestone: str
   milestoneNumber: str
   since: DateTime
   states: IssueState ##NON NULL ##LIST
   viewerSubscribed: bool

class IpAllowListEntryOrder(GQLObject):
   """
   IpAllowListEntryOrder - Ordering options for IP allow list entry connections.

   field - The field to order IP allow list entries by.

   direction - The ordering direction.

   """
   field: IpAllowListEntryOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class HovercardContext(GQLObject):
   """
   HovercardContext - An individual line of a hovercard

   message - A string describing this context

   octicon - An octicon to accompany this context

   """
   message: str ##NON NULL
   octicon: str ##NON NULL

class GrantMigratorRoleInput(GQLObject):
   """
   GrantMigratorRoleInput - Autogenerated input type of GrantMigratorRole

   organizationId - The ID of the organization that the user/team belongs to.

   actor - The user login or Team slug to grant the migrator role.

   actorType - Specifies the type of the actor, can be either USER or TEAM.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID ##NON NULL
   actor: str ##NON NULL
   actorType: ActorType ##NON NULL
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
   gitHubServicesSha: GitObjectID ##NON NULL
   gitIpAddresses: str ##LIST
   hookIpAddresses: str ##LIST
   importerIpAddresses: str ##LIST
   isPasswordAuthenticationVerifiable: bool ##NON NULL
   pagesIpAddresses: str ##LIST

class GenericHovercardContext(GQLObject):
   """
   GenericHovercardContext - A generic hovercard context with a message and icon

   message - A string describing this context

   octicon - An octicon to accompany this context

   """
   message: str ##NON NULL
   octicon: str ##NON NULL

class FollowUserInput(GQLObject):
   """
   FollowUserInput - Autogenerated input type of FollowUser

   userId - ID of the user to follow.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   userId: ID ##NON NULL
   clientMutationId: str

class FileDeletion(GQLObject):
   """
   FileDeletion - A command to delete the file at the given path as part of a commit.

   path - The path to delete

   """
   path: str ##NON NULL

class ExternalIdentityAttribute(GQLObject):
   """
   ExternalIdentityAttribute - An attribute for the External Identity attributes collection

   metadata - The attribute metadata as JSON

   name - The attribute name

   value - The attribute value

   """
   metadata: str
   name: str ##NON NULL
   value: str ##NON NULL

class EnterpriseServerUserAccountOrder(GQLObject):
   """
   EnterpriseServerUserAccountOrder - Ordering options for Enterprise Server user account connections.

   field - The field to order user accounts by.

   direction - The ordering direction.

   """
   field: EnterpriseServerUserAccountOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseServerInstallationOrder(GQLObject):
   """
   EnterpriseServerInstallationOrder - Ordering options for Enterprise Server installation connections.

   field - The field to order Enterprise Server installations by.

   direction - The ordering direction.

   """
   field: EnterpriseServerInstallationOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseMemberOrder(GQLObject):
   """
   EnterpriseMemberOrder - Ordering options for enterprise member connections.

   field - The field to order enterprise members by.

   direction - The ordering direction.

   """
   field: EnterpriseMemberOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

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
   pullRequestId: ID ##NON NULL
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
   path: str ##NON NULL
   position: int ##NON NULL
   body: str ##NON NULL

class DismissPullRequestReviewInput(GQLObject):
   """
   DismissPullRequestReviewInput - Autogenerated input type of DismissPullRequestReview

   pullRequestReviewId - The Node ID of the pull request review to modify.

   message - The contents of the pull request review dismissal message.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestReviewId: ID ##NON NULL
   message: str ##NON NULL
   clientMutationId: str

class DiscussionOrder(GQLObject):
   """
   DiscussionOrder - Ways in which lists of discussions can be ordered upon return.

   field - The field by which to order discussions.

   direction - The direction in which to order discussions by the specified field.

   """
   field: DiscussionOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class DeploymentOrder(GQLObject):
   """
   DeploymentOrder - Ordering options for deployment connections

   field - The field to order deployments by.

   direction - The ordering direction.

   """
   field: DeploymentOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class DependabotUpdateError(GQLObject):
   """
   DependabotUpdateError - An error produced from a Dependabot Update

   body - The body of the error

   errorType - The error code

   title - The title of the error

   """
   body: str ##NON NULL
   errorType: str ##NON NULL
   title: str ##NON NULL

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
   pullRequestReviewId: ID ##NON NULL
   clientMutationId: str

class DeleteProjectV2ItemPayload(GQLObject):
   """
   DeleteProjectV2ItemPayload - Autogenerated return type of DeleteProjectV2Item

   clientMutationId - A unique identifier for the client performing the mutation.

   deletedItemId - The ID of the deleted item.

   """
   clientMutationId: str
   deletedItemId: ID

class DeleteProjectNextItemPayload(GQLObject):
   """
   DeleteProjectNextItemPayload - Autogenerated return type of DeleteProjectNextItem

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   clientMutationId: str

class DeleteProjectInput(GQLObject):
   """
   DeleteProjectInput - Autogenerated input type of DeleteProject

   projectId - The Project ID to update.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID ##NON NULL
   clientMutationId: str

class DeleteProjectCardInput(GQLObject):
   """
   DeleteProjectCardInput - Autogenerated input type of DeleteProjectCard

   cardId - The id of the card to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   cardId: ID ##NON NULL
   clientMutationId: str

class DeleteIssueInput(GQLObject):
   """
   DeleteIssueInput - Autogenerated input type of DeleteIssue

   issueId - The ID of the issue to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID ##NON NULL
   clientMutationId: str

class DeleteIssueCommentInput(GQLObject):
   """
   DeleteIssueCommentInput - Autogenerated input type of DeleteIssueComment

   id - The ID of the comment to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
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
   id: ID ##NON NULL
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
   viewerCanDelete: bool ##NON NULL

class CreateTeamDiscussionInput(GQLObject):
   """
   CreateTeamDiscussionInput - Autogenerated input type of CreateTeamDiscussion

   teamId - The ID of the team to which the discussion belongs.

   title - The title of the discussion.

   body - The content of the discussion.

   private - If true, restricts the visibility of this discussion to team members and organization admins. If false or not specified, allows any organization member to view this discussion.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   teamId: ID ##NON NULL
   title: str ##NON NULL
   body: str ##NON NULL
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
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   oid: GitObjectID ##NON NULL
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
   ownerId: ID ##NON NULL
   title: str ##NON NULL
   repositoryId: ID
   teamId: ID
   clientMutationId: str

class CreateMigrationSourceInput(GQLObject):
   """
   CreateMigrationSourceInput - Autogenerated input type of CreateMigrationSource

   name - The migration source name.

   url - The migration source URL.

   accessToken - The migration source access token.

   type - The migration source type.

   ownerId - The ID of the organization that will own the migration source.

   githubPat - The GitHub personal access token of the user importing to the target repository.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   name: str ##NON NULL
   url: str ##NON NULL
   accessToken: str
   type: MigrationSourceType ##NON NULL
   ownerId: ID ##NON NULL
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
   repositoryId: ID ##NON NULL
   title: str ##NON NULL
   body: str
   assigneeIds: ID ##NON NULL ##LIST
   milestoneId: ID
   labelIds: ID ##NON NULL ##LIST
   projectIds: ID ##NON NULL ##LIST
   issueTemplate: str
   clientMutationId: str

class CreateEnvironmentInput(GQLObject):
   """
   CreateEnvironmentInput - Autogenerated input type of CreateEnvironment

   repositoryId - The node ID of the repository.

   name - The name of the environment.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
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
   repositoryId: ID ##NON NULL
   title: str ##NON NULL
   body: str ##NON NULL
   categoryId: ID ##NON NULL
   clientMutationId: str

class CreateAttributionInvitationInput(GQLObject):
   """
   CreateAttributionInvitationInput - Autogenerated input type of CreateAttributionInvitation

   ownerId - The Node ID of the owner scoping the reattributable data.

   sourceId - The Node ID of the account owning the data to reattribute.

   targetId - The Node ID of the account which may claim the data.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID ##NON NULL
   sourceId: ID ##NON NULL
   targetId: ID ##NON NULL
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
   projectCardId: ID ##NON NULL
   repositoryId: ID ##NON NULL
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
   firstDay: Date ##NON NULL
   name: str ##NON NULL
   totalWeeks: int ##NON NULL
   year: int ##NON NULL

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
   field: CommitContributionOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

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
   id: ID ##NON NULL
   key: str ##NON NULL
   name: str ##NON NULL
   resourcePath: URI
   url: URI

class CloseIssueInput(GQLObject):
   """
   CloseIssueInput - Autogenerated input type of CloseIssue

   issueId - ID of the issue to be closed.

   stateReason - The reason the issue is to be closed.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   issueId: ID ##NON NULL
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
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   ownerId: ID ##NON NULL
   description: str
   visibility: RepositoryVisibility ##NON NULL
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
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   fieldId: ID ##NON NULL
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
   name: str ##NON NULL
   number: int ##NON NULL
   secondsToCompletion: int
   startedAt: DateTime
   status: CheckStatusState ##NON NULL

class CheckRunOutputImage(GQLObject):
   """
   CheckRunOutputImage - Images attached to the check run output displayed in the GitHub pull request UI.

   alt - The alternative text for the image.

   imageUrl - The full URL of the image.

   caption - A short image description.

   """
   alt: str ##NON NULL
   imageUrl: URI ##NON NULL
   caption: str

class CheckRunAction(GQLObject):
   """
   CheckRunAction - Possible further actions the integrator can perform.

   label - The text to be displayed on a button in the web UI.

   description - A short explanation of what this action would do.

   identifier - A reference for the action on the integrator's system. 

   """
   label: str ##NON NULL
   description: str ##NON NULL
   identifier: str ##NON NULL

class CheckAnnotationPosition(GQLObject):
   """
   CheckAnnotationPosition - A character position in a check annotation.

   column - Column number (1 indexed).

   line - Line number (1 indexed).

   """
   column: int
   line: int ##NON NULL

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
   cweId: str ##NON NULL
   description: str ##NON NULL
   id: ID ##NON NULL
   name: str ##NON NULL

class VCSUI_URI_Field(ArguedStr):
   """
   VCSUI_URI_Field - A URL pointing to the GitHub App's public avatar.

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
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   clientMutationId: str

class ApproveDeploymentsInput(GQLObject):
   """
   ApproveDeploymentsInput - Autogenerated input type of ApproveDeployments

   workflowRunId - The node ID of the workflow run containing the pending deployments.

   environmentIds - The ids of environments to reject deployments

   comment - Optional comment for approving deployments

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   workflowRunId: ID ##NON NULL
   environmentIds: ID ##NON NULL ##LIST
   comment: str
   clientMutationId: str

class AddUpvoteInput(GQLObject):
   """
   AddUpvoteInput - Autogenerated input type of AddUpvote

   subjectId - The Node ID of the discussion or comment to upvote.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID ##NON NULL
   clientMutationId: str

class AddReactionInput(GQLObject):
   """
   AddReactionInput - Autogenerated input type of AddReaction

   subjectId - The Node ID of the subject to modify.

   content - The name of the emoji to react with.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID ##NON NULL
   content: ReactionContent ##NON NULL
   clientMutationId: str

class AddPullRequestReviewCommentInput(GQLObject):
   """
   AddPullRequestReviewCommentInput - Autogenerated input type of AddPullRequestReviewComment

   pullRequestId - The node ID of the pull request reviewing

   pullRequestReviewId - The Node ID of the review to modify.

   commitOID - The SHA of the commit to comment on.

   body - The text of the comment.

   path - The relative path of the file to comment on.

   position - The line index in the diff to comment on.

   inReplyTo - The comment id to reply to.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID
   pullRequestReviewId: ID
   commitOID: GitObjectID
   body: str ##NON NULL
   path: str
   position: int
   inReplyTo: ID
   clientMutationId: str

class AddProjectV2DraftIssueInput(GQLObject):
   """
   AddProjectV2DraftIssueInput - Autogenerated input type of AddProjectV2DraftIssue

   projectId - The ID of the Project to add the draft issue to.

   title - The title of the draft issue.

   body - The body of the draft issue.

   assigneeIds - The IDs of the assignees of the draft issue.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID ##NON NULL
   title: str ##NON NULL
   body: str
   assigneeIds: ID ##NON NULL ##LIST
   clientMutationId: str

class AddProjectDraftIssueInput(GQLObject):
   """
   AddProjectDraftIssueInput - Autogenerated input type of AddProjectDraftIssue

   projectId - The ID of the Project to add the draft issue to. This field is required.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `projectId` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   title - The title of the draft issue. This field is required.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `title` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   body - The body of the draft issue.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `body` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   assigneeIds - The IDs of the assignees of the draft issue.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `assigneeIds` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   title: str
   body: str
   assigneeIds: ID ##NON NULL ##LIST
   clientMutationId: str

class AddProjectCardInput(GQLObject):
   """
   AddProjectCardInput - Autogenerated input type of AddProjectCard

   projectColumnId - The Node ID of the ProjectColumn.

   contentId - The content of the card. Must be a member of the ProjectCardItem union

   note - The note on the card.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectColumnId: ID ##NON NULL
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
   enterpriseId: ID ##NON NULL
   organizationId: ID ##NON NULL
   userIds: ID ##NON NULL ##LIST
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
   discussionId: ID ##NON NULL
   replyToId: ID
   body: str ##NON NULL
   clientMutationId: str

class AddAssigneesToAssignableInput(GQLObject):
   """
   AddAssigneesToAssignableInput - Autogenerated input type of AddAssigneesToAssignable

   assignableId - The id of the assignable object to add assignees to.

   assigneeIds - The id of users to add as assignees.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   assignableId: ID ##NON NULL
   assigneeIds: ID ##NON NULL ##LIST
   clientMutationId: str

class HQAWT_URI_Field(ArguedStr):
   """
   HQAWT_URI_Field - A URL pointing to the actor's public avatar.

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
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   clientMutationId: str

class AbortQueuedMigrationsPayload(GQLObject):
   """
   AbortQueuedMigrationsPayload - Autogenerated return type of AbortQueuedMigrations

   clientMutationId - A unique identifier for the client performing the mutation.

   success - Did the operation succeed?

   """
   clientMutationId: str
   success: bool
