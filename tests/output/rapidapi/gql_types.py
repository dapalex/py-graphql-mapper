from typing import Generic, Union, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
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
   userIds: list[ID]
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
   socialLinks: list[Any]

class SaveUserApi(GQLObject):
   id: ID
   apiId: str
   status: int

class UserInvitesDeleteInput(GQLObject):
   emails: NonNull_list[str]
   orgId: int

class UserInvitesCreateInput(GQLObject):
   email: str
   teamIds: NonNull_list[int]
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
   id: list[ID]
   apiVersionId: list[ID]

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
   plans: NonNull_list[ID]
   endpoints: NonNull_list[ID]

class DeletedTransformation(GQLObject):
   id: ID
   deleted: bool

class updateTransactionInput(GQLObject):
   ids: list[ID]
   paidout: bool
   amount: float

class OrgTransaction(GQLObject):
   invoiceLink: str
   createdAt: str
   totalAmount: float

class TransactionsSummaryWhereInput(GQLObject):
   fromDate: str
   toDate: str
   apiIds: list[ID]
   userIds: list[ID]

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
   """
   loadBalancingStrategyValue - Currently only required when the containing target group's `loadBalancingStrategy` is `GEO_IP`
(otherwise must be `null` or omitted) in which case will represent the origin location of requests to be assigned to the specified `url`.
Value must be an identifier string of either a two-letter continent code (e.g `"AF"` for Africa),
a three-letter country code (e.g `"FRA"` for France) or `"default"`.
It is *required* that exactly one of the identifiers will be set to `"default"` and that the other values given are unique
across all the target URLs.

   """
   url: str
   loadBalancingStrategyValue: str

class TagDefinition(GQLObject):
   """
   editableByProvider - When set to `false`, an API provider themself shouldn't be allowed to apply this tag to an API -
instead, this would be reserved only for tenant admins to perform. Note that setting this attribute to `false` isn't
meant to affect regular visibility of the tags' attachment whatsoever.

   forceEnumValidation - Determines whether the tag definition is acting in a "values are exclusively selected from a predefined set"
mode (when `forceEnumValidation: true`) or a "any arbitrary value can be set freely" mode
(when `forceEnumValidation: false`).

When in the "free" value mode (`forceEnumValidation: false`), the values listed via the `values` attribute act as mere suggestions
that constitute no enforcement. Also, if at any point in time such tag definition is modified to be `forceEnumValidation: true`,
then any arbitrary values set beforehand by providers that aren't listed in `values` would still remain effective and intact.

   isVisible - When setting this to `false`, the tag definition is effectively considered "deactivated" on the platform,
thus it "should" not be allowed to see/attach on their APIs, and in case there were some APIs
associated with it before it was deactivated as said, then in terms of showcasing an API's attached tags -
all instances of this particular one "should" be hidden among the rest.

   requiredOnAPI - Specifies whether this particular tag definition "should" be considered mandatory, requiring every API in the given
tenant to have it attached with at least one of its listed values.

Note that if at any point in time a tag definition's `requiredOnAPI` is updated to whichever state, then all tags currently attached
to actual APIs remain unchanged from that whatsoever.

   showTagName - For when an API's attached tags are being showcased, this attributes is meant to instruct whether the name of
the tag definition should be visually displayed next to every value of it set on an API as it is being showcased,
or otherwise to have just the plain values displayed alone.

   """
   id: str
   color: str
   description: str
   status: str
   type: str
   name: str
   values: list[str]
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
   projectAllowedAPIIds: NonNull_list[int]
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
   messageThreadIds: NonNull_list[int]
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
   entityIds: NonNull_list[int]
   orgId: int
   parentIds: list[int]

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
   options: list[str]
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
   id: NonNull_list[ID]

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
   apiId: NonNull_list[ID]
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
   """
   BillingFeatureEndpoint -  Deprecated, soon to be removed from schema 

   """
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
   apiVersionId: NonNull_list[ID]

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
   """
   ApiWhereInput - Can not act as a single filter, either id, ownerId or subscriberId input must be provided as well.

   ownerId - The owner Id of the API

   visibility - Filter by API visibility

   """
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
   """
   rapidapiProxySecret - Value of the `X-RapidAPI-Proxy-Secret` header that RapidAPI adds on every request.
This header has a unique value for each API.
Only APIs owned by the current user would show the actual value on this. Otherwise, the value would be `null`.

   """
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
   apiIds: list[ID]
   projectIds: list[ID]
   endpointsIds: list[ID]
   apiVersionsIds: list[ID]
   billingPlansIds: list[ID]
   endpointHashes: list[ID]

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
   apiIds: list[ID]
   projectIds: list[ID]
   baseUrl: str
   minNextAlertTime: DateTime
   endpointsIds: list[ID]
   apiVersionsIds: list[ID]
   billingPlansIds: list[ID]
   endpointHashes: list[ID]

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
   """
   EventLog - event log

   """
   id: str
   url: str
   eventType: str
   eventData: str
   eventText: str
   statusCode: str
   highlight: list[str]
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
   """
   EnvConfigCategory - env config category

   """
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

class list_StatsData(list, StatsData): pass

class Stats(GQLObject):
   apiStats: list_StatsData[StatsData]

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

class list_GqlDoc(list, GqlDoc): pass

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
   documentation: list_GqlDoc[GqlDoc]

class RUING_GraphQLSchema_Field(GraphQLSchema):
   class GraphQLSchemaArgs(GQLArgsSet, GQLObject):
      withOverrides: bool

   _args: GraphQLSchemaArgs



class list_RequestPayload(list, RequestPayload): pass

class list_ResponsePayload(list, ResponsePayload): pass

class QBOXY_ResponsePayload_Field(ResponsePayload):
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
   graphQLSchema: RUING_GraphQLSchema_Field
   mockResponseId: ID
   isMockResponse: bool
   summary: str
   externalDocs: ExternalDocs
   endpointHash: str
   appliedOauth2Scopes: AuthenticationParam
   requestPayloads: list_RequestPayload[RequestPayload]
   responsePayloads: list_ResponsePayload[ResponsePayload]
   mockResponse: QBOXY_ResponsePayload_Field

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
   """
   requests - Count of requests made in this context and period

   subscriptionId - `SubscriptionId` might be null if `groupBy` parameter was not passed to the analytics service as value `subscription`

   """
   period: str
   requests: int
   billingItemId: ID
   subscriptionId: ID
   billingItem: NewType('BillingItem', GQLObject) ## Circular Reference for BillingItem

class VYUFE_BillingItemEndpoint_Field(BillingItemEndpoint):
   class BillingItemEndpointArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: BillingItemEndpointArgs



class list_BillingItemEndpoint(list, BillingItemEndpoint): pass

class HOGXN_UsageData_Field(UsageData):
   class UsageDataArgs(GQLArgsSet, GQLObject):
      subscriptionId: NonNull_ID
      fromDate: str
      toDate: str
      resolution: UsageResolution
      orderDir: OrderDirection

   _args: UsageDataArgs



class list_UsageData(list, UsageData): pass

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
   billingitemendpoints: VYUFE_BillingItemEndpoint_Field
   allEndpoints: bool
   usageInSubscription: HOGXN_UsageData_Field

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

class list_usageByBillingItem(list, usageByBillingItem): pass

class SubscriptionUsage(GQLObject):
   mostUsagePercentage: float
   topPercentageLimitedUsage: float
   usageByBillingItem: list_usageByBillingItem[usageByBillingItem]
   pricing: str

class list_UsageItem(list, UsageItem): pass

class UsagePeriodGrouper(GQLObject):
   period: str
   calculated: list_UsageItem[UsageItem]

class Usage(GQLObject):
   quotaId: ID
   quota: int
   title: str
   overChargePrice: float
   period: str
   calculated: list_UsageItem[UsageItem]

class list_Usage(list, Usage): pass

class Usages(GQLObject):
   usage: list_Usage[Usage]
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

