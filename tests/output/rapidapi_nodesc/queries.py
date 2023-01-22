from typing import List
from pygqlmap import GQLQuery
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

NonNull_EnvConfigTerm = EnvConfigTerm

NonNull_UserAlertsWhereInput = UserAlertsWhereInput

NonNull_ApiFollowerWhereInput = ApiFollowerWhereInput

NonNull_AppAuthorizationsWhereInput = AppAuthorizationsWhereInput

NonNull_AssetWhereInput = AssetWhereInput

NonNull_AsyncApiConfigurationWhereInput = AsyncApiConfigurationWhereInput

NonNull_AuditWhereInput = AuditWhereInput

NonNull_BillingItemsWhereInput = BillingItemsWhereInput

NonNull_ConsumersWhereInput = ConsumersWhereInput

NonNull_ContactAdminSubscribeToAPIEvent = ContactAdminSubscribeToAPIEvent

NonNull_endpointsWithinDateInput = endpointsWithinDateInput

NonNull_EndpointWhereInput = EndpointWhereInput

NonNull_EntityMetadataWhereInput = EntityMetadataWhereInput

NonNull_EntityRoleWhereInput = EntityRoleWhereInput

NonNull_GetLegalAgreementSigningURLInput = GetLegalAgreementSigningURLInput

NonNull_MessagesWhereInput = MessagesWhereInput

NonNull_RoleWhereInput = RoleWhereInput

NonNull_SearchApiWhereInput = SearchApiWhereInput

NonNull_SearchBlogPostWhereInput = SearchBlogPostWhereInput

NonNull_SpotlightWhereInput = SpotlightWhereInput

NonNull_TeamUserWhereInput = TeamUserWhereInput

NonNull_TutorialWhereInput = TutorialWhereInput

NonNull_SearchUsersWhereInput = SearchUsersWhereInput

NonNull_UserWhereInput = UserWhereInput

NonNull_VirtualPermissionWhereInput = VirtualPermissionWhereInput

class ping(GQLQuery):
   type: str

