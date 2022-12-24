from pygqlmap import GQLMutation
from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *


class createEventUrl(GQLMutation):
   """
   createEventUrl - Create an Event that can be subscribed to via a webhook

   """
   class Args(GQLArgsSet, GQLObject): 
      createDto: EventUrlCreateInput ##NON NULL

   _args: Args


   type: EventUrl ##NON NULL

class updateEventUrl(GQLMutation):
   """
   updateEventUrl - URLs for the events webhooks feature

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL
      updateDto: EventUrlUpdateInput ##NON NULL

   _args: Args


   type: EventUrl ##NON NULL

class deleteEventUrl(GQLMutation):
   """
   deleteEventUrl - Delete event Url

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class upsertEventConfig(GQLMutation):
   """
   upsertEventConfig - Update or Insert event configuration

   """
   class Args(GQLArgsSet, GQLObject): 
      input: EventConfigUpdateInput ##NON NULL

   _args: Args


   type: EventConfig ##NON NULL

class deleteEventConfig(GQLMutation):
   """
   deleteEventConfig - Delete event configuration

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayInstance(GQLMutation):
   """
   createGatewayInstance - Create a Gateway Instance in the Enterprise Tenant

   """
   class Args(GQLArgsSet, GQLObject): 
      createDto: GatewayInstanceCreateInput ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class updateGatewayInstance(GQLMutation):
   """
   updateGatewayInstance - Update the gateway instance information

   """
   class Args(GQLArgsSet, GQLObject): 
      updateDto: GatewayInstanceUpdateInput ##NON NULL

   _args: Args


   type: GatewayInstance ##NON NULL

class deleteGatewayInstance(GQLMutation):
   """
   deleteGatewayInstance - Delete Gateway Instance

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayTemplate(GQLMutation):
   """
   createGatewayTemplate - Create a code template that can be referenced in a Gateway instance

   """
   class Args(GQLArgsSet, GQLObject): 
      createDto: GatewayTemplateCreateInput ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class updateGatewayTemplate(GQLMutation):
   """
   updateGatewayTemplate - Update the gateway configuration

   """
   class Args(GQLArgsSet, GQLObject): 
      updateDto: GatewayTemplateUpdateInput ##NON NULL

   _args: Args


   type: GwTemplate ##NON NULL

class deleteGatewayTemplate(GQLMutation):
   """
   deleteGatewayTemplate - Delete a code template and all its references in Gateways

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createGatewayTemplateParam(GQLMutation):
   """
   createGatewayTemplateParam - Create a user specified variable that can be referenced in the Gatway templates 

   """
   class Args(GQLArgsSet, GQLObject): 
      createDto: GatewayTemplateParamsCreateInput ##NON NULL

   _args: Args


   type: GatewayTemplateParam ##NON NULL

class updateEnvConfig(GQLMutation):
   """
   updateEnvConfig - updating advance settings   

   """
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
   """
   addUserAlert - Creates an alert to be notified when a metric crosses a threshold

   """
   class Args(GQLArgsSet, GQLObject): 
      input: addUserAlertInput

   _args: Args


   type: UserAlert ##NON NULL

class deleteUserAlerts(GQLMutation):
   """
   deleteUserAlerts - Delete alerts created by an API provider for an API

   """
   class Args(GQLArgsSet, GQLObject): 
      input: deleteUserAlertsInput ##NON NULL

   _args: Args


   type: ID ##NON NULL

class editUserAlert(GQLMutation):
   """
   editUserAlert - Update alert created by an API provider for an API

   """
   class Args(GQLArgsSet, GQLObject): 
      input: editUserAlertInput ##NON NULL

   _args: Args


   type: UserAlert ##NON NULL

class updateUserAlerts(GQLMutation):
   """
   updateUserAlerts - Update alerts created by an API provider for an API

   """
   class Args(GQLArgsSet, GQLObject): 
      input: list[UserAlertUpdateInput] ##NON NULL

   _args: Args


   type: UserAlert ##NON NULL

class createApiCertificates(GQLMutation):
   """
   createApiCertificates - Creates API certificate for 

   """
   class Args(GQLArgsSet, GQLObject): 
      certificates: list[ApiCertificateCreateInput] ##NON NULL

   _args: Args


   type: ApiCertificateCreationResult ##NON NULL

class deleteApiCertificates(GQLMutation):
   """
   deleteApiCertificates - Delete the API Certificate

   """
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: bool ##NON NULL

class saveApiDevelopersToApi(GQLMutation):
   """
   saveApiDevelopersToApi - Invite developers to an API 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: SaveApiDevelopersInput ##NON NULL

   _args: Args


   type: bool