class TRUVH_UsagePeriodGrouper_Field(UsagePeriodGrouper):
   class UsagePeriodGrouperArgs(GQLArgsSet, GQLObject):
      billingItemIds: list[NonNull_ID]
      fromDate: str
      toDate: str
      resolution: UsageResolution
      orderDir: OrderDirection

   _args: UsagePeriodGrouperArgs



class list_UsagePeriodGrouper(list, UsagePeriodGrouper): pass

class list_GQLObject(list, GQLObject): pass

class list_Transaction(list, Transaction): pass

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
   usageByBillingItem: TRUVH_UsagePeriodGrouper_Field
   usages: SubscriptionUsage
   parentId: int
   teamsSubscriptions: list_GQLObject[GQLObject] ## Circular Reference for BillingSubscription
   entity: NewType('Entity', GQLObject) ## Circular Reference for Entity
   transactions: list_Transaction[Transaction]

class QOXUK_ApiVersionBillingPlanVersion_Field(ApiVersionBillingPlanVersion):
   class ApiVersionBillingPlanVersionArgs(GQLArgsSet, GQLObject):
      apiVersionId: str
      filters: BillingPlanVersionFilters

   _args: ApiVersionBillingPlanVersionArgs



class list_ApiVersionBillingPlanVersion(list, ApiVersionBillingPlanVersion): pass

class ETXFQ_BillingLimit_Field(BillingLimit):
   class BillingLimitArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: BillingLimitArgs



class list_BillingLimit(list, BillingLimit): pass

class list_EnableBillingFeature(list, EnableBillingFeature): pass

class list_BillingSubscription(list, BillingSubscription): pass

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
   apiVersionBillingPlanVersion: QOXUK_ApiVersionBillingPlanVersion_Field
   billinglimits: ETXFQ_BillingLimit_Field
   enablebillingfeatures: list_EnableBillingFeature[EnableBillingFeature]
   rateLimit: RateLimit
   subscriptions: list_BillingSubscription[BillingSubscription]
   subscriptionsCount: int

class TargetGroup(GQLObject):
   id: ID
   apiId: ID
   loadBalancingStrategy: LoadBalancingStrategy
   name: str
   targetUrls: TargetUrl

class list_AllowedPlanDeveloper(list, AllowedPlanDeveloper): pass

class JHBVB_BillingPlanVersion_Field(BillingPlanVersion):
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
   allowedPlanDevelopers: list_AllowedPlanDeveloper[AllowedPlanDeveloper]
   allowedPlanDevelopersCount: int
   legalDocumentId: str
   legalAccountId: str
   isStudent: bool
   version: JHBVB_BillingPlanVersion_Field
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

class FVDZH_ResponsePayload_Field(ResponsePayload):
   class ResponsePayloadArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: ResponsePayloadArgs



class GHIAZ_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: EndpointArgs



class list_Endpoint(list, Endpoint): pass

class URXKP_EndpointsGroup_Field(EndpointsGroup):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: EndpointsGroupArgs



class list_EndpointsGroup(list, EndpointsGroup): pass

class FYZTY_Publicdns_Field(Publicdns):
   class PublicdnsArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: PublicdnsArgs



class list_Publicdns(list, Publicdns): pass

class LICGU_BillingPlan_Field(BillingPlan):
   class BillingPlanArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs
      showDeleted: bool
      visibility: Visibility

   _args: BillingPlanArgs



class list_BillingPlan(list, BillingPlan): pass

class HIVLP_BillingItem_Field(BillingItem):
   class BillingItemArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: BillingItemArgs



class list_BillingItem(list, BillingItem): pass

class SYNHO_BillingItemEndpoint_Field(BillingItemEndpoint):
   class BillingItemEndpointArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: BillingItemEndpointArgs



class list_Transformation(list, Transformation): pass

class PCHIH_Asset_Field(Asset):
   class AssetArgs(GQLArgsSet, GQLObject):
      visible: bool

   _args: AssetArgs



class ApiVersion(GQLObject):
   id: ID
   api: str
   current: bool
   name: str
   status: str
   keywords: list[str]
   createdAt: DateTime
   updatedAt: DateTime
   visibility: str
   apiInstance: NewType('Api', GQLObject) ## Circular Reference for Api
   kafkaConfiguration: KafkaConfiguration
   asyncApiConfiguration: AsyncApiConfiguration
   webhooks: bool
   payloads: FVDZH_ResponsePayload_Field
   accessControl: ApiVersionAccessControlInfo
   endpoints: GHIAZ_Endpoint_Field
   groups: URXKP_EndpointsGroup_Field
   publicdns: FYZTY_Publicdns_Field
   billingplans: LICGU_BillingPlan_Field
   billingitems: HIVLP_BillingItem_Field
   billingitemendpoints: SYNHO_BillingItemEndpoint_Field
   publicBillingPlanVersions: list_ApiVersionBillingPlanVersion[ApiVersionBillingPlanVersion]
   targetGroup: TargetGroup
   targetGroupId: str
   transformations: list_Transformation[Transformation]
   versionStatus: VersionStatus
   apiSubType: apiSubTypeEnum
   associatedApiCertificates: ApiCertificateAssociation
   assets: PCHIH_Asset_Field
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

class ZIJAW_Comment_Field(Comment):
   class CommentArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: CommentArgs



class list_Comment(list, Comment): pass

class AVUIL_Comment_Field(Comment):
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
   comments: ZIJAW_Comment_Field
   commentsV2: AVUIL_Comment_Field
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

class EDMWU_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject):
      showDeleted: bool

   _args: EndpointArgs



class RequestLog(GQLObject):
   requestId: ID
   projectId: ID
   api: str
   apiId: ID
   endpoint: str
   endpointObject: EDMWU_Endpoint_Field
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

class list_RequestLog(list, RequestLog): pass

class RequestLogsResult(GQLObject):
   """
   totalCount - Total count of requests matching supplied `fromDate`, `toDate` and `filters`, **regardless of pagination**.
This is not *the mere count of items in the sibling `requests` field*."

   """
   requests: list_RequestLog[RequestLog]
   totalCount: int

class list_FollowApi(list, FollowApi): pass

class XWBQR_Issue_Field(Issue):
   class IssueArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: IssueArgs



class list_Issue(list, Issue): pass

class list_Spotlight(list, Spotlight): pass

class ZNINK_Announcement_Field(Announcement):
   class AnnouncementArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: AnnouncementArgs



class list_Announcement(list, Announcement): pass

class CJVTS_ApiDeveloper_Field(ApiDeveloper):
   class ApiDeveloperArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: ApiDeveloperArgs



class list_ApiDeveloper(list, ApiDeveloper): pass

class list_TargetGroup(list, TargetGroup): pass

class list_ApiVersion(list, ApiVersion): pass

class MESAV_Headline_Field(Headline):
   class HeadlineArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: HeadlineArgs



class list_Headline(list, Headline): pass

class NOEVE_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: EndpointArgs



class QXFQU_BillingFeature_Field(BillingFeature):
   class BillingFeatureArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: BillingFeatureArgs



class list_BillingFeature(list, BillingFeature): pass

class RYJRL_BillingItem_Field(BillingItem):
   class BillingItemArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: BillingItemArgs



class LTDMI_BillingPlan_Field(BillingPlan):
   class BillingPlanArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: BillingPlanArgs



