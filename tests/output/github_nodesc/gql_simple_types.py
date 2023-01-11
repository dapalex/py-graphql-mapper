from typing import Generic
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import ID
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *

class WFJINanyPinnableItems_anyPinnableItems_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      type: PinnableItemType

   _args: boolArgs



class TFGINlogoUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class PWCKBlogoUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class RYMBWavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class TBIOZshortDescriptionHTML_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject): 
      limit: int

   _args: HTMLArgs



class LGGPVavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class RJNKNtotalSponsorshipAmountAsSponsorInCents_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject): 
      since: DateTime
      until: DateTime
      sponsorableLogins: str ##NON NULL ##LIST

   _args: intArgs



class FTVHUisSponsoredBy_isSponsoredBy_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      accountLogin: str ##NON NULL

   _args: boolArgs



class CIEGFavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class TUIMCanyPinnableItems_anyPinnableItems_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      type: PinnableItemType

   _args: boolArgs



class TTQFXtotalSponsorshipAmountAsSponsorInCents_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject): 
      since: DateTime
      until: DateTime
      sponsorableLogins: str ##NON NULL ##LIST

   _args: intArgs



class VOKLTorganizationVerifiedDomainEmails_organizationVerifiedDomainEmails_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: strArgs



class NJGXQisSponsoredBy_isSponsoredBy_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      accountLogin: str ##NON NULL

   _args: boolArgs



class EUQZPcanReceiveOrganizationEmailsWhenNotificationsRestricted_canReceiveOrganizationEmailsWhenNotificationsRestricted_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      login: str ##NON NULL

   _args: boolArgs



class CXWXWavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class PAVFBanyPinnableItems_anyPinnableItems_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      type: PinnableItemType

   _args: boolArgs



class SKLUNtotalSponsorshipAmountAsSponsorInCents_totalSponsorshipAmountAsSponsorInCents_Field(ArguedInt):
   class intArgs(GQLArgsSet, GQLObject): 
      since: DateTime
      until: DateTime
      sponsorableLogins: str ##NON NULL ##LIST

   _args: intArgs



class ZBRXEisSponsoredBy_isSponsoredBy_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      accountLogin: str ##NON NULL

   _args: boolArgs



class FJLCMtext_text_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject): 
      truncate: int

   _args: strArgs



class WRAUHtotalRepositoryContributions_totalRepositoryContributions_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      excludeFirst: bool

   _args: intArgs



class MKNWQtotalRepositoriesWithContributedPullRequests_totalRepositoriesWithContributedPullRequests_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class DTRDFtotalRepositoriesWithContributedIssues_totalRepositoriesWithContributedIssues_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class YKCTStotalPullRequestContributions_totalPullRequestContributions_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class YPMUQtotalIssueContributions_totalIssueContributions_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      excludeFirst: bool
      excludePopular: bool

   _args: intArgs



class BGXTIisRequired_isRequired_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class CGJEFavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class AJAYYisRequired_isRequired_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class AYRUCavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class DCFSAviewerMergeHeadlineText_viewerMergeHeadlineText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject): 
      mergeType: PullRequestMergeMethod

   _args: strArgs



class IDPRXviewerMergeBodyText_viewerMergeBodyText_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject): 
      mergeType: PullRequestMergeMethod

   _args: strArgs



class DHJTLavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class ZJDREtrackedIssuesCount_trackedIssuesCount_Field(ArguedStr):
   class intArgs(GQLArgsSet, GQLObject): 
      states: TrackedIssueStates ##LIST

   _args: intArgs



class BEWAXshortDescriptionHTML_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject): 
      limit: int

   _args: HTMLArgs



class EVFVBavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class NDSVKshortDescriptionHTML_HTML_Field(ArguedStr):
   class HTMLArgs(GQLArgsSet, GQLObject): 
      limit: int

   _args: HTMLArgs



class SORVHavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class WorkflowRunOrder(GQLObject):
   field: WorkflowRunOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class VerifyVerifiableDomainInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class UserStatusOrder(GQLObject):
   field: UserStatusOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class UpdateTopicsInput(GQLObject):
   repositoryId: ID ##NON NULL
   topicNames: str ##NON NULL ##LIST
   clientMutationId: str

