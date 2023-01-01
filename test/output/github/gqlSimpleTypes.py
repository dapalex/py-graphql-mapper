from typing import Generic
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gqlTypes import ID
from pygqlmap.src.gqlArgBuiltin import *
from .enums import *
from .scalars import *

class YJSWWanyPinnableItems_anyPinnableItems_Field(ArguedStr):
   """
   YJSWWanyPinnableItems_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class SSPIUlogoUrl_URI_Field(ArguedStr):
   """
   SSPIUlogoUrl_URI_Field - URL for the listing's logo image.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class DBFUClogoUrl_URI_Field(ArguedStr):
   """
   DBFUClogoUrl_URI_Field - A URL pointing to the app's logo.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting image.

      """
      size: int

   _args: URIArgs



class LWKKGavatarUrl_URI_Field(ArguedStr):
   """
   LWKKGavatarUrl_URI_Field - A URL pointing to the enterprise's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class TWLVDshortDescriptionHTML_HTML_Field(ArguedStr):
   """
   TWLVDshortDescriptionHTML_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject): 
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class FEKUFavatarUrl_URI_Field(ArguedStr):
   """
   FEKUFavatarUrl_URI_Field - A URL pointing to the enterprise user account's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class RMFCKisSponsoredBy_isSponsoredBy_Field(ArguedStr):
   """
   RMFCKisSponsoredBy_isSponsoredBy_Field - Check if the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      accountLogin - The target account's login.

      """
      accountLogin: str ##NON NULL

   _args: boolArgs



class QCCLJavatarUrl_URI_Field(ArguedStr):
   """
   QCCLJavatarUrl_URI_Field - A URL pointing to the organization's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class LVEHManyPinnableItems_anyPinnableItems_Field(ArguedStr):
   """
   LVEHManyPinnableItems_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class HNRYGorganizationVerifiedDomainEmails_organizationVerifiedDomainEmails_Field(ArguedStr):
   """
   HNRYGorganizationVerifiedDomainEmails_organizationVerifiedDomainEmails_Field - Verified email addresses that match verified domains for a specified organization the user is a member of.

   """
   class strArgs(GQLArgsSet, GQLObject): 
      """
      login - The login of the organization to match verified domains from.

      """
      login: str ##NON NULL

   _args: strArgs



class OQLBYisSponsoredBy_isSponsoredBy_Field(ArguedStr):
   """
   OQLBYisSponsoredBy_isSponsoredBy_Field - Check if the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      accountLogin - The target account's login.

      """
      accountLogin: str ##NON NULL

   _args: boolArgs



class PJCOQcanReceiveOrganizationEmailsWhenNotificationsRestricted_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedStr):
   """
   PJCOQcanReceiveOrganizationEmailsWhenNotificationsRestricted_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field - Could this user receive email notifications, if the organization had notification restrictions enabled?

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      login - The login of the organization to check.

      """
      login: str ##NON NULL

   _args: boolArgs



class PEZMOavatarUrl_URI_Field(ArguedStr):
   """
   PEZMOavatarUrl_URI_Field - A URL pointing to the user's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class CTJBSanyPinnableItems_anyPinnableItems_Field(ArguedStr):
   """
   CTJBSanyPinnableItems_anyPinnableItems_Field - Determine if this repository owner has any items that can be pinned to their profile.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      type - Filter to only a particular kind of pinnable item.

      """
      type: PinnableItemType

   _args: boolArgs



class GUCYDisSponsoredBy_isSponsoredBy_Field(ArguedStr):
   """
   GUCYDisSponsoredBy_isSponsoredBy_Field - Check if the given account is sponsoring this user/organization.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      accountLogin - The target account's login.

      """
      accountLogin: str ##NON NULL

   _args: boolArgs



class LBEIAtext_text_Field(ArguedStr):
   """
   LBEIAtext_text_Field - UTF8 text data or null if the file is binary

   """
   class strArgs(GQLArgsSet, GQLObject): 
      """
      truncate - Optionally truncate the returned file to this length.

      """
      truncate: int

   _args: strArgs



class UARJBtotalRepositoryContributions_totalRepositoryContributions_Field(ArguedStr):
   """
   UARJBtotalRepositoryContributions_totalRepositoryContributions_Field - How many repositories the user created.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      excludeFirst - Should the user's first repository ever be excluded from this count.

      """
      excludeFirst: bool

   _args: intArgs



