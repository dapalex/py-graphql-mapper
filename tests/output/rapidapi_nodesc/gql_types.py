from typing import Generic, Union, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import ID
from pygqlmap.src.arg_builtin import *
from typing import NewType
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

class GetWorkflowCountOptions(GQLObject):
   requestorId: int
   requesteeId: int
   requestorContextId: int
   workflowStatus: WorkflowStatus
   status: str
   componentId: str
   subComponentId: str
   topic: str

class CreateSignupApprovalWorkflowInput(GQLObject):
   topic: SignupApprovalWorkflowTopic
   additionalData: Any

class CanWorkflowBeSubmittedOptions(GQLObject):
   topic: WorkflowTopic
   componentId: str

class Workflow(GQLObject):
   id: ID
   workflowId: int
   topic: str
   requestorId: int
   requestorContextId: int
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
   requesteeContextId: int

class RolePermissionUpdateInput(GQLObject):
   granted: bool
   readOnly: bool

class SearchUsersWhereInput(GQLObject):
   brand: str
   term: str
   offset: int
   limit: int

class UserWhereInput(GQLObject):
   username: str
   includeUserAttributes: bool
   email: str
   userIds: List[ID]
   teamId: ID

class UserPasswordInput(GQLObject):
   currentPassword: str
   newPassword: str

class UserEnrichment(GQLObject):
   name: str
   bio: str
   company: str
   position: str
   location: str
   thumbnail: str
   socialLinks: List[Any]

class SaveUserApi(GQLObject):
   id: ID
   apiId: str
   status: int

class UserInvitesDeleteInput(GQLObject):
   emails: List[str]
   orgId: int

class UserInvitesCreateInput(GQLObject):
   email: str
   teamIds: List[int]
   organizationId: int
   role: str
   id: int
   inviterId: int

class UserInvite(GQLObject):
   id: ID
   token: str
   email: str
   teamId: int
   organizationId: int
   role: str

class FollowInput(GQLObject):
   followerId: int
   followeeId: int

class UsageByOrg(GQLObject):
   quota: float
   usage: float
   billingCycleStart: DateTime
   period: str
   usagePercentages: float

class UsageItem(GQLObject):
   startDate: str
   endDate: str
   usage: int
   overUsageAmount: float
   overChargePrice: float

class Phone(GQLObject):
   id: ID
   userId: ID
   phoneNumber: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   status: str

class TutorialSortingField(GQLObject):
   fieldName: TutorialFieldName
   by: SortingFieldOrder

class TutorialDeleteInput(GQLObject):
   apiId: ID
   apiVersion: ID
   slugifiedName: str

class TutorialCreateInput(GQLObject):
   apiId: ID
   apiVersion: ID
   published: bool
   title: str
   content: str
   thumbnailURL: str
   type: str

class TransformationWhereInput(GQLObject):
   id: List[ID]
   apiVersionId: List[ID]

class TransformationUpdateInput(GQLObject):
   id: ID
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
   plans: List[ID]
   endpoints: List[ID]

class DeletedTransformation(GQLObject):
   id: ID
   deleted: bool

class updateTransactionInput(GQLObject):
   ids: List[ID]
   paidout: bool
   amount: float

class OrgTransaction(GQLObject):
   invoiceLink: str
   createdAt: str
   totalAmount: float

class TransactionsSummaryWhereInput(GQLObject):
   fromDate: str
   toDate: str
   apiIds: List[ID]
   userIds: List[ID]

class TransactionsItem(GQLObject):
   title: str
   sum: float

class Tenant(GQLObject):
   id: ID
   name: str
   domain: str
   slugifiedKey: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   pricingPlanId: int

class TeamUpdateInput(GQLObject):
   id: int
   name: str
   thumbnail: str
   description: str

class EditTeamInput(GQLObject):
   id: int
   name: str
   thumbnail: str
   description: str

class UserRolesUpdateInput(GQLObject):
   entityId: int
   roleId: int
   orgId: int

class TargetUrlUpdateInput(GQLObject):
   url: str
   loadBalancingStrategyValue: str

class TagDefinition(GQLObject):
   id: str
   color: str
   description: str
   status: str
   type: str
   name: str
   values: List[str]
   editableByProvider: bool
   forceEnumValidation: bool
   isVisible: bool
   requiredOnAPI: bool
   showTagName: bool
   createdAt: DateTime
   updatedAt: DateTime

class SubscriptionsCount(GQLObject):
   createdAt: str
   count: int

class SubscribeLegalAgreementMetadataInput(GQLObject):
   dsLegalAccountId: str
   dsLegalEnvelopId: str

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
   apiIds: List[ID]
   endpoints: List[str]
   httpMethods: List[HttpMethod]
   httpStatuses: List[int]
   originIps: List[str]

class RequestLogFilters(GQLObject):
   projectIds: List[str]
   apiIds: List[str]
   userIds: List[ID]
   endpoints: List[str]
   endpointRoutes: List[str]
   httpMethods: List[HttpMethod]
   httpStatuses: List[int]
   originIps: List[str]
   gatewayIds: List[ID]

class deleteProjectAllowedAPIsInput(GQLObject):
   projectAllowedAPIIds: List[int]
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
   messageThreadIds: List[int]
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
   apiIds: List[str]
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

class UpdateLegalAgreementInfo(GQLObject):
   id: ID
   refreshToken: str
   accessToken: str
   vendor: str

class ProduceMessageInput(GQLObject):
   apiVersionId: str
   topicName: str
   key: str
   value: str
   partition: str
   compression: Compression
   headers: Any
   valueSchemaId: int
   keySchemaId: int

class SchemaRegistryConfigurationInput(GQLObject):
   url: str
   user: str
   password: str

class SaslConfigurationInput(GQLObject):
   mechanism: str
   password: str
   username: str

class TopicSchema(GQLObject):
   id: int
   schema: str
   schemaType: SchemaType
   subject: str
   version: int

class TopicOffset(GQLObject):
   partition: int
   offset: str
   high: str
   low: str

class SubscribeKafkaResponse(GQLObject):
   actionsChannel: str
   authKey: str
   messagesChannel: str
   publishKey: str
   subscribeKey: str

class KafkaTopic(GQLObject):
   name: str

class IssueFollow(GQLObject):
   id: int
   follower: int
   followee: int
   mashapeId: str
   mashapeIssueId: str
   createdAt: DateTime
   updatedAt: DateTime
   status: str

class updateHeadlines(GQLObject):
   apiId: str
   apiVersionId: str
   headlineId: str
   text: str
   textModified: bool

class Headline(GQLObject):
   text: str
   id: str
   status: str
   index: int
   title: str
   type: str
   apiversion: str
   textModified: bool
   createdAt: DateTime
   updatedAt: DateTime

class GraphQLSchemaCreateInput(GQLObject):
   id: ID
   endpointId: ID
   schema: Any
   isIntrospectionCall: bool
   allowHubSchemaRefresh: bool
   introspectionCallUrl: str
   status: GRAPH_QL_SCHEMA_STATUS

class Header(GQLObject):
   id: int
   paramName: str
   paramValue: str
   paramDescription: str

class FollowApiInput(GQLObject):
   apiId: str
   userId: str

class LogsCSV(GQLObject):
   id: ID
   requestorId: ID
   requestorUsername: str
   fileName: str
   downloadUrl: str
   filters: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   ttl: DateTime

class EntityRoleWhereInput(GQLObject):
   entityIds: List[int]
   orgId: int
   parentIds: List[int]

class EntityMetadataSortingField(GQLObject):
   fieldName: EntityMetadataSortingFieldName
   by: SortingFieldOrder

class EntityMetadata(GQLObject):
   id: ID
   entityId: ID
   attributeName: str
   attributeValue: str

class EntityAttribute(GQLObject):
   attributeName: str
   attributeValue: str

class EndpointOrder(GQLObject):
   endpointId: str
   groupId: str
   index: int

class MockResponseObjectInput(GQLObject):
   mockResponseStatusCode: int
   body: str
   headers: str
   format: str
   isMockResponse: bool

class endpointData(GQLObject):
   apiversion: str
   code: int
   createdAt: DateTime
   updatedAt: DateTime
   description: str
   group: str
   method: str
   name: str
   pricing: str
   response: str
   route: str
   routeregex: str
   status: str
   thumbail: str
   type: str
   webhook: bool
   payload: str
   displayResponse: bool

class payloadModelForUpdateOrCreateEndpointWithParameters(GQLObject):
   id: str
   body: str
   description: str
   format: str
   name: str
   status: str
   statusCode: ID
   condition: str
   apiendpoint: str
   payloadType: str
   schema: Any
   schemaDefinition: Any
   examples: Any

class headerParametersArray(GQLObject):
   index: int
   id: str
   condition: str
   description: str
   name: str
   status: str
   querystring: bool
   paramType: str
   options: List[str]
   value: Any
   schema: Any
   schemaDefinition: Any
   examples: Any

class EndpointPath(GQLObject):
   description: str
   summary: str
   path: str
   type: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   meta: Any
   status: str

class EndpointWhereInput(GQLObject):
   id: List[ID]

class EndpointStatsData(GQLObject):
   date: str
   requests: int
   errors: int
   latency: float
   endpointid: ID

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
   apiId: List[ID]
   offset: int
   limit: int
   order: str
   lastActive: List[str]
   userId: List[int]
   sort: str
   usernames: List[str]
   plansFilter: List[str]
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
   apis: List[ID]
   ownerId: int

class CollectionCreateInput(GQLObject):
   title: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: List[ID]
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
   apis: List[str]

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

class geo(GQLObject):
   country: str
   city: str
   region: str
   timezone: str
   ll: List[float]

class params(GQLObject):
   input: Any

class AuditWhereInput(GQLObject):
   searchTerm: str
   from_: int
   orgId: int

class UserAttributesInput(GQLObject):
   type: str
   attributeValue: List[Any]

