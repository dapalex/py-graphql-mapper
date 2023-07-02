from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class QHWJB_name_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      showDeleted: bool

   _args: strArgs



class Exclusion(GQLObject):
   topic: str

class UpdateWorkflowsInput(GQLObject):
   workflowIds: list[int]
   status: DeletionStatus
   workflowStatus: WorkflowStatus
   additionalData: Any
   componentId: str
   subComponentId: str
   topic: str

class CreateWorkflowInput(GQLObject):
   componentId: str
   subComponentId: str
   componentDisplayName: str
   topic: WorkflowTopic
   workflowStatus: WorkflowStatus
   additionalData: Any

class WorkflowAudit(GQLObject):
   elasticSearchId: ID
   id: int
   topic: str
   requestorId: int
   requestorEmail: str
   requestorDisplayName: str
   requesteeEmail: str
   requesteeDisplayName: str
   requestorContextDisplayName: str
   requesteeContextDisplayName: str
   requesteeId: int
   componentId: str
   subComponentId: str
   additionalData: Any
   workflowStatus: WorkflowStatus
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   componentDisplayName: str

class VirtualPermissionWhereInput(GQLObject):
   permissionLevel: list[RoleLevel]

class RolePermission(GQLObject):
   granted: bool
   readOnly: bool

class UserUpdateInput(GQLObject):
   currentPassword: str
   newPassword: str
   name: str
   company: str
   position: str
   location: str
   bio: str
   imageFile: str
   email: str

class VerifyEmailCodeInput(GQLObject):
   token: str
   verificationCode: str

class UpdateUserInput(GQLObject):
   name: str
   company: str
   position: str
   location: str
   bio: str
   imageFile: str
   email: str

class ProfileInfo(GQLObject):
   id: int
   mashapeId: str
   github: str
   twitter: str
   website: str
   location: str
   linkedin: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   userId: int
   fullname: str
   company: str
   position: str
   description: str
   facebook: str
   quora: str
   stackoverflow: str
   googleplus: str

class UserInvitesReactivateInput(GQLObject):
   emails: list[str]
   orgId: int

class UserInvitesBrandingInput(GQLObject):
   email: str
   id: int
   inviterId: int

class UserInvitesInput(GQLObject):
   email: str
   teamIds: list[int]
   organizationId: int
   role: str
   id: int
   inviterId: int

class InviteUsersSearch(GQLObject):
   id: ID
   username: str
   name: str
   email: str
   thumbnail: str
   isPendingUser: bool
   isOrganizationUser: bool

class UsageByTeam(GQLObject):
   limit: float
   subscriptionId: float
   total: float
   teamId: float

class TeamsUsages(GQLObject):
   usage: int
   id: str

class PhoneVerification(GQLObject):
   id: ID
   userId: ID
   retries: int
   token: str
   code: str
   phoneNumber: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   status: str

class RecoveryCode(GQLObject):
   id: ID
   userId: ID
   code: str
   used: bool
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   status: str

class TutorialWhereInput(GQLObject):
   id: ID
   apiId: ID
   apiVersion: ID
   slugifiedName: str
   authorId: str
   published: bool
   title: str
   content: str
   thumbnailURL: str
   publishedDate: DateTime
   readTime: str
   type: str
   createdAt: DateTime
   updatedAt: DateTime

class TutorialUpdateInput(GQLObject):
   slugifiedName: str
   apiId: ID
   apiVersion: ID
   published: bool
   title: str
   content: str
   thumbnailURL: str
   readTime: str
   type: str

class Tutorial(GQLObject):
   id: ID
   slugifiedName: str
   apiId: ID
   apiVersion: ID
   authorId: str
   published: bool
   title: str
   content: str
   thumbnailURL: str
   publishedDate: DateTime
   readTime: str
   type: TutorialType
   createdAt: DateTime
   updatedAt: DateTime

class TransformationSortingField(GQLObject):
   fieldName: TransformationSortingFieldName
   by: SortingFieldOrder

class TransformationCreateInput(GQLObject):
   apiVersionId: ID
   action: TransformationActionType
   transformationType: TransformationType
   condition: TransformationConditionType
   targetPath: str
   targetMethod: TransformationMethodType
   from_: str
   target: str
   value: str
   valueType: TransformationValueType
   plans: list[ID]
   endpoints: list[ID]