class CGSZDtotalRepositoriesWithContributedPullRequests_totalRepositoriesWithContributedPullRequests_Field(ArguedStr):
   """
   CGSZDtotalRepositoriesWithContributedPullRequests_totalRepositoriesWithContributedPullRequests_Field - How many different repositories the user opened pull requests in.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class RYQDDtotalRepositoriesWithContributedIssues_totalRepositoriesWithContributedIssues_Field(ArguedStr):
   """
   RYQDDtotalRepositoriesWithContributedIssues_totalRepositoriesWithContributedIssues_Field - How many different repositories the user opened issues in.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class TJCLRtotalPullRequestContributions_totalPullRequestContributions_Field(ArguedStr):
   """
   TJCLRtotalPullRequestContributions_totalPullRequestContributions_Field - How many pull requests the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      excludeFirst - Should the user's first pull request ever be excluded from this count.

      excludePopular - Should the user's most commented pull request be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class XOWLRtotalIssueContributions_totalIssueContributions_Field(ArguedStr):
   """
   XOWLRtotalIssueContributions_totalIssueContributions_Field - How many issues the user opened.

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      excludeFirst - Should the user's first issue ever be excluded from this count.

      excludePopular - Should the user's most commented issue be excluded from this count.

      """
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class ZCDZSisRequired_isRequired_Field(ArguedStr):
   """
   ZCDZSisRequired_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class IJYLXavatarUrl_URI_Field(ArguedStr):
   """
   IJYLXavatarUrl_URI_Field - The avatar of the OAuth application or the user that created the status

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class ZUOQHisRequired_isRequired_Field(ArguedStr):
   """
   ZUOQHisRequired_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

   """
   class boolArgs(GQLArgsSet, GQLObject): 
      """
      pullRequestId - The id of the pull request this is required for

      pullRequestNumber - The number of the pull request this is required for

      """
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class MKEHEavatarUrl_URI_Field(ArguedStr):
   """
   MKEHEavatarUrl_URI_Field - A URL pointing to the author's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class ZOLOUviewerMergeHeadlineText_viewerMergeHeadlineText_Field(ArguedStr):
   """
   ZOLOUviewerMergeHeadlineText_viewerMergeHeadlineText_Field - The merge headline text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject): 
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class LJPLAviewerMergeBodyText_viewerMergeBodyText_Field(ArguedStr):
   """
   LJPLAviewerMergeBodyText_viewerMergeBodyText_Field - The merge body text for the viewer and method.

   """
   class strArgs(GQLArgsSet, GQLObject): 
      """
      mergeType - The merge method for the message.

      """
      mergeType: PullRequestMergeMethod

   _args: strArgs



class UZNJWavatarUrl_URI_Field(ArguedStr):
   """
   UZNJWavatarUrl_URI_Field - A URL pointing to the team's avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size in pixels of the resulting square image.

      """
      size: int

   _args: URIArgs



class QWXLQtrackedIssuesCount_trackedIssuesCount_Field(ArguedStr):
   """
   QWXLQtrackedIssuesCount_trackedIssuesCount_Field - The number of tracked issues for this issue

   """
   class intArgs(GQLArgsSet, GQLObject): 
      """
      states - Limit the count to tracked issues with the specified states.

      """
      states: TrackedIssueStates ##LIST

   _args: intArgs



class VCGAKshortDescriptionHTML_HTML_Field(ArguedStr):
   """
   VCGAKshortDescriptionHTML_HTML_Field - A description of the repository, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject): 
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class PUFQFavatarUrl_URI_Field(ArguedStr):
   """
   PUFQFavatarUrl_URI_Field - A URL pointing to the owner's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class MFKQWshortDescriptionHTML_HTML_Field(ArguedStr):
   """
   MFKQWshortDescriptionHTML_HTML_Field - A description of the release, rendered to HTML without any links in it.

   """
   class HTMLArgs(GQLArgsSet, GQLObject): 
      """
      limit - How many characters to return.

      """
      limit: int

   _args: HTMLArgs



class LMXBNavatarUrl_URI_Field(ArguedStr):
   """
   LMXBNavatarUrl_URI_Field - A URL pointing to the GitHub App's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class SPEYWavatarUrl_URI_Field(ArguedStr):
   """
   SPEYWavatarUrl_URI_Field - A URL pointing to the actor's public avatar.

   """
   class URIArgs(GQLArgsSet, GQLObject): 
      """
      size - The size of the resulting square image.

      """
      size: int

   _args: URIArgs