class AsyncApiConfigurationWhereInput(GQLObject):
   apiVersionId: List[ID]

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
   id: List[ID]
   externalCustomIds: List[ID]
   ownerId: List[ID]
   subscriberId: List[ID]
   visibility: ApiVisibility
   apiSlugifiedName: List[str]
   ownerSlugifiedName: List[str]
   name: List[str]
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
   categoryNames: List[str]
   exclude: List[str]
   term: str
   sortBy: str
   size: int
   offset: int
   page: int
   tags: List[Any]
   collectionIds: List[str]
   privateApisJwt: str

class ApiReferenceWhereInput(GQLObject):
   apiVersionId: List[ID]

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
   apiIds: List[ID]

class ApiDeveloperEntityInput(GQLObject):
   id: ID
   mashapeId: str
   name: str
   type: EntityType

class ApiCertificateWhereInput(GQLObject):
   id: List[ID]
   ownerId: List[ID]

class ApiCertificateSubjectInfo(GQLObject):
   alternativeNames: str
   commonName: str
   countryName: str
   localityName: str
   organizationName: str
   organizationalUnitName: str
   stateOrProvinceName: str
   emailAddress: str

class UserAlertsWhereInput(GQLObject):
   scope: ID

class UserAlertUpdateInput(GQLObject):
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
   baseUrl: str
   apiIds: List[ID]
   projectIds: List[ID]
   endpointsIds: List[ID]
   apiVersionsIds: List[ID]
   billingPlansIds: List[ID]
   endpointHashes: List[ID]

class addUserAlertInput(GQLObject):
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
   apiIds: List[ID]
   projectIds: List[ID]
   baseUrl: str
   minNextAlertTime: DateTime
   endpointsIds: List[ID]
   apiVersionsIds: List[ID]
   billingPlansIds: List[ID]
   endpointHashes: List[ID]

class AlertDefinition(GQLObject):
   id: ID
   type: str
   status: AlertStatus
   description: str
   units: str

class EnvConfigUpdateInput(GQLObject):
   id: int
   value: str

class GatewayTemplateParamsUpdateInput(GQLObject):
   paramName: str
   paramValue: str
   paramDescription: str
   id: ID

class GatewayCustomMessageUpdateInput(GQLObject):
   messageKey: MessageKey
   messageValue: str
   id: ID

class GatewayCustomMessageCreateInput(GQLObject):
   messageKey: MessageKey
   messageValue: str

class EventConfigUpdateInput(GQLObject):
   isActive: bool
   shouldGenerateSecret: bool

class EventUrlCreateInput(GQLObject):
   url: str

class EventLogSortablesSortingField(GQLObject):
   fieldName: EventLogSortables
   order: Order

class AdminAuditLogSortablesSortingField(GQLObject):
   fieldName: AdminAuditLogSortables
   order: Order

class EnvConfigTerm(GQLObject):
   key: str
   brand: Brand
   categoryId: int
   hideInAdvancedSettingsUI: bool

class GatewayTemplateParamsWhereInput(GQLObject):
   status: str

class GatewayTemplateWhereInput(GQLObject):
   status: str

class GatewayInstanceWhereInput(GQLObject):
   status: str

class EventUrlWhereInput(GQLObject):
   url: str

class EventLog(GQLObject):
   id: str
   url: str
   eventType: str
   eventData: str
   eventText: str
   statusCode: str
   highlight: List[str]
   createdAt: DateTime

class AuditUser(GQLObject):
   id: int
   email: str
   name: str
   thumbnail: str
   type: str
   mashapeId: str
   slugifiedName: str

class EventType(GQLObject):
   id: ID
   name: str
   label: str
   example: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime

class EnvConfigCategory(GQLObject):
   id: int
   name: str
   createdAt: DateTime
   updatedAt: DateTime

class GatewayConfigurations(GQLObject):
   gatewayDefaultTimeOut: int
   limitRequestSize: int
   allowHttpTraffic: bool

class PageInfo(GQLObject):
   hasNextPage: bool
   hasPreviousPage: bool
   startCursor: str
   endCursor: str

class Stats(GQLObject):
   apiStats: List[StatsData]

class FollowersUser(GQLObject):
   startFollowDate: str
   id: int
   email: str
   username: str
   user: NewType('User', GQLObject) ## Circular Reference for User
   attributes: Any

class KafkaJSConfiguration(GQLObject):
   brokers: str
   clientId: str
   ssl: bool
   sasl: SaslConfiguration

class KafkaConfiguration(GQLObject):
   kafkaConfiguration: KafkaJSConfiguration
   schemaRegistryConfiguration: SchemaRegistryConfiguration
   allowProducingRecords: bool

class Authentication(GQLObject):
   id: ID
   apiVersionId: str
   authType: AuthenticationType
   description: str
   accessTokenUrl: str
   authorizationUrl: str
   requestTokenUrl: str
   grantType: GrantType
   separator: SeparatorType
   clientSecretRequired: bool
   clientAuthentication: ClientAuthenticationType
   authParams: AuthenticationParam
   handleOauthTokenAtFrontend: bool

class ApiVersionAccessControlInfo(GQLObject):
   authentication: Authentication
   secretParameters: SecretParameter

class GraphQLSchema(GQLObject):
   id: ID
   endpointId: ID
   schema: Any
   allowHubSchemaRefresh: bool
   isIntrospectionCall: bool
   status: str
   type: str
   createdAt: DateTime
   updatedAt: DateTime
   documentation: List[GqlDoc]

class VCYYU_GraphQLSchema_Field(GraphQLSchema):
   class GraphQLSchemaArgs(GQLArgsSet, GQLObject): 
      withOverrides: bool

   _args: GraphQLSchemaArgs



class MDCSH_ResponsePayload_Field(ResponsePayload):
   class ResponsePayloadArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: ResponsePayloadArgs



class Endpoint(GQLObject):
   id: ID
   index: int
   apiversion: str
   createdAt: DateTime
   updatedAt: DateTime
   description: str
   group: str
   method: ApiEndpointHttpMethod
   name: str
   route: str
   routeregex: str
   webhook: bool
   params: EndpointParams
   displayResponse: bool
   isGraphQL: bool
   graphQLSchema: VCYYU_GraphQLSchema_Field
   mockResponseId: ID
   isMockResponse: bool
   summary: str
   externalDocs: ExternalDocs
   endpointHash: str
   appliedOauth2Scopes: AuthenticationParam
   requestPayloads: List[RequestPayload]
   responsePayloads: List[ResponsePayload]
   mockResponse: MDCSH_ResponsePayload_Field

class EndpointsGroup(GQLObject):
   id: ID
   name: str
   apiVersionId: ID
   index: int
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   description: str
   externalDocs: ExternalDocs

class AllowedPlanDeveloper(GQLObject):
   id: int
   mashapeId: str
   billingPlanId: str
   user: NewType('Entity', GQLObject) ## Circular Reference for Entity
   userId: int
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime

class ApiVersionBillingPlanVersion(GQLObject):
   id: str
   apiVersionId: str
   billingPlan: NewType('BillingPlan', GQLObject) ## Circular Reference for BillingPlan
   billingPlanId: str
   billingPlanVersion: NewType('BillingPlanVersion', GQLObject) ## Circular Reference for BillingPlanVersion
   billingPlanVersionId: str
   showInMarketplace: bool
   allowBillingVersionForApiVersion: bool
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   status: str

class BillingItemEndpoint(GQLObject):
   id: str
   endpoint: str
   endpointHash: str
   apiEndpoint: Endpoint
   bulk: bool
   billingitem: str
   type: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime

class UsageData(GQLObject):
   period: str
   requests: int
   billingItemId: ID
   subscriptionId: ID
   billingItem: NewType('BillingItem', GQLObject) ## Circular Reference for BillingItem

class QATZD_BillingItemEndpoint_Field(BillingItemEndpoint):
   class BillingItemEndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingItemEndpointArgs



class IJNUC_UsageData_Field(UsageData):
   class UsageDataArgs(GQLArgsSet, GQLObject): 
      subscriptionId: NonNull_ID
      fromDate: str
      toDate: str
      resolution: UsageResolution
      orderDir: OrderDirection

   _args: UsageDataArgs



class BillingItem(GQLObject):
   id: str
   name: str
   title: str
   description: str
   apiversion: str
   type: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   billingitemendpoints: QATZD_BillingItemEndpoint_Field
   allEndpoints: bool
   usageInSubscription: IJNUC_UsageData_Field

class BillingLimit(GQLObject):
   id: str
   period: str
   amount: int
   currency: str
   unlimited: bool
   overageprice: float
   overageLocalePrice: OverageLocalePrice
   item: str
   limitType: str
   billingplanversion: str
   type: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   billingitem: BillingItem

class BillingFeature(GQLObject):
   id: ID
   name: str
   slugifiedName: str
   description: str
   apiVersionId: ID
   status: BillingFeatureStatus
   createdAt: DateTime
   updatedAt: DateTime
   billingFeatureEndpoints: Endpoint

class EnableBillingFeature(GQLObject):
   id: str
   billingfeature: str
   billingFeatureObject: BillingFeature
   billingplanversion: str
   type: str
   status: str
   note: str
   createdAt: DateTime
   updatedAt: DateTime

class SubscriptionUsage(GQLObject):
   mostUsagePercentage: float
   topPercentageLimitedUsage: float
   usageByBillingItem: List[usageByBillingItem]
   pricing: str

class UsagePeriodGrouper(GQLObject):
   period: str
   calculated: List[UsageItem]

class Usage(GQLObject):
   quotaId: ID
   quota: int
   title: str
   overChargePrice: float
   period: str
   calculated: List[UsageItem]

class Usages(GQLObject):
   usage: List[Usage]
   version: str
   startDate: str
   endDate: str

class Transaction(GQLObject):
   id: int
   stripId: str
   subscriptionId: str
   totalAmount: float
   additionalAmount: float
   refunded: int
   paid: int
   payoutAmount: float
   periodStart: str
   periodEnd: str
   invoiceLink: str
   refundDate: str
   refundedAmount: float
   mashapeId: str
   status: str
   updatedAt: str
   createdAt: str
   deletedAt: str
   userId: int
   apiId: str
   paidout: str
   chargeId: str
   disputed: int
   subscription: NewType('BillingSubscription', GQLObject) ## Circular Reference for BillingSubscription
   entity: NewType('Entity', GQLObject) ## Circular Reference for Entity
   usages: Usages
   Charge: TransactionCharge
   stripeId: str
   invoicePeriodStart: str
   invoicePeriodEnd: str

