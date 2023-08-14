from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class UFTQJ_name_Field(ArguedStr):
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
   id: str
   currentPassword: str
   newPassword: str
   name: str
   company: str
   position: str
   location: str
   bio: str
   imageFile: str
   email: str
   status: str

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

class UpdateUserResult(GQLObject):
   status: str

class SaveUserApi(GQLObject):
   id: ID
   apiId: str
   status: int

class UserInvitesDeleteInput(GQLObject):
   emails: list[str]
   orgId: int

class UserInvitesCreateInput(GQLObject):
   email: str
   teamIds: list[int]
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
   plans: list[ID]
   endpoints: list[ID]

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

class TenantPricingPlan(GQLObject):
   id: int
   name: str
   contentDescription: JSONObject
   price: float
   currency: str
   billingPlanId: str
   trialPeriod: int
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   displayName: str

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

class ActiveSubscriptionCount(GQLObject):
   date: str
   count: int

class AdditionalSubscriptionProviderData(GQLObject):
   subscriptionTrialEnd: DateTime
   cancelAt: DateTime
   canceledAt: DateTime
   startDate: DateTime
   endedAt: DateTime
   currentPeriodStart: DateTime
   currentPeriodEnd: DateTime

class SubscriptionQuotaUsage(GQLObject):
   id: ID
   limit: int
   subscriptionId: ID
   billingCycleStart: DateTime
   billingCycleEnd: DateTime
   quotaId: ID
   total: int
   period: Period

class SpotlightWhereInput(GQLObject):
   id: ID
   apiId: ID
   type: SpotlightType
   weight: int
   published: bool
   title: str
   description: str
   spotlightURL: str
   status: str
   slugifiedName: str
   thumbnailURL: str
   updatedAt: DateTime
   createdAt: DateTime

class SpotlightUpdateInput(GQLObject):
   id: ID
   apiId: ID
   type: SpotlightType
   weight: int
   published: bool
   title: str
   description: str
   spotlightURL: str
   file: Upload

class SecretParameter(GQLObject):
   id: ID
   placement: SecretParameterPlacement
   name: str
   value: str
   description: str

class createSecretDataInput(GQLObject):
   apiVersionId: str
   url: str
   secret: str

class SearchCollectionWhereInput(GQLObject):
   term: str
   locale: Locale

class SearchBlogPost(GQLObject):
   slugifiedName: str
   title: str
   link: str
   readTime: str
   thumbnail: str
   description: str
   updatedAt: DateTime

class SearchApiWhereInput(GQLObject):
   categoryNames: list[str]
   exclude: list[str]
   term: str
   tags: list[Any]
   collectionIds: list[str]
   privateApisJwt: str
   pricing: list[ApiPricing]
   locale: Locale

class Score(GQLObject):
   apiId: str
   avgSuccessRate: int
   avgServiceLevel: int
   avgLatency: int
   popularityScore: float

class RoleWhereInput(GQLObject):
   roleLevels: list[RoleLevel]

class RequestLogsOnApiFilters(GQLObject):
   projectIds: list[ID]
   endpoints: list[str]
   httpMethods: list[HttpMethod]
   httpStatuses: list[int]
   originIps: list[str]

class RapidReasonInput(GQLObject):
   consumerUserId: int
   providerUserId: int
   externalId: Any
   eventType: RapidReasonsEvents
   reasonType: UnsubscribeReasons
   reasonComments: str
   apiId: str
   apiVersionId: str

class updateProjectAllowedAPIInput(GQLObject):
   id: int
   projectId: int
   apiId: str
   apiVersionId: str
   mashapeId: str

class ProjectUpdateInput(GQLObject):
   projectId: ID
   projectName: str
   projectDescription: str
   thumbnail: Upload
   enableLimitsToAPIs: bool

class EditProjectInput(GQLObject):
   projectId: ID
   projectName: str
   projectDescription: str
   thumbnail: Upload
   enableLimitsToAPIs: bool

class AddProjectInput(GQLObject):
   projectOwner: ID
   projectName: str
   description: str
   thumbnail: Upload
   billing: str

class ValidateTokenResponse(GQLObject):
   status: int
   isValid: bool
   took: int

class CorporateDomainOrganization(GQLObject):
   organizationId: ID
   members: int
   thumbnail: str
   orgname: str

class OrganizationUpdateInput(GQLObject):
   organizationId: int
   name: str
   email: str
   seats: int
   thumbnail: str
   description: str