class OTJBI_RequestLogsResult_Field(RequestLogsResult):
   """
   OTJBI_RequestLogsResult_Field - Raw non-aggregated request logs related to the parent `Api` entity.

   """
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
   """
   Api - Contains information about an API in the API Hub.

   id - The RapidAPI API ID for the API. This can be obtained using the **apis** query.

   externalCustomId - An optional provider-specified custom ID by which the API can be later fetched.
If any external custom ID was set by the API provider, it could then be directly fetched by it as a convenient alternative for the API's basic platform-generated \`id\`, but either one may still be used independently.
`externalCustomId`s are guaranteed to be **unique** among all APIs in the scope of a certain tenant environment.

   name - The API name as displayed in the API Hub.

   requestLogs - Raw non-aggregated request logs related to the parent `Api` entity.

   """
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
   followers: list_FollowApi[FollowApi]
   followersCount: int
   subscriptionsCount: int
   issues: XWBQR_Issue_Field
   rating: apiRating
   slugifiedName: str
   categoryId: str
   allowedContext: list[str]
   spotlights: list_Spotlight[Spotlight]
   patternMatch: bool
   patternMatchAllowOtherTypes: bool
   requestSchemaValidation: bool
   requestSchemaValidationUnknownAttributePolicy: SchemaValidationUnknownAttributePolicy
   gatewayIds: ID
   announcements: ZNINK_Announcement_Field
   apiDevelopers: CJVTS_ApiDeveloper_Field
   targetGroups: list_TargetGroup[TargetGroup]
   publishApiPendingRequest: bool
   saveRequestHeadersLogging: bool
   saveRequestQueryParametersLogging: bool
   saveRequestBodyLogging: bool
   saveResponseHeadersLogging: bool
   saveResponseBodyLogging: bool
   useHttpProxy: bool
   security: ApiSecurityInfo
   versions: list_ApiVersion[ApiVersion]
   headlines: MESAV_Headline_Field
   endpoints: NOEVE_Endpoint_Field
   billingFeatures: QXFQU_BillingFeature_Field
   billingItems: RYJRL_BillingItem_Field
   billingPlans: LTDMI_BillingPlan_Field
   isFavorite: bool
   quality: ApiQuality
   requestLogs: OTJBI_RequestLogsResult_Field

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

class list_Account(list, Account): pass

class DEJUV_ProjectAllowedAPI_Field(ProjectAllowedAPI):
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: ProjectAllowedAPIArgs



class list_ProjectAllowedAPI(list, ProjectAllowedAPI): pass

class EWCZP_RequestLogsResult_Field(RequestLogsResult):
   """
   EWCZP_RequestLogsResult_Field - Raw non-aggregated request logs related to the parent `Project` entity.

   """
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
   """
   requestLogs - Raw non-aggregated request logs related to the parent `Project` entity.

   """
   id: int
   mashapeId: str
   name: str
   description: str
   thumbnail: str
   favorite: bool
   accounts: list_Account[Account]
   xMashapeKey: str
   acl: NewType('ProjectInfo', GQLObject) ## Circular Reference for ProjectInfo
   enableLimitsToAPIs: bool
   projectAllowedAPIs: DEJUV_ProjectAllowedAPI_Field
   requestLogs: EWCZP_RequestLogsResult_Field

class ProjectInfo(GQLObject):
   id: int
   owner: int
   project: int
   user: NewType('User', GQLObject) ## Circular Reference for User
   entity: NewType('Entity', GQLObject) ## Circular Reference for Entity
   Project: Project

class SubscriptionsPaging(GQLObject):
   subscriptions: list_BillingSubscription[BillingSubscription]
   totalCount: int

class TransactionsPaging(GQLObject):
   transactions: list_Transaction[Transaction]
   totalCount: int

class TransactionsGraphData(GQLObject):
   prev: TransactionsItem
   curr: TransactionsItem
   overages: TransactionsItem

class list_UserAttributesRow(list, UserAttributesRow): pass

class UserAttributes(GQLObject):
   count: int
   rows: list_UserAttributesRow[UserAttributesRow]

class list_EnvelopeDocument(list, EnvelopeDocument): pass

class EnvelopeTemplate(GQLObject):
   documents: list_EnvelopeDocument[EnvelopeDocument]
   templateId: str
   uri: str
   created: DateTime
   name: str
   description: str

class list_EnvelopeTemplate(list, EnvelopeTemplate): pass

class Template(GQLObject):
   envelopeTemplates: list_EnvelopeTemplate[EnvelopeTemplate]

class DocuSignAccount(GQLObject):
   id: str
   name: str
   baseUri: str
   template: Template

class list_DocuSignAccount(list, DocuSignAccount): pass

class DocuSignUserInfo(GQLObject):
   name: str
   email: str
   accounts: list_DocuSignAccount[DocuSignAccount]

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

class list_ProjectInfo(list, ProjectInfo): pass

class AKAUD_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs
      isStripeId: bool
      getAllSubscriptions: bool

   _args: BillingSubscriptionArgs



class UQLHQ_SubscriptionsPaging_Field(SubscriptionsPaging):
   class SubscriptionsPagingArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs
      isStripeId: bool
      getAllSubscriptions: bool

   _args: SubscriptionsPagingArgs



class WKIAX_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_ID

   _args: BillingSubscriptionArgs



class SXQUE_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_ID
      billingPlanVersionId: ID

   _args: BillingSubscriptionArgs



class list_MultipleValuesQueryFilter(list, MultipleValuesQueryFilter): pass

class QueryFilter(GQLObject):
   columnName: str
   operand: str
   value: Any
   values: list_MultipleValuesQueryFilter[MultipleValuesQueryFilter]

class list_QueryFilter(list, QueryFilter): pass

class QueryFilters(GQLObject):
   filters: list_QueryFilter[QueryFilter]

class EAQKN_TransactionsPaging_Field(TransactionsPaging):
   class TransactionsPagingArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs
      apiNameFilter: str
      queryFilters: QueryFilters

   _args: TransactionsPagingArgs



class WQNFD_TransactionsPaging_Field(TransactionsPaging):
   class TransactionsPagingArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs
      apiNameFilter: str
      queryFilters: QueryFilters

   _args: TransactionsPagingArgs



class AWYZV_Transaction_Field(Transaction):
   class TransactionArgs(GQLArgsSet, GQLObject):
      id: ID
      mashapeId: ID

   _args: TransactionArgs



class NonNull_DateTime(DateTime): pass

class XVMIJ_Stats_Field(Stats):
   class StatsArgs(GQLArgsSet, GQLObject):
      apiId: ID
      fromDate: NonNull_DateTime
      toDate: DateTime
      resolution: Resolution
      groupBy: StatsGroupBy

   _args: StatsArgs



class list_Stats(list, Stats): pass

class list_Api(list, Api): pass

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
   followsList: list_GQLObject[GQLObject] ## Circular Reference for FollowUser
   numOfSubscriptions: int
   projectAcls: list_ProjectInfo[ProjectInfo]
   subscriptions: AKAUD_BillingSubscription_Field
   subscriptionsPaging: UQLHQ_SubscriptionsPaging_Field
   activeSubscriptionByApiId: WKIAX_BillingSubscription_Field
   activeSubscriptionByApiIdAndBillingPlanVersionId: SXQUE_BillingSubscription_Field
   pagedTransactions: EAQKN_TransactionsPaging_Field
   notFullyRefundedTransactions: WQNFD_TransactionsPaging_Field
   transactionsGraphData: TransactionsGraphData
   transaction: AWYZV_Transaction_Field
   parents: list_GQLObject[GQLObject] ## Circular Reference for Entity
   stats: XVMIJ_Stats_Field
   billingInformation: BillingInformation
   bio: str
   publishedApisList: list_Api[Api]
   apis: list_Api[Api]
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
   teams: list_GQLObject[GQLObject] ## Circular Reference for Team
   role: str
   token: str
   userData: NewType('User', GQLObject) ## Circular Reference for User
   teamsCount: int

class IssueObject(GQLObject):
   data: list_Issue[Issue]
   total: int

class list_TeamUser(list, TeamUser): pass

class list_ProjectAcl(list, ProjectAcl): pass

class HWRRP_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs
      isStripeId: bool

   _args: BillingSubscriptionArgs



class XINKJ_FollowersUser_Field(FollowersUser):
   class FollowersUserArgs(GQLArgsSet, GQLObject):
      includeUserAttributes: bool

   _args: FollowersUserArgs



class list_FollowersUser(list, FollowersUser): pass

class QQPVA_IssueObject_Field(IssueObject):
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
   users: list_TeamUser[TeamUser]
   ProjectAcls: list_ProjectAcl[ProjectAcl]
   usersCount: int
   description: str
   subscriptions: HWRRP_BillingSubscription_Field
   followersList: XINKJ_FollowersUser_Field
   publishedApisList: list_Api[Api]
   isTeamMember: bool
   issues: QQPVA_IssueObject_Field