class copyApiDevelopersFromVersion(GQLMutation):
   """
   copyApiDevelopersFromVersion - Copies all API developers from an API Version

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CopyApiDevelopersInput

   _args: Args


   type: bool

class createApiFavorites(GQLMutation):
   """
   createApiFavorites - Adding an API to the user favoites list on the user/team context on studio

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CreateApiFavoritesInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class deleteApiFavorites(GQLMutation):
   """
   deleteApiFavorites - Unmark the API from the user's favorites list 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteApiFavoritesInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class createApiFollowers(GQLMutation):
   """
   createApiFollowers - Adds a follower to an API

   """
   class Args(GQLArgsSet, GQLObject): 
      apiFollowers: ApiFollowerCreateInput ##NON NULL

   _args: Args


   type: ApiFollower ##NON NULL

class deleteApiFollowers(GQLMutation):
   """
   deleteApiFollowers - Removes a follower from an API

   """
   class Args(GQLArgsSet, GQLObject): 
      apiFollowers: ApiFollowerDeleteInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class createApisFromSpecs(GQLMutation):
   """
   createApisFromSpecs - Create an API from Supported spec files

   """
   class Args(GQLArgsSet, GQLObject): 
      creations: list[ApiCreateFromSpecInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class updateApisFromSpecs(GQLMutation):
   """
   updateApisFromSpecs - Update API version from spec file

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#update-an-api

   """
   class Args(GQLArgsSet, GQLObject): 
      updates: list[ApiUpdateFromSpecInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class createApisFromRapidOas(GQLMutation):
   """
   createApisFromRapidOas - This mutation currently supports providing no more than one item to create at a time

   """
   class Args(GQLArgsSet, GQLObject): 
      creations: list[ApiCreateFromRapidOasInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class updateApisFromRapidOas(GQLMutation):
   """
   updateApisFromRapidOas - This mutation currently supports providing no more than one item to update at a time

   """
   class Args(GQLArgsSet, GQLObject): 
      updates: list[ApiUpdateFromRapidOasInput] ##NON NULL

   _args: Args


   type: ApiSpecImportResult ##NON NULL

class createApiVersions(GQLMutation):
   """
   createApiVersions - Creates a multiple API Versions

   """
   class Args(GQLArgsSet, GQLObject): 
      apiVersions: list[ApiVersionCreateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class createGqlApiVersions(GQLMutation):
   """
   createGqlApiVersions - Create a new GraphQL API Version

   """
   class Args(GQLArgsSet, GQLObject): 
      gqlApiVersions: list[GqlApiVersionCreateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class updateApiVersions(GQLMutation):
   """
   updateApiVersions - update the API Versions

   """
   class Args(GQLArgsSet, GQLObject): 
      apiVersions: list[ApiVersionUpdateInput] ##NON NULL

   _args: Args


   type: ApiVersion ##NON NULL

class createApiVersionBillingPlanVersion(GQLMutation):
   """
   createApiVersionBillingPlanVersion - [will be deprecated; do not use] Create API version and Billing Plan Version

   """
   class Args(GQLArgsSet, GQLObject): 
      input: createApiVersionBillingPlanVersionInput

   _args: Args


   type: ApiVersionBillingPlanVersion

class createApi(GQLMutation):
   """
   createApi - Creates an API

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#create-an-api

   """
   class Args(GQLArgsSet, GQLObject): 
      api: ApiCreateInput ##NON NULL

   _args: Args


   type: Api ##NON NULL

class updateApi(GQLMutation):
   """
   updateApi - Update API metadata



   """
   class Args(GQLArgsSet, GQLObject): 
      api: ApiUpdateInput ##NON NULL

   _args: Args


   type: Api ##NON NULL

class provisionSwaggerFiles(GQLMutation):
   """
   provisionSwaggerFiles - [do not use; will be deprecated] use createApisFromSpecs

   """
   class Args(GQLArgsSet, GQLObject): 
      input: list[ProvisionApiFromFileInput] ##NON NULL

   _args: Args


   type: list[str]

class deleteApi(GQLMutation):
   """
   deleteApi - Delete the API

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool ##NON NULL

class createApplicationAuthorization(GQLMutation):
   """
   createApplicationAuthorization - Creates authorization of type OAuth 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: AppAuthorizationCreateInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class updateApplicationAuthorization(GQLMutation):
   """
   updateApplicationAuthorization - updated authorization value  

   """
   class Args(GQLArgsSet, GQLObject): 
      input: AppAuthorizationUpdateInput ##NON NULL

   _args: Args


   type: ApplicationAuthorization ##NON NULL

class deleteApplicationAuthorization(GQLMutation):
   """
   deleteApplicationAuthorization - delete application authorization by id

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool ##NON NULL

class addApplicationEnvironmentKey(GQLMutation):
   """
   addApplicationEnvironmentKey - Creates an authorization of type x-rapid-key

   """
   class Args(GQLArgsSet, GQLObject): 
      input: AddApplicationEnvironmentKeyInput ##NON NULL

   _args: Args


   type: Any

class editApplicationEnvironmentKey(GQLMutation):
   """
   editApplicationEnvironmentKey - edit authorization value ( aka application env key )

   """
   class Args(GQLArgsSet, GQLObject): 
      input: EditApplicationEnviornmentKeyInput ##NON NULL

   _args: Args


   type: Any

class deleteApplicationEnvironmentKey(GQLMutation):
   """
   deleteApplicationEnvironmentKey - delete application authorization of type x-rapid-key

   """
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteApplicationEnvironmentKeyInput ##NON NULL

   _args: Args


   type: ID

class generateAssetUploadUrl(GQLMutation):
   """
   generateAssetUploadUrl - Creates asset object; returns presignedURL used to upload asset.

   """
   class Args(GQLArgsSet, GQLObject): 
      input: GenerateAssetUploadUrlInput ##NON NULL

   _args: Args


   type: Asset ##NON NULL

class deleteAsset(GQLMutation):
   """
   deleteAsset - Delete an asset by ID

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool ##NON NULL

class updateAssetUploaded(GQLMutation):
   """
   updateAssetUploaded - Updates asset object state to uploaded after asset is uploaded to the presignedURL

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Asset

class updateAsset(GQLMutation):
   """
   updateAsset - Update asset metadata: title, description, visibility - will control whether is visible in the hub 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: AssetUpdateInput ##NON NULL

   _args: Args


   type: Asset

class upsertAsyncApiConfiguration(GQLMutation):
   """
   upsertAsyncApiConfiguration - [experimental] Update Async API configuration

   """
   class Args(GQLArgsSet, GQLObject): 
      asyncApiConfigurations: list[AsyncApiConfigurationCreateInput] ##NON NULL

   _args: Args


   type: AsyncApiConfiguration ##NON NULL

class upsertUserAttributes(GQLMutation):
   """
   upsertUserAttributes - Takes a set of user attributes and updates them for a user

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UserAttributesInput

   _args: Args


   type: Any