class Transformation(GQLObject):
   id: ID
   apiVersionId: ID
   action: TransformationActionType
   transformationType: TransformationType
   condition: TransformationConditionType
   from_: str
   target: str
   targetPath: str
   targetMethod: TransformationMethodType
   value: str
   valueType: TransformationValueType
   plans: list[ID]
   endpoints: list[ID]
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   status: str

class TransactionsSummaryMonth(GQLObject):
   monthlySubscriptions: float
   overages: float
   date: str

class TransactionsAnalytics(GQLObject):
   total: float
   mrrTotal: float
   overagesTotal: float
   categories: list[str]
   series: Any

class TransactionCharge(GQLObject):
   status: str

class TermsOfService(GQLObject):
   id: ID
   name: str
   text: str
   createdAt: DateTime
   updatedAt: DateTime

class TeamWhereInput(GQLObject):
   slugifiedName: str
   orgId: int

class TeamCreateInput(GQLObject):
   organizationId: int
   name: str
   thumbnail: str
   description: str

class TeamUserWhereInput(GQLObject):
   email: str
   orgId: int

class TeamUserUpdateInput(GQLObject):
   orgId: int
   teamUserId: int
   teamToRemove: int
   teamToAdd: int
   newRole: str

class TargetUrl(GQLObject):
   url: str
   loadBalancingStrategyValue: str

class SubscriptionsCountWhereInput(GQLObject):
   apiId: str
   fromDate: str
   toDate: str
   resolution: Resolution
   isParent: bool

class ExternalGatewaySubscriptionCreateInput(GQLObject):
   apiId: str
   apiVersionId: str

class SubscribeLegalAgreementMetadataInput(GQLObject):
   dsLegalAccountId: str
   dsLegalEnvelopId: str

class usageByBillingItem(GQLObject):
   id: ID
   name: str
   quota: int
   usage: int
   period: str
   usagePercentages: float
   billingCycleStart: DateTime

class SpotlightSortingField(GQLObject):
   fieldName: SpotlightFieldName
   by: SortingFieldOrder

class SpotlightDeleteInput(GQLObject):
   id: ID
   apiId: ID

class SpotlightCreateInput(GQLObject):
   apiId: ID
   type: SpotlightType
   weight: int
   published: bool
   title: str
   description: str
   spotlightURL: str
   file: Upload

class updateBaseUrlInput(GQLObject):
   secretDataId: str
   url: str

class SearchCollectionSortingField(GQLObject):
   fieldName: SearchCollectionSortingFieldName
   by: SortingFieldOrder

class SearchBlogPostWhereInput(GQLObject):
   term: str

class SearchApiSortingField(GQLObject):
   fieldName: SearchApiSortingFieldName
   by: SortingFieldOrder

class SearchApiUser(GQLObject):
   id: int
   thumbnail: str
   name: str
   username: str

class RoleSorting(GQLObject):
   fieldName: RoleSortingFieldName
   by: SortingFieldOrder

class RequestLogsOnProjectFilters(GQLObject):
   apiIds: list[ID]
   endpoints: list[str]
   httpMethods: list[HttpMethod]
   httpStatuses: list[int]
   originIps: list[str]

class RequestLogFilters(GQLObject):
   projectIds: list[str]
   apiIds: list[str]
   userIds: list[ID]
   endpoints: list[str]
   endpointRoutes: list[str]
   httpMethods: list[HttpMethod]
   httpStatuses: list[int]
   originIps: list[str]
   gatewayIds: list[ID]

class deleteProjectAllowedAPIsInput(GQLObject):
   projectAllowedAPIIds: list[int]
   projectId: int
   mashapeId: str

class createProjectAllowedAPIInput(GQLObject):
   projectId: int
   apiId: str
   apiVersionId: str
   mashapeId: str

class ProjectCreateInput(GQLObject):
   projectOwner: ID
   projectName: str
   description: str
   thumbnail: Upload

class DeleteProjectInput(GQLObject):
   projectId: ID
   projectName: str
   mashapeId: ID

class PayoutInfo(GQLObject):
   id: ID
   userId: int
   mashapeId: str
   name: str
   address: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime

class ResetUserPasswordInput(GQLObject):
   password: str
   confirmPassword: str
   token: str

class CorporateDomain(GQLObject):
   domain: str
   ignore: bool

class UsersInvitation(GQLObject):
   id: str
   email: str
   role: str

class BillingAdditionalValues(GQLObject):
   total: int
   subscriptionId: ID

class NotificationMessage(GQLObject):
   title: str
   link: str
   text: str
   thumbnail: str
   user: str

class MarkNewNotificationsAsReadInput(GQLObject):
   notificationId: int
   isRead: bool

