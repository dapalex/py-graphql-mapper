from typing import Generic, Union
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import ID
from pygqlmap.src.arg_builtin import *
from typing import NewType
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .circular_refs import *

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
   topic: WorkflowTopic ##NON NULL
   componentId: str ##NON NULL

class Workflow(GQLObject):
   id: ID ##NON NULL
   workflowId: int
   topic: str ##NON NULL
   requestorId: int ##NON NULL
   requestorContextId: int ##NON NULL
   requestorEmail: str ##NON NULL
   requestorDisplayName: str ##NON NULL
   requesteeEmail: str
   requesteeDisplayName: str
   requestorContextDisplayName: str
   requesteeContextDisplayName: str
   requesteeId: int ##NON NULL
   componentId: str ##NON NULL
   subComponentId: str
   additionalData: Any
   workflowStatus: WorkflowStatus ##NON NULL
   status: str ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL
   deletedAt: DateTime
   componentDisplayName: str
   requesteeContextId: int

class RolePermissionUpdateInput(GQLObject):
   granted: bool ##NON NULL
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
   userIds: ID ##NON NULL ##LIST
   teamId: ID

class UserPasswordInput(GQLObject):
   currentPassword: str ##NON NULL
   newPassword: str ##NON NULL

class UserEnrichment(GQLObject):
   name: str
   bio: str
   company: str
   position: str
   location: str
   thumbnail: str
   socialLinks: Any ##LIST

class SaveUserApi(GQLObject):
   id: ID
   apiId: str ##NON NULL
   status: int ##NON NULL

class UserInvitesDeleteInput(GQLObject):
   emails: str ##NON NULL ##LIST
   orgId: int ##NON NULL

class UserInvitesCreateInput(GQLObject):
   email: str
   teamIds: int ##NON NULL ##LIST
   organizationId: int ##NON NULL
   role: str
   id: int
   inviterId: int

class UserInvite(GQLObject):
   id: ID ##NON NULL
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
   fieldName: TutorialFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class TutorialDeleteInput(GQLObject):
   apiId: ID ##NON NULL
   apiVersion: ID ##NON NULL
   slugifiedName: str ##NON NULL

class TutorialCreateInput(GQLObject):
   apiId: ID ##NON NULL
   apiVersion: ID ##NON NULL
   published: bool ##NON NULL
   title: str ##NON NULL
   content: str ##NON NULL
   thumbnailURL: str
   type: str

class TransformationWhereInput(GQLObject):
   id: ID ##NON NULL ##LIST
   apiVersionId: ID ##NON NULL ##LIST

class TransformationUpdateInput(GQLObject):
   id: ID ##NON NULL
   apiVersionId: ID
   action: TransformationActionType ##NON NULL
   transformationType: TransformationType ##NON NULL
   condition: TransformationConditionType
   targetPath: str
   targetMethod: TransformationMethodType
   from_: str
   target: str
   value: str
   valueType: TransformationValueType
   plans: ID ##NON NULL ##LIST
   endpoints: ID ##NON NULL ##LIST

class DeletedTransformation(GQLObject):
   id: ID ##NON NULL
   deleted: bool

class updateTransactionInput(GQLObject):
   ids: ID ##LIST
   paidout: bool
   amount: float

class OrgTransaction(GQLObject):
   invoiceLink: str
   createdAt: str
   totalAmount: float

class TransactionsSummaryWhereInput(GQLObject):
   fromDate: str
   toDate: str
   apiIds: ID ##LIST
   userIds: ID ##LIST

class TransactionsItem(GQLObject):
   title: str
   sum: float

class Tenant(GQLObject):
   id: ID ##NON NULL
   name: str
   domain: str
   slugifiedKey: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime

class TeamUpdateInput(GQLObject):
   id: int ##NON NULL
   name: str
   thumbnail: str
   description: str

class EditTeamInput(GQLObject):
   id: int ##NON NULL
   name: str
   thumbnail: str
   description: str

class UserRolesUpdateInput(GQLObject):
   entityId: int ##NON NULL
   roleId: int ##NON NULL
   orgId: int ##NON NULL

class TargetUrlUpdateInput(GQLObject):
   url: str ##NON NULL
   loadBalancingStrategyValue: str

class TagDefinition(GQLObject):
   id: str
   color: str
   description: str
   status: str
   type: str
   name: str
   values: str ##LIST
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
   dsLegalAccountId: str ##NON NULL
   dsLegalEnvelopId: str ##NON NULL

class SpotlightSortingField(GQLObject):
   fieldName: SpotlightFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class SpotlightDeleteInput(GQLObject):
   id: ID ##NON NULL
   apiId: ID ##NON NULL

class SpotlightCreateInput(GQLObject):
   apiId: ID ##NON NULL
   type: SpotlightType ##NON NULL
   weight: int ##NON NULL
   published: bool
   title: str
   description: str
   spotlightURL: str
   file: Upload

class updateBaseUrlInput(GQLObject):
   secretDataId: str
   url: str

class SearchCollectionSortingField(GQLObject):
   fieldName: SearchCollectionSortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class SearchBlogPostWhereInput(GQLObject):
   term: str ##NON NULL

class SearchApiSortingField(GQLObject):
   fieldName: SearchApiSortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class SearchApiUser(GQLObject):
   id: int
   thumbnail: str
   name: str
   username: str

class RoleSorting(GQLObject):
   fieldName: RoleSortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class RequestLogsOnProjectFilters(GQLObject):
   apiIds: ID ##NON NULL ##LIST
   endpoints: str ##NON NULL ##LIST
   httpMethods: HttpMethod ##NON NULL ##LIST
   httpStatuses: int ##NON NULL ##LIST
   originIps: str ##NON NULL ##LIST

class RequestLogFilters(GQLObject):
   projectIds: str ##LIST
   apiIds: str ##LIST
   userIds: ID ##NON NULL ##LIST
   endpoints: str ##NON NULL ##LIST
   endpointRoutes: str ##NON NULL ##LIST
   httpMethods: HttpMethod ##NON NULL ##LIST
   httpStatuses: int ##NON NULL ##LIST
   originIps: str ##NON NULL ##LIST
   gatewayIds: ID ##LIST

class deleteProjectAllowedAPIsInput(GQLObject):
   projectAllowedAPIIds: int ##NON NULL ##LIST
   projectId: int ##NON NULL
   mashapeId: str ##NON NULL

class createProjectAllowedAPIInput(GQLObject):
   projectId: int ##NON NULL
   apiId: str ##NON NULL
   apiVersionId: str ##NON NULL
   mashapeId: str ##NON NULL

class ProjectCreateInput(GQLObject):
   projectOwner: ID ##NON NULL
   projectName: str ##NON NULL
   description: str
   thumbnail: Upload

class DeleteProjectInput(GQLObject):
   projectId: ID ##NON NULL
   projectName: str ##NON NULL
   mashapeId: ID ##NON NULL

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
   password: str ##NON NULL
   confirmPassword: str ##NON NULL
   token: str ##NON NULL

class CorporateDomain(GQLObject):
   domain: str
   ignore: bool

class UsersInvitation(GQLObject):
   id: str
   email: str
   role: str

class BillingAdditionalValues(GQLObject):
   total: int ##NON NULL
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
   messageThreadIds: int ##NON NULL ##LIST
   flag: EntityStatusFlag ##NON NULL
   value: bool ##NON NULL

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
   apiIds: str ##LIST
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
   entityId: str ##NON NULL
   legalDocumentId: str ##NON NULL
   legalAccountId: str ##NON NULL

class UpdateLegalAgreementInfo(GQLObject):
   id: ID ##NON NULL
   refreshToken: str
   accessToken: str
   vendor: str

class ProduceMessageInput(GQLObject):
   apiVersionId: str ##NON NULL
   topicName: str ##NON NULL
   key: str ##NON NULL
   value: str ##NON NULL
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
   id: int ##NON NULL
   schema: str ##NON NULL
   schemaType: SchemaType ##NON NULL
   subject: str ##NON NULL
   version: int ##NON NULL

class TopicOffset(GQLObject):
   partition: int ##NON NULL
   offset: str ##NON NULL
   high: str ##NON NULL
   low: str ##NON NULL

class SubscribeKafkaResponse(GQLObject):
   actionsChannel: str ##NON NULL
   authKey: str ##NON NULL
   messagesChannel: str ##NON NULL
   publishKey: str ##NON NULL
   subscribeKey: str ##NON NULL

class KafkaTopic(GQLObject):
   name: str ##NON NULL

class IssueFollow(GQLObject):
   id: int ##NON NULL
   follower: int
   followee: int
   mashapeId: str
   mashapeIssueId: str
   createdAt: DateTime
   updatedAt: DateTime
   status: str

class updateHeadlines(GQLObject):
   apiId: str ##NON NULL
   apiVersionId: str ##NON NULL
   headlineId: str ##NON NULL
   text: str
   textModified: bool ##NON NULL

class Headline(GQLObject):
   text: str ##NON NULL
   id: str
   status: str
   index: int ##NON NULL
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
   entityIds: int ##NON NULL ##LIST
   orgId: int
   parentIds: int ##LIST

class EntityMetadataSortingField(GQLObject):
   fieldName: EntityMetadataSortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class EntityMetadata(GQLObject):
   id: ID ##NON NULL
   entityId: ID ##NON NULL
   attributeName: str ##NON NULL
   attributeValue: str ##NON NULL

class EntityAttribute(GQLObject):
   attributeName: str ##NON NULL
   attributeValue: str ##NON NULL

class EndpointOrder(GQLObject):
   endpointId: str ##NON NULL
   groupId: str
   index: int ##NON NULL

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
   options: str ##LIST
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
   id: ID ##NON NULL ##LIST

class EndpointStatsData(GQLObject):
   date: str
   requests: int
   errors: int
   latency: float
   endpointid: ID

class IssueUpdateInput(GQLObject):
   title: str ##NON NULL
   body: str ##NON NULL
   issueId: int ##NON NULL

class IssueCreateInputV2(GQLObject):
   title: str ##NON NULL
   body: str ##NON NULL
   apiId: str ##NON NULL
   apiVersion: str

class ContextEntity(GQLObject):
   context: Any
   token: str
   privateApisJwt: str

class ConsumersWhereInput(GQLObject):
   apiId: ID ##NON NULL ##LIST
   offset: int
   limit: int
   order: str
   lastActive: str ##NON NULL ##LIST
   userId: int ##NON NULL ##LIST
   sort: str
   usernames: str ##NON NULL ##LIST
   plansFilter: str ##NON NULL ##LIST
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
   body: str ##NON NULL
   issueId: int ##NON NULL
   commentId: int ##NON NULL