class updateUserAttributeItem(GQLMutation):
   """
   updateUserAttributeItem - Update user metadata 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: ThemeUserAttributesInput ##NON NULL

   _args: Args


   type: Any

class createAuthentications(GQLMutation):
   """
   createAuthentications - Create provider specific authentication for an API

   """
   class Args(GQLArgsSet, GQLObject): 
      authentications: list[AuthenticationCreateInput] ##NON NULL

   _args: Args


   type: Authentication ##NON NULL

class updateAuthentications(GQLMutation):
   """
   updateAuthentications - Set the API authentications configuration

   """
   class Args(GQLArgsSet, GQLObject): 
      authentications: list[AuthenticationUpdateInput] ##NON NULL

   _args: Args


   type: Authentication ##NON NULL

class createOrUpdateAPIVersionAuthentication(GQLMutation):
   """
   createOrUpdateAPIVersionAuthentication - Create or Update the authentication used to access an API

   """
   class Args(GQLArgsSet, GQLObject): 
      input: createAuthenticationInput

   _args: Args


   type: AuthenticationCreateOrUpdateResult

class createBillingFeature(GQLMutation):
   """
   createBillingFeature - Create a new Billing Feature

   """
   class Args(GQLArgsSet, GQLObject): 
      createBillingFeature: createBillingFeature

   _args: Args


   type: BillingFeature

class updateBillingFeature(GQLMutation):
   """
   updateBillingFeature - Update the API billing feature

   """
   class Args(GQLArgsSet, GQLObject): 
      updateBillingFeature: updateBillingFeature

   _args: Args


   type: BillingFeature

class upsertBillingFeature(GQLMutation):
   """
   upsertBillingFeature - [will be deprecated; do not use] Updates billing feature for 1 API

   """
   class Args(GQLArgsSet, GQLObject): 
      upsertBillingFeature: upsertBillingFeatureInput ##NON NULL

   _args: Args


   type: BillingFeature

class deleteBillingFeature(GQLMutation):
   """
   deleteBillingFeature - Delete API billing feature by id

   """
   class Args(GQLArgsSet, GQLObject): 
      billingFeatureId: str

   _args: Args


   type: Any

class deleteBillingFeatures(GQLMutation):
   """
   deleteBillingFeatures - Delete API billing features

   """
   class Args(GQLArgsSet, GQLObject): 
      billingFeatureIds: list[str]

   _args: Args


   type: Any

class createStripeCustomer(GQLMutation):
   """
   createStripeCustomer - Create a customer in Stripe with credit card details and personal details

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class updateStripeCustomer(GQLMutation):
   """
   updateStripeCustomer - Updates customer details in Stripe

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class createStripeCustomerV2(GQLMutation):
   """
   createStripeCustomerV2 - Create a customer in Stripe with credit card details and personal details

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class updateStripeCustomerV2(GQLMutation):
   """
   updateStripeCustomerV2 - Updates customer details in Stripe

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CreateStripeCustomerInput

   _args: Args


   type: BillingInformation

class deleteCustomerPaymentMethod(GQLMutation):
   """
   deleteCustomerPaymentMethod - Detele the payment method for a customer

   """
   type: bool

class upsertBillingItem(GQLMutation):
   """
   upsertBillingItem - [will be deprecated; do not use] Updates 1 billing item

   """
   class Args(GQLArgsSet, GQLObject): 
      input: BillingItemUpsertInput ##NON NULL

   _args: Args


   type: BillingItem

class deleteBillingItem(GQLMutation):
   """
   deleteBillingItem - Delete a single billing item, in the UI we call these Objects

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: Any

class deleteBillingItems(GQLMutation):
   """
   deleteBillingItems - Delete all billing items for an API Project

   """
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: bool ##NON NULL

class deleteBillingPlans(GQLMutation):
   """
   deleteBillingPlans - Delete billing plan from the API level 

   """
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: bool

class updateAllowedPlanDevelopers(GQLMutation):
   """
   updateAllowedPlanDevelopers - Invite developer to a private created plan

   """
   class Args(GQLArgsSet, GQLObject): 
      input: AllowedPlanDevelopersUpdateInput

   _args: Args


   type: list[AllowedPlanDeveloper]

class editOrganizationInvoice(GQLMutation):
   """
   editOrganizationInvoice - Update Orgs free seats count ( will be deprecated )

   """
   class Args(GQLArgsSet, GQLObject): 
      input: EditOrganizationInvoiceInput

   _args: Args


   type: bool

class createBillingPlan(GQLMutation):
   """
   createBillingPlan - Create a new Billing Plan

   """
   class Args(GQLArgsSet, GQLObject): 
      billingPlan: BillingPlanCreateInput ##NON NULL

   _args: Args


   type: BillingPlan

class updateBillingPlanMetadata(GQLMutation):
   """
   updateBillingPlanMetadata - Updates the data of the billing plan

   """
   class Args(GQLArgsSet, GQLObject): 
      billingPlan: BillingPlanMetadataUpdateInput ##NON NULL

   _args: Args


   type: BillingPlan

class updateBillingPlanExtended(GQLMutation):
   """
   updateBillingPlanExtended - Updates billing plan sub object

   """
   class Args(GQLArgsSet, GQLObject): 
      billingPlan: BillingPlanExtendedUpdateInput ##NON NULL

   _args: Args


   type: BillingPlan

class upsertBillingPlanAndVersion(GQLMutation):
   """
   upsertBillingPlanAndVersion - [will be deprecated; do not use] Updates plan and version for 1 API

   """
   class Args(GQLArgsSet, GQLObject): 
      upsertBillingPlanAndVersionInput: upsertBillingPlanAndVersionInput ##NON NULL

   _args: Args


   type: BillingPlanVersion

class blockUsers(GQLMutation):
   """
   blockUsers - Block paid users from accessing the API

   """
   class Args(GQLArgsSet, GQLObject): 
      input: BlockedUserInput

   _args: Args


   type: bool

class unblockUsers(GQLMutation):
   """
   unblockUsers - Unblock paied users from accessing the API

   """
   class Args(GQLArgsSet, GQLObject): 
      input: BlockedUserInput

   _args: Args


   type: bool