class list_Team(list, Team): pass

class EPWAK_FollowersUser_Field(FollowersUser):
   class FollowersUserArgs(GQLArgsSet, GQLObject):
      includeUserAttributes: bool

   _args: FollowersUserArgs



class TIFPW_IssueObject_Field(IssueObject):
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
   teams: list_Team[Team]
   publishedApisList: list_Api[Api]
   users: list_GQLObject[GQLObject] ## Circular Reference for User
   followersList: EPWAK_FollowersUser_Field
   isOrganizationAdmin: bool
   apisCount: int
   internalSubscriptionsCount: int
   externalSubscriptionsCount: int
   issues: TIFPW_IssueObject_Field
   billingAdditionalValues: BillingAdditionalValues
   payoutInfo: PayoutInfo
   balance: float
   occupiedSeats: int
   entity: Any
   seatsBillingInformation: SeatsBillingInformation
   billingType: str

class list_StatsFilterBy(list, StatsFilterBy): pass

class PSNMG_Stats_Field(Stats):
   class StatsArgs(GQLArgsSet, GQLObject):
      fromDate: NonNull_str
      toDate: NonNull_str
      resolution: str
      projectId: str
      apiId: str
      groupBy: StatsGroupBy
      filters: list_StatsFilterBy[StatsFilterBy]
      timeOffset: int

   _args: StatsArgs



class KZIPX_FollowersUser_Field(FollowersUser):
   class FollowersUserArgs(GQLArgsSet, GQLObject):
      includeUserAttributes: bool

   _args: FollowersUserArgs



class KPXKK_FollowUser_Field(FollowUser):
   class FollowUserArgs(GQLArgsSet, GQLObject):
      includeUserAttributes: bool

   _args: FollowUserArgs



class list_FollowUser(list, FollowUser): pass

class list_ApiFollower(list, ApiFollower): pass

class list_IssueFollow(list, IssueFollow): pass

class OCDAU_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs
      isStripeId: bool

   _args: BillingSubscriptionArgs



class GCPNG_SubscriptionsPaging_Field(SubscriptionsPaging):
   class SubscriptionsPagingArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs
      isStripeId: bool

   _args: SubscriptionsPagingArgs



class BSUAF_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_ID

   _args: BillingSubscriptionArgs



class JONSZ_BillingSubscription_Field(BillingSubscription):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_ID
      billingPlanVersionId: ID

   _args: BillingSubscriptionArgs



class list_Notification(list, Notification): pass

class GMCLM_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      projectId: ID
      mashapeId: ID

   _args: ProjectArgs



class UPWBS_Project_Field(Project):
   class ProjectArgs(GQLArgsSet, GQLObject):
      projectIds: list[NonNull_ID]
      mashapeIds: list[NonNull_ID]

   _args: ProjectArgs



class list_Project(list, Project): pass

class QBYUT_ProjectInfo_Field(ProjectInfo):
   class ProjectInfoArgs(GQLArgsSet, GQLObject):
      projectId: NonNull_ID

   _args: ProjectInfoArgs



class TKGAO_Transaction_Field(Transaction):
   class TransactionArgs(GQLArgsSet, GQLObject):
      id: ID
      mashapeId: ID

   _args: TransactionArgs



class list_Organization(list, Organization): pass

class list_CorporateDomainOrganization(list, CorporateDomainOrganization): pass

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
   stats: PSNMG_Stats_Field
   apisCount: int
   followersList: KZIPX_FollowersUser_Field
   followsList: KPXKK_FollowUser_Field
   followedApis: list_ApiFollower[ApiFollower]
   followsIssues: list_IssueFollow[IssueFollow]
   followsIssuesV2: list_IssueFollow[IssueFollow]
   subscriptions: OCDAU_BillingSubscription_Field
   subscriptionsPaging: GCPNG_SubscriptionsPaging_Field
   activeSubscriptionByApiId: BSUAF_BillingSubscription_Field
   activeSubscriptionByApiIdAndBillingPlanVersionId: JONSZ_BillingSubscription_Field
   notifications: list_Notification[Notification]
   numOfApisUsed: int
   numOfProjects: int
   numOfSubscriptions: int
   billingInformation: BillingInformation
   allowedPlanDevelopers: list_AllowedPlanDeveloper[AllowedPlanDeveloper]
   payoutInfo: PayoutInfo
   project: GMCLM_Project_Field
   projects: UPWBS_Project_Field
   projectACL: QBYUT_ProjectInfo_Field
   ProjectACLs: list_ProjectInfo[ProjectInfo]
   ProfileInfo: ProfileInfo
   transactionsGraphData: TransactionsGraphData
   transaction: TKGAO_Transaction_Field
   ProjectAcls: list_ProjectAcl[ProjectAcl]
   publishedApisList: list_Api[Api]
   bio: str
   Teams: list_Team[Team]
   organizations: list_Organization[Organization]
   attributes: UserAttributes
   isCurrentUser: bool
   balance: float
   entity: Any
   userEnrichment: UserEnrichment
   corporateDomain: CorporateDomain
   organizationsWithTheSameDomain: list_CorporateDomainOrganization[CorporateDomainOrganization]
   billingType: str
   isUserCreatedBySSO: bool

class list_UsageByTeam(list, UsageByTeam): pass

class OrgSubscriptionUsage(GQLObject):
   id: ID
   name: str
   byOrg: UsageByOrg
   byTeam: list_UsageByTeam[UsageByTeam]

class TutorialEdge(GQLObject):
   node: Tutorial
   cursor: str

class list_Tutorial(list, Tutorial): pass

class list_TutorialEdge(list, TutorialEdge): pass

class TutorialConnection(GQLObject):
   nodes: list_Tutorial[Tutorial]
   edges: list_TutorialEdge[TutorialEdge]
   pageInfo: PageInfo

class TransformationEdge(GQLObject):
   node: Transformation
   cursor: str

class TransformationConnection(GQLObject):
   nodes: Transformation
   edges: TransformationEdge
   pageInfo: PageInfo

class TransactionsWhereInput(GQLObject):
   """
   TransactionsWhereInput -  The Filters for the transactions query. You can either filter by apiIds or by apiOwnerIds, but not both. 

   """
   userId: ID
   apiIds: list[ID]
   apiOwnerIds: list[ID]
   withCharges: bool
   queryFilters: QueryFilters
   pagingArgs: PagingArgs

class TransactionEdge(GQLObject):
   node: Transaction
   cursor: str

class list_TransactionEdge(list, TransactionEdge): pass

class TransactionConnection(GQLObject):
   nodes: list_Transaction[Transaction]
   edges: list_TransactionEdge[TransactionEdge]
   pageInfo: PageInfo
   totalCount: int

class TagDefinitionEdge(GQLObject):
   node: TagDefinition
   cursor: str

class list_TagDefinition(list, TagDefinition): pass

class list_TagDefinitionEdge(list, TagDefinitionEdge): pass

class TagDefinitionConnection(GQLObject):
   nodes: list_TagDefinition[TagDefinition]
   edges: list_TagDefinitionEdge[TagDefinitionEdge]
   pageInfo: PageInfo

class BillingSubscriptionEdge(GQLObject):
   node: BillingSubscription
   cursor: str

class list_BillingSubscriptionEdge(list, BillingSubscriptionEdge): pass

class SubscriptionConnection(GQLObject):
   nodes: list_BillingSubscription[BillingSubscription]
   edges: list_BillingSubscriptionEdge[BillingSubscriptionEdge]
   pageInfo: PageInfo
   totalCount: int

class SpotlightEdge(GQLObject):
   node: Spotlight
   cursor: str

class list_SpotlightEdge(list, SpotlightEdge): pass

class SpotlightConnection(GQLObject):
   nodes: list_Spotlight[Spotlight]
   edges: list_SpotlightEdge[SpotlightEdge]
   pageInfo: PageInfo

