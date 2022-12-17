from typing import Generic
from pygqlmap.components import GQLObject
from pygqlmap.gqlTypes import ID
from .enums import *
from .scalars import *

class nameField(name):
   class Args(): 
      showDeleted: bool

   _args: Args



class Exclusion(GQLObject):
   topic: str

class UpdateWorkflowsInput(GQLObject):
   workflowIds: list[int] ##NON NULL
   status: DeletionStatus
   workflowStatus: WorkflowStatus
   additionalData: Any
   componentId: str
   subComponentId: str

class CreateWorkflowInput(GQLObject):
   componentId: str ##NON NULL
   subComponentId: str
   componentDisplayName: str
   topic: WorkflowTopic ##NON NULL
   workflowStatus: WorkflowStatus
   additionalData: Any

class WorkflowAudit(GQLObject):
   elasticSearchId: ID ##NON NULL
   id: int
   topic: str ##NON NULL
   requestorId: int ##NON NULL
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
   id: int ##NON NULL
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
   emails: list[str] ##NON NULL
   orgId: int ##NON NULL

class UserInvitesBrandingInput(GQLObject):
   email: str
   id: int
   inviterId: int

class UserInvitesInput(GQLObject):
   email: str
   teamIds: list[int] ##NON NULL
   organizationId: int ##NON NULL
   role: str
   id: int
   inviterId: int

class InviteUsersSearch(GQLObject):
   id: ID ##NON NULL
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
   apiId: ID ##NON NULL
   apiVersion: ID ##NON NULL
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
   slugifiedName: str ##NON NULL
   apiId: ID ##NON NULL
   apiVersion: ID ##NON NULL
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
   fieldName: TransformationSortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class TransformationCreateInput(GQLObject):
   apiVersionId: ID ##NON NULL
   action: TransformationActionType ##NON NULL
   transformationType: TransformationType ##NON NULL
   condition: TransformationConditionType
   targetPath: str
   targetMethod: TransformationMethodType
   from_: str
   target: str
   value: str
   valueType: TransformationValueType
   plans: list[ID] ##NON NULL
   endpoints: list[ID] ##NON NULL

class Transformation(GQLObject):
   id: ID ##NON NULL
   apiVersionId: ID ##NON NULL
   action: TransformationActionType ##NON NULL
   transformationType: TransformationType ##NON NULL
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
   id: ID ##NON NULL
   name: str
   text: str
   createdAt: DateTime
   updatedAt: DateTime

class TeamWhereInput(GQLObject):
   slugifiedName: str
   orgId: int

class TeamCreateInput(GQLObject):
   organizationId: int ##NON NULL
   name: str ##NON NULL
   thumbnail: str
   description: str

class TeamUserWhereInput(GQLObject):
   email: str ##NON NULL
   orgId: int ##NON NULL

class TeamUserUpdateInput(GQLObject):
   orgId: int ##NON NULL
   teamUserId: int ##NON NULL
   teamToRemove: int
   teamToAdd: int
   newRole: str

class TargetUrl(GQLObject):
   url: str ##NON NULL
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
   apiId: ID ##NON NULL
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
   id: ID ##NON NULL
   apiId: ID ##NON NULL
   type: SpotlightType
   weight: int
   published: bool
   title: str
   description: str
   spotlightURL: str
   file: Upload

class SecretParameter(GQLObject):
   id: ID ##NON NULL
   placement: SecretParameterPlacement ##NON NULL
   name: str ##NON NULL
   value: str ##NON NULL
   description: str ##NON NULL

class createSecretDataInput(GQLObject):
   apiVersionId: str ##NON NULL
   url: str ##NON NULL
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
   term: str ##NON NULL
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
   projectIds: list[ID] ##NON NULL
   endpoints: list[str] ##NON NULL
   httpMethods: list[HttpMethod] ##NON NULL
   httpStatuses: list[int] ##NON NULL
   originIps: list[str] ##NON NULL

class RapidReasonInput(GQLObject):
   consumerUserId: int
   providerUserId: int
   externalId: Any
   eventType: RapidReasonsEvents ##NON NULL
   reasonType: UnsubscribeReasons ##NON NULL
   reasonComments: str
   apiId: str ##NON NULL
   apiVersionId: str ##NON NULL