class SMRWX_UsagePeriodGrouper_Field(UsagePeriodGrouper):
   class UsagePeriodGrouperArgs(GQLArgsSet, GQLObject): 
      billingItemIds: List[NonNull_ID]
      fromDate: str
      toDate: str
      resolution: UsageResolution
      orderDir: OrderDirection

   _args: UsagePeriodGrouperArgs



class BillingSubscription(GQLObject):
   subscriptionUsage: SubscriptionUsage
   id: int
   userId: int
   apiId: str
   stripeId: str
   billingPlanVersionId: str
   canceled: int
   autocanceled: bool
   type: str
   isInternal: bool
   mashapeId: str
   status: str
   apiVersionId: str
   customToken: str
   canceledAt: DateTime
   createdAt: DateTime
   deletedAt: DateTime
   updatedAt: DateTime
   apiVersion: NewType('ApiVersion', GQLObject) ## Circular Reference for ApiVersion
   api: NewType('Api', GQLObject) ## Circular Reference for Api
   user: NewType('User', GQLObject) ## Circular Reference for User
   billingPlanVersion: NewType('BillingPlanVersion', GQLObject) ## Circular Reference for BillingPlanVersion
   usageByBillingItem: SMRWX_UsagePeriodGrouper_Field
   usages: SubscriptionUsage
   parentId: int
   teamsSubscriptions: List[NewType('BillingSubscription', GQLObject)] ## Circular Reference for BillingSubscription
   entity: NewType('Entity', GQLObject) ## Circular Reference for Entity
   transactions: List[Transaction]

class QQLJN_ApiVersionBillingPlanVersion_Field(ApiVersionBillingPlanVersion):
   class ApiVersionBillingPlanVersionArgs(GQLArgsSet, GQLObject): 
      apiVersionId: str
      filters: BillingPlanVersionFilters

   _args: ApiVersionBillingPlanVersionArgs



class UEFUB_BillingLimit_Field(BillingLimit):
   class BillingLimitArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingLimitArgs



class BillingPlanVersion(GQLObject):
   id: str
   name: str
   current: bool
   period: str
   visibility: str
   option: str
   price: float
   localePrice: LocalePrice
   pricing: str
   billingplan: str
   billingPlan: NewType('BillingPlan', GQLObject) ## Circular Reference for BillingPlan
   type: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   apiVersionBillingPlanVersion: QQLJN_ApiVersionBillingPlanVersion_Field
   billinglimits: UEFUB_BillingLimit_Field
   enablebillingfeatures: List[EnableBillingFeature]
   rateLimit: RateLimit
   subscriptions: List[BillingSubscription]
   subscriptionsCount: int

class TargetGroup(GQLObject):
   id: ID
   apiId: ID
   loadBalancingStrategy: LoadBalancingStrategy
   name: str
   targetUrls: TargetUrl

class GVEAZ_BillingPlanVersion_Field(BillingPlanVersion):
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject): 
      id: str
      showDeleted: bool

   _args: BillingPlanVersionArgs



class BillingPlan(GQLObject):
   id: str
   apiversion: str
   name: str
   slugifiedName: str
   status: str
   type: str
   visibility: Visibility
   hidden: bool
   recommended: bool
   createdAt: DateTime
   updatedAt: DateTime
   allowedPlanDevelopers: List[AllowedPlanDeveloper]
   allowedPlanDevelopersCount: int
   legalDocumentId: str
   legalAccountId: str
   isStudent: bool
   version: GVEAZ_BillingPlanVersion_Field
   targetGroup: TargetGroup
   targetGroupId: str
   shouldRequestApproval: bool
   requestApprovalQuestion: str

class ApiCertificate(GQLObject):
   id: ID
   ownerId: ID
   alias: str
   effectiveDate: DateTime
   expiry: DateTime
   createdAt: DateTime
   updatedAt: DateTime
   serialNumber: str
   signatureAlgorithm: str
   publicKeySignatureAlgorithm: ApiCertificatePublicKeySignatureAlgorithm
   publicKeySizeInBits: int
   publicKeyExponent: int
   certificateDataAsPem: str
   issuer: ApiCertificateIssuerInfo
   subject: ApiCertificateSubjectInfo
   associations: NewType('ApiCertificateAssociation', GQLObject) ## Circular Reference for ApiCertificateAssociation
   associatedApiVersionsCount: int

class ApiCertificateAssociation(GQLObject):
   apiCertificateId: ID
   apiVersionId: ID
   createdAt: DateTime
   apiCertificate: ApiCertificate
   apiVersion: NewType('ApiVersion', GQLObject) ## Circular Reference for ApiVersion

class ApiSchema(GQLObject):
   identifier: str
   apiVersion: NewType('ApiVersion', GQLObject) ## Circular Reference for ApiVersion
   definition: Any
   index: int

class SecretData(GQLObject):
   id: ID
   apiversion: ID

class QSXVL_ResponsePayload_Field(ResponsePayload):
   class ResponsePayloadArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: ResponsePayloadArgs



class FIWQG_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointArgs



class OMJXF_EndpointsGroup_Field(EndpointsGroup):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointsGroupArgs



class WBBVZ_Publicdns_Field(Publicdns):
   class PublicdnsArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: PublicdnsArgs



class CPXFO_BillingPlan_Field(BillingPlan):
   class BillingPlanArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      showDeleted: bool
      visibility: Visibility

   _args: BillingPlanArgs



class UOCWW_BillingItem_Field(BillingItem):
   class BillingItemArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingItemArgs



class XQLSY_BillingItemEndpoint_Field(BillingItemEndpoint):
   class BillingItemEndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingItemEndpointArgs



class PQYXM_Asset_Field(Asset):
   class AssetArgs(GQLArgsSet, GQLObject): 
      visible: bool

   _args: AssetArgs



class ApiVersion(GQLObject):
   id: ID
   api: str
   current: bool
   name: str
   status: str
   keywords: List[str]
   createdAt: DateTime
   updatedAt: DateTime
   visibility: str
   apiInstance: NewType('Api', GQLObject) ## Circular Reference for Api
   kafkaConfiguration: KafkaConfiguration
   asyncApiConfiguration: AsyncApiConfiguration
   webhooks: bool
   payloads: QSXVL_ResponsePayload_Field
   accessControl: ApiVersionAccessControlInfo
   endpoints: FIWQG_Endpoint_Field
   groups: OMJXF_EndpointsGroup_Field
   publicdns: WBBVZ_Publicdns_Field
   billingplans: CPXFO_BillingPlan_Field
   billingitems: UOCWW_BillingItem_Field
   billingitemendpoints: XQLSY_BillingItemEndpoint_Field
   publicBillingPlanVersions: List[ApiVersionBillingPlanVersion]
   targetGroup: TargetGroup
   targetGroupId: str
   transformations: List[Transformation]
   versionStatus: VersionStatus
   apiSubType: apiSubTypeEnum
   associatedApiCertificates: ApiCertificateAssociation
   assets: PQYXM_Asset_Field
   apiSchemas: ApiSchema

class FollowApi(GQLObject):
   id: str
   follower: str
   api: str
   status: str
   apiData: NewType('Api', GQLObject) ## Circular Reference for Api
   user: NewType('User', GQLObject) ## Circular Reference for User

class Comment(GQLObject):
   id: int
   issueId: int
   userId: int
   body: str
   top: bool
   rating: int
   mashapeId: str
   mashapeAccountId: str
   mashapeIssueId: str
   index: int
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   user: NewType('User', GQLObject) ## Circular Reference for User

class QFUDS_Comment_Field(Comment):
   class CommentArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: CommentArgs



class ZUQGY_Comment_Field(Comment):
   class CommentArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: CommentArgs



class Issue(GQLObject):
   id: int
   userId: int
   topicId: str
   title: str
   body: str
   rating: int
   commentsCount: int
   mashapeId: str
   visibility: str
   index: int
   mashapeAccountId: str
   closed: bool
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   comments: QFUDS_Comment_Field
   commentsV2: ZUQGY_Comment_Field
   user: NewType('User', GQLObject) ## Circular Reference for User
   api: NewType('Api', GQLObject) ## Circular Reference for Api

class Spotlight(GQLObject):
   id: ID
   type: SpotlightType
   apiId: ID
   spotlightURL: str
   status: str
   slugifiedName: str
   thumbnailURL: str
   title: str
   description: str
   weight: int
   published: bool
   updatedAt: DateTime
   createdAt: DateTime

class ApiDeveloper(GQLObject):
   id: ID
   developer: ID
   api: ID
   type: EntityType
   status: ApiDeveloperStatus
   blocked: bool
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   user: NewType('Entity', GQLObject) ## Circular Reference for Entity

class OFDKL_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      showDeleted: bool

   _args: EndpointArgs



class RequestLog(GQLObject):
   requestId: ID
   projectId: ID
   api: str
   apiId: ID
   endpoint: str
   endpointObject: OFDKL_Endpoint_Field
   endpointId: str
   httpMethod: HttpMethod
   period: int
   apiLatency: int
   callTime: DateTime
   displayCallTime: DateTime
   originIp: str
   originCountry: str
   engineError: int
   httpStatus: int
   reqHeadersSize: int
   resHeadersSize: int
   reqBodySize: int
   resBodySize: int
   project: NewType('Project', GQLObject) ## Circular Reference for Project
   version: ApiVersion

class RequestLogsResult(GQLObject):
   requests: List[RequestLog]
   totalCount: int

class NOTYC_Issue_Field(Issue):
   class IssueArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: IssueArgs



class KQLWK_Announcement_Field(Announcement):
   class AnnouncementArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: AnnouncementArgs



class YTVYX_ApiDeveloper_Field(ApiDeveloper):
   class ApiDeveloperArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: ApiDeveloperArgs



class FJXUC_Headline_Field(Headline):
   class HeadlineArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: HeadlineArgs