class ThreadEntityStatusUpdateInput(GQLObject):
   messageThreadIds: list[int]
   flag: EntityStatusFlag
   value: bool

class Message(GQLObject):
   id: ID
   authorId: int
   title: str
   body: str
   apiId: str
   entityId: int
   ownerId: int
   messageThreadId: int
   ownerDisplayName: str
   entityDisplayName: str
   apiDisplayName: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime

class ThreadEntityStatus(GQLObject):
   id: ID
   entityId: int
   messageThreadId: int
   createdAt: DateTime
   updatedAt: DateTime
   flag: int
   isRead: bool
   isArchived: bool
   isStarred: bool

class MessageThreadsWhereInput(GQLObject):
   apiIds: list[str]
   apiDisplayName: str
   entityDisplayName: str
   entityStatusFlag: EntityStatusFlag
   entityId: ID

class RestrictedLogPayload(GQLObject):
   requestid: ID
   reqparams: Any
   reqheaders: Any
   resheaders: Any
   reqbody: Any
   resbody: Any
   saveRequestQueryParametersLogging: bool
   saveRequestHeadersLogging: bool
   saveResponseHeadersLogging: bool
   saveRequestBodyLogging: bool
   saveResponseBodyLogging: bool

class GetLegalAgreementSigningURLInput(GQLObject):
   entityId: str
   legalDocumentId: str
   legalAccountId: str
   billingPlanId: str

class UpdateLegalAgreementInfo(GQLObject):
   id: ID
   refreshToken: str
   accessToken: str
   vendor: str

class LegalAgreementInfoUrl(GQLObject):
   url: str

class KafkaOffset(GQLObject):
   partition: int
   offset: int

class SchemaRegistryConfiguration(GQLObject):
   url: str
   user: str
   password: str

class SaslConfiguration(GQLObject):
   mechanism: str
   password: str
   username: str

class TopicConfigurationItem(GQLObject):
   configName: str
   configValue: str
   readOnly: bool
   isDefault: bool
   isSensitive: bool

class ProduceMessageResponse(GQLObject):
   topicName: str
   partition: int
   errorCode: int
   baseOffset: str

class KafkaSchemas(GQLObject):
   schemas: list[str]

class IssueFollowInputV2(GQLObject):
   issueId: int

class Announcement(GQLObject):
   id: int
   apiId: str
   providerId: str
   body: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime

class createHeadlines(GQLObject):
   apiId: str
   text: str
   textModified: bool

class UpdateGraphQLSchemaInput(GQLObject):
   source: Upload
   graphQLSchemaId: ID
   endpointId: ID

class GqlDoc(GQLObject):
   docKey: str
   defaultDescription: str
   description: str
   visible: bool

class GatewayConfiguration(GQLObject):
   id: ID
   gatewayDefaultTimeOut: int
   limitRequestSize: int
   allowHttpTraffic: bool
   apiGatewayInstanceId: int

class LogsCSVExports(GQLObject):
   status: int
   statusText: str

class EntityRoleSorting(GQLObject):
   fieldName: EntityRoleSortingFieldName
   by: SortingFieldOrder

class EntityRoleInput(GQLObject):
   id: ID
   entityId: int
   roleId: int
   parentId: int
   orgId: int

class EntityMetadataWhereInput(GQLObject):
   entityId: list[ID]
   attributeName: str
   attributeValue: str

class DuplicateNameCheckInput(GQLObject):
   term: str
   id: int
   actionType: str

class ExternalDocsInput(GQLObject):
   description: str
   url: str

class PayloadObjectInput(GQLObject):
   body: str
   headers: str
   format: str
   id: str
   name: str
   description: str
   status: str
   type: str
   statusCode: int
   examples: Any
   schema: Any
   schemaDefinition: Any

class ResponseObjectInput(GQLObject):
   body: str
   headers: str
   format: str

class payloadParametersForUpdateOrCreateEndpointWithParameters(GQLObject):
   index: int
   id: str
   condition: str
   description: str
   name: str
   paramType: str
   value: str
   querystring: bool
   type: str
   status: str
   options: list[str]
   schema: Any
   schemaDefinition: Any
   examples: Any

class routeParametersArray(GQLObject):
   index: int
   id: str
   condition: str
   description: str
   name: str
   status: str
   paramType: str
   querystring: bool
   value: Any
   options: list[str]
   schema: Any
   schemaDefinition: Any
   examples: Any