class createCategory(GQLMutation):
   """
   createCategory - Create a new Category (API Level)

   """
   class Args(GQLArgsSet, GQLObject): 
      category: CategoryCreateInput ##NON NULL

   _args: Args


   type: Category ##NON NULL

class updateCategory(GQLMutation):
   """
   updateCategory - Update category itself

   """
   class Args(GQLArgsSet, GQLObject): 
      category: CategoryUpdateInput ##NON NULL

   _args: Args


   type: Category ##NON NULL

class deleteCategories(GQLMutation):
   """
   deleteCategories - Deletes a category

   """
   class Args(GQLArgsSet, GQLObject): 
      categories: list[ID] ##NON NULL

   _args: Args


   type: DeletedCategory ##NON NULL

class deleteCollection(GQLMutation):
   """
   deleteCollection - Deletes an existing collection 

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool

class updateCollection(GQLMutation):
   """
   updateCollection - Update single collection

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CollectionUpdateInput ##NON NULL

   _args: Args


   type: Collection

class createCollection(GQLMutation):
   """
   createCollection - Create a new Hub Category

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CollectionCreateInput ##NON NULL

   _args: Args


   type: Collection

class bulkUpdateCollections(GQLMutation):
   """
   bulkUpdateCollections - Updates collection 

   """
   class Args(GQLArgsSet, GQLObject): 
      collections: list[UpdateCollectionsInput] ##NON NULL

   _args: Args


   type: list[Collection]

class updateCollections(GQLMutation):
   """
   updateCollections - Update multiple collections

   """
   class Args(GQLArgsSet, GQLObject): 
      collections: list[UpdateCollectionsInput] ##NON NULL

   _args: Args


   type: list[Collection]

class postCommentV2(GQLMutation):
   """
   postCommentV2 - Post a comment

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CommentCreateInput

   _args: Args


   type: Comment

class deleteCommentV2(GQLMutation):
   """
   deleteCommentV2 - Delete a comment

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CommentDeleteInput

   _args: Args


   type: Any

class updateCommentV2(GQLMutation):
   """
   updateCommentV2 - Update a comment

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CommentUpdateInput

   _args: Args


   type: Any

class postCommentV3(GQLMutation):
   """
   postCommentV3 - Post a comment

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CommentCreateInput

   _args: Args


   type: Comment

class subscribeToPlan(GQLMutation):
   """
   subscribeToPlan - A user or team can subscribe to an API

   """
   class Args(GQLArgsSet, GQLObject): 
      input: SubscribeInput

   _args: Args


   type: BillingSubscription

class unfollowUser(GQLMutation):
   """
   unfollowUser - Unfollow a user

   """
   class Args(GQLArgsSet, GQLObject): 
      input: FollowInput

   _args: Args


   type: bool

class followUser(GQLMutation):
   """
   followUser - Follow a user

   """
   class Args(GQLArgsSet, GQLObject): 
      input: FollowInput

   _args: Args


   type: bool

class followApi(GQLMutation):
   """
   followApi - [do not use; will be deprecated] Use createApiFollower

   """
   class Args(GQLArgsSet, GQLObject): 
      input: FollowApiInput

   _args: Args


   type: bool

class unfollowApi(GQLMutation):
   """
   unfollowApi - Unfollow selected API

   """
   class Args(GQLArgsSet, GQLObject): 
      input: FollowApiInput

   _args: Args


   type: bool

class sendMessage(GQLMutation):
   """
   sendMessage - Send a message to an API provider

   """
   class Args(GQLArgsSet, GQLObject): 
      input: SendMessageInput

   _args: Args


   type: bool

class rateApi(GQLMutation):
   """
   rateApi - Give an API rating

   """
   class Args(GQLArgsSet, GQLObject): 
      input: RatingInput

   _args: Args


   type: Any

class upsertEntityMetadataBulk(GQLMutation):
   """
   upsertEntityMetadataBulk - [will be deprecated; do not use] Assign one or more attributes to an entity

   """
   class Args(GQLArgsSet, GQLObject): 
      entityId: ID
      entityAttributes: list[EntityAttribute] ##NON NULL

   _args: Args


   type: Any

class upsertEntityMetadata(GQLMutation):
   """
   upsertEntityMetadata - Assign one or more attributes to an entity (user, role, team)

   """
   class Args(GQLArgsSet, GQLObject): 
      entityMetadata: EntityMetadataInput

   _args: Args


   type: Any

class deleteIssueV2(GQLMutation):
   """
   deleteIssueV2 - Deletes an issue 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: IssueDeleteInput

   _args: Args


   type: Any

class updateIssueV2(GQLMutation):
   """
   updateIssueV2 - Make a change to a public comment on an API.

   """
   class Args(GQLArgsSet, GQLObject): 
      input: IssueUpdateInput

   _args: Args


   type: Any

