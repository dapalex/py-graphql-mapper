from typing import List
from pygqlmap import GQLQuery
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

class NonNull_EnvConfigTerm(EnvConfigTerm): pass

class list_Extension(list, Extension): pass

class list_UserAlert(list, UserAlert): pass

class NonNull_UserAlertsWhereInput(UserAlertsWhereInput): pass

class NonNull_ApiFollowerWhereInput(ApiFollowerWhereInput): pass

class NonNull_AppAuthorizationsWhereInput(AppAuthorizationsWhereInput): pass

class NonNull_AssetWhereInput(AssetWhereInput): pass

class NonNull_AsyncApiConfigurationWhereInput(AsyncApiConfigurationWhereInput): pass

class NonNull_AuditWhereInput(AuditWhereInput): pass

class list_authStrategy(list, authStrategy): pass

class NonNull_BillingItemsWhereInput(BillingItemsWhereInput): pass

class NonNull_list_endpointsAndApiVersionCouples(list, endpointsAndApiVersionCouples): pass

class list_CategoryEntity(list, CategoryEntity): pass

class list_Category(list, Category): pass

class list_CollapsedCollection(list, CollapsedCollection): pass

class list_Follower(list, Follower): pass

class list_OrgTransaction(list, OrgTransaction): pass

class NonNull_ConsumersWhereInput(ConsumersWhereInput): pass

class NonNull_ContactAdminSubscribeToAPIEvent(ContactAdminSubscribeToAPIEvent): pass

class list_EndpointStats(list, EndpointStats): pass

class list_EndpointAndVersion(list, EndpointAndVersion): pass

class list_VersionEndpointStats(list, VersionEndpointStats): pass

class NonNull_endpointsWithinDateInput(endpointsWithinDateInput): pass

class NonNull_EndpointWhereInput(EndpointWhereInput): pass

class list_Entity(list, Entity): pass

class NonNull_EntityMetadataWhereInput(EntityMetadataWhereInput): pass

class NonNull_EntityRoleWhereInput(EntityRoleWhereInput): pass

class list_LogsCSV(list, LogsCSV): pass

class NonNull_GetLegalAgreementSigningURLInput(GetLegalAgreementSigningURLInput): pass

class NonNull_MessagesWhereInput(MessagesWhereInput): pass

class list_NewNotification(list, NewNotification): pass

class NonNull_RoleWhereInput(RoleWhereInput): pass

class NonNull_SearchApiWhereInput(SearchApiWhereInput): pass

class NonNull_SearchBlogPostWhereInput(SearchBlogPostWhereInput): pass

class NonNull_SpotlightWhereInput(SpotlightWhereInput): pass

class list_ActiveSubscriptionCount(list, ActiveSubscriptionCount): pass

class list_SubscriptionsCount(list, SubscriptionsCount): pass

class NonNull_TeamUserWhereInput(TeamUserWhereInput): pass

class NonNull_TutorialWhereInput(TutorialWhereInput): pass

class list_Phone(list, Phone): pass

class list_RecoveryCode(list, RecoveryCode): pass

class list_UsagesStats(list, UsagesStats): pass

class list_InviteUsersSearch(list, InviteUsersSearch): pass

class list_User(list, User): pass

class NonNull_SearchUsersWhereInput(SearchUsersWhereInput): pass

class NonNull_UserWhereInput(UserWhereInput): pass

class list_Permission(list, Permission): pass

class NonNull_VirtualPermissionWhereInput(VirtualPermissionWhereInput): pass

class list_VirtualPermission(list, VirtualPermission): pass

class list_Exclusion(list, Exclusion): pass

class ping(GQLQuery):
   """
   ping - Used to determine whether or not RapidAPI is responding to API calls

   """
   type: str

class eventUrls(GQLQuery):
   """
   eventUrls - Get all URLs for an Event

   """
   class EventUrlConnectionArgs(GQLArgsSet, GQLObject):
      pagination: PaginationArgs
      where: EventUrlWhereInput
      order: EventUrlSortablesInput

   _args: EventUrlConnectionArgs


   type: EventUrlConnection

class eventUrl(GQLQuery):
   """
   eventUrl - Get details of the specific URL for the Event

   """
   class EventUrlArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: EventUrlArgs


   type: EventUrl

class eventTypes(GQLQuery):
   """
   eventTypes - Get types of Events

   """
   type: EventType

class eventConfig(GQLQuery):
   """
   eventConfig - Get event configuration information

   """
   type: EventConfig

class gatewayInstances(GQLQuery):
   """
   gatewayInstances - Get all gateway instances

   """
   class GatewayInstanceConnectionArgs(GQLArgsSet, GQLObject):
      pagination: PaginationArgs
      where: GatewayInstanceWhereInput
      order: GatewayInstanceSortingInput

   _args: GatewayInstanceConnectionArgs


   type: GatewayInstanceConnection

class gatewayInstance(GQLQuery):
   """
   gatewayInstance - Get the gateway instance information

   """
   class GatewayInstanceArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: GatewayInstanceArgs


   type: GatewayInstance

class gatewayTemplates(GQLQuery):
   """
   gatewayTemplates - Get all templates

   """
   class GatewayTemplateConnectionArgs(GQLArgsSet, GQLObject):
      pagination: PaginationArgs
      where: GatewayTemplateWhereInput
      order: GatewayTemplateSortingInput

   _args: GatewayTemplateConnectionArgs


   type: GatewayTemplateConnection

class gatewayTemplate(GQLQuery):
   """
   gatewayTemplate - Get details of a specific tempalte 

   """
   class GwTemplateArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: GwTemplateArgs


   type: GwTemplate

class gatewayTemplatesParams(GQLQuery):
   """
   gatewayTemplatesParams - Get all parameters across a tempalte

   """
   class GatewayTemplateParamConnectionArgs(GQLArgsSet, GQLObject):
      pagination: PaginationArgs
      where: GatewayTemplateParamsWhereInput
      order: GatewayTemplateParamSortingInput

   _args: GatewayTemplateParamConnectionArgs


   type: GatewayTemplateParamConnection

class gatewayTemplateParam(GQLQuery):
   """
   gatewayTemplateParam - Get details of a specific template prameter

   """
   class GatewayTemplateParamArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: GatewayTemplateParamArgs


   type: GatewayTemplateParam

class envConfigCategories(GQLQuery):
   """
   envConfigCategories - A category of enterprise congfiguration

   """
   type: EnvConfigCategory

class envConfig(GQLQuery):
   """
   envConfig - An individaul enterprise configruation

   """
   class EnvConfigArgs(GQLArgsSet, GQLObject):
      id: NonNull_int

   _args: EnvConfigArgs


   type: EnvConfig

class envConfigs(GQLQuery):
   """
   envConfigs - All configurations for an Enterprise

   """
   class EnvConfigArgs(GQLArgsSet, GQLObject):
      envConfigTerm: NonNull_EnvConfigTerm

   _args: EnvConfigArgs


   type: EnvConfig

class adminAuditLogs(GQLQuery):
   """
   adminAuditLogs - Enterprise admin audit logs 

   """
   class AdminAuditLogConnectionArgs(GQLArgsSet, GQLObject):
      where: AdminAuditLogInput
      pagination: PaginationArgs
      orderBy: AdminAuditLogSortablesInput

   _args: AdminAuditLogConnectionArgs


   type: AdminAuditLogConnection

class eventLogs(GQLQuery):
   """
   eventLogs - Get audit trail(s) for Events

   """
   class EventLogConnectionArgs(GQLArgsSet, GQLObject):
      where: EventLogInput
      pagination: PaginationArgs
      orderBy: EventLogSortablesInput

   _args: EventLogConnectionArgs


   type: EventLogConnection

class extensions(GQLQuery):
   """
   extensions - Get extensions for an API

   """
   class ExtensionArgs(GQLArgsSet, GQLObject):
      client: str
      page: str
      path: str

   _args: ExtensionArgs


   type: list_Extension[Extension]

class getSEOTagsByURL(GQLQuery):
   """
   getSEOTagsByURL - returns the CEO tags defined for an API

   """
   class SEOArgs(GQLArgsSet, GQLObject):
      url: str

   _args: SEOArgs


   type: SEO

class getUserAlertById(GQLQuery):
   """
   getUserAlertById - Get alert created by an API Provider by Id

   """
   class UserAlertArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: UserAlertArgs


   type: UserAlert

class getUserAlertsByScope(GQLQuery):
   """
   getUserAlertsByScope - Get alerts created by an API provider for an API by scope

   """
   class UserAlertArgs(GQLArgsSet, GQLObject):
      scope: NonNull_ID

   _args: UserAlertArgs


   type: list_UserAlert[UserAlert]

class getAlertsDefinitions(GQLQuery):
   """
   getAlertsDefinitions - Get definitions of alerts across RapidAPI

   """
   type: AlertDefinition

class userAlerts(GQLQuery):
   """
   userAlerts - Get alerts created by an API provider for an API

   """
   class UserAlertsConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_UserAlertsWhereInput

   _args: UserAlertsConnectionArgs


   type: UserAlertsConnection

class userAlert(GQLQuery):
   """
   userAlert - Get alert created by an API provider for an API

   """
   class UserAlertArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: UserAlertArgs


   type: UserAlert

class allowedPlanDeveloperByPlanId(GQLQuery):
   """
   allowedPlanDeveloperByPlanId - Get invited developers for a private plan of an API

   """
   class AllowedPlanDeveloperArgs(GQLArgsSet, GQLObject):
      planId: str

   _args: AllowedPlanDeveloperArgs


   type: list_AllowedPlanDeveloper[AllowedPlanDeveloper]

class apiCertificate(GQLQuery):
   """
   apiCertificate - returns the API Certificate details based on the certificate Id

   """
   class ApiCertificateArgs(GQLArgsSet, GQLObject):
      apiCertificateId: NonNull_ID

   _args: ApiCertificateArgs


   type: ApiCertificate

class apiCertificates(GQLQuery):
   """
   apiCertificates - returns the API Certificates details based on the API Id and User Id

   """
   class ApiCertificateConnectionArgs(GQLArgsSet, GQLObject):
      where: ApiCertificateWhereInput
      orderBy: ApiCertificateOrderByInput
      pagination: PaginationInput

   _args: ApiCertificateConnectionArgs


   type: ApiCertificateConnection

class apiDevelopersByApiId(GQLQuery):
   """
   apiDevelopersByApiId - returns API developer details based on the API Id parameter

   """
   class ApiDeveloperArgs(GQLArgsSet, GQLObject):
      apiId: str
      pagingArgs: PagingArgs

   _args: ApiDeveloperArgs


   type: ApiDeveloper