class updateProjectAllowedAPIInput(GQLObject):
   id: int ##NON NULL
   projectId: int ##NON NULL
   apiId: str
   apiVersionId: str
   mashapeId: str ##NON NULL

class ProjectUpdateInput(GQLObject):
   projectId: ID ##NON NULL
   projectName: str ##NON NULL
   projectDescription: str ##NON NULL
   thumbnail: Upload
   enableLimitsToAPIs: bool ##NON NULL

class EditProjectInput(GQLObject):
   projectId: ID ##NON NULL
   projectName: str ##NON NULL
   projectDescription: str ##NON NULL
   thumbnail: Upload
   enableLimitsToAPIs: bool ##NON NULL

class AddProjectInput(GQLObject):
   projectOwner: ID ##NON NULL
   projectName: str ##NON NULL
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
   organizationId: int ##NON NULL
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
   id: int ##NON NULL
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
   fromEmail: str ##NON NULL
   toEmail: str ##NON NULL
   toId: str ##NON NULL
   title: str
   body: str ##NON NULL
   apiName: str ##NON NULL
   apiId: str
   type: str

class MessageInput(GQLObject):
   authorId: int
   title: str
   body: str
   apiId: str ##NON NULL
   entityId: int
   ownerId: int
   messageThreadId: int
   ownerDisplayName: str ##NON NULL
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
   partition: int ##NON NULL
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
   configName: str ##NON NULL
   configValue: str ##NON NULL
   readOnly: bool ##NON NULL
   isDefault: bool ##NON NULL
   isSensitive: bool ##NON NULL

class ProduceMessageResponse(GQLObject):
   topicName: str
   partition: int
   errorCode: int
   baseOffset: str

class KafkaSchemas(GQLObject):
   schemas: str ##NON NULL

class IssueFollowInputV2(GQLObject):
   issueId: int ##NON NULL

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
   apiId: str ##NON NULL
   apiVersionId: str ##NON NULL
   text: str
   textModified: bool ##NON NULL

class UpdateGraphQLSchemaInput(GQLObject):
   source: Upload ##NON NULL
   graphQLSchemaId: ID
   endpointId: ID

class GqlDoc(GQLObject):
   docKey: str ##NON NULL
   defaultDescription: str ##NON NULL
   description: str ##NON NULL
   visible: bool ##NON NULL

class GatewayConfiguration(GQLObject):
   gatewayDefaultTimeOut: int
   limitRequestSize: int
   allowHttpTraffic: bool

class LogsCSVExports(GQLObject):
   status: int
   statusText: str

class EntityRoleSorting(GQLObject):
   fieldName: EntityRoleSortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class EntityRoleInput(GQLObject):
   id: ID
   entityId: int
   roleId: int
   parentId: int
   orgId: int

class EntityMetadataWhereInput(GQLObject):
   entityId: list[ID] ##NON NULL
   attributeName: str
   attributeValue: str

class DuplicateNameCheckInput(GQLObject):
   term: str ##NON NULL
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
   issueId: int ##NON NULL

class IssuesDeleteInput(GQLObject):
   issueIds: list[int] ##NON NULL

class Currency(GQLObject):
   code: str
   name: str
   symbol: str
   symbol_native: str
   decimal_digits: int
   rakuten_symbol: Any

class ContactAdminSubscribeToAPIEvent(GQLObject):
   api_name: str ##NON NULL
   api_link: str ##NON NULL
   team_id: int ##NON NULL
   org_id: int ##NON NULL
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
   issueId: int ##NON NULL
   commentId: int ##NON NULL

class CommentCreateInput(GQLObject):
   body: str ##NON NULL
   issueId: int ##NON NULL

class CollectionUpdateInput(GQLObject):
   id: ID ##NON NULL
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
   id: list[ID] ##NON NULL
   name: list[str]
   language: CategoryLanguage
   slugifiedName: list[str]

class CategoryTextualDataInput(GQLObject):
   language: CategoryLanguage ##NON NULL
   name: str ##NON NULL
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
   item: str ##NON NULL
   amount: int
   limitType: str
   overagePrice: float
   period: str ##NON NULL
   unlimited: bool ##NON NULL
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
   billingFeature: str ##NON NULL
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
   apiId: str ##NON NULL
   apiVersionId: str ##NON NULL
   name: str
   description: str
   billingFeatureId: str
   endpointHashes: list[str]