class OrganizationWhereInput(GQLObject):
   userId: ID
   slugifiedName: str

class AdminOwnerProject(GQLObject):
   email: str
   id: int
   mashapeId: str
   name: str
   slugifiedName: str
   status: str
   thumbnail: str
   type: str

class MarkNotificationsAsReadInput(GQLObject):
   userId: str
   createdAt: str

class MarkNewNotificationAsViewedInput(GQLObject):
   notificationsIds: list[int]
   isNew: bool

class NewNotification(GQLObject):
   id: int
   userId: int
   type: str
   createdAt: DateTime
   updatedAt: DateTime
   isRead: bool
   isNew: bool
   title: str
   body: str
   callToAction: str
   image: str
   any: str

class SendMessageInput(GQLObject):
   fromEmail: str
   toEmail: str
   toId: str
   title: str
   body: str
   apiName: str
   apiId: str
   type: str

class MessageInput(GQLObject):
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

class MessagesWhereInput(GQLObject):
   messageThreadId: ID

class RelativeARTResponse(GQLObject):
   currentProviderAverage: float
   allProvidersAverage: float

class LogPayload(GQLObject):
   requestid: ID
   reqpayload: Any

class CreateLegalAgreementInfo(GQLObject):
   refreshToken: str
   accessToken: str
   vendor: str

class EnvelopeDocument(GQLObject):
   documentId: str
   uri: str
   name: str
   order: int

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
   headlineId: str
   text: str
   textModified: bool

class Headline(GQLObject):
   text: str
   id: str
   status: str
   index: int
   title: str
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
   entityIds: list[int]
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
   id: list[ID]

class EndpointStatsData(GQLObject):
   date: str
   requests: int
   errors: int
   latency: float
   endpointid: ID

class IssueDeleteInput(GQLObject):
   issueId: int

class IssuesDeleteInput(GQLObject):
   issueIds: list[int]

class Currency(GQLObject):
   code: str
   name: str
   symbol: str
   symbol_native: str
   decimal_digits: int
   rakuten_symbol: Any

class ContactAdminSubscribeToAPIEvent(GQLObject):
   api_name: str
   api_link: str
   team_id: int
   org_id: int
   consumer_name: str
   email: str
   plan_name: str
   plan_price: int

class ConsumerQuota(GQLObject):
   limit: int
   period: str
   quotaId: str
   title: str
   total: float
   billingCycleStart: DateTime

class PaginationInput(GQLObject):
   """
   first - Returns the first n elements from the list.

   after - Returns the elements in the list that come after the specified cursor.

   last - Returns the last n elements from the list.

   before - Returns the elements in the list that come before the specified cursor.

   """
   first: int
   after: str
   last: int
   before: str

class Follower(GQLObject):
   startFollowDate: str
   id: int
   email: str
   username: str

class PagingArgs(GQLObject):
   offset: int
   limit: int
   orderBy: str
   orderDirection: OrderDirection
   searchTerm: str

class CommentDeleteInput(GQLObject):
   issueId: int
   commentId: int

class CommentCreateInput(GQLObject):
   body: str
   issueId: int

class CollectionUpdateInput(GQLObject):
   id: ID
   title: str
   weight: float
   shortDescription: str
   longDescription: str
   thumbnail: str
   apis: list[ID]
   ownerId: int

class BlogPosts(GQLObject):
   id: str
   link: str
   type: str
   title: str
   thumbnail: str
   image: str

class CollectionsWhereInput(GQLObject):
   ownerId: str
   isByOwner: bool
   collectionType: str

class CategoryWhereInput(GQLObject):
   id: list[ID]
   name: list[str]
   language: CategoryLanguage
   slugifiedName: list[str]

class CategoryTextualDataInput(GQLObject):
   language: CategoryLanguage
   name: str
   shortDescription: str
   longDescription: str

class CategoryEntity(GQLObject):
   createdAt: DateTime
   id: ID
   longDescription: str
   name: str
   shortDescription: str
   slugifiedName: str
   status: str
   type: str
   updatedAt: DateTime
   weight: int

class endpointsAndApiVersionCouples(GQLObject):
   endpointHash: str
   apiversion: str

class BlockedUserInput(GQLObject):
   apiId: str
   usersIds: list[int]

class BillingLimitInputV2(GQLObject):
   id: str
   item: str
   amount: int
   limitType: str
   overagePrice: float
   period: str
   unlimited: bool
   perusagePrice: float
   status: str
   currency: str