class apiFollowers(GQLQuery):
   """
   apiFollowers - Returns a list of users who follow a specific API(s)

   """
   class ApiFollowerConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_ApiFollowerWhereInput
      orderBy: ApiFollowerOrderByInput
      pagination: PaginationInput

   _args: ApiFollowerConnectionArgs


   type: ApiFollowerConnection

class apiReferenceByApiAndVersionId(GQLQuery):
   """
   apiReferenceByApiAndVersionId - [will be deprecated; do not use] Use apiReferences

   """
   class ApiReferenceArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_str
      versionId: NonNull_str

   _args: ApiReferenceArgs


   type: ApiReference

class apiReferences(GQLQuery):
   """
   apiReferences - Something with API Spotlights...

   """
   class ApiReferenceConnectionArgs(GQLArgsSet, GQLObject):
      where: ApiReferenceWhereInput

   _args: ApiReferenceConnectionArgs


   type: ApiReferenceConnection

class apiSearch(GQLQuery):
   """
   apiSearch - [will be deprecated; do not use] Search for API

   """
   class ApiSearchPagedArgs(GQLArgsSet, GQLObject):
      searchArguments: SearchArguments

   _args: ApiSearchPagedArgs


   type: ApiSearchPaged

class apiSearchV3(GQLQuery):
   """
   apiSearchV3 - [will be deprecated; do not use] Search for API

   """
   class ApiSearchPagedArgs(GQLArgsSet, GQLObject):
      searchArguments: SearchArguments

   _args: ApiSearchPagedArgs


   type: ApiSearchPaged

class apiSpecImportProgresses(GQLQuery):
   """
   apiSpecImportProgresses - Supports the async process for the API import (especially for long time upload might be a result of a big file import. Polling request from the client to the backend - returns success result only when the API was completely imported. 

   """
   class ApiSpecImportProcessArgs(GQLArgsSet, GQLObject):
      trackingIds: NonNull_list[NonNull_ID]

   _args: ApiSpecImportProcessArgs


   type: ApiSpecImportProcess

class bulkApisSummaryByTrackingIds(GQLQuery):
   """
   bulkApisSummaryByTrackingIds - Check to see if the API import operation has completed across multiple APIs

   """
   class BatchTrackingIdsSummaryArgs(GQLArgsSet, GQLObject):
      trackingIds: NonNull_list[ID]

   _args: BatchTrackingIdsSummaryArgs


   type: BatchTrackingIdsSummary

class calculatedStatistics(GQLQuery):
   """
   calculatedStatistics - Get API usage analytics

   """
   class CalculatedStatisticsArgs(GQLArgsSet, GQLObject):
      fromDate: NonNull_str
      toDate: NonNull_str
      resolution: str
      projectIds: list[str]
      apiIds: list[str]
      endpoints: list[str]
      groupBy: StatsGroupBy
      apiVersionIds: list[ID]
      entityId: ID
      timeOffset: int
      filters: list_StatsFilterBy[StatsFilterBy]

   _args: CalculatedStatisticsArgs


   type: CalculatedStatistics

class getApiVersion(GQLQuery):
   """
   getApiVersion - [will be deprecated; do not use] return the apiVersion information based on the apiVersion's Id input

   """
   class ApiVersionArgs(GQLArgsSet, GQLObject):
      versionId: NonNull_ID

   _args: ApiVersionArgs


   type: ApiVersion

class apiVersion(GQLQuery):
   """
   apiVersion - [will be deprecated; do not use] return the apiVersion information based on the apiVersion's Id input

   """
   class ApiVersionArgs(GQLArgsSet, GQLObject):
      apiVersionId: NonNull_ID

   _args: ApiVersionArgs


   type: ApiVersion

class apiVersions(GQLQuery):
   """
   apiVersions - returns a list of apiVersions based on the ApiVersionWhereInput

   """
   class ApiVersionConnectionArgs(GQLArgsSet, GQLObject):
      where: ApiVersionWhereInput
      orderBy: ApiVersionOrderByInput
      pagination: PaginationInput

   _args: ApiVersionConnectionArgs


   type: ApiVersionConnection

class api(GQLQuery):
   """
   api - Obtain an API's details, such as its name and current version.

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#obtain-an-apis-details

   """
   class ApiArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: ApiArgs


   type: Api

class apis(GQLQuery):
   """
   apis - Returns the APIs based on the APIWhereInput

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#query-apis



   """
   class ApiConnectionArgs(GQLArgsSet, GQLObject):
      where: ApiWhereInput
      orderBy: ApiOrderByInput
      pagination: PaginationInput

   _args: ApiConnectionArgs


   type: ApiConnection

class exportOpenApi(GQLQuery):
   """
   exportOpenApi - Returns a generated OAS 3 representation of a certain API version in the platform, including the RapidAPI metadata extension properties.\n\n`apiId` and the optional `apiVersionId` args specify which API and version to target for export.\nOmitting the `apiVersionId` arg will target the *current* version of the API specified by `apiId`.\n\nA non-null result would be returned only in accordance with the following rules:\n- the target `apiId` or `apiVersionId` (if specifically provided) have some match in the platform, and either:\n  - the target API is defined with `PUBLIC` visibility, or\n  - the target API is defined with `PRIVATE` visibility and either:\n    - the requestor or any team they are a member of is owning the target API or\n    - the requestor or any team they are a member of is **invited** to the target API\n\nIf the API is visible to the requestor for export but not owned by it, certain sensitive fields (e.g `servers` array) in the exported document may be returned blank.

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#export-an-oas-document-for-an-api

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_ID
      apiVersionId: ID

   _args: AnyArgs


   type: Any

class validateSwagger(GQLQuery):
   """
   validateSwagger - [marked for deprecation; do not use] Validates a swagger input

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: validateSwaggerInput

   _args: AnyArgs


   type: Any

class applicationAuthorization(GQLQuery):
   """
   applicationAuthorization - get application authorization (x-rapid-key/oauth)

   """
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization

class applicationAuthorizations(GQLQuery):
   """
   applicationAuthorizations - get application authorization (x-rapid-key/oauth)

   """
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject):
      where: NonNull_AppAuthorizationsWhereInput

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization

class applicationEnvironmentsKeysByApplicationIdAndEnvironment(GQLQuery):
   """
   applicationEnvironmentsKeysByApplicationIdAndEnvironment - applicationEnvironments (applicationAuthorization) by application Id. going to be deprecated, please don't know

   """
   class ApplicationEnvironmentPagingArgs(GQLArgsSet, GQLObject):
      applicationId: str
      environment: str

   _args: ApplicationEnvironmentPagingArgs


   type: ApplicationEnvironmentPaging

class applicationEnvironmentsByApplicationIdAndEnvironment(GQLQuery):
   """
   applicationEnvironmentsByApplicationIdAndEnvironment - applicationEnvironments (applicationAuthorization) by application Id.  going to be deprecated, please don't know 

   """
   class ApplicationEnvironmentArgs(GQLArgsSet, GQLObject):
      applicationId: str
      environment: str

   _args: ApplicationEnvironmentArgs


   type: ApplicationEnvironment

class applicationById(GQLQuery):
   """
   applicationById - application by Id 

   """
   class ApplicationArgs(GQLArgsSet, GQLObject):
      id: int

   _args: ApplicationArgs


   type: Application

class asset(GQLQuery):
   """
   asset - Fetch an asset by ID

   """
   class AssetArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: AssetArgs


   type: Asset

class assets(GQLQuery):
   """
   assets - Query assets by IDs or external IDs, optional filter on visibility

   """
   class AssetArgs(GQLArgsSet, GQLObject):
      where: NonNull_AssetWhereInput

   _args: AssetArgs


   type: Asset

class assetsDownloadUrls(GQLQuery):
   """
   assetsDownloadUrls - Query assets by IDs or external IDs, optional filter on visibility; Includes download URL in response

   """
   class AssetForDownloadArgs(GQLArgsSet, GQLObject):
      where: NonNull_AssetWhereInput

   _args: AssetForDownloadArgs


   type: AssetForDownload

class asyncApiConfigurations(GQLQuery):
   """
   asyncApiConfigurations - [experimental] Get async API configuration

   """
   class AsyncApiConfigurationConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_AsyncApiConfigurationWhereInput

   _args: AsyncApiConfigurationConnectionArgs


   type: AsyncApiConfigurationConnection

class userAttributesByUserId(GQLQuery):
   """
   userAttributesByUserId - Get all user attributes by user ID

   """
   class UserAttributesArgs(GQLArgsSet, GQLObject):
      userId: int

   _args: UserAttributesArgs


   type: UserAttributes

class auditByOrganizationId(GQLQuery):
   """
   auditByOrganizationId - Organization level Audits (e.g. creation, user invited, etc...)

   """
   class auditTrailsArgs(GQLArgsSet, GQLObject):
      searchTerm: str
      from_: int
      orgId: int

   _args: auditTrailsArgs


   type: auditTrails

class audit(GQLQuery):
   """
   audit - Enterprise Admin Audit (e.g. config CRUD events)

   """
   class auditTrailsArgs(GQLArgsSet, GQLObject):
      where: NonNull_AuditWhereInput

   _args: auditTrailsArgs


   type: auditTrails

class auditLogin(GQLQuery):
   """
   auditLogin - Audit for user logins

   """
   class auditTrailsArgs(GQLArgsSet, GQLObject):
      from_: int
      userId: str

   _args: auditTrailsArgs


   type: auditTrails

class userByEmail(GQLQuery):
   """
   userByEmail - Get user ID by user email address

   """
   class UserArgs(GQLArgsSet, GQLObject):
      email: str

   _args: UserArgs


   type: User

class activeUser(GQLQuery):
   """
   activeUser - The User making the request

   """
   type: User

class getAuthStrategies(GQLQuery):
   """
   getAuthStrategies - Get the configured  login options 

   """
   type: list_authStrategy[authStrategy]

class getBillingFeaturesByApiVersionId(GQLQuery):
   """
   getBillingFeaturesByApiVersionId - [will be deprecated; do not use] Get billing feature by API versionId (will have same results as getBillingFeaturesByApiId)

   """
   class BillingFeatureArgs(GQLArgsSet, GQLObject):
      versionId: str

   _args: BillingFeatureArgs


   type: list_BillingFeature[BillingFeature]

class getBillingFeaturesByApiId(GQLQuery):
   """
   getBillingFeaturesByApiId - Get billing feature by API id

   """
   class BillingFeatureArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_str

   _args: BillingFeatureArgs


   type: list_BillingFeature[BillingFeature]

class isMonetizationEnabled(GQLQuery):
   """
   isMonetizationEnabled - check if the monetization is enabled in the environment 

   """
   type: bool