class UFJIV_Api_Field(Api):
   class ApiArgs(GQLArgsSet, GQLObject):
      weightLowerThan: int

   _args: ApiArgs



class list_BlogPosts(list, BlogPosts): pass

class SearchCollection(GQLObject):
   id: str
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: UFJIV_Api_Field
   blogPostId: str
   post: BlogPost
   blogPosts: list_BlogPosts[BlogPosts]
   orderCollectionItems: list[str]
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

class list_SearchCollection(list, SearchCollection): pass

class list_SearchConnectionEdge(list, SearchConnectionEdge): pass

class SearchCollectionConnection(GQLObject):
   nodes: list_SearchCollection[SearchCollection]
   edges: list_SearchConnectionEdge[SearchConnectionEdge]
   pageInfo: PageInfo
   total: int

class SearchBlogPostEdge(GQLObject):
   node: SearchBlogPost
   cursor: str

class list_SearchBlogPost(list, SearchBlogPost): pass

class list_SearchBlogPostEdge(list, SearchBlogPostEdge): pass

class SearchBlogPostConnection(GQLObject):
   nodes: list_SearchBlogPost[SearchBlogPost]
   edges: list_SearchBlogPostEdge[SearchBlogPostEdge]
   pageInfo: PageInfo
   total: int

class RSPPL_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: EndpointArgs



class list_APITag(list, APITag): pass

class LYHNI_EndpointsGroup_Field(EndpointsGroup):
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
   keywords: list[str]
   thumbnail: str
   thumbnailSmall: str
   type: str
   createdAt: DateTime
   updatedAt: DateTime
   visibility: str
   webhooks: bool
   websiteUrl: str
   endpoints: RSPPL_Endpoint_Field
   tags: list_APITag[APITag]
   groups: LYHNI_EndpointsGroup_Field
   authentication: Authentication

class SearchApi(GQLObject):
   id: str
   apiType: str
   name: str
   title: str
   description: str
   keywords: list[str]
   installsAllTime: int
   installsDaily: int
   thumbnail: str
   thumbnailSmall: str
   rating: int
   categoryName: str
   User: SearchApiUser
   Ratings: list[int]
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

class list_SearchApi(list, SearchApi): pass

class list_SearchApiEdge(list, SearchApiEdge): pass

class SearchApiConnection(GQLObject):
   """
   took - how long the query takes to return the result.

   """
   nodes: list_SearchApi[SearchApi]
   edges: list_SearchApiEdge[SearchApiEdge]
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

class list_Role(list, Role): pass

class list_RoleEdge(list, RoleEdge): pass

class RoleConnection(GQLObject):
   nodes: list_Role[Role]
   edges: list_RoleEdge[RoleEdge]
   pageInfo: PageInfo

class list_Message(list, Message): pass

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
   messages: list_Message[Message]
   lastMessage: Message
   api: Api
   entity: Entity
   threadEntityStatus: ThreadEntityStatus
   body: str

class list_MessageThread(list, MessageThread): pass

class MessageThreadsObject(GQLObject):
   threads: list_MessageThread[MessageThread]
   messages: list_Message[Message]

class KafkaJSConfigurationInput(GQLObject):
   brokers: NonNull_list[str]
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

class list_Header(list, Header): pass

class GatewayTemplate(GQLObject):
   id: int
   name: str
   description: str
   urlPattern: str
   status: str
   type: str
   headers: list_Header[Header]

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

class list_Gateway(list, Gateway): pass

class list_GatewayEdge(list, GatewayEdge): pass

class GatewayConnection(GQLObject):
   nodes: list_Gateway[Gateway]
   edges: list_GatewayEdge[GatewayEdge]
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

class list_EntityRole(list, EntityRole): pass

class list_EntityRoleEdge(list, EntityRoleEdge): pass

class EntityRoleConnection(GQLObject):
   nodes: list_EntityRole[EntityRole]
   edges: list_EntityRoleEdge[EntityRoleEdge]
   pageInfo: PageInfo

class list_headerParametersArray(list, headerParametersArray): pass

class list_routeParametersArray(list, routeParametersArray): pass

class parametersForUpdateOrCreateEndpointWithParameters(GQLObject):
   header: list_headerParametersArray[headerParametersArray]
   route: list_routeParametersArray[routeParametersArray]

class list_payloadParametersForUpdateOrCreateEndpointWithParameters(list, payloadParametersForUpdateOrCreateEndpointWithParameters): pass

class list_PayloadObjectInput(list, PayloadObjectInput): pass

class updateOrCreateEndpointWithParameters(GQLObject):
   apiVersionId: str
   endpointId: str
   description: str
   method: str
   name: str
   params: parametersForUpdateOrCreateEndpointWithParameters
   patternMatch: bool
   payloadModel: payloadModelForUpdateOrCreateEndpointWithParameters
   payloadParameters: list_payloadParametersForUpdateOrCreateEndpointWithParameters[payloadParametersForUpdateOrCreateEndpointWithParameters]
   route: str
   routeregex: str
   displayResponse: bool
   response: str
   responseObject: ResponseObjectInput
   mockResponseId: ID
   mockResponseObject: MockResponseObjectInput
   responsePayloads: list_PayloadObjectInput[PayloadObjectInput]
   requestPayloads: list_PayloadObjectInput[PayloadObjectInput]
   group: str
   isGraphQL: bool
   graphQLSchemaObject: GraphQLSchemaCreateInput
   externalDocs: ExternalDocsInput

class list_EndpointStatsData(list, EndpointStatsData): pass

class EndpointStatsV2(GQLObject):
   endpoint: Endpoint
   stats: list_EndpointStatsData[EndpointStatsData]
   apiData: Api

class EndpointStats(GQLObject):
   endpointid: ID
   name: YNSOJ_name_Field
   stats: list_EndpointStatsData[EndpointStatsData]
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
   transactions: list[str]
   blocked: bool
   apiId: ID
   requests: int
   entity: Entity
   api: Api
   apiVersionId: ID
   billingItems: list_BillingItem[BillingItem]

class ConsumerEdge(GQLObject):
   node: Consumer
   cursor: str

class list_ConsumerEdge(list, ConsumerEdge): pass

class ConsumerConnection(GQLObject):
   nodes: Consumer
   edges: list_ConsumerEdge[ConsumerEdge]
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
   transactions: list[str]
   blocked: bool
   apiId: ID
   requests: int
   entity: Entity
   api: Api
   apiVersionId: ID
   billingItems: list_BillingItem[BillingItem]

class CollectionItem(GQLObject): 
   pass

class PMWYD_CollectionItem_Field(CollectionItem):
   class CollectionItemArgs(GQLArgsSet, GQLObject):
      apisSkip: int
      apisLimit: int

   _args: CollectionItemArgs



class list_CollectionItem(list, CollectionItem): pass

class CollectionV3(GQLObject):
   id: str
   title: str
   slugifiedKey: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: PMWYD_CollectionItem_Field
   blogPostId: str
   post: BlogPost
   blogPosts: list_BlogPosts[BlogPosts]
   orderCollectionItems: list[str]
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   ownerId: int
   orgId: str
   orgName: str
   collection_type: str

class KBJLS_CollectionItem_Field(CollectionItem):
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
   apis: KBJLS_CollectionItem_Field
   blogPostId: str
   post: BlogPost
   blogPosts: list_BlogPosts[BlogPosts]
   orderCollectionItems: list[str]
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   ownerId: int
   orgId: str
   orgName: str
   collection_type: str

class EXAAX_Api_Field(Api):
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
   apis: EXAAX_Api_Field
   blogPostId: str
   post: BlogPost
   blogPosts: list_BlogPosts[BlogPosts]
   orderCollectionItems: list[str]
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

class list_BillingPlanVersion(list, BillingPlanVersion): pass

class list_BillingPlanVersionEdge(list, BillingPlanVersionEdge): pass

class BillingPlanVersionConnection(GQLObject):
   nodes: list_BillingPlanVersion[BillingPlanVersion]
   edges: list_BillingPlanVersionEdge[BillingPlanVersionEdge]
   pageInfo: PageInfo