class UpdateTeamDiscussionInput(GQLObject):
   id: ID ##NON NULL
   title: str
   body: str
   bodyVersion: str
   pinned: bool
   clientMutationId: str

class UpdateSubscriptionInput(GQLObject):
   subscribableId: ID ##NON NULL
   state: SubscriptionState ##NON NULL
   clientMutationId: str

class UpdateRepositoryWebCommitSignoffSettingInput(GQLObject):
   repositoryId: ID ##NON NULL
   webCommitSignoffRequired: bool ##NON NULL
   clientMutationId: str

class UpdateRefInput(GQLObject):
   refId: ID ##NON NULL
   oid: GitObjectID ##NON NULL
   force: bool
   clientMutationId: str

class UpdatePullRequestReviewCommentInput(GQLObject):
   pullRequestReviewCommentId: ID ##NON NULL
   body: str ##NON NULL
   clientMutationId: str

class UpdatePullRequestBranchInput(GQLObject):
   pullRequestId: ID ##NON NULL
   expectedHeadOid: GitObjectID
   clientMutationId: str

class UpdateProjectV2Input(GQLObject):
   projectId: ID ##NON NULL
   title: str
   shortDescription: str
   readme: str
   closed: bool
   public: bool
   clientMutationId: str

class UpdateProjectNextItemFieldInput(GQLObject):
   projectId: ID
   itemId: ID
   fieldId: ID
   fieldWithSettingId: ID
   fieldConstraintId: ID
   value: str
   clientMutationId: str

class UpdateProjectInput(GQLObject):
   projectId: ID ##NON NULL
   name: str
   body: str
   state: ProjectState
   public: bool
   clientMutationId: str

class UpdateProjectColumnInput(GQLObject):
   projectColumnId: ID ##NON NULL
   name: str ##NON NULL
   clientMutationId: str

class UpdateOrganizationWebCommitSignoffSettingInput(GQLObject):
   organizationId: ID ##NON NULL
   webCommitSignoffRequired: bool ##NON NULL
   clientMutationId: str

class UpdateNotificationRestrictionSettingInput(GQLObject):
   ownerId: ID ##NON NULL
   settingValue: NotificationRestrictionSettingValue ##NON NULL
   clientMutationId: str

class UpdateIssueCommentInput(GQLObject):
   id: ID ##NON NULL
   body: str ##NON NULL
   clientMutationId: str

class UpdateIpAllowListEntryInput(GQLObject):
   ipAllowListEntryId: ID ##NON NULL
   allowListValue: str ##NON NULL
   name: str
   isActive: bool ##NON NULL
   clientMutationId: str

class UpdateEnvironmentInput(GQLObject):
   environmentId: ID ##NON NULL
   waitTimer: int
   reviewers: ID ##NON NULL ##LIST
   clientMutationId: str

class UpdateEnterpriseTeamDiscussionsSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseProfileInput(GQLObject):
   enterpriseId: ID ##NON NULL
   name: str
   description: str
   websiteUrl: str
   location: str
   clientMutationId: str

class UpdateEnterpriseOwnerOrganizationRoleInput(GQLObject):
   enterpriseId: ID ##NON NULL
   organizationId: ID ##NON NULL
   organizationRole: RoleInOrganization ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanMakePurchasesSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseMembersCanMakePurchasesSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseEnabledDisabledSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseMembersCanCreateRepositoriesSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseMembersCanCreateRepositoriesSettingValue
   membersCanCreateRepositoriesPolicyEnabled: bool
   membersCanCreatePublicRepositories: bool
   membersCanCreatePrivateRepositories: bool
   membersCanCreateInternalRepositories: bool
   clientMutationId: str

class UpdateEnterpriseDefaultRepositoryPermissionSettingInput(GQLObject):
   enterpriseId: ID ##NON NULL
   settingValue: EnterpriseDefaultRepositoryPermissionSettingValue ##NON NULL
   clientMutationId: str

class UpdateEnterpriseAdministratorRolePayload(GQLObject):
   clientMutationId: str
   message: str