class VNZOGavatarUrl_URI_Field(ArguedStr):
   """
   VNZOGavatarUrl_URI_Field - A URL pointing to the GitHub App's public avatar.

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


   value - The value which will be set on the field. This field is required.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `value` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   itemId: ID
   fieldId: ID
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

class StarOrder(GQLObject):
   """
   StarOrder - Ways in which star connections can be ordered.

   field - The field in which to order nodes by.

   direction - The direction in which to order nodes.

   """
   field: StarOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorshipNewsletterOrder(GQLObject):
   """
   SponsorshipNewsletterOrder - Ordering options for sponsorship newsletter connections.

   field - The field to order sponsorship newsletters by.

   direction - The ordering direction.

   """
   field: SponsorshipNewsletterOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

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
   kind: SponsorsGoalKind ##NON NULL
   percentComplete: int ##NON NULL
   targetValue: int ##NON NULL
   title: str ##NON NULL

class SponsorableOrder(GQLObject):
   """
   SponsorableOrder - Ordering options for connections to get sponsorable entities for GitHub Sponsors.

   field - The field to order sponsorable entities by.

   direction - The ordering direction.

   """
   field: SponsorableOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SortBy(GQLObject):
   """
   SortBy - Represents a sort by field and direction.

   direction - The direction of the sorting. Possible values are ASC and DESC.

   field - The id of the field by which the column is sorted.

   """
   direction: OrderDirection ##NON NULL
   field: int ##NON NULL

class SetRepositoryInteractionLimitInput(GQLObject):
   """
   SetRepositoryInteractionLimitInput - Autogenerated input type of SetRepositoryInteractionLimit

   repositoryId - The ID of the repository to set a limit for.

   limit - The limit to set.

   expiry - When this limit should expire.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID ##NON NULL
   limit: RepositoryInteractionLimit ##NON NULL
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
   enterpriseId: ID ##NON NULL
   ssoUrl: URI ##NON NULL
   issuer: str
   idpCertificate: str ##NON NULL
   signatureMethod: SamlSignatureAlgorithm ##NON NULL
   digestMethod: SamlDigestAlgorithm ##NON NULL
   clientMutationId: str

class SecurityAdvisoryReference(GQLObject):
   """
   SecurityAdvisoryReference - A GitHub Security Advisory Reference

   url - A publicly accessible reference

   """
   url: URI ##NON NULL

class SecurityAdvisoryPackage(GQLObject):
   """
   SecurityAdvisoryPackage - An individual package

   ecosystem - The ecosystem the package belongs to, e.g. RUBYGEMS, NPM

   name - The package name

   """
   ecosystem: SecurityAdvisoryEcosystem ##NON NULL
   name: str ##NON NULL

class SecurityAdvisoryIdentifierFilter(GQLObject):
   """
   SecurityAdvisoryIdentifierFilter - An advisory identifier to filter results on.

   type - The identifier type.

   value - The identifier string. Supports exact or partial matching.

   """
   type: SecurityAdvisoryIdentifierType ##NON NULL
   value: str ##NON NULL

class SavedReplyOrder(GQLObject):
   """
   SavedReplyOrder - Ordering options for saved reply connections.

   field - The field to order saved replies by.

   direction - The ordering direction.

   """
   field: SavedReplyOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class RevokeMigratorRoleInput(GQLObject):
   """
   RevokeMigratorRoleInput - Autogenerated input type of RevokeMigratorRole

   organizationId - The ID of the organization that the user/team belongs to.

   actor - The user login or Team slug to revoke the migrator role from.

   actorType - Specifies the type of the actor, can be either USER or TEAM.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID ##NON NULL
   actor: str ##NON NULL
   actorType: ActorType ##NON NULL
   clientMutationId: str

class ReviewStatusHovercardContext(GQLObject):
   """
   ReviewStatusHovercardContext - A hovercard context with a message describing the current code review state of the pull
request.


   message - A string describing this context

   octicon - An octicon to accompany this context

   reviewDecision - The current status of the pull request with respect to code review.

   """
   message: str ##NON NULL
   octicon: str ##NON NULL
   reviewDecision: PullRequestReviewDecision

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

class FQUFDisRequired_isRequired_Field(ArguedStr):
   """
   FQUFDisRequired_isRequired_Field - Whether this is required to pass before merging for a specific pull request.

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

class OrgEnterpriseOwnerOrder(GQLObject):
   """
   OrgEnterpriseOwnerOrder - Ordering options for an organization's enterprise owner connections.

   field - The field to order enterprise owners by.

   direction - The ordering direction.

   """
   field: OrgEnterpriseOwnerOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class Node(GQLObject):
   """
   Node - An object with an ID.

   id - ID of the object.

   """
   id: ID ##NON NULL

