from pygqlmap.components import GQLOperationArgs, GQLQuery
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

ping = str

class eventUrls(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      pagination: PaginationArgs
      where: EventUrlWhereInput
      order: EventUrlSortablesInput

   _args: Args


   type: EventUrlConnection ##NON NULL

class eventUrl(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: EventUrl

class eventTypes(GQLQuery):
   type: EventType ##NON NULL

class eventConfig(GQLQuery):
   type: EventConfig

class gatewayInstances(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      pagination: PaginationArgs
      where: GatewayInstanceWhereInput
      order: GatewayInstanceSortingInput

   _args: Args


   type: GatewayInstanceConnection ##NON NULL

class gatewayInstance(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class gatewayTemplates(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      pagination: PaginationArgs
      where: GatewayTemplateWhereInput
      order: GatewayTemplateSortingInput

   _args: Args


   type: GatewayTemplateConnection ##NON NULL

class gatewayTemplate(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class gatewayTemplatesParams(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      pagination: PaginationArgs
      where: GatewayTemplateParamsWhereInput
      order: GatewayTemplateParamSortingInput

   _args: Args


   type: GatewayTemplateParamConnection ##NON NULL

class gatewayTemplateParam(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: GatewayTemplateParam ##NON NULL

class envConfigCategories(GQLQuery):
   type: EnvConfigCategory ##NON NULL

class envConfig(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: int ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class envConfigs(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      envConfigTerm: EnvConfigTerm ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class adminAuditLogs(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: AdminAuditLogInput
      pagination: PaginationArgs
      orderBy: AdminAuditLogSortablesInput

   _args: Args


   type: AdminAuditLogConnection

class eventLogs(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: EventLogInput
      pagination: PaginationArgs
      orderBy: EventLogSortablesInput

   _args: Args


   type: EventLogConnection

extensions = list[Extension]

class getSEOTagsByURL(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      url: str

   _args: Args


   type: SEO

class getUserAlertById(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: UserAlert

getUserAlertsByScope = list[UserAlert]

class getAlertsDefinitions(GQLQuery):
   type: AlertDefinition ##NON NULL

class userAlerts(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: UserAlertsWhereInput ##NON NULL

   _args: Args


   type: UserAlertsConnection ##NON NULL

class userAlert(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: UserAlert

allowedPlanDeveloperByPlanId = list[AllowedPlanDeveloper]

class apiCertificate(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiCertificateId: ID ##NON NULL

   _args: Args


   type: ApiCertificate

class apiCertificates(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: ApiCertificateWhereInput
      orderBy: ApiCertificateOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiCertificateConnection ##NON NULL

class apiDevelopersByApiId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiId: str
      pagingArgs: PagingArgs

   _args: Args


   type: ApiDeveloper ##NON NULL

class apiFollowers(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: ApiFollowerWhereInput ##NON NULL
      orderBy: ApiFollowerOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiFollowerConnection ##NON NULL

class apiReferenceByApiAndVersionId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiId: str ##NON NULL
      versionId: str ##NON NULL

   _args: Args


   type: ApiReference

class apiReferences(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: ApiReferenceWhereInput

   _args: Args


   type: ApiReferenceConnection ##NON NULL

class apiSearch(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      searchArguments: SearchArguments

   _args: Args


   type: ApiSearchPaged

class apiSearchV3(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      searchArguments: SearchArguments

   _args: Args


   type: ApiSearchPaged

class apiSpecImportProgresses(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      trackingIds: list[ID] ##NON NULL

   _args: Args


   type: ApiSpecImportProcess ##NON NULL

class bulkApisSummaryByTrackingIds(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      trackingIds: list[ID] ##NON NULL

   _args: Args


   type: BatchTrackingIdsSummary

class calculatedStatistics(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
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
   class Args(GQLOperationArgs, GQLObject): 
      versionId: ID ##NON NULL

   _args: Args


   type: ApiVersion

class apiVersion(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiVersionId: ID ##NON NULL

   _args: Args


   type: ApiVersion

class apiVersions(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: ApiVersionWhereInput
      orderBy: ApiVersionOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiVersionConnection ##NON NULL

class api(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Api

class apis(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: ApiWhereInput
      orderBy: ApiOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiConnection ##NON NULL

class exportOpenApi(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiId: ID ##NON NULL
      apiVersionId: ID

   _args: Args


   type: Any

class validateSwagger(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      input: validateSwaggerInput

   _args: Args


   type: Any

class applicationAuthorization(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class applicationAuthorizations(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: AppAuthorizationsWhereInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class applicationEnvironmentsKeysByApplicationIdAndEnvironment(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      applicationId: str
      environment: str

   _args: Args


   type: ApplicationEnvironmentPaging

class applicationEnvironmentsByApplicationIdAndEnvironment(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      applicationId: str
      environment: str

   _args: Args


   type: ApplicationEnvironment

class applicationById(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: int

   _args: Args


   type: Application

class asset(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Asset

class assets(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: AssetWhereInput ##NON NULL

   _args: Args


   type: Asset ##NON NULL

class assetsDownloadUrls(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: AssetWhereInput ##NON NULL

   _args: Args


   type: AssetForDownload ##NON NULL

class asyncApiConfigurations(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: AsyncApiConfigurationWhereInput ##NON NULL

   _args: Args


   type: AsyncApiConfigurationConnection ##NON NULL

class userAttributesByUserId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      userId: int

   _args: Args


   type: UserAttributes

class auditByOrganizationId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      searchTerm: str
      from_: int
      orgId: int

   _args: Args


   type: auditTrails

class audit(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: AuditWhereInput ##NON NULL

   _args: Args


   type: auditTrails

class auditLogin(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      from_: int
      userId: str

   _args: Args


   type: auditTrails

class userByEmail(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      email: str

   _args: Args


   type: User

class activeUser(GQLQuery):
   type: User

getAuthStrategies = list[authStrategy]

getBillingFeaturesByApiVersionId = list[BillingFeature]

getBillingFeaturesByApiId = list[BillingFeature]

isMonetizationEnabled = bool

class billingItems(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: BillingItemsWhereInput ##NON NULL

   _args: Args


   type: BillingItemConnection

class getFreeSeatsObj(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      orgId: ID ##NON NULL

   _args: Args


   type: SeatsBillingInformation

class getBillingPlanVersionsByApiId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiId: str ##NON NULL
      apiVersionId: str
      pagingArgs: PagingArgsBilling
      filters: BillingPlanVersionFilters

   _args: Args


   type: BillingPlanVersionsResponse

class getBillingPlanVersionById(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      billingPlanVersionId: str ##NON NULL

   _args: Args


   type: BillingPlanVersion

class billingPlanVersion(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: BillingPlanVersion

class billingPlanVersions(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: BillingPlanVersionWhereInput
      pagination: PaginationInput

   _args: Args


   type: BillingPlanVersionConnection

class calculatedStatisticsByEndpointAndApiversion(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
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
   class Args(GQLOperationArgs, GQLObject): 
      where: CategoryWhereInput
      orderBy: CategoryOrderByInput
      pagination: PaginationInput

   _args: Args


   type: CategoryConnection ##NON NULL

categoryEntities = list[CategoryEntity]

categories = list[Category]

collectionsItemsByIds = list[CollectionItem]

class collections(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: CollectionsWhereInput
      orderBy: CollectionsOrderByInput
      minWeightToFetchApis: int

   _args: Args


   type: CollectionsResponse

class collectionsByOwnerId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection
      minWeightToFetchApis: int
      collection_type: str

   _args: Args


   type: CollectionsResponse

class getOrgHomepageCollections(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      orderByField: str
      orderDirection: OrderDirection
      minWeightToFetchApis: int

   _args: Args


   type: CollectionsResponse

class collectionById(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      collectionId: ID ##NON NULL

   _args: Args


   type: Collection

class collection(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Collection

collapsedCollections = list[CollapsedCollection]

class collectionBySlugifiedKey(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      slugifiedKey: str

   _args: Args


   type: Collection

getPrivateCollections = list[Collection]

getPrivateCollectionsV2 = list[Collection]

class collectionBySlugifiedKeyV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      slugifiedKey: str

   _args: Args


   type: CollectionV2

class collectionBySlugifiedKeyV3(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      slugifiedKey: str

   _args: Args


   type: CollectionV3

class getCommentsByIssueIdV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      issueId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: PaginatedComments

class getCommentByIdV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      issueId: int ##NON NULL
      commentId: int ##NON NULL

   _args: Args


   type: Comment

class search(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      term: str ##NON NULL

   _args: Args


   type: ApiSearch ##NON NULL

searchEntityByApiId = list[Any]

class getOpenApiSpecByApiId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiId: ID

   _args: Args


   type: Any

class entityById(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID

   _args: Args


   type: Entity

class activeEntity(GQLQuery):
   type: Entity

class apiByNameAndOwnerName(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiName: str
      ownerName: str

   _args: Args


   type: Api

class apiBySlugifiedNameAndOwnerName(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      slugifiedName: str
      ownerName: str

   _args: Args


   type: Api

class apiByNameAndOwnerId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiName: str
      ownerId: str

   _args: Args


   type: Api

userFollows = list[FollowUser]

class apiById(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiId: str

   _args: Args


   type: Api

apisById = list[Api]

class followUserAction(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      followerId: int
      followeeId: int

   _args: Args


   type: FollowPair

userFollowers = list[Follower]

calculateSeatsPrice = float

getSeatsTransactionsByOrgId = list[OrgTransaction]

organizationsTreeToken = str

getMinimumSeats = int

class transactionsById(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiId: str
      userId: int
      type: str
      pagingArgs: PagingArgs
      queryFilters: QueryFilters
      paymentStatusFilters: list[TransactionPaymentStatus]

   _args: Args


   type: TransactionsPaging

class unionDiscussionsByAuthor(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      authorId: int
      limit: int
      offset: int
      orderField: str
      orderType: str
      type: str

   _args: Args


   type: DiscussionObject

class getActiveUserContext(GQLQuery):
   type: ContextEntity

class getActiveTeamContext(GQLQuery):
   type: ContextEntity

class transactionsAnalyticsByApiId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiId: str
      fromDate: str
      toDate: str
      attributes: str

   _args: Args


   type: TransactionsAnalytics

class getConsumers(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
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
   class Args(GQLOperationArgs, GQLObject): 
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
   class Args(GQLOperationArgs, GQLObject): 
      where: ConsumersWhereInput ##NON NULL

   _args: Args


   type: ConsumerConnection

requestAdminToSubscribeToAnAPI = bool

class getCountryMetadata(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      ip: str

   _args: Args


   type: Country

class unionIssuesByAuthorV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      authorId: int
      type: str
      pagingArgs: PagingArgs
      apiIds: list[str]

   _args: Args


   type: DiscussionObject

class getIssuesByApiIdV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiId: str ##NON NULL
      pagingArgs: PagingArgs
      providerId: str

   _args: Args


   type: IssueObject

class getIssuesByApiIdsV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiIds: list[str] ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

endpointStats = list[EndpointStats]

endpointStatsByEntity = list[EndpointStats]

endpointStatsByEntityV2 = list[VersionEndpointStats]

getEndpointsWithinDateByParameters = list[EndpointStats]

class endpoint(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Endpoint

class endpoints(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: EndpointWhereInput ##NON NULL

   _args: Args


   type: EndpointConnection

searchEntities = list[Entity]

class entitiesMetadata(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: EntityMetadataWhereInput ##NON NULL
      orderBy: EntityMetadataOrderByInput
      pagination: PaginationInput

   _args: Args


   type: EntityMetadataConnection ##NON NULL

getEntitiesRoles = list[EntityRole]

class entitiesRoles(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: EntityRoleWhereInput ##NON NULL
      orderBy: EntityRoleOrderByInput
      pagination: PaginationInput

   _args: Args


   type: EntityRoleConnection ##NON NULL

getLogsCSV = list[LogsCSV]

class exportLogsCSVProvider(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      contextId: ID ##NON NULL
      fromDate: DateTime ##NON NULL
      toDate: DateTime ##NON NULL
      totalCount: int ##NON NULL
      filters: RequestLogFilters
      timeOffset: int

   _args: Args


   type: LogsCSVExports

class exportLogsCSVDeveloper(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      contextId: ID ##NON NULL
      fromDate: DateTime ##NON NULL
      toDate: DateTime ##NON NULL
      totalCount: int ##NON NULL
      filters: RequestLogFilters
      timeOffset: int

   _args: Args


   type: LogsCSVExports

class gateways(GQLQuery):
   type: GatewayConnection

getGateways = list[Gateway]

class getGatewayConfiguration(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: int ##NON NULL

   _args: Args


   type: ApiGatewayConfiguration

class graphQlIntrospectionSchema(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      introspectionCallUrl: str ##NON NULL

   _args: Args


   type: Any ##NON NULL

headlinesByApiNameAndOwnerId = list[Headline]

class getIssuesByOrganizatonId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: str ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

getResponseTimeByProviderId = float

getAverageResponseTime = float

class unionIssuesByAuthor(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      authorId: int
      type: str
      pagingArgs: PagingArgs

   _args: Args


   type: DiscussionObject

class getIssueByIdV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      issueId: int

   _args: Args


   type: Issue

class getIssuesByOrganizationId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: str
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

class getIssuesByTeamIdV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: str
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

getIssuesFollowsByUserIdV2 = list[IssueFollow]

class kafkaConfiguration(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiVersionId: str ##NON NULL

   _args: Args


   type: KafkaConfiguration

class kafkaTopics(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiVersionId: str ##NON NULL

   _args: Args


   type: KafkaTopics

class kafkaSchemas(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiVersionId: str ##NON NULL

   _args: Args


   type: KafkaSchemas

class kafkaTopicMetadata(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiVersionId: str ##NON NULL
      topicName: str ##NON NULL

   _args: Args


   type: TopicMetadataResponse

class getTemplate(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      accountId: str
      templateId: str

   _args: Args


   type: EnvelopeTemplate

class getLegalAgreementInfo(GQLQuery):
   type: LegalAgreementInfo

class updateLegalAgreementInfo(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      input: UpdateLegalAgreementInfo

   _args: Args


   type: LegalAgreementInfo

class createLegalAgreementInfo(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      input: CreateLegalAgreementInfo

   _args: Args


   type: LegalAgreementInfo

class deleteLegalAgreementInfo(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      entityId: str

   _args: Args


   type: Any

class getLegalAgreementSigningURL(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      input: GetLegalAgreementSigningURLInput ##NON NULL

   _args: Args


   type: Any

class logPayloadByRequestId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      requestId: ID
      callTime: str

   _args: Args


   type: LogPayload

class logPayloadByRequestIdWithLoggingRestrictions(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      requestId: ID
      callTime: str
      apiId: str

   _args: Args


   type: RestrictedLogPayload

class developerLogPayloadByRequestIdWithLoggingRestrictions(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      requestId: ID
      callTime: str
      apiId: str
      projectId: str

   _args: Args


   type: RestrictedLogPayload

class messageThreads(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: MessageThreadsWhereInput

   _args: Args


   type: MessageThreadsObject

messages = list[Message]

getApiAverageResponseTime = float

getProviderAverageResponseTime = float

class getRelativeAverageResponseTime(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      providerId: int ##NON NULL

   _args: Args


   type: RelativeARTResponse

class getMessageThread(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      threadId: int

   _args: Args


   type: MessageThread

newNotificationsByUserId = list[NewNotification]

notificationsByUserId = list[Notification]

class organization(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Organization

organizations = list[Organization]

getOrganizations = list[Organization]

class getOrganizationBySlugifiedName(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      slugifiedName: str

   _args: Args


   type: Organization

class getOrganizationById(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      orgId: ID ##NON NULL

   _args: Args


   type: Organization

class getEmailDomainAndCheckIfIgnored(GQLQuery):
   type: CorporateDomain

getOrganizationsWithTheSameEmail = list[CorporateDomainOrganization]

searchOrganizations = list[Entity]

class validateResetPasswordToken(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      token: str ##NON NULL

   _args: Args


   type: ValidateTokenResponse

getProjectAllowedAPIs = list[ProjectAllowedAPI]

class requestLogsByEntity(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
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

getAccessControlRoles = list[Role]

getRoles = list[Role]

class roles(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: RoleWhereInput ##NON NULL
      orderBy: RoleOrderByInput
      pagination: PaginationInput

   _args: Args


   type: RoleConnection ##NON NULL

class searchApis(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: SearchApiWhereInput ##NON NULL
      orderBy: SearchApiOrderByInput
      pagination: PaginationInput

   _args: Args


   type: SearchApiConnection ##NON NULL

class searchBlogPosts(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: SearchBlogPostWhereInput ##NON NULL
      pagination: PaginationInput

   _args: Args


   type: SearchBlogPostConnection

class searchCollections(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: SearchCollectionWhereInput
      orderBy: SearchCollectionOrderByInput
      pagination: PaginationInput

   _args: Args


   type: SearchCollectionConnection

class spotlights(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: SpotlightWhereInput ##NON NULL
      orderBy: SpotlightOrderByInput
      pagination: PaginationInput

   _args: Args


   type: SpotlightConnection ##NON NULL

searchSubscribedEntityByApiIdAndAppName = list[Project]

activeSubscriptionsCount = list[ActiveSubscriptionCount]

getInternalSubscriptions = list[BillingSubscription]

searchSubscribedEntityByApiId = list[Any]

class getSubscriptions(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: int
      userId: int
      apiId: str
      mashapeId: str
      pagingArgs: PagingArgs

   _args: Args


   type: SubscriptionsPaging

class getOrganizationSubscriptions(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      pagingArgs: PagingArgs

   _args: Args


   type: OrgSubscriptions

class subscriptions(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: SubscriptionsWhereInput
      pagination: PaginationInput

   _args: Args


   type: SubscriptionConnection

class subscription(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: int

   _args: Args


   type: BillingSubscription

subscriptionsCount = list[SubscriptionsCount]

getTagsList = list[TagDefinition]

class tagDefinitions(GQLQuery):
   type: TagDefinitionConnection

class paginatedTeamUsersByOrganizationId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      orgId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: PaginatedTeamUsers

class paginatedTeamUsersByOrganizationIdV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      orgId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: PaginatedTeamUsers

class teamUserByEmailAndOrgId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      email: str
      orgId: int

   _args: Args


   type: TeamUser

class teamUser(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: TeamUserWhereInput ##NON NULL

   _args: Args


   type: TeamUser

findUsersInOrganization = list[TeamUser]

class teamByTeamId(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      teamId: int
      orgId: int

   _args: Args


   type: Team

teamsByOrganizationId = list[Team]

class getTeamBySlugifiedName(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      slugifiedName: str

   _args: Args


   type: Team

searchTeams = list[Team]

class team(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Team

teams = list[Team]

class tenant(GQLQuery):
   type: Tenant

class transactions(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: TransactionsWhereInput
      pagination: PaginationInput

   _args: Args


   type: TransactionConnection

class transactionsSummary(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: TransactionsSummaryWhereInput

   _args: Args


   type: TransactionsSummary

class transformations(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: TransformationWhereInput
      orderBy: TransformationOrderByInput
      pagination: PaginationInput

   _args: Args


   type: TransformationConnection ##NON NULL

class tutorials(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: TutorialWhereInput ##NON NULL
      orderBy: TutorialOrderByInput
      pagination: PaginationInput

   _args: Args


   type: TutorialConnection

getPhoneNumbers = list[Phone]

getRecoveryCodes = list[RecoveryCode]

isTwoFactorEnabledByType = bool

getUsagesAndParentUsageForSubscription = list[UsagesStats]

getUsagesAgrregatedByTeamsForSubscription = list[UsagesStats]

getUsagesAndParentUsageForSubscriptionByBuckets = list[UsagesStats]

getUsagesAgrregatedByTeamsForSubscriptionByBuckets = list[UsagesStats]

class organizationQuotaUsageByApiIdV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      apiId: ID
      apiVersionId: ID
      internalData: Any

   _args: Args


   type: OrganizationApiUsagesV2

class getUserInviteByToken(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      token: str ##NON NULL

   _args: Args


   type: UserInvite

checkUserInvitesBranding = bool

class checkIfEmailsAlreadyInvited(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      orgId: ID ##NON NULL
      emails: list[str] ##NON NULL

   _args: Args


   type: Any

searchUsersToInvite = list[InviteUsersSearch]

class getUserSavedApis(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      userCollectionId: str

   _args: Args


   type: UserSavedApi ##NON NULL

class userById(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: int

   _args: Args


   type: User

class userByUsername(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      username: str
      includeUserAttributes: bool

   _args: Args


   type: User

getPrivateApisJwt = str

searchUsers = list[User]

class searchUsersV2(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      where: SearchUsersWhereInput ##NON NULL

   _args: Args


   type: User ##NON NULL

class user(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: User

users = list[User]

getVirtualPermissions = list[Permission]

virtualPermissions = list[VirtualPermission]

class getWorkflowsForProvider(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

class getWorkflowsForDeveloper(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

class getWorkflowsByRequestor(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

class getWorkflowsByRequestee(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

canWorkflowBeSubmitted = bool

class getWorkflowAudits(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      workflowId: int

   _args: Args


   type: WorkFlowAuditsResponse

getWorkflowsCount = int

exclusions = list[Exclusion]


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