class billingItems(GQLQuery):
   """
   billingItems - Get Billing items where input must include apiId or apiVersionId,\nPagination not supported

   """
   class BillingItemConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_BillingItemsWhereInput

   _args: BillingItemConnectionArgs


   type: BillingItemConnection

class getFreeSeatsObj(GQLQuery):
   """
   getFreeSeatsObj - Get billing information attached to an org

   """
   class SeatsBillingInformationArgs(GQLArgsSet, GQLObject):
      orgId: NonNull_ID

   _args: SeatsBillingInformationArgs


   type: SeatsBillingInformation

class getBillingPlanVersionsByApiId(GQLQuery):
   """
   getBillingPlanVersionsByApiId - [will be deprecated; do not use] use billingPlanVersions query

   """
   class BillingPlanVersionsResponseArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_str
      apiVersionId: str
      pagingArgs: PagingArgsBilling
      filters: BillingPlanVersionFilters

   _args: BillingPlanVersionsResponseArgs


   type: BillingPlanVersionsResponse

class getBillingPlanVersionById(GQLQuery):
   """
   getBillingPlanVersionById - [will be deprecated; do not use] use billingPlanVersion query

   """
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject):
      billingPlanVersionId: NonNull_str

   _args: BillingPlanVersionArgs


   type: BillingPlanVersion

class billingPlanVersion(GQLQuery):
   """
   billingPlanVersion - Get Billing Plan Version details

   """
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: BillingPlanVersionArgs


   type: BillingPlanVersion

class billingPlanVersions(GQLQuery):
   """
   billingPlanVersions -  Get Billing Plan versions\nPagination is not fully supported yet. 

   """
   class BillingPlanVersionConnectionArgs(GQLArgsSet, GQLObject):
      where: BillingPlanVersionWhereInput
      pagination: PaginationInput

   _args: BillingPlanVersionConnectionArgs


   type: BillingPlanVersionConnection

class calculatedStatisticsByEndpointAndApiversion(GQLQuery):
   """
   calculatedStatisticsByEndpointAndApiversion - Get API usage analytics by endpoint and API Version

   """
   class CalculatedStatisticsArgs(GQLArgsSet, GQLObject):
      fromDate: NonNull_str
      toDate: NonNull_str
      resolution: str
      endpointsAndApiVersions: NonNull_list_endpointsAndApiVersionCouples[endpointsAndApiVersionCouples]
      groupBy: StatsGroupBy
      apiId: NonNull_str
      entityId: ID
      timeOffset: int
      filters: list_StatsFilterBy[StatsFilterBy]

   _args: CalculatedStatisticsArgs


   type: CalculatedStatistics

class categoriesV2(GQLQuery):
   """
   categoriesV2 - [will be deprecated; do not use] Returns a list categories

   """
   class CategoryConnectionArgs(GQLArgsSet, GQLObject):
      where: CategoryWhereInput
      orderBy: CategoryOrderByInput
      pagination: PaginationInput

   _args: CategoryConnectionArgs


   type: CategoryConnection

class categoryEntities(GQLQuery):
   """
   categoryEntities - [will be deprecated; do not use] Return the category entity information

   """
   class CategoryEntityArgs(GQLArgsSet, GQLObject):
      lang: str
      pagingArgs: PagingArgs

   _args: CategoryEntityArgs


   type: list_CategoryEntity[CategoryEntity]

class categories(GQLQuery):
   """
   categories - [will be deprecated; do not use] Returns a list of categories based on search inputs

   """
   class CategoryArgs(GQLArgsSet, GQLObject):
      orderByField: str
      orderDirection: OrderDirection

   _args: CategoryArgs


   type: list_Category[Category]

class collectionsItemsByIds(GQLQuery):
   """
   collectionsItemsByIds - Returns the collections of items by IDs

   """
   class CollectionItemArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[ID]

   _args: CollectionItemArgs


   type: list_CollectionItem[CollectionItem]

class collections(GQLQuery):
   """
   collections - Get API collection list

   """
   class CollectionsResponseArgs(GQLArgsSet, GQLObject):
      where: CollectionsWhereInput
      orderBy: CollectionsOrderByInput
      minWeightToFetchApis: int

   _args: CollectionsResponseArgs


   type: CollectionsResponse

class collectionsByOwnerId(GQLQuery):
   """
   collectionsByOwnerId - Returns the collections for a specific tenant id (Assumption Owner = tenant in this context)

   """
   class CollectionsResponseArgs(GQLArgsSet, GQLObject):
      orderByField: str
      orderDirection: OrderDirection
      minWeightToFetchApis: int
      collection_type: str

   _args: CollectionsResponseArgs


   type: CollectionsResponse

class getOrgHomepageCollections(GQLQuery):
   """
   getOrgHomepageCollections - Returns a list of collections for a specific organization

   """
   class CollectionsResponseArgs(GQLArgsSet, GQLObject):
      orderByField: str
      orderDirection: OrderDirection
      minWeightToFetchApis: int

   _args: CollectionsResponseArgs


   type: CollectionsResponse

class collectionById(GQLQuery):
   """
   collectionById - Returns a collection based on Collection ID

   """
   class CollectionArgs(GQLArgsSet, GQLObject):
      collectionId: NonNull_ID

   _args: CollectionArgs


   type: Collection

class collection(GQLQuery):
   """
   collection - Returns a collection based on Collection ID

   """
   class CollectionArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: CollectionArgs


   type: Collection

class collapsedCollections(GQLQuery):
   """
   collapsedCollections - Get the list of collapsed Collections

   """
   class CollapsedCollectionArgs(GQLArgsSet, GQLObject):
      orderByField: str
      orderDirection: OrderDirection
      limit: int
      page: int

   _args: CollapsedCollectionArgs


   type: list_CollapsedCollection[CollapsedCollection]

class collectionBySlugifiedKey(GQLQuery):
   """
   collectionBySlugifiedKey - Returns a collection based on name

   """
   class CollectionArgs(GQLArgsSet, GQLObject):
      slugifiedKey: str

   _args: CollectionArgs


   type: Collection

class getPrivateCollections(GQLQuery):
   """
   getPrivateCollections - [Marked for deprecation; do not use ]Returns private collection

   """
   type: list_Collection[Collection]

class getPrivateCollectionsV2(GQLQuery):
   """
   getPrivateCollectionsV2 - Returns private collection

   """
   type: list_Collection[Collection]

class collectionBySlugifiedKeyV2(GQLQuery):
   """
   collectionBySlugifiedKeyV2 - Returns a collection based on name V2

   """
   class CollectionV2Args(GQLArgsSet, GQLObject):
      slugifiedKey: str

   _args: CollectionV2Args


   type: CollectionV2

class collectionBySlugifiedKeyV3(GQLQuery):
   """
   collectionBySlugifiedKeyV3 - Returns a collection based on name V3

   """
   class CollectionV3Args(GQLArgsSet, GQLObject):
      slugifiedKey: str

   _args: CollectionV3Args


   type: CollectionV3

class getCommentsByIssueIdV2(GQLQuery):
   """
   getCommentsByIssueIdV2 - Returns the comments by an issue ID

   """
   class PaginatedCommentsArgs(GQLArgsSet, GQLObject):
      issueId: NonNull_int
      pagingArgs: PagingArgs

   _args: PaginatedCommentsArgs


   type: PaginatedComments

class getCommentByIdV2(GQLQuery):
   """
   getCommentByIdV2 - Returns the comment by an issue and comment ID

   """
   class CommentArgs(GQLArgsSet, GQLObject):
      issueId: NonNull_int
      commentId: NonNull_int

   _args: CommentArgs


   type: Comment

class search(GQLQuery):
   """
   search - Returns a list of APIs based on search parameters

   """
   class ApiSearchArgs(GQLArgsSet, GQLObject):
      term: NonNull_str

   _args: ApiSearchArgs


   type: ApiSearch

class searchEntityByApiId(GQLQuery):
   """
   searchEntityByApiId - Search for a specific entity within a specific API

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      userName: NonNull_str
      apiId: NonNull_str
      distinct: str

   _args: AnyArgs


   type: list[Any]

class getOpenApiSpecByApiId(GQLQuery):
   """
   getOpenApiSpecByApiId - [will be deprecated; do not use] returns the OAS for the API ID parameter provided

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      apiId: ID

   _args: AnyArgs


   type: Any

class entityById(GQLQuery):
   """
   entityById - returns (User/Team/organization) by entityId

   """
   class EntityArgs(GQLArgsSet, GQLObject):
      id: ID

   _args: EntityArgs


   type: Entity

class activeEntity(GQLQuery):
   """
   activeEntity - The entity ( User/Team ) making the request 

   """
   type: Entity

class apiByNameAndOwnerName(GQLQuery):
   """
   apiByNameAndOwnerName - [will be deprecated; do not use] Query an API by Name and Owner Name

   """
   class ApiArgs(GQLArgsSet, GQLObject):
      apiName: str
      ownerName: str

   _args: ApiArgs


   type: Api

class apiBySlugifiedNameAndOwnerName(GQLQuery):
   """
   apiBySlugifiedNameAndOwnerName - [will be deprecated; do not use] Query and API by Slugified Name and Owner Name

   """
   class ApiArgs(GQLArgsSet, GQLObject):
      slugifiedName: str
      ownerName: str

   _args: ApiArgs


   type: Api

class apiByNameAndOwnerId(GQLQuery):
   """
   apiByNameAndOwnerId - [will be deprecated; do not use] Query an API by Name and Owner Id

   """
   class ApiArgs(GQLArgsSet, GQLObject):
      apiName: str
      ownerId: str

   _args: ApiArgs


   type: Api

class userFollows(GQLQuery):
   """
   userFollows - Query the ID of a user and get back the users they follow.

   """
   class FollowUserArgs(GQLArgsSet, GQLObject):
      userId: int

   _args: FollowUserArgs


   type: list_FollowUser[FollowUser]

class apiById(GQLQuery):
   """
   apiById - [will be deprecated; do not use] Query an API by id

   """
   class ApiArgs(GQLArgsSet, GQLObject):
      apiId: str

   _args: ApiArgs


   type: Api

class apisById(GQLQuery):
   """
   apisById - [will be deprecated; do not use] Get APIs by Id

   """
   class ApiArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[ID]

   _args: ApiArgs


   type: list_Api[Api]

class followUserAction(GQLQuery):
   """
   followUserAction - **This needs to be updated to a mutation** Follow a provider

   """
   class FollowPairArgs(GQLArgsSet, GQLObject):
      followerId: int
      followeeId: int

   _args: FollowPairArgs


   type: FollowPair

class userFollowers(GQLQuery):
   """
   userFollowers - Get follows by user ID

   """
   class FollowerArgs(GQLArgsSet, GQLObject):
      userId: int

   _args: FollowerArgs


   type: list_Follower[Follower]