class HLRTR_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointArgs



class UIAZV_BillingFeature_Field(BillingFeature):
   class BillingFeatureArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingFeatureArgs



class YJNBL_BillingItem_Field(BillingItem):
   class BillingItemArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingItemArgs



class ZBECM_BillingPlan_Field(BillingPlan):
   class BillingPlanArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingPlanArgs



class BKCTN_RequestLogsResult_Field(RequestLogsResult):
   class RequestLogsResultArgs(GQLArgsSet, GQLObject): 
      fromDate: NonNull_str
      toDate: str
      limit: int
      offset: int
      orderBy: RequestLogsOrderBy
      orderDir: OrderDirection
      filters: RequestLogsOnApiFilters

   _args: RequestLogsResultArgs



class Api(GQLObject):
   id: str
   externalCustomId: ID
   name: str
   installsAllTime: int
   requestTimeout: int
   requestSizeLimit: int
   installsDaily: int
   installsMonthly: int
   installsWeekly: int
   pricing: ApiPricing
   apiType: ApiType
   currentVersion: ApiVersion
   category: str
   createdAt: str
   updatedAt: str
   ownerId: int
   proxy: bool
   status: ApiStatus
   description: str
   longDescription: str
   tags: APITag
   thumbnail: str
   thumbnailSmall: str
   websiteUrl: str
   termsOfService: TermsOfService
   visibility: ApiVisibility
   owner: NewType('Entity', GQLObject) ## Circular Reference for Entity
   score: Score
   followers: List[FollowApi]
   followersCount: int
   subscriptionsCount: int
   issues: NOTYC_Issue_Field
   rating: apiRating
   slugifiedName: str
   categoryId: str
   allowedContext: List[str]
   spotlights: List[Spotlight]
   patternMatch: bool
   patternMatchAllowOtherTypes: bool
   requestSchemaValidation: bool
   requestSchemaValidationUnknownAttributePolicy: SchemaValidationUnknownAttributePolicy
   gatewayIds: ID
   announcements: KQLWK_Announcement_Field
   apiDevelopers: YTVYX_ApiDeveloper_Field
   targetGroups: List[TargetGroup]
   publishApiPendingRequest: bool
   saveRequestHeadersLogging: bool
   saveRequestQueryParametersLogging: bool
   saveRequestBodyLogging: bool
   saveResponseHeadersLogging: bool
   saveResponseBodyLogging: bool
   useHttpProxy: bool
   security: ApiSecurityInfo
   versions: List[ApiVersion]
   headlines: FJXUC_Headline_Field
   endpoints: HLRTR_Endpoint_Field
   billingFeatures: UIAZV_BillingFeature_Field
   billingItems: YJNBL_BillingItem_Field
   billingPlans: ZBECM_BillingPlan_Field
   isFavorite: bool
   quality: ApiQuality
   requestLogs: BKCTN_RequestLogsResult_Field

class ProjectAllowedAPI(GQLObject):
   id: int
   projectId: int
   apiId: str
   api: Api
   apiVersionId: str
   apiVersion: ApiVersion
   createdAt: DateTime
   updatedAt: DateTime
   status: str

class VLKAT_ProjectAllowedAPI_Field(ProjectAllowedAPI):
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: ProjectAllowedAPIArgs



class MVBBL_RequestLogsResult_Field(RequestLogsResult):
   class RequestLogsResultArgs(GQLArgsSet, GQLObject): 
      fromDate: NonNull_str
      toDate: str
      limit: int
      offset: int
      orderBy: RequestLogsOrderBy
      orderDir: OrderDirection
      filters: RequestLogsOnProjectFilters

   _args: RequestLogsResultArgs



class Project(GQLObject):
   id: int
   mashapeId: str
   name: str
   description: str
   thumbnail: str
   favorite: bool
   accounts: List[Account]
   xMashapeKey: str
   acl: NewType('ProjectInfo', GQLObject) ## Circular Reference for ProjectInfo
   enableLimitsToAPIs: bool
   projectAllowedAPIs: VLKAT_ProjectAllowedAPI_Field
   requestLogs: MVBBL_RequestLogsResult_Field

class ProjectInfo(GQLObject):
   id: int
   owner: int
   project: int
   user: NewType('User', GQLObject) ## Circular Reference for User
   entity: NewType('Entity', GQLObject) ## Circular Reference for Entity
   Project: Project

class SubscriptionsPaging(GQLObject):
   subscriptions: List[BillingSubscription]
   totalCount: int

class TransactionsPaging(GQLObject):
   transactions: List[Transaction]
   totalCount: int

class TransactionsGraphData(GQLObject):
   prev: TransactionsItem
   curr: TransactionsItem
   overages: TransactionsItem

class UserAttributes(GQLObject):
   count: int
   rows: List[UserAttributesRow]

class EnvelopeTemplate(GQLObject):
   documents: List[EnvelopeDocument]
   templateId: str
   uri: str
   created: DateTime
   name: str
   description: str

class Template(GQLObject):
   envelopeTemplates: List[EnvelopeTemplate]

class DocuSignAccount(GQLObject):
   id: str
   name: str
   baseUri: str
   template: Template

class DocuSignUserInfo(GQLObject):
   name: str
   email: str
   accounts: List[DocuSignAccount]

class DocuSign(GQLObject):
   docuSignUserInfo: DocuSignUserInfo

class LegalAgreementInfo(GQLObject):
   id: ID
   entityId: int
   isLoggedIn: bool
   vendor: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   docuSign: DocuSign

class IXRAP_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      isStripeId: bool
      getAllSubscriptions: bool

   _args: BillingSubscriptionArgs



class YMHMW_SubscriptionsPaging_Field(SubscriptionsPaging):
   class SubscriptionsPagingArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      isStripeId: bool
      getAllSubscriptions: bool

   _args: SubscriptionsPagingArgs



class ZXTGC_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_ID

   _args: BillingSubscriptionArgs



class XYYTA_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_ID
      billingPlanVersionId: ID

   _args: BillingSubscriptionArgs



class QueryFilter(GQLObject):
   columnName: str
   operand: str
   value: Any
   values: List[MultipleValuesQueryFilter]

class QueryFilters(GQLObject):
   filters: List[QueryFilter]

class CEZPH_TransactionsPaging_Field(TransactionsPaging):
   class TransactionsPagingArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      apiNameFilter: str
      queryFilters: QueryFilters

   _args: TransactionsPagingArgs



class KVFKN_TransactionsPaging_Field(TransactionsPaging):
   class TransactionsPagingArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      apiNameFilter: str
      queryFilters: QueryFilters

   _args: TransactionsPagingArgs



class QHUJE_Transaction_Field(Transaction):
   class TransactionArgs(GQLArgsSet, GQLObject): 
      id: ID
      mashapeId: ID

   _args: TransactionArgs



NonNull_DateTime = DateTime

class MPOCV_Stats_Field(Stats):
   class StatsArgs(GQLArgsSet, GQLObject): 
      apiId: ID
      fromDate: NonNull_DateTime
      toDate: DateTime
      resolution: Resolution
      groupBy: StatsGroupBy

   _args: StatsArgs



class Entity(GQLObject):
   id: str
   mashapeId: str
   thumbnail: str
   name: str
   email: str
   username: str
   location: str
   company: str
   position: str
   slugifiedName: str
   type: str
   createdAt: DateTime
   numOfApisUsed: int
   numOfProjects: int
   followsList: List[NewType('FollowUser', GQLObject)] ## Circular Reference for FollowUser
   numOfSubscriptions: int
   projectAcls: List[ProjectInfo]
   subscriptions: IXRAP_BillingSubscription_Field
   subscriptionsPaging: YMHMW_SubscriptionsPaging_Field
   activeSubscriptionByApiId: ZXTGC_BillingSubscription_Field
   activeSubscriptionByApiIdAndBillingPlanVersionId: XYYTA_BillingSubscription_Field
   pagedTransactions: CEZPH_TransactionsPaging_Field
   notFullyRefundedTransactions: KVFKN_TransactionsPaging_Field
   transactionsGraphData: TransactionsGraphData
   transaction: QHUJE_Transaction_Field
   parents: List[NewType('Entity', GQLObject)] ## Circular Reference for Entity
   stats: MPOCV_Stats_Field
   billingInformation: BillingInformation
   bio: str
   publishedApisList: List[Api]
   apis: List[Api]
   attributes: UserAttributes
   userEnrichment: UserEnrichment
   legalAgreementInfo: LegalAgreementInfo
   payoutInfo: PayoutInfo

class FollowUser(GQLObject):
   startFollowDate: str
   id: int
   email: str
   username: str
   user: Entity
   attributes: Any

class ApiFollower(GQLObject):
   id: ID
   followerId: ID
   apiId: ID
   createdAt: DateTime
   api: Api
   follower: NewType('User', GQLObject) ## Circular Reference for User

class Notification(GQLObject):
   id: int
   userId: int
   type: int
   text: str
   message: NotificationMessage
   messageType: str
   read: bool
   createdAt: DateTime
   updatedAt: DateTime

class ProjectAcl(GQLObject):
   id: int
   owner: int
   project: int
   createdAt: DateTime
   updatedAt: DateTime
   Project: Project

class TeamUser(GQLObject):
   id: int
   name: str
   username: str
   thumbnail: str
   email: str
   inviteStatus: str
   teams: List[NewType('Team', GQLObject)] ## Circular Reference for Team
   role: str
   token: str
   userData: NewType('User', GQLObject) ## Circular Reference for User
   teamsCount: int

class IssueObject(GQLObject):
   data: List[Issue]
   total: int

class HNMSH_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      isStripeId: bool

   _args: BillingSubscriptionArgs



class KUKWK_FollowersUser_Field(FollowersUser):
   class FollowersUserArgs(GQLArgsSet, GQLObject): 
      includeUserAttributes: bool

   _args: FollowersUserArgs



class MFNQS_IssueObject_Field(IssueObject):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: IssueObjectArgs