class eventUrls(GQLQuery):
   class EventUrlConnectionArgs(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: EventUrlWhereInput
      order: EventUrlSortablesInput

   _args: EventUrlConnectionArgs


   type: EventUrlConnection

class eventUrl(GQLQuery):
   class EventUrlArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: EventUrlArgs


   type: EventUrl

class eventTypes(GQLQuery):
   type: EventType

class eventConfig(GQLQuery):
   type: EventConfig

class gatewayInstances(GQLQuery):
   class GatewayInstanceConnectionArgs(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: GatewayInstanceWhereInput
      order: GatewayInstanceSortingInput

   _args: GatewayInstanceConnectionArgs


   type: GatewayInstanceConnection

class gatewayInstance(GQLQuery):
   class GatewayInstanceArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: GatewayInstanceArgs


   type: GatewayInstance

class gatewayTemplates(GQLQuery):
   class GatewayTemplateConnectionArgs(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: GatewayTemplateWhereInput
      order: GatewayTemplateSortingInput

   _args: GatewayTemplateConnectionArgs


   type: GatewayTemplateConnection

class gatewayTemplate(GQLQuery):
   class GwTemplateArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: GwTemplateArgs


   type: GwTemplate

class gatewayTemplatesParams(GQLQuery):
   class GatewayTemplateParamConnectionArgs(GQLArgsSet, GQLObject): 
      pagination: PaginationArgs
      where: GatewayTemplateParamsWhereInput
      order: GatewayTemplateParamSortingInput

   _args: GatewayTemplateParamConnectionArgs


   type: GatewayTemplateParamConnection

class gatewayTemplateParam(GQLQuery):
   class GatewayTemplateParamArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: GatewayTemplateParamArgs


   type: GatewayTemplateParam

class envConfigCategories(GQLQuery):
   type: EnvConfigCategory

class envConfig(GQLQuery):
   class EnvConfigArgs(GQLArgsSet, GQLObject): 
      id: NonNull_int

   _args: EnvConfigArgs


   type: EnvConfig

class envConfigs(GQLQuery):
   class EnvConfigArgs(GQLArgsSet, GQLObject): 
      envConfigTerm: NonNull_EnvConfigTerm

   _args: EnvConfigArgs


   type: EnvConfig

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


   type: List[Extension]

class getSEOTagsByURL(GQLQuery):
   class SEOArgs(GQLArgsSet, GQLObject): 
      url: str

   _args: SEOArgs


   type: SEO

class getUserAlertById(GQLQuery):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: UserAlertArgs


   type: UserAlert

class getUserAlertsByScope(GQLQuery):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      scope: NonNull_ID

   _args: UserAlertArgs


   type: List[UserAlert]

class getAlertsDefinitions(GQLQuery):
   type: AlertDefinition

class userAlerts(GQLQuery):
   class UserAlertsConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_UserAlertsWhereInput

   _args: UserAlertsConnectionArgs


   type: UserAlertsConnection

class userAlert(GQLQuery):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: UserAlertArgs


   type: UserAlert

class allowedPlanDeveloperByPlanId(GQLQuery):
   class AllowedPlanDeveloperArgs(GQLArgsSet, GQLObject): 
      planId: str

   _args: AllowedPlanDeveloperArgs


   type: List[AllowedPlanDeveloper]

class apiCertificate(GQLQuery):
   class ApiCertificateArgs(GQLArgsSet, GQLObject): 
      apiCertificateId: NonNull_ID

   _args: ApiCertificateArgs


   type: ApiCertificate

class apiCertificates(GQLQuery):
   class ApiCertificateConnectionArgs(GQLArgsSet, GQLObject): 
      where: ApiCertificateWhereInput
      orderBy: ApiCertificateOrderByInput
      pagination: PaginationInput

   _args: ApiCertificateConnectionArgs


   type: ApiCertificateConnection

class apiDevelopersByApiId(GQLQuery):
   class ApiDeveloperArgs(GQLArgsSet, GQLObject): 
      apiId: str
      pagingArgs: PagingArgs

   _args: ApiDeveloperArgs


   type: ApiDeveloper

class apiFollowers(GQLQuery):
   class ApiFollowerConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_ApiFollowerWhereInput
      orderBy: ApiFollowerOrderByInput
      pagination: PaginationInput

   _args: ApiFollowerConnectionArgs


   type: ApiFollowerConnection

class apiReferenceByApiAndVersionId(GQLQuery):
   class ApiReferenceArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_str
      versionId: NonNull_str

   _args: ApiReferenceArgs


   type: ApiReference

class apiReferences(GQLQuery):
   class ApiReferenceConnectionArgs(GQLArgsSet, GQLObject): 
      where: ApiReferenceWhereInput

   _args: ApiReferenceConnectionArgs


   type: ApiReferenceConnection

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
      trackingIds: NonNull_List[NonNull_ID]

   _args: ApiSpecImportProcessArgs


   type: ApiSpecImportProcess

class bulkApisSummaryByTrackingIds(GQLQuery):
   class BatchTrackingIdsSummaryArgs(GQLArgsSet, GQLObject): 
      trackingIds: NonNull_List[ID]

   _args: BatchTrackingIdsSummaryArgs


   type: BatchTrackingIdsSummary

class calculatedStatistics(GQLQuery):
   class CalculatedStatisticsArgs(GQLArgsSet, GQLObject): 
      fromDate: NonNull_str
      toDate: NonNull_str
      resolution: str
      projectIds: List[str]
      apiIds: List[str]
      endpoints: List[str]
      groupBy: StatsGroupBy
      apiVersionIds: List[ID]
      entityId: ID
      timeOffset: int
      filters: List[StatsFilterBy]

   _args: CalculatedStatisticsArgs


   type: CalculatedStatistics

class getApiVersion(GQLQuery):
   class ApiVersionArgs(GQLArgsSet, GQLObject): 
      versionId: NonNull_ID

   _args: ApiVersionArgs


   type: ApiVersion

class apiVersion(GQLQuery):
   class ApiVersionArgs(GQLArgsSet, GQLObject): 
      apiVersionId: NonNull_ID

   _args: ApiVersionArgs


   type: ApiVersion

class apiVersions(GQLQuery):
   class ApiVersionConnectionArgs(GQLArgsSet, GQLObject): 
      where: ApiVersionWhereInput
      orderBy: ApiVersionOrderByInput
      pagination: PaginationInput

   _args: ApiVersionConnectionArgs


   type: ApiVersionConnection

class api(GQLQuery):
   class ApiArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: ApiArgs


   type: Api

class apis(GQLQuery):
   class ApiConnectionArgs(GQLArgsSet, GQLObject): 
      where: ApiWhereInput
      orderBy: ApiOrderByInput
      pagination: PaginationInput

   _args: ApiConnectionArgs


   type: ApiConnection

class exportOpenApi(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_ID
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
      id: NonNull_ID

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization

class applicationAuthorizations(GQLQuery):
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject): 
      where: NonNull_AppAuthorizationsWhereInput

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization

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
      id: NonNull_ID

   _args: AssetArgs


   type: Asset

class assets(GQLQuery):
   class AssetArgs(GQLArgsSet, GQLObject): 
      where: NonNull_AssetWhereInput

   _args: AssetArgs


   type: Asset

class assetsDownloadUrls(GQLQuery):
   class AssetForDownloadArgs(GQLArgsSet, GQLObject): 
      where: NonNull_AssetWhereInput

   _args: AssetForDownloadArgs


   type: AssetForDownload

class asyncApiConfigurations(GQLQuery):
   class AsyncApiConfigurationConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_AsyncApiConfigurationWhereInput

   _args: AsyncApiConfigurationConnectionArgs


   type: AsyncApiConfigurationConnection

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
      where: NonNull_AuditWhereInput

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
   type: List[authStrategy]

class getBillingFeaturesByApiVersionId(GQLQuery):
   class BillingFeatureArgs(GQLArgsSet, GQLObject): 
      versionId: str

   _args: BillingFeatureArgs


   type: List[BillingFeature]

class getBillingFeaturesByApiId(GQLQuery):
   class BillingFeatureArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_str

   _args: BillingFeatureArgs


   type: List[BillingFeature]

class isMonetizationEnabled(GQLQuery):
   type: bool

class billingItems(GQLQuery):
   class BillingItemConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_BillingItemsWhereInput

   _args: BillingItemConnectionArgs


   type: BillingItemConnection

class getFreeSeatsObj(GQLQuery):
   class SeatsBillingInformationArgs(GQLArgsSet, GQLObject): 
      orgId: NonNull_ID

   _args: SeatsBillingInformationArgs


   type: SeatsBillingInformation

class getBillingPlanVersionsByApiId(GQLQuery):
   class BillingPlanVersionsResponseArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_str
      apiVersionId: str
      pagingArgs: PagingArgsBilling
      filters: BillingPlanVersionFilters

   _args: BillingPlanVersionsResponseArgs


   type: BillingPlanVersionsResponse

class getBillingPlanVersionById(GQLQuery):
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject): 
      billingPlanVersionId: NonNull_str

   _args: BillingPlanVersionArgs


   type: BillingPlanVersion

class billingPlanVersion(GQLQuery):
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

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
      fromDate: NonNull_str
      toDate: NonNull_str
      resolution: str
      endpointsAndApiVersions: NonNull_List[endpointsAndApiVersionCouples]
      groupBy: StatsGroupBy
      apiId: NonNull_str
      entityId: ID
      timeOffset: int
      filters: List[StatsFilterBy]

   _args: CalculatedStatisticsArgs


   type: CalculatedStatistics

class categoriesV2(GQLQuery):
   class CategoryConnectionArgs(GQLArgsSet, GQLObject): 
      where: CategoryWhereInput
      orderBy: CategoryOrderByInput
      pagination: PaginationInput

   _args: CategoryConnectionArgs


   type: CategoryConnection

class categoryEntities(GQLQuery):
   class CategoryEntityArgs(GQLArgsSet, GQLObject): 
      lang: str
      pagingArgs: PagingArgs

   _args: CategoryEntityArgs


   type: List[CategoryEntity]

class categories(GQLQuery):
   class CategoryArgs(GQLArgsSet, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection

   _args: CategoryArgs


   type: List[Category]

class collectionsItemsByIds(GQLQuery):
   class CollectionItemArgs(GQLArgsSet, GQLObject): 
      ids: NonNull_List[ID]

   _args: CollectionItemArgs


   type: List[CollectionItem]

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
      collectionId: NonNull_ID

   _args: CollectionArgs


   type: Collection

class collection(GQLQuery):
   class CollectionArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: CollectionArgs


   type: Collection

class collapsedCollections(GQLQuery):
   class CollapsedCollectionArgs(GQLArgsSet, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection
      limit: int
      page: int

   _args: CollapsedCollectionArgs


   type: List[CollapsedCollection]

class collectionBySlugifiedKey(GQLQuery):
   class CollectionArgs(GQLArgsSet, GQLObject): 
      slugifiedKey: str

   _args: CollectionArgs


   type: Collection

class getPrivateCollections(GQLQuery):
   type: List[Collection]

class getPrivateCollectionsV2(GQLQuery):
   type: List[Collection]

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
      issueId: NonNull_int
      pagingArgs: PagingArgs

   _args: PaginatedCommentsArgs


   type: PaginatedComments

class getCommentByIdV2(GQLQuery):
   class CommentArgs(GQLArgsSet, GQLObject): 
      issueId: NonNull_int
      commentId: NonNull_int

   _args: CommentArgs


   type: Comment

class search(GQLQuery):
   class ApiSearchArgs(GQLArgsSet, GQLObject): 
      term: NonNull_str

   _args: ApiSearchArgs


   type: ApiSearch

class searchEntityByApiId(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      userName: NonNull_str
      apiId: NonNull_str
      distinct: str

   _args: AnyArgs


   type: List[Any]

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


   type: List[FollowUser]

class apiById(GQLQuery):
   class ApiArgs(GQLArgsSet, GQLObject): 
      apiId: str

   _args: ApiArgs


   type: Api

class apisById(GQLQuery):
   class ApiArgs(GQLArgsSet, GQLObject): 
      ids: NonNull_List[ID]

   _args: ApiArgs


   type: List[Api]

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


   type: List[Follower]

class calculateSeatsPrice(GQLQuery):
   class floatArgs(GQLArgsSet, GQLObject): 
      seats: NonNull_int

   _args: floatArgs


   type: float

class getSeatsTransactionsByOrgId(GQLQuery):
   class OrgTransactionArgs(GQLArgsSet, GQLObject): 
      orgId: NonNull_int

   _args: OrgTransactionArgs


   type: List[OrgTransaction]

class organizationsTreeToken(GQLQuery):
   type: str

class getMinimumSeats(GQLQuery):
   type: int

class transactionsById(GQLQuery):
   class TransactionsPagingArgs(GQLArgsSet, GQLObject): 
      apiId: str
      userId: int
      type: str
      pagingArgs: PagingArgs
      queryFilters: QueryFilters
      paymentStatusFilters: List[TransactionPaymentStatus]

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
      userId: List[int]
      offset: int
      limit: int
      sort: str
      usernames: str
      plansFilter: List[str]
      lastActive: List[str]

   _args: ConsumersArgs


   type: Consumers

class getFreeConsumers(GQLQuery):
   class ConsumersArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_List[NonNull_ID]
      offset: int
      limit: int
      order: str
      lastActive: List[str]
      username: List[str]
      userId: List[int]

   _args: ConsumersArgs


   type: Consumers

class consumers(GQLQuery):
   class ConsumerConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_ConsumersWhereInput

   _args: ConsumerConnectionArgs


   type: ConsumerConnection

class requestAdminToSubscribeToAnAPI(GQLQuery):
   class boolArgs(GQLArgsSet, GQLObject): 
      eventData: NonNull_ContactAdminSubscribeToAPIEvent

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
      apiIds: List[str]

   _args: DiscussionObjectArgs


   type: DiscussionObject

class getIssuesByApiIdV2(GQLQuery):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_str
      pagingArgs: PagingArgs
      providerId: str

   _args: IssueObjectArgs


   type: IssueObject

class getIssuesByApiIdsV2(GQLQuery):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      apiIds: List[NonNull_str]
      pagingArgs: PagingArgs

   _args: IssueObjectArgs


   type: IssueObject

class endpointStats(GQLQuery):
   class EndpointStatsArgs(GQLArgsSet, GQLObject): 
      apiIds: NonNull_List[ID]
      projectIds: List[ID]
      endpointIds: List[ID]
      fromDate: str
      toDate: str
      resolution: str

   _args: EndpointStatsArgs


   type: List[EndpointStats]

class endpointStatsByEntity(GQLQuery):
   class EndpointStatsArgs(GQLArgsSet, GQLObject): 
      entityId: ID
      apiId: NonNull_ID
      endpointIds: List[ID]
      fromDate: DateTime
      toDate: DateTime
      resolution: Resolution
      timeOffset: int
      filters: List[StatsFilterBy]

   _args: EndpointStatsArgs


   type: List[EndpointStats]

class endpointStatsByEntityV2(GQLQuery):
   class VersionEndpointStatsArgs(GQLArgsSet, GQLObject): 
      entityId: ID
      apiId: NonNull_ID
      endpointsAndApiVersions: List[EndpointAndVersion]
      fromDate: DateTime
      toDate: DateTime
      resolution: Resolution
      timeOffset: int
      filters: List[StatsFilterBy]

   _args: VersionEndpointStatsArgs


   type: List[VersionEndpointStats]

class getEndpointsWithinDateByParameters(GQLQuery):
   class EndpointStatsArgs(GQLArgsSet, GQLObject): 
      input: NonNull_endpointsWithinDateInput
      showDeleted: bool

   _args: EndpointStatsArgs


   type: List[EndpointStats]

class endpoint(GQLQuery):
   class EndpointArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: EndpointArgs


   type: Endpoint

class endpoints(GQLQuery):
   class EndpointConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_EndpointWhereInput

   _args: EndpointConnectionArgs


   type: EndpointConnection

class searchEntities(GQLQuery):
   class EntityArgs(GQLArgsSet, GQLObject): 
      term: str
      limit: int
      status: str
      type: str

   _args: EntityArgs


   type: List[Entity]

class entitiesMetadata(GQLQuery):
   class EntityMetadataConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_EntityMetadataWhereInput
      orderBy: EntityMetadataOrderByInput
      pagination: PaginationInput

   _args: EntityMetadataConnectionArgs


   type: EntityMetadataConnection

class getEntitiesRoles(GQLQuery):
   class EntityRoleArgs(GQLArgsSet, GQLObject): 
      entityIds: List[int]
      orgId: int
      parentIds: List[int]

   _args: EntityRoleArgs


   type: List[EntityRole]

class entitiesRoles(GQLQuery):
   class EntityRoleConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_EntityRoleWhereInput
      orderBy: EntityRoleOrderByInput
      pagination: PaginationInput

   _args: EntityRoleConnectionArgs


   type: EntityRoleConnection

class getLogsCSV(GQLQuery):
   class LogsCSVArgs(GQLArgsSet, GQLObject): 
      apiId: ID
      projectId: ID

   _args: LogsCSVArgs


   type: List[LogsCSV]

class exportLogsCSVProvider(GQLQuery):
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
   type: GatewayConnection

class getGateways(GQLQuery):
   type: List[Gateway]

class getGatewayConfiguration(GQLQuery):
   class ApiGatewayConfigurationArgs(GQLArgsSet, GQLObject): 
      id: NonNull_int

   _args: ApiGatewayConfigurationArgs


   type: ApiGatewayConfiguration

class graphQlIntrospectionSchema(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      introspectionCallUrl: NonNull_str

   _args: AnyArgs


   type: Any

class headlinesByApiNameAndOwnerId(GQLQuery):
   class HeadlineArgs(GQLArgsSet, GQLObject): 
      apiName: str
      apiOwnerId: str
      size: int

   _args: HeadlineArgs


   type: List[Headline]

class getIssuesByOrganizatonId(GQLQuery):
   class IssueObjectArgs(GQLArgsSet, GQLObject): 
      id: NonNull_str
      pagingArgs: PagingArgs

   _args: IssueObjectArgs


   type: IssueObject

class getResponseTimeByProviderId(GQLQuery):
   class floatArgs(GQLArgsSet, GQLObject): 
      providerId: NonNull_int

   _args: floatArgs


   type: float

class getAverageResponseTime(GQLQuery):
   type: float

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


   type: List[IssueFollow]

class kafkaConfiguration(GQLQuery):
   class KafkaConfigurationArgs(GQLArgsSet, GQLObject): 
      apiVersionId: NonNull_str

   _args: KafkaConfigurationArgs


   type: KafkaConfiguration

class kafkaTopics(GQLQuery):
   class KafkaTopicsArgs(GQLArgsSet, GQLObject): 
      apiVersionId: NonNull_str

   _args: KafkaTopicsArgs


   type: KafkaTopics

class kafkaSchemas(GQLQuery):
   class KafkaSchemasArgs(GQLArgsSet, GQLObject): 
      apiVersionId: NonNull_str

   _args: KafkaSchemasArgs


   type: KafkaSchemas

class kafkaTopicMetadata(GQLQuery):
   class TopicMetadataResponseArgs(GQLArgsSet, GQLObject): 
      apiVersionId: NonNull_str
      topicName: NonNull_str

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
      input: NonNull_GetLegalAgreementSigningURLInput

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
      where: NonNull_MessagesWhereInput

   _args: MessageArgs


   type: List[Message]

class getApiAverageResponseTime(GQLQuery):
   class floatArgs(GQLArgsSet, GQLObject): 
      apiId: NonNull_str

   _args: floatArgs


   type: float

class getProviderAverageResponseTime(GQLQuery):
   class floatArgs(GQLArgsSet, GQLObject): 
      providerId: NonNull_int

   _args: floatArgs


   type: float

class getRelativeAverageResponseTime(GQLQuery):
   class RelativeARTResponseArgs(GQLArgsSet, GQLObject): 
      providerId: NonNull_int

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


   type: List[NewNotification]

class notificationsByUserId(GQLQuery):
   class NotificationArgs(GQLArgsSet, GQLObject): 
      userId: int
      limit: int
      offset: int

   _args: NotificationArgs


   type: List[Notification]

class organization(GQLQuery):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: OrganizationArgs


   type: Organization

class organizations(GQLQuery):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      where: OrganizationWhereInput

   _args: OrganizationArgs


   type: List[Organization]

class getOrganizations(GQLQuery):
   type: List[Organization]

class getOrganizationBySlugifiedName(GQLQuery):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      slugifiedName: str

   _args: OrganizationArgs


   type: Organization

class getOrganizationById(GQLQuery):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      orgId: NonNull_ID

   _args: OrganizationArgs


   type: Organization

class getEmailDomainAndCheckIfIgnored(GQLQuery):
   type: CorporateDomain

class getOrganizationsWithTheSameEmail(GQLQuery):
   type: List[CorporateDomainOrganization]

class searchOrganizations(GQLQuery):
   class EntityArgs(GQLArgsSet, GQLObject): 
      term: str
      limit: int

   _args: EntityArgs


   type: List[Entity]

class validateResetPasswordToken(GQLQuery):
   class ValidateTokenResponseArgs(GQLArgsSet, GQLObject): 
      token: NonNull_str

   _args: ValidateTokenResponseArgs


   type: ValidateTokenResponse

class getProjectAllowedAPIs(GQLQuery):
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject): 
      mashapeId: NonNull_str
      projectId: NonNull_int
      pagingArgs: PagingArgs

   _args: ProjectAllowedAPIArgs


   type: List[ProjectAllowedAPI]

class requestLogsByEntity(GQLQuery):
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
   class RoleArgs(GQLArgsSet, GQLObject): 
      roleLevels: List[RoleLevel]

   _args: RoleArgs


   type: List[Role]

class getRoles(GQLQuery):
   class RoleArgs(GQLArgsSet, GQLObject): 
      roleLevels: List[RoleLevel]

   _args: RoleArgs


   type: List[Role]

class roles(GQLQuery):
   class RoleConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_RoleWhereInput
      orderBy: RoleOrderByInput
      pagination: PaginationInput

   _args: RoleConnectionArgs


   type: RoleConnection

class searchApis(GQLQuery):
   class SearchApiConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_SearchApiWhereInput
      orderBy: SearchApiOrderByInput
      pagination: PaginationInput

   _args: SearchApiConnectionArgs


   type: SearchApiConnection

class searchBlogPosts(GQLQuery):
   class SearchBlogPostConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_SearchBlogPostWhereInput
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
      where: NonNull_SpotlightWhereInput
      orderBy: SpotlightOrderByInput
      pagination: PaginationInput

   _args: SpotlightConnectionArgs


   type: SpotlightConnection

class searchSubscribedEntityByApiIdAndAppName(GQLQuery):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      appName: NonNull_str
      apiId: NonNull_str

   _args: ProjectArgs


   type: List[Project]

class activeSubscriptionsCount(GQLQuery):
   class ActiveSubscriptionCountArgs(GQLArgsSet, GQLObject): 
      apiId: str
      fromDate: str
      toDate: str
      resolution: Resolution

   _args: ActiveSubscriptionCountArgs


   type: List[ActiveSubscriptionCount]

class getInternalSubscriptions(GQLQuery):
   type: List[BillingSubscription]

class searchSubscribedEntityByApiId(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      userName: NonNull_str
      apiId: NonNull_str

   _args: AnyArgs


   type: List[Any]

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


   type: List[SubscriptionsCount]

class getTagsList(GQLQuery):
   type: List[TagDefinition]

class tagDefinitions(GQLQuery):
   type: TagDefinitionConnection

class paginatedTeamUsersByOrganizationId(GQLQuery):
   class PaginatedTeamUsersArgs(GQLArgsSet, GQLObject): 
      orgId: NonNull_int
      pagingArgs: PagingArgs

   _args: PaginatedTeamUsersArgs


   type: PaginatedTeamUsers

class paginatedTeamUsersByOrganizationIdV2(GQLQuery):
   class PaginatedTeamUsersArgs(GQLArgsSet, GQLObject): 
      orgId: NonNull_int
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
      where: NonNull_TeamUserWhereInput

   _args: TeamUserArgs


   type: TeamUser

class findUsersInOrganization(GQLQuery):
   class TeamUserArgs(GQLArgsSet, GQLObject): 
      orgId: int
      term: str

   _args: TeamUserArgs


   type: List[TeamUser]

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


   type: List[Team]

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


   type: List[Team]

class team(GQLQuery):
   class TeamArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: TeamArgs


   type: Team

class teams(GQLQuery):
   class TeamArgs(GQLArgsSet, GQLObject): 
      where: TeamWhereInput

   _args: TeamArgs


   type: List[Team]

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


   type: TransformationConnection

class tutorials(GQLQuery):
   class TutorialConnectionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_TutorialWhereInput
      orderBy: TutorialOrderByInput
      pagination: PaginationInput

   _args: TutorialConnectionArgs


   type: TutorialConnection

class getPhoneNumbers(GQLQuery):
   type: List[Phone]

class getRecoveryCodes(GQLQuery):
   type: List[RecoveryCode]

class isTwoFactorEnabledByType(GQLQuery):
   class boolArgs(GQLArgsSet, GQLObject): 
      type: NonNull_str

   _args: boolArgs


   type: bool

class getUsagesAndParentUsageForSubscription(GQLQuery):
   class UsagesStatsArgs(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: List[str]
      resolution: str
      orderDir: str
      periods: List[str]
      parentId: int
      isInternal: bool

   _args: UsagesStatsArgs


   type: List[UsagesStats]

class getUsagesAgrregatedByTeamsForSubscription(GQLQuery):
   class UsagesStatsArgs(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: List[str]
      resolution: str
      orderDir: str
      periods: List[str]
      apiVersionId: str
      internalData: List[str]

   _args: UsagesStatsArgs


   type: List[UsagesStats]

class getUsagesAndParentUsageForSubscriptionByBuckets(GQLQuery):
   class UsagesStatsArgs(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: List[str]
      resolution: str
      periods: List[str]
      parentId: int

   _args: UsagesStatsArgs


   type: List[UsagesStats]

class getUsagesAgrregatedByTeamsForSubscriptionByBuckets(GQLQuery):
   class UsagesStatsArgs(GQLArgsSet, GQLObject): 
      apiId: str
      subscriptionId: str
      billingItemIds: List[str]
      resolution: str
      periods: List[str]
      apiVersionId: str

   _args: UsagesStatsArgs


   type: List[UsagesStats]

class organizationQuotaUsageByApiIdV2(GQLQuery):
   class OrganizationApiUsagesV2Args(GQLArgsSet, GQLObject): 
      apiId: ID
      apiVersionId: ID
      internalData: Any

   _args: OrganizationApiUsagesV2Args


   type: OrganizationApiUsagesV2

class getUserInviteByToken(GQLQuery):
   class UserInviteArgs(GQLArgsSet, GQLObject): 
      token: NonNull_str

   _args: UserInviteArgs


   type: UserInvite

class checkUserInvitesBranding(GQLQuery):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: UserInvitesBrandingInput

   _args: boolArgs


   type: bool

class checkIfEmailsAlreadyInvited(GQLQuery):
   class AnyArgs(GQLArgsSet, GQLObject): 
      orgId: NonNull_ID
      emails: NonNull_List[str]

   _args: AnyArgs


   type: Any

class searchUsersToInvite(GQLQuery):
   class InviteUsersSearchArgs(GQLArgsSet, GQLObject): 
      orgId: NonNull_ID
      brand: str
      term: str
      offset: int
      limit: int

   _args: InviteUsersSearchArgs


   type: List[InviteUsersSearch]

class getUserSavedApis(GQLQuery):
   class UserSavedApiArgs(GQLArgsSet, GQLObject): 
      userCollectionId: str

   _args: UserSavedApiArgs


   type: UserSavedApi

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


   type: List[User]

class searchUsersV2(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      where: NonNull_SearchUsersWhereInput

   _args: UserArgs


   type: User

class user(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: UserArgs


   type: User

class users(GQLQuery):
   class UserArgs(GQLArgsSet, GQLObject): 
      where: NonNull_UserWhereInput

   _args: UserArgs


   type: List[User]

class getVirtualPermissions(GQLQuery):
   class PermissionArgs(GQLArgsSet, GQLObject): 
      permissionLevel: List[RoleLevel]

   _args: PermissionArgs


   type: List[Permission]

class virtualPermissions(GQLQuery):
   class VirtualPermissionArgs(GQLArgsSet, GQLObject): 
      where: NonNull_VirtualPermissionWhereInput

   _args: VirtualPermissionArgs


   type: List[VirtualPermission]

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


   type: List[Exclusion]


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