class MoveProjectCardInput(GQLObject):
   """
   MoveProjectCardInput - Autogenerated input type of MoveProjectCard

   cardId - The id of the card to move.

   columnId - The id of the column to move it into.

   afterCardId - Place the new card after the card with this id. Pass null to place it at the top.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   cardId: ID ##NON NULL
   columnId: ID ##NON NULL
   afterCardId: ID
   clientMutationId: str

class Minimizable(GQLObject):
   """
   Minimizable - Entities that can be minimized.

   isMinimized - Returns whether or not a comment has been minimized.

   minimizedReason - Returns why the comment was minimized. One of `abuse`, `off-topic`, `outdated`, `resolved`, `duplicate` and `spam`. Note that the case and formatting of these values differs from the inputs to the `MinimizeComment` mutation.

   viewerCanMinimize - Check if the current viewer can minimize this object.

   """
   isMinimized: bool ##NON NULL
   minimizedReason: str
   viewerCanMinimize: bool ##NON NULL

class MigrationSource(GQLObject):
   """
   MigrationSource - A GitHub Enterprise Importer (GEI) migration source.

   name - The migration source name.

   type - The migration source type.

   url - The migration source URL.

   """
   id: ID ##NON NULL
   name: str ##NON NULL
   type: MigrationSourceType ##NON NULL
   url: URI ##NON NULL

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
   repositoryId: ID ##NON NULL
   base: str ##NON NULL
   head: str ##NON NULL
   commitMessage: str
   authorEmail: str
   clientMutationId: str

class MarkPullRequestReadyForReviewInput(GQLObject):
   """
   MarkPullRequestReadyForReviewInput - Autogenerated input type of MarkPullRequestReadyForReview

   pullRequestId - ID of the pull request to be marked as ready for review.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID ##NON NULL
   clientMutationId: str

class MarkDiscussionCommentAsAnswerInput(GQLObject):
   """
   MarkDiscussionCommentAsAnswerInput - Autogenerated input type of MarkDiscussionCommentAsAnswer

   id - The Node ID of the discussion comment to mark as an answer.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   clientMutationId: str

class Lockable(GQLObject):
   """
   Lockable - An object that can be locked.

   activeLockReason - Reason that the conversation was locked.

   locked - `true` if the object is locked

   """
   activeLockReason: LockReason
   locked: bool ##NON NULL

class LinkRepositoryToProjectInput(GQLObject):
   """
   LinkRepositoryToProjectInput - Autogenerated input type of LinkRepositoryToProject

   projectId - The ID of the Project to link to a Repository

   repositoryId - The ID of the Repository to link to a Project.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID ##NON NULL
   repositoryId: ID ##NON NULL
   clientMutationId: str

class LinkProjectV2ToRepositoryInput(GQLObject):
   """
   LinkProjectV2ToRepositoryInput - Autogenerated input type of LinkProjectV2ToRepository

   projectId - The ID of the project to link to the repository.

   repositoryId - The ID of the repository to link to the project.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID ##NON NULL
   repositoryId: ID ##NON NULL
   clientMutationId: str

class LanguageOrder(GQLObject):
   """
   LanguageOrder - Ordering options for language connections.

   field - The field to order languages by.

   direction - The ordering direction.

   """
   field: LanguageOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class LabelOrder(GQLObject):
   """
   LabelOrder - Ways in which lists of labels can be ordered upon return.

   field - The field in which to order labels by.

   direction - The direction in which to order labels by the specified field.

   """
   field: LabelOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class IssueOrder(GQLObject):
   """
   IssueOrder - Ways in which lists of issues can be ordered upon return.

   field - The field in which to order issues by.

   direction - The direction in which to order issues by the specified field.

   """
   field: IssueOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class IssueCommentOrder(GQLObject):
   """
   IssueCommentOrder - Ways in which lists of issue comments can be ordered upon return.

   field - The field in which to order issue comments by.

   direction - The direction in which to order issue comments by the specified field.

   """
   field: IssueCommentOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class InviteEnterpriseAdminInput(GQLObject):
   """
   InviteEnterpriseAdminInput - Autogenerated input type of InviteEnterpriseAdmin

   enterpriseId - The ID of the enterprise to which you want to invite an administrator.

   invitee - The login of a user to invite as an administrator.

   email - The email of the person to invite as an administrator.

   role - The role of the administrator.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
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
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class GistOrder(GQLObject):
   """
   GistOrder - Ordering options for gist connections

   field - The field to order repositories by.

   direction - The ordering direction.

   """
   field: GistOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class FundingLink(GQLObject):
   """
   FundingLink - A funding platform link for a repository.

   platform - The funding platform this link is for.

   url - The configured URL for this funding link.

   """
   platform: FundingPlatform ##NON NULL
   url: URI ##NON NULL