class EndpointParams(GQLObject):
   optional: Any
   required: Any
   headers: Any
   constant: Any
   parameters: Any

class ExternalDocs(GQLObject):
   description: str
   url: str

class EndpointAndVersion(GQLObject):
   apiversion: str
   endpointid: str
   endpointHash: str

class Readme(GQLObject):
   text: str
   updatedAt: DateTime

class IssueUpdateInput(GQLObject):
   title: str
   body: str
   issueId: int

class IssueCreateInputV2(GQLObject):
   title: str
   body: str
   apiId: str
   apiVersion: str

class ContextEntity(GQLObject):
   context: Any
   token: str
   privateApisJwt: str

class ConsumersWhereInput(GQLObject):
   apiId: list[ID]
   offset: int
   limit: int
   order: str
   lastActive: list[str]
   userId: list[int]
   sort: str
   usernames: list[str]
   plansFilter: list[str]
   consumersType: ConsumersType

class SubscriptionString(GQLObject):
   status: str

class MultipleValuesQueryFilter(GQLObject):
   operand: str
   value: str

class FollowPair(GQLObject):
   id: int
   follower: int
   followee: int
   status: str
   updatedAt: DateTime
   createdAt: DateTime

class Account(GQLObject):
   id: int
   credentials: str
   projectName: str
   name: str
   domain: str
   thumbnail: str

class CommentUpdateInput(GQLObject):
   body: str
   issueId: int
   commentId: int

class UpdateCollectionsInput(GQLObject):
   collectionId: ID
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   title: str
   apis: list[ID]
   ownerId: int

class CollectionCreateInput(GQLObject):
   title: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: list[ID]
   ownerId: int
   collection_type: str

class CollapsedCollection(GQLObject):
   id: str
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: list[str]

class CollectionsSortingField(GQLObject):
   fieldName: str
   order: SortingFieldOrder

class CategorySortingField(GQLObject):
   fieldName: CategorySortingFieldName
   by: SortingFieldOrder

class DeletedCategory(GQLObject):
   id: ID
   deleted: bool
   reason: str

class Category(GQLObject):
   id: ID
   name: str
   slugifiedName: str
   status: str
   shortDescription: str
   longDescription: str
   thumbnail: str
   pageTitle: str
   weight: int
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime

class BlogPost(GQLObject):
   slugifiedName: str
   title: str
   id: str
   link: str
   readTime: str
   thumbnail: str
   description: str
   image: str
   updatedAt: DateTime

class EnableBillingFeatureInputV2(GQLObject):
   id: str
   billingFeature: str
   note: str
   status: str

class RateLimitInputV2(GQLObject):
   enabled: bool
   unit: int
   unitName: str
   amount: int

class PagingArgsBilling(GQLObject):
   page: int
   limit: int
   orderBy: str
   orderDirection: OrderDirection
   visibility: str

class LocalePrice(GQLObject):
   price: float
   symbol: str

class EditOrganizationInvoiceInput(GQLObject):
   organizationId: int
   freeSeats: int
   isCustomInvoiceBilling: bool

class BillingPlanMetadataUpdateInput(GQLObject):
   billingPlanId: str
   legalDocumentId: str
   legalAccountId: str
   name: str
   visibility: str
   hidden: bool
   recommended: bool
   targetGroup: str
   isStudent: bool
   shouldRequestApproval: bool
   requestApprovalQuestion: str

class BillingLimitInput(GQLObject):
   item: str
   amount: int
   limitType: str
   overagePrice: float
   period: str
   unlimited: bool
   perusagePrice: float
   currency: str

class PlanDeveloperUserInput(GQLObject):
   id: str
   type: str

class BillingItemsWhereInput(GQLObject):
   versionId: str
   apiId: str

class CreateStripeCustomerInput(GQLObject):
   cardToken: str
   fullName: str
   userId: int

class BillingFeatureEndpoint(GQLObject):
   id: str
   endpoint: str
   endpointHash: str
   billingfeature: str
   type: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime

class billingFeatureEndpointArray(GQLObject):
   endpoint: str

class AuthenticationParam(GQLObject):
   id: ID
   name: str
   description: str
   authentication: str

class AuthenticationExtraMetadata(GQLObject):
   pkceEnabled: bool
   codeChallengeMethod: CodeChallengeMethod
   customOAuth2AuthPrefix: str

class geo(GQLObject):
   country: str
   city: str
   region: str
   timezone: str
   ll: list[float]

class params(GQLObject):
   input: Any