class upsertBillingPlanInput(GQLObject):
   billingPlanId: str
   name: str
   targetGroup: str
   isPrivatePlan: bool
   isStudent: bool
   legalDocumentId: str
   legalAccountId: str
   shouldRequestApproval: bool
   requestApprovalQuestion: str

class BillingPlanVersionFilters(GQLObject):
   query: str

class RateLimit(GQLObject):
   enabled: bool
   unit: int
   unitName: str
   amount: int

class SeatsBillingInformation(GQLObject):
   freeSeats: int
   unitPrice: int
   isCustomInvoiceBilling: bool
   billingPlanVersionId: str

class RateLimitInput(GQLObject):
   enabled: bool
   unit: int
   unitName: str
   amount: int

class EnableBillingFeatureInput(GQLObject):
   billingFeature: str
   note: str

class OverageLocalePrice(GQLObject):
   price: float
   symbol: str

class upsertBillingItem(GQLObject):
   billingItemId: str
   name: str
   description: str
   allEndpoints: bool
   endpointHashes: list[str]

class BillingInformation(GQLObject):
   id: int
   stripeId: str
   userId: int
   customerId: str
   fullName: str
   last4: str
   type: str
   exp_month: int
   exp_year: int
   zip: str
   billingStatus: str
   mashapeId: str
   createdAt: DateTime
   updatedAt: DateTime
   deletedAt: DateTime
   status: str

class upsertBillingFeatureInput(GQLObject):
   apiId: str
   apiVersionId: str
   name: str
   description: str
   billingFeatureId: str
   endpointHashes: list[str]

class AuthenticationParamInput(GQLObject):
   id: ID
   name: str
   description: str
   status: str

class AuthenticationExtraMetadataInput(GQLObject):
   pkceEnabled: bool
   codeChallengeMethod: CodeChallengeMethod
   customOAuth2AuthPrefix: str
   JWTProfile: bool

class SecurityRequirement(GQLObject):
   id: ID
   scope: SecurityRequirementAuthScope

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
   """
   ApiWhereInput - Can not act as a single filter, either id, ownerId or subscriberId input must be provided as well.

   ownerId - The owner Id of the API

   visibility - Filter by API visibility

   searchTerm - Option to send a search term and in the service it will filter either by api name, id or owner id

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
   categories: list[ID]
   searchTerm: str

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

class APITag(GQLObject):
   id: str
   status: str
   tagdefinition: str
   value: str
   createdAt: DateTime

class StatsFilterBy(GQLObject):
   values: list[str]
   name: str

class BatchTrackingIdsSummary(GQLObject):
   success: int
   failed: int
   total: int
   finishedEntities: int
   totalEntities: int

class ApiSpecImportWarning(GQLObject):
   type: ApiSpecImportWarningType
   critical: bool
   text: str
   info: Any

class ApiCreateFromRapidOasInput(GQLObject):
   spec: Upload

class ApiCreateFromSpecInput(GQLObject):
   spec: Upload
   specType: ApiSpecType
   category: str
   name: str
   description: str

class ApiSearchUser(GQLObject):
   id: int
   thumbnail: str
   name: str
   username: str

class Feature(GQLObject):
   heading: str
   caption: str
   image: str

class apiRating(GQLObject):
   rating: float
   votes: int
   bestRating: int

class ApiFollowerWhereInput(GQLObject):
   apiId: ID
   followerIds: list[ID]

class ApiFollowerDeleteInput(GQLObject):
   apiId: ID

class DeleteApiFavoritesInput(GQLObject):
   apiIds: list[ID]

class CopyApiDevelopersInput(GQLObject):
   apiId: str
   apiVersionIdFrom: str
   apiVersionIdTo: str

class ApiCertificateSortingField(GQLObject):
   fieldName: ApiCertificateSortingFieldName
   by: SortingFieldOrder

class ApiCertificateCreateInput(GQLObject):
   alias: str
   certificateFile: Upload

class ApiCertificateIssuerInfo(GQLObject):
   commonName: str
   countryName: str
   localityName: str
   organizationName: str
   organizationalUnitName: str
   stateOrProvinceName: str
   emailAddress: str

class AnalyticsStatsGroupByInput(GQLObject):
   fields: list[AnalyticsStatsGroupBy]

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
   allowAdminAccess: bool

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
