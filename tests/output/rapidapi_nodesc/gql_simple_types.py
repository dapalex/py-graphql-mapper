from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class UVJVW_name_Field(ArguedStr):
   class strArgs(GQLArgsSet, GQLObject):
      showDeleted: bool

   _args: strArgs



class Exclusion(GQLObject):
   topic: str

class UpdateWorkflowsInput(GQLObject):
   workflowIds: NonNull_list[int]
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
   emails: NonNull_list[str]
   orgId: int

class UserInvitesBrandingInput(GQLObject):
   email: str
   id: int
   inviterId: int

class UserInvitesInput(GQLObject):
   email: str
   teamIds: NonNull_list[int]
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
   plans: NonNull_list[ID]
   endpoints: NonNull_list[ID]

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

class ActiveSubscriptionCount(GQLObject):
   date: str
   count: int

class usageByBillingItem(GQLObject):
   id: ID
   name: str
   quota: int
   usage: int
   period: str
   usagePercentages: float
   billingCycleStart: DateTime

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
   schemas: str

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
   apiVersionId: str
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
   gatewayDefaultTimeOut: int
   limitRequestSize: int
   allowHttpTraffic: bool

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

class authStrategyType(GQLObject):
   type: str

class attributes(GQLObject):
   rapidClient: str
   userAgent: str

class activeEntity(GQLObject):
   id: int
   type: str
   name: str

class ThemeUserAttributesInput(GQLObject):
   attributeName: str
   attributeValue: str

class UserAttributesRow(GQLObject):
   userId: int
   attributeName: str
   attributeValue: Any

class AsyncApiConfigurationCreateInput(GQLObject):
   apiVersionId: ID
   spec: str

class GenerateAssetUploadUrlInput(GQLObject):
   externalId: ID
   filename: str
   description: str
   title: str

class AssetWhereInput(GQLObject):
   ids: list[ID]
   externalIds: list[ID]
   visible: bool

class Asset(GQLObject):
   id: ID
   externalId: ID
   filename: str
   title: str
   description: str
   visible: bool
   fileSizeBytes: float
   isUploadDone: bool
   presignedUrl: str
   createdAt: DateTime

class DeleteApplicationEnvironmentKeyInput(GQLObject):
   applicationEnviornmentId: ID

class AddApplicationEnvironmentKeyInput(GQLObject):
   applicationId: ID
   environment: str

class AppAuthorizationCreateInput(GQLObject):
   projectId: ID
   name: str
   authorizationType: AppAuthorizationType
   grantType: AuthorizationGrantType
   authorizationValues: str
   gatewayIds: list[ID]

class GqlOptions(GQLObject):
   enableSchemaIntrospectionOnHub: bool

class ApiSortingField(GQLObject):
   fieldName: ApiSortingFieldName
   by: SortingFieldOrder

class ProvisionApiFromFileInput(GQLObject):
   name: str
   category: str
   description: str
   file: Upload
   fileFormat: ApiImportFileFormat
   ownerId: ID

class ApiTagValueInput(GQLObject):
   id: ID
   definitionId: ID
   value: str

class createApiVersionBillingPlanVersionInput(GQLObject):
   billingPlanVersionId: str
   billingPlanId: str
   apiVersionId: str
   showInMarketplace: bool

class ApiCertificateAssociationTarget(GQLObject):
   apiCertificateId: ID

class ApiVersionCreateInput(GQLObject):
   api: str
   name: str
   visibility: Visibility
   oldApiVersionId: str

class ResponsePayload(GQLObject):
   id: str
   name: str
   format: str
   body: str
   headers: str
   description: str
   type: str
   apiversion: str
   status: str
   createdAt: DateTime
   updatedAt: DateTime
   statusCode: int
   apiendpoint: str
   examples: Any
   schema: Any
   schemaDefinition: Any

class ApiVersionWhereInput(GQLObject):
   id: list[ID]
   apiId: list[ID]
   versionStatus: list[VersionStatus]

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

class deleteUserAlertsInput(GQLObject):
   ids: NonNull_list[ID]

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
   endpointsIds: ID
   baseUrl: str
   apiVersionsIds: ID
   billingPlansIds: ID
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
   type: EnvConfigType
   description: str
   categoryId: int
   label: str
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