class deleteIssues(GQLMutation):
   """
   deleteIssues - Deletes an issue 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: IssuesDeleteInput

   _args: Args


   type: Any

class postIssueV3(GQLMutation):
   """
   postIssueV3 - Post an issue to a provider

   """
   class Args(GQLArgsSet, GQLObject): 
      input: IssueCreateInputV2

   _args: Args


   type: Any

class updateOrCreateEndpointWithParameters(GQLMutation):
   """
   updateOrCreateEndpointWithParameters - Create or make changes to an endpoint with a parameter on a provider's API.

   """
   class Args(GQLArgsSet, GQLObject): 
      input: updateOrCreateEndpointWithParameters

   _args: Args


   type: Any

class updateEndpointEntity(GQLMutation):
   """
   updateEndpointEntity - [do not use; will be deprecated] use updateOrCreateEndpointWithParameters

   """
   class Args(GQLArgsSet, GQLObject): 
      input: updateEndpointEntity

   _args: Args


   type: Any

class deleteEndpoint(GQLMutation):
   """
   deleteEndpoint - Delete an endpoint

   """
   class Args(GQLArgsSet, GQLObject): 
      endpointId: str

   _args: Args


   type: Any

class deleteEndpoints(GQLMutation):
   """
   deleteEndpoints - Delete a few endpoints at once

   """
   class Args(GQLArgsSet, GQLObject): 
      endpointIds: list[str]

   _args: Args


   type: Any

class updateEndpointsCollectionOrder(GQLMutation):
   """
   updateEndpointsCollectionOrder - Update selected endpoints order on playground

   """
   class Args(GQLArgsSet, GQLObject): 
      endpointsCollectionOrder: list[EndpointOrder]

   _args: Args


   type: Any

class createEndpointsGroups(GQLMutation):
   """
   createEndpointsGroups - Create a group object that later user can attach endpoints

   """
   class Args(GQLArgsSet, GQLObject): 
      groups: list[EndpointsGroupCreateInput] ##NON NULL

   _args: Args


   type: EndpointsGroup ##NON NULL

class updateEndpointsGroups(GQLMutation):
   """
   updateEndpointsGroups - Update endpoints group properties

   """
   class Args(GQLArgsSet, GQLObject): 
      groups: list[EndpointsGroupUpdateInput] ##NON NULL

   _args: Args


   type: EndpointsGroup ##NON NULL

class deleteEndpointsGroups(GQLMutation):
   """
   deleteEndpointsGroups - Delete a group that endpoints are attached to

   """
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: ID ##NON NULL

class duplicateNameCheck(GQLMutation):
   """
   duplicateNameCheck - get entities ( User/Governance/Identity ) by term

   """
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
   """
   createEntitiesRoles - Assign roles to users ( in all levels )

   """
   class Args(GQLArgsSet, GQLObject): 
      input: EntityRoleCreateInput

   _args: Args


   type: bool

class upsertEntityRole(GQLMutation):
   """
   upsertEntityRole - Assigning roles to an entity (user, role, team)

   """
   class Args(GQLArgsSet, GQLObject): 
      input: EntityRoleInput

   _args: Args


   type: bool

class updateGraphQLSchema(GQLMutation):
   """
   updateGraphQLSchema - Update GraphQLSchema by graphQLSchemaId or endpointId (at least one is mandatory, graphQLSchemaId is prioritized)

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateGraphQLSchemaInput ##NON NULL

   _args: Args


   type: ID ##NON NULL

class createHeadlines(GQLMutation):
   """
   createHeadlines - [will be deprecated; do not use] use createHeadlinesPerApiId

   """
   class Args(GQLArgsSet, GQLObject): 
      createHeadlines: createHeadlines

   _args: Args


   type: str

class createHeadlinesPerApiId(GQLMutation):
   """
   createHeadlinesPerApiId - Creates a readme for the API, shows on the hub about page

   """
   class Args(GQLArgsSet, GQLObject): 
      createHeadlines: createHeadlines

   _args: Args


   type: str

class updateHeadlines(GQLMutation):
   """
   updateHeadlines - Updates a readme for the API, shows on the hub about page

   """
   class Args(GQLArgsSet, GQLObject): 
      updateHeadlines: updateHeadlines

   _args: Args


   type: bool

class followIssueV2(GQLMutation):
   """
   followIssueV2 - Follow an issue 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: IssueFollowInputV2

   _args: Args


   type: Any

class updateKafkaConfiguration(GQLMutation):
   """
   updateKafkaConfiguration - Update the configuration of the Kafka service

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateKafkaConfigurationInput

   _args: Args


   type: KafkaConfiguration

class subscribeToKafkaTopic(GQLMutation):
   """
   subscribeToKafkaTopic - Get kafka subscription by topic for an API verison

   """
   class Args(GQLArgsSet, GQLObject): 
      apiVersionId: str ##NON NULL
      topicName: str ##NON NULL
      options: SubscribeOptions ##NON NULL

   _args: Args


   type: SubscribeKafkaResponse

class produceKafkaMessage(GQLMutation):
   """
   produceKafkaMessage - Produce a message to a Kafka API

   """
   class Args(GQLArgsSet, GQLObject): 
      message: ProduceMessageInput ##NON NULL

   _args: Args


   type: list[ProduceMessageResponse]

class postMessage(GQLMutation):
   """
   postMessage - Adds a message to an API's discussion board

   """
   class Args(GQLArgsSet, GQLObject): 
      message: MessageCreateInput ##NON NULL

   _args: Args


   type: Any

class postMessageV2(GQLMutation):
   """
   postMessageV2 - Adds a message to an API's discussion board

   """
   class Args(GQLArgsSet, GQLObject): 
      message: MessageCreateInput ##NON NULL

   _args: Args


   type: Any

class updateThreadEntityStatus(GQLMutation):
   """
   updateThreadEntityStatus - updates issues thread status 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: ThreadEntityStatusUpdateInput

   _args: Args


   type: bool

class markNotificationAsViewed(GQLMutation):
   """
   markNotificationAsViewed - Mark new notification as view

   """
   class Args(GQLArgsSet, GQLObject): 
      input: MarkNewNotificationAsViewedInput

   _args: Args


   type: bool

class markNewNotificationAsRead(GQLMutation):
   """
   markNewNotificationAsRead - Mark new notification as read

   """
   class Args(GQLArgsSet, GQLObject): 
      input: MarkNewNotificationsAsReadInput

   _args: Args


   type: bool

class markNotificationsAsRead(GQLMutation):
   """
   markNotificationsAsRead - [do not use; will be deprecated] Mark new notification as read

   """
   class Args(GQLArgsSet, GQLObject): 
      input: MarkNotificationsAsReadInput

   _args: Args


   type: bool

class updateOrganization(GQLMutation):
   """
   updateOrganization - Updating organization 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: OrganizationUpdateInput ##NON NULL

   _args: Args


   type: Organization