class list_BillingLimitInputV2(list, BillingLimitInputV2): pass

class list_EnableBillingFeatureInputV2(list, EnableBillingFeatureInputV2): pass

class upsertBillingPlanVersionInput(GQLObject):
   billingPlanVersionId: str
   showInMarketplace: bool
   price: float
   planType: str
   rateLimit: RateLimitInputV2
   billingLimits: list_BillingLimitInputV2[BillingLimitInputV2]
   enableBillingFeatures: list_EnableBillingFeatureInputV2[EnableBillingFeatureInputV2]

class upsertBillingPlanAndVersionInput(GQLObject):
   apiId: str
   apiName: str
   apiVersionId: str
   apiVersionName: str
   providerName: str
   upsertBillingPlanInput: upsertBillingPlanInput
   upsertBillingPlanVersionInput: upsertBillingPlanVersionInput

class list_EnableBillingFeatureInput(list, EnableBillingFeatureInput): pass

class list_BillingLimitInput(list, BillingLimitInput): pass

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
   enableBillingFeatures: list_EnableBillingFeatureInput[EnableBillingFeatureInput]
   billingLimits: list_BillingLimitInput[BillingLimitInput]

class NonNull_list_BillingLimitInput(list, BillingLimitInput): pass

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
   enableBillingFeatures: list_EnableBillingFeatureInput[EnableBillingFeatureInput]
   billingLimits: NonNull_list_BillingLimitInput[BillingLimitInput]

class BillingItemEdge(GQLObject):
   node: BillingItem
   cursor: str

class list_BillingItemEdge(list, BillingItemEdge): pass

class BillingItemConnection(GQLObject):
   nodes: list_BillingItem[BillingItem]
   edges: list_BillingItemEdge[BillingItemEdge]
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

class list_ApiTagValueInput(list, ApiTagValueInput): pass

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
   tags: list_ApiTagValueInput[ApiTagValueInput]
   gatewayIds: list[ID]
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

class list_ApiVersionSecretParameterInput(list, ApiVersionSecretParameterInput): pass

class ApiVersionAccessControlUpdateInput(GQLObject):
   secretParameters: list_ApiVersionSecretParameterInput[ApiVersionSecretParameterInput]

class list_ApiCertificateAssociationTarget(list, ApiCertificateAssociationTarget): pass

class ApiVersionUpdateInput(GQLObject):
   current: bool
   versionStatus: str
   visibility: Visibility
   apiVersionId: str
   accessControl: ApiVersionAccessControlUpdateInput
   associatedCertificates: list_ApiCertificateAssociationTarget[ApiCertificateAssociationTarget]

class ApiVersionEdge(GQLObject):
   node: ApiVersion
   cursor: str

class list_ApiVersionEdge(list, ApiVersionEdge): pass

class ApiVersionConnection(GQLObject):
   nodes: list_ApiVersion[ApiVersion]
   edges: list_ApiVersionEdge[ApiVersionEdge]
   pageInfo: PageInfo

class GZWDE_Endpoint_Field(Endpoint):
   class EndpointArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: EndpointArgs



class ZNEXW_EndpointsGroup_Field(EndpointsGroup):
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
   keywords: list[str]
   thumbnail: str
   thumbnailSmall: str
   type: str
   createdAt: DateTime
   updatedAt: DateTime
   visibility: str
   webhooks: bool
   websiteUrl: str
   endpoints: GZWDE_Endpoint_Field
   groups: ZNEXW_EndpointsGroup_Field
   authentication: Authentication

class ApiSearch(GQLObject):
   id: str
   apiType: str
   name: str
   title: str
   description: str
   keywords: list[str]
   installsAllTime: int
   installsDaily: int
   thumbnail: str
   thumbnailSmall: str
   rating: int
   categoryName: str
   User: ApiSearchUser
   Ratings: list[int]
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
   apis: list_Api[Api]

class list_Feature(list, Feature): pass

class list_ReferenceSpotlight(list, ReferenceSpotlight): pass

class ApiReference(GQLObject):
   id: ID
   image: str
   videoId: ID
   headline: str
   features: list_Feature[Feature]
   spotlights: list_ReferenceSpotlight[ReferenceSpotlight]

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

class list_UserAlertEdge(list, UserAlertEdge): pass

class UserAlertsConnection(GQLObject):
   nodes: UserAlert
   edges: list_UserAlertEdge[UserAlertEdge]
   pageInfo: PageInfo

class list_GatewayCustomMessageUpdateInput(list, GatewayCustomMessageUpdateInput): pass

class GatewayInstanceUpdateInput(GQLObject):
   id: ID
   apiGatewayCodeTemplateId: int
   dns: str
   configurations: GatewayConfigurationUpdateInput
   customMessages: list_GatewayCustomMessageUpdateInput[GatewayCustomMessageUpdateInput]
   isDefault: bool

class list_GatewayCustomMessageCreateInput(list, GatewayCustomMessageCreateInput): pass

class GatewayInstanceCreateInput(GQLObject):
   apiGatewayCodeTemplateId: int
   dns: str
   type: GatewayType
   configurations: GatewayConfigurationCreateInput
   customMessages: list_GatewayCustomMessageCreateInput[GatewayCustomMessageCreateInput]
   isDefault: bool

class EventLogEdge(GQLObject):
   cursor: str
   node: EventLog

class list_EventLogEdge(list, EventLogEdge): pass

class list_EventLog(list, EventLog): pass

class EventLogConnection(GQLObject):
   edges: list_EventLogEdge[EventLogEdge]
   nodes: list_EventLog[EventLog]
   totalCount: int
   pageInfo: PageInfo

class AdminAuditLog(GQLObject):
   """
   AdminAuditLog - admin audit log

   """
   id: str
   action: str
   eventName: str
   user: AuditUser
   auditText: str
   statusCode: str
   highlight: list[str]
   createdAt: DateTime

class AdminAuditLogEdge(GQLObject):
   cursor: str
   node: AdminAuditLog

class list_AdminAuditLogEdge(list, AdminAuditLogEdge): pass

class list_AdminAuditLog(list, AdminAuditLog): pass

class AdminAuditLogConnection(GQLObject):
   edges: list_AdminAuditLogEdge[AdminAuditLogEdge]
   nodes: list_AdminAuditLog[AdminAuditLog]
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

class list_EventUrlEdge(list, EventUrlEdge): pass

class list_EventUrl(list, EventUrl): pass

class EventUrlConnection(GQLObject):
   edges: list_EventUrlEdge[EventUrlEdge]
   nodes: list_EventUrl[EventUrl]
   totalCount: int
   pageInfo: PageInfo

class GatewayTemplateParamEdge(GQLObject):
   cursor: str
   node: GatewayTemplateParam

class list_GatewayTemplateParamEdge(list, GatewayTemplateParamEdge): pass

class list_GatewayTemplateParam(list, GatewayTemplateParam): pass

class GatewayTemplateParamConnection(GQLObject):
   edges: list_GatewayTemplateParamEdge[GatewayTemplateParamEdge]
   nodes: list_GatewayTemplateParam[GatewayTemplateParam]
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
   templateParams: list_GatewayTemplateParam[GatewayTemplateParam]

class list_GatewayCustomMessage(list, GatewayCustomMessage): pass

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
   customMessages: list_GatewayCustomMessage[GatewayCustomMessage]

class GatewayInstanceEdge(GQLObject):
   cursor: str
   node: GatewayInstance

class list_GatewayInstanceEdge(list, GatewayInstanceEdge): pass

class list_GatewayInstance(list, GatewayInstance): pass

class GatewayInstanceConnection(GQLObject):
   edges: list_GatewayInstanceEdge[GatewayInstanceEdge]
   nodes: list_GatewayInstance[GatewayInstance]
   totalCount: int
   pageInfo: PageInfo

class GwTemplateEdge(GQLObject):
   cursor: str
   node: GwTemplate