class calculateSeatsPrice(GQLQuery):
   """
   calculateSeatsPrice - Calculate the seat price

   """
   class floatArgs(GQLArgsSet, GQLObject):
      seats: NonNull_int

   _args: floatArgs


   type: float

class getSeatsTransactionsByOrgId(GQLQuery):
   """
   getSeatsTransactionsByOrgId -   Return a list of transactions for seats by organization Id

   """
   class OrgTransactionArgs(GQLArgsSet, GQLObject):
      orgId: NonNull_int

   _args: OrgTransactionArgs


   type: list_OrgTransaction[OrgTransaction]

class organizationsTreeToken(GQLQuery):
   """
   organizationsTreeToken - Getting organization hierarchy of API requestor encode by JWT 

   """
   type: str

class getMinimumSeats(GQLQuery):
   """
   getMinimumSeats - Get the default seats configuration 

   """
   type: int

class transactionsById(GQLQuery):
   """
   transactionsById - Get a transaction based on an API Id or a User Id

   """
   class TransactionsPagingArgs(GQLArgsSet, GQLObject):
      apiId: str
      userId: int
      type: str
      pagingArgs: PagingArgs
      queryFilters: QueryFilters
      paymentStatusFilters: list[TransactionPaymentStatus]

   _args: TransactionsPagingArgs


   type: TransactionsPaging

class unionDiscussionsByAuthor(GQLQuery):
   """
   unionDiscussionsByAuthor - [marked for deprecation; do not use] Returns discussions by author

   """
   class DiscussionObjectArgs(GQLArgsSet, GQLObject):
      authorId: int
      limit: int
      offset: int
      orderField: str
      orderType: str
      type: str

   _args: DiscussionObjectArgs


   type: DiscussionObject

class getActiveUserContext(GQLQuery):
   """
   getActiveUserContext - Get the active user context of the logged in user 

   """
   type: ContextEntity

class getActiveTeamContext(GQLQuery):
   """
   getActiveTeamContext - Get the active team context of the logged in user

   """
   type: ContextEntity

class transactionsAnalyticsByApiId(GQLQuery):
   """
   transactionsAnalyticsByApiId - Returns the transactions analytics for one API by ID

   """
   class TransactionsAnalyticsArgs(GQLArgsSet, GQLObject):
      apiId: str
      fromDate: str
      toDate: str
      attributes: str

   _args: TransactionsAnalyticsArgs


   type: TransactionsAnalytics

class getConsumers(GQLQuery):
   """
   getConsumers - Gets a list of consumers for an API by type (Free, Paid, All)

   """
   class ConsumersArgs(GQLArgsSet, GQLObject):
      apiId: str
      userId: list[int]
      offset: int
      limit: int
      sort: str
      usernames: str
      plansFilter: list[str]
      lastActive: list[str]

   _args: ConsumersArgs


   type: Consumers

class getFreeConsumers(GQLQuery):
   """
   getFreeConsumers - Return free users by Api Id

   """
   class ConsumersArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_list[NonNull_ID]
      offset: int
      limit: int
      order: str
      lastActive: list[str]
      username: list[str]
      userId: list[int]

   _args: ConsumersArgs


   type: Consumers

class consumers(GQLQuery):
   """
   consumers - return all the consumers based on the API ID

   """
   class ConsumerConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_ConsumersWhereInput

   _args: ConsumerConnectionArgs


   type: ConsumerConnection

class requestAdminToSubscribeToAnAPI(GQLQuery):
   """
   requestAdminToSubscribeToAnAPI - [will be deprecated; do not use] requesting subscribe to an API 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      eventData: NonNull_ContactAdminSubscribeToAPIEvent

   _args: boolArgs


   type: bool

class getCountryMetadata(GQLQuery):
   """
   getCountryMetadata - Get metadata about a Country

   """
   class CountryArgs(GQLArgsSet, GQLObject):
      ip: str

   _args: CountryArgs


   type: Country

class unionIssuesByAuthorV2(GQLQuery):
   """
   unionIssuesByAuthorV2 - Returns discussions by author

   """
   class DiscussionObjectArgs(GQLArgsSet, GQLObject):
      authorId: int
      type: str
      pagingArgs: PagingArgs
      apiIds: list[str]

   _args: DiscussionObjectArgs


   type: DiscussionObject

class getIssuesByApiIdV2(GQLQuery):
   """
   getIssuesByApiIdV2 - Returns the issues associated with an API id

   """
   class IssueObjectArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_str
      pagingArgs: PagingArgs
      providerId: str

   _args: IssueObjectArgs


   type: IssueObject

class getIssuesByApiIdsV2(GQLQuery):
   """
   getIssuesByApiIdsV2 - Returns the issues associated with an APIs ids

   """
   class IssueObjectArgs(GQLArgsSet, GQLObject):
      apiIds: list[NonNull_str]
      pagingArgs: PagingArgs

   _args: IssueObjectArgs


   type: IssueObject

class endpointStats(GQLQuery):
   """
   endpointStats - The analytics for each endpoint

   """
   class EndpointStatsArgs(GQLArgsSet, GQLObject):
      apiIds: NonNull_list[ID]
      projectIds: list[ID]
      endpointIds: list[ID]
      fromDate: str
      toDate: str
      resolution: str

   _args: EndpointStatsArgs


   type: list_EndpointStats[EndpointStats]

class endpointStatsByEntity(GQLQuery):
   """
   endpointStatsByEntity - The analytics for each endpoint by entity

   """
   class EndpointStatsArgs(GQLArgsSet, GQLObject):
      entityId: ID
      apiId: NonNull_ID
      endpointIds: list[ID]
      fromDate: DateTime
      toDate: DateTime
      resolution: Resolution
      timeOffset: int
      filters: list_StatsFilterBy[StatsFilterBy]

   _args: EndpointStatsArgs


   type: list_EndpointStats[EndpointStats]

class endpointStatsByEntityV2(GQLQuery):
   """
   endpointStatsByEntityV2 - The analytics for each endpoint by entity v2

   """
   class VersionEndpointStatsArgs(GQLArgsSet, GQLObject):
      entityId: ID
      apiId: NonNull_ID
      endpointsAndApiVersions: list_EndpointAndVersion[EndpointAndVersion]
      fromDate: DateTime
      toDate: DateTime
      resolution: Resolution
      timeOffset: int
      filters: list_StatsFilterBy[StatsFilterBy]

   _args: VersionEndpointStatsArgs


   type: list_VersionEndpointStats[VersionEndpointStats]

class getEndpointsWithinDateByParameters(GQLQuery):
   """
   getEndpointsWithinDateByParameters - Get the endpoints of an API within a date range

   """
   class EndpointStatsArgs(GQLArgsSet, GQLObject):
      input: NonNull_endpointsWithinDateInput
      showDeleted: bool

   _args: EndpointStatsArgs


   type: list_EndpointStats[EndpointStats]

class endpoint(GQLQuery):
   """
   endpoint - Get an Endpoint

   """
   class EndpointArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: EndpointArgs


   type: Endpoint

class endpoints(GQLQuery):
   """
   endpoints - Get a list of endpoints

   """
   class EndpointConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_EndpointWhereInput

   _args: EndpointConnectionArgs


   type: EndpointConnection

class searchEntities(GQLQuery):
   """
   searchEntities - Search for API by all associated entities (e.g. users, types, etc...)

   """
   class EntityArgs(GQLArgsSet, GQLObject):
      term: str
      limit: int
      status: str
      type: str

   _args: EntityArgs


   type: list_Entity[Entity]

class entitiesMetadata(GQLQuery):
   class EntityMetadataConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_EntityMetadataWhereInput
      orderBy: EntityMetadataOrderByInput
      pagination: PaginationInput

   _args: EntityMetadataConnectionArgs


   type: EntityMetadataConnection

class getEntitiesRoles(GQLQuery):
   """
   getEntitiesRoles - get Entity (User/Team/Organization ) assigned roles 

   """
   class EntityRoleArgs(GQLArgsSet, GQLObject):
      entityIds: list[int]
      orgId: int
      parentIds: list[int]

   _args: EntityRoleArgs


   type: list_EntityRole[EntityRole]

class entitiesRoles(GQLQuery):
   """
   entitiesRoles - get roles assigned to Entity

   """
   class EntityRoleConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_EntityRoleWhereInput
      orderBy: EntityRoleOrderByInput
      pagination: PaginationInput

   _args: EntityRoleConnectionArgs


   type: EntityRoleConnection

class getLogsCSV(GQLQuery):
   """
   getLogsCSV - Export analytics to a CSV file

   """
   class LogsCSVArgs(GQLArgsSet, GQLObject):
      apiId: ID
      projectId: ID

   _args: LogsCSVArgs


   type: list_LogsCSV[LogsCSV]

class exportLogsCSVProvider(GQLQuery):
   """
   exportLogsCSVProvider - Export CSV of audit trails for Provider related actions

   """
   class LogsCSVExportsArgs(GQLArgsSet, GQLObject):
      contextId: NonNull_ID
      fromDate: NonNull_DateTime
      toDate: NonNull_DateTime
      totalCount: NonNull_int
      filters: RequestLogFilters
      timeOffset: int

   _args: LogsCSVExportsArgs


   type: LogsCSVExports

class exportLogsCSVDeveloper(GQLQuery):
   """
   exportLogsCSVDeveloper - Export CSV of audit trails for Developer related actions

   """
   class LogsCSVExportsArgs(GQLArgsSet, GQLObject):
      contextId: NonNull_ID
      fromDate: NonNull_DateTime
      toDate: NonNull_DateTime
      totalCount: NonNull_int
      filters: RequestLogFilters
      timeOffset: int

   _args: LogsCSVExportsArgs


   type: LogsCSVExports

class gateways(GQLQuery):
   """
   gateways - [will be deprecated; do not use] Get all gateway instance

   """
   type: GatewayConnection

class getGateways(GQLQuery):
   """
   getGateways - Return a list of Gateways

   """
   type: list_Gateway[Gateway]

class getGatewayConfiguration(GQLQuery):
   """
   getGatewayConfiguration - Get the configuration of a Gateway

   """
   class ApiGatewayConfigurationArgs(GQLArgsSet, GQLObject):
      id: NonNull_int

   _args: ApiGatewayConfigurationArgs


   type: ApiGatewayConfiguration

class graphQlIntrospectionSchema(GQLQuery):
   """
   graphQlIntrospectionSchema - Get the current GraphQL __schema using introspectionCall query

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      introspectionCallUrl: NonNull_str

   _args: AnyArgs


   type: Any

