from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class createEventUrl(GQLObject):
   class Args(): 
      createDto: EventUrlCreateInput ##NON NULL

   _args: Args


   type: EventUrl ##NON NULL

class updateEventUrl(GQLObject):
   class Args(): 
      id: ID ##NON NULL
      updateDto: EventUrlUpdateInput ##NON NULL

   _args: Args


   type: EventUrl ##NON NULL

class deleteEventUrl(GQLObject):
   class Args(): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class upsertEventConfig(GQLObject):
   class Args(): 
      input: EventConfigUpdateInput ##NON NULL

   _args: Args


   type: EventConfig ##NON NULL

class deleteEventConfig(GQLObject):
   class Args(): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayInstance(GQLObject):
   class Args(): 
      createDto: GatewayInstanceCreateInput ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class updateGatewayInstance(GQLObject):
   class Args(): 
      updateDto: GatewayInstanceUpdateInput ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class deleteGatewayInstance(GQLObject):
   class Args(): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayTemplate(GQLObject):
   class Args(): 
      createDto: GatewayTemplateCreateInput ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class updateGatewayTemplate(GQLObject):
   class Args(): 
      updateDto: GatewayTemplateUpdateInput ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class deleteGatewayTemplate(GQLObject):
   class Args(): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayTemplateParam(GQLObject):
   class Args(): 
      createDto: GatewayTemplateParamsCreateInput ##NON NULL

   _args: Args


   type: GatewayTemplateParam ##NON NULL

class updateEnvConfig(GQLObject):
   class Args(): 
      envConfig: EnvConfigUpdateInput ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class resetEnvConfig(GQLObject):
   class Args(): 
      id: int ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class addUserAlert(GQLObject):
   class Args(): 
      input: addUserAlertInput

   _args: Args


   type: UserAlert ##NON NULL

class deleteUserAlerts(GQLObject):
   class Args(): 
      input: deleteUserAlertsInput ##NON NULL

   _args: Args


   type: ID ##NON NULL

class editUserAlert(GQLObject):
   class Args(): 
      input: editUserAlertInput ##NON NULL

   _args: Args


   type: UserAlert ##NON NULL

class updateUserAlerts(GQLObject):
   class Args(): 
      input: list[UserAlertUpdateInput] ##NON NULL

   _args: Args


   type: UserAlert ##NON NULL

class createApiCertificates(GQLObject):
   class Args(): 
      certificates: list[ApiCertificateCreateInput] ##NON NULL

   _args: Args


   type: ApiCertificateCreationResult ##NON NULL

deleteApiCertificates = bool

saveApiDevelopersToApi = bool

copyApiDevelopersFromVersion = bool

createApiFavorites = bool

deleteApiFavorites = bool

class createApiFollowers(GQLObject):
   class Args(): 
      apiFollowers: ApiFollowerCreateInput ##NON NULL

   _args: Args


   type: ApiFollower ##NON NULL

deleteApiFollowers = bool