class list_GwTemplateEdge(list, GwTemplateEdge): pass

class list_GwTemplate(list, GwTemplate): pass

class GatewayTemplateConnection(GQLObject):
   edges: list_GwTemplateEdge[GwTemplateEdge]
   nodes: list_GwTemplate[GwTemplate]
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

class list_EventUrlSortablesSortingField(list, EventUrlSortablesSortingField): pass

class EventUrlSortablesInput(GQLObject):
   sortingFields: list_EventUrlSortablesSortingField[EventUrlSortablesSortingField]

class list_GatewayInstanceSortingSortingField(list, GatewayInstanceSortingSortingField): pass

class GatewayInstanceSortingInput(GQLObject):
   sortingFields: list_GatewayInstanceSortingSortingField[GatewayInstanceSortingSortingField]

class list_GatewayTemplateSortingSortingField(list, GatewayTemplateSortingSortingField): pass

class GatewayTemplateSortingInput(GQLObject):
   sortingFields: list_GatewayTemplateSortingSortingField[GatewayTemplateSortingSortingField]

class list_GatewayTemplateParamsSortingFieldNameSortingField(list, GatewayTemplateParamsSortingFieldNameSortingField): pass

class GatewayTemplateParamSortingInput(GQLObject):
   sortingFields: list_GatewayTemplateParamsSortingFieldNameSortingField[GatewayTemplateParamsSortingFieldNameSortingField]

class list_AdminAuditLogSortablesSortingField(list, AdminAuditLogSortablesSortingField): pass

class AdminAuditLogSortablesInput(GQLObject):
   sortingFields: list_AdminAuditLogSortablesSortingField[AdminAuditLogSortablesSortingField]

class list_EventLogSortablesSortingField(list, EventLogSortablesSortingField): pass

class EventLogSortablesInput(GQLObject):
   sortingFields: list_EventLogSortablesSortingField[EventLogSortablesSortingField]

class list_PartialGatewayTemplateParamCreateInput(list, PartialGatewayTemplateParamCreateInput): pass

class GatewayTemplateCreateInput(GQLObject):
   name: str
   description: str
   urlPattern: str
   headers: list_PartialGatewayTemplateParamCreateInput[PartialGatewayTemplateParamCreateInput]

class list_GatewayTemplateParamsUpdateInput(list, GatewayTemplateParamsUpdateInput): pass

class GatewayTemplateUpdateInput(GQLObject):
   name: str
   description: str
   urlPattern: str
   id: ID
   headers: list_GatewayTemplateParamsUpdateInput[GatewayTemplateParamsUpdateInput]

class list_SEOTagAttribute(list, SEOTagAttribute): pass

class SEOTag(GQLObject):
   tag: str
   innerBody: str
   attributes: list_SEOTagAttribute[SEOTagAttribute]

class list_SEOTag(list, SEOTag): pass

class SEO(GQLObject):
   id: str
   url: str
   description: str
   brand: str
   lang: str
   tags: list_SEOTag[SEOTag]

class ApiCertificateCreationResult(GQLObject):
   apiCertificate: ApiCertificate
   isExpired: bool

class list_ApiCertificateSortingField(list, ApiCertificateSortingField): pass

class ApiCertificateOrderByInput(GQLObject):
   sortingFields: list_ApiCertificateSortingField[ApiCertificateSortingField]

class ApiDeveloperInput(GQLObject):
   id: ID
   developer: ID
   status: ApiDeveloperStatus
   user: ApiDeveloperEntityInput

class NonNull_list_ApiDeveloperInput(list, ApiDeveloperInput): pass

class SaveApiDevelopersInput(GQLObject):
   apiId: ID
   developers: NonNull_list_ApiDeveloperInput[ApiDeveloperInput]

class list_ApiFollowerSortingField(list, ApiFollowerSortingField): pass

class ApiFollowerOrderByInput(GQLObject):
   fields: list_ApiFollowerSortingField[ApiFollowerSortingField]

class list_ApiReference(list, ApiReference): pass

class ApiReferenceConnection(GQLObject):
   nodes: list_ApiReference[ApiReference]

class list_ApiSearch(list, ApiSearch): pass

class ApiSearchPaged(GQLObject):
   results: list_ApiSearch[ApiSearch]
   total: int

class ApiSpecImportResult(GQLObject):
   apiId: ID
   trackingId: ID
   warnings: ApiSpecImportWarning

class ApiSpecImportProcess(GQLObject):
   """
   progress - Current progress of the import process - ranges from `0` to `1` and all that's in between. When a progress of `1` is reached having occurred no issues of severity `ERROR` - it means the API has been fully imported.

   hasError - If `true` - indicates that one or more issues with severity of `ERROR` had occurred

   """
   trackingId: ID
   apiId: ID
   progress: float
   hasError: bool
   issues: ApiSpecImportProcessIssue

class list_ApiVersionSortingField(list, ApiVersionSortingField): pass

class ApiVersionOrderByInput(GQLObject):
   sortingFields: list_ApiVersionSortingField[ApiVersionSortingField]

class list_ApiSortingField(list, ApiSortingField): pass

class ApiOrderByInput(GQLObject):
   sortingFields: list_ApiSortingField[ApiSortingField]

class SchemaDefinitionSourceInput(GQLObject):
   """
   SchemaDefinitionSourceInput - Provide the schema definition source

   """
   type: GqlSchemaSourceType
   source: str
   options: GqlOptions

class GqlSpecInput(GQLObject):
   baseUrl: str
   schemaSource: SchemaDefinitionSourceInput

class SpecInput(GQLObject):
   gql: GqlSpecInput

class NewApiVersionInput(GQLObject):
   """
   spec - provide api specifications to fully define the api's current version

   """
   name: str
   spec: SpecInput

class ApiCreateInput(GQLObject):
   """
   externalCustomId - An optional user-selected custom ID to attach to the created API by which it can be later fetched.
Value must be **unique** among all APIs in the current tenant.
Will serve as a convenient alternative for the API's basic platform-generated \`id\`, but either one may still be used independently.

   """
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
   gateways: list_Gateway[Gateway]
   grantType: AuthorizationGrantType

class list_ApplicationEnvironment(list, ApplicationEnvironment): pass

class ApplicationEnvironmentPaging(GQLObject):
   applicationEnvironments: list_ApplicationEnvironment[ApplicationEnvironment]
   totalCount: int

class list_AsyncApiConfiguration(list, AsyncApiConfiguration): pass

class AsyncApiConfigurationConnection(GQLObject):
   nodes: list_AsyncApiConfiguration[AsyncApiConfiguration]

class list_audit(list, audit): pass

class auditTrails(GQLObject):
   total: int
   audits: list_audit[audit]

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

class list_AuthenticationParamInput(list, AuthenticationParamInput): pass

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
   authParams: list_AuthenticationParamInput[AuthenticationParamInput]
   handleOauthTokenAtFrontend: bool

class createAuthenticationInput(GQLObject):
   apiVersionId: str
   authentication: authenticationInput

class list_AuthenticationParam(list, AuthenticationParam): pass

class AuthenticationCreateOrUpdateResult(GQLObject):
   id: ID
   authParams: list_AuthenticationParam[AuthenticationParam]

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
   authParams: list_AuthenticationParamInput[AuthenticationParamInput]
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
   authParams: list_AuthenticationParamInput[AuthenticationParamInput]
   handleOauthTokenAtFrontend: bool

class list_billingFeatureEndpointArray(list, billingFeatureEndpointArray): pass

class createBillingFeature(GQLObject):
   apiVersionId: str
   name: str
   description: str
   billingFeatureEndpoints: list_billingFeatureEndpointArray[billingFeatureEndpointArray]

class updateBillingFeature(GQLObject):
   name: str
   description: str
   billingFeatureId: str
   apiVersionId: str
   billingFeatureEndpoints: list_billingFeatureEndpointArray[billingFeatureEndpointArray]

class BillingItemUpsertInput(GQLObject):
   apiId: str
   apiVersionId: str
   billingItem: upsertBillingItem