class Team(GQLObject):
   id: ID
   mashapeId: str
   thumbnail: str
   name: str
   slugifiedName: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   status: str
   users: List[TeamUser]
   ProjectAcls: List[ProjectAcl]
   usersCount: int
   description: str
   subscriptions: HNMSH_BillingSubscription_Field
   followersList: KUKWK_FollowersUser_Field
   publishedApisList: List[Api]
   isTeamMember: bool
   issues: MFNQS_IssueObject_Field

class BRNGT_FollowersUser_Field(FollowersUser):
   class FollowersUserArgs(GQLArgsSet, GQLObject): 
      includeUserAttributes: bool

   _args: FollowersUserArgs



class QUIMZ_IssueObject_Field(IssueObject):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: IssueObjectArgs



class Organization(GQLObject):
   id: ID
   email: str
   name: str
   thumbnail: str
   slugifiedName: str
   status: str
   billingInformation: BillingInformation
   description: str
   teams: List[Team]
   publishedApisList: List[Api]
   users: List[NewType('User', GQLObject)] ## Circular Reference for User
   followersList: BRNGT_FollowersUser_Field
   isOrganizationAdmin: bool
   apisCount: int
   internalSubscriptionsCount: int
   externalSubscriptionsCount: int
   issues: QUIMZ_IssueObject_Field
   billingAdditionalValues: BillingAdditionalValues
   payoutInfo: PayoutInfo
   balance: float
   occupiedSeats: int
   entity: Any
   seatsBillingInformation: SeatsBillingInformation
   billingType: str

class OEBXE_Stats_Field(Stats):
   class StatsArgs(GQLArgsSet, GQLObject): 
      fromDate: NonNull_str
      toDate: NonNull_str
      resolution: str
      projectId: str
      apiId: str
      groupBy: StatsGroupBy
      filters: List[StatsFilterBy]
      timeOffset: int

   _args: StatsArgs



class DDVNI_FollowersUser_Field(FollowersUser):
   class FollowersUserArgs(GQLArgsSet, GQLObject): 
      includeUserAttributes: bool

   _args: FollowersUserArgs



class QZADF_FollowUser_Field(FollowUser):
   class FollowUserArgs(GQLArgsSet, GQLObject): 
      includeUserAttributes: bool

   _args: FollowUserArgs



class NSAIN_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      isStripeId: bool

   _args: BillingSubscriptionArgs



class CSKJN_SubscriptionsPaging_Field(SubscriptionsPaging):
   class SubscriptionsPagingArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      isStripeId: bool

   _args: SubscriptionsPagingArgs



class VCHNY_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_ID

   _args: BillingSubscriptionArgs



class FLJKY_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_ID
      billingPlanVersionId: ID

   _args: BillingSubscriptionArgs



class MHFZN_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      projectId: ID
      mashapeId: ID

   _args: ProjectArgs



class XTVGL_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      projectIds: List[NonNull_ID]
      mashapeIds: List[NonNull_ID]

   _args: ProjectArgs



class ZLRSR_ProjectInfo_Field(ProjectInfo):
   class ProjectInfoArgs(GQLArgsSet, GQLObject): 
      projectId: NonNull_ID

   _args: ProjectInfoArgs



class ZVEAC_Transaction_Field(Transaction):
   class TransactionArgs(GQLArgsSet, GQLObject): 
      id: ID
      mashapeId: ID

   _args: TransactionArgs



class User(GQLObject):
   id: str
   email: str
   gmail: str
   githubUsername: str
   facebookUsername: str
   rememberMe: str
   followers: int
   company: str
   position: str
   location: str
   lastActive: DateTime
   thumbnail: str
   name: str
   username: str
   packages: int
   discussions: int
   lastActivePublic: bool
   emailPublic: bool
   githubUrl: str
   githubUrlPublic: bool
   mashapeId: str
   status: str
   origin_site: str
   rakutenToken: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   stats: OEBXE_Stats_Field
   apisCount: int
   followersList: DDVNI_FollowersUser_Field
   followsList: QZADF_FollowUser_Field
   followedApis: List[ApiFollower]
   followsIssues: List[IssueFollow]
   followsIssuesV2: List[IssueFollow]
   subscriptions: NSAIN_BillingSubscription_Field
   subscriptionsPaging: CSKJN_SubscriptionsPaging_Field
   activeSubscriptionByApiId: VCHNY_BillingSubscription_Field
   activeSubscriptionByApiIdAndBillingPlanVersionId: FLJKY_BillingSubscription_Field
   notifications: List[Notification]
   numOfApisUsed: int
   numOfProjects: int
   numOfSubscriptions: int
   billingInformation: BillingInformation
   allowedPlanDevelopers: List[AllowedPlanDeveloper]
   payoutInfo: PayoutInfo
   project: MHFZN_Project_Field
   projects: XTVGL_Project_Field
   projectACL: ZLRSR_ProjectInfo_Field
   ProjectACLs: List[ProjectInfo]
   ProfileInfo: ProfileInfo
   transactionsGraphData: TransactionsGraphData
   transaction: ZVEAC_Transaction_Field
   ProjectAcls: List[ProjectAcl]
   publishedApisList: List[Api]
   bio: str
   Teams: List[Team]
   organizations: List[Organization]
   attributes: UserAttributes
   isCurrentUser: bool
   balance: float
   entity: Any
   userEnrichment: UserEnrichment
   corporateDomain: CorporateDomain
   organizationsWithTheSameDomain: List[CorporateDomainOrganization]
   billingType: str
   isUserCreatedBySSO: bool

class OrgSubscriptionUsage(GQLObject):
   id: ID
   name: str
   byOrg: UsageByOrg
   byTeam: List[UsageByTeam]

class TutorialEdge(GQLObject):
   node: Tutorial
   cursor: str

class TutorialConnection(GQLObject):
   nodes: List[Tutorial]
   edges: List[TutorialEdge]
   pageInfo: PageInfo

class TransformationEdge(GQLObject):
   node: Transformation
   cursor: str

class TransformationConnection(GQLObject):
   nodes: Transformation
   edges: TransformationEdge
   pageInfo: PageInfo

class TransactionsWhereInput(GQLObject):
   userId: ID
   apiIds: List[ID]
   apiOwnerIds: List[ID]
   withCharges: bool
   queryFilters: QueryFilters
   pagingArgs: PagingArgs

class TransactionEdge(GQLObject):
   node: Transaction
   cursor: str

class TransactionConnection(GQLObject):
   nodes: List[Transaction]
   edges: List[TransactionEdge]
   pageInfo: PageInfo
   totalCount: int

class TagDefinitionEdge(GQLObject):
   node: TagDefinition
   cursor: str

class TagDefinitionConnection(GQLObject):
   nodes: List[TagDefinition]
   edges: List[TagDefinitionEdge]
   pageInfo: PageInfo

class BillingSubscriptionEdge(GQLObject):
   node: BillingSubscription
   cursor: str

class SubscriptionConnection(GQLObject):
   nodes: List[BillingSubscription]
   edges: List[BillingSubscriptionEdge]
   pageInfo: PageInfo
   totalCount: int

class SpotlightEdge(GQLObject):
   node: Spotlight
   cursor: str

class SpotlightConnection(GQLObject):
   nodes: List[Spotlight]
   edges: List[SpotlightEdge]
   pageInfo: PageInfo

class WLCHC_Api_Field(Api):
   class ApiArgs(GQLArgsSet, GQLObject): 
      weightLowerThan: int

   _args: ApiArgs



class SearchCollection(GQLObject):
   id: str
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: WLCHC_Api_Field
   blogPostId: str
   post: BlogPost
   blogPosts: List[BlogPosts]
   orderCollectionItems: List[str]
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   ownerId: int
   orgId: str
   orgName: str
   collection_type: str

class SearchConnectionEdge(GQLObject):
   node: SearchCollection
   cursor: str

class SearchCollectionConnection(GQLObject):
   nodes: List[SearchCollection]
   edges: List[SearchConnectionEdge]
   pageInfo: PageInfo
   total: int

class SearchBlogPostEdge(GQLObject):
   node: SearchBlogPost
   cursor: str

class SearchBlogPostConnection(GQLObject):
   nodes: List[SearchBlogPost]
   edges: List[SearchBlogPostEdge]
   pageInfo: PageInfo
   total: int

class YVLDU_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointArgs



class UBSQO_EndpointsGroup_Field(EndpointsGroup):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointsGroupArgs



class SearchApiVersion(GQLObject):
   id: ID
   api: str
   description: str
   longDescription: str
   name: str
   pricing: str
   status: str
   keywords: List[str]
   thumbnail: str
   thumbnailSmall: str
   type: str
   createdAt: DateTime
   updatedAt: DateTime
   visibility: str
   webhooks: bool
   websiteUrl: str
   endpoints: YVLDU_Endpoint_Field
   tags: List[APITag]
   groups: UBSQO_EndpointsGroup_Field
   authentication: Authentication

class SearchApi(GQLObject):
   id: str
   apiType: str
   name: str
   title: str
   description: str
   keywords: List[str]
   installsAllTime: int
   installsDaily: int
   thumbnail: str
   thumbnailSmall: str
   rating: int
   categoryName: str
   User: SearchApiUser
   Ratings: List[int]
   key: str
   longDescription: str
   visibility: str
   score: Score
   pricing: str
   version: SearchApiVersion
   createdAt: DateTime
   updatedAt: DateTime
   slugifiedName: str
   objectID: str
   locale: Locale
   tags: APITag

class SearchApiEdge(GQLObject):
   node: SearchApi
   cursor: str

class SearchApiConnection(GQLObject):
   nodes: List[SearchApi]
   edges: List[SearchApiEdge]
   pageInfo: PageInfo
   total: int
   took: int

class VirtualPermission(GQLObject):
   id: ID
   key: str
   displayName: str
   permissionLevel: str
   description: str
   dependsOn: int
   rolePermission: RolePermission

class Role(GQLObject):
   id: ID
   key: str
   name: str
   description: str
   roleLevel: str
   isBasicRole: bool
   isDefault: bool
   permissions: VirtualPermission

class RoleEdge(GQLObject):
   node: Role
   cursor: str

class RoleConnection(GQLObject):
   nodes: List[Role]
   edges: List[RoleEdge]
   pageInfo: PageInfo

