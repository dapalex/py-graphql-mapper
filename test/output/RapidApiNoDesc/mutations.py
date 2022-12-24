from pygqlmap import GQLMutation
from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *


class createEventUrl(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      createDto: EventUrlCreateInput ##NON NULL

   _args: Args


   type: EventUrl ##NON NULL

class updateEventUrl(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL
      updateDto: EventUrlUpdateInput ##NON NULL

   _args: Args


   type: EventUrl ##NON NULL

class deleteEventUrl(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class upsertEventConfig(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: EventConfigUpdateInput ##NON NULL

   _args: Args


   type: EventConfig ##NON NULL

class deleteEventConfig(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayInstance(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      createDto: GatewayInstanceCreateInput ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class updateGatewayInstance(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      updateDto: GatewayInstanceUpdateInput ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class deleteGatewayInstance(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayTemplate(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      createDto: GatewayTemplateCreateInput ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class updateGatewayTemplate(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      updateDto: GatewayTemplateUpdateInput ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class deleteGatewayTemplate(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayTemplateParam(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      createDto: GatewayTemplateParamsCreateInput ##NON NULL

   _args: Args


   type: GatewayTemplateParam ##NON NULL

class updateEnvConfig(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      envConfig: EnvConfigUpdateInput ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class resetEnvConfig(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: int ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class addUserAlert(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: addUserAlertInput

   _args: Args


   type: UserAlert ##NON NULL

class deleteUserAlerts(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: deleteUserAlertsInput ##NON NULL

   _args: Args


   type: ID ##NON NULL

class editUserAlert(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: editUserAlertInput ##NON NULL

   _args: Args


   type: UserAlert ##NON NULL

class updateUserAlerts(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: list[UserAlertUpdateInput] ##NON NULL

   _args: Args


   type: UserAlert ##NON NULL

class createApiCertificates(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      certificates: list[ApiCertificateCreateInput] ##NON NULL

   _args: Args


   type: ApiCertificateCreationResult ##NON NULL

class deleteApiCertificates(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: bool ##NON NULL

class saveApiDevelopersToApi(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: SaveApiDevelopersInput ##NON NULL

   _args: Args


   type: bool

class copyApiDevelopersFromVersion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CopyApiDevelopersInput

   _args: Args


   type: bool

class createApiFavorites(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateApiFavoritesInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class deleteApiFavorites(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteApiFavoritesInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class createApiFollowers(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      apiFollowers: ApiFollowerCreateInput ##NON NULL

   _args: Args


   type: ApiFollower ##NON NULL

class deleteApiFollowers(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      apiFollowers: ApiFollowerDeleteInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class createApisFromSpecs(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      creations: list[ApiCreateFromSpecInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class updateApisFromSpecs(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      updates: list[ApiUpdateFromSpecInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class createApisFromRapidOas(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      creations: list[ApiCreateFromRapidOasInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class updateApisFromRapidOas(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      updates: list[ApiUpdateFromRapidOasInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class createApiVersions(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      apiVersions: list[ApiVersionCreateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class createGqlApiVersions(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      gqlApiVersions: list[GqlApiVersionCreateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class updateApiVersions(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      apiVersions: list[ApiVersionUpdateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class createApiVersionBillingPlanVersion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: createApiVersionBillingPlanVersionInput

   _args: Args


   type: ApiVersionBillingPlanVersion

class createApi(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      api: ApiCreateInput ##NON NULL

   _args: Args


   type: Api ##NON NULL

class updateApi(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      api: ApiUpdateInput ##NON NULL

   _args: Args


   type: Api ##NON NULL

class provisionSwaggerFiles(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: list[ProvisionApiFromFileInput] ##NON NULL

   _args: Args


   type: list[str]

class deleteApi(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool ##NON NULL

class createApplicationAuthorization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AppAuthorizationCreateInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class updateApplicationAuthorization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AppAuthorizationUpdateInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class deleteApplicationAuthorization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool ##NON NULL

class addApplicationEnvironmentKey(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddApplicationEnvironmentKeyInput ##NON NULL

   _args: Args


   type: Any

class editApplicationEnvironmentKey(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: EditApplicationEnviornmentKeyInput ##NON NULL

   _args: Args


   type: Any

class deleteApplicationEnvironmentKey(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteApplicationEnvironmentKeyInput ##NON NULL

   _args: Args


   type: ID

class generateAssetUploadUrl(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: GenerateAssetUploadUrlInput ##NON NULL

   _args: Args


   type: Asset ##NON NULL

class deleteAsset(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool ##NON NULL

class updateAssetUploaded(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Asset

class updateAsset(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AssetUpdateInput ##NON NULL

   _args: Args


   type: Asset

class upsertAsyncApiConfiguration(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      asyncApiConfigurations: list[AsyncApiConfigurationCreateInput] ##NON NULL

   _args: Args


   type: AsyncApiConfiguration ##NON NULL

class upsertUserAttributes(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UserAttributesInput

   _args: Args


   type: Any

class updateUserAttributeItem(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ThemeUserAttributesInput ##NON NULL

   _args: Args


   type: Any

class createAuthentications(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      authentications: list[AuthenticationCreateInput] ##NON NULL

   _args: Args


   type: Authentication ##NON NULL

class updateAuthentications(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      authentications: list[AuthenticationUpdateInput] ##NON NULL

   _args: Args


   type: Authentication ##NON NULL

class createOrUpdateAPIVersionAuthentication(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: createAuthenticationInput

   _args: Args


   type: AuthenticationCreateOrUpdateResult

class createBillingFeature(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      createBillingFeature: createBillingFeature

   _args: Args


   type: BillingFeature

class updateBillingFeature(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      updateBillingFeature: updateBillingFeature

   _args: Args


   type: BillingFeature

class upsertBillingFeature(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      upsertBillingFeature: upsertBillingFeatureInput ##NON NULL

   _args: Args


   type: BillingFeature

class deleteBillingFeature(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      billingFeatureId: str

   _args: Args


   type: Any

class deleteBillingFeatures(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      billingFeatureIds: list[str]

   _args: Args


   type: Any

class createStripeCustomer(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class updateStripeCustomer(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class createStripeCustomerV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class updateStripeCustomerV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class deleteCustomerPaymentMethod(GQLMutation):
   type: bool

class upsertBillingItem(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: BillingItemUpsertInput ##NON NULL

   _args: Args


   type: BillingItem

class deleteBillingItem(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Any

class deleteBillingItems(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: bool ##NON NULL

class deleteBillingPlans(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: bool

class updateAllowedPlanDevelopers(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AllowedPlanDevelopersUpdateInput

   _args: Args


   type: list[AllowedPlanDeveloper]

class editOrganizationInvoice(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: EditOrganizationInvoiceInput

   _args: Args


   type: bool

class createBillingPlan(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      billingPlan: BillingPlanCreateInput ##NON NULL

   _args: Args


   type: BillingPlan

class updateBillingPlanMetadata(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      billingPlan: BillingPlanMetadataUpdateInput ##NON NULL

   _args: Args


   type: BillingPlan

class updateBillingPlanExtended(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      billingPlan: BillingPlanExtendedUpdateInput ##NON NULL

   _args: Args


   type: BillingPlan

class upsertBillingPlanAndVersion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      upsertBillingPlanAndVersionInput: upsertBillingPlanAndVersionInput ##NON NULL

   _args: Args


   type: BillingPlanVersion

class blockUsers(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: BlockedUserInput

   _args: Args


   type: bool

class unblockUsers(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: BlockedUserInput

   _args: Args


   type: bool

class createCategory(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      category: CategoryCreateInput ##NON NULL

   _args: Args


   type: Category ##NON NULL

class updateCategory(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      category: CategoryUpdateInput ##NON NULL

   _args: Args


   type: Category ##NON NULL

class deleteCategories(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      categories: list[ID] ##NON NULL

   _args: Args


   type: DeletedCategory ##NON NULL

class deleteCollection(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool

class updateCollection(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CollectionUpdateInput ##NON NULL

   _args: Args


   type: Collection

class createCollection(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CollectionCreateInput ##NON NULL

   _args: Args


   type: Collection

class bulkUpdateCollections(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      collections: list[UpdateCollectionsInput] ##NON NULL

   _args: Args


   type: list[Collection]

class updateCollections(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      collections: list[UpdateCollectionsInput] ##NON NULL

   _args: Args


   type: list[Collection]

class postCommentV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CommentCreateInput

   _args: Args


   type: Comment

class deleteCommentV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CommentDeleteInput

   _args: Args


   type: Any

class updateCommentV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CommentUpdateInput

   _args: Args


   type: Any

class postCommentV3(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CommentCreateInput

   _args: Args


   type: Comment

class subscribeToPlan(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: SubscribeInput

   _args: Args


   type: BillingSubscription

class unfollowUser(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: FollowInput

   _args: Args


   type: bool

class followUser(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: FollowInput

   _args: Args


   type: bool

class followApi(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: FollowApiInput

   _args: Args


   type: bool

class unfollowApi(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: FollowApiInput

   _args: Args


   type: bool

class sendMessage(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: SendMessageInput

   _args: Args


   type: bool

class rateApi(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: RatingInput

   _args: Args


   type: Any

class upsertEntityMetadataBulk(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      entityId: ID
      entityAttributes: list[EntityAttribute] ##NON NULL

   _args: Args


   type: Any

class upsertEntityMetadata(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      entityMetadata: EntityMetadataInput

   _args: Args


   type: Any

class deleteIssueV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: IssueDeleteInput

   _args: Args


   type: Any

class updateIssueV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: IssueUpdateInput

   _args: Args


   type: Any

class deleteIssues(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: IssuesDeleteInput

   _args: Args


   type: Any

class postIssueV3(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: IssueCreateInputV2

   _args: Args


   type: Any

class updateOrCreateEndpointWithParameters(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: updateOrCreateEndpointWithParameters

   _args: Args


   type: Any

class updateEndpointEntity(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: updateEndpointEntity

   _args: Args


   type: Any

class deleteEndpoint(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      endpointId: str

   _args: Args


   type: Any

class deleteEndpoints(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      endpointIds: list[str]

   _args: Args


   type: Any

class updateEndpointsCollectionOrder(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      endpointsCollectionOrder: list[EndpointOrder]

   _args: Args


   type: Any

class createEndpointsGroups(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      groups: list[EndpointsGroupCreateInput] ##NON NULL

   _args: Args


   type: EndpointsGroup ##NON NULL

class updateEndpointsGroups(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      groups: list[EndpointsGroupUpdateInput] ##NON NULL

   _args: Args


   type: EndpointsGroup ##NON NULL

class deleteEndpointsGroups(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: ID ##NON NULL

class duplicateNameCheck(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DuplicateNameCheckInput

   _args: Args


   type: bool

class createEntityMetadata(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      entityMetadata: EntityMetadataInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class updateEntityMetadata(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      entityMetadata: EntityMetadataInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class createEntitiesRoles(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: EntityRoleCreateInput

   _args: Args


   type: bool

class upsertEntityRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: EntityRoleInput

   _args: Args


   type: bool

class updateGraphQLSchema(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateGraphQLSchemaInput ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createHeadlines(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      createHeadlines: createHeadlines

   _args: Args


   type: str

class createHeadlinesPerApiId(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      createHeadlines: createHeadlines

   _args: Args


   type: str

class updateHeadlines(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      updateHeadlines: updateHeadlines

   _args: Args


   type: bool

class followIssueV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: IssueFollowInputV2

   _args: Args


   type: Any

class updateKafkaConfiguration(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateKafkaConfigurationInput

   _args: Args


   type: KafkaConfiguration

class subscribeToKafkaTopic(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      apiVersionId: str ##NON NULL
      topicName: str ##NON NULL
      options: SubscribeOptions ##NON NULL

   _args: Args


   type: SubscribeKafkaResponse

class produceKafkaMessage(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      message: ProduceMessageInput ##NON NULL

   _args: Args


   type: list[ProduceMessageResponse]

class postMessage(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      message: MessageCreateInput ##NON NULL

   _args: Args


   type: Any

class postMessageV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      message: MessageCreateInput ##NON NULL

   _args: Args


   type: Any

class updateThreadEntityStatus(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ThreadEntityStatusUpdateInput

   _args: Args


   type: bool

class markNotificationAsViewed(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MarkNewNotificationAsViewedInput

   _args: Args


   type: bool

class markNewNotificationAsRead(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MarkNewNotificationsAsReadInput

   _args: Args


   type: bool

class markNotificationsAsRead(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: MarkNotificationsAsReadInput

   _args: Args


   type: bool

class updateOrganization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: OrganizationUpdateInput ##NON NULL

   _args: Args


   type: Organization

class deleteOrganization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool ##NON NULL

class createOrganization(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: OrganizationCreateInput ##NON NULL

   _args: Args


   type: Organization ##NON NULL

class createNewOrganizationV4(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: CreateNewOrganizationInputV4

   _args: Args


   type: Any

class generateResetPasswordToken(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      email: str ##NON NULL

   _args: Args


   type: Any

class resetUserPassword(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: ResetUserPasswordInput ##NON NULL

   _args: Args


   type: Any

class deletePayoutInfo(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      userId: ID ##NON NULL

   _args: Args


   type: bool ##NON NULL

class addProject(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddProjectInput ##NON NULL

   _args: Args


   type: Project

class addProjectV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: AddProjectInput ##NON NULL

   _args: Args


   type: Project

class editProjectV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: EditProjectInput ##NON NULL

   _args: Args


   type: Any

class deleteProject(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteProjectInput ##NON NULL

   _args: Args


   type: ID

class createProject(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      project: ProjectCreateInput ##NON NULL

   _args: Args


   type: Project

class updateProject(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      project: ProjectUpdateInput ##NON NULL

   _args: Args


   type: list[Project]

class createProjectAllowedAPIs(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: list[createProjectAllowedAPIInput]

   _args: Args


   type: list[ProjectAllowedAPI]

class updateProjectAllowedAPI(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: updateProjectAllowedAPIInput

   _args: Args


   type: ProjectAllowedAPI

class deleteProjectAllowedAPIs(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: deleteProjectAllowedAPIsInput

   _args: Args


   type: bool

class changeApiUsedVersion(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: changeApiUsedVersionInput

   _args: Args


   type: bool

class createRapidReason(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      rapidReasonInput: RapidReasonInput

   _args: Args


   type: ID

class deprecatedUpdateRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      role: RoleUpdateInput ##NON NULL

   _args: Args


   type: Any

class updateRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      role: RoleUpdateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class deprecatedCreateRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      role: RoleCreateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class createRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      role: RoleCreateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class deprecatedDeleteRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      roleId: ID

   _args: Args


   type: Any

class deleteRole(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: list[ID] ##NON NULL

   _args: Args


   type: bool

class createSecretData(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: createSecretDataInput

   _args: Args


   type: Any

class updateBaseUrl(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: updateBaseUrlInput

   _args: Args


   type: bool

class createSpotlight(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      spotlight: SpotlightCreateInput ##NON NULL

   _args: Args


   type: Spotlight ##NON NULL

class updateSpotlight(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      spotlight: SpotlightUpdateInput ##NON NULL

   _args: Args


   type: Spotlight ##NON NULL

class deleteSpotlight(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      spotlight: SpotlightDeleteInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class deleteSubscriptions(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: bool

class deleteSubscription(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool

class createSubscription(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: SubscriptionCreateInput ##NON NULL

   _args: Args


   type: BillingSubscription ##NON NULL

class updateTargetGroups(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      targetGroups: list[TargetGroupUpdateInput] ##NON NULL

   _args: Args


   type: TargetGroup ##NON NULL

class removeTeamUserFromAllOrgTeams(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      orgId: int ##NON NULL
      email: str ##NON NULL

   _args: Args


   type: bool

class updateTeamUser(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: TeamUserUpdateInput

   _args: Args


   type: bool

class updateUserRoles(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UserRolesUpdateInput

   _args: Args


   type: bool

class editTeam(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: EditTeamInput

   _args: Args


   type: bool

class addUserToTeams(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      userId: int ##NON NULL
      teamIds: list[int] ##NON NULL

   _args: Args


   type: bool

class deleteTeam(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool

class createTeam(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: TeamCreateInput ##NON NULL

   _args: Args


   type: Team

class updateTeam(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: TeamUpdateInput ##NON NULL

   _args: Args


   type: Team

class updateTransactions(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: updateTransactionInput

   _args: Args


   type: bool

class createTransformations(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      transformations: list[TransformationCreateInput] ##NON NULL

   _args: Args


   type: Transformation ##NON NULL

class updateTransformations(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      transformations: list[TransformationUpdateInput] ##NON NULL

   _args: Args


   type: Transformation ##NON NULL

class deleteTransformations(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      transformations: list[ID] ##NON NULL

   _args: Args


   type: DeletedTransformation ##NON NULL

class createTutorial(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      tutorial: TutorialCreateInput ##NON NULL

   _args: Args


   type: Tutorial

class updateTutorial(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      tutorial: TutorialUpdateInput ##NON NULL

   _args: Args


   type: Tutorial

class deleteTutorial(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      tutorial: TutorialDeleteInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class phoneAuthSetup(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      phoneNumber: str ##NON NULL

   _args: Args


   type: PhoneVerification

class phoneAuthSetupVerify(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      code: str ##NON NULL
      token: str ##NON NULL

   _args: Args


   type: bool

class authenticateUsingPhone(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      phoneId: ID ##NON NULL

   _args: Args


   type: PhoneVerification

class authenticateUsingPhoneVerify(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      code: str ##NON NULL
      token: str ##NON NULL

   _args: Args


   type: bool

class deletePhoneNumber(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      phoneId: int ##NON NULL

   _args: Args


   type: bool

class generateRecoveryCodes(GQLMutation):
   type: list[RecoveryCode]

class regenerateRecoveryCodes(GQLMutation):
   type: list[RecoveryCode]

class markRecoveryCodeAsUsed(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      code: str ##NON NULL

   _args: Args


   type: bool

class applicationAuthSetup(GQLMutation):
   type: str

class applicationAuthSetupVerify(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      code: str ##NON NULL

   _args: Args


   type: bool

class authenticateUsingApp(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      code: str ##NON NULL

   _args: Args


   type: bool

class deleteApplicationAuth(GQLMutation):
   type: bool

class createUserInvites(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UserInvitesInput

   _args: Args


   type: bool

class createUserInvitesV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UserInvitesCreateInput

   _args: Args


   type: bool

class acceptUserInvite(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      token: str ##NON NULL

   _args: Args


   type: bool

class bulkDeleteUserInvitesV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      emails: list[str]
      orgId: int

   _args: Args


   type: Any

class deleteUserInvites(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UserInvitesDeleteInput ##NON NULL

   _args: Args


   type: Any

class bulkReactivateUserInvitesV2(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      emails: list[str]
      orgId: int

   _args: Args


   type: bool

class reactivateUserInvites(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UserInvitesReactivateInput ##NON NULL

   _args: Args


   type: bool

class inviteUsersToTeams(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      usersToInvite: Any
      orgId: ID ##NON NULL
      meta: Any

   _args: Args


   type: bool

class saveUserApi(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      saveUserApi: SaveUserApi

   _args: Args


   type: UserSavedApi ##NON NULL

class updateUserById(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateUserInput

   _args: Args


   type: Any

class updateUserPassword(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UserPasswordInput

   _args: Args


   type: bool

class deleteAll2faData(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      userId: str ##NON NULL

   _args: Args


   type: Any

class updateUserEmail(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      email: str ##NON NULL

   _args: Args


   type: Any

class verifyEmailCode(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: VerifyEmailCodeInput

   _args: Args


   type: bool

class updateUser(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      input: UserUpdateInput ##NON NULL

   _args: Args


   type: User

class createWorkflow(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      options: CreateWorkflowInput

   _args: Args


   type: Any

class createSignupApprovalWorkflow(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      options: CreateSignupApprovalWorkflowInput

   _args: Args


   type: Any

class updateWorkflows(GQLMutation):
   class Args(GQLArgsSet, GQLObject): 
      options: UpdateWorkflowsInput

   _args: Args


   type: Any


class Mutations(Enum):
   createEventUrl = createEventUrl
   updateEventUrl = updateEventUrl
   deleteEventUrl = deleteEventUrl
   upsertEventConfig = upsertEventConfig
   deleteEventConfig = deleteEventConfig
   createGatewayInstance = createGatewayInstance
   updateGatewayInstance = updateGatewayInstance
   deleteGatewayInstance = deleteGatewayInstance
   createGatewayTemplate = createGatewayTemplate
   updateGatewayTemplate = updateGatewayTemplate
   deleteGatewayTemplate = deleteGatewayTemplate
   createGatewayTemplateParam = createGatewayTemplateParam
   updateEnvConfig = updateEnvConfig
   resetEnvConfig = resetEnvConfig
   addUserAlert = addUserAlert
   deleteUserAlerts = deleteUserAlerts
   editUserAlert = editUserAlert
   updateUserAlerts = updateUserAlerts
   createApiCertificates = createApiCertificates
   deleteApiCertificates = deleteApiCertificates
   saveApiDevelopersToApi = saveApiDevelopersToApi
   copyApiDevelopersFromVersion = copyApiDevelopersFromVersion
   createApiFavorites = createApiFavorites
   deleteApiFavorites = deleteApiFavorites
   createApiFollowers = createApiFollowers
   deleteApiFollowers = deleteApiFollowers
   createApisFromSpecs = createApisFromSpecs
   updateApisFromSpecs = updateApisFromSpecs
   createApisFromRapidOas = createApisFromRapidOas
   updateApisFromRapidOas = updateApisFromRapidOas
   createApiVersions = createApiVersions
   createGqlApiVersions = createGqlApiVersions
   updateApiVersions = updateApiVersions
   createApiVersionBillingPlanVersion = createApiVersionBillingPlanVersion
   createApi = createApi
   updateApi = updateApi
   provisionSwaggerFiles = provisionSwaggerFiles
   deleteApi = deleteApi
   createApplicationAuthorization = createApplicationAuthorization
   updateApplicationAuthorization = updateApplicationAuthorization
   deleteApplicationAuthorization = deleteApplicationAuthorization
   addApplicationEnvironmentKey = addApplicationEnvironmentKey
   editApplicationEnvironmentKey = editApplicationEnvironmentKey
   deleteApplicationEnvironmentKey = deleteApplicationEnvironmentKey
   generateAssetUploadUrl = generateAssetUploadUrl
   deleteAsset = deleteAsset
   updateAssetUploaded = updateAssetUploaded
   updateAsset = updateAsset
   upsertAsyncApiConfiguration = upsertAsyncApiConfiguration
   upsertUserAttributes = upsertUserAttributes
   updateUserAttributeItem = updateUserAttributeItem
   createAuthentications = createAuthentications
   updateAuthentications = updateAuthentications
   createOrUpdateAPIVersionAuthentication = createOrUpdateAPIVersionAuthentication
   createBillingFeature = createBillingFeature
   updateBillingFeature = updateBillingFeature
   upsertBillingFeature = upsertBillingFeature
   deleteBillingFeature = deleteBillingFeature
   deleteBillingFeatures = deleteBillingFeatures
   createStripeCustomer = createStripeCustomer
   updateStripeCustomer = updateStripeCustomer
   createStripeCustomerV2 = createStripeCustomerV2
   updateStripeCustomerV2 = updateStripeCustomerV2
   deleteCustomerPaymentMethod = deleteCustomerPaymentMethod
   upsertBillingItem = upsertBillingItem
   deleteBillingItem = deleteBillingItem
   deleteBillingItems = deleteBillingItems
   deleteBillingPlans = deleteBillingPlans
   updateAllowedPlanDevelopers = updateAllowedPlanDevelopers
   editOrganizationInvoice = editOrganizationInvoice
   createBillingPlan = createBillingPlan
   updateBillingPlanMetadata = updateBillingPlanMetadata
   updateBillingPlanExtended = updateBillingPlanExtended
   upsertBillingPlanAndVersion = upsertBillingPlanAndVersion
   blockUsers = blockUsers
   unblockUsers = unblockUsers
   createCategory = createCategory
   updateCategory = updateCategory
   deleteCategories = deleteCategories
   deleteCollection = deleteCollection
   updateCollection = updateCollection
   createCollection = createCollection
   bulkUpdateCollections = bulkUpdateCollections
   updateCollections = updateCollections
   postCommentV2 = postCommentV2
   deleteCommentV2 = deleteCommentV2
   updateCommentV2 = updateCommentV2
   postCommentV3 = postCommentV3
   subscribeToPlan = subscribeToPlan
   unfollowUser = unfollowUser
   followUser = followUser
   followApi = followApi
   unfollowApi = unfollowApi
   sendMessage = sendMessage
   rateApi = rateApi
   upsertEntityMetadataBulk = upsertEntityMetadataBulk
   upsertEntityMetadata = upsertEntityMetadata
   deleteIssueV2 = deleteIssueV2
   updateIssueV2 = updateIssueV2
   deleteIssues = deleteIssues
   postIssueV3 = postIssueV3
   updateOrCreateEndpointWithParameters = updateOrCreateEndpointWithParameters
   updateEndpointEntity = updateEndpointEntity
   deleteEndpoint = deleteEndpoint
   deleteEndpoints = deleteEndpoints
   updateEndpointsCollectionOrder = updateEndpointsCollectionOrder
   createEndpointsGroups = createEndpointsGroups
   updateEndpointsGroups = updateEndpointsGroups
   deleteEndpointsGroups = deleteEndpointsGroups
   duplicateNameCheck = duplicateNameCheck
   createEntityMetadata = createEntityMetadata
   updateEntityMetadata = updateEntityMetadata
   createEntitiesRoles = createEntitiesRoles
   upsertEntityRole = upsertEntityRole
   updateGraphQLSchema = updateGraphQLSchema
   createHeadlines = createHeadlines
   createHeadlinesPerApiId = createHeadlinesPerApiId
   updateHeadlines = updateHeadlines
   followIssueV2 = followIssueV2
   updateKafkaConfiguration = updateKafkaConfiguration
   subscribeToKafkaTopic = subscribeToKafkaTopic
   produceKafkaMessage = produceKafkaMessage
   postMessage = postMessage
   postMessageV2 = postMessageV2
   updateThreadEntityStatus = updateThreadEntityStatus
   markNotificationAsViewed = markNotificationAsViewed
   markNewNotificationAsRead = markNewNotificationAsRead
   markNotificationsAsRead = markNotificationsAsRead
   updateOrganization = updateOrganization
   deleteOrganization = deleteOrganization
   createOrganization = createOrganization
   createNewOrganizationV4 = createNewOrganizationV4
   generateResetPasswordToken = generateResetPasswordToken
   resetUserPassword = resetUserPassword
   deletePayoutInfo = deletePayoutInfo
   addProject = addProject
   addProjectV2 = addProjectV2
   editProjectV2 = editProjectV2
   deleteProject = deleteProject
   createProject = createProject
   updateProject = updateProject
   createProjectAllowedAPIs = createProjectAllowedAPIs
   updateProjectAllowedAPI = updateProjectAllowedAPI
   deleteProjectAllowedAPIs = deleteProjectAllowedAPIs
   changeApiUsedVersion = changeApiUsedVersion
   createRapidReason = createRapidReason
   deprecatedUpdateRole = deprecatedUpdateRole
   updateRole = updateRole
   deprecatedCreateRole = deprecatedCreateRole
   createRole = createRole
   deprecatedDeleteRole = deprecatedDeleteRole
   deleteRole = deleteRole
   createSecretData = createSecretData
   updateBaseUrl = updateBaseUrl
   createSpotlight = createSpotlight
   updateSpotlight = updateSpotlight
   deleteSpotlight = deleteSpotlight
   deleteSubscriptions = deleteSubscriptions
   deleteSubscription = deleteSubscription
   createSubscription = createSubscription
   updateTargetGroups = updateTargetGroups
   removeTeamUserFromAllOrgTeams = removeTeamUserFromAllOrgTeams
   updateTeamUser = updateTeamUser
   updateUserRoles = updateUserRoles
   editTeam = editTeam
   addUserToTeams = addUserToTeams
   deleteTeam = deleteTeam
   createTeam = createTeam
   updateTeam = updateTeam
   updateTransactions = updateTransactions
   createTransformations = createTransformations
   updateTransformations = updateTransformations
   deleteTransformations = deleteTransformations
   createTutorial = createTutorial
   updateTutorial = updateTutorial
   deleteTutorial = deleteTutorial
   phoneAuthSetup = phoneAuthSetup
   phoneAuthSetupVerify = phoneAuthSetupVerify
   authenticateUsingPhone = authenticateUsingPhone
   authenticateUsingPhoneVerify = authenticateUsingPhoneVerify
   deletePhoneNumber = deletePhoneNumber
   generateRecoveryCodes = generateRecoveryCodes
   regenerateRecoveryCodes = regenerateRecoveryCodes
   markRecoveryCodeAsUsed = markRecoveryCodeAsUsed
   applicationAuthSetup = applicationAuthSetup
   applicationAuthSetupVerify = applicationAuthSetupVerify
   authenticateUsingApp = authenticateUsingApp
   deleteApplicationAuth = deleteApplicationAuth
   createUserInvites = createUserInvites
   createUserInvitesV2 = createUserInvitesV2
   acceptUserInvite = acceptUserInvite
   bulkDeleteUserInvitesV2 = bulkDeleteUserInvitesV2
   deleteUserInvites = deleteUserInvites
   bulkReactivateUserInvitesV2 = bulkReactivateUserInvitesV2
   reactivateUserInvites = reactivateUserInvites
   inviteUsersToTeams = inviteUsersToTeams
   saveUserApi = saveUserApi
   updateUserById = updateUserById
   updateUserPassword = updateUserPassword
   deleteAll2faData = deleteAll2faData
   updateUserEmail = updateUserEmail
   verifyEmailCode = verifyEmailCode
   updateUser = updateUser
   createWorkflow = createWorkflow
   createSignupApprovalWorkflow = createSignupApprovalWorkflow
   updateWorkflows = updateWorkflows