class headlinesByApiNameAndOwnerId(GQLQuery):
   """
   headlinesByApiNameAndOwnerId - Get the API readme by ownerId

   """
   class HeadlineArgs(GQLArgsSet, GQLObject):
      apiName: str
      apiOwnerId: str
      size: int

   _args: HeadlineArgs


   type: list_Headline[Headline]

class getIssuesByOrganizatonId(GQLQuery):
   """
   getIssuesByOrganizatonId - Return the issues associated with an organziation Id

   """
   class IssueObjectArgs(GQLArgsSet, GQLObject):
      id: NonNull_str
      pagingArgs: PagingArgs

   _args: IssueObjectArgs


   type: IssueObject

class getResponseTimeByProviderId(GQLQuery):
   """
   getResponseTimeByProviderId - returns provider response time 

   """
   class floatArgs(GQLArgsSet, GQLObject):
      providerId: NonNull_int

   _args: floatArgs


   type: float

class getAverageResponseTime(GQLQuery):
   """
   getAverageResponseTime - Returns the average API Response Time

   """
   type: float

class unionIssuesByAuthor(GQLQuery):
   """
   unionIssuesByAuthor - [marked for deprecation; do not use] Returns discussions by author

   """
   class DiscussionObjectArgs(GQLArgsSet, GQLObject):
      authorId: int
      type: str
      pagingArgs: PagingArgs

   _args: DiscussionObjectArgs


   type: DiscussionObject

class getIssueByIdV2(GQLQuery):
   """
   getIssueByIdV2 - Returns the issues by Id

   """
   class IssueArgs(GQLArgsSet, GQLObject):
      issueId: int

   _args: IssueArgs


   type: Issue

class getIssuesByOrganizationId(GQLQuery):
   """
   getIssuesByOrganizationId - Return the issues associated with an organziation Id

   """
   class IssueObjectArgs(GQLArgsSet, GQLObject):
      id: str
      pagingArgs: PagingArgs

   _args: IssueObjectArgs


   type: IssueObject

class getIssuesByTeamIdV2(GQLQuery):
   """
   getIssuesByTeamIdV2 - Returns the issues associated with a team id

   """
   class IssueObjectArgs(GQLArgsSet, GQLObject):
      id: str
      pagingArgs: PagingArgs

   _args: IssueObjectArgs


   type: IssueObject

class getIssuesFollowsByUserIdV2(GQLQuery):
   """
   getIssuesFollowsByUserIdV2 - Returns issues for APIs followed by a user

   """
   class IssueFollowArgs(GQLArgsSet, GQLObject):
      userId: int

   _args: IssueFollowArgs


   type: list_IssueFollow[IssueFollow]

class kafkaConfiguration(GQLQuery):
   """
   kafkaConfiguration - returns the kafka configuration for the apiVersion

   """
   class KafkaConfigurationArgs(GQLArgsSet, GQLObject):
      apiVersionId: NonNull_str

   _args: KafkaConfigurationArgs


   type: KafkaConfiguration

class kafkaTopics(GQLQuery):
   """
   kafkaTopics - returns a list of all the kafka topics related to the apiVersion

   """
   class KafkaTopicsArgs(GQLArgsSet, GQLObject):
      apiVersionId: NonNull_str

   _args: KafkaTopicsArgs


   type: KafkaTopics

class kafkaSchemas(GQLQuery):
   """
   kafkaSchemas - returns a list of all the kafka schemas related to the apiVersion

   """
   class KafkaSchemasArgs(GQLArgsSet, GQLObject):
      apiVersionId: NonNull_str

   _args: KafkaSchemasArgs


   type: KafkaSchemas

class kafkaTopicMetadata(GQLQuery):
   """
   kafkaTopicMetadata - returns the kafka topic metadata

   """
   class TopicMetadataResponseArgs(GQLArgsSet, GQLObject):
      apiVersionId: NonNull_str
      topicName: NonNull_str

   _args: TopicMetadataResponseArgs


   type: TopicMetadataResponse

class getTemplate(GQLQuery):
   """
   getTemplate - Gets the document for Docusign workflow

   """
   class EnvelopeTemplateArgs(GQLArgsSet, GQLObject):
      accountId: str
      templateId: str

   _args: EnvelopeTemplateArgs


   type: EnvelopeTemplate

class getLegalAgreementInfo(GQLQuery):
   """
   getLegalAgreementInfo - Gets the created legal document provider information

   """
   type: LegalAgreementInfo

class updateLegalAgreementInfo(GQLQuery):
   """
   updateLegalAgreementInfo - Update the attributes attached to an API's legal agreement

   """
   class LegalAgreementInfoArgs(GQLArgsSet, GQLObject):
      input: UpdateLegalAgreementInfo

   _args: LegalAgreementInfoArgs


   type: LegalAgreementInfo

class createLegalAgreementInfo(GQLQuery):
   """
   createLegalAgreementInfo - Create a new legal agreement provider integration for API plans

   """
   class LegalAgreementInfoArgs(GQLArgsSet, GQLObject):
      input: CreateLegalAgreementInfo

   _args: LegalAgreementInfoArgs


   type: LegalAgreementInfo

class deleteLegalAgreementInfo(GQLQuery):
   """
   deleteLegalAgreementInfo - Upadte existing legal agreement provider integration for API plans

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      entityId: str

   _args: AnyArgs


   type: Any

class getLegalAgreementSigningURL(GQLQuery):
   """
   getLegalAgreementSigningURL - Build a legal agreement signging url for the UI as an external integration for signing on plans 

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_GetLegalAgreementSigningURLInput

   _args: AnyArgs


   type: Any

class logPayloadByRequestId(GQLQuery):
   """
   logPayloadByRequestId - Returns the details of a request by Id

   """
   class LogPayloadArgs(GQLArgsSet, GQLObject):
      requestId: ID
      callTime: str

   _args: LogPayloadArgs


   type: LogPayload

class logPayloadByRequestIdWithLoggingRestrictions(GQLQuery):
   """
   logPayloadByRequestIdWithLoggingRestrictions - Returns the details of the request by Id with logging restrictions

   """
   class RestrictedLogPayloadArgs(GQLArgsSet, GQLObject):
      requestId: ID
      callTime: str
      apiId: str

   _args: RestrictedLogPayloadArgs


   type: RestrictedLogPayload

class developerLogPayloadByRequestIdWithLoggingRestrictions(GQLQuery):
   """
   developerLogPayloadByRequestIdWithLoggingRestrictions - Get request payload for developer

   """
   class RestrictedLogPayloadArgs(GQLArgsSet, GQLObject):
      requestId: ID
      callTime: str
      apiId: str
      projectId: str

   _args: RestrictedLogPayloadArgs


   type: RestrictedLogPayload

class messageThreads(GQLQuery):
   """
   messageThreads - Search for message threads by specific filters

   """
   class MessageThreadsObjectArgs(GQLArgsSet, GQLObject):
      where: MessageThreadsWhereInput

   _args: MessageThreadsObjectArgs


   type: MessageThreadsObject

class messages(GQLQuery):
   """
   messages - Get messages by filters

   """
   class MessageArgs(GQLArgsSet, GQLObject):
      where: NonNull_MessagesWhereInput

   _args: MessageArgs


   type: list_Message[Message]

class getApiAverageResponseTime(GQLQuery):
   """
   getApiAverageResponseTime - Returns the average API Response Time

   """
   class floatArgs(GQLArgsSet, GQLObject):
      apiId: NonNull_str

   _args: floatArgs


   type: float

class getProviderAverageResponseTime(GQLQuery):
   """
   getProviderAverageResponseTime - Get providers average response time for responding to an private message 

   """
   class floatArgs(GQLArgsSet, GQLObject):
      providerId: NonNull_int

   _args: floatArgs


   type: float

class getRelativeAverageResponseTime(GQLQuery):
   """
   getRelativeAverageResponseTime - returns provider response time compared to other providers

   """
   class RelativeARTResponseArgs(GQLArgsSet, GQLObject):
      providerId: NonNull_int

   _args: RelativeARTResponseArgs


   type: RelativeARTResponse

class getMessageThread(GQLQuery):
   """
   getMessageThread - Get the messages of a thread

   """
   class MessageThreadArgs(GQLArgsSet, GQLObject):
      threadId: int

   _args: MessageThreadArgs


   type: MessageThread

class newNotificationsByUserId(GQLQuery):
   """
   newNotificationsByUserId - [will be deprecated; do not use] Get new notifications by User Id

   """
   class NewNotificationArgs(GQLArgsSet, GQLObject):
      userId: int
      limit: int
      offset: int

   _args: NewNotificationArgs


   type: list_NewNotification[NewNotification]

class notificationsByUserId(GQLQuery):
   """
   notificationsByUserId - [will be deprecated; do not use] Get notifications by User Id

   """
   class NotificationArgs(GQLArgsSet, GQLObject):
      userId: int
      limit: int
      offset: int

   _args: NotificationArgs


   type: list_Notification[Notification]

class organization(GQLQuery):
   """
   organization - Getting an organization list of the API requestor

   """
   class OrganizationArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: OrganizationArgs


   type: Organization

class organizations(GQLQuery):
   """
   organizations - Obtains a list of organizations in which the API requester is an organization administrator. The **teams** field returns an array of teams in each organization. The **users** field returns an array of users in the organization.

   """
   class OrganizationArgs(GQLArgsSet, GQLObject):
      where: OrganizationWhereInput

   _args: OrganizationArgs


   type: list_Organization[Organization]

class getOrganizations(GQLQuery):
   """
   getOrganizations - Get organization of user executing the query

   """
   type: list_Organization[Organization]

class getOrganizationBySlugifiedName(GQLQuery):
   """
   getOrganizationBySlugifiedName - [will be deprecated; do not use] returns the organization based on the Sluggified name

   """
   class OrganizationArgs(GQLArgsSet, GQLObject):
      slugifiedName: str

   _args: OrganizationArgs


   type: Organization

class getOrganizationById(GQLQuery):
   """
   getOrganizationById - [will be deprecated; do not use]  returns the organization based on the orgId

   """
   class OrganizationArgs(GQLArgsSet, GQLObject):
      orgId: NonNull_ID

   _args: OrganizationArgs


   type: Organization

class getEmailDomainAndCheckIfIgnored(GQLQuery):
   """
   getEmailDomainAndCheckIfIgnored - Get the email domain and check if it's ignored by an org

   """
   type: CorporateDomain

class getOrganizationsWithTheSameEmail(GQLQuery):
   """
   getOrganizationsWithTheSameEmail - Get organizations that were created by an admin and his/her email domain matches the API caller domain 

   """
   type: list_CorporateDomainOrganization[CorporateDomainOrganization]

class searchOrganizations(GQLQuery):
   """
   searchOrganizations - Returns a list of organizations

   """
   class EntityArgs(GQLArgsSet, GQLObject):
      term: str
      limit: int

   _args: EntityArgs


   type: list_Entity[Entity]