class UpdateDiscussionInput(GQLObject):
   discussionId: ID ##NON NULL
   title: str
   body: str
   categoryId: ID
   clientMutationId: str

class UpdatableComment(GQLObject):
   viewerCannotUpdateReasons: CommentCannotUpdateReason ##NON NULL

class UnresolveReviewThreadInput(GQLObject):
   threadId: ID ##NON NULL
   clientMutationId: str

class UnminimizeCommentInput(GQLObject):
   subjectId: ID ##NON NULL
   clientMutationId: str

class UnmarkFileAsViewedInput(GQLObject):
   pullRequestId: ID ##NON NULL
   path: str ##NON NULL
   clientMutationId: str

class UnlockLockableInput(GQLObject):
   lockableId: ID ##NON NULL
   clientMutationId: str

class UnlinkProjectV2FromTeamInput(GQLObject):
   projectId: ID ##NON NULL
   teamId: ID ##NON NULL
   clientMutationId: str

class UniformResourceLocatable(GQLObject):
   resourcePath: URI ##NON NULL
   url: URI ##NON NULL

class UnfollowOrganizationInput(GQLObject):
   organizationId: ID ##NON NULL
   clientMutationId: str

class UnarchiveProjectV2ItemInput(GQLObject):
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   clientMutationId: str

class TransferEnterpriseOrganizationInput(GQLObject):
   organizationId: ID ##NON NULL
   destinationEnterpriseId: ID ##NON NULL
   clientMutationId: str

class TeamRepositoryOrder(GQLObject):
   field: TeamRepositoryOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class TeamMemberOrder(GQLObject):
   field: TeamMemberOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class TeamDiscussionCommentOrder(GQLObject):
   field: TeamDiscussionCommentOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class Submodule(GQLObject):
   branch: str
   gitUrl: URI ##NON NULL
   name: str ##NON NULL
   nameRaw: Base64String ##NON NULL
   path: str ##NON NULL
   pathRaw: Base64String ##NON NULL
   subprojectCommitOid: GitObjectID

class StatusContextStateCount(GQLObject):
   count: int ##NON NULL
   state: StatusState ##NON NULL

class StartOrganizationMigrationInput(GQLObject):
   sourceOrgUrl: URI ##NON NULL
   targetOrgName: str ##NON NULL
   targetEnterpriseId: ID ##NON NULL
   sourceAccessToken: str ##NON NULL
   clientMutationId: str

class SponsorshipOrder(GQLObject):
   field: SponsorshipOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorsTierOrder(GQLObject):
   field: SponsorsTierOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorsActivityOrder(GQLObject):
   field: SponsorsActivityOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SponsorOrder(GQLObject):
   field: SponsorOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SetUserInteractionLimitInput(GQLObject):
   userId: ID ##NON NULL
   limit: RepositoryInteractionLimit ##NON NULL
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SetOrganizationInteractionLimitInput(GQLObject):
   organizationId: ID ##NON NULL
   limit: RepositoryInteractionLimit ##NON NULL
   expiry: RepositoryInteractionLimitExpiry
   clientMutationId: str

class SecurityVulnerabilityOrder(GQLObject):
   field: SecurityVulnerabilityOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SecurityAdvisoryPackageVersion(GQLObject):
   identifier: str ##NON NULL

class SecurityAdvisoryOrder(GQLObject):
   field: SecurityAdvisoryOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class SecurityAdvisoryIdentifier(GQLObject):
   type: str ##NON NULL
   value: str ##NON NULL

class RevokeMigratorRolePayload(GQLObject):
   clientMutationId: str
   success: bool

class RevokeEnterpriseOrganizationsMigratorRoleInput(GQLObject):
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class RetireSponsorsTierInput(GQLObject):
   tierId: ID ##NON NULL
   clientMutationId: str

class RerequestCheckSuiteInput(GQLObject):
   repositoryId: ID ##NON NULL
   checkSuiteId: ID ##NON NULL
   clientMutationId: str

class ZKGFLisRequired_isRequired_Field(ArguedStr):
   class boolArgs(GQLArgsSet, GQLObject): 
      pullRequestId: ID
      pullRequestNumber: int

   _args: boolArgs