class createApisFromSpecs(GQLObject):
   class Args(): 
      creations: list[ApiCreateFromSpecInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class updateApisFromSpecs(GQLObject):
   class Args(): 
      updates: list[ApiUpdateFromSpecInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class createApisFromRapidOas(GQLObject):
   class Args(): 
      creations: list[ApiCreateFromRapidOasInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class updateApisFromRapidOas(GQLObject):
   class Args(): 
      updates: list[ApiUpdateFromRapidOasInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class createApiVersions(GQLObject):
   class Args(): 
      apiVersions: list[ApiVersionCreateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class createGqlApiVersions(GQLObject):
   class Args(): 
      gqlApiVersions: list[GqlApiVersionCreateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class updateApiVersions(GQLObject):
   class Args(): 
      apiVersions: list[ApiVersionUpdateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class createApiVersionBillingPlanVersion(GQLObject):
   class Args(): 
      input: createApiVersionBillingPlanVersionInput

   _args: Args


   type: ApiVersionBillingPlanVersion

class createApi(GQLObject):
   class Args(): 
      api: ApiCreateInput ##NON NULL

   _args: Args


   type: Api ##NON NULL

class updateApi(GQLObject):
   class Args(): 
      api: ApiUpdateInput ##NON NULL

   _args: Args


   type: Api ##NON NULL

provisionSwaggerFiles = list[str]

deleteApi = bool

class createApplicationAuthorization(GQLObject):
   class Args(): 
      input: AppAuthorizationCreateInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class updateApplicationAuthorization(GQLObject):
   class Args(): 
      input: AppAuthorizationUpdateInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

deleteApplicationAuthorization = bool

class addApplicationEnvironmentKey(GQLObject):
   class Args(): 
      input: AddApplicationEnvironmentKeyInput ##NON NULL

   _args: Args


   type: Any

class editApplicationEnvironmentKey(GQLObject):
   class Args(): 
      input: EditApplicationEnviornmentKeyInput ##NON NULL

   _args: Args


   type: Any

class deleteApplicationEnvironmentKey(GQLObject):
   class Args(): 
      input: DeleteApplicationEnvironmentKeyInput ##NON NULL

   _args: Args


   type: ID

class generateAssetUploadUrl(GQLObject):
   class Args(): 
      input: GenerateAssetUploadUrlInput ##NON NULL

   _args: Args


   type: Asset ##NON NULL

deleteAsset = bool

class updateAssetUploaded(GQLObject):
   class Args(): 
      id: ID ##NON NULL

   _args: Args


   type: Asset

class updateAsset(GQLObject):
   class Args(): 
      input: AssetUpdateInput ##NON NULL

   _args: Args


   type: Asset

class upsertAsyncApiConfiguration(GQLObject):
   class Args(): 
      asyncApiConfigurations: list[AsyncApiConfigurationCreateInput] ##NON NULL

   _args: Args


   type: AsyncApiConfiguration ##NON NULL

class upsertUserAttributes(GQLObject):
   class Args(): 
      input: UserAttributesInput

   _args: Args


   type: Any

class updateUserAttributeItem(GQLObject):
   class Args(): 
      input: ThemeUserAttributesInput ##NON NULL

   _args: Args


   type: Any

class createAuthentications(GQLObject):
   class Args(): 
      authentications: list[AuthenticationCreateInput] ##NON NULL

   _args: Args


   type: Authentication ##NON NULL

class updateAuthentications(GQLObject):
   class Args(): 
      authentications: list[AuthenticationUpdateInput] ##NON NULL

   _args: Args


   type: Authentication ##NON NULL

class createOrUpdateAPIVersionAuthentication(GQLObject):
   class Args(): 
      input: createAuthenticationInput

   _args: Args


   type: AuthenticationCreateOrUpdateResult

class createBillingFeature(GQLObject):
   class Args(): 
      createBillingFeature: createBillingFeature

   _args: Args


   type: BillingFeature

class updateBillingFeature(GQLObject):
   class Args(): 
      updateBillingFeature: updateBillingFeature

   _args: Args


   type: BillingFeature

class upsertBillingFeature(GQLObject):
   class Args(): 
      upsertBillingFeature: upsertBillingFeatureInput ##NON NULL

   _args: Args


   type: BillingFeature

class deleteBillingFeature(GQLObject):
   class Args(): 
      billingFeatureId: str

   _args: Args


   type: Any

class deleteBillingFeatures(GQLObject):
   class Args(): 
      billingFeatureIds: list[str]

   _args: Args


   type: Any

class createStripeCustomer(GQLObject):
   class Args(): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class updateStripeCustomer(GQLObject):
   class Args(): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class createStripeCustomerV2(GQLObject):
   class Args(): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class updateStripeCustomerV2(GQLObject):
   class Args(): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

deleteCustomerPaymentMethod = bool

class upsertBillingItem(GQLObject):
   class Args(): 
      input: BillingItemUpsertInput ##NON NULL

   _args: Args


   type: BillingItem

class deleteBillingItem(GQLObject):
   class Args(): 
      id: ID ##NON NULL

   _args: Args


   type: Any

deleteBillingItems = bool

deleteBillingPlans = bool

updateAllowedPlanDevelopers = list[AllowedPlanDeveloper]

editOrganizationInvoice = bool

class createBillingPlan(GQLObject):
   class Args(): 
      billingPlan: BillingPlanCreateInput ##NON NULL

   _args: Args


   type: BillingPlan

class updateBillingPlanMetadata(GQLObject):
   class Args(): 
      billingPlan: BillingPlanMetadataUpdateInput ##NON NULL

   _args: Args


   type: BillingPlan

class updateBillingPlanExtended(GQLObject):
   class Args(): 
      billingPlan: BillingPlanExtendedUpdateInput ##NON NULL

   _args: Args


   type: BillingPlan

class upsertBillingPlanAndVersion(GQLObject):
   class Args(): 
      upsertBillingPlanAndVersionInput: upsertBillingPlanAndVersionInput ##NON NULL

   _args: Args


   type: BillingPlanVersion

blockUsers = bool

unblockUsers = bool

class createCategory(GQLObject):
   class Args(): 
      category: CategoryCreateInput ##NON NULL

   _args: Args


   type: Category ##NON NULL

class updateCategory(GQLObject):
   class Args(): 
      category: CategoryUpdateInput ##NON NULL

   _args: Args


   type: Category ##NON NULL

class deleteCategories(GQLObject):
   class Args(): 
      categories: list[ID] ##NON NULL

   _args: Args


   type: DeletedCategory ##NON NULL

deleteCollection = bool

class updateCollection(GQLObject):
   class Args(): 
      input: CollectionUpdateInput ##NON NULL

   _args: Args


   type: Collection

class createCollection(GQLObject):
   class Args(): 
      input: CollectionCreateInput ##NON NULL

   _args: Args


   type: Collection

bulkUpdateCollections = list[Collection]

updateCollections = list[Collection]

class postCommentV2(GQLObject):
   class Args(): 
      input: CommentCreateInput

   _args: Args


   type: Comment

class deleteCommentV2(GQLObject):
   class Args(): 
      input: CommentDeleteInput

   _args: Args


   type: Any

class updateCommentV2(GQLObject):
   class Args(): 
      input: CommentUpdateInput

   _args: Args


   type: Any

class postCommentV3(GQLObject):
   class Args(): 
      input: CommentCreateInput

   _args: Args


   type: Comment

class subscribeToPlan(GQLObject):
   class Args(): 
      input: SubscribeInput

   _args: Args


   type: BillingSubscription

unfollowUser = bool

followUser = bool

followApi = bool

unfollowApi = bool

sendMessage = bool

class rateApi(GQLObject):
   class Args(): 
      input: RatingInput

   _args: Args


   type: Any

class upsertEntityMetadataBulk(GQLObject):
   class Args(): 
      entityId: ID
      entityAttributes: list[EntityAttribute] ##NON NULL

   _args: Args


   type: Any

class upsertEntityMetadata(GQLObject):
   class Args(): 
      entityMetadata: EntityMetadataInput

   _args: Args


   type: Any

class deleteIssueV2(GQLObject):
   class Args(): 
      input: IssueDeleteInput

   _args: Args


   type: Any

class updateIssueV2(GQLObject):
   class Args(): 
      input: IssueUpdateInput

   _args: Args


   type: Any

class deleteIssues(GQLObject):
   class Args(): 
      input: IssuesDeleteInput

   _args: Args


   type: Any

class postIssueV3(GQLObject):
   class Args(): 
      input: IssueCreateInputV2

   _args: Args


   type: Any

class updateOrCreateEndpointWithParameters(GQLObject):
   class Args(): 
      input: updateOrCreateEndpointWithParameters

   _args: Args


   type: Any

class updateEndpointEntity(GQLObject):
   class Args(): 
      input: updateEndpointEntity

   _args: Args


   type: Any

class deleteEndpoint(GQLObject):
   class Args(): 
      endpointId: str

   _args: Args


   type: Any

class deleteEndpoints(GQLObject):
   class Args(): 
      endpointIds: list[str]

   _args: Args


   type: Any

class updateEndpointsCollectionOrder(GQLObject):
   class Args(): 
      endpointsCollectionOrder: list[EndpointOrder]

   _args: Args


   type: Any

class createEndpointsGroups(GQLObject):
   class Args(): 
      groups: list[EndpointsGroupCreateInput] ##NON NULL

   _args: Args


   type: EndpointsGroup ##NON NULL

class updateEndpointsGroups(GQLObject):
   class Args(): 
      groups: list[EndpointsGroupUpdateInput] ##NON NULL

   _args: Args


   type: EndpointsGroup ##NON NULL

class deleteEndpointsGroups(GQLObject):
   class Args(): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: ID ##NON NULL

duplicateNameCheck = bool

createEntityMetadata = bool

updateEntityMetadata = bool

createEntitiesRoles = bool

upsertEntityRole = bool

class updateGraphQLSchema(GQLObject):
   class Args(): 
      input: UpdateGraphQLSchemaInput ##NON NULL

   _args: Args


   type: ID ##NON NULL

createHeadlines = str

createHeadlinesPerApiId = str

updateHeadlines = bool

class followIssueV2(GQLObject):
   class Args(): 
      input: IssueFollowInputV2

   _args: Args


   type: Any

class updateKafkaConfiguration(GQLObject):
   class Args(): 
      input: UpdateKafkaConfigurationInput

   _args: Args


   type: KafkaConfiguration

class subscribeToKafkaTopic(GQLObject):
   class Args(): 
      apiVersionId: str ##NON NULL
      topicName: str ##NON NULL
      options: SubscribeOptions ##NON NULL

   _args: Args


   type: SubscribeKafkaResponse

produceKafkaMessage = list[ProduceMessageResponse]

class postMessage(GQLObject):
   class Args(): 
      message: MessageCreateInput ##NON NULL

   _args: Args


   type: Any

class postMessageV2(GQLObject):
   class Args(): 
      message: MessageCreateInput ##NON NULL

   _args: Args


   type: Any

updateThreadEntityStatus = bool

markNotificationAsViewed = bool

markNewNotificationAsRead = bool

markNotificationsAsRead = bool

class updateOrganization(GQLObject):
   class Args(): 
      input: OrganizationUpdateInput ##NON NULL

   _args: Args


   type: Organization

deleteOrganization = bool

class createOrganization(GQLObject):
   class Args(): 
      input: OrganizationCreateInput ##NON NULL

   _args: Args


   type: Organization ##NON NULL

class createNewOrganizationV4(GQLObject):
   class Args(): 
      input: CreateNewOrganizationInputV4

   _args: Args


   type: Any

class generateResetPasswordToken(GQLObject):
   class Args(): 
      email: str ##NON NULL

   _args: Args


   type: Any

class resetUserPassword(GQLObject):
   class Args(): 
      input: ResetUserPasswordInput ##NON NULL

   _args: Args


   type: Any

deletePayoutInfo = bool

class addProject(GQLObject):
   class Args(): 
      input: AddProjectInput ##NON NULL

   _args: Args


   type: Project

class addProjectV2(GQLObject):
   class Args(): 
      input: AddProjectInput ##NON NULL

   _args: Args


   type: Project

class editProjectV2(GQLObject):
   class Args(): 
      input: EditProjectInput ##NON NULL

   _args: Args


   type: Any

class deleteProject(GQLObject):
   class Args(): 
      input: DeleteProjectInput ##NON NULL

   _args: Args


   type: ID

class createProject(GQLObject):
   class Args(): 
      project: ProjectCreateInput ##NON NULL

   _args: Args


   type: Project

updateProject = list[Project]

createProjectAllowedAPIs = list[ProjectAllowedAPI]

class updateProjectAllowedAPI(GQLObject):
   class Args(): 
      input: updateProjectAllowedAPIInput

   _args: Args


   type: ProjectAllowedAPI

deleteProjectAllowedAPIs = bool

changeApiUsedVersion = bool

class createRapidReason(GQLObject):
   class Args(): 
      rapidReasonInput: RapidReasonInput

   _args: Args


   type: ID

class deprecatedUpdateRole(GQLObject):
   class Args(): 
      role: RoleUpdateInput ##NON NULL

   _args: Args


   type: Any

class updateRole(GQLObject):
   class Args(): 
      role: RoleUpdateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class deprecatedCreateRole(GQLObject):
   class Args(): 
      role: RoleCreateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class createRole(GQLObject):
   class Args(): 
      role: RoleCreateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class deprecatedDeleteRole(GQLObject):
   class Args(): 
      roleId: ID

   _args: Args


   type: Any

deleteRole = bool

class createSecretData(GQLObject):
   class Args(): 
      input: createSecretDataInput

   _args: Args


   type: Any

updateBaseUrl = bool

class createSpotlight(GQLObject):
   class Args(): 
      spotlight: SpotlightCreateInput ##NON NULL

   _args: Args


   type: Spotlight ##NON NULL

class updateSpotlight(GQLObject):
   class Args(): 
      spotlight: SpotlightUpdateInput ##NON NULL

   _args: Args


   type: Spotlight ##NON NULL

deleteSpotlight = bool

deleteSubscriptions = bool

deleteSubscription = bool

class createSubscription(GQLObject):
   class Args(): 
      input: SubscriptionCreateInput ##NON NULL

   _args: Args


   type: BillingSubscription ##NON NULL

class updateTargetGroups(GQLObject):
   class Args(): 
      targetGroups: list[TargetGroupUpdateInput] ##NON NULL

   _args: Args


   type: TargetGroup ##NON NULL

removeTeamUserFromAllOrgTeams = bool

updateTeamUser = bool

updateUserRoles = bool

editTeam = bool

addUserToTeams = bool

deleteTeam = bool

class createTeam(GQLObject):
   class Args(): 
      input: TeamCreateInput ##NON NULL

   _args: Args


   type: Team

class updateTeam(GQLObject):
   class Args(): 
      input: TeamUpdateInput ##NON NULL

   _args: Args


   type: Team

updateTransactions = bool

class createTransformations(GQLObject):
   class Args(): 
      transformations: list[TransformationCreateInput] ##NON NULL

   _args: Args


   type: Transformation ##NON NULL

class updateTransformations(GQLObject):
   class Args(): 
      transformations: list[TransformationUpdateInput] ##NON NULL

   _args: Args


   type: Transformation ##NON NULL

class deleteTransformations(GQLObject):
   class Args(): 
      transformations: list[ID] ##NON NULL

   _args: Args


   type: DeletedTransformation ##NON NULL

class createTutorial(GQLObject):
   class Args(): 
      tutorial: TutorialCreateInput ##NON NULL

   _args: Args


   type: Tutorial

class updateTutorial(GQLObject):
   class Args(): 
      tutorial: TutorialUpdateInput ##NON NULL

   _args: Args


   type: Tutorial

deleteTutorial = bool

class phoneAuthSetup(GQLObject):
   class Args(): 
      phoneNumber: str ##NON NULL

   _args: Args


   type: PhoneVerification

phoneAuthSetupVerify = bool

class authenticateUsingPhone(GQLObject):
   class Args(): 
      phoneId: ID ##NON NULL

   _args: Args


   type: PhoneVerification

authenticateUsingPhoneVerify = bool

deletePhoneNumber = bool

generateRecoveryCodes = list[RecoveryCode]

regenerateRecoveryCodes = list[RecoveryCode]

markRecoveryCodeAsUsed = bool

applicationAuthSetup = str

applicationAuthSetupVerify = bool

authenticateUsingApp = bool

deleteApplicationAuth = bool

createUserInvites = bool

createUserInvitesV2 = bool

acceptUserInvite = bool

class bulkDeleteUserInvitesV2(GQLObject):
   class Args(): 
      emails: list[str]
      orgId: int

   _args: Args


   type: Any

class deleteUserInvites(GQLObject):
   class Args(): 
      input: UserInvitesDeleteInput ##NON NULL

   _args: Args


   type: Any

bulkReactivateUserInvitesV2 = bool

reactivateUserInvites = bool

inviteUsersToTeams = bool

class saveUserApi(GQLObject):
   class Args(): 
      saveUserApi: SaveUserApi

   _args: Args


   type: UserSavedApi ##NON NULL

class updateUserById(GQLObject):
   class Args(): 
      input: UpdateUserInput

   _args: Args


   type: Any

updateUserPassword = bool

class deleteAll2faData(GQLObject):
   class Args(): 
      userId: str ##NON NULL

   _args: Args


   type: Any

class updateUserEmail(GQLObject):
   class Args(): 
      email: str ##NON NULL

   _args: Args


   type: Any

verifyEmailCode = bool

class updateUser(GQLObject):
   class Args(): 
      input: UserUpdateInput ##NON NULL

   _args: Args


   type: User

class createWorkflow(GQLObject):
   class Args(): 
      options: CreateWorkflowInput

   _args: Args


   type: Any

class createSignupApprovalWorkflow(GQLObject):
   class Args(): 
      options: CreateSignupApprovalWorkflowInput

   _args: Args


   type: Any

class updateWorkflows(GQLObject):
   class Args(): 
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