class FollowOrganizationInput(GQLObject):
   """
   FollowOrganizationInput - Autogenerated input type of FollowOrganization

   organizationId - ID of the organization to follow.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   organizationId: ID ##NON NULL
   clientMutationId: str

class FileAddition(GQLObject):
   """
   FileAddition - A command to add a file at the given path with the given contents as part of a commit.  Any existing file at that that path will be replaced.

   path - The path in the repository where the file will be located

   contents - The base64 encoded contents of the file

   """
   path: str ##NON NULL
   contents: Base64String ##NON NULL

class EnterpriseServerUserAccountsUploadOrder(GQLObject):
   """
   EnterpriseServerUserAccountsUploadOrder - Ordering options for Enterprise Server user accounts upload connections.

   field - The field to order user accounts uploads by.

   direction - The ordering direction.

   """
   field: EnterpriseServerUserAccountsUploadOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseServerUserAccountEmailOrder(GQLObject):
   """
   EnterpriseServerUserAccountEmailOrder - Ordering options for Enterprise Server user account email connections.

   field - The field to order emails by.

   direction - The ordering direction.

   """
   field: EnterpriseServerUserAccountEmailOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseRepositoryInfo(GQLObject):
   """
   EnterpriseRepositoryInfo - A subset of repository information queryable from an enterprise.

   isPrivate - Identifies if the repository is private or internal.

   name - The repository's name.

   nameWithOwner - The repository's name with owner.

   """
   id: ID ##NON NULL
   isPrivate: bool ##NON NULL
   name: str ##NON NULL
   nameWithOwner: str ##NON NULL

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
   allLicensableUsersCount: int ##NON NULL
   assetPacks: int ##NON NULL
   bandwidthQuota: float ##NON NULL
   bandwidthUsage: float ##NON NULL
   bandwidthUsagePercentage: int ##NON NULL
   storageQuota: float ##NON NULL
   storageUsage: float ##NON NULL
   storageUsagePercentage: int ##NON NULL
   totalAvailableLicenses: int ##NON NULL
   totalLicenses: int ##NON NULL

class EnterpriseAdministratorInvitationOrder(GQLObject):
   """
   EnterpriseAdministratorInvitationOrder - Ordering options for enterprise administrator invitation connections

   field - The field to order enterprise administrator invitations by.

   direction - The ordering direction.

   """
   field: EnterpriseAdministratorInvitationOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

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
   path: str ##NON NULL
   line: int ##NON NULL
   side: DiffSide
   startLine: int
   startSide: DiffSide
   body: str ##NON NULL

class DismissRepositoryVulnerabilityAlertInput(GQLObject):
   """
   DismissRepositoryVulnerabilityAlertInput - Autogenerated input type of DismissRepositoryVulnerabilityAlert

   repositoryVulnerabilityAlertId - The Dependabot alert ID to dismiss.

   dismissReason - The reason the Dependabot alert is being dismissed.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryVulnerabilityAlertId: ID ##NON NULL
   dismissReason: DismissReason ##NON NULL
   clientMutationId: str

class DiscussionPollOptionOrder(GQLObject):
   """
   DiscussionPollOptionOrder - Ordering options for discussion poll option connections.

   field - The field to order poll options by.

   direction - The ordering direction.

   """
   field: DiscussionPollOptionOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class DisablePullRequestAutoMergeInput(GQLObject):
   """
   DisablePullRequestAutoMergeInput - Autogenerated input type of DisablePullRequestAutoMerge

   pullRequestId - ID of the pull request to disable auto merge on.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID ##NON NULL
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
   createdAt: DateTime ##NON NULL
   id: ID ##NON NULL
   key: str ##NON NULL
   readOnly: bool ##NON NULL
   title: str ##NON NULL
   verified: bool ##NON NULL

class DeleteVerifiableDomainInput(GQLObject):
   """
   DeleteVerifiableDomainInput - Autogenerated input type of DeleteVerifiableDomain

   id - The ID of the verifiable domain to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   clientMutationId: str

class DeleteTeamDiscussionInput(GQLObject):
   """
   DeleteTeamDiscussionInput - Autogenerated input type of DeleteTeamDiscussion

   id - The discussion ID to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   clientMutationId: str

class DeleteTeamDiscussionCommentInput(GQLObject):
   """
   DeleteTeamDiscussionCommentInput - Autogenerated input type of DeleteTeamDiscussionComment

   id - The ID of the comment to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   clientMutationId: str