class RequestReviewsInput(GQLObject):
   pullRequestId: ID ##NON NULL
   userIds: ID ##NON NULL ##LIST
   teamIds: ID ##NON NULL ##LIST
   union: bool
   clientMutationId: str

class RepositoryMigrationOrder(GQLObject):
   field: RepositoryMigrationOrderField ##NON NULL
   direction: RepositoryMigrationOrderDirection ##NON NULL

class RepositoryInteractionAbility(GQLObject):
   expiresAt: DateTime
   limit: RepositoryInteractionLimit ##NON NULL
   origin: RepositoryInteractionLimitOrigin ##NON NULL

class RepositoryCodeownersError(GQLObject):
   column: int ##NON NULL
   kind: str ##NON NULL
   line: int ##NON NULL
   message: str ##NON NULL
   path: str ##NON NULL
   source: str ##NON NULL
   suggestion: str

class ReopenIssueInput(GQLObject):
   issueId: ID ##NON NULL
   clientMutationId: str

class RemoveStarInput(GQLObject):
   starrableId: ID ##NON NULL
   clientMutationId: str

class RemoveOutsideCollaboratorInput(GQLObject):
   userId: ID ##NON NULL
   organizationId: ID ##NON NULL
   clientMutationId: str

class RemoveEnterpriseSupportEntitlementPayload(GQLObject):
   clientMutationId: str
   message: str

class RemoveEnterpriseOrganizationInput(GQLObject):
   enterpriseId: ID ##NON NULL
   organizationId: ID ##NON NULL
   clientMutationId: str

class RemoveEnterpriseAdminInput(GQLObject):
   enterpriseId: ID ##NON NULL
   login: str ##NON NULL
   clientMutationId: str

class ReleaseOrder(GQLObject):
   field: ReleaseOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class RegenerateVerifiableDomainTokenPayload(GQLObject):
   clientMutationId: str
   verificationToken: str

class RegenerateEnterpriseIdentityProviderRecoveryCodesInput(GQLObject):
   enterpriseId: ID ##NON NULL
   clientMutationId: str

class RefOrder(GQLObject):
   field: RefOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class RateLimit(GQLObject):
   cost: int ##NON NULL
   limit: int ##NON NULL
   nodeCount: int ##NON NULL
   remaining: int ##NON NULL
   resetAt: DateTime ##NON NULL
   used: int ##NON NULL

class PullRequestChangedFile(GQLObject):
   additions: int ##NON NULL
   changeType: PatchStatus ##NON NULL
   deletions: int ##NON NULL
   path: str ##NON NULL
   viewerViewedState: FileViewedState ##NON NULL

class PublicKey(GQLObject):
   accessedAt: DateTime
   createdAt: DateTime
   fingerprint: str ##NON NULL
   id: ID ##NON NULL
   isReadOnly: bool
   key: str ##NON NULL
   updatedAt: DateTime

class ProjectV2SingleSelectFieldOption(GQLObject):
   id: str ##NON NULL
   name: str ##NON NULL
   nameHTML: str ##NON NULL

class ProjectV2IterationFieldIteration(GQLObject):
   duration: int ##NON NULL
   id: str ##NON NULL
   startDate: Date ##NON NULL
   title: str ##NON NULL
   titleHTML: str ##NON NULL

class ProjectV2ItemFieldValueOrder(GQLObject):
   field: ProjectV2ItemFieldValueOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class ProjectV2FieldValue(GQLObject):
   text: str
   number: float
   date: Date
   singleSelectOptionId: str
   iterationId: str

class ProjectProgress(GQLObject):
   doneCount: int ##NON NULL
   donePercentage: float ##NON NULL
   enabled: bool ##NON NULL
   inProgressCount: int ##NON NULL
   inProgressPercentage: float ##NON NULL
   todoCount: int ##NON NULL
   todoPercentage: float ##NON NULL

class PinIssueInput(GQLObject):
   issueId: ID ##NON NULL
   clientMutationId: str

class PackageVersionStatistics(GQLObject):
   downloadsTotalCount: int ##NON NULL

