from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *


class createEventUrl(GQLObject):
   """
   createEventUrl - Create an Event that can be subscribed to via a webhook

   """
   class Args(GQLOperationArgs): 
      createDto: EventUrlCreateInput ##NON NULL

   _args: Args


   type: EventUrl ##NON NULL

class updateEventUrl(GQLObject):
   """
   updateEventUrl - URLs for the events webhooks feature

   """
   class Args(GQLOperationArgs): 
      updateDto: EventUrlUpdateInput ##NON NULL
      id: ID ##NON NULL

   _args: Args


   type: EventUrl ##NON NULL

class deleteEventUrl(GQLObject):
   """
   deleteEventUrl - Delete event Url

   """
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class upsertEventConfig(GQLObject):
   """
   upsertEventConfig - Update or Insert event configuration

   """
   class Args(GQLOperationArgs): 
      input: EventConfigUpdateInput ##NON NULL

   _args: Args


   type: EventConfig ##NON NULL

class deleteEventConfig(GQLObject):
   """
   deleteEventConfig - Delete event configuration

   """
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayInstance(GQLObject):
   """
   createGatewayInstance - Create a Gateway Instance in the Enterprise Tenant

   """
   class Args(GQLOperationArgs): 
      createDto: GatewayInstanceCreateInput ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class updateGatewayInstance(GQLObject):
   """
   updateGatewayInstance - Update the gateway instance information

   """
   class Args(GQLOperationArgs): 
      updateDto: GatewayInstanceUpdateInput ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class deleteGatewayInstance(GQLObject):
   """
   deleteGatewayInstance - Delete Gateway Instance

   """
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayTemplate(GQLObject):
   """
   createGatewayTemplate - Create a code template that can be referenced in a Gateway instance

   """
   class Args(GQLOperationArgs): 
      createDto: GatewayTemplateCreateInput ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class updateGatewayTemplate(GQLObject):
   """
   updateGatewayTemplate - Update the gateway configuration

   """
   class Args(GQLOperationArgs): 
      updateDto: GatewayTemplateUpdateInput ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class deleteGatewayTemplate(GQLObject):
   """
   deleteGatewayTemplate - Delete a code template and all its references in Gateways

   """
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayTemplateParam(GQLObject):
   """
   createGatewayTemplateParam - Create a user specified variable that can be referenced in the Gatway templates 

   """
   class Args(GQLOperationArgs): 
      createDto: GatewayTemplateParamsCreateInput ##NON NULL

   _args: Args


   type: GatewayTemplateParam ##NON NULL

class updateEnvConfig(GQLObject):
   """
   updateEnvConfig - updating advance settings   

   """
   class Args(GQLOperationArgs): 
      envConfig: EnvConfigUpdateInput ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class resetEnvConfig(GQLObject):
   class Args(GQLOperationArgs): 
      id: int ##NON NULL

   _args: Args


   type: EnvConfig ##NON NULL

class addUserAlert(GQLObject):
   """
   addUserAlert - Creates an alert to be notified when a metric crosses a threshold

   """
   class Args(GQLOperationArgs): 
      input: addUserAlertInput

   _args: Args


   type: UserAlert ##NON NULL

class deleteUserAlerts(GQLObject):
   """
   deleteUserAlerts - Delete alerts created by an API provider for an API

   """
   class Args(GQLOperationArgs): 
      input: deleteUserAlertsInput ##NON NULL

   _args: Args


   type: ID ##NON NULL

class editUserAlert(GQLObject):
   """
   editUserAlert - Update alert created by an API provider for an API

   """
   class Args(GQLOperationArgs): 
      input: editUserAlertInput ##NON NULL

   _args: Args


   type: UserAlert ##NON NULL

class updateUserAlerts(GQLObject):
   """
   updateUserAlerts - Update alerts created by an API provider for an API

   """
   class Args(GQLOperationArgs): 
      input: list[UserAlertUpdateInput] ##NON NULL

   _args: Args


   type: UserAlert ##NON NULL

class createApiCertificates(GQLObject):
   """
   createApiCertificates - Creates API certificate for 

   """
   class Args(GQLOperationArgs): 
      certificates: list[ApiCertificateCreateInput] ##NON NULL

   _args: Args


   type: ApiCertificateCreationResult ##NON NULL