class DeleteRefInput(GQLObject):
   """
   DeleteRefInput - Autogenerated input type of DeleteRef

   refId - The Node ID of the Ref to be deleted.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   refId: ID ##NON NULL
   clientMutationId: str

class DeletePullRequestReviewCommentInput(GQLObject):
   """
   DeletePullRequestReviewCommentInput - Autogenerated input type of DeletePullRequestReviewComment

   id - The ID of the comment to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   clientMutationId: str

class DeleteProjectV2ItemInput(GQLObject):
   """
   DeleteProjectV2ItemInput - Autogenerated input type of DeleteProjectV2Item

   projectId - The ID of the Project from which the item should be removed.

   itemId - The ID of the item to be removed.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   clientMutationId: str

class DeleteProjectNextItemInput(GQLObject):
   """
   DeleteProjectNextItemInput - Autogenerated input type of DeleteProjectNextItem

   projectId - The ID of the Project from which the item should be removed. This field is required.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `projectId` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   itemId - The ID of the item to be removed. This field is required.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `itemId` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   clientMutationId - A unique identifier for the client performing the mutation.

   """
   projectId: ID
   itemId: ID
   clientMutationId: str

class DeleteProjectColumnInput(GQLObject):
   """
   DeleteProjectColumnInput - Autogenerated input type of DeleteProjectColumn

   columnId - The id of the column to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   columnId: ID ##NON NULL
   clientMutationId: str

class DeleteLinkedBranchInput(GQLObject):
   """
   DeleteLinkedBranchInput - Autogenerated input type of DeleteLinkedBranch

   linkedBranchId - The ID of the linked branch

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   linkedBranchId: ID ##NON NULL
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
   ipAllowListEntryId: ID ##NON NULL
   clientMutationId: str

class DeleteEnvironmentInput(GQLObject):
   """
   DeleteEnvironmentInput - Autogenerated input type of DeleteEnvironment

   id - The Node ID of the environment to be deleted.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   clientMutationId: str

class DeleteDiscussionCommentInput(GQLObject):
   """
   DeleteDiscussionCommentInput - Autogenerated input type of DeleteDiscussionComment

   id - The Node id of the discussion comment to delete.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   clientMutationId: str

class DeleteDeploymentInput(GQLObject):
   """
   DeleteDeploymentInput - Autogenerated input type of DeleteDeployment

   id - The Node ID of the deployment to be deleted.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   clientMutationId: str

class DeleteBranchProtectionRuleInput(GQLObject):
   """
   DeleteBranchProtectionRuleInput - Autogenerated input type of DeleteBranchProtectionRule

   branchProtectionRuleId - The global relay id of the branch protection rule to be deleted.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   branchProtectionRuleId: ID ##NON NULL
   clientMutationId: str

class DeclineTopicSuggestionInput(GQLObject):
   """
   DeclineTopicSuggestionInput - Autogenerated input type of DeclineTopicSuggestion

   repositoryId - The Node ID of the repository.

   name - The name of the suggested topic.

   reason - The reason why the suggested topic is declined.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   reason: TopicSuggestionDeclineReason ##NON NULL
   clientMutationId: str

class CreateTeamDiscussionCommentInput(GQLObject):
   """
   CreateTeamDiscussionCommentInput - Autogenerated input type of CreateTeamDiscussionComment

   discussionId - The ID of the discussion to which the comment belongs.

   body - The content of the comment.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   discussionId: ID ##NON NULL
   body: str ##NON NULL
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
   amount: int ##NON NULL
   isRecurring: bool
   repositoryId: ID
   repositoryOwnerLogin: str
   repositoryName: str
   welcomeMessage: str
   description: str ##NON NULL
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
   name: str ##NON NULL
   ownerId: ID
   description: str
   visibility: RepositoryVisibility ##NON NULL
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
   repositoryId: ID ##NON NULL
   baseRefName: str ##NON NULL
   headRefName: str ##NON NULL
   headRepositoryId: ID
   title: str ##NON NULL
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
   ownerId: ID ##NON NULL
   name: str ##NON NULL
   body: str
   template: ProjectTemplate
   repositoryIds: ID ##NON NULL ##LIST
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
   issueId: ID ##NON NULL
   oid: GitObjectID ##NON NULL
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
   ownerId: ID ##NON NULL
   allowListValue: str ##NON NULL
   name: str
   isActive: bool ##NON NULL
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
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   profileName: str ##NON NULL
   billingEmail: str ##NON NULL
   adminLogins: str ##NON NULL ##LIST
   clientMutationId: str

class CreateCheckSuiteInput(GQLObject):
   """
   CreateCheckSuiteInput - Autogenerated input type of CreateCheckSuite

   repositoryId - The Node ID of the repository.

   headSha - The SHA of the head commit.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID ##NON NULL
   headSha: GitObjectID ##NON NULL
   clientMutationId: str