class AuditWhereInput(GQLObject):
   searchTerm: str
   from_: int
   orgId: int

class UserAttributesInput(GQLObject):
   type: str
   attributeValue: list[Any]

class AsyncApiConfigurationWhereInput(GQLObject):
   apiVersionId: list[ID]

class AsyncApiConfiguration(GQLObject):
   id: ID
   spec: str

class AssetUpdateInput(GQLObject):
   id: ID
   title: str
   description: str
   visible: bool

class AssetForDownload(GQLObject):
   id: ID
   downloadUrl: str
   filename: str
   title: str
   externalId: str
   fileSizeBytes: float

class Application(GQLObject):
   id: ID
   mashapeId: str
   mashapeAccountId: str
   name: str
   thumbnail: str
   billing: int
   description: str
   mashapeApplicationName: str
   hasLogo: bool
   favorite: bool
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime

class EditApplicationEnviornmentKeyInput(GQLObject):
   applicationEnviornmentId: ID
   mashapeId: str
   keyName: str
   environment: str

class AppAuthorizationUpdateInput(GQLObject):
   id: ID
   name: str

class AppAuthorizationsWhereInput(GQLObject):
   projectId: ID

class ApiWhereInput(GQLObject):
   id: list[ID]
   externalCustomIds: list[ID]
   ownerId: list[ID]
   subscriberId: list[ID]
   visibility: ApiVisibility
   apiSlugifiedName: list[str]
   ownerSlugifiedName: list[str]
   name: list[str]
   isFavorite: bool

class ApiSecurityInfo(GQLObject):
   rapidapiProxySecret: str

class ApiTermsOfServiceInput(GQLObject):
   text: str

class validateSwaggerInput(GQLObject):
   file: Upload

class ApiVersionSecretParameterInput(GQLObject):
   name: str
   value: str
   description: str
   placement: SecretParameterPlacement

class GqlApiVersionCreateInput(GQLObject):
   api: str
   name: str
   visibility: Visibility
   oldApiVersionId: str
   introspectionCallUrl: str
   isIntrospectionCall: bool
   allowHubSchemaRefresh: bool
   gqlFile: Any

class RequestPayload(GQLObject):
   id: str
   name: str
   format: str
   body: str
   description: str
   type: str
   apiversion: str
   createdAt: DateTime
   updatedAt: DateTime
   statusCode: int
   apiendpoint: str
   examples: Any
   schema: Any
   schemaDefinition: Any

class Publicdns(GQLObject):
   address: str
   proxyMode: str
   apiversion: str
   current: bool
   id: ID
   createdAt: DateTime
   updatedAt: DateTime
   status: str

class ApiVersionSortingField(GQLObject):
   fieldName: ApiSortingFieldName
   by: SortingFieldOrder

class CalculatedStatistics(GQLObject):
   requeststotal: float
   requestsmax: int
   requestsmin: int
   requestsavg: float
   requeststps: float
   errorsavg: float
   errorsmedian: float
   errorsmax: float
   errorsmin: float
   errorstotal: int
   latencyavg: float
   latencymedian: float
   latencymax: float
   latencymin: float

class StatsData(GQLObject):
   date: str
   requests: int
   errors: float
   latency: float
   projectId: str
   apiid: str

class ApiSpecImportProcessIssue(GQLObject):
   message: str
   severity: ApiSpecImportProcessIssueSeverity

class ApiUpdateFromRapidOasInput(GQLObject):
   spec: Upload
   apiVersionId: ID

class ApiUpdateFromSpecInput(GQLObject):
   apiVersionId: ID
   spec: Upload
   specType: ApiSpecType

class SearchArguments(GQLObject):
   categoryName: str
   categoryNames: list[str]
   exclude: list[str]
   term: str
   sortBy: str
   size: int
   offset: int
   page: int
   tags: list[Any]
   collectionIds: list[str]
   privateApisJwt: str

class ApiReferenceWhereInput(GQLObject):
   apiVersionId: list[ID]

class RatingInput(GQLObject):
   apiId: str
   rating: int

class ApiQuality(GQLObject):
   apiId: ID
   score: int

class ApiFollowerSortingField(GQLObject):
   fieldName: ApiFollowerSortingFieldName
   by: SortingFieldOrder

class ApiFollowerCreateInput(GQLObject):
   apiId: ID

class CreateApiFavoritesInput(GQLObject):
   apiIds: list[ID]

class ApiDeveloperEntityInput(GQLObject):
   id: ID
   mashapeId: str
   name: str
   type: EntityType