class MessageThread(GQLObject):
   id: ID
   apiId: str
   ownerId: int
   entityId: int
   ownerDisplayName: str
   entityDisplayName: str
   apiDisplayName: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   messages: List[Message]
   lastMessage: Message
   api: Api
   entity: Entity
   threadEntityStatus: ThreadEntityStatus
   body: str

class MessageThreadsObject(GQLObject):
   threads: List[MessageThread]
   messages: List[Message]

class KafkaJSConfigurationInput(GQLObject):
   brokers: List[str]
   clientId: str
   ssl: bool
   sasl: SaslConfigurationInput

class UpdateKafkaConfigurationInput(GQLObject):
   kafkaConfiguration: KafkaJSConfigurationInput
   schemaRegistryConfiguration: SchemaRegistryConfigurationInput
   allowProducingRecords: bool
   apiVersionId: str

class TopicSchemaPair(GQLObject):
   key: TopicSchema
   value: TopicSchema

class TopicMetadataResponse(GQLObject):
   topicOffsets: TopicOffset
   topicConfiguration: TopicConfigurationItem
   schemas: TopicSchemaPair

class GatewayTemplate(GQLObject):
   id: int
   name: str
   description: str
   urlPattern: str
   status: str
   type: str
   headers: List[Header]

class Gateway(GQLObject):
   id: int
   apiGatewayCodeTemplateId: int
   version: str
   dns: str
   type: str
   serviceStatus: str
   status: str
   lastActive: str
   gatewayTemplate: GatewayTemplate
   configurations: GatewayConfiguration
   isDefault: bool

class GatewayEdge(GQLObject):
   node: Gateway
   cursor: str

class GatewayConnection(GQLObject):
   nodes: List[Gateway]
   edges: List[GatewayEdge]
   pageInfo: PageInfo

class EntityRole(GQLObject):
   id: ID
   entityId: int
   roleId: int
   parentId: int
   orgId: int
   role: Role

class EntityRoleEdge(GQLObject):
   node: EntityRole
   cursor: str

class EntityRoleConnection(GQLObject):
   nodes: List[EntityRole]
   edges: List[EntityRoleEdge]
   pageInfo: PageInfo

class parametersForUpdateOrCreateEndpointWithParameters(GQLObject):
   header: List[headerParametersArray]
   route: List[routeParametersArray]

class updateOrCreateEndpointWithParameters(GQLObject):
   apiVersionId: str
   endpointId: str
   description: str
   method: str
   name: str
   params: parametersForUpdateOrCreateEndpointWithParameters
   patternMatch: bool
   payloadModel: payloadModelForUpdateOrCreateEndpointWithParameters
   payloadParameters: List[payloadParametersForUpdateOrCreateEndpointWithParameters]
   route: str
   routeregex: str
   displayResponse: bool
   response: str
   responseObject: ResponseObjectInput
   mockResponseId: ID
   mockResponseObject: MockResponseObjectInput
   responsePayloads: List[PayloadObjectInput]
   requestPayloads: List[PayloadObjectInput]
   group: str
   isGraphQL: bool
   graphQLSchemaObject: GraphQLSchemaCreateInput
   externalDocs: ExternalDocsInput

class EndpointStatsV2(GQLObject):
   endpoint: Endpoint
   stats: List[EndpointStatsData]
   apiData: Api

class EndpointStats(GQLObject):
   endpointid: ID
   name: GNQEQ_name_Field
   stats: List[EndpointStatsData]
   apiData: Api

class Discussion(GQLObject):
   id: int
   userId: int
   topicId: str
   title: str
   body: str
   rating: int
   commentsCount: int
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   visibility: str
   api: Api
   user: User
   type: str

class Consumer(GQLObject):
   id: ID
   userId: ID
   subscriptionId: ID
   subscriptionObjectId: ID
   billingPlanVersionId: ID
   username: str
   name: str
   dateSubscribed: DateTime
   createdAt: DateTime
   plan: str
   planPeriod: str
   planPrice: float
   planVersion: BillingPlanVersion
   usages: SubscriptionUsage
   quotaId: ID
   lastActive: str
   limit: int
   total: float
   subscription: SubscriptionString
   transactions: List[str]
   blocked: bool
   apiId: ID
   requests: int
   entity: Entity
   api: Api
   apiVersionId: ID
   billingItems: List[BillingItem]

class ConsumerEdge(GQLObject):
   node: Consumer
   cursor: str

class ConsumerConnection(GQLObject):
   nodes: Consumer
   edges: List[ConsumerEdge]
   pageInfo: PageInfo
   count: int

class ConsumersRow(GQLObject):
   id: ID
   userId: ID
   subscriptionId: ID
   subscriptionObjectId: ID
   billingPlanVersionId: ID
   username: str
   name: str
   dateSubscribed: DateTime
   createdAt: DateTime
   plan: str
   planPeriod: str
   planPrice: float
   planVersion: BillingPlanVersion
   usages: SubscriptionUsage
   quotaId: ID
   lastActive: str
   limit: int
   total: float
   subscription: SubscriptionString
   transactions: List[str]
   blocked: bool
   apiId: ID
   requests: int
   entity: Entity
   api: Api
   apiVersionId: ID
   billingItems: List[BillingItem]

class CollectionItem(GQLObject): 
   pass

class LASWH_CollectionItem_Field(CollectionItem):
   class CollectionItemArgs(GQLArgsSet, GQLObject): 
      apisSkip: int
      apisLimit: int

   _args: CollectionItemArgs



class CollectionV3(GQLObject):
   id: str
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: LASWH_CollectionItem_Field
   blogPostId: str
   post: BlogPost
   blogPosts: List[BlogPosts]
   orderCollectionItems: List[str]
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   ownerId: int
   orgId: str
   orgName: str
   collection_type: str

class FODCW_CollectionItem_Field(CollectionItem):
   class CollectionItemArgs(GQLArgsSet, GQLObject): 
      weightLowerThan: int

   _args: CollectionItemArgs



class CollectionV2(GQLObject):
   id: str
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: FODCW_CollectionItem_Field
   blogPostId: str
   post: BlogPost
   blogPosts: List[BlogPosts]
   orderCollectionItems: List[str]
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   ownerId: int
   orgId: str
   orgName: str
   collection_type: str

class ZMIJY_Api_Field(Api):
   class ApiArgs(GQLArgsSet, GQLObject): 
      weightLowerThan: int

   _args: ApiArgs



class Collection(GQLObject):
   id: str
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: ZMIJY_Api_Field
   blogPostId: str
   post: BlogPost
   blogPosts: List[BlogPosts]
   orderCollectionItems: List[str]
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   ownerId: int
   orgId: str
   orgName: str
   collection_type: str

class CategoryEdge(GQLObject):
   node: Category
   cursor: str

class CategoryConnection(GQLObject):
   nodes: Category
   edges: CategoryEdge
   pageInfo: PageInfo

class BillingPlanVersionEdge(GQLObject):
   node: BillingPlanVersion
   cursor: str

class BillingPlanVersionConnection(GQLObject):
   nodes: List[BillingPlanVersion]
   edges: List[BillingPlanVersionEdge]
   pageInfo: PageInfo

class upsertBillingPlanVersionInput(GQLObject):
   billingPlanVersionId: str
   showInMarketplace: bool
   price: float
   planType: str
   rateLimit: RateLimitInputV2
   billingLimits: List[BillingLimitInputV2]
   enableBillingFeatures: List[EnableBillingFeatureInputV2]

class upsertBillingPlanAndVersionInput(GQLObject):
   apiId: str
   apiName: str
   apiVersionId: str
   apiVersionName: str
   providerName: str
   upsertBillingPlanInput: upsertBillingPlanInput
   upsertBillingPlanVersionInput: upsertBillingPlanVersionInput

class BillingPlanExtendedUpdateInput(GQLObject):
   billingPlanId: str
   api: str
   apiName: str
   apiVersion: str
   apiVersionName: str
   providerName: str
   name: str
   targetGroup: str
   isPrivatePlan: bool
   isStudent: bool
   legalDocumentId: str
   legalAccountId: str
   shouldRequestApproval: bool
   requestApprovalQuestion: str
   price: float
   type: BillingPlanType
   rateLimit: RateLimitInput
   enableBillingFeatures: List[EnableBillingFeatureInput]
   billingLimits: List[BillingLimitInput]

class BillingPlanCreateInput(GQLObject):
   api: str
   apiName: str
   apiVersion: str
   apiVersionName: str
   providerName: str
   name: str
   targetGroup: str
   isPrivatePlan: bool
   isStudent: bool
   legalDocumentId: str
   legalAccountId: str
   shouldRequestApproval: bool
   requestApprovalQuestion: str
   price: float
   type: BillingPlanType
   rateLimit: RateLimitInput
   enableBillingFeatures: List[EnableBillingFeatureInput]
   billingLimits: List[BillingLimitInput]

class BillingItemEdge(GQLObject):
   node: BillingItem
   cursor: str

class BillingItemConnection(GQLObject):
   nodes: List[BillingItem]
   edges: List[BillingItemEdge]
   pageInfo: PageInfo

class audit(GQLObject):
   id: str
   time: DateTime
   actorRole: str
   action: str
   eventName: str
   user: AuditUser
   activeEntity: activeEntity
   params: params
   attributes: attributes
   geo: geo

class ApiUpdateInput(GQLObject):
   id: ID
   ownerId: ID
   category: str
   visibility: ApiVisibility
   termsOfService: ApiTermsOfServiceInput
   description: str
   longDescription: str
   websiteUrl: str
   thumbnail: Upload
   tags: List[ApiTagValueInput]
   gatewayIds: List[ID]
   useHttpProxy: bool
   requestTimeout: int
   requestSizeLimit: int
   saveRequestHeadersLogging: bool
   saveRequestQueryParametersLogging: bool
   saveRequestBodyLogging: bool
   saveResponseHeadersLogging: bool
   saveResponseBodyLogging: bool
   requestSchemaValidation: bool
   requestSchemaValidationUnknownAttributePolicy: SchemaValidationUnknownAttributePolicy
   patternMatch: bool
   patternMatchAllowOtherTypes: bool