class deleteOrganization(GQLMutation):
   """
   deleteOrganization - Delete an organization

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool ##NON NULL

class createOrganization(GQLMutation):
   """
   createOrganization - Create an organization 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: OrganizationCreateInput ##NON NULL

   _args: Args


   type: Organization ##NON NULL

class createNewOrganizationV4(GQLMutation):
   """
   createNewOrganizationV4 - [will be deprecated; do not use] Create an organization 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: CreateNewOrganizationInputV4

   _args: Args


   type: Any

class generateResetPasswordToken(GQLMutation):
   """
   generateResetPasswordToken - Generate a reset password token

   """
   class Args(GQLArgsSet, GQLObject): 
      email: str ##NON NULL

   _args: Args


   type: Any

class resetUserPassword(GQLMutation):
   """
   resetUserPassword - resets user password 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: ResetUserPasswordInput ##NON NULL

   _args: Args


   type: Any

class deletePayoutInfo(GQLMutation):
   """
   deletePayoutInfo - Delete payout information

   """
   class Args(GQLArgsSet, GQLObject): 
      userId: ID ##NON NULL

   _args: Args


   type: bool ##NON NULL

class addProject(GQLMutation):
   """
   addProject - [will be deprecated; do not use] Creates Application ( application and x-rapid-key  ) 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: AddProjectInput ##NON NULL

   _args: Args


   type: Project

class addProjectV2(GQLMutation):
   """
   addProjectV2 - Creates Application ( application and x-rapid-key  ) 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: AddProjectInput ##NON NULL

   _args: Args


   type: Project

class editProjectV2(GQLMutation):
   """
   editProjectV2 - Edit user application properties

   """
   class Args(GQLArgsSet, GQLObject): 
      input: EditProjectInput ##NON NULL

   _args: Args


   type: Any

class deleteProject(GQLMutation):
   """
   deleteProject - Delete a user application project

   """
   class Args(GQLArgsSet, GQLObject): 
      input: DeleteProjectInput ##NON NULL

   _args: Args


   type: ID

class createProject(GQLMutation):
   """
   createProject - Create an Application

   """
   class Args(GQLArgsSet, GQLObject): 
      project: ProjectCreateInput ##NON NULL

   _args: Args


   type: Project

class updateProject(GQLMutation):
   """
   updateProject - updating project ( aka application ) 

   """
   class Args(GQLArgsSet, GQLObject): 
      project: ProjectUpdateInput ##NON NULL

   _args: Args


   type: list[Project]

class createProjectAllowedAPIs(GQLMutation):
   """
   createProjectAllowedAPIs - Create the allowed APIs in an Application

   """
   class Args(GQLArgsSet, GQLObject): 
      input: list[createProjectAllowedAPIInput]

   _args: Args


   type: list[ProjectAllowedAPI]

class updateProjectAllowedAPI(GQLMutation):
   """
   updateProjectAllowedAPI - Change the APIs list that the app/project has access to

   """
   class Args(GQLArgsSet, GQLObject): 
      input: updateProjectAllowedAPIInput

   _args: Args


   type: ProjectAllowedAPI

class deleteProjectAllowedAPIs(GQLMutation):
   """
   deleteProjectAllowedAPIs - Deattach APIs from a project allowed list

   """
   class Args(GQLArgsSet, GQLObject): 
      input: deleteProjectAllowedAPIsInput

   _args: Args


   type: bool

class changeApiUsedVersion(GQLMutation):
   """
   changeApiUsedVersion - Changes the API version used by the developer application

   """
   class Args(GQLArgsSet, GQLObject): 
      input: changeApiUsedVersionInput

   _args: Args


   type: bool

class createRapidReason(GQLMutation):
   """
   createRapidReason - Give a reason for unsubscribing to an API

   """
   class Args(GQLArgsSet, GQLObject): 
      rapidReasonInput: RapidReasonInput

   _args: Args


   type: ID

class deprecatedUpdateRole(GQLMutation):
   """
   deprecatedUpdateRole - [do not use; will be deprecated] update role

   """
   class Args(GQLArgsSet, GQLObject): 
      role: RoleUpdateInput ##NON NULL

   _args: Args


   type: Any

class updateRole(GQLMutation):
   """
   updateRole - Updates a role's description or permissions, or change whether it's set as default.

   """
   class Args(GQLArgsSet, GQLObject): 
      role: RoleUpdateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class deprecatedCreateRole(GQLMutation):
   """
   deprecatedCreateRole - [do not use; will be deprecated] create role

   """
   class Args(GQLArgsSet, GQLObject): 
      role: RoleCreateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class createRole(GQLMutation):
   """
   createRole - Create a role 

   """
   class Args(GQLArgsSet, GQLObject): 
      role: RoleCreateInput ##NON NULL

   _args: Args


   type: Role ##NON NULL

class deprecatedDeleteRole(GQLMutation):
   """
   deprecatedDeleteRole - [do not use; will be deprecated] delete role

   """
   class Args(GQLArgsSet, GQLObject): 
      roleId: ID

   _args: Args


   type: Any

class deleteRole(GQLMutation):
   """
   deleteRole - Delete Role 

   """
   class Args(GQLArgsSet, GQLObject): 
      id: list[ID] ##NON NULL

   _args: Args


   type: bool

class createSecretData(GQLMutation):
   """
   createSecretData - [will be deprecated; do not use] Create an API secret

   """
   class Args(GQLArgsSet, GQLObject): 
      input: createSecretDataInput

   _args: Args


   type: Any

class updateBaseUrl(GQLMutation):
   """
   updateBaseUrl - [do not use; will be deprecated] use updateTargetGroups

   """
   class Args(GQLArgsSet, GQLObject): 
      input: updateBaseUrlInput

   _args: Args


   type: bool

class createSpotlight(GQLMutation):
   """
   createSpotlight - Creates a spotlight on an API listing

   """
   class Args(GQLArgsSet, GQLObject): 
      spotlight: SpotlightCreateInput ##NON NULL

   _args: Args


   type: Spotlight ##NON NULL