class ConvertPullRequestToDraftInput(GQLObject):
   """
   ConvertPullRequestToDraftInput - Autogenerated input type of ConvertPullRequestToDraft

   pullRequestId - ID of the pull request to convert to draft

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID ##NON NULL
   clientMutationId: str

class ContributionOrder(GQLObject):
   """
   ContributionOrder - Ordering options for contribution connections.

   direction - The ordering direction.

   """
   direction: OrderDirection ##NON NULL

class ContributionCalendarDay(GQLObject):
   """
   ContributionCalendarDay - Represents a single day of contributions on GitHub by a user.

   color - The hex color code that represents how many contributions were made on this day compared to others in the calendar.

   contributionCount - How many contributions were made by the user on this day.

   contributionLevel - Indication of contributions, relative to other days. Can be used to indicate which color to represent this day on a calendar.

   date - The day this square represents.

   weekday - A number representing which day of the week this square represents, e.g., 1 is Monday.

   """
   color: str ##NON NULL
   contributionCount: int ##NON NULL
   contributionLevel: ContributionLevel ##NON NULL
   date: Date ##NON NULL
   weekday: int ##NON NULL

class CommitMessage(GQLObject):
   """
   CommitMessage - A message to include with a new commit

   headline - The headline of the message.

   body - The body of the message.

   """
   headline: str ##NON NULL
   body: str

class CommitAuthor(GQLObject):
   """
   CommitAuthor - Specifies an author for filtering Git commits.

   id - ID of a User to filter by. If non-null, only commits authored by this user will be returned. This field takes precedence over emails.

   emails - Email addresses to filter by. Commits authored by any of the specified email addresses will be returned.

   """
   id: ID
   emails: str ##NON NULL ##LIST

class ClosePullRequestInput(GQLObject):
   """
   ClosePullRequestInput - Autogenerated input type of ClosePullRequest

   pullRequestId - ID of the pull request to be closed.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pullRequestId: ID ##NON NULL
   clientMutationId: str

class Closable(GQLObject):
   """
   Closable - An object that can be closed

   closed - `true` if the object is closed (definition of closed may depend on type)

   closedAt - Identifies the date and time when the object was closed.

   """
   closed: bool ##NON NULL
   closedAt: DateTime

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
   targetOwnerId: ID ##NON NULL
   sourceId: ID ##NON NULL
   includeWorkflows: bool ##NON NULL
   name: str ##NON NULL
   body: str
   public: bool
   clientMutationId: str

class ClearLabelsFromLabelableInput(GQLObject):
   """
   ClearLabelsFromLabelableInput - Autogenerated input type of ClearLabelsFromLabelable

   labelableId - The id of the labelable object to clear the labels from.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   labelableId: ID ##NON NULL
   clientMutationId: str

class CheckSuiteAutoTriggerPreference(GQLObject):
   """
   CheckSuiteAutoTriggerPreference - The auto-trigger preferences that are available for check suites.

   appId - The node ID of the application that owns the check suite.

   setting - Set to `true` to enable automatic creation of CheckSuite events upon pushes to the repository.

   """
   appId: ID ##NON NULL
   setting: bool ##NON NULL

class CheckRunStateCount(GQLObject):
   """
   CheckRunStateCount - Represents a count of the state of a check run.

   count - The number of check runs with this state.

   state - The state of a check run.

   """
   count: int ##NON NULL
   state: CheckRunState ##NON NULL

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
   statuses: CheckStatusState ##NON NULL ##LIST
   conclusions: CheckConclusionState ##NON NULL ##LIST

class CheckAnnotationRange(GQLObject):
   """
   CheckAnnotationRange - Information from a check run analysis to specific lines of code.

   startLine - The starting line of the range.

   startColumn - The starting column of the range.

   endLine - The ending line of the range.

   endColumn - The ending column of the range.

   """
   startLine: int ##NON NULL
   startColumn: int
   endLine: int ##NON NULL
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
   invitationId: ID ##NON NULL
   clientMutationId: str

class CVSS(GQLObject):
   """
   CVSS - The Common Vulnerability Scoring System

   score - The CVSS score associated with this advisory

   vectorString - The CVSS vector string associated with this advisory

   """
   score: float ##NON NULL
   vectorString: str

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
   avatarUrl: VNZOGavatarUrl_URI_Field
   createdAt: DateTime ##NON NULL
   databaseId: int
   id: ID ##NON NULL
   login: str ##NON NULL
   resourcePath: URI ##NON NULL
   updatedAt: DateTime ##NON NULL
   url: URI ##NON NULL

class ArchiveRepositoryInput(GQLObject):
   """
   ArchiveRepositoryInput - Autogenerated input type of ArchiveRepository

   repositoryId - The ID of the repository to mark as archived.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   repositoryId: ID ##NON NULL
   clientMutationId: str

