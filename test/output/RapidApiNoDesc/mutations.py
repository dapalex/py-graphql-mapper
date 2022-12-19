from pygqlmap.components import GQLOperationArgs, GQLMutation
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *


class createEventUrl(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      createDto: EventUrlCreateInput ##NON NULL

   _args: Args


   type: EventUrl ##NON NULL

class updateEventUrl(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL
      updateDto: EventUrlUpdateInput ##NON NULL

   _args: Args


   type: EventUrl ##NON NULL

class deleteEventUrl(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class upsertEventConfig(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: EventConfigUpdateInput ##NON NULL

   _args: Args


   type: EventConfig ##NON NULL

class deleteEventConfig(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayInstance(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      createDto: GatewayInstanceCreateInput ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class updateGatewayInstance(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      updateDto: GatewayInstanceUpdateInput ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class deleteGatewayInstance(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayTemplate(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      createDto: GatewayTemplateCreateInput ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class updateGatewayTemplate(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      updateDto: GatewayTemplateUpdateInput ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class deleteGatewayTemplate(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayTemplateParam(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      createDto: GatewayTemplateParamsCreateInput ##NON NULL

   _args: Args


   type: GatewayTemplateParam ##NON NULL

class updateEnvConfig(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      envConfig: EnvConfigUpdateInput ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class resetEnvConfig(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      id: int ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class addUserAlert(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: addUserAlertInput

   _args: Args


   type: UserAlert ##NON NULL

class deleteUserAlerts(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: deleteUserAlertsInput ##NON NULL

   _args: Args


   type: ID ##NON NULL

class editUserAlert(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: editUserAlertInput ##NON NULL

   _args: Args


   type: UserAlert ##NON NULL

class updateUserAlerts(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: list[UserAlertUpdateInput] ##NON NULL

   _args: Args


   type: UserAlert ##NON NULL

class createApiCertificates(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      certificates: list[ApiCertificateCreateInput] ##NON NULL

   _args: Args


   type: ApiCertificateCreationResult ##NON NULL

deleteApiCertificates = bool

saveApiDevelopersToApi = bool

copyApiDevelopersFromVersion = bool

createApiFavorites = bool

deleteApiFavorites = bool

class createApiFollowers(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      apiFollowers: ApiFollowerCreateInput ##NON NULL

   _args: Args


   type: ApiFollower ##NON NULL

deleteApiFollowers = bool

class createApisFromSpecs(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      creations: list[ApiCreateFromSpecInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class updateApisFromSpecs(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      updates: list[ApiUpdateFromSpecInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class createApisFromRapidOas(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      creations: list[ApiCreateFromRapidOasInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class updateApisFromRapidOas(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      updates: list[ApiUpdateFromRapidOasInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class createApiVersions(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      apiVersions: list[ApiVersionCreateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class createGqlApiVersions(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      gqlApiVersions: list[GqlApiVersionCreateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class updateApiVersions(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      apiVersions: list[ApiVersionUpdateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class createApiVersionBillingPlanVersion(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: createApiVersionBillingPlanVersionInput

   _args: Args


   type: ApiVersionBillingPlanVersion

class createApi(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      api: ApiCreateInput ##NON NULL

   _args: Args


   type: Api ##NON NULL

class updateApi(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      api: ApiUpdateInput ##NON NULL

   _args: Args


   type: Api ##NON NULL

provisionSwaggerFiles = list[str]

deleteApi = bool

class createApplicationAuthorization(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: AppAuthorizationCreateInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class updateApplicationAuthorization(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: AppAuthorizationUpdateInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

deleteApplicationAuthorization = bool

class addApplicationEnvironmentKey(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: AddApplicationEnvironmentKeyInput ##NON NULL

   _args: Args


   type: Any

class editApplicationEnvironmentKey(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: EditApplicationEnviornmentKeyInput ##NON NULL

   _args: Args


   type: Any

class deleteApplicationEnvironmentKey(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: DeleteApplicationEnvironmentKeyInput ##NON NULL

   _args: Args


   type: ID

class generateAssetUploadUrl(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: GenerateAssetUploadUrlInput ##NON NULL

   _args: Args


   type: Asset ##NON NULL

deleteAsset = bool

class updateAssetUploaded(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Asset

class updateAsset(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: AssetUpdateInput ##NON NULL

   _args: Args


   type: Asset

class upsertAsyncApiConfiguration(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      asyncApiConfigurations: list[AsyncApiConfigurationCreateInput] ##NON NULL

   _args: Args


   type: AsyncApiConfiguration ##NON NULL

class upsertUserAttributes(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: UserAttributesInput

   _args: Args


   type: Any

class updateUserAttributeItem(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: ThemeUserAttributesInput ##NON NULL

   _args: Args


   type: Any

class createAuthentications(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      authentications: list[AuthenticationCreateInput] ##NON NULL

   _args: Args


   type: Authentication ##NON NULL

class updateAuthentications(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      authentications: list[AuthenticationUpdateInput] ##NON NULL

   _args: Args


   type: Authentication ##NON NULL

class createOrUpdateAPIVersionAuthentication(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: createAuthenticationInput

   _args: Args


   type: AuthenticationCreateOrUpdateResult

class createBillingFeature(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      createBillingFeature: createBillingFeature

   _args: Args


   type: BillingFeature

class updateBillingFeature(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      updateBillingFeature: updateBillingFeature

   _args: Args


   type: BillingFeature

class upsertBillingFeature(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      upsertBillingFeature: upsertBillingFeatureInput ##NON NULL

   _args: Args


   type: BillingFeature

class deleteBillingFeature(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      billingFeatureId: str

   _args: Args


   type: Any

class deleteBillingFeatures(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      billingFeatureIds: list[str]

   _args: Args


   type: Any

class createStripeCustomer(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class updateStripeCustomer(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class createStripeCustomerV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class updateStripeCustomerV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

deleteCustomerPaymentMethod = bool

class upsertBillingItem(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: BillingItemUpsertInput ##NON NULL

   _args: Args


   type: BillingItem

class deleteBillingItem(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Any

deleteBillingItems = bool

deleteBillingPlans = bool

updateAllowedPlanDevelopers = list[AllowedPlanDeveloper]

editOrganizationInvoice = bool

class createBillingPlan(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      billingPlan: BillingPlanCreateInput ##NON NULL

   _args: Args


   type: BillingPlan

class updateBillingPlanMetadata(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      billingPlan: BillingPlanMetadataUpdateInput ##NON NULL

   _args: Args


   type: BillingPlan

class updateBillingPlanExtended(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      billingPlan: BillingPlanExtendedUpdateInput ##NON NULL

   _args: Args


   type: BillingPlan

class upsertBillingPlanAndVersion(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      upsertBillingPlanAndVersionInput: upsertBillingPlanAndVersionInput ##NON NULL

   _args: Args


   type: BillingPlanVersion

blockUsers = bool

unblockUsers = bool

class createCategory(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      category: CategoryCreateInput ##NON NULL

   _args: Args


   type: Category ##NON NULL

class updateCategory(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      category: CategoryUpdateInput ##NON NULL

   _args: Args


   type: Category ##NON NULL

class deleteCategories(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      categories: list[ID] ##NON NULL

   _args: Args


   type: DeletedCategory ##NON NULL

deleteCollection = bool

class updateCollection(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CollectionUpdateInput ##NON NULL

   _args: Args


   type: Collection

class createCollection(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CollectionCreateInput ##NON NULL

   _args: Args


   type: Collection

bulkUpdateCollections = list[Collection]

updateCollections = list[Collection]

class postCommentV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CommentCreateInput

   _args: Args


   type: Comment

class deleteCommentV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CommentDeleteInput

   _args: Args


   type: Any

class updateCommentV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CommentUpdateInput

   _args: Args


   type: Any

class postCommentV3(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CommentCreateInput

   _args: Args


   type: Comment

class subscribeToPlan(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: SubscribeInput

   _args: Args


   type: BillingSubscription

unfollowUser = bool

followUser = bool

followApi = bool

unfollowApi = bool

sendMessage = bool

class rateApi(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: RatingInput

   _args: Args


   type: Any

class upsertEntityMetadataBulk(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      entityId: ID
      entityAttributes: list[EntityAttribute] ##NON NULL

   _args: Args


   type: Any

class upsertEntityMetadata(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      entityMetadata: EntityMetadataInput

   _args: Args


   type: Any

class deleteIssueV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: IssueDeleteInput

   _args: Args


   type: Any

class updateIssueV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: IssueUpdateInput

   _args: Args


   type: Any

class deleteIssues(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: IssuesDeleteInput

   _args: Args


   type: Any

class postIssueV3(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: IssueCreateInputV2

   _args: Args


   type: Any

class updateOrCreateEndpointWithParameters(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: updateOrCreateEndpointWithParameters

   _args: Args


   type: Any

class updateEndpointEntity(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: updateEndpointEntity

   _args: Args


   type: Any

class deleteEndpoint(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      endpointId: str

   _args: Args


   type: Any

class deleteEndpoints(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      endpointIds: list[str]

   _args: Args


   type: Any

class updateEndpointsCollectionOrder(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      endpointsCollectionOrder: list[EndpointOrder]

   _args: Args


   type: Any

class createEndpointsGroups(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      groups: list[EndpointsGroupCreateInput] ##NON NULL

   _args: Args


   type: EndpointsGroup ##NON NULL

class updateEndpointsGroups(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      groups: list[EndpointsGroupUpdateInput] ##NON NULL

   _args: Args


   type: EndpointsGroup ##NON NULL

class deleteEndpointsGroups(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: ID ##NON NULL

duplicateNameCheck = bool

createEntityMetadata = bool

updateEntityMetadata = bool

createEntitiesRoles = bool

upsertEntityRole = bool

class updateGraphQLSchema(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: UpdateGraphQLSchemaInput ##NON NULL

   _args: Args


   type: ID ##NON NULL

createHeadlines = str

createHeadlinesPerApiId = str

updateHeadlines = bool

class followIssueV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: IssueFollowInputV2

   _args: Args


   type: Any

class updateKafkaConfiguration(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: UpdateKafkaConfigurationInput

   _args: Args


   type: KafkaConfiguration

class subscribeToKafkaTopic(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      apiVersionId: str ##NON NULL
      topicName: str ##NON NULL
      options: SubscribeOptions ##NON NULL

   _args: Args


   type: SubscribeKafkaResponse

produceKafkaMessage = list[ProduceMessageResponse]

class postMessage(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      message: MessageCreateInput ##NON NULL

   _args: Args


   type: Any

class postMessageV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      message: MessageCreateInput ##NON NULL

   _args: Args


   type: Any

updateThreadEntityStatus = bool

markNotificationAsViewed = bool

markNewNotificationAsRead = bool

markNotificationsAsRead = bool

class updateOrganization(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: OrganizationUpdateInput ##NON NULL

   _args: Args


   type: Organization

deleteOrganization = bool

class createOrganization(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: OrganizationCreateInput ##NON NULL

   _args: Args


   type: Organization ##NON NULL

class createNewOrganizationV4(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: CreateNewOrganizationInputV4

   _args: Args


   type: Any

class generateResetPasswordToken(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      email: str ##NON NULL

   _args: Args


   type: Any

class resetUserPassword(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: ResetUserPasswordInput ##NON NULL

   _args: Args


   type: Any

deletePayoutInfo = bool

class addProject(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: AddProjectInput ##NON NULL

   _args: Args


   type: Project

class addProjectV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: AddProjectInput ##NON NULL

   _args: Args


   type: Project

class editProjectV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: EditProjectInput ##NON NULL

   _args: Args


   type: Any

class deleteProject(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: DeleteProjectInput ##NON NULL

   _args: Args


   type: ID

class createProject(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      project: ProjectCreateInput ##NON NULL

   _args: Args


   type: Project

updateProject = list[Project]

createProjectAllowedAPIs = list[ProjectAllowedAPI]

class updateProjectAllowedAPI(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: updateProjectAllowedAPIInput

   _args: Args


   type: ProjectAllowedAPI

deleteProjectAllowedAPIs = bool

changeApiUsedVersion = bool

class createRapidReason(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      rapidReasonInput: RapidReasonInput

   _args: Args


   type: ID

class deprecatedUpdateRole(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      role: RoleUpdateInput ##NON NULL

   _args: Args


   type: Any

class updateRole(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      role: RoleUpdateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class deprecatedCreateRole(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      role: RoleCreateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class createRole(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      role: RoleCreateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class deprecatedDeleteRole(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      roleId: ID

   _args: Args


   type: Any

deleteRole = bool

class createSecretData(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: createSecretDataInput

   _args: Args


   type: Any

updateBaseUrl = bool

class createSpotlight(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      spotlight: SpotlightCreateInput ##NON NULL

   _args: Args


   type: Spotlight ##NON NULL

class updateSpotlight(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      spotlight: SpotlightUpdateInput ##NON NULL

   _args: Args


   type: Spotlight ##NON NULL

deleteSpotlight = bool

deleteSubscriptions = bool

deleteSubscription = bool

class createSubscription(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: SubscriptionCreateInput ##NON NULL

   _args: Args


   type: BillingSubscription ##NON NULL

class updateTargetGroups(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      targetGroups: list[TargetGroupUpdateInput] ##NON NULL

   _args: Args


   type: TargetGroup ##NON NULL

removeTeamUserFromAllOrgTeams = bool

updateTeamUser = bool

updateUserRoles = bool

editTeam = bool

addUserToTeams = bool

deleteTeam = bool

class createTeam(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: TeamCreateInput ##NON NULL

   _args: Args


   type: Team

class updateTeam(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: TeamUpdateInput ##NON NULL

   _args: Args


   type: Team

updateTransactions = bool

class createTransformations(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      transformations: list[TransformationCreateInput] ##NON NULL

   _args: Args


   type: Transformation ##NON NULL

class updateTransformations(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      transformations: list[TransformationUpdateInput] ##NON NULL

   _args: Args


   type: Transformation ##NON NULL

class deleteTransformations(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      transformations: list[ID] ##NON NULL

   _args: Args


   type: DeletedTransformation ##NON NULL

class createTutorial(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      tutorial: TutorialCreateInput ##NON NULL

   _args: Args


   type: Tutorial

class updateTutorial(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      tutorial: TutorialUpdateInput ##NON NULL

   _args: Args


   type: Tutorial

deleteTutorial = bool

class phoneAuthSetup(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      phoneNumber: str ##NON NULL

   _args: Args


   type: PhoneVerification

phoneAuthSetupVerify = bool

class authenticateUsingPhone(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
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

class bulkDeleteUserInvitesV2(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      emails: list[str]
      orgId: int

   _args: Args


   type: Any

class deleteUserInvites(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: UserInvitesDeleteInput ##NON NULL

   _args: Args


   type: Any

bulkReactivateUserInvitesV2 = bool

reactivateUserInvites = bool

inviteUsersToTeams = bool

class saveUserApi(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      saveUserApi: SaveUserApi

   _args: Args


   type: UserSavedApi ##NON NULL

class updateUserById(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: UpdateUserInput

   _args: Args


   type: Any

updateUserPassword = bool

class deleteAll2faData(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      userId: str ##NON NULL

   _args: Args


   type: Any

class updateUserEmail(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      email: str ##NON NULL

   _args: Args


   type: Any

verifyEmailCode = bool

class updateUser(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      input: UserUpdateInput ##NON NULL

   _args: Args


   type: User

class createWorkflow(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      options: CreateWorkflowInput

   _args: Args


   type: Any

class createSignupApprovalWorkflow(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
      options: CreateSignupApprovalWorkflowInput

   _args: Args


   type: Any

class updateWorkflows(GQLMutation):
   class Args(GQLOperationArgs, GQLObject): 
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