class updateSpotlight(GQLMutation):
   """
   updateSpotlight - Updates an existing spotlight on an API listing

   """
   class Args(GQLArgsSet, GQLObject): 
      spotlight: SpotlightUpdateInput ##NON NULL

   _args: Args


   type: Spotlight ##NON NULL

class deleteSpotlight(GQLMutation):
   """
   deleteSpotlight - Delete a spotlight connected to an API

   """
   class Args(GQLArgsSet, GQLObject): 
      spotlight: SpotlightDeleteInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class deleteSubscriptions(GQLMutation):
   """
   deleteSubscriptions - Delete a range of subscriptions by aray of IDs

   """
   class Args(GQLArgsSet, GQLObject): 
      ids: list[ID] ##NON NULL

   _args: Args


   type: bool

class deleteSubscription(GQLMutation):
   """
   deleteSubscription - Delete a single API subscription by ID

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool

class createSubscription(GQLMutation):
   """
   createSubscription - Create a new API subscription

   """
   class Args(GQLArgsSet, GQLObject): 
      input: SubscriptionCreateInput ##NON NULL

   _args: Args


   type: BillingSubscription ##NON NULL

class updateTargetGroups(GQLMutation):
   """
   updateTargetGroups - Updates the target URL on 1 API version

   """
   class Args(GQLArgsSet, GQLObject): 
      targetGroups: list[TargetGroupUpdateInput] ##NON NULL

   _args: Args


   type: TargetGroup ##NON NULL

class removeTeamUserFromAllOrgTeams(GQLMutation):
   """
   removeTeamUserFromAllOrgTeams - remove user from the organization

   """
   class Args(GQLArgsSet, GQLObject): 
      orgId: int ##NON NULL
      email: str ##NON NULL

   _args: Args


   type: bool

class updateTeamUser(GQLMutation):
   """
   updateTeamUser - Add/Remove team for user

   """
   class Args(GQLArgsSet, GQLObject): 
      input: TeamUserUpdateInput

   _args: Args


   type: bool

class updateUserRoles(GQLMutation):
   """
   updateUserRoles - Update the role of user

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UserRolesUpdateInput

   _args: Args


   type: bool

class editTeam(GQLMutation):
   """
   editTeam - Edit a team 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: EditTeamInput

   _args: Args


   type: bool

class addUserToTeams(GQLMutation):
   """
   addUserToTeams - Adds organization users to teams 

   """
   class Args(GQLArgsSet, GQLObject): 
      userId: int ##NON NULL
      teamIds: list[int] ##NON NULL

   _args: Args


   type: bool

class deleteTeam(GQLMutation):
   """
   deleteTeam - Delete team

   """
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: bool

class createTeam(GQLMutation):
   """
   createTeam - Create a team

   """
   class Args(GQLArgsSet, GQLObject): 
      input: TeamCreateInput ##NON NULL

   _args: Args


   type: Team

class updateTeam(GQLMutation):
   """
   updateTeam - Updates team

   """
   class Args(GQLArgsSet, GQLObject): 
      input: TeamUpdateInput ##NON NULL

   _args: Args


   type: Team

class updateTransactions(GQLMutation):
   """
   updateTransactions - Update transactions payout status

   """
   class Args(GQLArgsSet, GQLObject): 
      input: updateTransactionInput

   _args: Args


   type: bool

class createTransformations(GQLMutation):
   """
   createTransformations - Create a new API verison transformation

   """
   class Args(GQLArgsSet, GQLObject): 
      transformations: list[TransformationCreateInput] ##NON NULL

   _args: Args


   type: Transformation ##NON NULL

class updateTransformations(GQLMutation):
   """
   updateTransformations - Update API version transformations

   """
   class Args(GQLArgsSet, GQLObject): 
      transformations: list[TransformationUpdateInput] ##NON NULL

   _args: Args


   type: Transformation ##NON NULL

class deleteTransformations(GQLMutation):
   """
   deleteTransformations - delete transformation from the api version 

   """
   class Args(GQLArgsSet, GQLObject): 
      transformations: list[ID] ##NON NULL

   _args: Args


   type: DeletedTransformation ##NON NULL

class createTutorial(GQLMutation):
   """
   createTutorial - Creates a tutorial on an API listing

   """
   class Args(GQLArgsSet, GQLObject): 
      tutorial: TutorialCreateInput ##NON NULL

   _args: Args


   type: Tutorial

class updateTutorial(GQLMutation):
   """
   updateTutorial - Updates an existing tutorial on an API listing

   """
   class Args(GQLArgsSet, GQLObject): 
      tutorial: TutorialUpdateInput ##NON NULL

   _args: Args


   type: Tutorial

class deleteTutorial(GQLMutation):
   """
   deleteTutorial - Removes an existing tutorial on an API listing

   """
   class Args(GQLArgsSet, GQLObject): 
      tutorial: TutorialDeleteInput ##NON NULL

   _args: Args


   type: bool ##NON NULL

class phoneAuthSetup(GQLMutation):
   """
   phoneAuthSetup - setting up phone authentication ( 2fa flow)

   """
   class Args(GQLArgsSet, GQLObject): 
      phoneNumber: str ##NON NULL

   _args: Args


   type: PhoneVerification

class phoneAuthSetupVerify(GQLMutation):
   """
   phoneAuthSetupVerify - verifying phone authentication setup

   """
   class Args(GQLArgsSet, GQLObject): 
      code: str ##NON NULL
      token: str ##NON NULL

   _args: Args


   type: bool

class authenticateUsingPhone(GQLMutation):
   """
   authenticateUsingPhone - Authenticates the user using phone code 

   """
   class Args(GQLArgsSet, GQLObject): 
      phoneId: ID ##NON NULL

   _args: Args


   type: PhoneVerification

class authenticateUsingPhoneVerify(GQLMutation):
   """
   authenticateUsingPhoneVerify - Verifies that the phone setup succeeded ( by the user sending a code + token)

   """
   class Args(GQLArgsSet, GQLObject): 
      code: str ##NON NULL
      token: str ##NON NULL

   _args: Args


   type: bool

class deletePhoneNumber(GQLMutation):
   """
   deletePhoneNumber - Delete user phone number

   """
   class Args(GQLArgsSet, GQLObject): 
      phoneId: int ##NON NULL

   _args: Args


   type: bool

class generateRecoveryCodes(GQLMutation):
   """
   generateRecoveryCodes - Generate a recovery codes for MFA 

   """
   type: list[RecoveryCode]

class regenerateRecoveryCodes(GQLMutation):
   """
   regenerateRecoveryCodes - generates recovery codes part of setting up 2fa to a user

   """
   type: list[RecoveryCode]

class markRecoveryCodeAsUsed(GQLMutation):
   """
   markRecoveryCodeAsUsed - authenticates the user using recovery code ( 2fa flow )

   """
   class Args(GQLArgsSet, GQLObject): 
      code: str ##NON NULL

   _args: Args


   type: bool

class applicationAuthSetup(GQLMutation):
   """
   applicationAuthSetup - Sets up google authentication app

   """
   type: str

class applicationAuthSetupVerify(GQLMutation):
   """
   applicationAuthSetupVerify - Verifies that the Google authenticator setup succeeded ( by user sending a code)

   """
   class Args(GQLArgsSet, GQLObject): 
      code: str ##NON NULL

   _args: Args


   type: bool

class authenticateUsingApp(GQLMutation):
   """
   authenticateUsingApp - Authenticates the user using google auth app 

   """
   class Args(GQLArgsSet, GQLObject): 
      code: str ##NON NULL

   _args: Args


   type: bool

class deleteApplicationAuth(GQLMutation):
   """
   deleteApplicationAuth - Delete app authentication

   """
   type: bool

class createUserInvites(GQLMutation):
   """
   createUserInvites - Invite users to organization

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UserInvitesInput

   _args: Args


   type: bool