class validateResetPasswordToken(GQLQuery):
   """
   validateResetPasswordToken - Takes a password reset token and returns whether it is valid

   """
   class ValidateTokenResponseArgs(GQLArgsSet, GQLObject):
      token: NonNull_str

   _args: ValidateTokenResponseArgs


   type: ValidateTokenResponse

class getProjectAllowedAPIs(GQLQuery):
   """
   getProjectAllowedAPIs - Returns the allowed API IDs by Project/App

   """
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject):
      mashapeId: NonNull_str
      projectId: NonNull_int
      pagingArgs: PagingArgs

   _args: ProjectAllowedAPIArgs


   type: list_ProjectAllowedAPI[ProjectAllowedAPI]

class requestLogsByEntity(GQLQuery):
   """
   requestLogsByEntity - getting API calls logs associated to an application 

   """
   class RequestLogsResultArgs(GQLArgsSet, GQLObject):
      apiId: str
      projectId: str
      fromDate: NonNull_str
      toDate: str
      limit: int
      offset: int
      orderBy: RequestLogsOrderBy
      orderDir: OrderDirection
      filters: RequestLogFilters
      timeOffset: int

   _args: RequestLogsResultArgs


   type: RequestLogsResult

class getAccessControlRoles(GQLQuery):
   """
   getAccessControlRoles - Get all roles

   """
   class RoleArgs(GQLArgsSet, GQLObject):
      roleLevels: list[RoleLevel]

   _args: RoleArgs


   type: list_Role[Role]

class getRoles(GQLQuery):
   """
   getRoles - Get all defined roles 

   """
   class RoleArgs(GQLArgsSet, GQLObject):
      roleLevels: list[RoleLevel]

   _args: RoleArgs


   type: list_Role[Role]

class roles(GQLQuery):
   """
   roles - get roles metada

   """
   class RoleConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_RoleWhereInput
      orderBy: RoleOrderByInput
      pagination: PaginationInput

   _args: RoleConnectionArgs


   type: RoleConnection

class searchApis(GQLQuery):
   """
   searchApis - Returns a list of APIs based on search parameters

   """
   class SearchApiConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_SearchApiWhereInput
      orderBy: SearchApiOrderByInput
      pagination: PaginationInput

   _args: SearchApiConnectionArgs


   type: SearchApiConnection

class searchBlogPosts(GQLQuery):
   """
   searchBlogPosts - Returns a list of blog posts based on search parameters

   """
   class SearchBlogPostConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_SearchBlogPostWhereInput
      pagination: PaginationInput

   _args: SearchBlogPostConnectionArgs


   type: SearchBlogPostConnection

class searchCollections(GQLQuery):
   """
   searchCollections - Returns list of collections 

   """
   class SearchCollectionConnectionArgs(GQLArgsSet, GQLObject):
      where: SearchCollectionWhereInput
      orderBy: SearchCollectionOrderByInput
      pagination: PaginationInput

   _args: SearchCollectionConnectionArgs


   type: SearchCollectionConnection

class spotlights(GQLQuery):
   """
   spotlights - Returns the spotlights for a specific API

   """
   class SpotlightConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_SpotlightWhereInput
      orderBy: SpotlightOrderByInput
      pagination: PaginationInput

   _args: SpotlightConnectionArgs


   type: SpotlightConnection

class searchSubscribedEntityByApiIdAndAppName(GQLQuery):
   """
   searchSubscribedEntityByApiIdAndAppName - Returns a list of entities subscribed to an API and App Name

   """
   class ProjectArgs(GQLArgsSet, GQLObject):
      appName: NonNull_str
      apiId: NonNull_str

   _args: ProjectArgs


   type: list_Project[Project]

class activeSubscriptionsCount(GQLQuery):
   """
   activeSubscriptionsCount - [will be deprecated; do not use] Returns analytics data about an API per subscription by API id 

   """
   class ActiveSubscriptionCountArgs(GQLArgsSet, GQLObject):
      apiId: str
      fromDate: str
      toDate: str
      resolution: Resolution

   _args: ActiveSubscriptionCountArgs


   type: list_ActiveSubscriptionCount[ActiveSubscriptionCount]

class getInternalSubscriptions(GQLQuery):
   """
   getInternalSubscriptions - Get the subscriptions of a team that subscribed to other teams' APIs within the same org

   """
   type: list_BillingSubscription[BillingSubscription]