class PackageStatistics(GQLObject):
   downloadsTotalCount: int ##NON NULL

class PackageFileOrder(GQLObject):
   field: PackageFileOrderField
   direction: OrderDirection

class OrganizationMigration(GQLObject):
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
   oauthApplicationName: str
   oauthApplicationResourcePath: URI
   oauthApplicationUrl: URI

class MoveProjectColumnInput(GQLObject):
   columnId: ID ##NON NULL
   afterColumnId: ID
   clientMutationId: str

class MinimizeCommentInput(GQLObject):
   subjectId: ID ##NON NULL
   classifier: ReportedContentClassifiers ##NON NULL
   clientMutationId: str

class MilestoneOrder(GQLObject):
   field: MilestoneOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class MergePullRequestInput(GQLObject):
   pullRequestId: ID ##NON NULL
   commitHeadline: str
   commitBody: str
   expectedHeadOid: GitObjectID
   mergeMethod: PullRequestMergeMethod
   authorEmail: str
   clientMutationId: str

class MarketplaceCategory(GQLObject):
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
   pullRequestId: ID ##NON NULL
   path: str ##NON NULL
   clientMutationId: str

class MannequinOrder(GQLObject):
   field: MannequinOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class LockLockableInput(GQLObject):
   lockableId: ID ##NON NULL
   lockReason: LockReason
   clientMutationId: str

class LinkProjectV2ToTeamInput(GQLObject):
   projectId: ID ##NON NULL
   teamId: ID ##NON NULL
   clientMutationId: str

class LicenseRule(GQLObject):
   description: str ##NON NULL
   key: str ##NON NULL
   label: str ##NON NULL

class Language(GQLObject):
   color: str
   id: ID ##NON NULL
   name: str ##NON NULL

class IssueTemplate(GQLObject):
   about: str
   body: str
   filename: str ##NON NULL
   name: str ##NON NULL
   title: str

class IssueFilters(GQLObject):
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
   field: IpAllowListEntryOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class HovercardContext(GQLObject):
   message: str ##NON NULL
   octicon: str ##NON NULL

class GrantMigratorRoleInput(GQLObject):
   organizationId: ID ##NON NULL
   actor: str ##NON NULL
   actorType: ActorType ##NON NULL
   clientMutationId: str

class GitHubMetadata(GQLObject):
   gitHubServicesSha: GitObjectID ##NON NULL
   gitIpAddresses: str ##LIST
   hookIpAddresses: str ##LIST
   importerIpAddresses: str ##LIST
   isPasswordAuthenticationVerifiable: bool ##NON NULL
   pagesIpAddresses: str ##LIST

class GenericHovercardContext(GQLObject):
   message: str ##NON NULL
   octicon: str ##NON NULL

class FollowUserInput(GQLObject):
   userId: ID ##NON NULL
   clientMutationId: str

class FileDeletion(GQLObject):
   path: str ##NON NULL

class ExternalIdentityAttribute(GQLObject):
   metadata: str
   name: str ##NON NULL
   value: str ##NON NULL

class EnterpriseServerUserAccountOrder(GQLObject):
   field: EnterpriseServerUserAccountOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseServerInstallationOrder(GQLObject):
   field: EnterpriseServerInstallationOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseMemberOrder(GQLObject):
   field: EnterpriseMemberOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class EnterpriseAuditEntryData(GQLObject):
   enterpriseResourcePath: URI
   enterpriseSlug: str
   enterpriseUrl: URI

class EnablePullRequestAutoMergeInput(GQLObject):
   pullRequestId: ID ##NON NULL
   commitHeadline: str
   commitBody: str
   mergeMethod: PullRequestMergeMethod
   authorEmail: str
   clientMutationId: str

class DraftPullRequestReviewComment(GQLObject):
   path: str ##NON NULL
   position: int ##NON NULL
   body: str ##NON NULL

class DismissPullRequestReviewInput(GQLObject):
   pullRequestReviewId: ID ##NON NULL
   message: str ##NON NULL
   clientMutationId: str

class DiscussionOrder(GQLObject):
   field: DiscussionOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class DeploymentOrder(GQLObject):
   field: DeploymentOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class DependabotUpdateError(GQLObject):
   body: str ##NON NULL
   errorType: str ##NON NULL
   title: str ##NON NULL