class AuthenticationParamInput(GQLObject):
   id: ID
   name: str ##NON NULL
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
   apiVersionId: ID ##NON NULL
   spec: str ##NON NULL

class GenerateAssetUploadUrlInput(GQLObject):
   externalId: ID ##NON NULL
   filename: str ##NON NULL
   description: str
   title: str

class AssetWhereInput(GQLObject):
   ids: list[ID] ##NON NULL
   externalIds: list[ID] ##NON NULL
   visible: bool

class Asset(GQLObject):
   id: ID ##NON NULL
   externalId: ID ##NON NULL
   filename: str ##NON NULL
   title: str
   description: str
   visible: bool ##NON NULL
   fileSizeBytes: float
   isUploadDone: bool ##NON NULL
   presignedUrl: str
   createdAt: DateTime ##NON NULL

class DeleteApplicationEnvironmentKeyInput(GQLObject):
   applicationEnviornmentId: ID ##NON NULL

class AddApplicationEnvironmentKeyInput(GQLObject):
   applicationId: ID ##NON NULL
   environment: str ##NON NULL

class AppAuthorizationCreateInput(GQLObject):
   projectId: ID ##NON NULL
   name: str
   authorizationType: AppAuthorizationType
   grantType: AuthorizationGrantType
   authorizationValues: str
   gatewayIds: list[ID] ##NON NULL

class GqlOptions(GQLObject):
   enableSchemaIntrospectionOnHub: bool

class ApiSortingField(GQLObject):
   fieldName: ApiSortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class ProvisionApiFromFileInput(GQLObject):
   name: str ##NON NULL
   category: str ##NON NULL
   description: str
   file: Upload ##NON NULL
   fileFormat: ApiImportFileFormat ##NON NULL
   ownerId: ID

class ApiTagValueInput(GQLObject):
   id: ID
   definitionId: ID ##NON NULL
   value: str ##NON NULL

class createApiVersionBillingPlanVersionInput(GQLObject):
   billingPlanVersionId: str ##NON NULL
   billingPlanId: str ##NON NULL
   apiVersionId: str ##NON NULL
   showInMarketplace: bool ##NON NULL

class ApiCertificateAssociationTarget(GQLObject):
   apiCertificateId: ID ##NON NULL

class ApiVersionCreateInput(GQLObject):
   api: str ##NON NULL
   name: str ##NON NULL
   visibility: Visibility
   oldApiVersionId: str

class ResponsePayload(GQLObject):
   id: str ##NON NULL
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
   examples: Any ##NON NULL
   schema: Any
   schemaDefinition: Any

class ApiVersionWhereInput(GQLObject):
   id: list[ID] ##NON NULL
   apiId: list[ID] ##NON NULL
   versionStatus: list[VersionStatus] ##NON NULL

class APITag(GQLObject):
   id: str
   apiversion: str
   status: str
   tagdefinition: str
   type: str
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
   type: ApiSpecImportWarningType ##NON NULL
   critical: bool ##NON NULL
   text: str
   info: Any

class ApiCreateFromRapidOasInput(GQLObject):
   spec: Upload ##NON NULL

class ApiCreateFromSpecInput(GQLObject):
   spec: Upload ##NON NULL
   specType: ApiSpecType ##NON NULL
   category: str ##NON NULL
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
   apiId: ID ##NON NULL
   followerIds: list[ID] ##NON NULL

class ApiFollowerDeleteInput(GQLObject):
   apiId: ID ##NON NULL

class DeleteApiFavoritesInput(GQLObject):
   apiIds: list[ID] ##NON NULL

class CopyApiDevelopersInput(GQLObject):
   apiId: str
   apiVersionIdFrom: str
   apiVersionIdTo: str

class ApiCertificateSortingField(GQLObject):
   fieldName: ApiCertificateSortingFieldName ##NON NULL
   by: SortingFieldOrder ##NON NULL

class ApiCertificateCreateInput(GQLObject):
   alias: str ##NON NULL
   certificateFile: Upload ##NON NULL