class searchSubscribedEntityByApiId(GQLQuery):
   """
   searchSubscribedEntityByApiId - Returns a list of entities subscribed to an API

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      userName: NonNull_str
      apiId: NonNull_str

   _args: AnyArgs


   type: list[Any]

class getSubscriptions(GQLQuery):
   """
   getSubscriptions - [will be deprecated; do not use] Get subscriptions by Id

   """
   class SubscriptionsPagingArgs(GQLArgsSet, GQLObject):
      id: int
      userId: int
      apiId: str
      mashapeId: str
      pagingArgs: PagingArgs

   _args: SubscriptionsPagingArgs


   type: SubscriptionsPaging

class getOrganizationSubscriptions(GQLQuery):
   """
   getOrganizationSubscriptions - [will be deprecated; do not use] Get the subscriptions owned by an organization

   """
   class OrgSubscriptionsArgs(GQLArgsSet, GQLObject):
      pagingArgs: PagingArgs

   _args: OrgSubscriptionsArgs


   type: OrgSubscriptions

class subscriptions(GQLQuery):
   """
   subscriptions - Returns a set of subscriptions

   """
   class SubscriptionConnectionArgs(GQLArgsSet, GQLObject):
      where: SubscriptionsWhereInput
      pagination: PaginationInput

   _args: SubscriptionConnectionArgs


   type: SubscriptionConnection

class subscription(GQLQuery):
   """
   subscription - Returns one subscription.

   """
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      id: int

   _args: BillingSubscriptionArgs


   type: BillingSubscription

class subscriptionsCount(GQLQuery):
   """
   subscriptionsCount - Returns the count of a set of subscriptions by date range

   """
   class SubscriptionsCountArgs(GQLArgsSet, GQLObject):
      where: SubscriptionsCountWhereInput

   _args: SubscriptionsCountArgs


   type: list_SubscriptionsCount[SubscriptionsCount]

class getTagsList(GQLQuery):
   """
   getTagsList - gets defined tags list in environment level 

   """
   type: list_TagDefinition[TagDefinition]

class tagDefinitions(GQLQuery):
   """
   tagDefinitions - Returns the tag's definitions 

   """
   type: TagDefinitionConnection

class paginatedTeamUsersByOrganizationId(GQLQuery):
   """
   paginatedTeamUsersByOrganizationId - Get organization users ( should be deprecated , please don't use)

   """
   class PaginatedTeamUsersArgs(GQLArgsSet, GQLObject):
      orgId: NonNull_int
      pagingArgs: PagingArgs

   _args: PaginatedTeamUsersArgs


   type: PaginatedTeamUsers

class paginatedTeamUsersByOrganizationIdV2(GQLQuery):
   """
   paginatedTeamUsersByOrganizationIdV2 - Get organization users 

   """
   class PaginatedTeamUsersArgs(GQLArgsSet, GQLObject):
      orgId: NonNull_int
      pagingArgs: PagingArgs

   _args: PaginatedTeamUsersArgs


   type: PaginatedTeamUsers

class teamUserByEmailAndOrgId(GQLQuery):
   """
   teamUserByEmailAndOrgId - Get user in a team by email and Organization id

   """
   class TeamUserArgs(GQLArgsSet, GQLObject):
      email: str
      orgId: int

   _args: TeamUserArgs


   type: TeamUser

class teamUser(GQLQuery):
   """
   teamUser - Get user by organization Id

   """
   class TeamUserArgs(GQLArgsSet, GQLObject):
      where: NonNull_TeamUserWhereInput

   _args: TeamUserArgs


   type: TeamUser

class findUsersInOrganization(GQLQuery):
   """
   findUsersInOrganization - search users within organization by term 

   """
   class TeamUserArgs(GQLArgsSet, GQLObject):
      orgId: int
      term: str

   _args: TeamUserArgs


   type: list_TeamUser[TeamUser]

class teamByTeamId(GQLQuery):
   """
   teamByTeamId - get a team based on it's team id and organization id

   """
   class TeamArgs(GQLArgsSet, GQLObject):
      teamId: int
      orgId: int

   _args: TeamArgs


   type: Team

class teamsByOrganizationId(GQLQuery):
   """
   teamsByOrganizationId - Get the team based on the Organization Id

   """
   class TeamArgs(GQLArgsSet, GQLObject):
      orgId: int

   _args: TeamArgs


   type: list_Team[Team]

class getTeamBySlugifiedName(GQLQuery):
   """
   getTeamBySlugifiedName - Gets teams by slugified key

   """
   class TeamArgs(GQLArgsSet, GQLObject):
      slugifiedName: str

   _args: TeamArgs


   type: Team

class searchTeams(GQLQuery):
   """
   searchTeams - Returns a list of teams

   """
   class TeamArgs(GQLArgsSet, GQLObject):
      term: str
      limit: int

   _args: TeamArgs


   type: list_Team[Team]

class team(GQLQuery):
   """
   team - get a team based on its id

   """
   class TeamArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: TeamArgs


   type: Team

class teams(GQLQuery):
   """
   teams - get list of teams based on OrgId and Slugified name

   """
   class TeamArgs(GQLArgsSet, GQLObject):
      where: TeamWhereInput

   _args: TeamArgs


   type: list_Team[Team]

class tenant(GQLQuery):
   """
   tenant - Get tenant by tenant ID.

   """
   type: Tenant

class transactions(GQLQuery):
   """
   transactions - Get all transactions by the filters in 'where' input.\n\nNote: Pagination using PaginationInput is only partially supported.\nUse PagingArgs in Where input instead, both for pagination and for sorting.

   """
   class TransactionConnectionArgs(GQLArgsSet, GQLObject):
      where: TransactionsWhereInput
      pagination: PaginationInput

   _args: TransactionConnectionArgs


   type: TransactionConnection

class transactionsSummary(GQLQuery):
   """
   transactionsSummary - Get details about transactions

   """
   class TransactionsSummaryArgs(GQLArgsSet, GQLObject):
      where: TransactionsSummaryWhereInput

   _args: TransactionsSummaryArgs


   type: TransactionsSummary

class transformations(GQLQuery):
   """
   transformations - Get a list of all the transformations from the API Version

   """
   class TransformationConnectionArgs(GQLArgsSet, GQLObject):
      where: TransformationWhereInput
      orderBy: TransformationOrderByInput
      pagination: PaginationInput

   _args: TransformationConnectionArgs


   type: TransformationConnection

class tutorials(GQLQuery):
   """
   tutorials - Returns the tutorials for a specified API

   """
   class TutorialConnectionArgs(GQLArgsSet, GQLObject):
      where: NonNull_TutorialWhereInput
      orderBy: TutorialOrderByInput
      pagination: PaginationInput

   _args: TutorialConnectionArgs


   type: TutorialConnection

class getPhoneNumbers(GQLQuery):
   """
   getPhoneNumbers - returns user configures phones for 2fa 

   """
   type: list_Phone[Phone]

class getRecoveryCodes(GQLQuery):
   """
   getRecoveryCodes - get Users recovery codes

   """
   type: list_RecoveryCode[RecoveryCode]

class isTwoFactorEnabledByType(GQLQuery):
   """
   isTwoFactorEnabledByType - is 2fa factor configured on a type 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      type: NonNull_str

   _args: boolArgs


   type: bool

class getUsagesAndParentUsageForSubscription(GQLQuery):
   """
   getUsagesAndParentUsageForSubscription - Get usage for subscriptions

   """
   class UsagesStatsArgs(GQLArgsSet, GQLObject):
      apiId: str
      subscriptionId: str
      billingItemIds: list[str]
      resolution: str
      orderDir: str
      periods: list[str]
      parentId: int
      isInternal: bool

   _args: UsagesStatsArgs


   type: list_UsagesStats[UsagesStats]

class getUsagesAgrregatedByTeamsForSubscription(GQLQuery):
   """
   getUsagesAgrregatedByTeamsForSubscription - Get usage aggregated by teams using organizationId and apiId

   """
   class UsagesStatsArgs(GQLArgsSet, GQLObject):
      apiId: str
      subscriptionId: str
      billingItemIds: list[str]
      resolution: str
      orderDir: str
      periods: list[str]
      apiVersionId: str
      internalData: list[str]

   _args: UsagesStatsArgs


   type: list_UsagesStats[UsagesStats]

class getUsagesAndParentUsageForSubscriptionByBuckets(GQLQuery):
   """
   getUsagesAndParentUsageForSubscriptionByBuckets - Get usage for subscriptions

   """
   class UsagesStatsArgs(GQLArgsSet, GQLObject):
      apiId: str
      subscriptionId: str
      billingItemIds: list[str]
      resolution: str
      periods: list[str]
      parentId: int

   _args: UsagesStatsArgs


   type: list_UsagesStats[UsagesStats]

class getUsagesAgrregatedByTeamsForSubscriptionByBuckets(GQLQuery):
   """
   getUsagesAgrregatedByTeamsForSubscriptionByBuckets - Get usage aggregated by teams using organizationId and apiId

   """
   class UsagesStatsArgs(GQLArgsSet, GQLObject):
      apiId: str
      subscriptionId: str
      billingItemIds: list[str]
      resolution: str
      periods: list[str]
      apiVersionId: str

   _args: UsagesStatsArgs


   type: list_UsagesStats[UsagesStats]

class organizationQuotaUsageByApiIdV2(GQLQuery):
   """
   organizationQuotaUsageByApiIdV2 - Returns the usage of an organization's quota by one API

   """
   class OrganizationApiUsagesV2Args(GQLArgsSet, GQLObject):
      apiId: ID
      apiVersionId: ID
      internalData: Any

   _args: OrganizationApiUsagesV2Args


   type: OrganizationApiUsagesV2

class getUserInviteByToken(GQLQuery):
   """
   getUserInviteByToken - Get all user invited instances by per organization level token 

   """
   class UserInviteArgs(GQLArgsSet, GQLObject):
      token: NonNull_str

   _args: UserInviteArgs


   type: UserInvite

class checkUserInvitesBranding(GQLQuery):
   """
   checkUserInvitesBranding - [will be deprecated; do not use] checks users branding

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: UserInvitesBrandingInput

   _args: boolArgs


   type: bool

class checkIfEmailsAlreadyInvited(GQLQuery):
   """
   checkIfEmailsAlreadyInvited - check if user is already invite to an organization 

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      orgId: NonNull_ID
      emails: NonNull_list[str]

   _args: AnyArgs


   type: Any

class searchUsersToInvite(GQLQuery):
   """
   searchUsersToInvite - Returns a list of users to invite

   """
   class InviteUsersSearchArgs(GQLArgsSet, GQLObject):
      orgId: NonNull_ID
      brand: str
      term: str
      offset: int
      limit: int

   _args: InviteUsersSearchArgs


   type: list_InviteUsersSearch[InviteUsersSearch]

class getUserSavedApis(GQLQuery):
   """
   getUserSavedApis - Gets uses saved APIs

   """
   class UserSavedApiArgs(GQLArgsSet, GQLObject):
      userCollectionId: str

   _args: UserSavedApiArgs


   type: UserSavedApi

class userById(GQLQuery):
   """
   userById - Get user by ID

   """
   class UserArgs(GQLArgsSet, GQLObject):
      id: int

   _args: UserArgs


   type: User

class userByUsername(GQLQuery):
   """
   userByUsername - Get user by username

   """
   class UserArgs(GQLArgsSet, GQLObject):
      username: str
      includeUserAttributes: bool

   _args: UserArgs


   type: User

class getPrivateApisJwt(GQLQuery):
   """
   getPrivateApisJwt - returns API caller private APIs id list encoded in a JWT

   """
   type: str

class searchUsers(GQLQuery):
   """
   searchUsers - Returns a list of users

   """
   class UserArgs(GQLArgsSet, GQLObject):
      brand: str
      term: str
      offset: int
      limit: int

   _args: UserArgs


   type: list_User[User]

class searchUsersV2(GQLQuery):
   """
   searchUsersV2 - Returns a list of users

   """
   class UserArgs(GQLArgsSet, GQLObject):
      where: NonNull_SearchUsersWhereInput

   _args: UserArgs


   type: User

class user(GQLQuery):
   """
   user - Get details about a user

   """
   class UserArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: UserArgs


   type: User

class users(GQLQuery):
   """
   users - Get users by any attribute type

   """
   class UserArgs(GQLArgsSet, GQLObject):
      where: NonNull_UserWhereInput

   _args: UserArgs


   type: list_User[User]

class getVirtualPermissions(GQLQuery):
   """
   getVirtualPermissions - Get full permission list associate to a permission 

   """
   class PermissionArgs(GQLArgsSet, GQLObject):
      permissionLevel: list[RoleLevel]

   _args: PermissionArgs


   type: list_Permission[Permission]

class virtualPermissions(GQLQuery):
   """
   virtualPermissions - Query by ID or display name to get back a virtual permission

   """
   class VirtualPermissionArgs(GQLArgsSet, GQLObject):
      where: NonNull_VirtualPermissionWhereInput

   _args: VirtualPermissionArgs


   type: list_VirtualPermission[VirtualPermission]

class getWorkflowsForProvider(GQLQuery):
   """
   getWorkflowsForProvider - Get the approval list requested to the the API caller that is a provider

   """
   class WorkFlowsResponseArgs(GQLArgsSet, GQLObject):
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: WorkFlowsResponseArgs


   type: WorkFlowsResponse

class getWorkflowsForDeveloper(GQLQuery):
   """
   getWorkflowsForDeveloper - Get the approval list requested by the API caller 

   """
   class WorkFlowsResponseArgs(GQLArgsSet, GQLObject):
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: WorkFlowsResponseArgs


   type: WorkFlowsResponse

class getWorkflowsByRequestor(GQLQuery):
   """
   getWorkflowsByRequestor - Get the approval list requested to the  the API caller

   """
   class WorkFlowsResponseArgs(GQLArgsSet, GQLObject):
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: WorkFlowsResponseArgs


   type: WorkFlowsResponse

class getWorkflowsByRequestee(GQLQuery):
   """
   getWorkflowsByRequestee - Get the approval list requested by the API caller

   """
   class WorkFlowsResponseArgs(GQLArgsSet, GQLObject):
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: WorkFlowsResponseArgs


   type: WorkFlowsResponse

class canWorkflowBeSubmitted(GQLQuery):
   """
   canWorkflowBeSubmitted - Determine if a workflow can be submitted

   """
   class boolArgs(GQLArgsSet, GQLObject):
      options: CanWorkflowBeSubmittedOptions

   _args: boolArgs


   type: bool

class getWorkflowAudits(GQLQuery):
   """
   getWorkflowAudits - Get workflows operations audits 

   """
   class WorkFlowAuditsResponseArgs(GQLArgsSet, GQLObject):
      workflowId: int

   _args: WorkFlowAuditsResponseArgs


   type: WorkFlowAuditsResponse

class getWorkflowsCount(GQLQuery):
   """
   getWorkflowsCount - get approval list count 

   """
   class intArgs(GQLArgsSet, GQLObject):
      options: GetWorkflowCountOptions

   _args: intArgs


   type: int

class exclusions(GQLQuery):
   """
   exclusions - Returns exclusions for Hub Extensions

   """
   class ExclusionArgs(GQLArgsSet, GQLObject):
      client: str
      page: str

   _args: ExclusionArgs


   type: list_Exclusion[Exclusion]


class Queries(Enum):
   ping = ping
   eventUrls = eventUrls
   eventUrl = eventUrl
   eventTypes = eventTypes
   eventConfig = eventConfig
   gatewayInstances = gatewayInstances
   gatewayInstance = gatewayInstance
   gatewayTemplates = gatewayTemplates
   gatewayTemplate = gatewayTemplate
   gatewayTemplatesParams = gatewayTemplatesParams
   gatewayTemplateParam = gatewayTemplateParam
   envConfigCategories = envConfigCategories
   envConfig = envConfig
   envConfigs = envConfigs
   adminAuditLogs = adminAuditLogs
   eventLogs = eventLogs
   extensions = extensions
   getSEOTagsByURL = getSEOTagsByURL
   getUserAlertById = getUserAlertById
   getUserAlertsByScope = getUserAlertsByScope
   getAlertsDefinitions = getAlertsDefinitions
   userAlerts = userAlerts
   userAlert = userAlert
   allowedPlanDeveloperByPlanId = allowedPlanDeveloperByPlanId
   apiCertificate = apiCertificate
   apiCertificates = apiCertificates
   apiDevelopersByApiId = apiDevelopersByApiId
   apiFollowers = apiFollowers
   apiReferenceByApiAndVersionId = apiReferenceByApiAndVersionId
   apiReferences = apiReferences
   apiSearch = apiSearch
   apiSearchV3 = apiSearchV3
   apiSpecImportProgresses = apiSpecImportProgresses
   bulkApisSummaryByTrackingIds = bulkApisSummaryByTrackingIds
   calculatedStatistics = calculatedStatistics
   getApiVersion = getApiVersion
   apiVersion = apiVersion
   apiVersions = apiVersions
   api = api
   apis = apis
   exportOpenApi = exportOpenApi
   validateSwagger = validateSwagger
   applicationAuthorization = applicationAuthorization
   applicationAuthorizations = applicationAuthorizations
   applicationEnvironmentsKeysByApplicationIdAndEnvironment = applicationEnvironmentsKeysByApplicationIdAndEnvironment
   applicationEnvironmentsByApplicationIdAndEnvironment = applicationEnvironmentsByApplicationIdAndEnvironment
   applicationById = applicationById
   asset = asset
   assets = assets
   assetsDownloadUrls = assetsDownloadUrls
   asyncApiConfigurations = asyncApiConfigurations
   userAttributesByUserId = userAttributesByUserId
   auditByOrganizationId = auditByOrganizationId
   audit = audit
   auditLogin = auditLogin
   userByEmail = userByEmail
   activeUser = activeUser
   getAuthStrategies = getAuthStrategies
   getBillingFeaturesByApiVersionId = getBillingFeaturesByApiVersionId
   getBillingFeaturesByApiId = getBillingFeaturesByApiId
   isMonetizationEnabled = isMonetizationEnabled
   billingItems = billingItems
   getFreeSeatsObj = getFreeSeatsObj
   getBillingPlanVersionsByApiId = getBillingPlanVersionsByApiId
   getBillingPlanVersionById = getBillingPlanVersionById
   billingPlanVersion = billingPlanVersion
   billingPlanVersions = billingPlanVersions
   calculatedStatisticsByEndpointAndApiversion = calculatedStatisticsByEndpointAndApiversion
   categoriesV2 = categoriesV2
   categoryEntities = categoryEntities
   categories = categories
   collectionsItemsByIds = collectionsItemsByIds
   collections = collections
   collectionsByOwnerId = collectionsByOwnerId
   getOrgHomepageCollections = getOrgHomepageCollections
   collectionById = collectionById
   collection = collection
   collapsedCollections = collapsedCollections
   collectionBySlugifiedKey = collectionBySlugifiedKey
   getPrivateCollections = getPrivateCollections
   getPrivateCollectionsV2 = getPrivateCollectionsV2
   collectionBySlugifiedKeyV2 = collectionBySlugifiedKeyV2
   collectionBySlugifiedKeyV3 = collectionBySlugifiedKeyV3
   getCommentsByIssueIdV2 = getCommentsByIssueIdV2
   getCommentByIdV2 = getCommentByIdV2
   search = search
   searchEntityByApiId = searchEntityByApiId
   getOpenApiSpecByApiId = getOpenApiSpecByApiId
   entityById = entityById
   activeEntity = activeEntity
   apiByNameAndOwnerName = apiByNameAndOwnerName
   apiBySlugifiedNameAndOwnerName = apiBySlugifiedNameAndOwnerName
   apiByNameAndOwnerId = apiByNameAndOwnerId
   userFollows = userFollows
   apiById = apiById
   apisById = apisById
   followUserAction = followUserAction
   userFollowers = userFollowers
   calculateSeatsPrice = calculateSeatsPrice
   getSeatsTransactionsByOrgId = getSeatsTransactionsByOrgId
   organizationsTreeToken = organizationsTreeToken
   getMinimumSeats = getMinimumSeats
   transactionsById = transactionsById
   unionDiscussionsByAuthor = unionDiscussionsByAuthor
   getActiveUserContext = getActiveUserContext
   getActiveTeamContext = getActiveTeamContext
   transactionsAnalyticsByApiId = transactionsAnalyticsByApiId
   getConsumers = getConsumers
   getFreeConsumers = getFreeConsumers
   consumers = consumers
   requestAdminToSubscribeToAnAPI = requestAdminToSubscribeToAnAPI
   getCountryMetadata = getCountryMetadata
   unionIssuesByAuthorV2 = unionIssuesByAuthorV2
   getIssuesByApiIdV2 = getIssuesByApiIdV2
   getIssuesByApiIdsV2 = getIssuesByApiIdsV2
   endpointStats = endpointStats
   endpointStatsByEntity = endpointStatsByEntity
   endpointStatsByEntityV2 = endpointStatsByEntityV2
   getEndpointsWithinDateByParameters = getEndpointsWithinDateByParameters
   endpoint = endpoint
   endpoints = endpoints
   searchEntities = searchEntities
   entitiesMetadata = entitiesMetadata
   getEntitiesRoles = getEntitiesRoles
   entitiesRoles = entitiesRoles
   getLogsCSV = getLogsCSV
   exportLogsCSVProvider = exportLogsCSVProvider
   exportLogsCSVDeveloper = exportLogsCSVDeveloper
   gateways = gateways
   getGateways = getGateways
   getGatewayConfiguration = getGatewayConfiguration
   graphQlIntrospectionSchema = graphQlIntrospectionSchema
   headlinesByApiNameAndOwnerId = headlinesByApiNameAndOwnerId
   getIssuesByOrganizatonId = getIssuesByOrganizatonId
   getResponseTimeByProviderId = getResponseTimeByProviderId
   getAverageResponseTime = getAverageResponseTime
   unionIssuesByAuthor = unionIssuesByAuthor
   getIssueByIdV2 = getIssueByIdV2
   getIssuesByOrganizationId = getIssuesByOrganizationId
   getIssuesByTeamIdV2 = getIssuesByTeamIdV2
   getIssuesFollowsByUserIdV2 = getIssuesFollowsByUserIdV2
   kafkaConfiguration = kafkaConfiguration
   kafkaTopics = kafkaTopics
   kafkaSchemas = kafkaSchemas
   kafkaTopicMetadata = kafkaTopicMetadata
   getTemplate = getTemplate
   getLegalAgreementInfo = getLegalAgreementInfo
   updateLegalAgreementInfo = updateLegalAgreementInfo
   createLegalAgreementInfo = createLegalAgreementInfo
   deleteLegalAgreementInfo = deleteLegalAgreementInfo
   getLegalAgreementSigningURL = getLegalAgreementSigningURL
   logPayloadByRequestId = logPayloadByRequestId
   logPayloadByRequestIdWithLoggingRestrictions = logPayloadByRequestIdWithLoggingRestrictions
   developerLogPayloadByRequestIdWithLoggingRestrictions = developerLogPayloadByRequestIdWithLoggingRestrictions
   messageThreads = messageThreads
   messages = messages
   getApiAverageResponseTime = getApiAverageResponseTime
   getProviderAverageResponseTime = getProviderAverageResponseTime
   getRelativeAverageResponseTime = getRelativeAverageResponseTime
   getMessageThread = getMessageThread
   newNotificationsByUserId = newNotificationsByUserId
   notificationsByUserId = notificationsByUserId
   organization = organization
   organizations = organizations
   getOrganizations = getOrganizations
   getOrganizationBySlugifiedName = getOrganizationBySlugifiedName
   getOrganizationById = getOrganizationById
   getEmailDomainAndCheckIfIgnored = getEmailDomainAndCheckIfIgnored
   getOrganizationsWithTheSameEmail = getOrganizationsWithTheSameEmail
   searchOrganizations = searchOrganizations
   validateResetPasswordToken = validateResetPasswordToken
   getProjectAllowedAPIs = getProjectAllowedAPIs
   requestLogsByEntity = requestLogsByEntity
   getAccessControlRoles = getAccessControlRoles
   getRoles = getRoles
   roles = roles
   searchApis = searchApis
   searchBlogPosts = searchBlogPosts
   searchCollections = searchCollections
   spotlights = spotlights
   searchSubscribedEntityByApiIdAndAppName = searchSubscribedEntityByApiIdAndAppName
   activeSubscriptionsCount = activeSubscriptionsCount
   getInternalSubscriptions = getInternalSubscriptions
   searchSubscribedEntityByApiId = searchSubscribedEntityByApiId
   getSubscriptions = getSubscriptions
   getOrganizationSubscriptions = getOrganizationSubscriptions
   subscriptions = subscriptions
   subscription = subscription
   subscriptionsCount = subscriptionsCount
   getTagsList = getTagsList
   tagDefinitions = tagDefinitions
   paginatedTeamUsersByOrganizationId = paginatedTeamUsersByOrganizationId
   paginatedTeamUsersByOrganizationIdV2 = paginatedTeamUsersByOrganizationIdV2
   teamUserByEmailAndOrgId = teamUserByEmailAndOrgId
   teamUser = teamUser
   findUsersInOrganization = findUsersInOrganization
   teamByTeamId = teamByTeamId
   teamsByOrganizationId = teamsByOrganizationId
   getTeamBySlugifiedName = getTeamBySlugifiedName
   searchTeams = searchTeams
   team = team
   teams = teams
   tenant = tenant
   transactions = transactions
   transactionsSummary = transactionsSummary
   transformations = transformations
   tutorials = tutorials
   getPhoneNumbers = getPhoneNumbers
   getRecoveryCodes = getRecoveryCodes
   isTwoFactorEnabledByType = isTwoFactorEnabledByType
   getUsagesAndParentUsageForSubscription = getUsagesAndParentUsageForSubscription
   getUsagesAgrregatedByTeamsForSubscription = getUsagesAgrregatedByTeamsForSubscription
   getUsagesAndParentUsageForSubscriptionByBuckets = getUsagesAndParentUsageForSubscriptionByBuckets
   getUsagesAgrregatedByTeamsForSubscriptionByBuckets = getUsagesAgrregatedByTeamsForSubscriptionByBuckets
   organizationQuotaUsageByApiIdV2 = organizationQuotaUsageByApiIdV2
   getUserInviteByToken = getUserInviteByToken
   checkUserInvitesBranding = checkUserInvitesBranding
   checkIfEmailsAlreadyInvited = checkIfEmailsAlreadyInvited
   searchUsersToInvite = searchUsersToInvite
   getUserSavedApis = getUserSavedApis
   userById = userById
   userByUsername = userByUsername
   getPrivateApisJwt = getPrivateApisJwt
   searchUsers = searchUsers
   searchUsersV2 = searchUsersV2
   user = user
   users = users
   getVirtualPermissions = getVirtualPermissions
   virtualPermissions = virtualPermissions
   getWorkflowsForProvider = getWorkflowsForProvider
   getWorkflowsForDeveloper = getWorkflowsForDeveloper
   getWorkflowsByRequestor = getWorkflowsByRequestor
   getWorkflowsByRequestee = getWorkflowsByRequestee
   canWorkflowBeSubmitted = canWorkflowBeSubmitted
   getWorkflowAudits = getWorkflowAudits
   getWorkflowsCount = getWorkflowsCount
   exclusions = exclusions