class DeleteTeamDiscussionPayload(GQLObject):
   clientMutationId: str

class DeleteTeamDiscussionCommentPayload(GQLObject):
   clientMutationId: str

class DeleteRefPayload(GQLObject):
   clientMutationId: str

class DeletePullRequestReviewInput(GQLObject):
   pullRequestReviewId: ID ##NON NULL
   clientMutationId: str

class DeleteProjectV2ItemPayload(GQLObject):
   clientMutationId: str
   deletedItemId: ID

class DeleteProjectNextItemPayload(GQLObject):
   clientMutationId: str

class DeleteProjectInput(GQLObject):
   projectId: ID ##NON NULL
   clientMutationId: str

class DeleteProjectCardInput(GQLObject):
   cardId: ID ##NON NULL
   clientMutationId: str

class DeleteIssueInput(GQLObject):
   issueId: ID ##NON NULL
   clientMutationId: str

class DeleteIssueCommentInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteEnvironmentPayload(GQLObject):
   clientMutationId: str

class DeleteDiscussionInput(GQLObject):
   id: ID ##NON NULL
   clientMutationId: str

class DeleteDeploymentPayload(GQLObject):
   clientMutationId: str

class DeleteBranchProtectionRulePayload(GQLObject):
   clientMutationId: str

class Deletable(GQLObject):
   viewerCanDelete: bool ##NON NULL

class CreateTeamDiscussionInput(GQLObject):
   teamId: ID ##NON NULL
   title: str ##NON NULL
   body: str ##NON NULL
   private: bool
   clientMutationId: str

class CreateSponsorshipInput(GQLObject):
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
   sponsorableLogin: str
   fiscalHostLogin: str
   fiscallyHostedProjectProfileUrl: str
   billingCountryOrRegionCode: SponsorsCountryOrRegionCode
   residenceCountryOrRegionCode: SponsorsCountryOrRegionCode
   contactEmail: str
   fullDescription: str
   clientMutationId: str

class CreateRefInput(GQLObject):
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   oid: GitObjectID ##NON NULL
   clientMutationId: str

class CreateProjectV2Input(GQLObject):
   ownerId: ID ##NON NULL
   title: str ##NON NULL
   repositoryId: ID
   teamId: ID
   clientMutationId: str

class CreateMigrationSourceInput(GQLObject):
   name: str ##NON NULL
   url: str ##NON NULL
   accessToken: str
   type: MigrationSourceType ##NON NULL
   ownerId: ID ##NON NULL
   githubPat: str
   clientMutationId: str

class CreateIssueInput(GQLObject):
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
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   clientMutationId: str

class CreateDiscussionInput(GQLObject):
   repositoryId: ID ##NON NULL
   title: str ##NON NULL
   body: str ##NON NULL
   categoryId: ID ##NON NULL
   clientMutationId: str

class CreateAttributionInvitationInput(GQLObject):
   ownerId: ID ##NON NULL
   sourceId: ID ##NON NULL
   targetId: ID ##NON NULL
   clientMutationId: str

class ConvertProjectCardNoteToIssueInput(GQLObject):
   projectCardId: ID ##NON NULL
   repositoryId: ID ##NON NULL
   title: str
   body: str
   clientMutationId: str

class ContributionCalendarMonth(GQLObject):
   firstDay: Date ##NON NULL
   name: str ##NON NULL
   totalWeeks: int ##NON NULL
   year: int ##NON NULL

class CommittableBranch(GQLObject):
   id: ID
   repositoryNameWithOwner: str
   branchName: str

class CommitContributionOrder(GQLObject):
   field: CommitContributionOrderField ##NON NULL
   direction: OrderDirection ##NON NULL

class CodeOfConduct(GQLObject):
   body: str
   id: ID ##NON NULL
   key: str ##NON NULL
   name: str ##NON NULL
   resourcePath: URI
   url: URI

class CloseIssueInput(GQLObject):
   issueId: ID ##NON NULL
   stateReason: IssueClosedStateReason
   clientMutationId: str

