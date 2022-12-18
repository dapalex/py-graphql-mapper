from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

ping = str

class eventUrls(GQLObject):
   class Args(GQLOperationArgs): 
      pagination: PaginationArgs
      where: EventUrlWhereInput
      order: EventUrlSortablesInput

   _args: Args


   type: EventUrlConnection ##NON NULL

class eventUrl(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: EventUrl

class eventTypes(GQLObject):
   type: EventType ##NON NULL

class eventConfig(GQLObject):
   type: EventConfig

class gatewayInstances(GQLObject):
   class Args(GQLOperationArgs): 
      pagination: PaginationArgs
      where: GatewayInstanceWhereInput
      order: GatewayInstanceSortingInput

   _args: Args


   type: GatewayInstanceConnection ##NON NULL

class gatewayInstance(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class gatewayTemplates(GQLObject):
   class Args(GQLOperationArgs): 
      pagination: PaginationArgs
      where: GatewayTemplateWhereInput
      order: GatewayTemplateSortingInput

   _args: Args


   type: GatewayTemplateConnection ##NON NULL

class gatewayTemplate(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class gatewayTemplatesParams(GQLObject):
   class Args(GQLOperationArgs): 
      pagination: PaginationArgs
      where: GatewayTemplateParamsWhereInput
      order: GatewayTemplateParamSortingInput

   _args: Args


   type: GatewayTemplateParamConnection ##NON NULL

class gatewayTemplateParam(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: GatewayTemplateParam ##NON NULL

class envConfigCategories(GQLObject):
   type: EnvConfigCategory ##NON NULL

class envConfig(GQLObject):
   class Args(GQLOperationArgs): 
      id: int ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class envConfigs(GQLObject):
   class Args(GQLOperationArgs): 
      envConfigTerm: EnvConfigTerm ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class adminAuditLogs(GQLObject):
   class Args(GQLOperationArgs): 
      where: AdminAuditLogInput
      pagination: PaginationArgs
      orderBy: AdminAuditLogSortablesInput

   _args: Args


   type: AdminAuditLogConnection

class eventLogs(GQLObject):
   class Args(GQLOperationArgs): 
      where: EventLogInput
      pagination: PaginationArgs
      orderBy: EventLogSortablesInput

   _args: Args


   type: EventLogConnection

extensions = list[Extension]

class getSEOTagsByURL(GQLObject):
   class Args(GQLOperationArgs): 
      url: str

   _args: Args


   type: SEO

class getUserAlertById(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: UserAlert

getUserAlertsByScope = list[UserAlert]

class getAlertsDefinitions(GQLObject):
   type: AlertDefinition ##NON NULL

class userAlerts(GQLObject):
   class Args(GQLOperationArgs): 
      where: UserAlertsWhereInput ##NON NULL

   _args: Args


   type: UserAlertsConnection ##NON NULL

class userAlert(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: UserAlert

allowedPlanDeveloperByPlanId = list[AllowedPlanDeveloper]

class apiCertificate(GQLObject):
   class Args(GQLOperationArgs): 
      apiCertificateId: ID ##NON NULL

   _args: Args


   type: ApiCertificate

class apiCertificates(GQLObject):
   class Args(GQLOperationArgs): 
      where: ApiCertificateWhereInput
      orderBy: ApiCertificateOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiCertificateConnection ##NON NULL

class apiDevelopersByApiId(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: str
      pagingArgs: PagingArgs

   _args: Args


   type: ApiDeveloper ##NON NULL

class apiFollowers(GQLObject):
   class Args(GQLOperationArgs): 
      where: ApiFollowerWhereInput ##NON NULL
      orderBy: ApiFollowerOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiFollowerConnection ##NON NULL

class apiReferenceByApiAndVersionId(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: str ##NON NULL
      versionId: str ##NON NULL

   _args: Args


   type: ApiReference

class apiReferences(GQLObject):
   class Args(GQLOperationArgs): 
      where: ApiReferenceWhereInput

   _args: Args


   type: ApiReferenceConnection ##NON NULL

class apiSearch(GQLObject):
   class Args(GQLOperationArgs): 
      searchArguments: SearchArguments

   _args: Args


   type: ApiSearchPaged

class apiSearchV3(GQLObject):
   class Args(GQLOperationArgs): 
      searchArguments: SearchArguments

   _args: Args


   type: ApiSearchPaged

class apiSpecImportProgresses(GQLObject):
   class Args(GQLOperationArgs): 
      trackingIds: list[ID] ##NON NULL

   _args: Args


   type: ApiSpecImportProcess ##NON NULL

class bulkApisSummaryByTrackingIds(GQLObject):
   class Args(GQLOperationArgs): 
      trackingIds: list[ID] ##NON NULL

   _args: Args


   type: BatchTrackingIdsSummary

class calculatedStatistics(GQLObject):
   class Args(GQLOperationArgs): 
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

class getApiVersion(GQLObject):
   class Args(GQLOperationArgs): 
      versionId: ID ##NON NULL

   _args: Args


   type: ApiVersion

class apiVersion(GQLObject):
   class Args(GQLOperationArgs): 
      apiVersionId: ID ##NON NULL

   _args: Args


   type: ApiVersion

class apiVersions(GQLObject):
   class Args(GQLOperationArgs): 
      where: ApiVersionWhereInput
      orderBy: ApiVersionOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiVersionConnection ##NON NULL

class api(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: Api

class apis(GQLObject):
   class Args(GQLOperationArgs): 
      where: ApiWhereInput
      orderBy: ApiOrderByInput
      pagination: PaginationInput

   _args: Args


   type: ApiConnection ##NON NULL

class exportOpenApi(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: ID ##NON NULL
      apiVersionId: ID

   _args: Args


   type: Any

class validateSwagger(GQLObject):
   class Args(GQLOperationArgs): 
      input: validateSwaggerInput

   _args: Args


   type: Any

class applicationAuthorization(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class applicationAuthorizations(GQLObject):
   class Args(GQLOperationArgs): 
      where: AppAuthorizationsWhereInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class applicationEnvironmentsKeysByApplicationIdAndEnvironment(GQLObject):
   class Args(GQLOperationArgs): 
      applicationId: str
      environment: str

   _args: Args


   type: ApplicationEnvironmentPaging

class applicationEnvironmentsByApplicationIdAndEnvironment(GQLObject):
   class Args(GQLOperationArgs): 
      applicationId: str
      environment: str

   _args: Args


   type: ApplicationEnvironment

class applicationById(GQLObject):
   class Args(GQLOperationArgs): 
      id: int

   _args: Args


   type: Application

class asset(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: Asset

class assets(GQLObject):
   class Args(GQLOperationArgs): 
      where: AssetWhereInput ##NON NULL

   _args: Args


   type: Asset ##NON NULL

class assetsDownloadUrls(GQLObject):
   class Args(GQLOperationArgs): 
      where: AssetWhereInput ##NON NULL

   _args: Args


   type: AssetForDownload ##NON NULL

class asyncApiConfigurations(GQLObject):
   class Args(GQLOperationArgs): 
      where: AsyncApiConfigurationWhereInput ##NON NULL

   _args: Args


   type: AsyncApiConfigurationConnection ##NON NULL

class userAttributesByUserId(GQLObject):
   class Args(GQLOperationArgs): 
      userId: int

   _args: Args


   type: UserAttributes

class auditByOrganizationId(GQLObject):
   class Args(GQLOperationArgs): 
      searchTerm: str
      from_: int
      orgId: int

   _args: Args


   type: auditTrails

class audit(GQLObject):
   class Args(GQLOperationArgs): 
      where: AuditWhereInput ##NON NULL

   _args: Args


   type: auditTrails

class auditLogin(GQLObject):
   class Args(GQLOperationArgs): 
      from_: int
      userId: str

   _args: Args


   type: auditTrails

class userByEmail(GQLObject):
   class Args(GQLOperationArgs): 
      email: str

   _args: Args


   type: User

class activeUser(GQLObject):
   type: User

getAuthStrategies = list[authStrategy]

getBillingFeaturesByApiVersionId = list[BillingFeature]

getBillingFeaturesByApiId = list[BillingFeature]

isMonetizationEnabled = bool

class billingItems(GQLObject):
   class Args(GQLOperationArgs): 
      where: BillingItemsWhereInput ##NON NULL

   _args: Args


   type: BillingItemConnection

class getFreeSeatsObj(GQLObject):
   class Args(GQLOperationArgs): 
      orgId: ID ##NON NULL

   _args: Args


   type: SeatsBillingInformation

class getBillingPlanVersionsByApiId(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: str ##NON NULL
      apiVersionId: str
      pagingArgs: PagingArgsBilling
      filters: BillingPlanVersionFilters

   _args: Args


   type: BillingPlanVersionsResponse

class getBillingPlanVersionById(GQLObject):
   class Args(GQLOperationArgs): 
      billingPlanVersionId: str ##NON NULL

   _args: Args


   type: BillingPlanVersion

class billingPlanVersion(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: BillingPlanVersion

class billingPlanVersions(GQLObject):
   class Args(GQLOperationArgs): 
      where: BillingPlanVersionWhereInput
      pagination: PaginationInput

   _args: Args


   type: BillingPlanVersionConnection

class calculatedStatisticsByEndpointAndApiversion(GQLObject):
   class Args(GQLOperationArgs): 
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

class categoriesV2(GQLObject):
   class Args(GQLOperationArgs): 
      where: CategoryWhereInput
      orderBy: CategoryOrderByInput
      pagination: PaginationInput

   _args: Args


   type: CategoryConnection ##NON NULL

categoryEntities = list[CategoryEntity]

categories = list[Category]

collectionsItemsByIds = list[CollectionItem]

class collections(GQLObject):
   class Args(GQLOperationArgs): 
      where: CollectionsWhereInput
      orderBy: CollectionsOrderByInput
      minWeightToFetchApis: int

   _args: Args


   type: CollectionsResponse

class collectionsByOwnerId(GQLObject):
   class Args(GQLOperationArgs): 
      orderByField: str
      orderDirection: OrderDirection
      minWeightToFetchApis: int
      collection_type: str

   _args: Args


   type: CollectionsResponse

class getOrgHomepageCollections(GQLObject):
   class Args(GQLOperationArgs): 
      orderByField: str
      orderDirection: OrderDirection
      minWeightToFetchApis: int

   _args: Args


   type: CollectionsResponse

class collectionById(GQLObject):
   class Args(GQLOperationArgs): 
      collectionId: ID ##NON NULL

   _args: Args


   type: Collection

class collection(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: Collection

collapsedCollections = list[CollapsedCollection]

class collectionBySlugifiedKey(GQLObject):
   class Args(GQLOperationArgs): 
      slugifiedKey: str

   _args: Args


   type: Collection

getPrivateCollections = list[Collection]

getPrivateCollectionsV2 = list[Collection]

class collectionBySlugifiedKeyV2(GQLObject):
   class Args(GQLOperationArgs): 
      slugifiedKey: str

   _args: Args


   type: CollectionV2

class collectionBySlugifiedKeyV3(GQLObject):
   class Args(GQLOperationArgs): 
      slugifiedKey: str

   _args: Args


   type: CollectionV3

class getCommentsByIssueIdV2(GQLObject):
   class Args(GQLOperationArgs): 
      issueId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: PaginatedComments

class getCommentByIdV2(GQLObject):
   class Args(GQLOperationArgs): 
      issueId: int ##NON NULL
      commentId: int ##NON NULL

   _args: Args


   type: Comment

class search(GQLObject):
   class Args(GQLOperationArgs): 
      term: str ##NON NULL

   _args: Args


   type: ApiSearch ##NON NULL

searchEntityByApiId = list[Any]

class getOpenApiSpecByApiId(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: ID

   _args: Args


   type: Any

class entityById(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID

   _args: Args


   type: Entity

class activeEntity(GQLObject):
   type: Entity

class apiByNameAndOwnerName(GQLObject):
   class Args(GQLOperationArgs): 
      apiName: str
      ownerName: str

   _args: Args


   type: Api

class apiBySlugifiedNameAndOwnerName(GQLObject):
   class Args(GQLOperationArgs): 
      slugifiedName: str
      ownerName: str

   _args: Args


   type: Api

class apiByNameAndOwnerId(GQLObject):
   class Args(GQLOperationArgs): 
      apiName: str
      ownerId: str

   _args: Args


   type: Api

userFollows = list[FollowUser]

class apiById(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: str

   _args: Args


   type: Api

apisById = list[Api]

class followUserAction(GQLObject):
   class Args(GQLOperationArgs): 
      followerId: int
      followeeId: int

   _args: Args


   type: FollowPair

userFollowers = list[Follower]

calculateSeatsPrice = float

getSeatsTransactionsByOrgId = list[OrgTransaction]

organizationsTreeToken = str

getMinimumSeats = int

class transactionsById(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: str
      userId: int
      type: str
      pagingArgs: PagingArgs
      queryFilters: QueryFilters
      paymentStatusFilters: list[TransactionPaymentStatus]

   _args: Args


   type: TransactionsPaging

class unionDiscussionsByAuthor(GQLObject):
   class Args(GQLOperationArgs): 
      authorId: int
      limit: int
      offset: int
      orderField: str
      orderType: str
      type: str

   _args: Args


   type: DiscussionObject

class getActiveUserContext(GQLObject):
   type: ContextEntity

class getActiveTeamContext(GQLObject):
   type: ContextEntity

class transactionsAnalyticsByApiId(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: str
      fromDate: str
      toDate: str
      attributes: str

   _args: Args


   type: TransactionsAnalytics

class getConsumers(GQLObject):
   class Args(GQLOperationArgs): 
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

class getFreeConsumers(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: list[ID] ##NON NULL
      offset: int
      limit: int
      order: str
      lastActive: list[str]
      username: list[str]
      userId: list[int]

   _args: Args


   type: Consumers

class consumers(GQLObject):
   class Args(GQLOperationArgs): 
      where: ConsumersWhereInput ##NON NULL

   _args: Args


   type: ConsumerConnection

requestAdminToSubscribeToAnAPI = bool

class getCountryMetadata(GQLObject):
   class Args(GQLOperationArgs): 
      ip: str

   _args: Args


   type: Country

class unionIssuesByAuthorV2(GQLObject):
   class Args(GQLOperationArgs): 
      authorId: int
      type: str
      pagingArgs: PagingArgs
      apiIds: list[str]

   _args: Args


   type: DiscussionObject

class getIssuesByApiIdV2(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: str ##NON NULL
      pagingArgs: PagingArgs
      providerId: str

   _args: Args


   type: IssueObject

class getIssuesByApiIdsV2(GQLObject):
   class Args(GQLOperationArgs): 
      apiIds: list[str] ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

endpointStats = list[EndpointStats]

endpointStatsByEntity = list[EndpointStats]

endpointStatsByEntityV2 = list[VersionEndpointStats]

getEndpointsWithinDateByParameters = list[EndpointStats]

class endpoint(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: Endpoint

class endpoints(GQLObject):
   class Args(GQLOperationArgs): 
      where: EndpointWhereInput ##NON NULL

   _args: Args


   type: EndpointConnection

searchEntities = list[Entity]

class entitiesMetadata(GQLObject):
   class Args(GQLOperationArgs): 
      where: EntityMetadataWhereInput ##NON NULL
      orderBy: EntityMetadataOrderByInput
      pagination: PaginationInput

   _args: Args


   type: EntityMetadataConnection ##NON NULL

getEntitiesRoles = list[EntityRole]

class entitiesRoles(GQLObject):
   class Args(GQLOperationArgs): 
      where: EntityRoleWhereInput ##NON NULL
      orderBy: EntityRoleOrderByInput
      pagination: PaginationInput

   _args: Args


   type: EntityRoleConnection ##NON NULL

getLogsCSV = list[LogsCSV]

class exportLogsCSVProvider(GQLObject):
   class Args(GQLOperationArgs): 
      contextId: ID ##NON NULL
      fromDate: DateTime ##NON NULL
      toDate: DateTime ##NON NULL
      totalCount: int ##NON NULL
      filters: RequestLogFilters
      timeOffset: int

   _args: Args


   type: LogsCSVExports

class exportLogsCSVDeveloper(GQLObject):
   class Args(GQLOperationArgs): 
      contextId: ID ##NON NULL
      fromDate: DateTime ##NON NULL
      toDate: DateTime ##NON NULL
      totalCount: int ##NON NULL
      filters: RequestLogFilters
      timeOffset: int

   _args: Args


   type: LogsCSVExports

class gateways(GQLObject):
   type: GatewayConnection

getGateways = list[Gateway]

class getGatewayConfiguration(GQLObject):
   class Args(GQLOperationArgs): 
      id: int ##NON NULL

   _args: Args


   type: ApiGatewayConfiguration

class graphQlIntrospectionSchema(GQLObject):
   class Args(GQLOperationArgs): 
      introspectionCallUrl: str ##NON NULL

   _args: Args


   type: Any ##NON NULL

headlinesByApiNameAndOwnerId = list[Headline]

class getIssuesByOrganizatonId(GQLObject):
   class Args(GQLOperationArgs): 
      id: str ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

getResponseTimeByProviderId = float

getAverageResponseTime = float

class unionIssuesByAuthor(GQLObject):
   class Args(GQLOperationArgs): 
      authorId: int
      type: str
      pagingArgs: PagingArgs

   _args: Args


   type: DiscussionObject

class getIssueByIdV2(GQLObject):
   class Args(GQLOperationArgs): 
      issueId: int

   _args: Args


   type: Issue

class getIssuesByOrganizationId(GQLObject):
   class Args(GQLOperationArgs): 
      id: str
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

class getIssuesByTeamIdV2(GQLObject):
   class Args(GQLOperationArgs): 
      id: str
      pagingArgs: PagingArgs

   _args: Args


   type: IssueObject

getIssuesFollowsByUserIdV2 = list[IssueFollow]

class kafkaConfiguration(GQLObject):
   class Args(GQLOperationArgs): 
      apiVersionId: str ##NON NULL

   _args: Args


   type: KafkaConfiguration

class kafkaTopics(GQLObject):
   class Args(GQLOperationArgs): 
      apiVersionId: str ##NON NULL

   _args: Args


   type: KafkaTopics

class kafkaSchemas(GQLObject):
   class Args(GQLOperationArgs): 
      apiVersionId: str ##NON NULL

   _args: Args


   type: KafkaSchemas

class kafkaTopicMetadata(GQLObject):
   class Args(GQLOperationArgs): 
      apiVersionId: str ##NON NULL
      topicName: str ##NON NULL

   _args: Args


   type: TopicMetadataResponse

class getTemplate(GQLObject):
   class Args(GQLOperationArgs): 
      accountId: str
      templateId: str

   _args: Args


   type: EnvelopeTemplate

class getLegalAgreementInfo(GQLObject):
   type: LegalAgreementInfo

class updateLegalAgreementInfo(GQLObject):
   class Args(GQLOperationArgs): 
      input: UpdateLegalAgreementInfo

   _args: Args


   type: LegalAgreementInfo

class createLegalAgreementInfo(GQLObject):
   class Args(GQLOperationArgs): 
      input: CreateLegalAgreementInfo

   _args: Args


   type: LegalAgreementInfo

class deleteLegalAgreementInfo(GQLObject):
   class Args(GQLOperationArgs): 
      entityId: str

   _args: Args


   type: Any

class getLegalAgreementSigningURL(GQLObject):
   class Args(GQLOperationArgs): 
      input: GetLegalAgreementSigningURLInput ##NON NULL

   _args: Args


   type: Any

class logPayloadByRequestId(GQLObject):
   class Args(GQLOperationArgs): 
      requestId: ID
      callTime: str

   _args: Args


   type: LogPayload

class logPayloadByRequestIdWithLoggingRestrictions(GQLObject):
   class Args(GQLOperationArgs): 
      requestId: ID
      callTime: str
      apiId: str

   _args: Args


   type: RestrictedLogPayload

class developerLogPayloadByRequestIdWithLoggingRestrictions(GQLObject):
   class Args(GQLOperationArgs): 
      requestId: ID
      callTime: str
      apiId: str
      projectId: str

   _args: Args


   type: RestrictedLogPayload

class messageThreads(GQLObject):
   class Args(GQLOperationArgs): 
      where: MessageThreadsWhereInput

   _args: Args


   type: MessageThreadsObject

messages = list[Message]

getApiAverageResponseTime = float

getProviderAverageResponseTime = float

class getRelativeAverageResponseTime(GQLObject):
   class Args(GQLOperationArgs): 
      providerId: int ##NON NULL

   _args: Args


   type: RelativeARTResponse

class getMessageThread(GQLObject):
   class Args(GQLOperationArgs): 
      threadId: int

   _args: Args


   type: MessageThread

newNotificationsByUserId = list[NewNotification]

notificationsByUserId = list[Notification]

class organization(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: Organization

organizations = list[Organization]

getOrganizations = list[Organization]

class getOrganizationBySlugifiedName(GQLObject):
   class Args(GQLOperationArgs): 
      slugifiedName: str

   _args: Args


   type: Organization

class getOrganizationById(GQLObject):
   class Args(GQLOperationArgs): 
      orgId: ID ##NON NULL

   _args: Args


   type: Organization

class getEmailDomainAndCheckIfIgnored(GQLObject):
   type: CorporateDomain

getOrganizationsWithTheSameEmail = list[CorporateDomainOrganization]

searchOrganizations = list[Entity]

class validateResetPasswordToken(GQLObject):
   class Args(GQLOperationArgs): 
      token: str ##NON NULL

   _args: Args


   type: ValidateTokenResponse

getProjectAllowedAPIs = list[ProjectAllowedAPI]

class requestLogsByEntity(GQLObject):
   class Args(GQLOperationArgs): 
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

class roles(GQLObject):
   class Args(GQLOperationArgs): 
      where: RoleWhereInput ##NON NULL
      orderBy: RoleOrderByInput
      pagination: PaginationInput

   _args: Args


   type: RoleConnection ##NON NULL

class searchApis(GQLObject):
   class Args(GQLOperationArgs): 
      where: SearchApiWhereInput ##NON NULL
      orderBy: SearchApiOrderByInput
      pagination: PaginationInput

   _args: Args


   type: SearchApiConnection ##NON NULL

class searchBlogPosts(GQLObject):
   class Args(GQLOperationArgs): 
      where: SearchBlogPostWhereInput ##NON NULL
      pagination: PaginationInput

   _args: Args


   type: SearchBlogPostConnection

class searchCollections(GQLObject):
   class Args(GQLOperationArgs): 
      where: SearchCollectionWhereInput
      orderBy: SearchCollectionOrderByInput
      pagination: PaginationInput

   _args: Args


   type: SearchCollectionConnection

class spotlights(GQLObject):
   class Args(GQLOperationArgs): 
      where: SpotlightWhereInput ##NON NULL
      orderBy: SpotlightOrderByInput
      pagination: PaginationInput

   _args: Args


   type: SpotlightConnection ##NON NULL

searchSubscribedEntityByApiIdAndAppName = list[Project]

activeSubscriptionsCount = list[ActiveSubscriptionCount]

getInternalSubscriptions = list[BillingSubscription]

searchSubscribedEntityByApiId = list[Any]

class getSubscriptions(GQLObject):
   class Args(GQLOperationArgs): 
      id: int
      userId: int
      apiId: str
      mashapeId: str
      pagingArgs: PagingArgs

   _args: Args


   type: SubscriptionsPaging

class getOrganizationSubscriptions(GQLObject):
   class Args(GQLOperationArgs): 
      pagingArgs: PagingArgs

   _args: Args


   type: OrgSubscriptions

class subscriptions(GQLObject):
   class Args(GQLOperationArgs): 
      where: SubscriptionsWhereInput
      pagination: PaginationInput

   _args: Args


   type: SubscriptionConnection

class subscription(GQLObject):
   class Args(GQLOperationArgs): 
      id: int

   _args: Args


   type: BillingSubscription

subscriptionsCount = list[SubscriptionsCount]

getTagsList = list[TagDefinition]

class tagDefinitions(GQLObject):
   type: TagDefinitionConnection

class paginatedTeamUsersByOrganizationId(GQLObject):
   class Args(GQLOperationArgs): 
      orgId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: PaginatedTeamUsers

class paginatedTeamUsersByOrganizationIdV2(GQLObject):
   class Args(GQLOperationArgs): 
      orgId: int ##NON NULL
      pagingArgs: PagingArgs

   _args: Args


   type: PaginatedTeamUsers

class teamUserByEmailAndOrgId(GQLObject):
   class Args(GQLOperationArgs): 
      email: str
      orgId: int

   _args: Args


   type: TeamUser

class teamUser(GQLObject):
   class Args(GQLOperationArgs): 
      where: TeamUserWhereInput ##NON NULL

   _args: Args


   type: TeamUser

findUsersInOrganization = list[TeamUser]

class teamByTeamId(GQLObject):
   class Args(GQLOperationArgs): 
      teamId: int
      orgId: int

   _args: Args


   type: Team

teamsByOrganizationId = list[Team]

class getTeamBySlugifiedName(GQLObject):
   class Args(GQLOperationArgs): 
      slugifiedName: str

   _args: Args


   type: Team

searchTeams = list[Team]

class team(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: Team

teams = list[Team]

class tenant(GQLObject):
   type: Tenant

class transactions(GQLObject):
   class Args(GQLOperationArgs): 
      where: TransactionsWhereInput
      pagination: PaginationInput

   _args: Args


   type: TransactionConnection

class transactionsSummary(GQLObject):
   class Args(GQLOperationArgs): 
      where: TransactionsSummaryWhereInput

   _args: Args


   type: TransactionsSummary

class transformations(GQLObject):
   class Args(GQLOperationArgs): 
      where: TransformationWhereInput
      orderBy: TransformationOrderByInput
      pagination: PaginationInput

   _args: Args


   type: TransformationConnection ##NON NULL

class tutorials(GQLObject):
   class Args(GQLOperationArgs): 
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

class organizationQuotaUsageByApiIdV2(GQLObject):
   class Args(GQLOperationArgs): 
      apiId: ID
      apiVersionId: ID
      internalData: Any

   _args: Args


   type: OrganizationApiUsagesV2

class getUserInviteByToken(GQLObject):
   class Args(GQLOperationArgs): 
      token: str ##NON NULL

   _args: Args


   type: UserInvite

checkUserInvitesBranding = bool

class checkIfEmailsAlreadyInvited(GQLObject):
   class Args(GQLOperationArgs): 
      orgId: ID ##NON NULL
      emails: list[str] ##NON NULL

   _args: Args


   type: Any

searchUsersToInvite = list[InviteUsersSearch]

class getUserSavedApis(GQLObject):
   class Args(GQLOperationArgs): 
      userCollectionId: str

   _args: Args


   type: UserSavedApi ##NON NULL

class userById(GQLObject):
   class Args(GQLOperationArgs): 
      id: int

   _args: Args


   type: User

class userByUsername(GQLObject):
   class Args(GQLOperationArgs): 
      username: str
      includeUserAttributes: bool

   _args: Args


   type: User

getPrivateApisJwt = str

searchUsers = list[User]

class searchUsersV2(GQLObject):
   class Args(GQLOperationArgs): 
      where: SearchUsersWhereInput ##NON NULL

   _args: Args


   type: User ##NON NULL

class user(GQLObject):
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: User

users = list[User]

getVirtualPermissions = list[Permission]

virtualPermissions = list[VirtualPermission]

class getWorkflowsForProvider(GQLObject):
   class Args(GQLOperationArgs): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

class getWorkflowsForDeveloper(GQLObject):
   class Args(GQLOperationArgs): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

class getWorkflowsByRequestor(GQLObject):
   class Args(GQLOperationArgs): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

class getWorkflowsByRequestee(GQLObject):
   class Args(GQLOperationArgs): 
      options: GetWorkflowsOptions
      pagingArgs: PagingArgs

   _args: Args


   type: WorkFlowsResponse

canWorkflowBeSubmitted = bool

class getWorkflowAudits(GQLObject):
   class Args(GQLOperationArgs): 
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