deleteApiCertificates = bool

saveApiDevelopersToApi = bool

copyApiDevelopersFromVersion = bool

createApiFavorites = bool

deleteApiFavorites = bool

class createApiFollowers(GQLObject):
   """
   createApiFollowers - Adds a follower to an API

   """
   class Args(GQLOperationArgs): 
      apiFollowers: ApiFollowerCreateInput ##NON NULL

   _args: Args


   type: ApiFollower ##NON NULL

deleteApiFollowers = bool

class createApisFromSpecs(GQLObject):
   """
   createApisFromSpecs - Create an API from Supported spec files

   """
   class Args(GQLOperationArgs): 
      creations: list[ApiCreateFromSpecInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class updateApisFromSpecs(GQLObject):
   """
   updateApisFromSpecs - Update API version from spec file

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#update-an-api

   """
   class Args(GQLOperationArgs): 
      updates: list[ApiUpdateFromSpecInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class createApisFromRapidOas(GQLObject):
   """
   createApisFromRapidOas - This mutation currently supports providing no more than one item to create at a time

   """
   class Args(GQLOperationArgs): 
      creations: list[ApiCreateFromRapidOasInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class updateApisFromRapidOas(GQLObject):
   """
   updateApisFromRapidOas - This mutation currently supports providing no more than one item to update at a time

   """
   class Args(GQLOperationArgs): 
      updates: list[ApiUpdateFromRapidOasInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class createApiVersions(GQLObject):
   """
   createApiVersions - Creates a multiple API Versions

   """
   class Args(GQLOperationArgs): 
      apiVersions: list[ApiVersionCreateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class createGqlApiVersions(GQLObject):
   """
   createGqlApiVersions - Create a new GraphQL API Version

   """
   class Args(GQLOperationArgs): 
      gqlApiVersions: list[GqlApiVersionCreateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class updateApiVersions(GQLObject):
   """
   updateApiVersions - update the API Versions

   """
   class Args(GQLOperationArgs): 
      apiVersions: list[ApiVersionUpdateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class createApiVersionBillingPlanVersion(GQLObject):
   """
   createApiVersionBillingPlanVersion - [will be deprecated; do not use] Create API version and Billing Plan Version

   """
   class Args(GQLOperationArgs): 
      input: createApiVersionBillingPlanVersionInput

   _args: Args


   type: ApiVersionBillingPlanVersion

class createApi(GQLObject):
   """
   createApi - Creates an API

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#create-an-api

   """
   class Args(GQLOperationArgs): 
      api: ApiCreateInput ##NON NULL

   _args: Args


   type: Api ##NON NULL

class updateApi(GQLObject):
   """
   updateApi - Update API metadata



   """
   class Args(GQLOperationArgs): 
      api: ApiUpdateInput ##NON NULL

   _args: Args


   type: Api ##NON NULL

provisionSwaggerFiles = list[str]

deleteApi = bool

class createApplicationAuthorization(GQLObject):
   """
   createApplicationAuthorization - Creates authorization of type OAuth 

   """
   class Args(GQLOperationArgs): 
      input: AppAuthorizationCreateInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class updateApplicationAuthorization(GQLObject):
   """
   updateApplicationAuthorization - updated authorization value  

   """
   class Args(GQLOperationArgs): 
      input: AppAuthorizationUpdateInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

deleteApplicationAuthorization = bool

class addApplicationEnvironmentKey(GQLObject):
   """
   addApplicationEnvironmentKey - Creates an authorization of type x-rapid-key

   """
   class Args(GQLOperationArgs): 
      input: AddApplicationEnvironmentKeyInput ##NON NULL

   _args: Args


   type: Any

class editApplicationEnvironmentKey(GQLObject):
   """
   editApplicationEnvironmentKey - edit authorization value ( aka application env key )

   """
   class Args(GQLOperationArgs): 
      input: EditApplicationEnviornmentKeyInput ##NON NULL

   _args: Args


   type: Any

class deleteApplicationEnvironmentKey(GQLObject):
   """
   deleteApplicationEnvironmentKey - delete application authorization of type x-rapid-key

   """
   class Args(GQLOperationArgs): 
      input: DeleteApplicationEnvironmentKeyInput ##NON NULL

   _args: Args


   type: ID

class generateAssetUploadUrl(GQLObject):
   """
   generateAssetUploadUrl - Creates asset object; returns presignedURL used to upload asset.

   """
   class Args(GQLOperationArgs): 
      input: GenerateAssetUploadUrlInput ##NON NULL

   _args: Args


   type: Asset ##NON NULL

deleteAsset = bool

class updateAssetUploaded(GQLObject):
   """
   updateAssetUploaded - Updates asset object state to uploaded after asset is uploaded to the presignedURL

   """
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: Asset

class updateAsset(GQLObject):
   """
   updateAsset - Update asset metadata: title, description, visibility - will control whether is visible in the hub 

   """
   class Args(GQLOperationArgs): 
      input: AssetUpdateInput ##NON NULL

   _args: Args


   type: Asset

class upsertAsyncApiConfiguration(GQLObject):
   """
   upsertAsyncApiConfiguration - [experimental] Update Async API configuration

   """
   class Args(GQLOperationArgs): 
      asyncApiConfigurations: list[AsyncApiConfigurationCreateInput] ##NON NULL

   _args: Args


   type: AsyncApiConfiguration ##NON NULL

class upsertUserAttributes(GQLObject):
   """
   upsertUserAttributes - Takes a set of user attributes and updates them for a user

   """
   class Args(GQLOperationArgs): 
      input: UserAttributesInput

   _args: Args


   type: Any

class updateUserAttributeItem(GQLObject):
   """
   updateUserAttributeItem - Update user metadata 

   """
   class Args(GQLOperationArgs): 
      input: ThemeUserAttributesInput ##NON NULL

   _args: Args


   type: Any

class createAuthentications(GQLObject):
   """
   createAuthentications - Create provider specific authentication for an API

   """
   class Args(GQLOperationArgs): 
      authentications: list[AuthenticationCreateInput] ##NON NULL

   _args: Args


   type: Authentication ##NON NULL

class updateAuthentications(GQLObject):
   """
   updateAuthentications - Set the API authentications configuration

   """
   class Args(GQLOperationArgs): 
      authentications: list[AuthenticationUpdateInput] ##NON NULL

   _args: Args


   type: Authentication ##NON NULL

class createOrUpdateAPIVersionAuthentication(GQLObject):
   """
   createOrUpdateAPIVersionAuthentication - Create or Update the authentication used to access an API

   """
   class Args(GQLOperationArgs): 
      input: createAuthenticationInput

   _args: Args


   type: AuthenticationCreateOrUpdateResult

class createBillingFeature(GQLObject):
   """
   createBillingFeature - Create a new Billing Feature

   """
   class Args(GQLOperationArgs): 
      createBillingFeature: createBillingFeature

   _args: Args


   type: BillingFeature

class updateBillingFeature(GQLObject):
   """
   updateBillingFeature - Update the API billing feature

   """
   class Args(GQLOperationArgs): 
      updateBillingFeature: updateBillingFeature

   _args: Args


   type: BillingFeature

class upsertBillingFeature(GQLObject):
   """
   upsertBillingFeature - [will be deprecated; do not use] Updates billing feature for 1 API

   """
   class Args(GQLOperationArgs): 
      upsertBillingFeature: upsertBillingFeatureInput ##NON NULL

   _args: Args


   type: BillingFeature

class deleteBillingFeature(GQLObject):
   """
   deleteBillingFeature - Delete API billing feature by id

   """
   class Args(GQLOperationArgs): 
      billingFeatureId: str

   _args: Args


   type: Any

class deleteBillingFeatures(GQLObject):
   """
   deleteBillingFeatures - Delete API billing features

   """
   class Args(GQLOperationArgs): 
      billingFeatureIds: list[str]

   _args: Args


   type: Any

class createStripeCustomer(GQLObject):
   """
   createStripeCustomer - Create a customer in Stripe with credit card details and personal details

   """
   class Args(GQLOperationArgs): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class updateStripeCustomer(GQLObject):
   """
   updateStripeCustomer - Updates customer details in Stripe

   """
   class Args(GQLOperationArgs): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class createStripeCustomerV2(GQLObject):
   """
   createStripeCustomerV2 - Create a customer in Stripe with credit card details and personal details

   """
   class Args(GQLOperationArgs): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class updateStripeCustomerV2(GQLObject):
   """
   updateStripeCustomerV2 - Updates customer details in Stripe

   """
   class Args(GQLOperationArgs): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

deleteCustomerPaymentMethod = bool

class upsertBillingItem(GQLObject):
   """
   upsertBillingItem - [will be deprecated; do not use] Updates 1 billing item

   """
   class Args(GQLOperationArgs): 
      input: BillingItemUpsertInput ##NON NULL

   _args: Args


   type: BillingItem

class deleteBillingItem(GQLObject):
   """
   deleteBillingItem - Delete a single billing item, in the UI we call these Objects

   """
   class Args(GQLOperationArgs): 
      id: ID ##NON NULL

   _args: Args


   type: Any

deleteBillingItems = bool

deleteBillingPlans = bool

updateAllowedPlanDevelopers = list[AllowedPlanDeveloper]

editOrganizationInvoice = bool

class createBillingPlan(GQLObject):
   """
   createBillingPlan - Create a new Billing Plan

   """
   class Args(GQLOperationArgs): 
      billingPlan: BillingPlanCreateInput ##NON NULL

   _args: Args


   type: BillingPlan

class updateBillingPlanMetadata(GQLObject):
   """
   updateBillingPlanMetadata - Updates the data of the billing plan

   """
   class Args(GQLOperationArgs): 
      billingPlan: BillingPlanMetadataUpdateInput ##NON NULL

   _args: Args


   type: BillingPlan

class updateBillingPlanExtended(GQLObject):
   """
   updateBillingPlanExtended - Updates billing plan sub object

   """
   class Args(GQLOperationArgs): 
      billingPlan: BillingPlanExtendedUpdateInput ##NON NULL

   _args: Args


   type: BillingPlan

class upsertBillingPlanAndVersion(GQLObject):
   """
   upsertBillingPlanAndVersion - [will be deprecated; do not use] Updates plan and version for 1 API

   """
   class Args(GQLOperationArgs): 
      upsertBillingPlanAndVersionInput: upsertBillingPlanAndVersionInput ##NON NULL

   _args: Args


   type: BillingPlanVersion

blockUsers = bool

unblockUsers = bool

class createCategory(GQLObject):
   """
   createCategory - Create a new Category (API Level)

   """
   class Args(GQLOperationArgs): 
      category: CategoryCreateInput ##NON NULL

   _args: Args


   type: Category ##NON NULL

class updateCategory(GQLObject):
   """
   updateCategory - Update category itself

   """
   class Args(GQLOperationArgs): 
      category: CategoryUpdateInput ##NON NULL

   _args: Args


   type: Category ##NON NULL

class deleteCategories(GQLObject):
   """
   deleteCategories - Deletes a category

   """
   class Args(GQLOperationArgs): 
      categories: list[ID] ##NON NULL

   _args: Args


   type: DeletedCategory ##NON NULL

deleteCollection = bool

class updateCollection(GQLObject):
   """
   updateCollection - Update single collection

   """
   class Args(GQLOperationArgs): 
      input: CollectionUpdateInput ##NON NULL

   _args: Args


   type: Collection

class createCollection(GQLObject):
   """
   createCollection - Create a new Hub Category

   """
   class Args(GQLOperationArgs): 
      input: CollectionCreateInput ##NON NULL

   _args: Args


   type: Collection

bulkUpdateCollections = list[Collection]

updateCollections = list[Collection]

class postCommentV2(GQLObject):
   """
   postCommentV2 - Post a comment

   """
   class Args(GQLOperationArgs): 
      input: CommentCreateInput

   _args: Args


   type: Comment

class deleteCommentV2(GQLObject):
   """
   deleteCommentV2 - Delete a comment

   """
   class Args(GQLOperationArgs): 
      input: CommentDeleteInput

   _args: Args


   type: Any

class updateCommentV2(GQLObject):
   """
   updateCommentV2 - Update a comment

   """
   class Args(GQLOperationArgs): 
      input: CommentUpdateInput

   _args: Args


   type: Any

class postCommentV3(GQLObject):
   """
   postCommentV3 - Post a comment

   """
   class Args(GQLOperationArgs): 
      input: CommentCreateInput

   _args: Args


   type: Comment

class subscribeToPlan(GQLObject):
   """
   subscribeToPlan - A user or team can subscribe to an API

   """
   class Args(GQLOperationArgs): 
      input: SubscribeInput

   _args: Args


   type: BillingSubscription

unfollowUser = bool

followUser = bool

followApi = bool

unfollowApi = bool

sendMessage = bool

class rateApi(GQLObject):
   """
   rateApi - Give an API rating

   """
   class Args(GQLOperationArgs): 
      input: RatingInput

   _args: Args


   type: Any

class upsertEntityMetadataBulk(GQLObject):
   """
   upsertEntityMetadataBulk - [will be deprecated; do not use] Assign one or more attributes to an entity

   """
   class Args(GQLOperationArgs): 
      entityId: ID
      entityAttributes: list[EntityAttribute] ##NON NULL

   _args: Args


   type: Any

class upsertEntityMetadata(GQLObject):
   """
   upsertEntityMetadata - Assign one or more attributes to an entity (user, role, team)

   """
   class Args(GQLOperationArgs): 
      entityMetadata: EntityMetadataInput

   _args: Args


   type: Any

class deleteIssueV2(GQLObject):
   """
   deleteIssueV2 - Deletes an issue 

   """
   class Args(GQLOperationArgs): 
      input: IssueDeleteInput

   _args: Args


   type: Any

class updateIssueV2(GQLObject):
   """
   updateIssueV2 - Make a change to a public comment on an API.

   """
   class Args(GQLOperationArgs): 
      input: IssueUpdateInput

   _args: Args


   type: Any

class deleteIssues(GQLObject):
   """
   deleteIssues - Deletes an issue 

   """
   class Args(GQLOperationArgs): 
      input: IssuesDeleteInput

   _args: Args


   type: Any

class postIssueV3(GQLObject):
   """
   postIssueV3 - Post an issue to a provider

   """
   class Args(GQLOperationArgs): 
      input: IssueCreateInputV2

   _args: Args


   type: Any

class updateOrCreateEndpointWithParameters(GQLObject):
   """
   updateOrCreateEndpointWithParameters - Create or make changes to an endpoint with a parameter on a provider's API.

   """
   class Args(GQLOperationArgs): 
      input: updateOrCreateEndpointWithParameters

   _args: Args


   type: Any

class updateEndpointEntity(GQLObject):
   """
   updateEndpointEntity - [do not use; will be deprecated] use updateOrCreateEndpointWithParameters

   """
   class Args(GQLOperationArgs): 
      input: updateEndpointEntity

   _args: Args


   type: Any

class deleteEndpoint(GQLObject):
   """
   deleteEndpoint - Delete an endpoint

   """
   class Args(GQLOperationArgs): 
      endpointId: str

   _args: Args


   type: Any

class deleteEndpoints(GQLObject):
   """
   deleteEndpoints - Delete a few endpoints at once

   """
   class Args(GQLOperationArgs): 
      endpointIds: list[str]

   _args: Args


   type: Any

class updateEndpointsCollectionOrder(GQLObject):
   """
   updateEndpointsCollectionOrder - Update selected endpoints order on playground

   """
   class Args(GQLOperationArgs): 
      endpointsCollectionOrder: list[EndpointOrder]

   _args: Args


   type: Any

class createEndpointsGroups(GQLObject):
   """
   createEndpointsGroups - Create a group object that later user can attach endpoints

   """
   class Args(GQLOperationArgs): 
      groups: list[EndpointsGroupCreateInput] ##NON NULL

   _args: Args


   type: EndpointsGroup ##NON NULL

class updateEndpointsGroups(GQLObject):
   """
   updateEndpointsGroups - Update endpoints group properties

   """
   class Args(GQLOperationArgs): 
      groups: list[EndpointsGroupUpdateInput] ##NON NULL

   _args: Args


   type: EndpointsGroup ##NON NULL

class deleteEndpointsGroups(GQLObject):
   """
   deleteEndpointsGroups - Delete a group that endpoints are attached to

   """
   class Args(GQLOperationArgs): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: ID ##NON NULL

duplicateNameCheck = bool

createEntityMetadata = bool

updateEntityMetadata = bool

createEntitiesRoles = bool

upsertEntityRole = bool

class updateGraphQLSchema(GQLObject):
   """
   updateGraphQLSchema - Update GraphQLSchema by graphQLSchemaId or endpointId (at least one is mandatory, graphQLSchemaId is prioritized)

   """
   class Args(GQLOperationArgs): 
      input: UpdateGraphQLSchemaInput ##NON NULL

   _args: Args


   type: ID ##NON NULL

createHeadlines = str

createHeadlinesPerApiId = str

updateHeadlines = bool

class followIssueV2(GQLObject):
   """
   followIssueV2 - Follow an issue 

   """
   class Args(GQLOperationArgs): 
      input: IssueFollowInputV2

   _args: Args


   type: Any

class updateKafkaConfiguration(GQLObject):
   """
   updateKafkaConfiguration - Update the configuration of the Kafka service

   """
   class Args(GQLOperationArgs): 
      input: UpdateKafkaConfigurationInput

   _args: Args


   type: KafkaConfiguration

class subscribeToKafkaTopic(GQLObject):
   """
   subscribeToKafkaTopic - Get kafka subscription by topic for an API verison

   """
   class Args(GQLOperationArgs): 
      apiVersionId: str ##NON NULL
      topicName: str ##NON NULL
      options: SubscribeOptions ##NON NULL

   _args: Args


   type: SubscribeKafkaResponse

produceKafkaMessage = list[ProduceMessageResponse]

class postMessage(GQLObject):
   """
   postMessage - Adds a message to an API's discussion board

   """
   class Args(GQLOperationArgs): 
      message: MessageCreateInput ##NON NULL

   _args: Args


   type: Any

class postMessageV2(GQLObject):
   """
   postMessageV2 - Adds a message to an API's discussion board

   """
   class Args(GQLOperationArgs): 
      message: MessageCreateInput ##NON NULL

   _args: Args


   type: Any

updateThreadEntityStatus = bool

markNotificationAsViewed = bool

markNewNotificationAsRead = bool

markNotificationsAsRead = bool

class updateOrganization(GQLObject):
   """
   updateOrganization - Updating organization 

   """
   class Args(GQLOperationArgs): 
      input: OrganizationUpdateInput ##NON NULL

   _args: Args


   type: Organization

deleteOrganization = bool

class createOrganization(GQLObject):
   """
   createOrganization - Create an organization 

   """
   class Args(GQLOperationArgs): 
      input: OrganizationCreateInput ##NON NULL

   _args: Args


   type: Organization ##NON NULL

class createNewOrganizationV4(GQLObject):
   """
   createNewOrganizationV4 - [will be deprecated; do not use] Create an organization 

   """
   class Args(GQLOperationArgs): 
      input: CreateNewOrganizationInputV4

   _args: Args


   type: Any

class generateResetPasswordToken(GQLObject):
   """
   generateResetPasswordToken - Generate a reset password token

   """
   class Args(GQLOperationArgs): 
      email: str ##NON NULL

   _args: Args


   type: Any

class resetUserPassword(GQLObject):
   """
   resetUserPassword - resets user password 

   """
   class Args(GQLOperationArgs): 
      input: ResetUserPasswordInput ##NON NULL

   _args: Args


   type: Any

deletePayoutInfo = bool

class addProject(GQLObject):
   """
   addProject - [will be deprecated; do not use] Creates Application ( application and x-rapid-key  ) 

   """
   class Args(GQLOperationArgs): 
      input: AddProjectInput ##NON NULL

   _args: Args


   type: Project

class addProjectV2(GQLObject):
   """
   addProjectV2 - Creates Application ( application and x-rapid-key  ) 

   """
   class Args(GQLOperationArgs): 
      input: AddProjectInput ##NON NULL

   _args: Args


   type: Project

class editProjectV2(GQLObject):
   """
   editProjectV2 - Edit user application properties

   """
   class Args(GQLOperationArgs): 
      input: EditProjectInput ##NON NULL

   _args: Args


   type: Any

class deleteProject(GQLObject):
   """
   deleteProject - Delete a user application project

   """
   class Args(GQLOperationArgs): 
      input: DeleteProjectInput ##NON NULL

   _args: Args


   type: ID

class createProject(GQLObject):
   """
   createProject - Create an Application

   """
   class Args(GQLOperationArgs): 
      project: ProjectCreateInput ##NON NULL

   _args: Args


   type: Project

updateProject = list[Project]

createProjectAllowedAPIs = list[ProjectAllowedAPI]

class updateProjectAllowedAPI(GQLObject):
   """
   updateProjectAllowedAPI - Change the APIs list that the app/project has access to

   """
   class Args(GQLOperationArgs): 
      input: updateProjectAllowedAPIInput

   _args: Args


   type: ProjectAllowedAPI

deleteProjectAllowedAPIs = bool

changeApiUsedVersion = bool

class createRapidReason(GQLObject):
   """
   createRapidReason - Give a reason for unsubscribing to an API

   """
   class Args(GQLOperationArgs): 
      rapidReasonInput: RapidReasonInput

   _args: Args


   type: ID

class deprecatedUpdateRole(GQLObject):
   """
   deprecatedUpdateRole - [do not use; will be deprecated] update role

   """
   class Args(GQLOperationArgs): 
      role: RoleUpdateInput ##NON NULL

   _args: Args


   type: Any

class updateRole(GQLObject):
   """
   updateRole - Updates a role's description or permissions, or change whether it's set as default.

   """
   class Args(GQLOperationArgs): 
      role: RoleUpdateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class deprecatedCreateRole(GQLObject):
   """
   deprecatedCreateRole - [do not use; will be deprecated] create role

   """
   class Args(GQLOperationArgs): 
      role: RoleCreateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class createRole(GQLObject):
   """
   createRole - Create a role 

   """
   class Args(GQLOperationArgs): 
      role: RoleCreateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class deprecatedDeleteRole(GQLObject):
   """
   deprecatedDeleteRole - [do not use; will be deprecated] delete role

   """
   class Args(GQLOperationArgs): 
      roleId: ID

   _args: Args


   type: Any

deleteRole = bool

class createSecretData(GQLObject):
   """
   createSecretData - [will be deprecated; do not use] Create an API secret

   """
   class Args(GQLOperationArgs): 
      input: createSecretDataInput

   _args: Args


   type: Any

updateBaseUrl = bool

class createSpotlight(GQLObject):
   """
   createSpotlight - Creates a spotlight on an API listing

   """
   class Args(GQLOperationArgs): 
      spotlight: SpotlightCreateInput ##NON NULL

   _args: Args


   type: Spotlight ##NON NULL

class updateSpotlight(GQLObject):
   """
   updateSpotlight - Updates an existing spotlight on an API listing

   """
   class Args(GQLOperationArgs): 
      spotlight: SpotlightUpdateInput ##NON NULL

   _args: Args


   type: Spotlight ##NON NULL

deleteSpotlight = bool

deleteSubscriptions = bool

deleteSubscription = bool

class createSubscription(GQLObject):
   """
   createSubscription - Create a new API subscription

   """
   class Args(GQLOperationArgs): 
      input: SubscriptionCreateInput ##NON NULL

   _args: Args


   type: BillingSubscription ##NON NULL

class updateTargetGroups(GQLObject):
   """
   updateTargetGroups - Updates the target URL on 1 API version

   """
   class Args(GQLOperationArgs): 
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
   """
   createTeam - Create a team

   """
   class Args(GQLOperationArgs): 
      input: TeamCreateInput ##NON NULL

   _args: Args


   type: Team

class updateTeam(GQLObject):
   """
   updateTeam - Updates team

   """
   class Args(GQLOperationArgs): 
      input: TeamUpdateInput ##NON NULL

   _args: Args


   type: Team

updateTransactions = bool

class createTransformations(GQLObject):
   """
   createTransformations - Create a new API verison transformation

   """
   class Args(GQLOperationArgs): 
      transformations: list[TransformationCreateInput] ##NON NULL

   _args: Args


   type: Transformation ##NON NULL

class updateTransformations(GQLObject):
   """
   updateTransformations - Update API version transformations

   """
   class Args(GQLOperationArgs): 
      transformations: list[TransformationUpdateInput] ##NON NULL

   _args: Args


   type: Transformation ##NON NULL

class deleteTransformations(GQLObject):
   """
   deleteTransformations - delete transformation from the api version 

   """
   class Args(GQLOperationArgs): 
      transformations: list[ID] ##NON NULL

   _args: Args


   type: DeletedTransformation ##NON NULL

class createTutorial(GQLObject):
   """
   createTutorial - Creates a tutorial on an API listing

   """
   class Args(GQLOperationArgs): 
      tutorial: TutorialCreateInput ##NON NULL

   _args: Args


   type: Tutorial

class updateTutorial(GQLObject):
   """
   updateTutorial - Updates an existing tutorial on an API listing

   """
   class Args(GQLOperationArgs): 
      tutorial: TutorialUpdateInput ##NON NULL

   _args: Args


   type: Tutorial

deleteTutorial = bool

class phoneAuthSetup(GQLObject):
   """
   phoneAuthSetup - setting up phone authentication ( 2fa flow)

   """
   class Args(GQLOperationArgs): 
      phoneNumber: str ##NON NULL

   _args: Args


   type: PhoneVerification

phoneAuthSetupVerify = bool

class authenticateUsingPhone(GQLObject):
   """
   authenticateUsingPhone - Authenticates the user using phone code 

   """
   class Args(GQLOperationArgs): 
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
   """
   bulkDeleteUserInvitesV2 - Deletes users that are in pending mode from the organization 

   """
   class Args(GQLOperationArgs): 
      emails: list[str]
      orgId: int

   _args: Args


   type: Any

class deleteUserInvites(GQLObject):
   """
   deleteUserInvites - Used for deleting user/s that not yet confirmed the invitation

   """
   class Args(GQLOperationArgs): 
      input: UserInvitesDeleteInput ##NON NULL

   _args: Args


   type: Any

bulkReactivateUserInvitesV2 = bool

reactivateUserInvites = bool

inviteUsersToTeams = bool

class saveUserApi(GQLObject):
   """
   saveUserApi - Save an API as a favorite

   """
   class Args(GQLOperationArgs): 
      saveUserApi: SaveUserApi

   _args: Args


   type: UserSavedApi ##NON NULL

class updateUserById(GQLObject):
   """
   updateUserById - Update a set of attributes on a user by ID.

   """
   class Args(GQLOperationArgs): 
      input: UpdateUserInput

   _args: Args


   type: Any

updateUserPassword = bool

class deleteAll2faData(GQLObject):
   """
   deleteAll2faData - Delete all 2FA data

   """
   class Args(GQLOperationArgs): 
      userId: str ##NON NULL

   _args: Args


   type: Any

class updateUserEmail(GQLObject):
   """
   updateUserEmail - Update the email address of a user

   """
   class Args(GQLOperationArgs): 
      email: str ##NON NULL

   _args: Args


   type: Any

verifyEmailCode = bool

class updateUser(GQLObject):
   """
   updateUser - Updates user metadata / password 

   """
   class Args(GQLOperationArgs): 
      input: UserUpdateInput ##NON NULL

   _args: Args


   type: User

class createWorkflow(GQLObject):
   """
   createWorkflow - Create a workflow

   """
   class Args(GQLOperationArgs): 
      options: CreateWorkflowInput

   _args: Args


   type: Any

class createSignupApprovalWorkflow(GQLObject):
   """
   createSignupApprovalWorkflow - Create a signup approval request

   """
   class Args(GQLOperationArgs): 
      options: CreateSignupApprovalWorkflowInput

   _args: Args


   type: Any

class updateWorkflows(GQLObject):
   """
   updateWorkflows - Change an entity's workflow

   """
   class Args(GQLOperationArgs): 
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