class AllowedPlanDevelopersInput(GQLObject):
   id: str
   status: str
   user: PlanDeveloperUserInput

class list_AllowedPlanDevelopersInput(list, AllowedPlanDevelopersInput): pass

class AllowedPlanDevelopersUpdateInput(GQLObject):
   allowedPlanDevelopers: list_AllowedPlanDevelopersInput[AllowedPlanDevelopersInput]
   planId: str
   apiId: str
   apiVersionId: str

class BillingPlanVersionsResponse(GQLObject):
   data: list_BillingPlanVersion[BillingPlanVersion]
   totalCount: int

class BillingPlanVersionWhereInput(GQLObject):
   apiId: ID
   apiVersionId: ID
   filters: BillingPlanVersionFilters

class NonNull_list_CategoryTextualDataInput(list, CategoryTextualDataInput): pass

class CategoryCreateInput(GQLObject):
   information: NonNull_list_CategoryTextualDataInput[CategoryTextualDataInput]
   thumbnail: str
   pageTitle: str
   weight: int

class CategoryUpdateInput(GQLObject):
   id: ID
   information: NonNull_list_CategoryTextualDataInput[CategoryTextualDataInput]
   thumbnail: str
   pageTitle: str
   weight: int

class list_CategorySortingField(list, CategorySortingField): pass

class CategoryOrderByInput(GQLObject):
   fields: list_CategorySortingField[CategorySortingField]

class list_CollectionsSortingField(list, CollectionsSortingField): pass

class CollectionsOrderByInput(GQLObject):
   sortingFields: list_CollectionsSortingField[CollectionsSortingField]

class list_Collection(list, Collection): pass

class CollectionsResponse(GQLObject):
   data: list_Collection[Collection]
   total: int

class PaginatedComments(GQLObject):
   data: list_Comment[Comment]
   total: int

class NonNull_list_EntityAttribute(list, EntityAttribute): pass

class EntityMetadataInput(GQLObject):
   entityId: ID
   entityAttributes: NonNull_list_EntityAttribute[EntityAttribute]

class list_ConsumersRow(list, ConsumersRow): pass

class Consumers(GQLObject):
   count: int
   rows: list_ConsumersRow[ConsumersRow]

class Country(GQLObject):
   code: str
   currency: Currency

class list_Discussion(list, Discussion): pass

class DiscussionObject(GQLObject):
   data: list_Discussion[Discussion]
   total: int

class list_EndpointStatsV2(list, EndpointStatsV2): pass

class VersionEndpointStats(GQLObject):
   apiVersionId: ID
   apiVersionName: str
   endpointsStats: list_EndpointStatsV2[EndpointStatsV2]

class endpointsWithinDateInput(GQLObject):
   projectId: ID
   apiIds: list[ID]
   endpointIds: list[ID]
   fromDate: DateTime
   toDate: DateTime
   resolution: str
   filters: list_StatsFilterBy[StatsFilterBy]
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

class list_EntityMetadataSortingField(list, EntityMetadataSortingField): pass

class EntityMetadataOrderByInput(GQLObject):
   fields: list_EntityMetadataSortingField[EntityMetadataSortingField]

class list_EntityRoleInput(list, EntityRoleInput): pass

class EntityRoleCreateInput(GQLObject):
   entitiesRoles: list_EntityRoleInput[EntityRoleInput]

class NonNull_list_EntityRoleSorting(list, EntityRoleSorting): pass

class EntityRoleOrderByInput(GQLObject):
   sortingFields: NonNull_list_EntityRoleSorting[EntityRoleSorting]

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

class list_UsersInvitation(list, UsersInvitation): pass

class CreateNewOrganizationInputV4(GQLObject):
   name: str
   email: str
   seats: int
   thumbnail: str
   description: str
   cardToken: str
   recaptcha: str
   users: list_UsersInvitation[UsersInvitation]
   purchasing_power: str
   numofdevs: str
   apis: list[ID]

class OrganizationCreateInput(GQLObject):
   name: str
   email: str
   seats: int
   thumbnail: str
   description: str
   cardToken: str
   recaptcha: str
   users: list_UsersInvitation[UsersInvitation]
   purchasing_power: str
   numofdevs: str
   apis: list[ID]

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

class list_VirtualPermissionUpdateInput(list, VirtualPermissionUpdateInput): pass

class RoleCreateInput(GQLObject):
   name: str
   description: str
   roleLevel: RoleLevel
   isBasicRole: bool
   isDefault: bool
   permissions: list_VirtualPermissionUpdateInput[VirtualPermissionUpdateInput]

class NonNull_list_VirtualPermissionUpdateInput(list, VirtualPermissionUpdateInput): pass

class RoleUpdateInput(GQLObject):
   id: ID
   key: str
   name: str
   description: str
   roleLevel: str
   isBasicRole: bool
   isDefault: bool
   permissions: NonNull_list_VirtualPermissionUpdateInput[VirtualPermissionUpdateInput]

class list_RoleSorting(list, RoleSorting): pass

class RoleOrderByInput(GQLObject):
   sortingFields: list_RoleSorting[RoleSorting]

class list_SearchApiSortingField(list, SearchApiSortingField): pass

class SearchApiOrderByInput(GQLObject):
   sortingFields: list_SearchApiSortingField[SearchApiSortingField]

class list_SearchCollectionSortingField(list, SearchCollectionSortingField): pass

class SearchCollectionOrderByInput(GQLObject):
   sortingFields: list_SearchCollectionSortingField[SearchCollectionSortingField]

class list_SpotlightSortingField(list, SpotlightSortingField): pass

class SpotlightOrderByInput(GQLObject):
   sortingFields: list_SpotlightSortingField[SpotlightSortingField]

class SubscribeInput(GQLObject):
   apiId: str
   billingPlanVersionId: str
   apiVersionId: str
   ownerId: str
   legalAgreementMetadata: SubscribeLegalAgreementMetadataInput

class OrgSubscriptions(GQLObject):
   rows: list_BillingSubscription[BillingSubscription]
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

class list_TargetUrlUpdateInput(list, TargetUrlUpdateInput): pass

class TargetGroupUpdateInput(GQLObject):
   id: ID
   loadBalancingStrategy: LoadBalancingStrategy
   targetUrls: list_TargetUrlUpdateInput[TargetUrlUpdateInput]

class PaginatedTeamUsers(GQLObject):
   data: TeamUser
   total: int
   totalActive: int

class list_TransactionsSummaryMonth(list, TransactionsSummaryMonth): pass

class TransactionsSummary(GQLObject):
   totalAmount: float
   transactionsByMonths: list_TransactionsSummaryMonth[TransactionsSummaryMonth]

class list_TransformationSortingField(list, TransformationSortingField): pass

class TransformationOrderByInput(GQLObject):
   fields: list_TransformationSortingField[TransformationSortingField]

class list_TutorialSortingField(list, TutorialSortingField): pass

class TutorialOrderByInput(GQLObject):
   sortingFields: list_TutorialSortingField[TutorialSortingField]

class list_TeamsUsages(list, TeamsUsages): pass

class UsagesStats(GQLObject):
   usage: int
   period: str
   parentUsage: int
   teamsUsages: list_TeamsUsages[TeamsUsages]

class list_OrgSubscriptionUsage(list, OrgSubscriptionUsage): pass

class OrganizationApiUsagesV2(GQLObject):
   usages: list_OrgSubscriptionUsage[OrgSubscriptionUsage]

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

class list_Workflow(list, Workflow): pass

class WorkFlowsResponse(GQLObject):
   data: list_Workflow[Workflow]
   total: int

class GetWorkflowsOptions(GQLObject):
   topic: WorkflowTopic
   requesteeId: int
   requestorId: int
   componentId: str
   subComponentId: str
   componentDisplayName: str
   workflowStatus: list[WorkflowStatus]
   pagingArgs: PagingArgs

class list_WorkflowAudit(list, WorkflowAudit): pass

class WorkFlowAuditsResponse(GQLObject):
   data: list_WorkflowAudit[WorkflowAudit]
   total: int
