from pygqlmap import GQLQuery
from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class ping(GQLQuery):
   """
   ping - Used to determine whether or not RapidAPI is responding to API calls

   """
   type: str ##NON NULL

class eventUrls(GQLQuery):
   """
   eventUrls - Get all URLs for an Event

   """
   class Args(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: EventUrlWhereInput
      order: EventUrlSortablesInput

   _args: Args


   type: EventUrlConnection ##NON NULL

class eventUrl(GQLQuery):
   """
   eventUrl - Get details of the specific URL for the Event

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: EventUrl

class eventTypes(GQLQuery):
   """
   eventTypes - Get types of Events

   """
   type: EventType ##NON NULL

class eventConfig(GQLQuery):
   """
   eventConfig - Get event configuration information

   """
   type: EventConfig

class gatewayInstances(GQLQuery):
   """
   gatewayInstances - Get all gateway instances

   """
   class Args(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: GatewayInstanceWhereInput
      order: GatewayInstanceSortingInput

   _args: Args


   type: GatewayInstanceConnection ##NON NULL

class gatewayInstance(GQLQuery):
   """
   gatewayInstance - Get the gateway instance information

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class gatewayTemplates(GQLQuery):
   """
   gatewayTemplates - Get all templates

   """
   class Args(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: GatewayTemplateWhereInput
      order: GatewayTemplateSortingInput

   _args: Args


   type: GatewayTemplateConnection ##NON NULL

class gatewayTemplate(GQLQuery):
   """
   gatewayTemplate - Get details of a specific tempalte 

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class gatewayTemplatesParams(GQLQuery):
   """
   gatewayTemplatesParams - Get all parameters across a tempalte

   """
   class Args(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: GatewayTemplateParamsWhereInput
      order: GatewayTemplateParamSortingInput

   _args: Args


   type: GatewayTemplateParamConnection ##NON NULL

class gatewayTemplateParam(GQLQuery):
   """
   gatewayTemplateParam - Get details of a specific template prameter

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: GatewayTemplateParam ##NON NULL

class envConfigCategories(GQLQuery):
   """
   envConfigCategories - A category of enterprise congfiguration

   """
   type: EnvConfigCategory ##NON NULL

class envConfig(GQLQuery):
   """
   envConfig - An individaul enterprise configruation

   """
   class Args(GQLArgsSet, GQLObject): 
      id: int ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class envConfigs(GQLQuery):
   """
   envConfigs - All configurations for an Enterprise

   """
   class Args(GQLArgsSet, GQLObject): 
      envConfigTerm: EnvConfigTerm ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class adminAuditLogs(GQLQuery):
   """
   adminAuditLogs - Enterprise admin audit logs 

   """
   class Args(GQLArgsSet, GQLObject): 
      where: AdminAuditLogInput
      pagination: PaginationArgs
      orderBy: AdminAuditLogSortablesInput

   _args: Args


   type: AdminAuditLogConnection

class eventLogs(GQLQuery):
   """
   eventLogs - Get audit trail(s) for Events

   """
   class Args(GQLArgsSet, GQLObject): 
      where: EventLogInput
      pagination: PaginationArgs
      orderBy: EventLogSortablesInput

   _args: Args


   type: EventLogConnection

class extensions(GQLQuery):
   """
   extensions - Get extensions for an API

   """
   class Args(GQLArgsSet, GQLObject): 
      client: str
      page: str
      path: str

   _args: Args


   type: list[Extension]

class getSEOTagsByURL(GQLQuery):
   """
   getSEOTagsByURL - returns the CEO tags defined for an API

   """
   class Args(GQLArgsSet, GQLObject): 
      url: str

   _args: Args


   type: SEO

class getUserAlertById(GQLQuery):
   """
   getUserAlertById - Get alert created by an API Provider by Id

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: UserAlert

class getUserAlertsByScope(GQLQuery):
   """
   getUserAlertsByScope - Get alerts created by an API provider for an API by scope

   """
   class Args(GQLArgsSet, GQLObject): 
      scope: ID ##NON NULL

   _args: Args


   type: list[UserAlert]

class getAlertsDefinitions(GQLQuery):
   """
   getAlertsDefinitions - Get definitions of alerts across RapidAPI

   """
   type: AlertDefinition ##NON NULL

class userAlerts(GQLQuery):
   """
   userAlerts - Get alerts created by an API provider for an API

   """
   class Args(GQLArgsSet, GQLObject): 
      where: UserAlertsWhereInput ##NON NULL

   _args: Args


   type: UserAlertsConnection ##NON NULL

class userAlert(GQLQuery):
   """
   userAlert - Get alert created by an API provider for an API

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: UserAlert

class allowedPlanDeveloperByPlanId(GQLQuery):
   """
   allowedPlanDeveloperByPlanId - Get invited developers for a private plan of an API

   """
   class Args(GQLArgsSet, GQLObject): 
      planId: str

   _args: Args


   type: list[AllowedPlanDeveloper]

class apiCertificate(GQLQuery):
   """
   apiCertificate - returns the API Certificate details based on the certificate Id

   """
   class Args(GQLArgsSet, GQLObject): 
      apiCertificateId: ID ##NON NULL

   _args: Args


   type: ApiCertificate

class apiCertificates(GQLQuery):
   """
   apiCertificates - returns the API Certificates details based on the API Id and User Id

   """
   class Args(GQLArgsSet, GQLObject): 
      where: ApiCertificateWhereInput
      orderBy: ApiCertificateOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiCertificateConnection ##NON NULL

class apiDevelopersByApiId(GQLQuery):
   """
   apiDevelopersByApiId - returns API developer details based on the API Id parameter

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str
      pagingArgs: PagingArgs

   _args: Args


   type: ApiDeveloper ##NON NULL

class apiFollowers(GQLQuery):
   """
   apiFollowers - Returns a list of users who follow a specific API(s)

   """
   class Args(GQLArgsSet, GQLObject): 
      where: ApiFollowerWhereInput ##NON NULL
      orderBy: ApiFollowerOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiFollowerConnection ##NON NULL

class apiReferenceByApiAndVersionId(GQLQuery):
   """
   apiReferenceByApiAndVersionId - [will be deprecated; do not use] Use apiReferences

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str ##NON NULL
      versionId: str ##NON NULL

   _args: Args


   type: ApiReference

class apiReferences(GQLQuery):
   """
   apiReferences - Something with API Spotlights...

   """
   class Args(GQLArgsSet, GQLObject): 
      where: ApiReferenceWhereInput

   _args: Args


   type: ApiReferenceConnection ##NON NULL

class apiSearch(GQLQuery):
   """
   apiSearch - [will be deprecated; do not use] Search for API

   """
   class Args(GQLArgsSet, GQLObject): 
      searchArguments: SearchArguments

   _args: Args


   type: ApiSearchPaged

class apiSearchV3(GQLQuery):
   """
   apiSearchV3 - [will be deprecated; do not use] Search for API

   """
   class Args(GQLArgsSet, GQLObject): 
      searchArguments: SearchArguments

   _args: Args


   type: ApiSearchPaged

class apiSpecImportProgresses(GQLQuery):
   """
   apiSpecImportProgresses - Supports the async process for the API import (especially for long time upload might be a result of a big file import. Polling request from the client to the backend - returns success result only when the API was completely imported. 

   """
   class Args(GQLArgsSet, GQLObject): 
      trackingIds: list[ID] ##NON NULL

   _args: Args


   type: ApiSpecImportProcess ##NON NULL

class bulkApisSummaryByTrackingIds(GQLQuery):
   """
   bulkApisSummaryByTrackingIds - Check to see if the API import operation has completed across multiple APIs

   """
   class Args(GQLArgsSet, GQLObject): 
      trackingIds: list[ID] ##NON NULL

   _args: Args


   type: BatchTrackingIdsSummary

class calculatedStatistics(GQLQuery):
   """
   calculatedStatistics - Get API usage analytics

   """
   class Args(GQLArgsSet, GQLObject): 
      fromDate: str ##NON NULL
      toDate: str ##NON NULL
      resolution: str
      projectIds: list[str]
      apiIds: list[str]
      endpoints: list[str]
      groupBy: StatsGroupBy
      apiVersionIds: list[ID]
      entityId: ID
      timeOffset: int
      filters: list[StatsFilterBy]

   _args: Args


   type: CalculatedStatistics

class getApiVersion(GQLQuery):
   """
   getApiVersion - [will be deprecated; do not use] return the apiVersion information based on the apiVersion's Id input

   """
   class Args(GQLArgsSet, GQLObject): 
      versionId: ID ##NON NULL

   _args: Args


   type: ApiVersion

class apiVersion(GQLQuery):
   """
   apiVersion - [will be deprecated; do not use] return the apiVersion information based on the apiVersion's Id input

   """
   class Args(GQLArgsSet, GQLObject): 
      apiVersionId: ID ##NON NULL

   _args: Args


   type: ApiVersion

class apiVersions(GQLQuery):
   """
   apiVersions - returns a list of apiVersions based on the ApiVersionWhereInput

   """
   class Args(GQLArgsSet, GQLObject): 
      where: ApiVersionWhereInput
      orderBy: ApiVersionOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiVersionConnection ##NON NULL

class api(GQLQuery):
   """
   api - Obtain an API's details, such as its name and current version.

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#obtain-an-apis-details

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Api

class apis(GQLQuery):
   """
   apis - Returns the APIs based on the APIWhereInput

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#query-apis



   """
   class Args(GQLArgsSet, GQLObject): 
      where: ApiWhereInput
      orderBy: ApiOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiConnection ##NON NULL

class exportOpenApi(GQLQuery):
   """
   exportOpenApi - Returns a generated OAS 3 representation of a certain API version in the platform, including the RapidAPI metadata extension properties.\n\n`apiId` and the optional `apiVersionId` args specify which API and version to target for export.\nOmitting the `apiVersionId` arg will target the *current* version of the API specified by `apiId`.\n\nA non-null result would be returned only in accordance with the following rules:\n- the target `apiId` or `apiVersionId` (if specifically provided) have some match in the platform, and either:\n  - the target API is defined with `PUBLIC` visibility, or\n  - the target API is defined with `PRIVATE` visibility and either:\n    - the requestor or any team they are a member of is owning the target API or\n    - the requestor or any team they are a member of is **invited** to the target API\n\nIf the API is visible to the requestor for export but not owned by it, certain sensitive fields (e.g `servers` array) in the exported document may be returned blank.

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#export-an-oas-document-for-an-api

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: ID ##NON NULL
      apiVersionId: ID

   _args: Args


   type: Any

class validateSwagger(GQLQuery):
   """
   validateSwagger - [marked for deprecation; do not use] Validates a swagger input

   """
   class Args(GQLArgsSet, GQLObject): 
      input: validateSwaggerInput

   _args: Args


   type: Any

class applicationAuthorization(GQLQuery):
   """
   applicationAuthorization - get application authorization (x-rapid-key/oauth)

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class applicationAuthorizations(GQLQuery):
   """
   applicationAuthorizations - get application authorization (x-rapid-key/oauth)

   """
   class Args(GQLArgsSet, GQLObject): 
      where: AppAuthorizationsWhereInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class applicationEnvironmentsKeysByApplicationIdAndEnvironment(GQLQuery):
   """
   applicationEnvironmentsKeysByApplicationIdAndEnvironment - applicationEnvironments (applicationAuthorization) by application Id. going to be deprecated, please don't know

   """
   class Args(GQLArgsSet, GQLObject): 
      applicationId: str
      environment: str

   _args: Args


   type: ApplicationEnvironmentPaging

class applicationEnvironmentsByApplicationIdAndEnvironment(GQLQuery):
   """
   applicationEnvironmentsByApplicationIdAndEnvironment - applicationEnvironments (applicationAuthorization) by application Id.  going to be deprecated, please don't know 

   """
   class Args(GQLArgsSet, GQLObject): 
      applicationId: str
      environment: str

   _args: Args


   type: ApplicationEnvironment

class applicationById(GQLQuery):
   """
   applicationById - application by Id 

   """
   class Args(GQLArgsSet, GQLObject): 
      id: int

   _args: Args


   type: Application

class asset(GQLQuery):
   """
   asset - Fetch an asset by ID

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Asset

class assets(GQLQuery):
   """
   assets - Query assets by IDs or external IDs, optional filter on visibility

   """
   class Args(GQLArgsSet, GQLObject): 
      where: AssetWhereInput ##NON NULL

   _args: Args


   type: Asset ##NON NULL

class assetsDownloadUrls(GQLQuery):
   """
   assetsDownloadUrls - Query assets by IDs or external IDs, optional filter on visibility; Includes download URL in response

   """
   class Args(GQLArgsSet, GQLObject): 
      where: AssetWhereInput ##NON NULL

   _args: Args


   type: AssetForDownload ##NON NULL

class asyncApiConfigurations(GQLQuery):
   """
   asyncApiConfigurations - [experimental] Get async API configuration

   """
   class Args(GQLArgsSet, GQLObject): 
      where: AsyncApiConfigurationWhereInput ##NON NULL

   _args: Args


   type: AsyncApiConfigurationConnection ##NON NULL

class userAttributesByUserId(GQLQuery):
   """
   userAttributesByUserId - Get all user attributes by user ID

   """
   class Args(GQLArgsSet, GQLObject): 
      userId: int

   _args: Args


   type: UserAttributes

class auditByOrganizationId(GQLQuery):
   """
   auditByOrganizationId - Organization level Audits (e.g. creation, user invited, etc...)

   """
   class Args(GQLArgsSet, GQLObject): 
      searchTerm: str
      from_: int
      orgId: int

   _args: Args


   type: auditTrails

class audit(GQLQuery):
   """
   audit - Enterprise Admin Audit (e.g. config CRUD events)

   """
   class Args(GQLArgsSet, GQLObject): 
      where: AuditWhereInput ##NON NULL

   _args: Args


   type: auditTrails

class auditLogin(GQLQuery):
   """
   auditLogin - Audit for user logins

   """
   class Args(GQLArgsSet, GQLObject): 
      from_: int
      userId: str

   _args: Args


   type: auditTrails

class userByEmail(GQLQuery):
   """
   userByEmail - Get user ID by user email address

   """
   class Args(GQLArgsSet, GQLObject): 
      email: str

   _args: Args


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
   type: list[authStrategy]

class getBillingFeaturesByApiVersionId(GQLQuery):
   """
   getBillingFeaturesByApiVersionId - [will be deprecated; do not use] Get billing feature by API versionId (will have same results as getBillingFeaturesByApiId)

   """
   class Args(GQLArgsSet, GQLObject): 
      versionId: str

   _args: Args


   type: list[BillingFeature]

class getBillingFeaturesByApiId(GQLQuery):
   """
   getBillingFeaturesByApiId - Get billing feature by API id

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str ##NON NULL

   _args: Args


   type: list[BillingFeature]

class isMonetizationEnabled(GQLQuery):
   """
   isMonetizationEnabled - check if the monetization is enabled in the environment 

   """
   type: bool

class billingItems(GQLQuery):
   """
   billingItems - Get Billing items where input must include apiId or apiVersionId,\nPagination not supported

   """
   class Args(GQLArgsSet, GQLObject): 
      where: BillingItemsWhereInput ##NON NULL

   _args: Args


   type: BillingItemConnection

class getFreeSeatsObj(GQLQuery):
   """
   getFreeSeatsObj - Get billing information attached to an org

   """
   class Args(GQLArgsSet, GQLObject): 
      orgId: ID ##NON NULL

   _args: Args


   type: SeatsBillingInformation

class getBillingPlanVersionsByApiId(GQLQuery):
   """
   getBillingPlanVersionsByApiId - [will be deprecated; do not use] use billingPlanVersions query

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str ##NON NULL
      apiVersionId: str
      pagingArgs: PagingArgsBilling
      filters: BillingPlanVersionFilters

   _args: Args


   type: BillingPlanVersionsResponse

class getBillingPlanVersionById(GQLQuery):
   """
   getBillingPlanVersionById - [will be deprecated; do not use] use billingPlanVersion query

   """
   class Args(GQLArgsSet, GQLObject): 
      billingPlanVersionId: str ##NON NULL

   _args: Args


   type: BillingPlanVersion

class billingPlanVersion(GQLQuery):
   """
   billingPlanVersion - Get Billing Plan Version details

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: BillingPlanVersion

class billingPlanVersions(GQLQuery):
   """
   billingPlanVersions -  Get Billing Plan versions\nPagination is not fully supported yet. 

   """
   class Args(GQLArgsSet, GQLObject): 
      where: BillingPlanVersionWhereInput
      pagination: PaginationInput

   _args: Args


   type: BillingPlanVersionConnection

class calculatedStatisticsByEndpointAndApiversion(GQLQuery):
   """
   calculatedStatisticsByEndpointAndApiversion - Get API usage analytics by endpoint and API Version

   """
   class Args(GQLArgsSet, GQLObject): 
      fromDate: str ##NON NULL
      toDate: str ##NON NULL
      resolution: str
      endpointsAndApiVersions: list[endpointsAndApiVersionCouples] ##NON NULL
      groupBy: StatsGroupBy
      apiId: str ##NON NULL
      entityId: ID
      timeOffset: int
      filters: list[StatsFilterBy]

   _args: Args


   type: CalculatedStatistics

class categoriesV2(GQLQuery):
   """
   categoriesV2 - [will be deprecated; do not use] Returns a list categories

   """
   class Args(GQLArgsSet, GQLObject): 
      where: CategoryWhereInput
      orderBy: CategoryOrderByInput
      pagination: PaginationInput

   _args: Args


   type: CategoryConnection ##NON NULL

class categoryEntities(GQLQuery):
   """
   categoryEntities - [will be deprecated; do not use] Return the category entity information

   """
   class Args(GQLArgsSet, GQLObject): 
      lang: str
      pagingArgs: PagingArgs

   _args: Args


   type: list[CategoryEntity]

class categories(GQLQuery):
   """
   categories - [will be deprecated; do not use] Returns a list of categories based on search inputs

   """
   class Args(GQLArgsSet, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection

   _args: Args


   type: list[Category]

class collectionsItemsByIds(GQLQuery):
   """
   collectionsItemsByIds - Returns the collections of items by IDs

   """
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: list[CollectionItem]

class collections(GQLQuery):
   """
   collections - Get API collection list

   """
   class Args(GQLArgsSet, GQLObject): 
      where: CollectionsWhereInput
      orderBy: CollectionsOrderByInput
      minWeightToFetchApis: int

   _args: Args


   type: CollectionsResponse

class collectionsByOwnerId(GQLQuery):
   """
   collectionsByOwnerId - Returns the collections for a specific tenant id (Assumption Owner = tenant in this context)

   """
   class Args(GQLArgsSet, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection
      minWeightToFetchApis: int
      collection_type: str

   _args: Args


   type: CollectionsResponse

class getOrgHomepageCollections(GQLQuery):
   """
   getOrgHomepageCollections - Returns a list of collections for a specific organization

   """
   class Args(GQLArgsSet, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection
      minWeightToFetchApis: int

   _args: Args


   type: CollectionsResponse

class collectionById(GQLQuery):
   """
   collectionById - Returns a collection based on Collection ID

   """
   class Args(GQLArgsSet, GQLObject): 
      collectionId: ID ##NON NULL

   _args: Args


   type: Collection

class collection(GQLQuery):
   """
   collection - Returns a collection based on Collection ID

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Collection

class collapsedCollections(GQLQuery):
   """
   collapsedCollections - Get the list of collapsed Collections

   """
   class Args(GQLArgsSet, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection
      limit: int
      page: int

   _args: Args


   type: list[CollapsedCollection]

class collectionBySlugifiedKey(GQLQuery):
   """
   collectionBySlugifiedKey - Returns a collection based on name

   """
   class Args(GQLArgsSet, GQLObject): 
      slugifiedKey: str

   _args: Args


   type: Collection

class getPrivateCollections(GQLQuery):
   """
   getPrivateCollections - [Marked for deprecation; do not use ]Returns private collection

   """
   type: list[Collection]

class getPrivateCollectionsV2(GQLQuery):
   """
   getPrivateCollectionsV2 - Returns private collection

   """
   type: list[Collection]

class collectionBySlugifiedKeyV2(GQLQuery):
   """
   collectionBySlugifiedKeyV2 - Returns a collection based on name V2

   """
   class Args(GQLArgsSet, GQLObject): 
      slugifiedKey: str

   _args: Args


   type: CollectionV2

class collectionBySlugifiedKeyV3(GQLQuery):
   """
   collectionBySlugifiedKeyV3 - Returns a collection based on name V3

   """
   class Args(GQLArgsSet, GQLObject): 
      slugifiedKey: str

   _args: Args


   type: CollectionV3

class getCommentsByIssueIdV2(GQLQuery):
   """
   getCommentsByIssueIdV2 - Returns the comments by an issue ID

   """
   class Args(GQLArgsSet, GQLObject): 
      issueId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: PaginatedComments

class getCommentByIdV2(GQLQuery):
   """
   getCommentByIdV2 - Returns the comment by an issue and comment ID

   """
   class Args(GQLArgsSet, GQLObject): 
      issueId: int ##NON NULL
      commentId: int ##NON NULL

   _args: Args


   type: Comment

class search(GQLQuery):
   """
   search - Returns a list of APIs based on search parameters

   """
   class Args(GQLArgsSet, GQLObject): 
      term: str ##NON NULL

   _args: Args


   type: ApiSearch ##NON NULL

class searchEntityByApiId(GQLQuery):
   """
   searchEntityByApiId - Search for a specific entity within a specific API

   """
   class Args(GQLArgsSet, GQLObject): 
      userName: str ##NON NULL
      apiId: str ##NON NULL
      distinct: str

   _args: Args


   type: list[Any]

class getOpenApiSpecByApiId(GQLQuery):
   """
   getOpenApiSpecByApiId - [will be deprecated; do not use] returns the OAS for the API ID parameter provided

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: ID

   _args: Args


   type: Any

class entityById(GQLQuery):
   """
   entityById - returns (User/Team/organization) by entityId

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID

   _args: Args


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
   class Args(GQLArgsSet, GQLObject): 
      apiName: str
      ownerName: str

   _args: Args


   type: Api

class apiBySlugifiedNameAndOwnerName(GQLQuery):
   """
   apiBySlugifiedNameAndOwnerName - [will be deprecated; do not use] Query and API by Slugified Name and Owner Name

   """
   class Args(GQLArgsSet, GQLObject): 
      slugifiedName: str
      ownerName: str

   _args: Args


   type: Api

class apiByNameAndOwnerId(GQLQuery):
   """
   apiByNameAndOwnerId - [will be deprecated; do not use] Query an API by Name and Owner Id

   """
   class Args(GQLArgsSet, GQLObject): 
      apiName: str
      ownerId: str

   _args: Args


   type: Api

class userFollows(GQLQuery):
   """
   userFollows - Query the ID of a user and get back the users they follow.

   """
   class Args(GQLArgsSet, GQLObject): 
      userId: int

   _args: Args


   type: list[FollowUser]

class apiById(GQLQuery):
   """
   apiById - [will be deprecated; do not use] Query an API by id

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str

   _args: Args


   type: Api

class apisById(GQLQuery):
   """
   apisById - [will be deprecated; do not use] Get APIs by Id

   """
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: list[Api]

class followUserAction(GQLQuery):
   """
   followUserAction - **This needs to be updated to a mutation** Follow a provider

   """
   class Args(GQLArgsSet, GQLObject): 
      followerId: int
      followeeId: int

   _args: Args


   type: FollowPair

class userFollowers(GQLQuery):
   """
   userFollowers - Get follows by user ID

   """
   class Args(GQLArgsSet, GQLObject): 
      userId: int

   _args: Args


   type: list[Follower]

class calculateSeatsPrice(GQLQuery):
   """
   calculateSeatsPrice - Calculate the seat price

   """
   class Args(GQLArgsSet, GQLObject): 
      seats: int ##NON NULL

   _args: Args


   type: float ##NON NULL

class getSeatsTransactionsByOrgId(GQLQuery):
   """
   getSeatsTransactionsByOrgId -   Return a list of transactions for seats by organization Id

   """
   class Args(GQLArgsSet, GQLObject): 
      orgId: int ##NON NULL

   _args: Args


   type: list[OrgTransaction]

class organizationsTreeToken(GQLQuery):
   """
   organizationsTreeToken - Getting organization hierarchy of API requestor encode by JWT 

   """
   type: str

class getMinimumSeats(GQLQuery):
   """
   getMinimumSeats - Get the default seats configuration 

   """
   type: int ##NON NULL

class transactionsById(GQLQuery):
   """
   transactionsById - Get a transaction based on an API Id or a User Id

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str
      userId: int
      type: str
      pagingArgs: PagingArgs
      queryFilters: QueryFilters
      paymentStatusFilters: list[TransactionPaymentStatus]

   _args: Args


   type: TransactionsPaging

class unionDiscussionsByAuthor(GQLQuery):
   """
   unionDiscussionsByAuthor - [marked for deprecation; do not use] Returns discussions by author

   """
   class Args(GQLArgsSet, GQLObject): 
      authorId: int
      limit: int
      offset: int
      orderField: str
      orderType: str
      type: str

   _args: Args


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
   class Args(GQLArgsSet, GQLObject): 
      apiId: str
      fromDate: str
      toDate: str
      attributes: str

   _args: Args


   type: TransactionsAnalytics

class getConsumers(GQLQuery):
   """
   getConsumers - Gets a list of consumers for an API by type (Free, Paid, All)

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str
      userId: list[int]
      offset: int
      limit: int
      sort: str
      usernames: str
      plansFilter: list[str]
      lastActive: list[str]

   _args: Args


   type: Consumers

class getFreeConsumers(GQLQuery):
   """
   getFreeConsumers - Return free users by Api Id

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: list[ID] ##NON NULL
      offset: int
      limit: int
      order: str
      lastActive: list[str]
      username: list[str]
      userId: list[int]

   _args: Args


   type: Consumers

class consumers(GQLQuery):
   """
   consumers - return all the consumers based on the API ID

   """
   class Args(GQLArgsSet, GQLObject): 
      where: ConsumersWhereInput ##NON NULL

   _args: Args


   type: ConsumerConnection

class requestAdminToSubscribeToAnAPI(GQLQuery):
   """
   requestAdminToSubscribeToAnAPI - [will be deprecated; do not use] requesting subscribe to an API 

   """
   class Args(GQLArgsSet, GQLObject): 
      eventData: ContactAdminSubscribeToAPIEvent ##NON NULL

   _args: Args


   type: bool

class getCountryMetadata(GQLQuery):
   """
   getCountryMetadata - Get metadata about a Country

   """
   class Args(GQLArgsSet, GQLObject): 
      ip: str

   _args: Args


   type: Country

class unionIssuesByAuthorV2(GQLQuery):
   """
   unionIssuesByAuthorV2 - Returns discussions by author

   """
   class Args(GQLArgsSet, GQLObject): 
      authorId: int
      type: str
      pagingArgs: PagingArgs
      apiIds: list[str]

   _args: Args


   type: DiscussionObject

class getIssuesByApiIdV2(GQLQuery):
   """
   getIssuesByApiIdV2 - Returns the issues associated with an API id

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str ##NON NULL
      pagingArgs: PagingArgs
      providerId: str

   _args: Args


   type: IssueObject

class getIssuesByApiIdsV2(GQLQuery):
   """
   getIssuesByApiIdsV2 - Returns the issues associated with an APIs ids

   """
   class Args(GQLArgsSet, GQLObject): 
      apiIds: list[str] ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

class endpointStats(GQLQuery):
   """
   endpointStats - The analytics for each endpoint

   """
   class Args(GQLArgsSet, GQLObject): 
      apiIds: list[ID] ##NON NULL
      projectIds: list[ID]
      endpointIds: list[ID]
      fromDate: str
      toDate: str
      resolution: str

   _args: Args


   type: list[EndpointStats]

class endpointStatsByEntity(GQLQuery):
   """
   endpointStatsByEntity - The analytics for each endpoint by entity

   """
   class Args(GQLArgsSet, GQLObject): 
      entityId: ID
      apiId: ID ##NON NULL
      endpointIds: list[ID]
      fromDate: DateTime
      toDate: DateTime
      resolution: Resolution
      timeOffset: int
      filters: list[StatsFilterBy]

   _args: Args


   type: list[EndpointStats]

class endpointStatsByEntityV2(GQLQuery):
   """
   endpointStatsByEntityV2 - The analytics for each endpoint by entity v2

   """
   class Args(GQLArgsSet, GQLObject): 
      entityId: ID
      apiId: ID ##NON NULL
      endpointsAndApiVersions: list[EndpointAndVersion]
      fromDate: DateTime
      toDate: DateTime
      resolution: Resolution
      timeOffset: int
      filters: list[StatsFilterBy]

   _args: Args


   type: list[VersionEndpointStats]

class getEndpointsWithinDateByParameters(GQLQuery):
   """
   getEndpointsWithinDateByParameters - Get the endpoints of an API within a date range

   """
   class Args(GQLArgsSet, GQLObject): 
      input: endpointsWithinDateInput ##NON NULL
      showDeleted: bool

   _args: Args


   type: list[EndpointStats]

class endpoint(GQLQuery):
   """
   endpoint - Get an Endpoint

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Endpoint

class endpoints(GQLQuery):
   """
   endpoints - Get a list of endpoints

   """
   class Args(GQLArgsSet, GQLObject): 
      where: EndpointWhereInput ##NON NULL

   _args: Args


   type: EndpointConnection

class searchEntities(GQLQuery):
   """
   searchEntities - Search for API by all associated entities (e.g. users, types, etc...)

   """
   class Args(GQLArgsSet, GQLObject): 
      term: str
      limit: int
      status: str
      type: str

   _args: Args


   type: list[Entity]

class entitiesMetadata(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      where: EntityMetadataWhereInput ##NON NULL
      orderBy: EntityMetadataOrderByInput
      pagination: PaginationInput

   _args: Args


   type: EntityMetadataConnection ##NON NULL

class getEntitiesRoles(GQLQuery):
   """
   getEntitiesRoles - get Entity (User/Team/Organization ) assigned roles 

   """
   class Args(GQLArgsSet, GQLObject): 
      entityIds: list[int]
      orgId: int
      parentIds: list[int]

   _args: Args


   type: list[EntityRole]

class entitiesRoles(GQLQuery):
   """
   entitiesRoles - get roles assigned to Entity

   """
   class Args(GQLArgsSet, GQLObject): 
      where: EntityRoleWhereInput ##NON NULL
      orderBy: EntityRoleOrderByInput
      pagination: PaginationInput

   _args: Args


   type: EntityRoleConnection ##NON NULL

class getLogsCSV(GQLQuery):
   """
   getLogsCSV - Export analytics to a CSV file

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: ID
      projectId: ID

   _args: Args


   type: list[LogsCSV]

class exportLogsCSVProvider(GQLQuery):
   """
   exportLogsCSVProvider - Export CSV of audit trails for Provider related actions

   """
   class Args(GQLArgsSet, GQLObject): 
      contextId: ID ##NON NULL
      fromDate: DateTime ##NON NULL
      toDate: DateTime ##NON NULL
      totalCount: int ##NON NULL
      filters: RequestLogFilters
      timeOffset: int

   _args: Args


   type: LogsCSVExports

class exportLogsCSVDeveloper(GQLQuery):
   """
   exportLogsCSVDeveloper - Export CSV of audit trails for Developer related actions

   """
   class Args(GQLArgsSet, GQLObject): 
      contextId: ID ##NON NULL
      fromDate: DateTime ##NON NULL
      toDate: DateTime ##NON NULL
      totalCount: int ##NON NULL
      filters: RequestLogFilters
      timeOffset: int

   _args: Args


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
   type: list[Gateway]

class getGatewayConfiguration(GQLQuery):
   """
   getGatewayConfiguration - Get the configuration of a Gateway

   """
   class Args(GQLArgsSet, GQLObject): 
      id: int ##NON NULL

   _args: Args


   type: ApiGatewayConfiguration

class graphQlIntrospectionSchema(GQLQuery):
   """
   graphQlIntrospectionSchema - Get the current GraphQL __schema using introspectionCall query

   """
   class Args(GQLArgsSet, GQLObject): 
      introspectionCallUrl: str ##NON NULL

   _args: Args


   type: Any ##NON NULL

class headlinesByApiNameAndOwnerId(GQLQuery):
   """
   headlinesByApiNameAndOwnerId - Get the API readme by ownerId

   """
   class Args(GQLArgsSet, GQLObject): 
      apiName: str
      apiOwnerId: str
      size: int

   _args: Args


   type: list[Headline]

class getIssuesByOrganizatonId(GQLQuery):
   """
   getIssuesByOrganizatonId - Return the issues associated with an organziation Id

   """
   class Args(GQLArgsSet, GQLObject): 
      id: str ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

class getResponseTimeByProviderId(GQLQuery):
   """
   getResponseTimeByProviderId - returns provider response time 

   """
   class Args(GQLArgsSet, GQLObject): 
      providerId: int ##NON NULL

   _args: Args


   type: float ##NON NULL

class getAverageResponseTime(GQLQuery):
   """
   getAverageResponseTime - Returns the average API Response Time

   """
   type: float ##NON NULL

class unionIssuesByAuthor(GQLQuery):
   """
   unionIssuesByAuthor - [marked for deprecation; do not use] Returns discussions by author

   """
   class Args(GQLArgsSet, GQLObject): 
      authorId: int
      type: str
      pagingArgs: PagingArgs

   _args: Args


   type: DiscussionObject

class getIssueByIdV2(GQLQuery):
   """
   getIssueByIdV2 - Returns the issues by Id

   """
   class Args(GQLArgsSet, GQLObject): 
      issueId: int

   _args: Args


   type: Issue

class getIssuesByOrganizationId(GQLQuery):
   """
   getIssuesByOrganizationId - Return the issues associated with an organziation Id

   """
   class Args(GQLArgsSet, GQLObject): 
      id: str
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

class getIssuesByTeamIdV2(GQLQuery):
   """
   getIssuesByTeamIdV2 - Returns the issues associated with a team id

   """
   class Args(GQLArgsSet, GQLObject): 
      id: str
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

class getIssuesFollowsByUserIdV2(GQLQuery):
   """
   getIssuesFollowsByUserIdV2 - Returns issues for APIs followed by a user

   """
   class Args(GQLArgsSet, GQLObject): 
      userId: int

   _args: Args


   type: list[IssueFollow]

class kafkaConfiguration(GQLQuery):
   """
   kafkaConfiguration - returns the kafka configuration for the apiVersion

   """
   class Args(GQLArgsSet, GQLObject): 
      apiVersionId: str ##NON NULL

   _args: Args


   type: KafkaConfiguration

class kafkaTopics(GQLQuery):
   """
   kafkaTopics - returns a list of all the kafka topics related to the apiVersion

   """
   class Args(GQLArgsSet, GQLObject): 
      apiVersionId: str ##NON NULL

   _args: Args


   type: KafkaTopics

class kafkaSchemas(GQLQuery):
   """
   kafkaSchemas - returns a list of all the kafka schemas related to the apiVersion

   """
   class Args(GQLArgsSet, GQLObject): 
      apiVersionId: str ##NON NULL

   _args: Args


   type: KafkaSchemas

class kafkaTopicMetadata(GQLQuery):
   """
   kafkaTopicMetadata - returns the kafka topic metadata

   """
   class Args(GQLArgsSet, GQLObject): 
      apiVersionId: str ##NON NULL
      topicName: str ##NON NULL

   _args: Args


   type: TopicMetadataResponse

class getTemplate(GQLQuery):
   """
   getTemplate - Gets the document for Docusign workflow

   """
   class Args(GQLArgsSet, GQLObject): 
      accountId: str
      templateId: str

   _args: Args


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
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateLegalAgreementInfo

   _args: Args


   type: LegalAgreementInfo

class createLegalAgreementInfo(GQLQuery):
   """
   createLegalAgreementInfo - Create a new legal agreement provider integration for API plans

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CreateLegalAgreementInfo

   _args: Args


   type: LegalAgreementInfo

class deleteLegalAgreementInfo(GQLQuery):
   """
   deleteLegalAgreementInfo - Upadte existing legal agreement provider integration for API plans

   """
   class Args(GQLArgsSet, GQLObject): 
      entityId: str

   _args: Args


   type: Any

class getLegalAgreementSigningURL(GQLQuery):
   """
   getLegalAgreementSigningURL - Build a legal agreement signging url for the UI as an external integration for signing on plans 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: GetLegalAgreementSigningURLInput ##NON NULL

   _args: Args


   type: Any

class logPayloadByRequestId(GQLQuery):
   """
   logPayloadByRequestId - Returns the details of a request by Id

   """
   class Args(GQLArgsSet, GQLObject): 
      requestId: ID
      callTime: str

   _args: Args


   type: LogPayload

class logPayloadByRequestIdWithLoggingRestrictions(GQLQuery):
   """
   logPayloadByRequestIdWithLoggingRestrictions - Returns the details of the request by Id with logging restrictions

   """
   class Args(GQLArgsSet, GQLObject): 
      requestId: ID
      callTime: str
      apiId: str

   _args: Args


   type: RestrictedLogPayload

class developerLogPayloadByRequestIdWithLoggingRestrictions(GQLQuery):
   """
   developerLogPayloadByRequestIdWithLoggingRestrictions - Get request payload for developer

   """
   class Args(GQLArgsSet, GQLObject): 
      requestId: ID
      callTime: str
      apiId: str
      projectId: str

   _args: Args


   type: RestrictedLogPayload

class messageThreads(GQLQuery):
   """
   messageThreads - Search for message threads by specific filters

   """
   class Args(GQLArgsSet, GQLObject): 
      where: MessageThreadsWhereInput

   _args: Args


   type: MessageThreadsObject

class messages(GQLQuery):
   """
   messages - Get messages by filters

   """
   class Args(GQLArgsSet, GQLObject): 
      where: MessagesWhereInput ##NON NULL

   _args: Args


   type: list[Message]

class getApiAverageResponseTime(GQLQuery):
   """
   getApiAverageResponseTime - Returns the average API Response Time

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str ##NON NULL

   _args: Args


   type: float

class getProviderAverageResponseTime(GQLQuery):
   """
   getProviderAverageResponseTime - Get providers average response time for responding to an private message 

   """
   class Args(GQLArgsSet, GQLObject): 
      providerId: int ##NON NULL

   _args: Args


   type: float

class getRelativeAverageResponseTime(GQLQuery):
   """
   getRelativeAverageResponseTime - returns provider response time compared to other providers

   """
   class Args(GQLArgsSet, GQLObject): 
      providerId: int ##NON NULL

   _args: Args


   type: RelativeARTResponse

class getMessageThread(GQLQuery):
   """
   getMessageThread - Get the messages of a thread

   """
   class Args(GQLArgsSet, GQLObject): 
      threadId: int

   _args: Args


   type: MessageThread

class newNotificationsByUserId(GQLQuery):
   """
   newNotificationsByUserId - [will be deprecated; do not use] Get new notifications by User Id

   """
   class Args(GQLArgsSet, GQLObject): 
      userId: int
      limit: int
      offset: int

   _args: Args


   type: list[NewNotification]

class notificationsByUserId(GQLQuery):
   """
   notificationsByUserId - [will be deprecated; do not use] Get notifications by User Id

   """
   class Args(GQLArgsSet, GQLObject): 
      userId: int
      limit: int
      offset: int

   _args: Args


   type: list[Notification]

class organization(GQLQuery):
   """
   organization - Getting an organization list of the API requestor

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Organization

class organizations(GQLQuery):
   """
   organizations - Obtains a list of organizations in which the API requester is an organization administrator. The **teams** field returns an array of teams in each organization. The **users** field returns an array of users in the organization.

   """
   class Args(GQLArgsSet, GQLObject): 
      where: OrganizationWhereInput

   _args: Args


   type: list[Organization]

class getOrganizations(GQLQuery):
   """
   getOrganizations - Get organization of user executing the query

   """
   type: list[Organization]

class getOrganizationBySlugifiedName(GQLQuery):
   """
   getOrganizationBySlugifiedName - [will be deprecated; do not use] returns the organization based on the Sluggified name

   """
   class Args(GQLArgsSet, GQLObject): 
      slugifiedName: str

   _args: Args


   type: Organization

class getOrganizationById(GQLQuery):
   """
   getOrganizationById - [will be deprecated; do not use]  returns the organization based on the orgId

   """
   class Args(GQLArgsSet, GQLObject): 
      orgId: ID ##NON NULL

   _args: Args


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
   type: list[CorporateDomainOrganization]

class searchOrganizations(GQLQuery):
   """
   searchOrganizations - Returns a list of organizations

   """
   class Args(GQLArgsSet, GQLObject): 
      term: str
      limit: int

   _args: Args


   type: list[Entity]

class validateResetPasswordToken(GQLQuery):
   """
   validateResetPasswordToken - Takes a password reset token and returns whether it is valid

   """
   class Args(GQLArgsSet, GQLObject): 
      token: str ##NON NULL

   _args: Args


   type: ValidateTokenResponse

class getProjectAllowedAPIs(GQLQuery):
   """
   getProjectAllowedAPIs - Returns the allowed API IDs by Project/App

   """
   class Args(GQLArgsSet, GQLObject): 
      mashapeId: str ##NON NULL
      projectId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: list[ProjectAllowedAPI]

class requestLogsByEntity(GQLQuery):
   """
   requestLogsByEntity - getting API calls logs associated to an application 

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str
      projectId: str
      fromDate: str ##NON NULL
      toDate: str
      limit: int
      offset: int
      orderBy: RequestLogsOrderBy
      orderDir: OrderDirection
      filters: RequestLogFilters
      timeOffset: int

   _args: Args


   type: RequestLogsResult

class getAccessControlRoles(GQLQuery):
   """
   getAccessControlRoles - Get all roles

   """
   class Args(GQLArgsSet, GQLObject): 
      roleLevels: list[RoleLevel]

   _args: Args


   type: list[Role]

class getRoles(GQLQuery):
   """
   getRoles - Get all defined roles 

   """
   class Args(GQLArgsSet, GQLObject): 
      roleLevels: list[RoleLevel]

   _args: Args


   type: list[Role]

class roles(GQLQuery):
   """
   roles - get roles metada

   """
   class Args(GQLArgsSet, GQLObject): 
      where: RoleWhereInput ##NON NULL
      orderBy: RoleOrderByInput
      pagination: PaginationInput

   _args: Args


   type: RoleConnection ##NON NULL

class searchApis(GQLQuery):
   """
   searchApis - Returns a list of APIs based on search parameters

   """
   class Args(GQLArgsSet, GQLObject): 
      where: SearchApiWhereInput ##NON NULL
      orderBy: SearchApiOrderByInput
      pagination: PaginationInput

   _args: Args


   type: SearchApiConnection ##NON NULL

class searchBlogPosts(GQLQuery):
   """
   searchBlogPosts - Returns a list of blog posts based on search parameters

   """
   class Args(GQLArgsSet, GQLObject): 
      where: SearchBlogPostWhereInput ##NON NULL
      pagination: PaginationInput

   _args: Args


   type: SearchBlogPostConnection

class searchCollections(GQLQuery):
   """
   searchCollections - Returns list of collections 

   """
   class Args(GQLArgsSet, GQLObject): 
      where: SearchCollectionWhereInput
      orderBy: SearchCollectionOrderByInput
      pagination: PaginationInput

   _args: Args


   type: SearchCollectionConnection

class spotlights(GQLQuery):
   """
   spotlights - Returns the spotlights for a specific API

   """
   class Args(GQLArgsSet, GQLObject): 
      where: SpotlightWhereInput ##NON NULL
      orderBy: SpotlightOrderByInput
      pagination: PaginationInput

   _args: Args


   type: SpotlightConnection ##NON NULL

class searchSubscribedEntityByApiIdAndAppName(GQLQuery):
   """
   searchSubscribedEntityByApiIdAndAppName - Returns a list of entities subscribed to an API and App Name

   """
   class Args(GQLArgsSet, GQLObject): 
      appName: str ##NON NULL
      apiId: str ##NON NULL

   _args: Args


   type: list[Project]

class activeSubscriptionsCount(GQLQuery):
   """
   activeSubscriptionsCount - [will be deprecated; do not use] Returns analytics data about an API per subscription by API id 

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str
      fromDate: str
      toDate: str
      resolution: Resolution

   _args: Args


   type: list[ActiveSubscriptionCount]

class getInternalSubscriptions(GQLQuery):
   """
   getInternalSubscriptions - Get the subscriptions of a team that subscribed to other teams' APIs within the same org

   """
   type: list[BillingSubscription]

class searchSubscribedEntityByApiId(GQLQuery):
   """
   searchSubscribedEntityByApiId - Returns a list of entities subscribed to an API

   """
   class Args(GQLArgsSet, GQLObject): 
      userName: str ##NON NULL
      apiId: str ##NON NULL

   _args: Args


   type: list[Any]

class getSubscriptions(GQLQuery):
   """
   getSubscriptions - [will be deprecated; do not use] Get subscriptions by Id

   """
   class Args(GQLArgsSet, GQLObject): 
      id: int
      userId: int
      apiId: str
      mashapeId: str
      pagingArgs: PagingArgs

   _args: Args


   type: SubscriptionsPaging

class getOrganizationSubscriptions(GQLQuery):
   """
   getOrganizationSubscriptions - [will be deprecated; do not use] Get the subscriptions owned by an organization

   """
   class Args(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: Args


   type: OrgSubscriptions

class subscriptions(GQLQuery):
   """
   subscriptions - Returns a set of subscriptions

   """
   class Args(GQLArgsSet, GQLObject): 
      where: SubscriptionsWhereInput
      pagination: PaginationInput

   _args: Args


   type: SubscriptionConnection

class subscription(GQLQuery):
   """
   subscription - Returns one subscription.

   """
   class Args(GQLArgsSet, GQLObject): 
      id: int

   _args: Args


   type: BillingSubscription

class subscriptionsCount(GQLQuery):
   """
   subscriptionsCount - Returns the count of a set of subscriptions by date range

   """
   class Args(GQLArgsSet, GQLObject): 
      where: SubscriptionsCountWhereInput

   _args: Args


   type: list[SubscriptionsCount]

class getTagsList(GQLQuery):
   """
   getTagsList - gets defined tags list in environment level 

   """
   type: list[TagDefinition]

class tagDefinitions(GQLQuery):
   """
   tagDefinitions - Returns the tag's definitions 

   """
   type: TagDefinitionConnection

class paginatedTeamUsersByOrganizationId(GQLQuery):
   """
   paginatedTeamUsersByOrganizationId - Get organization users ( should be deprecated , please don't use)

   """
   class Args(GQLArgsSet, GQLObject): 
      orgId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: PaginatedTeamUsers

class paginatedTeamUsersByOrganizationIdV2(GQLQuery):
   """
   paginatedTeamUsersByOrganizationIdV2 - Get organization users 

   """
   class Args(GQLArgsSet, GQLObject): 
      orgId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: PaginatedTeamUsers

class teamUserByEmailAndOrgId(GQLQuery):
   """
   teamUserByEmailAndOrgId - Get user in a team by email and Organization id

   """
   class Args(GQLArgsSet, GQLObject): 
      email: str
      orgId: int

   _args: Args


   type: TeamUser

class teamUser(GQLQuery):
   """
   teamUser - Get user by organization Id

   """
   class Args(GQLArgsSet, GQLObject): 
      where: TeamUserWhereInput ##NON NULL

   _args: Args


   type: TeamUser

class findUsersInOrganization(GQLQuery):
   """
   findUsersInOrganization - search users within organization by term 

   """
   class Args(GQLArgsSet, GQLObject): 
      orgId: int
      term: str

   _args: Args


   type: list[TeamUser]

class teamByTeamId(GQLQuery):
   """
   teamByTeamId - get a team based on it's team id and organization id

   """
   class Args(GQLArgsSet, GQLObject): 
      teamId: int
      orgId: int

   _args: Args


   type: Team

class teamsByOrganizationId(GQLQuery):
   """
   teamsByOrganizationId - Get the team based on the Organization Id

   """
   class Args(GQLArgsSet, GQLObject): 
      orgId: int

   _args: Args


   type: list[Team]

class getTeamBySlugifiedName(GQLQuery):
   """
   getTeamBySlugifiedName - Gets teams by slugified key

   """
   class Args(GQLArgsSet, GQLObject): 
      slugifiedName: str

   _args: Args


   type: Team

class searchTeams(GQLQuery):
   """
   searchTeams - Returns a list of teams

   """
   class Args(GQLArgsSet, GQLObject): 
      term: str
      limit: int

   _args: Args


   type: list[Team]

class team(GQLQuery):
   """
   team - get a team based on its id

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Team

class teams(GQLQuery):
   """
   teams - get list of teams based on OrgId and Slugified name

   """
   class Args(GQLArgsSet, GQLObject): 
      where: TeamWhereInput

   _args: Args


   type: list[Team]

class tenant(GQLQuery):
   """
   tenant - Get tenant by tenant ID.

   """
   type: Tenant

class transactions(GQLQuery):
   """
   transactions - Get all transactions by the filters in 'where' input.\n\nNote: Pagination using PaginationInput is only partially supported.\nUse PagingArgs in Where input instead, both for pagination and for sorting.

   """
   class Args(GQLArgsSet, GQLObject): 
      where: TransactionsWhereInput
      pagination: PaginationInput

   _args: Args


   type: TransactionConnection

class transactionsSummary(GQLQuery):
   """
   transactionsSummary - Get details about transactions

   """
   class Args(GQLArgsSet, GQLObject): 
      where: TransactionsSummaryWhereInput

   _args: Args


   type: TransactionsSummary

class transformations(GQLQuery):
   """
   transformations - Get a list of all the transformations from the API Version

   """
   class Args(GQLArgsSet, GQLObject): 
      where: TransformationWhereInput
      orderBy: TransformationOrderByInput
      pagination: PaginationInput

   _args: Args


   type: TransformationConnection ##NON NULL

class tutorials(GQLQuery):
   """
   tutorials - Returns the tutorials for a specified API

   """
   class Args(GQLArgsSet, GQLObject): 
      where: TutorialWhereInput ##NON NULL
      orderBy: TutorialOrderByInput
      pagination: PaginationInput

   _args: Args


   type: TutorialConnection

class getPhoneNumbers(GQLQuery):
   """
   getPhoneNumbers - returns user configures phones for 2fa 

   """
   type: list[Phone]

class getRecoveryCodes(GQLQuery):
   """
   getRecoveryCodes - get Users recovery codes

   """
   type: list[RecoveryCode]

class isTwoFactorEnabledByType(GQLQuery):
   """
   isTwoFactorEnabledByType - is 2fa factor configured on a type 

   """
   class Args(GQLArgsSet, GQLObject): 
      type: str ##NON NULL

   _args: Args


   type: bool

class getUsagesAndParentUsageForSubscription(GQLQuery):
   """
   getUsagesAndParentUsageForSubscription - Get usage for subscriptions

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: list[str]
      resolution: str
      orderDir: str
      periods: list[str]
      parentId: int
      isInternal: bool

   _args: Args


   type: list[UsagesStats]

class getUsagesAgrregatedByTeamsForSubscription(GQLQuery):
   """
   getUsagesAgrregatedByTeamsForSubscription - Get usage aggregated by teams using organizationId and apiId

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: list[str]
      resolution: str
      orderDir: str
      periods: list[str]
      apiVersionId: str
      internalData: list[str]

   _args: Args


   type: list[UsagesStats]

class getUsagesAndParentUsageForSubscriptionByBuckets(GQLQuery):
   """
   getUsagesAndParentUsageForSubscriptionByBuckets - Get usage for subscriptions

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: list[str]
      resolution: str
      periods: list[str]
      parentId: int

   _args: Args


   type: list[UsagesStats]

class getUsagesAgrregatedByTeamsForSubscriptionByBuckets(GQLQuery):
   """
   getUsagesAgrregatedByTeamsForSubscriptionByBuckets - Get usage aggregated by teams using organizationId and apiId

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: list[str]
      resolution: str
      periods: list[str]
      apiVersionId: str

   _args: Args


   type: list[UsagesStats]

class organizationQuotaUsageByApiIdV2(GQLQuery):
   """
   organizationQuotaUsageByApiIdV2 - Returns the usage of an organization's quota by one API

   """
   class Args(GQLArgsSet, GQLObject): 
      apiId: ID
      apiVersionId: ID
      internalData: Any

   _args: Args


   type: OrganizationApiUsagesV2

class getUserInviteByToken(GQLQuery):
   """
   getUserInviteByToken - Get all user invited instances by per organization level token 

   """
   class Args(GQLArgsSet, GQLObject): 
      token: str ##NON NULL

   _args: Args


   type: UserInvite

class checkUserInvitesBranding(GQLQuery):
   """
   checkUserInvitesBranding - [will be deprecated; do not use] checks users branding

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UserInvitesBrandingInput

   _args: Args


   type: bool

class checkIfEmailsAlreadyInvited(GQLQuery):
   """
   checkIfEmailsAlreadyInvited - check if user is already invite to an organization 

   """
   class Args(GQLArgsSet, GQLObject): 
      orgId: ID ##NON NULL
      emails: list[str] ##NON NULL

   _args: Args


   type: Any

class searchUsersToInvite(GQLQuery):
   """
   searchUsersToInvite - Returns a list of users to invite

   """
   class Args(GQLArgsSet, GQLObject): 
      orgId: ID ##NON NULL
      brand: str
      term: str
      offset: int
      limit: int

   _args: Args


   type: list[InviteUsersSearch]

class getUserSavedApis(GQLQuery):
   """
   getUserSavedApis - Gets uses saved APIs

   """
   class Args(GQLArgsSet, GQLObject): 
      userCollectionId: str

   _args: Args


   type: UserSavedApi ##NON NULL

class userById(GQLQuery):
   """
   userById - Get user by ID

   """
   class Args(GQLArgsSet, GQLObject): 
      id: int

   _args: Args


   type: User

class userByUsername(GQLQuery):
   """
   userByUsername - Get user by username

   """
   class Args(GQLArgsSet, GQLObject): 
      username: str
      includeUserAttributes: bool

   _args: Args


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
   class Args(GQLArgsSet, GQLObject): 
      brand: str
      term: str
      offset: int
      limit: int

   _args: Args


   type: list[User]

class searchUsersV2(GQLQuery):
   """
   searchUsersV2 - Returns a list of users

   """
   class Args(GQLArgsSet, GQLObject): 
      where: SearchUsersWhereInput ##NON NULL

   _args: Args


   type: User ##NON NULL

class user(GQLQuery):
   """
   user - Get details about a user

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: User

class users(GQLQuery):
   """
   users - Get users by any attribute type

   """
   class Args(GQLArgsSet, GQLObject): 
      where: UserWhereInput ##NON NULL

   _args: Args


   type: list[User]

class getVirtualPermissions(GQLQuery):
   """
   getVirtualPermissions - Get full permission list associate to a permission 

   """
   class Args(GQLArgsSet, GQLObject): 
      permissionLevel: list[RoleLevel]

   _args: Args


   type: list[Permission]

class virtualPermissions(GQLQuery):
   """
   virtualPermissions - Query by ID or display name to get back a virtual permission

   """
   class Args(GQLArgsSet, GQLObject): 
      where: VirtualPermissionWhereInput ##NON NULL

   _args: Args


   type: list[VirtualPermission]

class getWorkflowsForProvider(GQLQuery):
   """
   getWorkflowsForProvider - Get the approval list requested to the the API caller that is a provider

   """
   class Args(GQLArgsSet, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

class getWorkflowsForDeveloper(GQLQuery):
   """
   getWorkflowsForDeveloper - Get the approval list requested by the API caller 

   """
   class Args(GQLArgsSet, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

class getWorkflowsByRequestor(GQLQuery):
   """
   getWorkflowsByRequestor - Get the approval list requested to the  the API caller

   """
   class Args(GQLArgsSet, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

class getWorkflowsByRequestee(GQLQuery):
   """
   getWorkflowsByRequestee - Get the approval list requested by the API caller

   """
   class Args(GQLArgsSet, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

class canWorkflowBeSubmitted(GQLQuery):
   """
   canWorkflowBeSubmitted - Determine if a workflow can be submitted

   """
   class Args(GQLArgsSet, GQLObject): 
      options: CanWorkflowBeSubmittedOptions

   _args: Args


   type: bool

class getWorkflowAudits(GQLQuery):
   """
   getWorkflowAudits - Get workflows operations audits 

   """
   class Args(GQLArgsSet, GQLObject): 
      workflowId: int

   _args: Args


   type: WorkFlowAuditsResponse

class getWorkflowsCount(GQLQuery):
   """
   getWorkflowsCount - get approval list count 

   """
   class Args(GQLArgsSet, GQLObject): 
      options: GetWorkflowCountOptions

   _args: Args


   type: int

class exclusions(GQLQuery):
   """
   exclusions - Returns exclusions for Hub Extensions

   """
   class Args(GQLArgsSet, GQLObject): 
      client: str
      page: str

   _args: Args


   type: list[Exclusion]


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
