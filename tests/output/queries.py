from pygqlmap import GQLQuery
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class ping(GQLQuery):
   type: str ##NON NULL

class eventUrls(GQLQuery):
   class EventUrlConnectionArgs(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: EventUrlWhereInput
      order: EventUrlSortablesInput

   _args: EventUrlConnectionArgs


   type: EventUrlConnection ##NON NULL

class eventUrl(GQLQuery):
   class EventUrlArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: EventUrlArgs


   type: EventUrl

class eventTypes(GQLQuery):
   type: EventType ##NON NULL

class eventConfig(GQLQuery):
   type: EventConfig

class gatewayInstances(GQLQuery):
   class GatewayInstanceConnectionArgs(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: GatewayInstanceWhereInput
      order: GatewayInstanceSortingInput

   _args: GatewayInstanceConnectionArgs


   type: GatewayInstanceConnection ##NON NULL

class gatewayInstance(GQLQuery):
   class GatewayInstanceArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: GatewayInstanceArgs


   type: GatewayInstance ##NON NULL

class gatewayTemplates(GQLQuery):
   class GatewayTemplateConnectionArgs(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: GatewayTemplateWhereInput
      order: GatewayTemplateSortingInput

   _args: GatewayTemplateConnectionArgs


   type: GatewayTemplateConnection ##NON NULL

class gatewayTemplate(GQLQuery):
   class GwTemplateArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: GwTemplateArgs


   type: GwTemplate ##NON NULL

class gatewayTemplatesParams(GQLQuery):
   class GatewayTemplateParamConnectionArgs(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: GatewayTemplateParamsWhereInput
      order: GatewayTemplateParamSortingInput

   _args: GatewayTemplateParamConnectionArgs


   type: GatewayTemplateParamConnection ##NON NULL

class gatewayTemplateParam(GQLQuery):
   class GatewayTemplateParamArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: GatewayTemplateParamArgs


   type: GatewayTemplateParam ##NON NULL

class envConfigCategories(GQLQuery):
   type: EnvConfigCategory ##NON NULL

class envConfig(GQLQuery):
   class EnvConfigArgs(GQLArgsSet, GQLObject): 
      id: int ##NON NULL

   _args: EnvConfigArgs


   type: EnvConfig ##NON NULL

class envConfigs(GQLQuery):
   class EnvConfigArgs(GQLArgsSet, GQLObject): 
      envConfigTerm: EnvConfigTerm ##NON NULL

   _args: EnvConfigArgs


   type: EnvConfig ##NON NULL

class adminAuditLogs(GQLQuery):
   class AdminAuditLogConnectionArgs(GQLArgsSet, GQLObject): 
      where: AdminAuditLogInput
      pagination: PaginationArgs
      orderBy: AdminAuditLogSortablesInput

   _args: AdminAuditLogConnectionArgs


   type: AdminAuditLogConnection

class eventLogs(GQLQuery):
   class EventLogConnectionArgs(GQLArgsSet, GQLObject): 
      where: EventLogInput
      pagination: PaginationArgs
      orderBy: EventLogSortablesInput

   _args: EventLogConnectionArgs


   type: EventLogConnection

class extensions(GQLQuery):
   class ExtensionArgs(GQLArgsSet, GQLObject): 
      client: str
      page: str
      path: str

   _args: ExtensionArgs


   type: Extension ##LIST

class getSEOTagsByURL(GQLQuery):
   class SEOArgs(GQLArgsSet, GQLObject): 
      url: str

   _args: SEOArgs


   type: SEO

class getUserAlertById(GQLQuery):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: UserAlertArgs


   type: UserAlert

class getUserAlertsByScope(GQLQuery):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      scope: ID ##NON NULL

   _args: UserAlertArgs


   type: UserAlert ##LIST

class getAlertsDefinitions(GQLQuery):
   type: AlertDefinition ##NON NULL

class userAlerts(GQLQuery):
   class UserAlertsConnectionArgs(GQLArgsSet, GQLObject): 
      where: UserAlertsWhereInput ##NON NULL

   _args: UserAlertsConnectionArgs


   type: UserAlertsConnection ##NON NULL

class userAlert(GQLQuery):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: UserAlertArgs


   type: UserAlert

class allowedPlanDeveloperByPlanId(GQLQuery):
   class AllowedPlanDeveloperArgs(GQLArgsSet, GQLObject): 
      planId: str

   _args: AllowedPlanDeveloperArgs


   type: AllowedPlanDeveloper ##LIST

class apiCertificate(GQLQuery):
   class ApiCertificateArgs(GQLArgsSet, GQLObject): 
      apiCertificateId: ID ##NON NULL

   _args: ApiCertificateArgs


   type: ApiCertificate

class apiCertificates(GQLQuery):
   class ApiCertificateConnectionArgs(GQLArgsSet, GQLObject): 
      where: ApiCertificateWhereInput
      orderBy: ApiCertificateOrderByInput
      pagination: PaginationInput

   _args: ApiCertificateConnectionArgs


   type: ApiCertificateConnection ##NON NULL

class apiDevelopersByApiId(GQLQuery):
   class ApiDeveloperArgs(GQLArgsSet, GQLObject): 
      apiId: str
      pagingArgs: PagingArgs

   _args: ApiDeveloperArgs


   type: ApiDeveloper ##NON NULL

class apiFollowers(GQLQuery):
   class ApiFollowerConnectionArgs(GQLArgsSet, GQLObject): 
      where: ApiFollowerWhereInput ##NON NULL
      orderBy: ApiFollowerOrderByInput
      pagination: PaginationInput

   _args: ApiFollowerConnectionArgs


   type: ApiFollowerConnection ##NON NULL

class apiReferenceByApiAndVersionId(GQLQuery):
   class ApiReferenceArgs(GQLArgsSet, GQLObject): 
      apiId: str ##NON NULL
      versionId: str ##NON NULL

   _args: ApiReferenceArgs


   type: ApiReference

class apiReferences(GQLQuery):
   class ApiReferenceConnectionArgs(GQLArgsSet, GQLObject): 
      where: ApiReferenceWhereInput

   _args: ApiReferenceConnectionArgs


   type: ApiReferenceConnection ##NON NULL

class apiSearch(GQLQuery):
   class ApiSearchPagedArgs(GQLArgsSet, GQLObject): 
      searchArguments: SearchArguments

   _args: ApiSearchPagedArgs


   type: ApiSearchPaged

class apiSearchV3(GQLQuery):
   class ApiSearchPagedArgs(GQLArgsSet, GQLObject): 
      searchArguments: SearchArguments

   _args: ApiSearchPagedArgs


   type: ApiSearchPaged

class apiSpecImportProgresses(GQLQuery):
   class ApiSpecImportProcessArgs(GQLArgsSet, GQLObject): 
      trackingIds: ID ##NON NULL ##LIST

   _args: ApiSpecImportProcessArgs


   type: ApiSpecImportProcess ##NON NULL

class bulkApisSummaryByTrackingIds(GQLQuery):
   class BatchTrackingIdsSummaryArgs(GQLArgsSet, GQLObject): 
      trackingIds: ID ##NON NULL ##LIST

   _args: BatchTrackingIdsSummaryArgs


   type: BatchTrackingIdsSummary

class calculatedStatistics(GQLQuery):
   class CalculatedStatisticsArgs(GQLArgsSet, GQLObject): 
      fromDate: str ##NON NULL
      toDate: str ##NON NULL
      resolution: str
      projectIds: str ##LIST
      apiIds: str ##LIST
      endpoints: str ##LIST
      groupBy: StatsGroupBy
      apiVersionIds: ID ##LIST
      entityId: ID
      timeOffset: int
      filters: StatsFilterBy ##LIST

   _args: CalculatedStatisticsArgs


   type: CalculatedStatistics

class getApiVersion(GQLQuery):
   class ApiVersionArgs(GQLArgsSet, GQLObject): 
      versionId: ID ##NON NULL

   _args: ApiVersionArgs


   type: ApiVersion

class apiVersion(GQLQuery):
   class ApiVersionArgs(GQLArgsSet, GQLObject): 
      apiVersionId: ID ##NON NULL

   _args: ApiVersionArgs


   type: ApiVersion

class apiVersions(GQLQuery):
   class ApiVersionConnectionArgs(GQLArgsSet, GQLObject): 
      where: ApiVersionWhereInput
      orderBy: ApiVersionOrderByInput
      pagination: PaginationInput

   _args: ApiVersionConnectionArgs


   type: ApiVersionConnection ##NON NULL

class api(GQLQuery):
   class ApiArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: ApiArgs


   type: Api

class apis(GQLQuery):
   class ApiConnectionArgs(GQLArgsSet, GQLObject): 
      where: ApiWhereInput
      orderBy: ApiOrderByInput
      pagination: PaginationInput

   _args: ApiConnectionArgs


   type: ApiConnection ##NON NULL

class exportOpenApi(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      apiId: ID ##NON NULL
      apiVersionId: ID

   _args: AnyArgs


   type: Any

class validateSwagger(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      input: validateSwaggerInput

   _args: AnyArgs


   type: Any

class applicationAuthorization(GQLQuery):
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization ##NON NULL

class applicationAuthorizations(GQLQuery):
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject): 
      where: AppAuthorizationsWhereInput ##NON NULL

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization ##NON NULL

class applicationEnvironmentsKeysByApplicationIdAndEnvironment(GQLQuery):
   class ApplicationEnvironmentPagingArgs(GQLArgsSet, GQLObject): 
      applicationId: str
      environment: str

   _args: ApplicationEnvironmentPagingArgs


   type: ApplicationEnvironmentPaging

class applicationEnvironmentsByApplicationIdAndEnvironment(GQLQuery):
   class ApplicationEnvironmentArgs(GQLArgsSet, GQLObject): 
      applicationId: str
      environment: str

   _args: ApplicationEnvironmentArgs


   type: ApplicationEnvironment

class applicationById(GQLQuery):
   class ApplicationArgs(GQLArgsSet, GQLObject): 
      id: int

   _args: ApplicationArgs


   type: Application

class asset(GQLQuery):
   class AssetArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: AssetArgs


   type: Asset

class assets(GQLQuery):
   class AssetArgs(GQLArgsSet, GQLObject): 
      where: AssetWhereInput ##NON NULL

   _args: AssetArgs


   type: Asset ##NON NULL

class assetsDownloadUrls(GQLQuery):
   class AssetForDownloadArgs(GQLArgsSet, GQLObject): 
      where: AssetWhereInput ##NON NULL

   _args: AssetForDownloadArgs


   type: AssetForDownload ##NON NULL

class asyncApiConfigurations(GQLQuery):
   class AsyncApiConfigurationConnectionArgs(GQLArgsSet, GQLObject): 
      where: AsyncApiConfigurationWhereInput ##NON NULL

   _args: AsyncApiConfigurationConnectionArgs


   type: AsyncApiConfigurationConnection ##NON NULL

class userAttributesByUserId(GQLQuery):
   class UserAttributesArgs(GQLArgsSet, GQLObject): 
      userId: int

   _args: UserAttributesArgs


   type: UserAttributes

class auditByOrganizationId(GQLQuery):
   class auditTrailsArgs(GQLArgsSet, GQLObject): 
      searchTerm: str
      from_: int
      orgId: int

   _args: auditTrailsArgs


   type: auditTrails

class audit(GQLQuery):
   class auditTrailsArgs(GQLArgsSet, GQLObject): 
      where: AuditWhereInput ##NON NULL

   _args: auditTrailsArgs


   type: auditTrails

class auditLogin(GQLQuery):
   class auditTrailsArgs(GQLArgsSet, GQLObject): 
      from_: int
      userId: str

   _args: auditTrailsArgs


   type: auditTrails

class userByEmail(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      email: str

   _args: UserArgs


   type: User

class activeUser(GQLQuery):
   type: User

class getAuthStrategies(GQLQuery):
   type: authStrategy ##LIST

class getBillingFeaturesByApiVersionId(GQLQuery):
   class BillingFeatureArgs(GQLArgsSet, GQLObject): 
      versionId: str

   _args: BillingFeatureArgs


   type: BillingFeature ##LIST

class getBillingFeaturesByApiId(GQLQuery):
   class BillingFeatureArgs(GQLArgsSet, GQLObject): 
      apiId: str ##NON NULL

   _args: BillingFeatureArgs


   type: BillingFeature ##LIST

class isMonetizationEnabled(GQLQuery):
   type: bool

class billingItems(GQLQuery):
   class BillingItemConnectionArgs(GQLArgsSet, GQLObject): 
      where: BillingItemsWhereInput ##NON NULL

   _args: BillingItemConnectionArgs


   type: BillingItemConnection

class getFreeSeatsObj(GQLQuery):
   class SeatsBillingInformationArgs(GQLArgsSet, GQLObject): 
      orgId: ID ##NON NULL

   _args: SeatsBillingInformationArgs


   type: SeatsBillingInformation

class getBillingPlanVersionsByApiId(GQLQuery):
   class BillingPlanVersionsResponseArgs(GQLArgsSet, GQLObject): 
      apiId: str ##NON NULL
      apiVersionId: str
      pagingArgs: PagingArgsBilling
      filters: BillingPlanVersionFilters

   _args: BillingPlanVersionsResponseArgs


   type: BillingPlanVersionsResponse

class getBillingPlanVersionById(GQLQuery):
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject): 
      billingPlanVersionId: str ##NON NULL

   _args: BillingPlanVersionArgs


   type: BillingPlanVersion

class billingPlanVersion(GQLQuery):
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: BillingPlanVersionArgs


   type: BillingPlanVersion

class billingPlanVersions(GQLQuery):
   class BillingPlanVersionConnectionArgs(GQLArgsSet, GQLObject): 
      where: BillingPlanVersionWhereInput
      pagination: PaginationInput

   _args: BillingPlanVersionConnectionArgs


   type: BillingPlanVersionConnection

class calculatedStatisticsByEndpointAndApiversion(GQLQuery):
   class CalculatedStatisticsArgs(GQLArgsSet, GQLObject): 
      fromDate: str ##NON NULL
      toDate: str ##NON NULL
      resolution: str
      endpointsAndApiVersions: endpointsAndApiVersionCouples ##NON NULL ##LIST
      groupBy: StatsGroupBy
      apiId: str ##NON NULL
      entityId: ID
      timeOffset: int
      filters: StatsFilterBy ##LIST

   _args: CalculatedStatisticsArgs


   type: CalculatedStatistics

class categoriesV2(GQLQuery):
   class CategoryConnectionArgs(GQLArgsSet, GQLObject): 
      where: CategoryWhereInput
      orderBy: CategoryOrderByInput
      pagination: PaginationInput

   _args: CategoryConnectionArgs


   type: CategoryConnection ##NON NULL

class categoryEntities(GQLQuery):
   class CategoryEntityArgs(GQLArgsSet, GQLObject): 
      lang: str
      pagingArgs: PagingArgs

   _args: CategoryEntityArgs


   type: CategoryEntity ##LIST

class categories(GQLQuery):
   class CategoryArgs(GQLArgsSet, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection

   _args: CategoryArgs


   type: Category ##LIST

class collectionsItemsByIds(GQLQuery):
   class CollectionItemArgs(GQLArgsSet, GQLObject): 
      ids: ID ##NON NULL ##LIST

   _args: CollectionItemArgs


   type: CollectionItem ##LIST

class collections(GQLQuery):
   class CollectionsResponseArgs(GQLArgsSet, GQLObject): 
      where: CollectionsWhereInput
      orderBy: CollectionsOrderByInput
      minWeightToFetchApis: int

   _args: CollectionsResponseArgs


   type: CollectionsResponse

class collectionsByOwnerId(GQLQuery):
   class CollectionsResponseArgs(GQLArgsSet, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection
      minWeightToFetchApis: int
      collection_type: str

   _args: CollectionsResponseArgs


   type: CollectionsResponse

class getOrgHomepageCollections(GQLQuery):
   class CollectionsResponseArgs(GQLArgsSet, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection
      minWeightToFetchApis: int

   _args: CollectionsResponseArgs


   type: CollectionsResponse

class collectionById(GQLQuery):
   class CollectionArgs(GQLArgsSet, GQLObject): 
      collectionId: ID ##NON NULL

   _args: CollectionArgs


   type: Collection

class collection(GQLQuery):
   class CollectionArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: CollectionArgs


   type: Collection

class collapsedCollections(GQLQuery):
   class CollapsedCollectionArgs(GQLArgsSet, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection
      limit: int
      page: int

   _args: CollapsedCollectionArgs


   type: CollapsedCollection ##LIST

class collectionBySlugifiedKey(GQLQuery):
   class CollectionArgs(GQLArgsSet, GQLObject): 
      slugifiedKey: str

   _args: CollectionArgs


   type: Collection

class getPrivateCollections(GQLQuery):
   type: Collection ##LIST

class getPrivateCollectionsV2(GQLQuery):
   type: Collection ##LIST

class collectionBySlugifiedKeyV2(GQLQuery):
   class CollectionV2Args(GQLArgsSet, GQLObject): 
      slugifiedKey: str

   _args: CollectionV2Args


   type: CollectionV2

class collectionBySlugifiedKeyV3(GQLQuery):
   class CollectionV3Args(GQLArgsSet, GQLObject): 
      slugifiedKey: str

   _args: CollectionV3Args


   type: CollectionV3

class getCommentsByIssueIdV2(GQLQuery):
   class PaginatedCommentsArgs(GQLArgsSet, GQLObject): 
      issueId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: PaginatedCommentsArgs


   type: PaginatedComments

class getCommentByIdV2(GQLQuery):
   class CommentArgs(GQLArgsSet, GQLObject): 
      issueId: int ##NON NULL
      commentId: int ##NON NULL

   _args: CommentArgs


   type: Comment

class search(GQLQuery):
   class ApiSearchArgs(GQLArgsSet, GQLObject): 
      term: str ##NON NULL

   _args: ApiSearchArgs


   type: ApiSearch ##NON NULL

class searchEntityByApiId(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      userName: str ##NON NULL
      apiId: str ##NON NULL
      distinct: str

   _args: AnyArgs


   type: Any ##LIST

class getOpenApiSpecByApiId(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      apiId: ID

   _args: AnyArgs


   type: Any

class entityById(GQLQuery):
   class EntityArgs(GQLArgsSet, GQLObject): 
      id: ID

   _args: EntityArgs


   type: Entity

class activeEntity(GQLQuery):
   type: Entity

class apiByNameAndOwnerName(GQLQuery):
   class ApiArgs(GQLArgsSet, GQLObject): 
      apiName: str
      ownerName: str

   _args: ApiArgs


   type: Api

class apiBySlugifiedNameAndOwnerName(GQLQuery):
   class ApiArgs(GQLArgsSet, GQLObject): 
      slugifiedName: str
      ownerName: str

   _args: ApiArgs


   type: Api

class apiByNameAndOwnerId(GQLQuery):
   class ApiArgs(GQLArgsSet, GQLObject): 
      apiName: str
      ownerId: str

   _args: ApiArgs


   type: Api

class userFollows(GQLQuery):
   class FollowUserArgs(GQLArgsSet, GQLObject): 
      userId: int

   _args: FollowUserArgs


   type: FollowUser ##LIST

class apiById(GQLQuery):
   class ApiArgs(GQLArgsSet, GQLObject): 
      apiId: str

   _args: ApiArgs


   type: Api

class apisById(GQLQuery):
   class ApiArgs(GQLArgsSet, GQLObject): 
      ids: ID ##NON NULL ##LIST

   _args: ApiArgs


   type: Api ##LIST

class followUserAction(GQLQuery):
   class FollowPairArgs(GQLArgsSet, GQLObject): 
      followerId: int
      followeeId: int

   _args: FollowPairArgs


   type: FollowPair

class userFollowers(GQLQuery):
   class FollowerArgs(GQLArgsSet, GQLObject): 
      userId: int

   _args: FollowerArgs


   type: Follower ##LIST

class calculateSeatsPrice(GQLQuery):
   class floatArgs(GQLArgsSet, GQLObject): 
      seats: int ##NON NULL

   _args: floatArgs


   type: float ##NON NULL

class getSeatsTransactionsByOrgId(GQLQuery):
   class OrgTransactionArgs(GQLArgsSet, GQLObject): 
      orgId: int ##NON NULL

   _args: OrgTransactionArgs


   type: OrgTransaction ##LIST

class organizationsTreeToken(GQLQuery):
   type: str

class getMinimumSeats(GQLQuery):
   type: int ##NON NULL

class transactionsById(GQLQuery):
   class TransactionsPagingArgs(GQLArgsSet, GQLObject): 
      apiId: str
      userId: int
      type: str
      pagingArgs: PagingArgs
      queryFilters: QueryFilters
      paymentStatusFilters: TransactionPaymentStatus ##LIST

   _args: TransactionsPagingArgs


   type: TransactionsPaging

class unionDiscussionsByAuthor(GQLQuery):
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
   type: ContextEntity

class getActiveTeamContext(GQLQuery):
   type: ContextEntity

class transactionsAnalyticsByApiId(GQLQuery):
   class TransactionsAnalyticsArgs(GQLArgsSet, GQLObject): 
      apiId: str
      fromDate: str
      toDate: str
      attributes: str

   _args: TransactionsAnalyticsArgs


   type: TransactionsAnalytics

class getConsumers(GQLQuery):
   class ConsumersArgs(GQLArgsSet, GQLObject): 
      apiId: str
      userId: int ##LIST
      offset: int
      limit: int
      sort: str
      usernames: str
      plansFilter: str ##LIST
      lastActive: str ##LIST

   _args: ConsumersArgs


   type: Consumers

class getFreeConsumers(GQLQuery):
   class ConsumersArgs(GQLArgsSet, GQLObject): 
      apiId: ID ##NON NULL ##LIST
      offset: int
      limit: int
      order: str
      lastActive: str ##LIST
      username: str ##LIST
      userId: int ##LIST

   _args: ConsumersArgs


   type: Consumers

class consumers(GQLQuery):
   class ConsumerConnectionArgs(GQLArgsSet, GQLObject): 
      where: ConsumersWhereInput ##NON NULL

   _args: ConsumerConnectionArgs


   type: ConsumerConnection

class requestAdminToSubscribeToAnAPI(GQLQuery):
   class boolArgs(GQLArgsSet, GQLObject): 
      eventData: ContactAdminSubscribeToAPIEvent ##NON NULL

   _args: boolArgs


   type: bool

class getCountryMetadata(GQLQuery):
   class CountryArgs(GQLArgsSet, GQLObject): 
      ip: str

   _args: CountryArgs


   type: Country

class unionIssuesByAuthorV2(GQLQuery):
   class DiscussionObjectArgs(GQLArgsSet, GQLObject): 
      authorId: int
      type: str
      pagingArgs: PagingArgs
      apiIds: str ##LIST

   _args: DiscussionObjectArgs


   type: DiscussionObject

class getIssuesByApiIdV2(GQLQuery):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      apiId: str ##NON NULL
      pagingArgs: PagingArgs
      providerId: str

   _args: IssueObjectArgs


   type: IssueObject

class getIssuesByApiIdsV2(GQLQuery):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      apiIds: str ##NON NULL ##LIST
      pagingArgs: PagingArgs

   _args: IssueObjectArgs


   type: IssueObject

class endpointStats(GQLQuery):
   class EndpointStatsArgs(GQLArgsSet, GQLObject): 
      apiIds: ID ##NON NULL ##LIST
      projectIds: ID ##LIST
      endpointIds: ID ##LIST
      fromDate: str
      toDate: str
      resolution: str

   _args: EndpointStatsArgs


   type: EndpointStats ##LIST

class endpointStatsByEntity(GQLQuery):
   class EndpointStatsArgs(GQLArgsSet, GQLObject): 
      entityId: ID
      apiId: ID ##NON NULL
      endpointIds: ID ##LIST
      fromDate: DateTime
      toDate: DateTime
      resolution: Resolution
      timeOffset: int
      filters: StatsFilterBy ##LIST

   _args: EndpointStatsArgs


   type: EndpointStats ##LIST

class endpointStatsByEntityV2(GQLQuery):
   class VersionEndpointStatsArgs(GQLArgsSet, GQLObject): 
      entityId: ID
      apiId: ID ##NON NULL
      endpointsAndApiVersions: EndpointAndVersion ##LIST
      fromDate: DateTime
      toDate: DateTime
      resolution: Resolution
      timeOffset: int
      filters: StatsFilterBy ##LIST

   _args: VersionEndpointStatsArgs


   type: VersionEndpointStats ##LIST

class getEndpointsWithinDateByParameters(GQLQuery):
   class EndpointStatsArgs(GQLArgsSet, GQLObject): 
      input: endpointsWithinDateInput ##NON NULL
      showDeleted: bool

   _args: EndpointStatsArgs


   type: EndpointStats ##LIST

class endpoint(GQLQuery):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: EndpointArgs


   type: Endpoint

class endpoints(GQLQuery):
   class EndpointConnectionArgs(GQLArgsSet, GQLObject): 
      where: EndpointWhereInput ##NON NULL

   _args: EndpointConnectionArgs


   type: EndpointConnection

class searchEntities(GQLQuery):
   class EntityArgs(GQLArgsSet, GQLObject): 
      term: str
      limit: int
      status: str
      type: str

   _args: EntityArgs


   type: Entity ##LIST

class entitiesMetadata(GQLQuery):
   class EntityMetadataConnectionArgs(GQLArgsSet, GQLObject): 
      where: EntityMetadataWhereInput ##NON NULL
      orderBy: EntityMetadataOrderByInput
      pagination: PaginationInput

   _args: EntityMetadataConnectionArgs


   type: EntityMetadataConnection ##NON NULL

class getEntitiesRoles(GQLQuery):
   class EntityRoleArgs(GQLArgsSet, GQLObject): 
      entityIds: int ##LIST
      orgId: int
      parentIds: int ##LIST

   _args: EntityRoleArgs


   type: EntityRole ##LIST

class entitiesRoles(GQLQuery):
   class EntityRoleConnectionArgs(GQLArgsSet, GQLObject): 
      where: EntityRoleWhereInput ##NON NULL
      orderBy: EntityRoleOrderByInput
      pagination: PaginationInput

   _args: EntityRoleConnectionArgs


   type: EntityRoleConnection ##NON NULL

class getLogsCSV(GQLQuery):
   class LogsCSVArgs(GQLArgsSet, GQLObject): 
      apiId: ID
      projectId: ID

   _args: LogsCSVArgs


   type: LogsCSV ##LIST

class exportLogsCSVProvider(GQLQuery):
   class LogsCSVExportsArgs(GQLArgsSet, GQLObject): 
      contextId: ID ##NON NULL
      fromDate: DateTime ##NON NULL
      toDate: DateTime ##NON NULL
      totalCount: int ##NON NULL
      filters: RequestLogFilters
      timeOffset: int

   _args: LogsCSVExportsArgs


   type: LogsCSVExports

class exportLogsCSVDeveloper(GQLQuery):
   class LogsCSVExportsArgs(GQLArgsSet, GQLObject): 
      contextId: ID ##NON NULL
      fromDate: DateTime ##NON NULL
      toDate: DateTime ##NON NULL
      totalCount: int ##NON NULL
      filters: RequestLogFilters
      timeOffset: int

   _args: LogsCSVExportsArgs


   type: LogsCSVExports

class gateways(GQLQuery):
   type: GatewayConnection

class getGateways(GQLQuery):
   type: Gateway ##LIST

class getGatewayConfiguration(GQLQuery):
   class ApiGatewayConfigurationArgs(GQLArgsSet, GQLObject): 
      id: int ##NON NULL

   _args: ApiGatewayConfigurationArgs


   type: ApiGatewayConfiguration

class graphQlIntrospectionSchema(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      introspectionCallUrl: str ##NON NULL

   _args: AnyArgs


   type: Any ##NON NULL

class headlinesByApiNameAndOwnerId(GQLQuery):
   class HeadlineArgs(GQLArgsSet, GQLObject): 
      apiName: str
      apiOwnerId: str
      size: int

   _args: HeadlineArgs


   type: Headline ##LIST

class getIssuesByOrganizatonId(GQLQuery):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      id: str ##NON NULL
      pagingArgs: PagingArgs

   _args: IssueObjectArgs


   type: IssueObject

class getResponseTimeByProviderId(GQLQuery):
   class floatArgs(GQLArgsSet, GQLObject): 
      providerId: int ##NON NULL

   _args: floatArgs


   type: float ##NON NULL

class getAverageResponseTime(GQLQuery):
   type: float ##NON NULL

class unionIssuesByAuthor(GQLQuery):
   class DiscussionObjectArgs(GQLArgsSet, GQLObject): 
      authorId: int
      type: str
      pagingArgs: PagingArgs

   _args: DiscussionObjectArgs


   type: DiscussionObject

class getIssueByIdV2(GQLQuery):
   class IssueArgs(GQLArgsSet, GQLObject): 
      issueId: int

   _args: IssueArgs


   type: Issue

class getIssuesByOrganizationId(GQLQuery):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      id: str
      pagingArgs: PagingArgs

   _args: IssueObjectArgs


   type: IssueObject

class getIssuesByTeamIdV2(GQLQuery):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      id: str
      pagingArgs: PagingArgs

   _args: IssueObjectArgs


   type: IssueObject

class getIssuesFollowsByUserIdV2(GQLQuery):
   class IssueFollowArgs(GQLArgsSet, GQLObject): 
      userId: int

   _args: IssueFollowArgs


   type: IssueFollow ##LIST

class kafkaConfiguration(GQLQuery):
   class KafkaConfigurationArgs(GQLArgsSet, GQLObject): 
      apiVersionId: str ##NON NULL

   _args: KafkaConfigurationArgs


   type: KafkaConfiguration

class kafkaTopics(GQLQuery):
   class KafkaTopicsArgs(GQLArgsSet, GQLObject): 
      apiVersionId: str ##NON NULL

   _args: KafkaTopicsArgs


   type: KafkaTopics

class kafkaSchemas(GQLQuery):
   class KafkaSchemasArgs(GQLArgsSet, GQLObject): 
      apiVersionId: str ##NON NULL

   _args: KafkaSchemasArgs


   type: KafkaSchemas

class kafkaTopicMetadata(GQLQuery):
   class TopicMetadataResponseArgs(GQLArgsSet, GQLObject): 
      apiVersionId: str ##NON NULL
      topicName: str ##NON NULL

   _args: TopicMetadataResponseArgs


   type: TopicMetadataResponse

class getTemplate(GQLQuery):
   class EnvelopeTemplateArgs(GQLArgsSet, GQLObject): 
      accountId: str
      templateId: str

   _args: EnvelopeTemplateArgs


   type: EnvelopeTemplate

class getLegalAgreementInfo(GQLQuery):
   type: LegalAgreementInfo

class updateLegalAgreementInfo(GQLQuery):
   class LegalAgreementInfoArgs(GQLArgsSet, GQLObject): 
      input: UpdateLegalAgreementInfo

   _args: LegalAgreementInfoArgs


   type: LegalAgreementInfo

class createLegalAgreementInfo(GQLQuery):
   class LegalAgreementInfoArgs(GQLArgsSet, GQLObject): 
      input: CreateLegalAgreementInfo

   _args: LegalAgreementInfoArgs


   type: LegalAgreementInfo

class deleteLegalAgreementInfo(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      entityId: str

   _args: AnyArgs


   type: Any

class getLegalAgreementSigningURL(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      input: GetLegalAgreementSigningURLInput ##NON NULL

   _args: AnyArgs


   type: Any

class logPayloadByRequestId(GQLQuery):
   class LogPayloadArgs(GQLArgsSet, GQLObject): 
      requestId: ID
      callTime: str

   _args: LogPayloadArgs


   type: LogPayload

class logPayloadByRequestIdWithLoggingRestrictions(GQLQuery):
   class RestrictedLogPayloadArgs(GQLArgsSet, GQLObject): 
      requestId: ID
      callTime: str
      apiId: str

   _args: RestrictedLogPayloadArgs


   type: RestrictedLogPayload

class developerLogPayloadByRequestIdWithLoggingRestrictions(GQLQuery):
   class RestrictedLogPayloadArgs(GQLArgsSet, GQLObject): 
      requestId: ID
      callTime: str
      apiId: str
      projectId: str

   _args: RestrictedLogPayloadArgs


   type: RestrictedLogPayload

class messageThreads(GQLQuery):
   class MessageThreadsObjectArgs(GQLArgsSet, GQLObject): 
      where: MessageThreadsWhereInput

   _args: MessageThreadsObjectArgs


   type: MessageThreadsObject

class messages(GQLQuery):
   class MessageArgs(GQLArgsSet, GQLObject): 
      where: MessagesWhereInput ##NON NULL

   _args: MessageArgs


   type: Message ##LIST

class getApiAverageResponseTime(GQLQuery):
   class floatArgs(GQLArgsSet, GQLObject): 
      apiId: str ##NON NULL

   _args: floatArgs


   type: float

class getProviderAverageResponseTime(GQLQuery):
   class floatArgs(GQLArgsSet, GQLObject): 
      providerId: int ##NON NULL

   _args: floatArgs


   type: float

class getRelativeAverageResponseTime(GQLQuery):
   class RelativeARTResponseArgs(GQLArgsSet, GQLObject): 
      providerId: int ##NON NULL

   _args: RelativeARTResponseArgs


   type: RelativeARTResponse

class getMessageThread(GQLQuery):
   class MessageThreadArgs(GQLArgsSet, GQLObject): 
      threadId: int

   _args: MessageThreadArgs


   type: MessageThread

class newNotificationsByUserId(GQLQuery):
   class NewNotificationArgs(GQLArgsSet, GQLObject): 
      userId: int
      limit: int
      offset: int

   _args: NewNotificationArgs


   type: NewNotification ##LIST

class notificationsByUserId(GQLQuery):
   class NotificationArgs(GQLArgsSet, GQLObject): 
      userId: int
      limit: int
      offset: int

   _args: NotificationArgs


   type: Notification ##LIST

class organization(GQLQuery):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: OrganizationArgs


   type: Organization

class organizations(GQLQuery):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      where: OrganizationWhereInput

   _args: OrganizationArgs


   type: Organization ##LIST

class getOrganizations(GQLQuery):
   type: Organization ##LIST

class getOrganizationBySlugifiedName(GQLQuery):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      slugifiedName: str

   _args: OrganizationArgs


   type: Organization

class getOrganizationById(GQLQuery):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      orgId: ID ##NON NULL

   _args: OrganizationArgs


   type: Organization

class getEmailDomainAndCheckIfIgnored(GQLQuery):
   type: CorporateDomain

class getOrganizationsWithTheSameEmail(GQLQuery):
   type: CorporateDomainOrganization ##LIST

class searchOrganizations(GQLQuery):
   class EntityArgs(GQLArgsSet, GQLObject): 
      term: str
      limit: int

   _args: EntityArgs


   type: Entity ##LIST

class validateResetPasswordToken(GQLQuery):
   class ValidateTokenResponseArgs(GQLArgsSet, GQLObject): 
      token: str ##NON NULL

   _args: ValidateTokenResponseArgs


   type: ValidateTokenResponse

class getProjectAllowedAPIs(GQLQuery):
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject): 
      mashapeId: str ##NON NULL
      projectId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: ProjectAllowedAPIArgs


   type: ProjectAllowedAPI ##LIST

class requestLogsByEntity(GQLQuery):
   class RequestLogsResultArgs(GQLArgsSet, GQLObject): 
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

   _args: RequestLogsResultArgs


   type: RequestLogsResult

class getAccessControlRoles(GQLQuery):
   class RoleArgs(GQLArgsSet, GQLObject): 
      roleLevels: RoleLevel ##LIST

   _args: RoleArgs


   type: Role ##LIST

class getRoles(GQLQuery):
   class RoleArgs(GQLArgsSet, GQLObject): 
      roleLevels: RoleLevel ##LIST

   _args: RoleArgs


   type: Role ##LIST

class roles(GQLQuery):
   class RoleConnectionArgs(GQLArgsSet, GQLObject): 
      where: RoleWhereInput ##NON NULL
      orderBy: RoleOrderByInput
      pagination: PaginationInput

   _args: RoleConnectionArgs


   type: RoleConnection ##NON NULL

class searchApis(GQLQuery):
   class SearchApiConnectionArgs(GQLArgsSet, GQLObject): 
      where: SearchApiWhereInput ##NON NULL
      orderBy: SearchApiOrderByInput
      pagination: PaginationInput

   _args: SearchApiConnectionArgs


   type: SearchApiConnection ##NON NULL

class searchBlogPosts(GQLQuery):
   class SearchBlogPostConnectionArgs(GQLArgsSet, GQLObject): 
      where: SearchBlogPostWhereInput ##NON NULL
      pagination: PaginationInput

   _args: SearchBlogPostConnectionArgs


   type: SearchBlogPostConnection

class searchCollections(GQLQuery):
   class SearchCollectionConnectionArgs(GQLArgsSet, GQLObject): 
      where: SearchCollectionWhereInput
      orderBy: SearchCollectionOrderByInput
      pagination: PaginationInput

   _args: SearchCollectionConnectionArgs


   type: SearchCollectionConnection

class spotlights(GQLQuery):
   class SpotlightConnectionArgs(GQLArgsSet, GQLObject): 
      where: SpotlightWhereInput ##NON NULL
      orderBy: SpotlightOrderByInput
      pagination: PaginationInput

   _args: SpotlightConnectionArgs


   type: SpotlightConnection ##NON NULL

class searchSubscribedEntityByApiIdAndAppName(GQLQuery):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      appName: str ##NON NULL
      apiId: str ##NON NULL

   _args: ProjectArgs


   type: Project ##LIST

class activeSubscriptionsCount(GQLQuery):
   class ActiveSubscriptionCountArgs(GQLArgsSet, GQLObject): 
      apiId: str
      fromDate: str
      toDate: str
      resolution: Resolution

   _args: ActiveSubscriptionCountArgs


   type: ActiveSubscriptionCount ##LIST

class getInternalSubscriptions(GQLQuery):
   type: BillingSubscription ##LIST

class searchSubscribedEntityByApiId(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      userName: str ##NON NULL
      apiId: str ##NON NULL

   _args: AnyArgs


   type: Any ##LIST

class getSubscriptions(GQLQuery):
   class SubscriptionsPagingArgs(GQLArgsSet, GQLObject): 
      id: int
      userId: int
      apiId: str
      mashapeId: str
      pagingArgs: PagingArgs

   _args: SubscriptionsPagingArgs


   type: SubscriptionsPaging

class getOrganizationSubscriptions(GQLQuery):
   class OrgSubscriptionsArgs(GQLArgsSet, GQLObject): 
      pagingArgs: PagingArgs

   _args: OrgSubscriptionsArgs


   type: OrgSubscriptions

class subscriptions(GQLQuery):
   class SubscriptionConnectionArgs(GQLArgsSet, GQLObject): 
      where: SubscriptionsWhereInput
      pagination: PaginationInput

   _args: SubscriptionConnectionArgs


   type: SubscriptionConnection

class subscription(GQLQuery):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      id: int

   _args: BillingSubscriptionArgs


   type: BillingSubscription

class subscriptionsCount(GQLQuery):
   class SubscriptionsCountArgs(GQLArgsSet, GQLObject): 
      where: SubscriptionsCountWhereInput

   _args: SubscriptionsCountArgs


   type: SubscriptionsCount ##LIST

class getTagsList(GQLQuery):
   type: TagDefinition ##LIST

class tagDefinitions(GQLQuery):
   type: TagDefinitionConnection

class paginatedTeamUsersByOrganizationId(GQLQuery):
   class PaginatedTeamUsersArgs(GQLArgsSet, GQLObject): 
      orgId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: PaginatedTeamUsersArgs


   type: PaginatedTeamUsers

class paginatedTeamUsersByOrganizationIdV2(GQLQuery):
   class PaginatedTeamUsersArgs(GQLArgsSet, GQLObject): 
      orgId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: PaginatedTeamUsersArgs


   type: PaginatedTeamUsers

class teamUserByEmailAndOrgId(GQLQuery):
   class TeamUserArgs(GQLArgsSet, GQLObject): 
      email: str
      orgId: int

   _args: TeamUserArgs


   type: TeamUser

class teamUser(GQLQuery):
   class TeamUserArgs(GQLArgsSet, GQLObject): 
      where: TeamUserWhereInput ##NON NULL

   _args: TeamUserArgs


   type: TeamUser

class findUsersInOrganization(GQLQuery):
   class TeamUserArgs(GQLArgsSet, GQLObject): 
      orgId: int
      term: str

   _args: TeamUserArgs


   type: TeamUser ##LIST

class teamByTeamId(GQLQuery):
   class TeamArgs(GQLArgsSet, GQLObject): 
      teamId: int
      orgId: int

   _args: TeamArgs


   type: Team

class teamsByOrganizationId(GQLQuery):
   class TeamArgs(GQLArgsSet, GQLObject): 
      orgId: int

   _args: TeamArgs


   type: Team ##LIST

class getTeamBySlugifiedName(GQLQuery):
   class TeamArgs(GQLArgsSet, GQLObject): 
      slugifiedName: str

   _args: TeamArgs


   type: Team

class searchTeams(GQLQuery):
   class TeamArgs(GQLArgsSet, GQLObject): 
      term: str
      limit: int

   _args: TeamArgs


   type: Team ##LIST

class team(GQLQuery):
   class TeamArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: TeamArgs


   type: Team

class teams(GQLQuery):
   class TeamArgs(GQLArgsSet, GQLObject): 
      where: TeamWhereInput

   _args: TeamArgs


   type: Team ##LIST

class tenant(GQLQuery):
   type: Tenant

class transactions(GQLQuery):
   class TransactionConnectionArgs(GQLArgsSet, GQLObject): 
      where: TransactionsWhereInput
      pagination: PaginationInput

   _args: TransactionConnectionArgs


   type: TransactionConnection

class transactionsSummary(GQLQuery):
   class TransactionsSummaryArgs(GQLArgsSet, GQLObject): 
      where: TransactionsSummaryWhereInput

   _args: TransactionsSummaryArgs


   type: TransactionsSummary

class transformations(GQLQuery):
   class TransformationConnectionArgs(GQLArgsSet, GQLObject): 
      where: TransformationWhereInput
      orderBy: TransformationOrderByInput
      pagination: PaginationInput

   _args: TransformationConnectionArgs


   type: TransformationConnection ##NON NULL

class tutorials(GQLQuery):
   class TutorialConnectionArgs(GQLArgsSet, GQLObject): 
      where: TutorialWhereInput ##NON NULL
      orderBy: TutorialOrderByInput
      pagination: PaginationInput

   _args: TutorialConnectionArgs


   type: TutorialConnection

class getPhoneNumbers(GQLQuery):
   type: Phone ##LIST

class getRecoveryCodes(GQLQuery):
   type: RecoveryCode ##LIST

class isTwoFactorEnabledByType(GQLQuery):
   class boolArgs(GQLArgsSet, GQLObject): 
      type: str ##NON NULL

   _args: boolArgs


   type: bool

class getUsagesAndParentUsageForSubscription(GQLQuery):
   class UsagesStatsArgs(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: str ##LIST
      resolution: str
      orderDir: str
      periods: str ##LIST
      parentId: int
      isInternal: bool

   _args: UsagesStatsArgs


   type: UsagesStats ##LIST

class getUsagesAgrregatedByTeamsForSubscription(GQLQuery):
   class UsagesStatsArgs(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: str ##LIST
      resolution: str
      orderDir: str
      periods: str ##LIST
      apiVersionId: str
      internalData: str ##LIST

   _args: UsagesStatsArgs


   type: UsagesStats ##LIST

class getUsagesAndParentUsageForSubscriptionByBuckets(GQLQuery):
   class UsagesStatsArgs(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: str ##LIST
      resolution: str
      periods: str ##LIST
      parentId: int

   _args: UsagesStatsArgs


   type: UsagesStats ##LIST

class getUsagesAgrregatedByTeamsForSubscriptionByBuckets(GQLQuery):
   class UsagesStatsArgs(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: str ##LIST
      resolution: str
      periods: str ##LIST
      apiVersionId: str

   _args: UsagesStatsArgs


   type: UsagesStats ##LIST

class organizationQuotaUsageByApiIdV2(GQLQuery):
   class OrganizationApiUsagesV2Args(GQLArgsSet, GQLObject): 
      apiId: ID
      apiVersionId: ID
      internalData: Any

   _args: OrganizationApiUsagesV2Args


   type: OrganizationApiUsagesV2

class getUserInviteByToken(GQLQuery):
   class UserInviteArgs(GQLArgsSet, GQLObject): 
      token: str ##NON NULL

   _args: UserInviteArgs


   type: UserInvite

class checkUserInvitesBranding(GQLQuery):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: UserInvitesBrandingInput

   _args: boolArgs


   type: bool

class checkIfEmailsAlreadyInvited(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      orgId: ID ##NON NULL
      emails: str ##NON NULL ##LIST

   _args: AnyArgs


   type: Any

class searchUsersToInvite(GQLQuery):
   class InviteUsersSearchArgs(GQLArgsSet, GQLObject): 
      orgId: ID ##NON NULL
      brand: str
      term: str
      offset: int
      limit: int

   _args: InviteUsersSearchArgs


   type: InviteUsersSearch ##LIST

class getUserSavedApis(GQLQuery):
   class UserSavedApiArgs(GQLArgsSet, GQLObject): 
      userCollectionId: str

   _args: UserSavedApiArgs


   type: UserSavedApi ##NON NULL

class userById(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      id: int

   _args: UserArgs


   type: User

class userByUsername(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      username: str
      includeUserAttributes: bool

   _args: UserArgs


   type: User

class getPrivateApisJwt(GQLQuery):
   type: str

class searchUsers(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      brand: str
      term: str
      offset: int
      limit: int

   _args: UserArgs


   type: User ##LIST

class searchUsersV2(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      where: SearchUsersWhereInput ##NON NULL

   _args: UserArgs


   type: User ##NON NULL

class user(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: UserArgs


   type: User

class users(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      where: UserWhereInput ##NON NULL

   _args: UserArgs


   type: User ##LIST

class getVirtualPermissions(GQLQuery):
   class PermissionArgs(GQLArgsSet, GQLObject): 
      permissionLevel: RoleLevel ##LIST

   _args: PermissionArgs


   type: Permission ##LIST

class virtualPermissions(GQLQuery):
   class VirtualPermissionArgs(GQLArgsSet, GQLObject): 
      where: VirtualPermissionWhereInput ##NON NULL

   _args: VirtualPermissionArgs


   type: VirtualPermission ##LIST

class getWorkflowsForProvider(GQLQuery):
   class WorkFlowsResponseArgs(GQLArgsSet, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: WorkFlowsResponseArgs


   type: WorkFlowsResponse

class getWorkflowsForDeveloper(GQLQuery):
   class WorkFlowsResponseArgs(GQLArgsSet, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: WorkFlowsResponseArgs


   type: WorkFlowsResponse

class getWorkflowsByRequestor(GQLQuery):
   class WorkFlowsResponseArgs(GQLArgsSet, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: WorkFlowsResponseArgs


   type: WorkFlowsResponse

class getWorkflowsByRequestee(GQLQuery):
   class WorkFlowsResponseArgs(GQLArgsSet, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: WorkFlowsResponseArgs


   type: WorkFlowsResponse

class canWorkflowBeSubmitted(GQLQuery):
   class boolArgs(GQLArgsSet, GQLObject): 
      options: CanWorkflowBeSubmittedOptions

   _args: boolArgs


   type: bool

class getWorkflowAudits(GQLQuery):
   class WorkFlowAuditsResponseArgs(GQLArgsSet, GQLObject): 
      workflowId: int

   _args: WorkFlowAuditsResponseArgs


   type: WorkFlowAuditsResponse

class getWorkflowsCount(GQLQuery):
   class intArgs(GQLArgsSet, GQLObject): 
      options: GetWorkflowCountOptions

   _args: intArgs


   type: int

class exclusions(GQLQuery):
   class ExclusionArgs(GQLArgsSet, GQLObject): 
      client: str
      page: str

   _args: ExclusionArgs


   type: Exclusion ##LIST


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