class ApiEdge(GQLObject):
   node: Api
   cursor: str

class ApiConnection(GQLObject):
   nodes: Api
   edges: ApiEdge
   pageInfo: PageInfo
   totalCount: int

class ApiVersionAccessControlUpdateInput(GQLObject):
   secretParameters: List[ApiVersionSecretParameterInput]

class ApiVersionUpdateInput(GQLObject):
   current: bool
   versionStatus: str
   visibility: Visibility
   apiVersionId: str
   accessControl: ApiVersionAccessControlUpdateInput
   associatedCertificates: List[ApiCertificateAssociationTarget]

class ApiVersionEdge(GQLObject):
   node: ApiVersion
   cursor: str

class ApiVersionConnection(GQLObject):
   nodes: List[ApiVersion]
   edges: List[ApiVersionEdge]
   pageInfo: PageInfo

class JYGBR_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointArgs



class OETXW_EndpointsGroup_Field(EndpointsGroup):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointsGroupArgs



class ApiVersionSearch(GQLObject):
   id: ID
   api: str
   description: str
   longDescription: str
   name: str
   pricing: str
   status: str
   keywords: List[str]
   thumbnail: str
   thumbnailSmall: str
   type: str
   createdAt: DateTime
   updatedAt: DateTime
   visibility: str
   webhooks: bool
   websiteUrl: str
   endpoints: JYGBR_Endpoint_Field
   groups: OETXW_EndpointsGroup_Field
   authentication: Authentication

class ApiSearch(GQLObject):
   id: str
   apiType: str
   name: str
   title: str
   description: str
   keywords: List[str]
   installsAllTime: int
   installsDaily: int
   thumbnail: str
   thumbnailSmall: str
   rating: int
   categoryName: str
   User: ApiSearchUser
   Ratings: List[int]
   key: str
   longDescription: str
   visibility: str
   score: Score
   pricing: str
   version: ApiVersionSearch
   createdAt: DateTime
   updatedAt: DateTime
   slugifiedName: str
   objectID: str
   tags: APITag

class ReferenceSpotlight(GQLObject):
   id: ID
   url: str
   title: str
   description: str
   thumbnailUrl: str
   display: bool
   weight: int
   apis: List[Api]

class ApiReference(GQLObject):
   id: ID
   image: str
   videoId: ID
   headline: str
   features: List[Feature]
   spotlights: List[ReferenceSpotlight]

class ApiFollowerEdge(GQLObject):
   node: ApiFollower
   cursor: str

class ApiFollowerConnection(GQLObject):
   nodes: ApiFollower
   edges: ApiFollowerEdge
   pageInfo: PageInfo

class ApiCertificateEdge(GQLObject):
   node: ApiCertificate
   cursor: str

class ApiCertificateConnection(GQLObject):
   nodes: ApiCertificate
   edges: ApiCertificateEdge
   pageInfo: PageInfo

class UserAlertEdge(GQLObject):
   node: UserAlert
   cursor: str

class UserAlertsConnection(GQLObject):
   nodes: UserAlert
   edges: List[UserAlertEdge]
   pageInfo: PageInfo

class GatewayInstanceUpdateInput(GQLObject):
   id: ID
   apiGatewayCodeTemplateId: int
   dns: str
   configurations: GatewayConfigurationUpdateInput
   customMessages: List[GatewayCustomMessageUpdateInput]
   isDefault: bool

class GatewayInstanceCreateInput(GQLObject):
   apiGatewayCodeTemplateId: int
   dns: str
   type: GatewayType
   configurations: GatewayConfigurationCreateInput
   customMessages: List[GatewayCustomMessageCreateInput]
   isDefault: bool

class EventLogEdge(GQLObject):
   cursor: str
   node: EventLog

class EventLogConnection(GQLObject):
   edges: List[EventLogEdge]
   nodes: List[EventLog]
   totalCount: int
   pageInfo: PageInfo

class AdminAuditLog(GQLObject):
   id: str
   action: str
   eventName: str
   user: AuditUser
   auditText: str
   statusCode: str
   highlight: List[str]
   createdAt: DateTime

class AdminAuditLogEdge(GQLObject):
   cursor: str
   node: AdminAuditLog

class AdminAuditLogConnection(GQLObject):
   edges: List[AdminAuditLogEdge]
   nodes: List[AdminAuditLog]
   totalCount: int
   pageInfo: PageInfo

class EventConfig(GQLObject):
   id: ID
   isActive: bool
   secret: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   urls: EventUrl
   types: EventType

class EventUrlEdge(GQLObject):
   cursor: str
   node: EventUrl

class EventUrlConnection(GQLObject):
   edges: List[EventUrlEdge]
   nodes: List[EventUrl]
   totalCount: int
   pageInfo: PageInfo

class GatewayTemplateParamEdge(GQLObject):
   cursor: str
   node: GatewayTemplateParam

class GatewayTemplateParamConnection(GQLObject):
   edges: List[GatewayTemplateParamEdge]
   nodes: List[GatewayTemplateParam]
   totalCount: int
   pageInfo: PageInfo

class GwTemplate(GQLObject):
   id: ID
   name: str
   description: str
   urlPattern: str
   status: str
   isCanBeDeleted: bool
   createdAt: DateTime
   updatedAt: DateTime
   templateParams: List[GatewayTemplateParam]

class GatewayInstance(GQLObject):
   id: ID
   apiGatewayCodeTemplateId: int
   dns: str
   type: str
   deploymentKey: str
   serviceStatus: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   isDefault: bool
   isCanBeEdited: bool
   template: GwTemplate
   configurations: GatewayConfigurations
   customMessages: List[GatewayCustomMessage]

class GatewayInstanceEdge(GQLObject):
   cursor: str
   node: GatewayInstance

class GatewayInstanceConnection(GQLObject):
   edges: List[GatewayInstanceEdge]
   nodes: List[GatewayInstance]
   totalCount: int
   pageInfo: PageInfo

class GwTemplateEdge(GQLObject):
   cursor: str
   node: GwTemplate

class GatewayTemplateConnection(GQLObject):
   edges: List[GwTemplateEdge]
   nodes: List[GwTemplate]
   totalCount: int
   pageInfo: PageInfo

class Extension(GQLObject):
   id: ID
   name: str
   description: str
   title: str
   url: str
   sourceUrl: str
   sourceType: str
   slugifiedKey: str
   isEnabled: bool
   loggedInRequired: bool
   path: str
   extensionConsumers: ExtensionConsumer
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   topic: str
   order: int

class EventUrlSortablesInput(GQLObject):
   sortingFields: List[EventUrlSortablesSortingField]

class GatewayInstanceSortingInput(GQLObject):
   sortingFields: List[GatewayInstanceSortingSortingField]

class GatewayTemplateSortingInput(GQLObject):
   sortingFields: List[GatewayTemplateSortingSortingField]

class GatewayTemplateParamSortingInput(GQLObject):
   sortingFields: List[GatewayTemplateParamsSortingFieldNameSortingField]

class AdminAuditLogSortablesInput(GQLObject):
   sortingFields: List[AdminAuditLogSortablesSortingField]

class EventLogSortablesInput(GQLObject):
   sortingFields: List[EventLogSortablesSortingField]

class GatewayTemplateCreateInput(GQLObject):
   name: str
   description: str
   urlPattern: str
   headers: List[PartialGatewayTemplateParamCreateInput]

class GatewayTemplateUpdateInput(GQLObject):
   name: str
   description: str
   urlPattern: str
   id: ID
   headers: List[GatewayTemplateParamsUpdateInput]

class SEOTag(GQLObject):
   tag: str
   innerBody: str
   attributes: List[SEOTagAttribute]

class SEO(GQLObject):
   id: str
   url: str
   description: str
   brand: str
   lang: str
   tags: List[SEOTag]

class ApiCertificateCreationResult(GQLObject):
   apiCertificate: ApiCertificate
   isExpired: bool

class ApiCertificateOrderByInput(GQLObject):
   sortingFields: List[ApiCertificateSortingField]

class ApiDeveloperInput(GQLObject):
   id: ID
   developer: ID
   status: ApiDeveloperStatus
   user: ApiDeveloperEntityInput

class SaveApiDevelopersInput(GQLObject):
   apiId: ID
   developers: List[ApiDeveloperInput]

class ApiFollowerOrderByInput(GQLObject):
   fields: List[ApiFollowerSortingField]

class ApiReferenceConnection(GQLObject):
   nodes: List[ApiReference]

class ApiSearchPaged(GQLObject):
   results: List[ApiSearch]
   total: int

class ApiSpecImportResult(GQLObject):
   apiId: ID
   trackingId: ID
   warnings: ApiSpecImportWarning

class ApiSpecImportProcess(GQLObject):
   trackingId: ID
   apiId: ID
   progress: float
   hasError: bool
   issues: ApiSpecImportProcessIssue

class ApiVersionOrderByInput(GQLObject):
   sortingFields: List[ApiVersionSortingField]

class ApiOrderByInput(GQLObject):
   sortingFields: List[ApiSortingField]

class SchemaDefinitionSourceInput(GQLObject):
   type: GqlSchemaSourceType
   source: str
   options: GqlOptions

class GqlSpecInput(GQLObject):
   baseUrl: str
   schemaSource: SchemaDefinitionSourceInput

class SpecInput(GQLObject):
   gql: GqlSpecInput

class NewApiVersionInput(GQLObject):
   name: str
   spec: SpecInput

class ApiCreateInput(GQLObject):
   name: str
   description: str
   category: str
   externalCustomId: str
   pricing: ApiPricing
   visibility: ApiVisibility
   apiType: ApiType
   version: NewApiVersionInput

class ApplicationAuthorization(GQLObject):
   id: ID
   name: str
   mashapeId: ID
   key: str
   applicationId: ID
   status: AppAuthorizationStatus
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   authorizationType: AppAuthorizationType
   authorizationValues: str
   gateways: Gateway
   grantType: AuthorizationGrantType