class ApiCertificateWhereInput(GQLObject):
   id: list[ID]
   ownerId: list[ID]

class ApiCertificateSubjectInfo(GQLObject):
   alternativeNames: list[str]
   commonName: str
   countryName: str
   localityName: str
   organizationName: str
   organizationalUnitName: str
   stateOrProvinceName: str
   emailAddress: str

class AnalyticsStatsHttpResponseInput(GQLObject):
   eq: list[int]
   ne: list[int]
   lt: int
   le: int
   gt: int
   ge: int

class AnalyticsStats(GQLObject):
   requests: int
   errors: int
   latency: float
   date: DateTime
   endpointId: ID
   apiId: ID
   endpointHash: ID
   appMashapeId: ID
   apiVersionId: ID

class deleteUserAlertsInput(GQLObject):
   ids: list[ID]

class editUserAlertInput(GQLObject):
   id: ID
   name: str
   description: str
   typeId: int
   condition: Condition
   threshold: float
   timeInterval: time
   timePeriod: int
   channel: Channel
   status: AlertStatus
   throttleInterval: time
   throttlePeriod: int
   apiIds: list[ID]
   projectIds: list[ID]
   baseUrl: str
   minNextAlertTime: DateTime
   endpointsIds: list[ID]
   apiVersionsIds: list[ID]
   billingPlansIds: list[ID]
   endpointHashes: list[ID]

class UserAlert(GQLObject):
   id: ID
   entityId: ID
   name: str
   description: str
   scope: ID
   typeId: int
   condition: Condition
   threshold: float
   timeInterval: time
   timePeriod: int
   channel: Channel
   status: AlertStatus
   throttleInterval: time
   throttlePeriod: int
   apiIds: list[ID]
   projectIds: list[ID]
   endpointsIds: list[ID]
   baseUrl: str
   apiVersionsIds: list[ID]
   billingPlansIds: list[ID]
   minNextAlertTime: DateTime
   endpointHashes: list[ID]
   deletedAt: DateTime
   createdAt: DateTime
   updatedAt: DateTime

class SEOTagAttribute(GQLObject):
   key: str
   value: str

class GatewayTemplateParamsCreateInput(GQLObject):
   paramName: str
   paramValue: str
   paramDescription: str
   codeTemplateId: int

class PartialGatewayTemplateParamCreateInput(GQLObject):
   paramName: str
   paramValue: str
   paramDescription: str

class GatewayConfigurationUpdateInput(GQLObject):
   gatewayDefaultTimeOut: int
   limitRequestSize: int
   allowHttpTraffic: bool

class GatewayConfigurationCreateInput(GQLObject):
   gatewayDefaultTimeOut: int
   limitRequestSize: int
   allowHttpTraffic: bool

class EventUrlUpdateInput(GQLObject):
   url: str

class ExtensionWhereInput(GQLObject):
   isEnabled: bool
   path: str
   isUserLoggedIn: bool
   page: str
   client: str

class EventLogInput(GQLObject):
   query: str

class AdminAuditLogInput(GQLObject):
   query: str

class GatewayTemplateParamsSortingFieldNameSortingField(GQLObject):
   fieldName: GatewayTemplateParamsSortingFieldName
   order: Order

class GatewayTemplateSortingSortingField(GQLObject):
   fieldName: GatewayTemplateSorting
   order: Order

class GatewayInstanceSortingSortingField(GQLObject):
   fieldName: GatewayInstanceSorting
   order: Order

class EventUrlSortablesSortingField(GQLObject):
   fieldName: EventUrlSortables
   order: Order

class PaginationArgs(GQLObject):
   first: int
   last: int
   before: str
   after: str

class EnvConfig(GQLObject):
   id: int
   key: str
   value: str
   isDefaultValue: bool
   type: EnvConfigType
   description: str
   categoryId: int
   label: str
   allowAdminAccess: bool
   isPrivate: bool
   createdAt: DateTime
   updatedAt: DateTime

class ExtensionConsumer(GQLObject):
   id: ID
   extensionId: int
   client: str
   page: str
   order: int
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime

class EventUrl(GQLObject):
   id: ID
   url: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime

class GatewayTemplateParam(GQLObject):
   id: ID
   codeTemplateId: int
   paramName: str
   paramValue: str
   paramDescription: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime

class GatewayCustomMessage(GQLObject):
   id: ID
   apiGatewayInstanceId: int
   messageKey: str
   messageValue: str
   createdAt: DateTime
   updatedAt: DateTime