class ApiCertificateIssuerInfo(GQLObject):
   commonName: str
   countryName: str
   localityName: str
   organizationName: str
   organizationalUnitName: str
   stateOrProvinceName: str
   emailAddress: str

class deleteUserAlertsInput(GQLObject):
   ids: list[ID] ##NON NULL

class editUserAlertInput(GQLObject):
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
   apiIds: list[ID]
   projectIds: list[ID]
   baseUrl: str
   minNextAlertTime: DateTime
   endpointsIds: list[ID] ##NON NULL
   apiVersionsIds: list[ID] ##NON NULL
   billingPlansIds: list[ID] ##NON NULL
   endpointHashes: list[ID] ##NON NULL

class UserAlert(GQLObject):
   id: ID ##NON NULL
   entityId: ID ##NON NULL
   name: str ##NON NULL
   description: str
   scope: ID ##NON NULL
   typeId: int ##NON NULL
   condition: Condition ##NON NULL
   threshold: float ##NON NULL
   timeInterval: time ##NON NULL
   timePeriod: int ##NON NULL
   channel: Channel ##NON NULL
   status: AlertStatus ##NON NULL
   throttleInterval: time ##NON NULL
   throttlePeriod: int ##NON NULL
   apiIds: list[ID]
   projectIds: list[ID]
   endpointsIds: ID ##NON NULL
   baseUrl: str
   apiVersionsIds: ID ##NON NULL
   billingPlansIds: ID ##NON NULL
   minNextAlertTime: DateTime
   endpointHashes: list[ID]
   deletedAt: DateTime
   createdAt: DateTime
   updatedAt: DateTime

class SEOTagAttribute(GQLObject):
   key: str
   value: str

class GatewayTemplateParamsCreateInput(GQLObject):
   paramName: str ##NON NULL
   paramValue: str ##NON NULL
   paramDescription: str ##NON NULL
   codeTemplateId: int ##NON NULL

class PartialGatewayTemplateParamCreateInput(GQLObject):
   paramName: str ##NON NULL
   paramValue: str ##NON NULL
   paramDescription: str ##NON NULL

class GatewayConfigurationUpdateInput(GQLObject):
   gatewayDefaultTimeOut: int
   limitRequestSize: int
   allowHttpTraffic: bool

class GatewayConfigurationCreateInput(GQLObject):
   gatewayDefaultTimeOut: int
   limitRequestSize: int
   allowHttpTraffic: bool

class EventUrlUpdateInput(GQLObject):
   url: str ##NON NULL

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
   fieldName: GatewayTemplateParamsSortingFieldName ##NON NULL
   order: Order

class GatewayTemplateSortingSortingField(GQLObject):
   fieldName: GatewayTemplateSorting ##NON NULL
   order: Order

class GatewayInstanceSortingSortingField(GQLObject):
   fieldName: GatewayInstanceSorting ##NON NULL
   order: Order

class EventUrlSortablesSortingField(GQLObject):
   fieldName: EventUrlSortables ##NON NULL
   order: Order

class PaginationArgs(GQLObject):
   first: int
   last: int
   before: str
   after: str

class EnvConfig(GQLObject):
   id: int ##NON NULL
   key: str ##NON NULL
   value: str ##NON NULL
   type: EnvConfigType ##NON NULL
   description: str
   categoryId: int ##NON NULL
   label: str
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL

class ExtensionConsumer(GQLObject):
   id: ID ##NON NULL
   extensionId: int ##NON NULL
   client: str ##NON NULL
   page: str ##NON NULL
   order: int ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL
   deletedAt: DateTime

class EventUrl(GQLObject):
   id: ID ##NON NULL
   url: str ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL
   deletedAt: DateTime

class GatewayTemplateParam(GQLObject):
   id: ID ##NON NULL
   codeTemplateId: int ##NON NULL
   paramName: str ##NON NULL
   paramValue: str ##NON NULL
   paramDescription: str
   status: str
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL

class GatewayCustomMessage(GQLObject):
   id: ID ##NON NULL
   apiGatewayInstanceId: int ##NON NULL
   messageKey: str ##NON NULL
   messageValue: str ##NON NULL
   createdAt: DateTime ##NON NULL
   updatedAt: DateTime ##NON NULL