class ApproveVerifiableDomainInput(GQLObject):
   """
   ApproveVerifiableDomainInput - Autogenerated input type of ApproveVerifiableDomain

   id - The ID of the verifiable domain to approve.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   id: ID ##NON NULL
   clientMutationId: str

class AddVerifiableDomainInput(GQLObject):
   """
   AddVerifiableDomainInput - Autogenerated input type of AddVerifiableDomain

   ownerId - The ID of the owner to add the domain to

   domain - The URL of the domain

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID ##NON NULL
   domain: URI ##NON NULL
   clientMutationId: str

class AddStarInput(GQLObject):
   """
   AddStarInput - Autogenerated input type of AddStar

   starrableId - The Starrable ID to star.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   starrableId: ID ##NON NULL
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
   path: str ##NON NULL
   body: str ##NON NULL
   pullRequestId: ID
   pullRequestReviewId: ID
   line: int ##NON NULL
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
   projectId: ID ##NON NULL
   contentId: ID ##NON NULL
   clientMutationId: str

class AddProjectNextItemInput(GQLObject):
   """
   AddProjectNextItemInput - Autogenerated input type of AddProjectNextItem

   projectId - The ID of the Project to add the item to. This field is required.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `projectId` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


   contentId - The content id of the item (Issue or PullRequest). This field is required.

**Upcoming Change on 2023-01-01 UTC**
**Description:** `contentId` will be removed. Follow the ProjectV2 guide at https://github.blog/changelog/2022-06-23-the-new-github-issues-june-23rd-update/, to find a suitable replacement.
**Reason:** The `ProjectNext` API is deprecated in favour of the more capable `ProjectV2` API.


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
   projectId: ID ##NON NULL
   name: str ##NON NULL
   clientMutationId: str

class AddLabelsToLabelableInput(GQLObject):
   """
   AddLabelsToLabelableInput - Autogenerated input type of AddLabelsToLabelable

   labelableId - The id of the labelable object to add labels to.

   labelIds - The ids of the labels to add.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   labelableId: ID ##NON NULL
   labelIds: ID ##NON NULL ##LIST
   clientMutationId: str

class AddEnterpriseSupportEntitlementInput(GQLObject):
   """
   AddEnterpriseSupportEntitlementInput - Autogenerated input type of AddEnterpriseSupportEntitlement

   enterpriseId - The ID of the Enterprise which the admin belongs to.

   login - The login of a member who will receive the support entitlement.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class AddDiscussionPollVoteInput(GQLObject):
   """
   AddDiscussionPollVoteInput - Autogenerated input type of AddDiscussionPollVote

   pollOptionId - The Node ID of the discussion poll option to vote for.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   pollOptionId: ID ##NON NULL
   clientMutationId: str

class AddCommentInput(GQLObject):
   """
   AddCommentInput - Autogenerated input type of AddComment

   subjectId - The Node ID of the subject to modify.

   body - The contents of the comment.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   subjectId: ID ##NON NULL
   body: str ##NON NULL
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
   avatarUrl: SPEYWavatarUrl_URI_Field
   login: str ##NON NULL
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class AcceptEnterpriseAdministratorInvitationInput(GQLObject):
   """
   AcceptEnterpriseAdministratorInvitationInput - Autogenerated input type of AcceptEnterpriseAdministratorInvitation

   invitationId - The id of the invitation being accepted

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   invitationId: ID ##NON NULL
   clientMutationId: str

class AbortQueuedMigrationsInput(GQLObject):
   """
   AbortQueuedMigrationsInput - Autogenerated input type of AbortQueuedMigrations

   ownerId - The ID of the organization that is running the migrations.

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID ##NON NULL
   clientMutationId: str