class ApplicationEnvironment(GQLObject):
   id: ID
   keyName: str
   mashapeId: str
   applicationEnvironmentName: EnvironmentName
   internalKey: str
   key: str
   applicationId: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   resetDate: int
   authorizationType: AuthorizationType
   authorizationValues: str
   gateways: List[Gateway]
   grantType: AuthorizationGrantType

class ApplicationEnvironmentPaging(GQLObject):
   applicationEnvironments: List[ApplicationEnvironment]
   totalCount: int

class AsyncApiConfigurationConnection(GQLObject):
   nodes: List[AsyncApiConfiguration]

class auditTrails(GQLObject):
   total: int
   audits: List[audit]

class authStrategy(GQLObject):
   id: int
   brand: str
   type: int
   txtColor: str
   title: str
   icon: str
   color: str
   customButton: Any
   authStrategy: authStrategyType

class authenticationInput(GQLObject):
   authType: AuthenticationType
   description: str
   accessTokenUrl: str
   authorizationUrl: str
   oauthTokenUrl: str
   requestTokenUrl: str
   grantType: GrantType
   separator: SeparatorType
   legs: int
   clientAuthentication: ClientAuthenticationType
   clientSecretRequired: bool
   authParams: List[AuthenticationParamInput]
   handleOauthTokenAtFrontend: bool

class createAuthenticationInput(GQLObject):
   apiVersionId: str
   authentication: authenticationInput

class AuthenticationCreateOrUpdateResult(GQLObject):
   id: ID
   authParams: List[AuthenticationParam]

class AuthenticationCreateInput(GQLObject):
   apiVersionId: ID
   authType: AuthenticationType
   description: str
   accessTokenUrl: str
   authorizationUrl: str
   requestTokenUrl: str
   grantType: GrantType
   separator: SeparatorType
   clientAuthentication: ClientAuthenticationType
   clientSecretRequired: bool
   authParams: List[AuthenticationParamInput]
   handleOauthTokenAtFrontend: bool

class AuthenticationUpdateInput(GQLObject):
   apiVersionId: ID
   authType: AuthenticationType
   description: str
   accessTokenUrl: str
   authorizationUrl: str
   requestTokenUrl: str
   grantType: GrantType
   separator: SeparatorType
   clientAuthentication: ClientAuthenticationType
   clientSecretRequired: bool
   authParams: List[AuthenticationParamInput]
   handleOauthTokenAtFrontend: bool

class createBillingFeature(GQLObject):
   apiVersionId: str
   name: str
   description: str
   billingFeatureEndpoints: List[billingFeatureEndpointArray]

class updateBillingFeature(GQLObject):
   name: str
   description: str
   billingFeatureId: str
   apiVersionId: str
   billingFeatureEndpoints: List[billingFeatureEndpointArray]

class BillingItemUpsertInput(GQLObject):
   apiId: str
   apiVersionId: str
   billingItem: upsertBillingItem

class AllowedPlanDevelopersInput(GQLObject):
   id: str
   status: str
   user: PlanDeveloperUserInput

class AllowedPlanDevelopersUpdateInput(GQLObject):
   allowedPlanDevelopers: List[AllowedPlanDevelopersInput]
   planId: str
   apiId: str
   apiVersionId: str

class BillingPlanVersionsResponse(GQLObject):
   data: List[BillingPlanVersion]
   totalCount: int

class BillingPlanVersionWhereInput(GQLObject):
   apiId: ID
   apiVersionId: ID
   filters: BillingPlanVersionFilters

class CategoryCreateInput(GQLObject):
   information: List[CategoryTextualDataInput]
   thumbnail: str
   pageTitle: str
   weight: int

class CategoryUpdateInput(GQLObject):
   id: ID
   information: List[CategoryTextualDataInput]
   thumbnail: str
   pageTitle: str
   weight: int

class CategoryOrderByInput(GQLObject):
   fields: List[CategorySortingField]

class CollectionsOrderByInput(GQLObject):
   sortingFields: List[CollectionsSortingField]

class CollectionsResponse(GQLObject):
   data: List[Collection]
   total: int

class PaginatedComments(GQLObject):
   data: List[Comment]
   total: int

class EntityMetadataInput(GQLObject):
   entityId: ID
   entityAttributes: List[EntityAttribute]

class Consumers(GQLObject):
   count: int
   rows: List[ConsumersRow]

class Country(GQLObject):
   code: str
   currency: Currency

class DiscussionObject(GQLObject):
   data: List[Discussion]
   total: int

class VersionEndpointStats(GQLObject):
   apiVersionId: ID
   apiVersionName: str
   endpointsStats: List[EndpointStatsV2]

class endpointsWithinDateInput(GQLObject):
   projectId: ID
   apiIds: List[ID]
   endpointIds: List[ID]
   fromDate: DateTime
   toDate: DateTime
   resolution: str
   filters: List[StatsFilterBy]
   timeOffset: int

class EndpointConnection(GQLObject):
   nodes: Endpoint

class updateEndpointEntity(GQLObject):
   apiId: str
   versionId: str
   endpointId: str
   newData: endpointData
   lang: str

class EndpointsGroupCreateInput(GQLObject):
   name: str
   apiVersionId: ID
   index: int
   description: str
   externalDocs: ExternalDocsInput

class EndpointsGroupUpdateInput(GQLObject):
   id: ID
   name: str
   index: int
   description: str
   externalDocs: ExternalDocsInput

class EntityMetadataConnection(GQLObject):
   nodes: EntityMetadata

class EntityMetadataOrderByInput(GQLObject):
   fields: List[EntityMetadataSortingField]

class EntityRoleCreateInput(GQLObject):
   entitiesRoles: List[EntityRoleInput]

class EntityRoleOrderByInput(GQLObject):
   sortingFields: List[EntityRoleSorting]

class ApiGatewayConfiguration(GQLObject):
   id: ID
   apiGatewayInstanceId: ID
   configurations: GatewayConfiguration

class KafkaTopics(GQLObject):
   topics: KafkaTopic
   allowProducingRecords: bool

class SubscribeOptions(GQLObject):
   customOffset: KafkaOffset
   fromBeginning: bool
   timestamp: str

class MessageCreateInput(GQLObject):
   messageType: MessageType
   message: MessageInput

class CreateNewOrganizationInputV4(GQLObject):
   name: str
   email: str
   seats: int
   thumbnail: str
   description: str
   cardToken: str
   recaptcha: str
   users: List[UsersInvitation]
   purchasing_power: str
   numofdevs: str
   apis: List[ID]

class OrganizationCreateInput(GQLObject):
   name: str
   email: str
   seats: int
   thumbnail: str
   description: str
   cardToken: str
   recaptcha: str
   users: List[UsersInvitation]
   purchasing_power: str
   numofdevs: str
   apis: List[ID]

class changeApiUsedVersionInput(GQLObject):
   newProjectAllowedApiInput: createProjectAllowedAPIInput
   currentProjectAllowedApiId: int

class VirtualPermissionUpdateInput(GQLObject):
   id: ID
   key: str
   displayName: str
   permissionLevel: str
   description: str
   dependsOn: int
   rolePermission: RolePermissionUpdateInput

class RoleCreateInput(GQLObject):
   name: str
   description: str
   roleLevel: RoleLevel
   isBasicRole: bool
   isDefault: bool
   permissions: List[VirtualPermissionUpdateInput]

class RoleUpdateInput(GQLObject):
   id: ID
   key: str
   name: str
   description: str
   roleLevel: str
   isBasicRole: bool
   isDefault: bool
   permissions: List[VirtualPermissionUpdateInput]

class RoleOrderByInput(GQLObject):
   sortingFields: List[RoleSorting]

class SearchApiOrderByInput(GQLObject):
   sortingFields: List[SearchApiSortingField]

class SearchCollectionOrderByInput(GQLObject):
   sortingFields: List[SearchCollectionSortingField]

class SpotlightOrderByInput(GQLObject):
   sortingFields: List[SpotlightSortingField]

class SubscribeInput(GQLObject):
   apiId: str
   billingPlanVersionId: str
   apiVersionId: str
   ownerId: str
   legalAgreementMetadata: SubscribeLegalAgreementMetadataInput

class OrgSubscriptions(GQLObject):
   rows: List[BillingSubscription]
   count: int

class SubscriptionsWhereInput(GQLObject):
   userId: int
   activeOnly: bool
   id: int
   apiId: str
   mashapeId: str
   pagingArgs: PagingArgs

class SubscriptionCreateInput(GQLObject):
   apiId: str
   billingPlanVersionId: str
   ownerId: str
   apiVersionId: str
   legalAgreementMetadata: SubscribeLegalAgreementMetadataInput

class TargetGroupUpdateInput(GQLObject):
   id: ID
   loadBalancingStrategy: LoadBalancingStrategy
   targetUrls: List[TargetUrlUpdateInput]

class PaginatedTeamUsers(GQLObject):
   data: TeamUser
   total: int
   totalActive: int

class TransactionsSummary(GQLObject):
   totalAmount: float
   transactionsByMonths: List[TransactionsSummaryMonth]

class TransformationOrderByInput(GQLObject):
   fields: List[TransformationSortingField]

class TutorialOrderByInput(GQLObject):
   sortingFields: List[TutorialSortingField]

class UsagesStats(GQLObject):
   usage: int
   period: str
   parentUsage: int
   teamsUsages: List[TeamsUsages]

class OrganizationApiUsagesV2(GQLObject):
   usages: List[OrgSubscriptionUsage]

class UserSavedApi(GQLObject):
   id: ID
   userId: int
   apiId: str
   status: int
   api: Api

class Permission(GQLObject):
   id: ID
   key: str
   displayName: str
   permissionLevel: str
   description: str
   dependsOn: int
   rolePermission: RolePermission

class WorkFlowsResponse(GQLObject):
   data: List[Workflow]
   total: int

class GetWorkflowsOptions(GQLObject):
   topic: WorkflowTopic
   requesteeId: int
   requestorId: int
   componentId: str
   subComponentId: str
   componentDisplayName: str
   workflowStatus: List[WorkflowStatus]
   pagingArgs: PagingArgs

class WorkFlowAuditsResponse(GQLObject):
   data: List[WorkflowAudit]
   total: int