class CloneTemplateRepositoryInput(GQLObject):
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   ownerId: ID ##NON NULL
   description: str
   visibility: RepositoryVisibility ##NON NULL
   includeAllBranches: bool
   clientMutationId: str

class ClearProjectV2ItemFieldValueInput(GQLObject):
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   fieldId: ID ##NON NULL
   clientMutationId: str

class CheckSuiteFilter(GQLObject):
   appId: int
   checkName: str

class CheckStep(GQLObject):
   completedAt: DateTime
   conclusion: CheckConclusionState
   externalId: str
   name: str ##NON NULL
   number: int ##NON NULL
   secondsToCompletion: int
   startedAt: DateTime
   status: CheckStatusState ##NON NULL

class CheckRunOutputImage(GQLObject):
   alt: str ##NON NULL
   imageUrl: URI ##NON NULL
   caption: str

class CheckRunAction(GQLObject):
   label: str ##NON NULL
   description: str ##NON NULL
   identifier: str ##NON NULL

class CheckAnnotationPosition(GQLObject):
   column: int
   line: int ##NON NULL

class CancelSponsorshipInput(GQLObject):
   sponsorId: ID
   sponsorLogin: str
   sponsorableId: ID
   sponsorableLogin: str
   clientMutationId: str

class CWE(GQLObject):
   cweId: str ##NON NULL
   description: str ##NON NULL
   id: ID ##NON NULL
   name: str ##NON NULL

class VYVHFavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class AuditLogOrder(GQLObject):
   field: AuditLogOrderField
   direction: OrderDirection

class ArchiveProjectV2ItemInput(GQLObject):
   projectId: ID ##NON NULL
   itemId: ID ##NON NULL
   clientMutationId: str

class ApproveDeploymentsInput(GQLObject):
   workflowRunId: ID ##NON NULL
   environmentIds: ID ##NON NULL ##LIST
   comment: str
   clientMutationId: str

class AddUpvoteInput(GQLObject):
   subjectId: ID ##NON NULL
   clientMutationId: str

class AddReactionInput(GQLObject):
   subjectId: ID ##NON NULL
   content: ReactionContent ##NON NULL
   clientMutationId: str

class AddPullRequestReviewCommentInput(GQLObject):
   pullRequestId: ID
   pullRequestReviewId: ID
   commitOID: GitObjectID
   body: str ##NON NULL
   path: str
   position: int
   inReplyTo: ID
   clientMutationId: str

class AddProjectV2DraftIssueInput(GQLObject):
   projectId: ID ##NON NULL
   title: str ##NON NULL
   body: str
   assigneeIds: ID ##NON NULL ##LIST
   clientMutationId: str

class AddProjectDraftIssueInput(GQLObject):
   projectId: ID
   title: str
   body: str
   assigneeIds: ID ##NON NULL ##LIST
   clientMutationId: str

class AddProjectCardInput(GQLObject):
   projectColumnId: ID ##NON NULL
   contentId: ID
   note: str
   clientMutationId: str

class AddEnterpriseSupportEntitlementPayload(GQLObject):
   clientMutationId: str
   message: str

class AddEnterpriseOrganizationMemberInput(GQLObject):
   enterpriseId: ID ##NON NULL
   organizationId: ID ##NON NULL
   userIds: ID ##NON NULL ##LIST
   role: OrganizationMemberRole
   clientMutationId: str

class AddDiscussionCommentInput(GQLObject):
   discussionId: ID ##NON NULL
   replyToId: ID
   body: str ##NON NULL
   clientMutationId: str

class AddAssigneesToAssignableInput(GQLObject):
   assignableId: ID ##NON NULL
   assigneeIds: ID ##NON NULL ##LIST
   clientMutationId: str

class JFRTRavatarUrl_URI_Field(ArguedStr):
   class URIArgs(GQLArgsSet, GQLObject): 
      size: int

   _args: URIArgs



class AcceptTopicSuggestionInput(GQLObject):
   repositoryId: ID ##NON NULL
   name: str ##NON NULL
   clientMutationId: str

class AbortQueuedMigrationsPayload(GQLObject):
   clientMutationId: str
   success: bool