class createUserInvitesV2(GQLMutation):
   """
   createUserInvitesV2 - [do not use; will be deprecated] Invite users to organization

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UserInvitesCreateInput

   _args: Args


   type: bool

class acceptUserInvite(GQLMutation):
   """
   acceptUserInvite - Accepts user invite to organization 

   """
   class Args(GQLArgsSet, GQLObject): 
      token: str ##NON NULL

   _args: Args


   type: bool

class bulkDeleteUserInvitesV2(GQLMutation):
   """
   bulkDeleteUserInvitesV2 - Deletes users that are in pending mode from the organization 

   """
   class Args(GQLArgsSet, GQLObject): 
      emails: list[str]
      orgId: int

   _args: Args


   type: Any

class deleteUserInvites(GQLMutation):
   """
   deleteUserInvites - Used for deleting user/s that not yet confirmed the invitation

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UserInvitesDeleteInput ##NON NULL

   _args: Args


   type: Any

class bulkReactivateUserInvitesV2(GQLMutation):
   """
   bulkReactivateUserInvitesV2 - Reactivates users from the organizartion 

   """
   class Args(GQLArgsSet, GQLObject): 
      emails: list[str]
      orgId: int

   _args: Args


   type: bool

class reactivateUserInvites(GQLMutation):
   """
   reactivateUserInvites - Used for activating user/s that was deactivated

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UserInvitesReactivateInput ##NON NULL

   _args: Args


   type: bool

class inviteUsersToTeams(GQLMutation):
   """
   inviteUsersToTeams - Adds an array of user IDs to a team at the time the Org is created

   """
   class Args(GQLArgsSet, GQLObject): 
      usersToInvite: Any
      orgId: ID ##NON NULL
      meta: Any

   _args: Args


   type: bool

class saveUserApi(GQLMutation):
   """
   saveUserApi - Save an API as a favorite

   """
   class Args(GQLArgsSet, GQLObject): 
      saveUserApi: SaveUserApi

   _args: Args


   type: UserSavedApi ##NON NULL

class updateUserById(GQLMutation):
   """
   updateUserById - Update a set of attributes on a user by ID.

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UpdateUserInput

   _args: Args


   type: Any

class updateUserPassword(GQLMutation):
   """
   updateUserPassword - Update the password of a user

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UserPasswordInput

   _args: Args


   type: bool

class deleteAll2faData(GQLMutation):
   """
   deleteAll2faData - Delete all 2FA data

   """
   class Args(GQLArgsSet, GQLObject): 
      userId: str ##NON NULL

   _args: Args


   type: Any

class updateUserEmail(GQLMutation):
   """
   updateUserEmail - Update the email address of a user

   """
   class Args(GQLArgsSet, GQLObject): 
      email: str ##NON NULL

   _args: Args


   type: Any

class verifyEmailCode(GQLMutation):
   """
   verifyEmailCode - Takes a verification code and returns a boolean

   """
   class Args(GQLArgsSet, GQLObject): 
      input: VerifyEmailCodeInput

   _args: Args


   type: bool

class updateUser(GQLMutation):
   """
   updateUser - Updates user metadata / password 

   """
   class Args(GQLArgsSet, GQLObject): 
      input: UserUpdateInput ##NON NULL

   _args: Args


   type: User

class createWorkflow(GQLMutation):
   """
   createWorkflow - Create a workflow

   """
   class Args(GQLArgsSet, GQLObject): 
      options: CreateWorkflowInput

   _args: Args


   type: Any

class createSignupApprovalWorkflow(GQLMutation):
   """
   createSignupApprovalWorkflow - Create a signup approval request

   """
   class Args(GQLArgsSet, GQLObject): 
      options: CreateSignupApprovalWorkflowInput

   _args: Args


   type: Any

class updateWorkflows(GQLMutation):
   """
   updateWorkflows - Change an entity's workflow

   """
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