class UpdateCollectionsInput(GQLObject):
   collectionId: ID ##NON NULL
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   title: str
   apis: ID ##LIST
   ownerId: int

class CollectionCreateInput(GQLObject):
   title: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: ID ##LIST
   ownerId: int
   collection_type: str

class CollapsedCollection(GQLObject):
   id: str ##NON NULL
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: str ##LIST

class CollectionsSortingField(GQLObject):
   fieldName: str ##NON NULL
   order: SortingFieldOrder ##NON NULL

class CategorySortingField(GQLObject):
   fieldName: CategorySortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class DeletedCategory(GQLObject):
   id: ID ##NON NULL
   deleted: bool
   reason: str

class Category(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   slugifiedName: str ##NON NULL
   status: str
   shortDescription: str ##NON NULL
   longDescription: str
   thumbnail: str
   pageTitle: str
   weight: int ##NON NULL
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
   billingFeature: str ##NON NULL
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
   billingPlanId: str ##NON NULL
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
   item: str ##NON NULL
   amount: int
   limitType: str
   overagePrice: float
   period: str ##NON NULL
   unlimited: bool ##NON NULL
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
   id: str ##NON NULL
   endpoint: str
   endpointHash: str
   billingfeature: str
   type: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime

class billingFeatureEndpointArray(GQLObject):
   endpoint: str ##NON NULL

class AuthenticationParam(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   description: str
   authentication: str ##NON NULL

class geo(GQLObject):
   country: str
   city: str
   region: str
   timezone: str
   ll: float ##LIST

class params(GQLObject):
   input: Any

class AuditWhereInput(GQLObject):
   searchTerm: str
   from_: int
   orgId: int

class UserAttributesInput(GQLObject):
   type: str
   attributeValue: Any ##LIST

class AsyncApiConfigurationWhereInput(GQLObject):
   apiVersionId: ID ##NON NULL ##LIST

class AsyncApiConfiguration(GQLObject):
   id: ID ##NON NULL
   spec: str

class AssetUpdateInput(GQLObject):
   id: ID ##NON NULL
   title: str
   description: str
   visible: bool

class AssetForDownload(GQLObject):
   id: ID ##NON NULL
   downloadUrl: str ##NON NULL
   filename: str ##NON NULL
   title: str
   externalId: str ##NON NULL
   fileSizeBytes: float

class Application(GQLObject):
   id: ID ##NON NULL
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
   applicationEnviornmentId: ID ##NON NULL
   mashapeId: str ##NON NULL
   keyName: str ##NON NULL
   environment: str ##NON NULL

class AppAuthorizationUpdateInput(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL

class AppAuthorizationsWhereInput(GQLObject):
   projectId: ID ##NON NULL

class ApiWhereInput(GQLObject):
   id: ID ##NON NULL ##LIST
   ownerId: ID ##NON NULL ##LIST
   subscriberId: ID ##NON NULL ##LIST
   visibility: ApiVisibility
   apiSlugifiedName: str ##NON NULL ##LIST
   ownerSlugifiedName: str ##NON NULL ##LIST
   name: str ##NON NULL ##LIST
   isFavorite: bool

class ApiSecurityInfo(GQLObject):
   rapidapiProxySecret: str

class ApiTermsOfServiceInput(GQLObject):
   text: str

class validateSwaggerInput(GQLObject):
   file: Upload

class ApiVersionSecretParameterInput(GQLObject):
   name: str ##NON NULL
   value: str ##NON NULL
   description: str
   placement: SecretParameterPlacement

class GqlApiVersionCreateInput(GQLObject):
   api: str ##NON NULL
   name: str ##NON NULL
   visibility: Visibility
   oldApiVersionId: str
   introspectionCallUrl: str ##NON NULL
   isIntrospectionCall: bool
   allowHubSchemaRefresh: bool
   gqlFile: Any

class RequestPayload(GQLObject):
   id: str ##NON NULL
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
   examples: Any ##NON NULL
   schema: Any
   schemaDefinition: Any

class Publicdns(GQLObject):
   address: str
   proxyMode: str
   apiversion: str
   current: bool
   id: ID ##NON NULL
   createdAt: DateTime
   updatedAt: DateTime
   status: str

class ApiVersionSortingField(GQLObject):
   fieldName: ApiSortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

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
   message: str ##NON NULL
   severity: ApiSpecImportProcessIssueSeverity ##NON NULL

class ApiUpdateFromRapidOasInput(GQLObject):
   spec: Upload ##NON NULL
   apiVersionId: ID ##NON NULL

class ApiUpdateFromSpecInput(GQLObject):
   apiVersionId: ID ##NON NULL
   spec: Upload ##NON NULL
   specType: ApiSpecType ##NON NULL

class SearchArguments(GQLObject):
   categoryName: str
   categoryNames: str ##LIST
   exclude: str ##LIST
   term: str
   sortBy: str
   size: int ##NON NULL
   offset: int ##NON NULL
   page: int ##NON NULL
   tags: Any ##LIST
   collectionIds: str ##LIST
   privateApisJwt: str

class ApiReferenceWhereInput(GQLObject):
   apiVersionId: ID ##NON NULL ##LIST

class RatingInput(GQLObject):
   apiId: str
   rating: int

class ApiQuality(GQLObject):
   apiId: ID ##NON NULL
   score: int

class ApiFollowerSortingField(GQLObject):
   fieldName: ApiFollowerSortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class ApiFollowerCreateInput(GQLObject):
   apiId: ID ##NON NULL

class CreateApiFavoritesInput(GQLObject):
   apiIds: ID ##NON NULL ##LIST

class ApiDeveloperEntityInput(GQLObject):
   id: ID
   mashapeId: str
   name: str
   type: EntityType

class ApiCertificateWhereInput(GQLObject):
   id: ID ##NON NULL ##LIST
   ownerId: ID ##NON NULL ##LIST

class ApiCertificateSubjectInfo(GQLObject):
   alternativeNames: str ##NON NULL
   commonName: str
   countryName: str
   localityName: str
   organizationName: str
   organizationalUnitName: str
   stateOrProvinceName: str
   emailAddress: str

class UserAlertsWhereInput(GQLObject):
   scope: ID ##NON NULL

class UserAlertUpdateInput(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   description: str
   typeId: int ##NON NULL
   condition: Condition ##NON NULL
   threshold: float ##NON NULL
   timeInterval: time ##NON NULL
   timePeriod: int ##NON NULL
   channel: Channel
   status: AlertStatus ##NON NULL
   throttleInterval: time ##NON NULL
   throttlePeriod: int ##NON NULL
   baseUrl: str
   apiIds: ID ##NON NULL ##LIST
   projectIds: ID ##NON NULL ##LIST
   endpointsIds: ID ##NON NULL ##LIST
   apiVersionsIds: ID ##NON NULL ##LIST
   billingPlansIds: ID ##NON NULL ##LIST
   endpointHashes: ID ##NON NULL ##LIST

class addUserAlertInput(GQLObject):
   name: str ##NON NULL
   description: str
   scope: ID ##NON NULL
   typeId: int ##NON NULL
   condition: Condition ##NON NULL
   threshold: float ##NON NULL
   timeInterval: time ##NON NULL
   timePeriod: int ##NON NULL
   channel: Channel
   status: AlertStatus ##NON NULL
   throttleInterval: time ##NON NULL
   throttlePeriod: int ##NON NULL
   apiIds: ID ##LIST
   projectIds: ID ##LIST
   baseUrl: str
   minNextAlertTime: DateTime
   endpointsIds: ID ##NON NULL ##LIST
   apiVersionsIds: ID ##NON NULL ##LIST
   billingPlansIds: ID ##NON NULL ##LIST
   endpointHashes: ID ##NON NULL ##LIST

class AlertDefinition(GQLObject):
   id: ID ##NON NULL
   type: str ##NON NULL
   status: AlertStatus ##NON NULL
   description: str ##NON NULL
   units: str

class EnvConfigUpdateInput(GQLObject):
   id: int ##NON NULL
   value: str ##NON NULL

class GatewayTemplateParamsUpdateInput(GQLObject):
   paramName: str ##NON NULL
   paramValue: str ##NON NULL
   paramDescription: str ##NON NULL
   id: ID

class GatewayCustomMessageUpdateInput(GQLObject):
   messageKey: MessageKey ##NON NULL
   messageValue: str ##NON NULL
   id: ID

class GatewayCustomMessageCreateInput(GQLObject):
   messageKey: MessageKey ##NON NULL
   messageValue: str ##NON NULL

class EventConfigUpdateInput(GQLObject):
   isActive: bool
   shouldGenerateSecret: bool

class EventUrlCreateInput(GQLObject):
   url: str ##NON NULL

class EventLogSortablesSortingField(GQLObject):
   fieldName: EventLogSortables ##NON NULL
   order: Order

class AdminAuditLogSortablesSortingField(GQLObject):
   fieldName: AdminAuditLogSortables ##NON NULL
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
   id: str ##NON NULL
   url: str ##NON NULL
   eventType: str ##NON NULL
   eventData: str ##NON NULL
   eventText: str ##NON NULL
   statusCode: str
   highlight: str ##LIST
   createdAt: DateTime

class AuditUser(GQLObject):
   id: int
   email: str ##NON NULL
   name: str
   thumbnail: str
   type: str
   mashapeId: str
   slugifiedName: str

class EventType(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   label: str ##NON NULL
   example: str ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL
   deletedAt: DateTime

class EnvConfigCategory(GQLObject):
   id: int ##NON NULL
   name: str ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL

class GatewayConfigurations(GQLObject):
   gatewayDefaultTimeOut: int
   limitRequestSize: int
   allowHttpTraffic: bool

class PageInfo(GQLObject):
   hasNextPage: bool ##NON NULL
   hasPreviousPage: bool ##NON NULL
   startCursor: str
   endCursor: str

class Stats(GQLObject):
   apiStats: StatsData ##LIST

class FollowersUser(GQLObject):
   startFollowDate: str
   id: int
   email: str
   username: str
   user: NewType('User', GQLObject) ## Circular Reference for User
   attributes: Any

class KafkaJSConfiguration(GQLObject):
   brokers: str ##NON NULL
   clientId: str
   ssl: bool
   sasl: SaslConfiguration

class KafkaConfiguration(GQLObject):
   kafkaConfiguration: KafkaJSConfiguration
   schemaRegistryConfiguration: SchemaRegistryConfiguration
   allowProducingRecords: bool

class Authentication(GQLObject):
   id: ID ##NON NULL
   apiVersionId: str ##NON NULL
   authType: AuthenticationType ##NON NULL
   description: str
   accessTokenUrl: str
   authorizationUrl: str
   requestTokenUrl: str
   grantType: GrantType
   separator: SeparatorType
   clientSecretRequired: bool
   clientAuthentication: ClientAuthenticationType
   authParams: AuthenticationParam ##NON NULL
   handleOauthTokenAtFrontend: bool

class ApiVersionAccessControlInfo(GQLObject):
   authentication: Authentication
   secretParameters: SecretParameter ##NON NULL

class GraphQLSchema(GQLObject):
   id: ID ##NON NULL
   endpointId: ID
   schema: Any
   allowHubSchemaRefresh: bool
   isIntrospectionCall: bool
   status: str
   type: str
   createdAt: DateTime
   updatedAt: DateTime
   documentation: GqlDoc ##LIST

class CCUEXgraphQLSchema_GraphQLSchema_Field(GraphQLSchema):
   class GraphQLSchemaArgs(GQLArgsSet, GQLObject): 
      withOverrides: bool

   _args: GraphQLSchemaArgs



class BBUBOmockResponse_ResponsePayload_Field(ResponsePayload):
   class ResponsePayloadArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: ResponsePayloadArgs



class Endpoint(GQLObject):
   id: ID ##NON NULL
   index: int
   apiversion: str
   createdAt: DateTime
   updatedAt: DateTime
   description: str
   group: str
   method: ApiEndpointHttpMethod ##NON NULL
   name: str
   route: str
   routeregex: str
   webhook: bool
   params: EndpointParams
   displayResponse: bool
   isGraphQL: bool
   graphQLSchema: CCUEXgraphQLSchema_GraphQLSchema_Field
   mockResponseId: ID
   isMockResponse: bool
   summary: str
   externalDocs: ExternalDocs
   endpointHash: str
   appliedOauth2Scopes: AuthenticationParam ##NON NULL
   requestPayloads: RequestPayload ##LIST
   responsePayloads: ResponsePayload ##LIST
   mockResponse: BBUBOmockResponse_ResponsePayload_Field

class EndpointsGroup(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   apiVersionId: ID ##NON NULL
   index: int ##NON NULL
   status: str ##NON NULL
   createdAt: DateTime ##NON NULL
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
   id: str ##NON NULL
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

class KVRQRbillingitemendpoints_BillingItemEndpoint_Field(BillingItemEndpoint):
   class BillingItemEndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingItemEndpointArgs



class WEQFKusageInSubscription_UsageData_Field(UsageData):
   class UsageDataArgs(GQLArgsSet, GQLObject): 
      subscriptionId: ID ##NON NULL
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
   billingitemendpoints: KVRQRbillingitemendpoints_BillingItemEndpoint_Field
   allEndpoints: bool
   usageInSubscription: WEQFKusageInSubscription_UsageData_Field

class BillingLimit(GQLObject):
   id: str
   period: str ##NON NULL
   amount: int ##NON NULL
   currency: str ##NON NULL
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
   id: ID ##NON NULL
   name: str ##NON NULL
   slugifiedName: str ##NON NULL
   description: str
   apiVersionId: ID ##NON NULL
   status: BillingFeatureStatus ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime
   billingFeatureEndpoints: Endpoint ##NON NULL

class EnableBillingFeature(GQLObject):
   id: str ##NON NULL
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
   usageByBillingItem: usageByBillingItem ##LIST
   pricing: str

class UsagePeriodGrouper(GQLObject):
   period: str
   calculated: UsageItem ##LIST

class Usage(GQLObject):
   quotaId: ID
   quota: int
   title: str
   overChargePrice: float
   period: str
   calculated: UsageItem ##LIST

class Usages(GQLObject):
   usage: Usage ##LIST
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
   usages: Usages ##NON NULL
   Charge: TransactionCharge
   stripeId: str
   invoicePeriodStart: str
   invoicePeriodEnd: str

class YIWVOusageByBillingItem_UsagePeriodGrouper_Field(UsagePeriodGrouper):
   class UsagePeriodGrouperArgs(GQLArgsSet, GQLObject): 
      billingItemIds: ID ##NON NULL ##LIST
      fromDate: str
      toDate: str
      resolution: UsageResolution
      orderDir: OrderDirection

   _args: UsagePeriodGrouperArgs



class BillingSubscription(GQLObject):
   subscriptionUsage: SubscriptionUsage
   id: int ##NON NULL
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
   usageByBillingItem: YIWVOusageByBillingItem_UsagePeriodGrouper_Field
   usages: SubscriptionUsage
   parentId: int
   teamsSubscriptions: NewType('BillingSubscription', GQLObject) ##LIST ## Circular Reference for BillingSubscription
   entity: NewType('Entity', GQLObject) ## Circular Reference for Entity
   transactions: Transaction ##LIST

class MDEQGapiVersionBillingPlanVersion_ApiVersionBillingPlanVersion_Field(ApiVersionBillingPlanVersion):
   class ApiVersionBillingPlanVersionArgs(GQLArgsSet, GQLObject): 
      apiVersionId: str
      filters: BillingPlanVersionFilters

   _args: ApiVersionBillingPlanVersionArgs



class IMDTWbillinglimits_BillingLimit_Field(BillingLimit):
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
   apiVersionBillingPlanVersion: MDEQGapiVersionBillingPlanVersion_ApiVersionBillingPlanVersion_Field
   billinglimits: IMDTWbillinglimits_BillingLimit_Field
   enablebillingfeatures: EnableBillingFeature ##LIST
   rateLimit: RateLimit
   subscriptions: BillingSubscription ##LIST
   subscriptionsCount: int

class TargetGroup(GQLObject):
   id: ID ##NON NULL
   apiId: ID ##NON NULL
   loadBalancingStrategy: LoadBalancingStrategy ##NON NULL
   name: str ##NON NULL
   targetUrls: TargetUrl ##NON NULL

class CIFNVversion_BillingPlanVersion_Field(BillingPlanVersion):
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject): 
      id: str
      showDeleted: bool

   _args: BillingPlanVersionArgs



class BillingPlan(GQLObject):
   id: str ##NON NULL
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
   allowedPlanDevelopers: AllowedPlanDeveloper ##LIST
   allowedPlanDevelopersCount: int
   legalDocumentId: str
   legalAccountId: str
   isStudent: bool
   version: CIFNVversion_BillingPlanVersion_Field
   targetGroup: TargetGroup
   targetGroupId: str
   shouldRequestApproval: bool
   requestApprovalQuestion: str

class ApiCertificate(GQLObject):
   id: ID ##NON NULL
   ownerId: ID ##NON NULL
   alias: str ##NON NULL
   effectiveDate: DateTime ##NON NULL
   expiry: DateTime ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime
   serialNumber: str ##NON NULL
   signatureAlgorithm: str ##NON NULL
   publicKeySignatureAlgorithm: ApiCertificatePublicKeySignatureAlgorithm ##NON NULL
   publicKeySizeInBits: int ##NON NULL
   publicKeyExponent: int ##NON NULL
   certificateDataAsPem: str ##NON NULL
   issuer: ApiCertificateIssuerInfo ##NON NULL
   subject: ApiCertificateSubjectInfo ##NON NULL
   associations: NewType('ApiCertificateAssociation', GQLObject) ##NON NULL ## Circular Reference for ApiCertificateAssociation
   associatedApiVersionsCount: int ##NON NULL

class ApiCertificateAssociation(GQLObject):
   apiCertificateId: ID ##NON NULL
   apiVersionId: ID ##NON NULL
   createdAt: DateTime ##NON NULL
   apiCertificate: ApiCertificate ##NON NULL
   apiVersion: NewType('ApiVersion', GQLObject) ##NON NULL ## Circular Reference for ApiVersion

class ApiSchema(GQLObject):
   identifier: str ##NON NULL
   apiVersion: NewType('ApiVersion', GQLObject) ##NON NULL ## Circular Reference for ApiVersion
   definition: Any ##NON NULL
   index: int

class SecretData(GQLObject):
   id: ID ##NON NULL
   apiversion: ID

class YNWXXpayloads_ResponsePayload_Field(ResponsePayload):
   class ResponsePayloadArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: ResponsePayloadArgs



class ERIJPendpoints_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointArgs



class WITCYgroups_EndpointsGroup_Field(EndpointsGroup):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointsGroupArgs



class TTFMOpublicdns_Publicdns_Field(Publicdns):
   class PublicdnsArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: PublicdnsArgs



class KWBKSbillingplans_BillingPlan_Field(BillingPlan):
   class BillingPlanArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      showDeleted: bool
      visibility: Visibility

   _args: BillingPlanArgs



class HQGYYheadlines_Headline_Field(Headline):
   class HeadlineArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: HeadlineArgs



class KJRZZbillingitems_BillingItem_Field(BillingItem):
   class BillingItemArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingItemArgs



class NJQOZbillingitemendpoints_BillingItemEndpoint_Field(BillingItemEndpoint):
   class BillingItemEndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingItemEndpointArgs



class OJLIIassets_Asset_Field(Asset):
   class AssetArgs(GQLArgsSet, GQLObject): 
      visible: bool

   _args: AssetArgs



class ApiVersion(GQLObject):
   id: ID ##NON NULL
   api: str
   current: bool
   name: str
   status: str
   keywords: str ##LIST
   createdAt: DateTime
   updatedAt: DateTime
   visibility: str
   apiInstance: NewType('Api', GQLObject) ## Circular Reference for Api
   kafkaConfiguration: KafkaConfiguration
   asyncApiConfiguration: AsyncApiConfiguration
   webhooks: bool
   payloads: YNWXXpayloads_ResponsePayload_Field
   accessControl: ApiVersionAccessControlInfo ##NON NULL
   endpoints: ERIJPendpoints_Endpoint_Field
   groups: WITCYgroups_EndpointsGroup_Field
   publicdns: TTFMOpublicdns_Publicdns_Field
   billingplans: KWBKSbillingplans_BillingPlan_Field
   headlines: HQGYYheadlines_Headline_Field
   billingitems: KJRZZbillingitems_BillingItem_Field
   billingitemendpoints: NJQOZbillingitemendpoints_BillingItemEndpoint_Field
   publicBillingPlanVersions: ApiVersionBillingPlanVersion ##LIST
   targetGroup: TargetGroup
   targetGroupId: str
   transformations: Transformation ##LIST
   versionStatus: VersionStatus
   apiSubType: apiSubTypeEnum
   associatedApiCertificates: ApiCertificateAssociation ##NON NULL
   assets: OJLIIassets_Asset_Field
   apiSchemas: ApiSchema ##NON NULL

class FollowApi(GQLObject):
   id: str
   follower: str
   api: str
   status: str
   apiData: NewType('Api', GQLObject) ## Circular Reference for Api
   user: NewType('User', GQLObject) ## Circular Reference for User

class Comment(GQLObject):
   id: int ##NON NULL
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
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User

class XZEFCcomments_Comment_Field(Comment):
   class CommentArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: CommentArgs



class KAGZYcommentsV2_Comment_Field(Comment):
   class CommentArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: CommentArgs



class Issue(GQLObject):
   id: int ##NON NULL
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
   comments: XZEFCcomments_Comment_Field
   commentsV2: KAGZYcommentsV2_Comment_Field
   user: NewType('User', GQLObject) ##NON NULL ## Circular Reference for User
   api: NewType('Api', GQLObject) ## Circular Reference for Api

class Spotlight(GQLObject):
   id: ID ##NON NULL
   type: SpotlightType ##NON NULL
   apiId: ID ##NON NULL
   spotlightURL: str
   status: str
   slugifiedName: str
   thumbnailURL: str
   title: str
   description: str
   weight: int ##NON NULL
   published: bool ##NON NULL
   updatedAt: DateTime
   createdAt: DateTime

class ApiDeveloper(GQLObject):
   id: ID ##NON NULL
   developer: ID ##NON NULL
   api: ID ##NON NULL
   type: EntityType
   status: ApiDeveloperStatus ##NON NULL
   blocked: bool
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime
   deletedAt: DateTime
   user: NewType('Entity', GQLObject) ## Circular Reference for Entity

class FKZRPendpointObject_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      showDeleted: bool

   _args: EndpointArgs



class RequestLog(GQLObject):
   requestId: ID
   projectId: ID
   api: str
   apiId: ID
   endpoint: str
   endpointObject: FKZRPendpointObject_Endpoint_Field
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
   requests: RequestLog ##LIST
   totalCount: int

class FBKCZissues_Issue_Field(Issue):
   class IssueArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: IssueArgs



class XSKBKannouncements_Announcement_Field(Announcement):
   class AnnouncementArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: AnnouncementArgs



class IGJFAapiDevelopers_ApiDeveloper_Field(ApiDeveloper):
   class ApiDeveloperArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: ApiDeveloperArgs



class HPHNIheadlines_Headline_Field(Headline):
   class HeadlineArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: HeadlineArgs



class XKMHSendpoints_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointArgs



class YWNERbillingFeatures_BillingFeature_Field(BillingFeature):
   class BillingFeatureArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingFeatureArgs



class HAECXbillingItems_BillingItem_Field(BillingItem):
   class BillingItemArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingItemArgs



class WHBGWbillingPlans_BillingPlan_Field(BillingPlan):
   class BillingPlanArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: BillingPlanArgs



class ZIZWBrequestLogs_RequestLogsResult_Field(RequestLogsResult):
   class RequestLogsResultArgs(GQLArgsSet, GQLObject): 
      fromDate: str ##NON NULL
      toDate: str
      limit: int
      offset: int
      orderBy: RequestLogsOrderBy
      orderDir: OrderDirection
      filters: RequestLogsOnApiFilters

   _args: RequestLogsResultArgs



class Api(GQLObject):
   id: str ##NON NULL
   name: str
   installsAllTime: int
   requestTimeout: int
   requestSizeLimit: int
   installsDaily: int
   installsMonthly: int
   installsWeekly: int
   pricing: ApiPricing ##NON NULL
   apiType: ApiType ##NON NULL
   currentVersion: ApiVersion
   category: str
   createdAt: str
   updatedAt: str
   ownerId: int
   proxy: bool
   status: ApiStatus ##NON NULL
   description: str
   longDescription: str
   tags: APITag ##NON NULL
   thumbnail: str
   thumbnailSmall: str
   websiteUrl: str
   termsOfService: TermsOfService
   visibility: ApiVisibility
   owner: NewType('Entity', GQLObject) ## Circular Reference for Entity
   score: Score
   followers: FollowApi ##LIST
   followersCount: int
   subscriptionsCount: int
   issues: FBKCZissues_Issue_Field
   rating: apiRating
   slugifiedName: str
   categoryId: str
   allowedContext: str ##LIST
   spotlights: Spotlight ##LIST
   patternMatch: bool
   patternMatchAllowOtherTypes: bool
   requestSchemaValidation: bool
   requestSchemaValidationUnknownAttributePolicy: SchemaValidationUnknownAttributePolicy
   gatewayIds: ID ##NON NULL
   announcements: XSKBKannouncements_Announcement_Field
   apiDevelopers: IGJFAapiDevelopers_ApiDeveloper_Field
   targetGroups: TargetGroup ##LIST
   publishApiPendingRequest: bool
   saveRequestHeadersLogging: bool
   saveRequestQueryParametersLogging: bool
   saveRequestBodyLogging: bool
   saveResponseHeadersLogging: bool
   saveResponseBodyLogging: bool
   useHttpProxy: bool
   security: ApiSecurityInfo ##NON NULL
   versions: ApiVersion ##LIST
   headlines: HPHNIheadlines_Headline_Field
   endpoints: XKMHSendpoints_Endpoint_Field
   billingFeatures: YWNERbillingFeatures_BillingFeature_Field
   billingItems: HAECXbillingItems_BillingItem_Field
   billingPlans: WHBGWbillingPlans_BillingPlan_Field
   isFavorite: bool ##NON NULL
   quality: ApiQuality ##NON NULL
   requestLogs: ZIZWBrequestLogs_RequestLogsResult_Field

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

class HAJPRprojectAllowedAPIs_ProjectAllowedAPI_Field(ProjectAllowedAPI):
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: ProjectAllowedAPIArgs



class NCIIVrequestLogs_RequestLogsResult_Field(RequestLogsResult):
   class RequestLogsResultArgs(GQLArgsSet, GQLObject): 
      fromDate: str ##NON NULL
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
   accounts: Account ##LIST
   xMashapeKey: str
   acl: NewType('ProjectInfo', GQLObject) ## Circular Reference for ProjectInfo
   enableLimitsToAPIs: bool
   projectAllowedAPIs: HAJPRprojectAllowedAPIs_ProjectAllowedAPI_Field
   requestLogs: NCIIVrequestLogs_RequestLogsResult_Field

class ProjectInfo(GQLObject):
   id: int
   owner: int
   project: int
   user: NewType('User', GQLObject) ## Circular Reference for User
   entity: NewType('Entity', GQLObject) ## Circular Reference for Entity
   Project: Project

class SubscriptionsPaging(GQLObject):
   subscriptions: BillingSubscription ##LIST
   totalCount: int

class TransactionsPaging(GQLObject):
   transactions: Transaction ##LIST
   totalCount: int

class TransactionsGraphData(GQLObject):
   prev: TransactionsItem
   curr: TransactionsItem
   overages: TransactionsItem

class UserAttributes(GQLObject):
   count: int
   rows: UserAttributesRow ##LIST

class EnvelopeTemplate(GQLObject):
   documents: EnvelopeDocument ##LIST
   templateId: str
   uri: str
   created: DateTime
   name: str
   description: str

class Template(GQLObject):
   envelopeTemplates: EnvelopeTemplate ##LIST

class DocuSignAccount(GQLObject):
   id: str
   name: str
   baseUri: str
   template: Template

class DocuSignUserInfo(GQLObject):
   name: str
   email: str
   accounts: DocuSignAccount ##LIST

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

class HAXCEsubscriptions_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      isStripeId: bool
      getAllSubscriptions: bool

   _args: BillingSubscriptionArgs



class GLEWCsubscriptionsPaging_SubscriptionsPaging_Field(SubscriptionsPaging):
   class SubscriptionsPagingArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      isStripeId: bool
      getAllSubscriptions: bool

   _args: SubscriptionsPagingArgs



class FINQZactiveSubscriptionByApiId_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      apiId: ID ##NON NULL

   _args: BillingSubscriptionArgs



class KKXWUactiveSubscriptionByApiIdAndBillingPlanVersionId_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      apiId: ID ##NON NULL
      billingPlanVersionId: ID

   _args: BillingSubscriptionArgs



class QueryFilter(GQLObject):
   columnName: str
   operand: str
   value: Any
   values: MultipleValuesQueryFilter ##LIST

class QueryFilters(GQLObject):
   filters: QueryFilter ##LIST

class ZIOZXpagedTransactions_TransactionsPaging_Field(TransactionsPaging):
   class TransactionsPagingArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      apiNameFilter: str
      queryFilters: QueryFilters

   _args: TransactionsPagingArgs



class ETZJBnotFullyRefundedTransactions_TransactionsPaging_Field(TransactionsPaging):
   class TransactionsPagingArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      apiNameFilter: str
      queryFilters: QueryFilters

   _args: TransactionsPagingArgs



class SPIVMtransaction_Transaction_Field(Transaction):
   class TransactionArgs(GQLArgsSet, GQLObject): 
      id: ID
      mashapeId: ID

   _args: TransactionArgs



class KZIPFstats_Stats_Field(Stats):
   class StatsArgs(GQLArgsSet, GQLObject): 
      apiId: ID
      fromDate: DateTime ##NON NULL
      toDate: DateTime
      resolution: Resolution
      groupBy: StatsGroupBy

   _args: StatsArgs



class Entity(GQLObject):
   id: str ##NON NULL
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
   followsList: NewType('FollowUser', GQLObject) ##LIST ## Circular Reference for FollowUser
   numOfSubscriptions: int
   projectAcls: ProjectInfo ##LIST
   subscriptions: HAXCEsubscriptions_BillingSubscription_Field
   subscriptionsPaging: GLEWCsubscriptionsPaging_SubscriptionsPaging_Field
   activeSubscriptionByApiId: FINQZactiveSubscriptionByApiId_BillingSubscription_Field
   activeSubscriptionByApiIdAndBillingPlanVersionId: KKXWUactiveSubscriptionByApiIdAndBillingPlanVersionId_BillingSubscription_Field
   pagedTransactions: ZIOZXpagedTransactions_TransactionsPaging_Field
   notFullyRefundedTransactions: ETZJBnotFullyRefundedTransactions_TransactionsPaging_Field
   transactionsGraphData: TransactionsGraphData
   transaction: SPIVMtransaction_Transaction_Field
   parents: NewType('Entity', GQLObject) ##LIST ## Circular Reference for Entity
   stats: KZIPFstats_Stats_Field
   billingInformation: BillingInformation
   bio: str
   publishedApisList: Api ##LIST
   apis: Api ##LIST
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
   id: ID ##NON NULL
   followerId: ID ##NON NULL
   apiId: ID ##NON NULL
   createdAt: DateTime
   api: Api
   follower: NewType('User', GQLObject) ## Circular Reference for User

class Notification(GQLObject):
   id: int ##NON NULL
   userId: int
   type: int
   text: str
   message: NotificationMessage
   messageType: str
   read: bool
   createdAt: DateTime
   updatedAt: DateTime

class ProjectAcl(GQLObject):
   id: int ##NON NULL
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
   email: str ##NON NULL
   inviteStatus: str
   teams: NewType('Team', GQLObject) ##LIST ## Circular Reference for Team
   role: str
   token: str
   userData: NewType('User', GQLObject) ## Circular Reference for User
   teamsCount: int

class IssueObject(GQLObject):
   data: Issue ##LIST
   total: int

class ZHUFQsubscriptions_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      isStripeId: bool

   _args: BillingSubscriptionArgs



class SJBHWfollowersList_FollowersUser_Field(FollowersUser):
   class FollowersUserArgs(GQLArgsSet, GQLObject): 
      includeUserAttributes: bool

   _args: FollowersUserArgs



class STNQPissues_IssueObject_Field(IssueObject):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: IssueObjectArgs



class Team(GQLObject):
   id: ID ##NON NULL
   mashapeId: str
   thumbnail: str
   name: str
   slugifiedName: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   status: str
   users: TeamUser ##LIST
   ProjectAcls: ProjectAcl ##LIST
   usersCount: int
   description: str
   subscriptions: ZHUFQsubscriptions_BillingSubscription_Field
   followersList: SJBHWfollowersList_FollowersUser_Field
   publishedApisList: Api ##LIST
   isTeamMember: bool
   issues: STNQPissues_IssueObject_Field

class ZOPUXfollowersList_FollowersUser_Field(FollowersUser):
   class FollowersUserArgs(GQLArgsSet, GQLObject): 
      includeUserAttributes: bool

   _args: FollowersUserArgs



class POGRUissues_IssueObject_Field(IssueObject):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: IssueObjectArgs



class Organization(GQLObject):
   id: ID ##NON NULL
   email: str
   name: str
   thumbnail: str
   slugifiedName: str
   status: str
   billingInformation: BillingInformation
   description: str
   teams: Team ##LIST
   publishedApisList: Api ##LIST
   users: NewType('User', GQLObject) ##LIST ## Circular Reference for User
   followersList: ZOPUXfollowersList_FollowersUser_Field
   isOrganizationAdmin: bool
   apisCount: int
   internalSubscriptionsCount: int
   externalSubscriptionsCount: int
   issues: POGRUissues_IssueObject_Field
   billingAdditionalValues: BillingAdditionalValues
   payoutInfo: PayoutInfo
   balance: float
   occupiedSeats: int
   entity: Any
   seatsBillingInformation: SeatsBillingInformation
   billingType: str

class FRNATstats_Stats_Field(Stats):
   class StatsArgs(GQLArgsSet, GQLObject): 
      fromDate: str ##NON NULL
      toDate: str ##NON NULL
      resolution: str
      projectId: str
      apiId: str
      groupBy: StatsGroupBy
      filters: StatsFilterBy ##LIST
      timeOffset: int

   _args: StatsArgs



class NVDDXfollowersList_FollowersUser_Field(FollowersUser):
   class FollowersUserArgs(GQLArgsSet, GQLObject): 
      includeUserAttributes: bool

   _args: FollowersUserArgs



class HDWTOfollowsList_FollowUser_Field(FollowUser):
   class FollowUserArgs(GQLArgsSet, GQLObject): 
      includeUserAttributes: bool

   _args: FollowUserArgs



class IOZLAsubscriptions_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      isStripeId: bool

   _args: BillingSubscriptionArgs



class EPJLDsubscriptionsPaging_SubscriptionsPaging_Field(SubscriptionsPaging):
   class SubscriptionsPagingArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs
      isStripeId: bool

   _args: SubscriptionsPagingArgs



class LQGNIactiveSubscriptionByApiId_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      apiId: ID ##NON NULL

   _args: BillingSubscriptionArgs



class QJNBXactiveSubscriptionByApiIdAndBillingPlanVersionId_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      apiId: ID ##NON NULL
      billingPlanVersionId: ID

   _args: BillingSubscriptionArgs



class OFXSTproject_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      projectId: ID
      mashapeId: ID

   _args: ProjectArgs



class VRQZVprojects_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      projectIds: ID ##NON NULL ##LIST
      mashapeIds: ID ##NON NULL ##LIST

   _args: ProjectArgs



class EUTHXprojectACL_ProjectInfo_Field(ProjectInfo):
   class ProjectInfoArgs(GQLArgsSet, GQLObject): 
      projectId: ID ##NON NULL

   _args: ProjectInfoArgs



class UNIWUtransaction_Transaction_Field(Transaction):
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
   stats: FRNATstats_Stats_Field
   apisCount: int
   followersList: NVDDXfollowersList_FollowersUser_Field
   followsList: HDWTOfollowsList_FollowUser_Field
   followedApis: ApiFollower ##LIST
   followsIssues: IssueFollow ##LIST
   followsIssuesV2: IssueFollow ##LIST
   subscriptions: IOZLAsubscriptions_BillingSubscription_Field
   subscriptionsPaging: EPJLDsubscriptionsPaging_SubscriptionsPaging_Field
   activeSubscriptionByApiId: LQGNIactiveSubscriptionByApiId_BillingSubscription_Field
   activeSubscriptionByApiIdAndBillingPlanVersionId: QJNBXactiveSubscriptionByApiIdAndBillingPlanVersionId_BillingSubscription_Field
   notifications: Notification ##LIST
   numOfApisUsed: int
   numOfProjects: int
   numOfSubscriptions: int
   billingInformation: BillingInformation
   allowedPlanDevelopers: AllowedPlanDeveloper ##LIST
   payoutInfo: PayoutInfo
   project: OFXSTproject_Project_Field
   projects: VRQZVprojects_Project_Field
   projectACL: EUTHXprojectACL_ProjectInfo_Field
   ProjectACLs: ProjectInfo ##LIST
   ProfileInfo: ProfileInfo
   transactionsGraphData: TransactionsGraphData
   transaction: UNIWUtransaction_Transaction_Field
   ProjectAcls: ProjectAcl ##LIST
   publishedApisList: Api ##LIST
   bio: str
   Teams: Team ##LIST
   organizations: Organization ##LIST
   attributes: UserAttributes
   isCurrentUser: bool
   balance: float
   entity: Any
   userEnrichment: UserEnrichment
   corporateDomain: CorporateDomain
   organizationsWithTheSameDomain: CorporateDomainOrganization ##LIST
   billingType: str
   isUserCreatedBySSO: bool

class OrgSubscriptionUsage(GQLObject):
   id: ID
   name: str
   byOrg: UsageByOrg
   byTeam: UsageByTeam ##LIST

class TutorialEdge(GQLObject):
   node: Tutorial
   cursor: str

class TutorialConnection(GQLObject):
   nodes: Tutorial ##LIST
   edges: TutorialEdge ##LIST
   pageInfo: PageInfo

class TransformationEdge(GQLObject):
   node: Transformation ##NON NULL
   cursor: str ##NON NULL

class TransformationConnection(GQLObject):
   nodes: Transformation ##NON NULL
   edges: TransformationEdge ##NON NULL
   pageInfo: PageInfo ##NON NULL

class TransactionsWhereInput(GQLObject):
   userId: ID
   apiIds: ID ##LIST
   apiOwnerIds: ID ##LIST
   withCharges: bool
   queryFilters: QueryFilters
   pagingArgs: PagingArgs

class TransactionEdge(GQLObject):
   node: Transaction
   cursor: str

class TransactionConnection(GQLObject):
   nodes: Transaction ##LIST
   edges: TransactionEdge ##LIST
   pageInfo: PageInfo
   totalCount: int

class TagDefinitionEdge(GQLObject):
   node: TagDefinition
   cursor: str

class TagDefinitionConnection(GQLObject):
   nodes: TagDefinition ##LIST
   edges: TagDefinitionEdge ##LIST
   pageInfo: PageInfo

class BillingSubscriptionEdge(GQLObject):
   node: BillingSubscription
   cursor: str

class SubscriptionConnection(GQLObject):
   nodes: BillingSubscription ##LIST
   edges: BillingSubscriptionEdge ##LIST
   pageInfo: PageInfo
   totalCount: int

class SpotlightEdge(GQLObject):
   node: Spotlight
   cursor: str

class SpotlightConnection(GQLObject):
   nodes: Spotlight ##LIST
   edges: SpotlightEdge ##LIST
   pageInfo: PageInfo

class XLDLOapis_Api_Field(Api):
   class ApiArgs(GQLArgsSet, GQLObject): 
      weightLowerThan: int

   _args: ApiArgs



class SearchCollection(GQLObject):
   id: str ##NON NULL
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: XLDLOapis_Api_Field
   blogPostId: str
   post: BlogPost
   blogPosts: BlogPosts ##LIST
   orderCollectionItems: str ##LIST
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
   nodes: SearchCollection ##LIST
   edges: SearchConnectionEdge ##LIST
   pageInfo: PageInfo
   total: int

class SearchBlogPostEdge(GQLObject):
   node: SearchBlogPost
   cursor: str

class SearchBlogPostConnection(GQLObject):
   nodes: SearchBlogPost ##LIST
   edges: SearchBlogPostEdge ##LIST
   pageInfo: PageInfo
   total: int

class MQAEDendpoints_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointArgs



class CYQSGgroups_EndpointsGroup_Field(EndpointsGroup):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointsGroupArgs



class VSBBNheadlines_Headline_Field(Headline):
   class HeadlineArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: HeadlineArgs



class SearchApiVersion(GQLObject):
   id: ID ##NON NULL
   api: str
   description: str
   longDescription: str
   name: str
   pricing: str
   status: str
   keywords: str ##LIST
   thumbnail: str
   thumbnailSmall: str
   type: str
   createdAt: DateTime
   updatedAt: DateTime
   visibility: str
   webhooks: bool
   websiteUrl: str
   endpoints: MQAEDendpoints_Endpoint_Field
   tags: APITag ##LIST
   groups: CYQSGgroups_EndpointsGroup_Field
   headlines: VSBBNheadlines_Headline_Field
   authentication: Authentication

class SearchApi(GQLObject):
   id: str
   apiType: str
   name: str
   title: str
   description: str
   keywords: str ##LIST
   installsAllTime: int
   installsDaily: int
   thumbnail: str
   thumbnailSmall: str
   rating: int
   categoryName: str
   User: SearchApiUser
   Ratings: int ##LIST
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
   tags: APITag ##NON NULL

class SearchApiEdge(GQLObject):
   node: SearchApi
   cursor: str

class SearchApiConnection(GQLObject):
   nodes: SearchApi ##LIST
   edges: SearchApiEdge ##LIST
   pageInfo: PageInfo
   total: int
   took: int

class VirtualPermission(GQLObject):
   id: ID ##NON NULL
   key: str ##NON NULL
   displayName: str ##NON NULL
   permissionLevel: str ##NON NULL
   description: str
   dependsOn: int
   rolePermission: RolePermission ##NON NULL

class Role(GQLObject):
   id: ID ##NON NULL
   key: str ##NON NULL
   name: str ##NON NULL
   description: str
   roleLevel: str ##NON NULL
   isBasicRole: bool ##NON NULL
   isDefault: bool ##NON NULL
   permissions: VirtualPermission ##NON NULL

class RoleEdge(GQLObject):
   node: Role
   cursor: str

class RoleConnection(GQLObject):
   nodes: Role ##LIST
   edges: RoleEdge ##LIST
   pageInfo: PageInfo

class MessageThread(GQLObject):
   id: ID ##NON NULL
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
   messages: Message ##LIST
   lastMessage: Message
   api: Api
   entity: Entity
   threadEntityStatus: ThreadEntityStatus
   body: str

class MessageThreadsObject(GQLObject):
   threads: MessageThread ##LIST
   messages: Message ##LIST

class KafkaJSConfigurationInput(GQLObject):
   brokers: str ##NON NULL ##LIST
   clientId: str
   ssl: bool
   sasl: SaslConfigurationInput

class UpdateKafkaConfigurationInput(GQLObject):
   kafkaConfiguration: KafkaJSConfigurationInput ##NON NULL
   schemaRegistryConfiguration: SchemaRegistryConfigurationInput
   allowProducingRecords: bool
   apiVersionId: str ##NON NULL

class TopicSchemaPair(GQLObject):
   key: TopicSchema
   value: TopicSchema

class TopicMetadataResponse(GQLObject):
   topicOffsets: TopicOffset ##NON NULL
   topicConfiguration: TopicConfigurationItem ##NON NULL
   schemas: TopicSchemaPair ##NON NULL

class GatewayTemplate(GQLObject):
   id: int
   name: str
   description: str
   urlPattern: str
   status: str
   type: str
   headers: Header ##LIST

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
   nodes: Gateway ##LIST
   edges: GatewayEdge ##LIST
   pageInfo: PageInfo

class EntityRole(GQLObject):
   id: ID ##NON NULL
   entityId: int ##NON NULL
   roleId: int ##NON NULL
   parentId: int
   orgId: int
   role: Role

class EntityRoleEdge(GQLObject):
   node: EntityRole
   cursor: str

class EntityRoleConnection(GQLObject):
   nodes: EntityRole ##LIST
   edges: EntityRoleEdge ##LIST
   pageInfo: PageInfo

class parametersForUpdateOrCreateEndpointWithParameters(GQLObject):
   header: headerParametersArray ##LIST
   route: routeParametersArray ##LIST

class updateOrCreateEndpointWithParameters(GQLObject):
   apiVersionId: str
   endpointId: str
   description: str
   method: str
   name: str
   params: parametersForUpdateOrCreateEndpointWithParameters
   patternMatch: bool
   payloadModel: payloadModelForUpdateOrCreateEndpointWithParameters
   payloadParameters: payloadParametersForUpdateOrCreateEndpointWithParameters ##LIST
   route: str
   routeregex: str
   displayResponse: bool
   response: str
   responseObject: ResponseObjectInput
   mockResponseId: ID
   mockResponseObject: MockResponseObjectInput
   responsePayloads: PayloadObjectInput ##LIST
   requestPayloads: PayloadObjectInput ##LIST
   group: str
   isGraphQL: bool
   graphQLSchemaObject: GraphQLSchemaCreateInput
   externalDocs: ExternalDocsInput

class EndpointStatsV2(GQLObject):
   endpoint: Endpoint
   stats: EndpointStatsData ##LIST
   apiData: Api

class EndpointStats(GQLObject):
   endpointid: ID
   name: QTCKKname_name_Field
   stats: EndpointStatsData ##LIST
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
   transactions: str ##LIST
   blocked: bool
   apiId: ID
   requests: int
   entity: Entity
   api: Api
   apiVersionId: ID
   billingItems: BillingItem ##LIST

class ConsumerEdge(GQLObject):
   node: Consumer
   cursor: str

class ConsumerConnection(GQLObject):
   nodes: Consumer ##NON NULL
   edges: ConsumerEdge ##LIST
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
   transactions: str ##LIST
   blocked: bool
   apiId: ID
   requests: int
   entity: Entity
   api: Api
   apiVersionId: ID
   billingItems: BillingItem ##LIST

class CollectionItem(GQLObject): 
   pass

class OGLJQapis_CollectionItem_Field(CollectionItem):
   class CollectionItemArgs(GQLArgsSet, GQLObject): 
      apisSkip: int
      apisLimit: int

   _args: CollectionItemArgs



class CollectionV3(GQLObject):
   id: str ##NON NULL
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: OGLJQapis_CollectionItem_Field
   blogPostId: str
   post: BlogPost
   blogPosts: BlogPosts ##LIST
   orderCollectionItems: str ##LIST
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   ownerId: int
   orgId: str
   orgName: str
   collection_type: str

class QCAZEapis_CollectionItem_Field(CollectionItem):
   class CollectionItemArgs(GQLArgsSet, GQLObject): 
      weightLowerThan: int

   _args: CollectionItemArgs



class CollectionV2(GQLObject):
   id: str ##NON NULL
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: QCAZEapis_CollectionItem_Field
   blogPostId: str
   post: BlogPost
   blogPosts: BlogPosts ##LIST
   orderCollectionItems: str ##LIST
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   ownerId: int
   orgId: str
   orgName: str
   collection_type: str

class CDRZMapis_Api_Field(Api):
   class ApiArgs(GQLArgsSet, GQLObject): 
      weightLowerThan: int

   _args: ApiArgs



class Collection(GQLObject):
   id: str ##NON NULL
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: CDRZMapis_Api_Field
   blogPostId: str
   post: BlogPost
   blogPosts: BlogPosts ##LIST
   orderCollectionItems: str ##LIST
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   ownerId: int
   orgId: str
   orgName: str
   collection_type: str

class CategoryEdge(GQLObject):
   node: Category ##NON NULL
   cursor: str ##NON NULL

class CategoryConnection(GQLObject):
   nodes: Category ##NON NULL
   edges: CategoryEdge ##NON NULL
   pageInfo: PageInfo ##NON NULL

class BillingPlanVersionEdge(GQLObject):
   node: BillingPlanVersion
   cursor: str

class BillingPlanVersionConnection(GQLObject):
   nodes: BillingPlanVersion ##LIST
   edges: BillingPlanVersionEdge ##LIST
   pageInfo: PageInfo

class upsertBillingPlanVersionInput(GQLObject):
   billingPlanVersionId: str
   showInMarketplace: bool
   price: float
   planType: str
   rateLimit: RateLimitInputV2
   billingLimits: BillingLimitInputV2 ##LIST
   enableBillingFeatures: EnableBillingFeatureInputV2 ##LIST

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
   enableBillingFeatures: EnableBillingFeatureInput ##LIST
   billingLimits: BillingLimitInput ##LIST

class BillingPlanCreateInput(GQLObject):
   api: str ##NON NULL
   apiName: str ##NON NULL
   apiVersion: str ##NON NULL
   apiVersionName: str ##NON NULL
   providerName: str ##NON NULL
   name: str ##NON NULL
   targetGroup: str
   isPrivatePlan: bool
   isStudent: bool
   legalDocumentId: str
   legalAccountId: str
   shouldRequestApproval: bool
   requestApprovalQuestion: str
   price: float
   type: BillingPlanType ##NON NULL
   rateLimit: RateLimitInput
   enableBillingFeatures: EnableBillingFeatureInput ##LIST
   billingLimits: BillingLimitInput ##NON NULL ##LIST

class BillingItemEdge(GQLObject):
   node: BillingItem
   cursor: str

class BillingItemConnection(GQLObject):
   nodes: BillingItem ##LIST
   edges: BillingItemEdge ##LIST
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
   id: ID ##NON NULL
   ownerId: ID
   category: str
   visibility: ApiVisibility
   termsOfService: ApiTermsOfServiceInput
   description: str
   longDescription: str
   websiteUrl: str
   thumbnail: Upload
   tags: ApiTagValueInput ##LIST
   gatewayIds: ID ##NON NULL ##LIST
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
   nodes: Api ##NON NULL
   edges: ApiEdge ##NON NULL
   pageInfo: PageInfo ##NON NULL
   totalCount: int ##NON NULL

class ApiVersionAccessControlUpdateInput(GQLObject):
   secretParameters: ApiVersionSecretParameterInput ##NON NULL ##LIST

class ApiVersionUpdateInput(GQLObject):
   current: bool
   versionStatus: str
   visibility: Visibility
   apiVersionId: str ##NON NULL
   accessControl: ApiVersionAccessControlUpdateInput
   associatedCertificates: ApiCertificateAssociationTarget ##NON NULL ##LIST

class ApiVersionEdge(GQLObject):
   node: ApiVersion ##NON NULL
   cursor: str ##NON NULL

class ApiVersionConnection(GQLObject):
   nodes: ApiVersion ##LIST
   edges: ApiVersionEdge ##LIST
   pageInfo: PageInfo ##NON NULL

class ZVTJEendpoints_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointArgs



class XTOERgroups_EndpointsGroup_Field(EndpointsGroup):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: EndpointsGroupArgs



class OZZMGheadlines_Headline_Field(Headline):
   class HeadlineArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: HeadlineArgs



class ApiVersionSearch(GQLObject):
   id: ID ##NON NULL
   api: str
   description: str
   longDescription: str
   name: str
   pricing: str
   status: str
   keywords: str ##LIST
   thumbnail: str
   thumbnailSmall: str
   type: str
   createdAt: DateTime
   updatedAt: DateTime
   visibility: str
   webhooks: bool
   websiteUrl: str
   endpoints: ZVTJEendpoints_Endpoint_Field
   groups: XTOERgroups_EndpointsGroup_Field
   headlines: OZZMGheadlines_Headline_Field
   authentication: Authentication

class ApiSearch(GQLObject):
   id: str
   apiType: str
   name: str
   title: str
   description: str
   keywords: str ##LIST
   installsAllTime: int
   installsDaily: int
   thumbnail: str
   thumbnailSmall: str
   rating: int
   categoryName: str
   User: ApiSearchUser
   Ratings: int ##LIST
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
   tags: APITag ##NON NULL

class ReferenceSpotlight(GQLObject):
   id: ID
   url: str
   title: str
   description: str
   thumbnailUrl: str
   display: bool
   weight: int
   apis: Api ##LIST

class ApiReference(GQLObject):
   id: ID
   image: str
   videoId: ID
   headline: str
   features: Feature ##LIST
   spotlights: ReferenceSpotlight ##LIST

class ApiFollowerEdge(GQLObject):
   node: ApiFollower ##NON NULL
   cursor: str ##NON NULL

class ApiFollowerConnection(GQLObject):
   nodes: ApiFollower ##NON NULL
   edges: ApiFollowerEdge ##NON NULL
   pageInfo: PageInfo ##NON NULL

class ApiCertificateEdge(GQLObject):
   node: ApiCertificate ##NON NULL
   cursor: str ##NON NULL

class ApiCertificateConnection(GQLObject):
   nodes: ApiCertificate ##NON NULL
   edges: ApiCertificateEdge ##NON NULL
   pageInfo: PageInfo ##NON NULL

class UserAlertEdge(GQLObject):
   node: UserAlert
   cursor: str

class UserAlertsConnection(GQLObject):
   nodes: UserAlert ##NON NULL
   edges: UserAlertEdge ##LIST
   pageInfo: PageInfo

class GatewayInstanceUpdateInput(GQLObject):
   id: ID ##NON NULL
   apiGatewayCodeTemplateId: int ##NON NULL
   dns: str ##NON NULL
   configurations: GatewayConfigurationUpdateInput
   customMessages: GatewayCustomMessageUpdateInput ##NON NULL ##LIST
   isDefault: bool

class GatewayInstanceCreateInput(GQLObject):
   apiGatewayCodeTemplateId: int ##NON NULL
   dns: str ##NON NULL
   type: GatewayType ##NON NULL
   configurations: GatewayConfigurationCreateInput
   customMessages: GatewayCustomMessageCreateInput ##NON NULL ##LIST
   isDefault: bool

class EventLogEdge(GQLObject):
   cursor: str ##NON NULL
   node: EventLog ##NON NULL

class EventLogConnection(GQLObject):
   edges: EventLogEdge ##LIST
   nodes: EventLog ##LIST
   totalCount: int ##NON NULL
   pageInfo: PageInfo ##NON NULL

class AdminAuditLog(GQLObject):
   id: str ##NON NULL
   action: str ##NON NULL
   eventName: str ##NON NULL
   user: AuditUser ##NON NULL
   auditText: str ##NON NULL
   statusCode: str
   highlight: str ##LIST
   createdAt: DateTime

class AdminAuditLogEdge(GQLObject):
   cursor: str ##NON NULL
   node: AdminAuditLog ##NON NULL

class AdminAuditLogConnection(GQLObject):
   edges: AdminAuditLogEdge ##LIST
   nodes: AdminAuditLog ##LIST
   totalCount: int ##NON NULL
   pageInfo: PageInfo ##NON NULL

class EventConfig(GQLObject):
   id: ID ##NON NULL
   isActive: bool ##NON NULL
   secret: str ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL
   deletedAt: DateTime
   urls: EventUrl ##NON NULL
   types: EventType ##NON NULL

class EventUrlEdge(GQLObject):
   cursor: str ##NON NULL
   node: EventUrl ##NON NULL

class EventUrlConnection(GQLObject):
   edges: EventUrlEdge ##LIST
   nodes: EventUrl ##LIST
   totalCount: int ##NON NULL
   pageInfo: PageInfo ##NON NULL

class GatewayTemplateParamEdge(GQLObject):
   cursor: str ##NON NULL
   node: GatewayTemplateParam ##NON NULL

class GatewayTemplateParamConnection(GQLObject):
   edges: GatewayTemplateParamEdge ##LIST
   nodes: GatewayTemplateParam ##LIST
   totalCount: int ##NON NULL
   pageInfo: PageInfo ##NON NULL

class GwTemplate(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   description: str ##NON NULL
   urlPattern: str ##NON NULL
   status: str
   isCanBeDeleted: bool ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL
   templateParams: GatewayTemplateParam ##LIST

class GatewayInstance(GQLObject):
   id: ID ##NON NULL
   apiGatewayCodeTemplateId: int ##NON NULL
   dns: str
   type: str
   deploymentKey: str
   serviceStatus: str
   status: str ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL
   isDefault: bool
   isCanBeEdited: bool ##NON NULL
   template: GwTemplate ##NON NULL
   configurations: GatewayConfigurations
   customMessages: GatewayCustomMessage ##LIST

class GatewayInstanceEdge(GQLObject):
   cursor: str ##NON NULL
   node: GatewayInstance ##NON NULL

class GatewayInstanceConnection(GQLObject):
   edges: GatewayInstanceEdge ##LIST
   nodes: GatewayInstance ##LIST
   totalCount: int ##NON NULL
   pageInfo: PageInfo ##NON NULL

class GwTemplateEdge(GQLObject):
   cursor: str ##NON NULL
   node: GwTemplate ##NON NULL

class GatewayTemplateConnection(GQLObject):
   edges: GwTemplateEdge ##LIST
   nodes: GwTemplate ##LIST
   totalCount: int ##NON NULL
   pageInfo: PageInfo ##NON NULL

class Extension(GQLObject):
   id: ID ##NON NULL
   name: str
   description: str
   title: str
   url: str
   sourceUrl: str ##NON NULL
   sourceType: str ##NON NULL
   slugifiedKey: str
   isEnabled: bool
   loggedInRequired: bool
   path: str
   extensionConsumers: ExtensionConsumer ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL
   deletedAt: DateTime
   topic: str
   order: int

class EventUrlSortablesInput(GQLObject):
   sortingFields: EventUrlSortablesSortingField ##NON NULL ##LIST

class GatewayInstanceSortingInput(GQLObject):
   sortingFields: GatewayInstanceSortingSortingField ##NON NULL ##LIST

class GatewayTemplateSortingInput(GQLObject):
   sortingFields: GatewayTemplateSortingSortingField ##NON NULL ##LIST

class GatewayTemplateParamSortingInput(GQLObject):
   sortingFields: GatewayTemplateParamsSortingFieldNameSortingField ##NON NULL ##LIST

class AdminAuditLogSortablesInput(GQLObject):
   sortingFields: AdminAuditLogSortablesSortingField ##NON NULL ##LIST

class EventLogSortablesInput(GQLObject):
   sortingFields: EventLogSortablesSortingField ##NON NULL ##LIST

class GatewayTemplateCreateInput(GQLObject):
   name: str ##NON NULL
   description: str ##NON NULL
   urlPattern: str ##NON NULL
   headers: PartialGatewayTemplateParamCreateInput ##NON NULL ##LIST

class GatewayTemplateUpdateInput(GQLObject):
   name: str ##NON NULL
   description: str ##NON NULL
   urlPattern: str ##NON NULL
   id: ID ##NON NULL
   headers: GatewayTemplateParamsUpdateInput ##NON NULL ##LIST

class SEOTag(GQLObject):
   tag: str
   innerBody: str
   attributes: SEOTagAttribute ##LIST

class SEO(GQLObject):
   id: str
   url: str
   description: str
   brand: str
   lang: str
   tags: SEOTag ##LIST

class ApiCertificateCreationResult(GQLObject):
   apiCertificate: ApiCertificate ##NON NULL
   isExpired: bool ##NON NULL

class ApiCertificateOrderByInput(GQLObject):
   sortingFields: ApiCertificateSortingField ##NON NULL ##LIST

class ApiDeveloperInput(GQLObject):
   id: ID
   developer: ID
   status: ApiDeveloperStatus
   user: ApiDeveloperEntityInput

class SaveApiDevelopersInput(GQLObject):
   apiId: ID ##NON NULL
   developers: ApiDeveloperInput ##NON NULL ##LIST

class ApiFollowerOrderByInput(GQLObject):
   fields: ApiFollowerSortingField ##NON NULL ##LIST

class ApiReferenceConnection(GQLObject):
   nodes: ApiReference ##LIST

class ApiSearchPaged(GQLObject):
   results: ApiSearch ##LIST
   total: int

class ApiSpecImportResult(GQLObject):
   apiId: ID ##NON NULL
   trackingId: ID ##NON NULL
   warnings: ApiSpecImportWarning ##NON NULL

class ApiSpecImportProcess(GQLObject):
   trackingId: ID ##NON NULL
   apiId: ID ##NON NULL
   progress: float ##NON NULL
   hasError: bool ##NON NULL
   issues: ApiSpecImportProcessIssue ##NON NULL

class ApiVersionOrderByInput(GQLObject):
   sortingFields: ApiVersionSortingField ##NON NULL ##LIST

class ApiOrderByInput(GQLObject):
   sortingFields: ApiSortingField ##NON NULL ##LIST

class SchemaDefinitionSourceInput(GQLObject):
   type: GqlSchemaSourceType ##NON NULL
   source: str
   options: GqlOptions

class GqlSpecInput(GQLObject):
   baseUrl: str ##NON NULL
   schemaSource: SchemaDefinitionSourceInput ##NON NULL

class SpecInput(GQLObject):
   gql: GqlSpecInput ##NON NULL

class NewApiVersionInput(GQLObject):
   name: str
   spec: SpecInput

class ApiCreateInput(GQLObject):
   name: str ##NON NULL
   pricing: ApiPricing
   description: str ##NON NULL
   category: str ##NON NULL
   visibility: ApiVisibility
   apiType: ApiType
   version: NewApiVersionInput

class ApplicationAuthorization(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   mashapeId: ID
   key: str
   applicationId: ID ##NON NULL
   status: AppAuthorizationStatus ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL
   deletedAt: DateTime
   authorizationType: AppAuthorizationType ##NON NULL
   authorizationValues: str
   gateways: Gateway ##NON NULL
   grantType: AuthorizationGrantType

class ApplicationEnvironment(GQLObject):
   id: ID ##NON NULL
   keyName: str ##NON NULL
   mashapeId: str
   applicationEnvironmentName: EnvironmentName ##NON NULL
   internalKey: str
   key: str
   applicationId: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   resetDate: int
   authorizationType: AuthorizationType ##NON NULL
   authorizationValues: str
   gateways: Gateway ##LIST
   grantType: AuthorizationGrantType

class ApplicationEnvironmentPaging(GQLObject):
   applicationEnvironments: ApplicationEnvironment ##LIST
   totalCount: int

class AsyncApiConfigurationConnection(GQLObject):
   nodes: AsyncApiConfiguration ##LIST

class auditTrails(GQLObject):
   total: int
   audits: audit ##LIST

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
   authParams: AuthenticationParamInput ##LIST
   handleOauthTokenAtFrontend: bool

class createAuthenticationInput(GQLObject):
   apiVersionId: str ##NON NULL
   authentication: authenticationInput ##NON NULL

class AuthenticationCreateOrUpdateResult(GQLObject):
   id: ID
   authParams: AuthenticationParam ##LIST

class AuthenticationCreateInput(GQLObject):
   apiVersionId: ID ##NON NULL
   authType: AuthenticationType ##NON NULL
   description: str
   accessTokenUrl: str
   authorizationUrl: str
   requestTokenUrl: str
   grantType: GrantType
   separator: SeparatorType
   clientAuthentication: ClientAuthenticationType
   clientSecretRequired: bool
   authParams: AuthenticationParamInput ##LIST
   handleOauthTokenAtFrontend: bool

class AuthenticationUpdateInput(GQLObject):
   apiVersionId: ID ##NON NULL
   authType: AuthenticationType
   description: str
   accessTokenUrl: str
   authorizationUrl: str
   requestTokenUrl: str
   grantType: GrantType
   separator: SeparatorType
   clientAuthentication: ClientAuthenticationType
   clientSecretRequired: bool
   authParams: AuthenticationParamInput ##LIST
   handleOauthTokenAtFrontend: bool

class createBillingFeature(GQLObject):
   apiVersionId: str ##NON NULL
   name: str ##NON NULL
   description: str
   billingFeatureEndpoints: billingFeatureEndpointArray ##LIST

class updateBillingFeature(GQLObject):
   name: str
   description: str
   billingFeatureId: str ##NON NULL
   apiVersionId: str ##NON NULL
   billingFeatureEndpoints: billingFeatureEndpointArray ##LIST

class BillingItemUpsertInput(GQLObject):
   apiId: str ##NON NULL
   apiVersionId: str ##NON NULL
   billingItem: upsertBillingItem

class AllowedPlanDevelopersInput(GQLObject):
   id: str
   status: str
   user: PlanDeveloperUserInput

class AllowedPlanDevelopersUpdateInput(GQLObject):
   allowedPlanDevelopers: AllowedPlanDevelopersInput ##LIST
   planId: str ##NON NULL
   apiId: str
   apiVersionId: str

class BillingPlanVersionsResponse(GQLObject):
   data: BillingPlanVersion ##LIST
   totalCount: int ##NON NULL

class BillingPlanVersionWhereInput(GQLObject):
   apiId: ID ##NON NULL
   apiVersionId: ID
   filters: BillingPlanVersionFilters

class CategoryCreateInput(GQLObject):
   information: CategoryTextualDataInput ##NON NULL ##LIST
   thumbnail: str
   pageTitle: str
   weight: int ##NON NULL

class CategoryUpdateInput(GQLObject):
   id: ID ##NON NULL
   information: CategoryTextualDataInput ##NON NULL ##LIST
   thumbnail: str
   pageTitle: str
   weight: int ##NON NULL

class CategoryOrderByInput(GQLObject):
   fields: CategorySortingField ##NON NULL ##LIST

class CollectionsOrderByInput(GQLObject):
   sortingFields: CollectionsSortingField ##NON NULL ##LIST

class CollectionsResponse(GQLObject):
   data: Collection ##LIST
   total: int ##NON NULL

class PaginatedComments(GQLObject):
   data: Comment ##LIST
   total: int

class EntityMetadataInput(GQLObject):
   entityId: ID
   entityAttributes: EntityAttribute ##NON NULL ##LIST

class Consumers(GQLObject):
   count: int
   rows: ConsumersRow ##LIST

class Country(GQLObject):
   code: str
   currency: Currency

class DiscussionObject(GQLObject):
   data: Discussion ##LIST
   total: int

class VersionEndpointStats(GQLObject):
   apiVersionId: ID
   apiVersionName: str
   endpointsStats: EndpointStatsV2 ##LIST

class endpointsWithinDateInput(GQLObject):
   projectId: ID
   apiIds: ID ##LIST
   endpointIds: ID ##LIST
   fromDate: DateTime ##NON NULL
   toDate: DateTime ##NON NULL
   resolution: str ##NON NULL
   filters: StatsFilterBy ##LIST
   timeOffset: int

class EndpointConnection(GQLObject):
   nodes: Endpoint ##NON NULL

class updateEndpointEntity(GQLObject):
   apiId: str
   versionId: str
   endpointId: str
   newData: endpointData
   lang: str

class EndpointsGroupCreateInput(GQLObject):
   name: str ##NON NULL
   apiVersionId: ID ##NON NULL
   index: int ##NON NULL
   description: str
   externalDocs: ExternalDocsInput

class EndpointsGroupUpdateInput(GQLObject):
   id: ID ##NON NULL
   name: str
   index: int
   description: str
   externalDocs: ExternalDocsInput

class EntityMetadataConnection(GQLObject):
   nodes: EntityMetadata ##NON NULL

class EntityMetadataOrderByInput(GQLObject):
   fields: EntityMetadataSortingField ##NON NULL ##LIST

class EntityRoleCreateInput(GQLObject):
   entitiesRoles: EntityRoleInput ##LIST

class EntityRoleOrderByInput(GQLObject):
   sortingFields: EntityRoleSorting ##NON NULL ##LIST

class ApiGatewayConfiguration(GQLObject):
   id: ID
   apiGatewayInstanceId: ID
   configurations: GatewayConfiguration

class KafkaTopics(GQLObject):
   topics: KafkaTopic ##NON NULL
   allowProducingRecords: bool ##NON NULL

class SubscribeOptions(GQLObject):
   customOffset: KafkaOffset
   fromBeginning: bool
   timestamp: str

class MessageCreateInput(GQLObject):
   messageType: MessageType ##NON NULL
   message: MessageInput ##NON NULL

class CreateNewOrganizationInputV4(GQLObject):
   name: str ##NON NULL
   email: str ##NON NULL
   seats: int ##NON NULL
   thumbnail: str
   description: str
   cardToken: str
   recaptcha: str
   users: UsersInvitation ##LIST
   purchasing_power: str
   numofdevs: str
   apis: ID ##LIST

class OrganizationCreateInput(GQLObject):
   name: str ##NON NULL
   email: str ##NON NULL
   seats: int ##NON NULL
   thumbnail: str
   description: str
   cardToken: str
   recaptcha: str
   users: UsersInvitation ##LIST
   purchasing_power: str
   numofdevs: str
   apis: ID ##LIST

class changeApiUsedVersionInput(GQLObject):
   newProjectAllowedApiInput: createProjectAllowedAPIInput
   currentProjectAllowedApiId: int

class VirtualPermissionUpdateInput(GQLObject):
   id: ID ##NON NULL
   key: str
   displayName: str
   permissionLevel: str
   description: str
   dependsOn: int
   rolePermission: RolePermissionUpdateInput ##NON NULL

class RoleCreateInput(GQLObject):
   name: str ##NON NULL
   description: str
   roleLevel: RoleLevel ##NON NULL
   isBasicRole: bool
   isDefault: bool
   permissions: VirtualPermissionUpdateInput ##LIST

class RoleUpdateInput(GQLObject):
   id: ID ##NON NULL
   key: str
   name: str
   description: str
   roleLevel: str
   isBasicRole: bool
   isDefault: bool
   permissions: VirtualPermissionUpdateInput ##NON NULL ##LIST

class RoleOrderByInput(GQLObject):
   sortingFields: RoleSorting ##NON NULL ##LIST

class SearchApiOrderByInput(GQLObject):
   sortingFields: SearchApiSortingField ##NON NULL ##LIST

class SearchCollectionOrderByInput(GQLObject):
   sortingFields: SearchCollectionSortingField ##NON NULL ##LIST

class SpotlightOrderByInput(GQLObject):
   sortingFields: SpotlightSortingField ##NON NULL ##LIST

class SubscribeInput(GQLObject):
   apiId: str ##NON NULL
   billingPlanVersionId: str ##NON NULL
   apiVersionId: str
   ownerId: str ##NON NULL
   legalAgreementMetadata: SubscribeLegalAgreementMetadataInput

class OrgSubscriptions(GQLObject):
   rows: BillingSubscription ##LIST
   count: int

class SubscriptionsWhereInput(GQLObject):
   userId: int
   activeOnly: bool
   id: int
   apiId: str
   mashapeId: str
   pagingArgs: PagingArgs

class SubscriptionCreateInput(GQLObject):
   apiId: str ##NON NULL
   billingPlanVersionId: str ##NON NULL
   ownerId: str ##NON NULL
   apiVersionId: str
   legalAgreementMetadata: SubscribeLegalAgreementMetadataInput

class TargetGroupUpdateInput(GQLObject):
   id: ID ##NON NULL
   loadBalancingStrategy: LoadBalancingStrategy
   targetUrls: TargetUrlUpdateInput ##NON NULL ##LIST

class PaginatedTeamUsers(GQLObject):
   data: TeamUser ##NON NULL
   total: int ##NON NULL
   totalActive: int

class TransactionsSummary(GQLObject):
   totalAmount: float
   transactionsByMonths: TransactionsSummaryMonth ##LIST

class TransformationOrderByInput(GQLObject):
   fields: TransformationSortingField ##NON NULL ##LIST

class TutorialOrderByInput(GQLObject):
   sortingFields: TutorialSortingField ##NON NULL ##LIST

class UsagesStats(GQLObject):
   usage: int ##NON NULL
   period: str ##NON NULL
   parentUsage: int
   teamsUsages: TeamsUsages ##LIST

class OrganizationApiUsagesV2(GQLObject):
   usages: OrgSubscriptionUsage ##LIST

class UserSavedApi(GQLObject):
   id: ID ##NON NULL
   userId: int ##NON NULL
   apiId: str ##NON NULL
   status: int ##NON NULL
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
   data: Workflow ##LIST
   total: int ##NON NULL

class GetWorkflowsOptions(GQLObject):
   topic: WorkflowTopic
   requesteeId: int
   requestorId: int
   componentId: str
   subComponentId: str
   componentDisplayName: str
   workflowStatus: WorkflowStatus ##LIST
   pagingArgs: PagingArgs

class WorkFlowAuditsResponse(GQLObject):
   data: WorkflowAudit ##LIST
   total: int ##NON NULL
