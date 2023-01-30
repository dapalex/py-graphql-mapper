from typing import List
from pygqlmap import GQLMutation
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *


class NonNull_EventUrlCreateInput(EventUrlCreateInput): pass

class NonNull_EventUrlUpdateInput(EventUrlUpdateInput): pass

class NonNull_EventConfigUpdateInput(EventConfigUpdateInput): pass

class NonNull_GatewayInstanceCreateInput(GatewayInstanceCreateInput): pass

class NonNull_GatewayInstanceUpdateInput(GatewayInstanceUpdateInput): pass

class NonNull_GatewayTemplateCreateInput(GatewayTemplateCreateInput): pass

class NonNull_GatewayTemplateUpdateInput(GatewayTemplateUpdateInput): pass

class NonNull_GatewayTemplateParamsCreateInput(GatewayTemplateParamsCreateInput): pass

class NonNull_EnvConfigUpdateInput(EnvConfigUpdateInput): pass

class NonNull_deleteUserAlertsInput(deleteUserAlertsInput): pass

class NonNull_editUserAlertInput(editUserAlertInput): pass

class NonNull_UserAlertUpdateInput(UserAlertUpdateInput): pass

class NonNull_list_UserAlertUpdateInput(list, UserAlertUpdateInput): pass

class NonNull_ApiCertificateCreateInput(ApiCertificateCreateInput): pass

class NonNull_list_ApiCertificateCreateInput(list, ApiCertificateCreateInput): pass

class NonNull_SaveApiDevelopersInput(SaveApiDevelopersInput): pass

class NonNull_CreateApiFavoritesInput(CreateApiFavoritesInput): pass

class NonNull_DeleteApiFavoritesInput(DeleteApiFavoritesInput): pass

class NonNull_ApiFollowerCreateInput(ApiFollowerCreateInput): pass

class NonNull_ApiFollowerDeleteInput(ApiFollowerDeleteInput): pass

class NonNull_ApiCreateFromSpecInput(ApiCreateFromSpecInput): pass

class NonNull_list_ApiCreateFromSpecInput(list, ApiCreateFromSpecInput): pass

class NonNull_ApiUpdateFromSpecInput(ApiUpdateFromSpecInput): pass

class NonNull_list_ApiUpdateFromSpecInput(list, ApiUpdateFromSpecInput): pass

class NonNull_ApiCreateFromRapidOasInput(ApiCreateFromRapidOasInput): pass

class NonNull_list_ApiCreateFromRapidOasInput(list, ApiCreateFromRapidOasInput): pass

class NonNull_ApiUpdateFromRapidOasInput(ApiUpdateFromRapidOasInput): pass

class NonNull_list_ApiUpdateFromRapidOasInput(list, ApiUpdateFromRapidOasInput): pass

class NonNull_ApiVersionCreateInput(ApiVersionCreateInput): pass

class NonNull_list_ApiVersionCreateInput(list, ApiVersionCreateInput): pass

class NonNull_GqlApiVersionCreateInput(GqlApiVersionCreateInput): pass

class NonNull_list_GqlApiVersionCreateInput(list, GqlApiVersionCreateInput): pass

class NonNull_ApiVersionUpdateInput(ApiVersionUpdateInput): pass

class NonNull_list_ApiVersionUpdateInput(list, ApiVersionUpdateInput): pass

class NonNull_ApiCreateInput(ApiCreateInput): pass

class NonNull_ApiUpdateInput(ApiUpdateInput): pass

class NonNull_ProvisionApiFromFileInput(ProvisionApiFromFileInput): pass

class list_ProvisionApiFromFileInput(list, ProvisionApiFromFileInput): pass

class NonNull_AppAuthorizationCreateInput(AppAuthorizationCreateInput): pass

class NonNull_AppAuthorizationUpdateInput(AppAuthorizationUpdateInput): pass

class NonNull_AddApplicationEnvironmentKeyInput(AddApplicationEnvironmentKeyInput): pass

class NonNull_EditApplicationEnviornmentKeyInput(EditApplicationEnviornmentKeyInput): pass

class NonNull_DeleteApplicationEnvironmentKeyInput(DeleteApplicationEnvironmentKeyInput): pass

class NonNull_GenerateAssetUploadUrlInput(GenerateAssetUploadUrlInput): pass

class NonNull_AssetUpdateInput(AssetUpdateInput): pass

class NonNull_AsyncApiConfigurationCreateInput(AsyncApiConfigurationCreateInput): pass

class NonNull_list_AsyncApiConfigurationCreateInput(list, AsyncApiConfigurationCreateInput): pass

class NonNull_ThemeUserAttributesInput(ThemeUserAttributesInput): pass

class NonNull_AuthenticationCreateInput(AuthenticationCreateInput): pass

class NonNull_list_AuthenticationCreateInput(list, AuthenticationCreateInput): pass

class NonNull_AuthenticationUpdateInput(AuthenticationUpdateInput): pass

class NonNull_list_AuthenticationUpdateInput(list, AuthenticationUpdateInput): pass

class NonNull_upsertBillingFeatureInput(upsertBillingFeatureInput): pass

class NonNull_BillingItemUpsertInput(BillingItemUpsertInput): pass

class NonNull_BillingPlanCreateInput(BillingPlanCreateInput): pass

class NonNull_BillingPlanMetadataUpdateInput(BillingPlanMetadataUpdateInput): pass

class NonNull_BillingPlanExtendedUpdateInput(BillingPlanExtendedUpdateInput): pass

class NonNull_upsertBillingPlanAndVersionInput(upsertBillingPlanAndVersionInput): pass

class NonNull_CategoryCreateInput(CategoryCreateInput): pass

class NonNull_CategoryUpdateInput(CategoryUpdateInput): pass

class NonNull_CollectionUpdateInput(CollectionUpdateInput): pass

class NonNull_CollectionCreateInput(CollectionCreateInput): pass

class NonNull_list_UpdateCollectionsInput(list, UpdateCollectionsInput): pass

class list_EndpointOrder(list, EndpointOrder): pass

class NonNull_EndpointsGroupCreateInput(EndpointsGroupCreateInput): pass

class NonNull_list_EndpointsGroupCreateInput(list, EndpointsGroupCreateInput): pass

class NonNull_EndpointsGroupUpdateInput(EndpointsGroupUpdateInput): pass

class NonNull_list_EndpointsGroupUpdateInput(list, EndpointsGroupUpdateInput): pass

class NonNull_EntityMetadataInput(EntityMetadataInput): pass

class NonNull_UpdateGraphQLSchemaInput(UpdateGraphQLSchemaInput): pass

class NonNull_SubscribeOptions(SubscribeOptions): pass

class NonNull_ProduceMessageInput(ProduceMessageInput): pass

class list_ProduceMessageResponse(list, ProduceMessageResponse): pass

class NonNull_MessageCreateInput(MessageCreateInput): pass

class NonNull_OrganizationUpdateInput(OrganizationUpdateInput): pass

class NonNull_OrganizationCreateInput(OrganizationCreateInput): pass

class NonNull_ResetUserPasswordInput(ResetUserPasswordInput): pass

class NonNull_AddProjectInput(AddProjectInput): pass

class NonNull_EditProjectInput(EditProjectInput): pass

class NonNull_DeleteProjectInput(DeleteProjectInput): pass

class NonNull_ProjectCreateInput(ProjectCreateInput): pass

class NonNull_ProjectUpdateInput(ProjectUpdateInput): pass

class list_createProjectAllowedAPIInput(list, createProjectAllowedAPIInput): pass

class NonNull_RoleUpdateInput(RoleUpdateInput): pass

class NonNull_RoleCreateInput(RoleCreateInput): pass

class NonNull_SpotlightCreateInput(SpotlightCreateInput): pass

class NonNull_SpotlightUpdateInput(SpotlightUpdateInput): pass

class NonNull_SpotlightDeleteInput(SpotlightDeleteInput): pass

class NonNull_SubscriptionCreateInput(SubscriptionCreateInput): pass

class NonNull_TargetGroupUpdateInput(TargetGroupUpdateInput): pass

class NonNull_list_TargetGroupUpdateInput(list, TargetGroupUpdateInput): pass

class NonNull_TeamCreateInput(TeamCreateInput): pass

class NonNull_TeamUpdateInput(TeamUpdateInput): pass

class NonNull_TransformationCreateInput(TransformationCreateInput): pass

class NonNull_list_TransformationCreateInput(list, TransformationCreateInput): pass

class NonNull_TransformationUpdateInput(TransformationUpdateInput): pass

class NonNull_list_TransformationUpdateInput(list, TransformationUpdateInput): pass

class NonNull_TutorialCreateInput(TutorialCreateInput): pass

class NonNull_TutorialUpdateInput(TutorialUpdateInput): pass

class NonNull_TutorialDeleteInput(TutorialDeleteInput): pass

class list_RecoveryCode(list, RecoveryCode): pass

class NonNull_UserInvitesDeleteInput(UserInvitesDeleteInput): pass

class NonNull_UserInvitesReactivateInput(UserInvitesReactivateInput): pass

class NonNull_UserUpdateInput(UserUpdateInput): pass

class createEventUrl(GQLMutation):
   """
   createEventUrl - Create an Event that can be subscribed to via a webhook

   """
   class EventUrlArgs(GQLArgsSet, GQLObject):
      createDto: NonNull_EventUrlCreateInput

   _args: EventUrlArgs


   type: EventUrl

class updateEventUrl(GQLMutation):
   """
   updateEventUrl - URLs for the events webhooks feature

   """
   class EventUrlArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID
      updateDto: NonNull_EventUrlUpdateInput

   _args: EventUrlArgs


   type: EventUrl

class deleteEventUrl(GQLMutation):
   """
   deleteEventUrl - Delete event Url

   """
   class IDArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: IDArgs


   type: ID

class upsertEventConfig(GQLMutation):
   """
   upsertEventConfig - Update or Insert event configuration

   """
   class EventConfigArgs(GQLArgsSet, GQLObject):
      input: NonNull_EventConfigUpdateInput

   _args: EventConfigArgs


   type: EventConfig

class deleteEventConfig(GQLMutation):
   """
   deleteEventConfig - Delete event configuration

   """
   class IDArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: IDArgs


   type: ID

class createGatewayInstance(GQLMutation):
   """
   createGatewayInstance - Create a Gateway Instance in the Enterprise Tenant

   """
   class GatewayInstanceArgs(GQLArgsSet, GQLObject):
      createDto: NonNull_GatewayInstanceCreateInput

   _args: GatewayInstanceArgs


   type: GatewayInstance

class updateGatewayInstance(GQLMutation):
   """
   updateGatewayInstance - Update the gateway instance information

   """
   class GatewayInstanceArgs(GQLArgsSet, GQLObject):
      updateDto: NonNull_GatewayInstanceUpdateInput

   _args: GatewayInstanceArgs


   type: GatewayInstance

class deleteGatewayInstance(GQLMutation):
   """
   deleteGatewayInstance - Delete Gateway Instance

   """
   class IDArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: IDArgs


   type: ID

class createGatewayTemplate(GQLMutation):
   """
   createGatewayTemplate - Create a code template that can be referenced in a Gateway instance

   """
   class GwTemplateArgs(GQLArgsSet, GQLObject):
      createDto: NonNull_GatewayTemplateCreateInput

   _args: GwTemplateArgs


   type: GwTemplate

class updateGatewayTemplate(GQLMutation):
   """
   updateGatewayTemplate - Update the gateway configuration

   """
   class GwTemplateArgs(GQLArgsSet, GQLObject):
      updateDto: NonNull_GatewayTemplateUpdateInput

   _args: GwTemplateArgs


   type: GwTemplate

class deleteGatewayTemplate(GQLMutation):
   """
   deleteGatewayTemplate - Delete a code template and all its references in Gateways

   """
   class IDArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: IDArgs


   type: ID

class createGatewayTemplateParam(GQLMutation):
   """
   createGatewayTemplateParam - Create a user specified variable that can be referenced in the Gatway templates 

   """
   class GatewayTemplateParamArgs(GQLArgsSet, GQLObject):
      createDto: NonNull_GatewayTemplateParamsCreateInput

   _args: GatewayTemplateParamArgs


   type: GatewayTemplateParam

class updateEnvConfig(GQLMutation):
   """
   updateEnvConfig - updating advance settings   

   """
   class EnvConfigArgs(GQLArgsSet, GQLObject):
      envConfig: NonNull_EnvConfigUpdateInput

   _args: EnvConfigArgs


   type: EnvConfig

class resetEnvConfig(GQLMutation):
   class EnvConfigArgs(GQLArgsSet, GQLObject):
      id: NonNull_int

   _args: EnvConfigArgs


   type: EnvConfig

class addUserAlert(GQLMutation):
   """
   addUserAlert - Creates an alert to be notified when a metric crosses a threshold

   """
   class UserAlertArgs(GQLArgsSet, GQLObject):
      input: addUserAlertInput

   _args: UserAlertArgs


   type: UserAlert

class deleteUserAlerts(GQLMutation):
   """
   deleteUserAlerts - Delete alerts created by an API provider for an API

   """
   class IDArgs(GQLArgsSet, GQLObject):
      input: NonNull_deleteUserAlertsInput

   _args: IDArgs


   type: ID

class editUserAlert(GQLMutation):
   """
   editUserAlert - Update alert created by an API provider for an API

   """
   class UserAlertArgs(GQLArgsSet, GQLObject):
      input: NonNull_editUserAlertInput

   _args: UserAlertArgs


   type: UserAlert

class updateUserAlerts(GQLMutation):
   """
   updateUserAlerts - Update alerts created by an API provider for an API

   """
   class UserAlertArgs(GQLArgsSet, GQLObject):
      input: NonNull_list_UserAlertUpdateInput[NonNull_UserAlertUpdateInput]

   _args: UserAlertArgs


   type: UserAlert

class createApiCertificates(GQLMutation):
   """
   createApiCertificates - Creates API certificate for 

   """
   class ApiCertificateCreationResultArgs(GQLArgsSet, GQLObject):
      certificates: NonNull_list_ApiCertificateCreateInput[NonNull_ApiCertificateCreateInput]

   _args: ApiCertificateCreationResultArgs


   type: ApiCertificateCreationResult

class deleteApiCertificates(GQLMutation):
   """
   deleteApiCertificates - Delete the API Certificate

   """
   class boolArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[ID]

   _args: boolArgs


   type: bool

class saveApiDevelopersToApi(GQLMutation):
   """
   saveApiDevelopersToApi - Invite developers to an API 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: NonNull_SaveApiDevelopersInput

   _args: boolArgs


   type: bool

class copyApiDevelopersFromVersion(GQLMutation):
   """
   copyApiDevelopersFromVersion - Copies all API developers from an API Version

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: CopyApiDevelopersInput

   _args: boolArgs


   type: bool

class createApiFavorites(GQLMutation):
   """
   createApiFavorites - Adding an API to the user favoites list on the user/team context on studio

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateApiFavoritesInput

   _args: boolArgs


   type: bool

class deleteApiFavorites(GQLMutation):
   """
   deleteApiFavorites - Unmark the API from the user's favorites list 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: NonNull_DeleteApiFavoritesInput

   _args: boolArgs


   type: bool

class createApiFollowers(GQLMutation):
   """
   createApiFollowers - Adds a follower to an API

   """
   class ApiFollowerArgs(GQLArgsSet, GQLObject):
      apiFollowers: NonNull_ApiFollowerCreateInput

   _args: ApiFollowerArgs


   type: ApiFollower

class deleteApiFollowers(GQLMutation):
   """
   deleteApiFollowers - Removes a follower from an API

   """
   class boolArgs(GQLArgsSet, GQLObject):
      apiFollowers: NonNull_ApiFollowerDeleteInput

   _args: boolArgs


   type: bool

class createApisFromSpecs(GQLMutation):
   """
   createApisFromSpecs - Create an API from Supported spec files

   """
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject):
      creations: NonNull_list_ApiCreateFromSpecInput[NonNull_ApiCreateFromSpecInput]

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult

class updateApisFromSpecs(GQLMutation):
   """
   updateApisFromSpecs - Update API version from spec file

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#update-an-api

   """
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject):
      updates: NonNull_list_ApiUpdateFromSpecInput[NonNull_ApiUpdateFromSpecInput]

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult

class createApisFromRapidOas(GQLMutation):
   """
   createApisFromRapidOas - This mutation currently supports providing no more than one item to create at a time

   """
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject):
      creations: NonNull_list_ApiCreateFromRapidOasInput[NonNull_ApiCreateFromRapidOasInput]

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult

class updateApisFromRapidOas(GQLMutation):
   """
   updateApisFromRapidOas - This mutation currently supports providing no more than one item to update at a time

   """
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject):
      updates: NonNull_list_ApiUpdateFromRapidOasInput[NonNull_ApiUpdateFromRapidOasInput]

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult

class createApiVersions(GQLMutation):
   """
   createApiVersions - Creates a multiple API Versions

   """
   class ApiVersionArgs(GQLArgsSet, GQLObject):
      apiVersions: NonNull_list_ApiVersionCreateInput[NonNull_ApiVersionCreateInput]

   _args: ApiVersionArgs


   type: ApiVersion

class createGqlApiVersions(GQLMutation):
   """
   createGqlApiVersions - Create a new GraphQL API Version

   """
   class ApiVersionArgs(GQLArgsSet, GQLObject):
      gqlApiVersions: NonNull_list_GqlApiVersionCreateInput[NonNull_GqlApiVersionCreateInput]

   _args: ApiVersionArgs


   type: ApiVersion

class updateApiVersions(GQLMutation):
   """
   updateApiVersions - update the API Versions

   """
   class ApiVersionArgs(GQLArgsSet, GQLObject):
      apiVersions: NonNull_list_ApiVersionUpdateInput[NonNull_ApiVersionUpdateInput]

   _args: ApiVersionArgs


   type: ApiVersion

class createApiVersionBillingPlanVersion(GQLMutation):
   """
   createApiVersionBillingPlanVersion - [will be deprecated; do not use] Create API version and Billing Plan Version

   """
   class ApiVersionBillingPlanVersionArgs(GQLArgsSet, GQLObject):
      input: createApiVersionBillingPlanVersionInput

   _args: ApiVersionBillingPlanVersionArgs


   type: ApiVersionBillingPlanVersion

class createApi(GQLMutation):
   """
   createApi - Creates an API

https://enterprise-docs.rapidapi.com/docs/graphql-platform-api-examples#create-an-api

   """
   class ApiArgs(GQLArgsSet, GQLObject):
      api: NonNull_ApiCreateInput

   _args: ApiArgs


   type: Api

class updateApi(GQLMutation):
   """
   updateApi - Update API metadata



   """
   class ApiArgs(GQLArgsSet, GQLObject):
      api: NonNull_ApiUpdateInput

   _args: ApiArgs


   type: Api

class provisionSwaggerFiles(GQLMutation):
   """
   provisionSwaggerFiles - [do not use; will be deprecated] use createApisFromSpecs

   """
   class strArgs(GQLArgsSet, GQLObject):
      input: list_ProvisionApiFromFileInput[NonNull_ProvisionApiFromFileInput]

   _args: strArgs


   type: list[str]

class deleteApi(GQLMutation):
   """
   deleteApi - Delete the API

   """
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class createApplicationAuthorization(GQLMutation):
   """
   createApplicationAuthorization - Creates authorization of type OAuth 

   """
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject):
      input: NonNull_AppAuthorizationCreateInput

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization

class updateApplicationAuthorization(GQLMutation):
   """
   updateApplicationAuthorization - updated authorization value  

   """
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject):
      input: NonNull_AppAuthorizationUpdateInput

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization

class deleteApplicationAuthorization(GQLMutation):
   """
   deleteApplicationAuthorization - delete application authorization by id

   """
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class addApplicationEnvironmentKey(GQLMutation):
   """
   addApplicationEnvironmentKey - Creates an authorization of type x-rapid-key

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_AddApplicationEnvironmentKeyInput

   _args: AnyArgs


   type: Any

class editApplicationEnvironmentKey(GQLMutation):
   """
   editApplicationEnvironmentKey - edit authorization value ( aka application env key )

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_EditApplicationEnviornmentKeyInput

   _args: AnyArgs


   type: Any

class deleteApplicationEnvironmentKey(GQLMutation):
   """
   deleteApplicationEnvironmentKey - delete application authorization of type x-rapid-key

   """
   class IDArgs(GQLArgsSet, GQLObject):
      input: NonNull_DeleteApplicationEnvironmentKeyInput

   _args: IDArgs


   type: ID

class generateAssetUploadUrl(GQLMutation):
   """
   generateAssetUploadUrl - Creates asset object; returns presignedURL used to upload asset.

   """
   class AssetArgs(GQLArgsSet, GQLObject):
      input: NonNull_GenerateAssetUploadUrlInput

   _args: AssetArgs


   type: Asset

class deleteAsset(GQLMutation):
   """
   deleteAsset - Delete an asset by ID

   """
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class updateAssetUploaded(GQLMutation):
   """
   updateAssetUploaded - Updates asset object state to uploaded after asset is uploaded to the presignedURL

   """
   class AssetArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: AssetArgs


   type: Asset

class updateAsset(GQLMutation):
   """
   updateAsset - Update asset metadata: title, description, visibility - will control whether is visible in the hub 

   """
   class AssetArgs(GQLArgsSet, GQLObject):
      input: NonNull_AssetUpdateInput

   _args: AssetArgs


   type: Asset

class upsertAsyncApiConfiguration(GQLMutation):
   """
   upsertAsyncApiConfiguration - [experimental] Update Async API configuration

   """
   class AsyncApiConfigurationArgs(GQLArgsSet, GQLObject):
      asyncApiConfigurations: NonNull_list_AsyncApiConfigurationCreateInput[NonNull_AsyncApiConfigurationCreateInput]

   _args: AsyncApiConfigurationArgs


   type: AsyncApiConfiguration

class upsertUserAttributes(GQLMutation):
   """
   upsertUserAttributes - Takes a set of user attributes and updates them for a user

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: UserAttributesInput

   _args: AnyArgs


   type: Any

class updateUserAttributeItem(GQLMutation):
   """
   updateUserAttributeItem - Update user metadata 

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_ThemeUserAttributesInput

   _args: AnyArgs


   type: Any

class createAuthentications(GQLMutation):
   """
   createAuthentications - Create provider specific authentication for an API

   """
   class AuthenticationArgs(GQLArgsSet, GQLObject):
      authentications: NonNull_list_AuthenticationCreateInput[NonNull_AuthenticationCreateInput]

   _args: AuthenticationArgs


   type: Authentication

class updateAuthentications(GQLMutation):
   """
   updateAuthentications - Set the API authentications configuration

   """
   class AuthenticationArgs(GQLArgsSet, GQLObject):
      authentications: NonNull_list_AuthenticationUpdateInput[NonNull_AuthenticationUpdateInput]

   _args: AuthenticationArgs


   type: Authentication

class createOrUpdateAPIVersionAuthentication(GQLMutation):
   """
   createOrUpdateAPIVersionAuthentication - Create or Update the authentication used to access an API

   """
   class AuthenticationCreateOrUpdateResultArgs(GQLArgsSet, GQLObject):
      input: createAuthenticationInput

   _args: AuthenticationCreateOrUpdateResultArgs


   type: AuthenticationCreateOrUpdateResult

class createBillingFeature(GQLMutation):
   """
   createBillingFeature - Create a new Billing Feature

   """
   class BillingFeatureArgs(GQLArgsSet, GQLObject):
      createBillingFeature: createBillingFeature

   _args: BillingFeatureArgs


   type: BillingFeature

class updateBillingFeature(GQLMutation):
   """
   updateBillingFeature - Update the API billing feature

   """
   class BillingFeatureArgs(GQLArgsSet, GQLObject):
      updateBillingFeature: updateBillingFeature

   _args: BillingFeatureArgs


   type: BillingFeature

class upsertBillingFeature(GQLMutation):
   """
   upsertBillingFeature - [will be deprecated; do not use] Updates billing feature for 1 API

   """
   class BillingFeatureArgs(GQLArgsSet, GQLObject):
      upsertBillingFeature: NonNull_upsertBillingFeatureInput

   _args: BillingFeatureArgs


   type: BillingFeature

class deleteBillingFeature(GQLMutation):
   """
   deleteBillingFeature - Delete API billing feature by id

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      billingFeatureId: str

   _args: AnyArgs


   type: Any

class deleteBillingFeatures(GQLMutation):
   """
   deleteBillingFeatures - Delete API billing features

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      billingFeatureIds: list[str]

   _args: AnyArgs


   type: Any

class createStripeCustomer(GQLMutation):
   """
   createStripeCustomer - Create a customer in Stripe with credit card details and personal details

   """
   class BillingInformationArgs(GQLArgsSet, GQLObject):
      input: CreateStripeCustomerInput

   _args: BillingInformationArgs


   type: BillingInformation

class updateStripeCustomer(GQLMutation):
   """
   updateStripeCustomer - Updates customer details in Stripe

   """
   class BillingInformationArgs(GQLArgsSet, GQLObject):
      input: CreateStripeCustomerInput

   _args: BillingInformationArgs


   type: BillingInformation

class createStripeCustomerV2(GQLMutation):
   """
   createStripeCustomerV2 - Create a customer in Stripe with credit card details and personal details

   """
   class BillingInformationArgs(GQLArgsSet, GQLObject):
      input: CreateStripeCustomerInput

   _args: BillingInformationArgs


   type: BillingInformation

class updateStripeCustomerV2(GQLMutation):
   """
   updateStripeCustomerV2 - Updates customer details in Stripe

   """
   class BillingInformationArgs(GQLArgsSet, GQLObject):
      input: CreateStripeCustomerInput

   _args: BillingInformationArgs


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
   class BillingItemArgs(GQLArgsSet, GQLObject):
      input: NonNull_BillingItemUpsertInput

   _args: BillingItemArgs


   type: BillingItem

class deleteBillingItem(GQLMutation):
   """
   deleteBillingItem - Delete a single billing item, in the UI we call these Objects

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: AnyArgs


   type: Any

class deleteBillingItems(GQLMutation):
   """
   deleteBillingItems - Delete all billing items for an API Project

   """
   class boolArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[NonNull_ID]

   _args: boolArgs


   type: bool

class deleteBillingPlans(GQLMutation):
   """
   deleteBillingPlans - Delete billing plan from the API level 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[NonNull_ID]

   _args: boolArgs


   type: bool

class updateAllowedPlanDevelopers(GQLMutation):
   """
   updateAllowedPlanDevelopers - Invite developer to a private created plan

   """
   class AllowedPlanDeveloperArgs(GQLArgsSet, GQLObject):
      input: AllowedPlanDevelopersUpdateInput

   _args: AllowedPlanDeveloperArgs


   type: list_AllowedPlanDeveloper[AllowedPlanDeveloper]

class editOrganizationInvoice(GQLMutation):
   """
   editOrganizationInvoice - Update Orgs free seats count ( will be deprecated )

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: EditOrganizationInvoiceInput

   _args: boolArgs


   type: bool

class createBillingPlan(GQLMutation):
   """
   createBillingPlan - Create a new Billing Plan

   """
   class BillingPlanArgs(GQLArgsSet, GQLObject):
      billingPlan: NonNull_BillingPlanCreateInput

   _args: BillingPlanArgs


   type: BillingPlan

class updateBillingPlanMetadata(GQLMutation):
   """
   updateBillingPlanMetadata - Updates the data of the billing plan

   """
   class BillingPlanArgs(GQLArgsSet, GQLObject):
      billingPlan: NonNull_BillingPlanMetadataUpdateInput

   _args: BillingPlanArgs


   type: BillingPlan

class updateBillingPlanExtended(GQLMutation):
   """
   updateBillingPlanExtended - Updates billing plan sub object

   """
   class BillingPlanArgs(GQLArgsSet, GQLObject):
      billingPlan: NonNull_BillingPlanExtendedUpdateInput

   _args: BillingPlanArgs


   type: BillingPlan

class upsertBillingPlanAndVersion(GQLMutation):
   """
   upsertBillingPlanAndVersion - [will be deprecated; do not use] Updates plan and version for 1 API

   """
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject):
      upsertBillingPlanAndVersionInput: NonNull_upsertBillingPlanAndVersionInput

   _args: BillingPlanVersionArgs


   type: BillingPlanVersion

class blockUsers(GQLMutation):
   """
   blockUsers - Block paid users from accessing the API

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: BlockedUserInput

   _args: boolArgs


   type: bool

class unblockUsers(GQLMutation):
   """
   unblockUsers - Unblock paied users from accessing the API

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: BlockedUserInput

   _args: boolArgs


   type: bool

class createCategory(GQLMutation):
   """
   createCategory - Create a new Category (API Level)

   """
   class CategoryArgs(GQLArgsSet, GQLObject):
      category: NonNull_CategoryCreateInput

   _args: CategoryArgs


   type: Category

class updateCategory(GQLMutation):
   """
   updateCategory - Update category itself

   """
   class CategoryArgs(GQLArgsSet, GQLObject):
      category: NonNull_CategoryUpdateInput

   _args: CategoryArgs


   type: Category

class deleteCategories(GQLMutation):
   """
   deleteCategories - Deletes a category

   """
   class DeletedCategoryArgs(GQLArgsSet, GQLObject):
      categories: NonNull_list[NonNull_ID]

   _args: DeletedCategoryArgs


   type: DeletedCategory

class deleteCollection(GQLMutation):
   """
   deleteCollection - Deletes an existing collection 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class updateCollection(GQLMutation):
   """
   updateCollection - Update single collection

   """
   class CollectionArgs(GQLArgsSet, GQLObject):
      input: NonNull_CollectionUpdateInput

   _args: CollectionArgs


   type: Collection

class createCollection(GQLMutation):
   """
   createCollection - Create a new Hub Category

   """
   class CollectionArgs(GQLArgsSet, GQLObject):
      input: NonNull_CollectionCreateInput

   _args: CollectionArgs


   type: Collection

class bulkUpdateCollections(GQLMutation):
   """
   bulkUpdateCollections - Updates collection 

   """
   class CollectionArgs(GQLArgsSet, GQLObject):
      collections: NonNull_list_UpdateCollectionsInput[UpdateCollectionsInput]

   _args: CollectionArgs


   type: list_Collection[Collection]

class updateCollections(GQLMutation):
   """
   updateCollections - Update multiple collections

   """
   class CollectionArgs(GQLArgsSet, GQLObject):
      collections: NonNull_list_UpdateCollectionsInput[UpdateCollectionsInput]

   _args: CollectionArgs


   type: list_Collection[Collection]

class postCommentV2(GQLMutation):
   """
   postCommentV2 - Post a comment

   """
   class CommentArgs(GQLArgsSet, GQLObject):
      input: CommentCreateInput

   _args: CommentArgs


   type: Comment

class deleteCommentV2(GQLMutation):
   """
   deleteCommentV2 - Delete a comment

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: CommentDeleteInput

   _args: AnyArgs


   type: Any

class updateCommentV2(GQLMutation):
   """
   updateCommentV2 - Update a comment

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: CommentUpdateInput

   _args: AnyArgs


   type: Any

class postCommentV3(GQLMutation):
   """
   postCommentV3 - Post a comment

   """
   class CommentArgs(GQLArgsSet, GQLObject):
      input: CommentCreateInput

   _args: CommentArgs


   type: Comment

class subscribeToPlan(GQLMutation):
   """
   subscribeToPlan - A user or team can subscribe to an API

   """
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      input: SubscribeInput

   _args: BillingSubscriptionArgs


   type: BillingSubscription

class unfollowUser(GQLMutation):
   """
   unfollowUser - Unfollow a user

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: FollowInput

   _args: boolArgs


   type: bool

class followUser(GQLMutation):
   """
   followUser - Follow a user

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: FollowInput

   _args: boolArgs


   type: bool

class followApi(GQLMutation):
   """
   followApi - [do not use; will be deprecated] Use createApiFollower

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: FollowApiInput

   _args: boolArgs


   type: bool

class unfollowApi(GQLMutation):
   """
   unfollowApi - Unfollow selected API

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: FollowApiInput

   _args: boolArgs


   type: bool

class sendMessage(GQLMutation):
   """
   sendMessage - Send a message to an API provider

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: SendMessageInput

   _args: boolArgs


   type: bool

class rateApi(GQLMutation):
   """
   rateApi - Give an API rating

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: RatingInput

   _args: AnyArgs


   type: Any

class upsertEntityMetadataBulk(GQLMutation):
   """
   upsertEntityMetadataBulk - [will be deprecated; do not use] Assign one or more attributes to an entity

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      entityId: ID
      entityAttributes: NonNull_list_EntityAttribute[EntityAttribute]

   _args: AnyArgs


   type: Any

class upsertEntityMetadata(GQLMutation):
   """
   upsertEntityMetadata - Assign one or more attributes to an entity (user, role, team)

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      entityMetadata: EntityMetadataInput

   _args: AnyArgs


   type: Any

class deleteIssueV2(GQLMutation):
   """
   deleteIssueV2 - Deletes an issue 

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: IssueDeleteInput

   _args: AnyArgs


   type: Any

class updateIssueV2(GQLMutation):
   """
   updateIssueV2 - Make a change to a public comment on an API.

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: IssueUpdateInput

   _args: AnyArgs


   type: Any

class deleteIssues(GQLMutation):
   """
   deleteIssues - Deletes an issue 

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: IssuesDeleteInput

   _args: AnyArgs


   type: Any

class postIssueV3(GQLMutation):
   """
   postIssueV3 - Post an issue to a provider

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: IssueCreateInputV2

   _args: AnyArgs


   type: Any

class updateOrCreateEndpointWithParameters(GQLMutation):
   """
   updateOrCreateEndpointWithParameters - Create or make changes to an endpoint with a parameter on a provider's API.

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: updateOrCreateEndpointWithParameters

   _args: AnyArgs


   type: Any

class updateEndpointEntity(GQLMutation):
   """
   updateEndpointEntity - [do not use; will be deprecated] use updateOrCreateEndpointWithParameters

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: updateEndpointEntity

   _args: AnyArgs


   type: Any

class deleteEndpoint(GQLMutation):
   """
   deleteEndpoint - Delete an endpoint

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      endpointId: str

   _args: AnyArgs


   type: Any

class deleteEndpoints(GQLMutation):
   """
   deleteEndpoints - Delete a few endpoints at once

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      endpointIds: list[str]

   _args: AnyArgs


   type: Any

class updateEndpointsCollectionOrder(GQLMutation):
   """
   updateEndpointsCollectionOrder - Update selected endpoints order on playground

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      endpointsCollectionOrder: list_EndpointOrder[EndpointOrder]

   _args: AnyArgs


   type: Any

class createEndpointsGroups(GQLMutation):
   """
   createEndpointsGroups - Create a group object that later user can attach endpoints

   """
   class EndpointsGroupArgs(GQLArgsSet, GQLObject):
      groups: NonNull_list_EndpointsGroupCreateInput[NonNull_EndpointsGroupCreateInput]

   _args: EndpointsGroupArgs


   type: EndpointsGroup

class updateEndpointsGroups(GQLMutation):
   """
   updateEndpointsGroups - Update endpoints group properties

   """
   class EndpointsGroupArgs(GQLArgsSet, GQLObject):
      groups: NonNull_list_EndpointsGroupUpdateInput[NonNull_EndpointsGroupUpdateInput]

   _args: EndpointsGroupArgs


   type: EndpointsGroup

class deleteEndpointsGroups(GQLMutation):
   """
   deleteEndpointsGroups - Delete a group that endpoints are attached to

   """
   class IDArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[NonNull_ID]

   _args: IDArgs


   type: ID

class duplicateNameCheck(GQLMutation):
   """
   duplicateNameCheck - get entities ( User/Governance/Identity ) by term

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: DuplicateNameCheckInput

   _args: boolArgs


   type: bool

class createEntityMetadata(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      entityMetadata: NonNull_EntityMetadataInput

   _args: boolArgs


   type: bool

class updateEntityMetadata(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      entityMetadata: NonNull_EntityMetadataInput

   _args: boolArgs


   type: bool

class createEntitiesRoles(GQLMutation):
   """
   createEntitiesRoles - Assign roles to users ( in all levels )

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: EntityRoleCreateInput

   _args: boolArgs


   type: bool

class upsertEntityRole(GQLMutation):
   """
   upsertEntityRole - Assigning roles to an entity (user, role, team)

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: EntityRoleInput

   _args: boolArgs


   type: bool

class updateGraphQLSchema(GQLMutation):
   """
   updateGraphQLSchema - Update GraphQLSchema by graphQLSchemaId or endpointId (at least one is mandatory, graphQLSchemaId is prioritized)

   """
   class IDArgs(GQLArgsSet, GQLObject):
      input: NonNull_UpdateGraphQLSchemaInput

   _args: IDArgs


   type: ID

class createHeadlines(GQLMutation):
   """
   createHeadlines - [will be deprecated; do not use] use createHeadlinesPerApiId

   """
   class strArgs(GQLArgsSet, GQLObject):
      createHeadlines: createHeadlines

   _args: strArgs


   type: str

class createHeadlinesPerApiId(GQLMutation):
   """
   createHeadlinesPerApiId - Creates a readme for the API, shows on the hub about page

   """
   class strArgs(GQLArgsSet, GQLObject):
      createHeadlines: createHeadlines

   _args: strArgs


   type: str

class updateHeadlines(GQLMutation):
   """
   updateHeadlines - Updates a readme for the API, shows on the hub about page

   """
   class boolArgs(GQLArgsSet, GQLObject):
      updateHeadlines: updateHeadlines

   _args: boolArgs


   type: bool

class followIssueV2(GQLMutation):
   """
   followIssueV2 - Follow an issue 

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: IssueFollowInputV2

   _args: AnyArgs


   type: Any

class updateKafkaConfiguration(GQLMutation):
   """
   updateKafkaConfiguration - Update the configuration of the Kafka service

   """
   class KafkaConfigurationArgs(GQLArgsSet, GQLObject):
      input: UpdateKafkaConfigurationInput

   _args: KafkaConfigurationArgs


   type: KafkaConfiguration

class subscribeToKafkaTopic(GQLMutation):
   """
   subscribeToKafkaTopic - Get kafka subscription by topic for an API verison

   """
   class SubscribeKafkaResponseArgs(GQLArgsSet, GQLObject):
      apiVersionId: NonNull_str
      topicName: NonNull_str
      options: NonNull_SubscribeOptions

   _args: SubscribeKafkaResponseArgs


   type: SubscribeKafkaResponse

class produceKafkaMessage(GQLMutation):
   """
   produceKafkaMessage - Produce a message to a Kafka API

   """
   class ProduceMessageResponseArgs(GQLArgsSet, GQLObject):
      message: NonNull_ProduceMessageInput

   _args: ProduceMessageResponseArgs


   type: list_ProduceMessageResponse[ProduceMessageResponse]

class postMessage(GQLMutation):
   """
   postMessage - Adds a message to an API's discussion board

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      message: NonNull_MessageCreateInput

   _args: AnyArgs


   type: Any

class postMessageV2(GQLMutation):
   """
   postMessageV2 - Adds a message to an API's discussion board

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      message: NonNull_MessageCreateInput

   _args: AnyArgs


   type: Any

class updateThreadEntityStatus(GQLMutation):
   """
   updateThreadEntityStatus - updates issues thread status 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: ThreadEntityStatusUpdateInput

   _args: boolArgs


   type: bool

class markNotificationAsViewed(GQLMutation):
   """
   markNotificationAsViewed - Mark new notification as view

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: MarkNewNotificationAsViewedInput

   _args: boolArgs


   type: bool

class markNewNotificationAsRead(GQLMutation):
   """
   markNewNotificationAsRead - Mark new notification as read

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: MarkNewNotificationsAsReadInput

   _args: boolArgs


   type: bool

class markNotificationsAsRead(GQLMutation):
   """
   markNotificationsAsRead - [do not use; will be deprecated] Mark new notification as read

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: MarkNotificationsAsReadInput

   _args: boolArgs


   type: bool

class updateOrganization(GQLMutation):
   """
   updateOrganization - Updating organization 

   """
   class OrganizationArgs(GQLArgsSet, GQLObject):
      input: NonNull_OrganizationUpdateInput

   _args: OrganizationArgs


   type: Organization

class deleteOrganization(GQLMutation):
   """
   deleteOrganization - Delete an organization

   """
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class createOrganization(GQLMutation):
   """
   createOrganization - Create an organization 

   """
   class OrganizationArgs(GQLArgsSet, GQLObject):
      input: NonNull_OrganizationCreateInput

   _args: OrganizationArgs


   type: Organization

class createNewOrganizationV4(GQLMutation):
   """
   createNewOrganizationV4 - [will be deprecated; do not use] Create an organization 

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: CreateNewOrganizationInputV4

   _args: AnyArgs


   type: Any

class generateResetPasswordToken(GQLMutation):
   """
   generateResetPasswordToken - Generate a reset password token

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      email: NonNull_str

   _args: AnyArgs


   type: Any

class resetUserPassword(GQLMutation):
   """
   resetUserPassword - resets user password 

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_ResetUserPasswordInput

   _args: AnyArgs


   type: Any

class deletePayoutInfo(GQLMutation):
   """
   deletePayoutInfo - Delete payout information

   """
   class boolArgs(GQLArgsSet, GQLObject):
      userId: NonNull_ID

   _args: boolArgs


   type: bool

class addProject(GQLMutation):
   """
   addProject - [will be deprecated; do not use] Creates Application ( application and x-rapid-key  ) 

   """
   class ProjectArgs(GQLArgsSet, GQLObject):
      input: NonNull_AddProjectInput

   _args: ProjectArgs


   type: Project

class addProjectV2(GQLMutation):
   """
   addProjectV2 - Creates Application ( application and x-rapid-key  ) 

   """
   class ProjectArgs(GQLArgsSet, GQLObject):
      input: NonNull_AddProjectInput

   _args: ProjectArgs


   type: Project

class editProjectV2(GQLMutation):
   """
   editProjectV2 - Edit user application properties

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_EditProjectInput

   _args: AnyArgs


   type: Any

class deleteProject(GQLMutation):
   """
   deleteProject - Delete a user application project

   """
   class IDArgs(GQLArgsSet, GQLObject):
      input: NonNull_DeleteProjectInput

   _args: IDArgs


   type: ID

class createProject(GQLMutation):
   """
   createProject - Create an Application

   """
   class ProjectArgs(GQLArgsSet, GQLObject):
      project: NonNull_ProjectCreateInput

   _args: ProjectArgs


   type: Project

class updateProject(GQLMutation):
   """
   updateProject - updating project ( aka application ) 

   """
   class ProjectArgs(GQLArgsSet, GQLObject):
      project: NonNull_ProjectUpdateInput

   _args: ProjectArgs


   type: list_Project[Project]

class createProjectAllowedAPIs(GQLMutation):
   """
   createProjectAllowedAPIs - Create the allowed APIs in an Application

   """
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject):
      input: list_createProjectAllowedAPIInput[createProjectAllowedAPIInput]

   _args: ProjectAllowedAPIArgs


   type: list_ProjectAllowedAPI[ProjectAllowedAPI]

class updateProjectAllowedAPI(GQLMutation):
   """
   updateProjectAllowedAPI - Change the APIs list that the app/project has access to

   """
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject):
      input: updateProjectAllowedAPIInput

   _args: ProjectAllowedAPIArgs


   type: ProjectAllowedAPI

class deleteProjectAllowedAPIs(GQLMutation):
   """
   deleteProjectAllowedAPIs - Deattach APIs from a project allowed list

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: deleteProjectAllowedAPIsInput

   _args: boolArgs


   type: bool

class changeApiUsedVersion(GQLMutation):
   """
   changeApiUsedVersion - Changes the API version used by the developer application

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: changeApiUsedVersionInput

   _args: boolArgs


   type: bool

class createRapidReason(GQLMutation):
   """
   createRapidReason - Give a reason for unsubscribing to an API

   """
   class IDArgs(GQLArgsSet, GQLObject):
      rapidReasonInput: RapidReasonInput

   _args: IDArgs


   type: ID

class deprecatedUpdateRole(GQLMutation):
   """
   deprecatedUpdateRole - [do not use; will be deprecated] update role

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      role: NonNull_RoleUpdateInput

   _args: AnyArgs


   type: Any

class updateRole(GQLMutation):
   """
   updateRole - Updates a role's description or permissions, or change whether it's set as default.

   """
   class RoleArgs(GQLArgsSet, GQLObject):
      role: NonNull_RoleUpdateInput

   _args: RoleArgs


   type: Role

class deprecatedCreateRole(GQLMutation):
   """
   deprecatedCreateRole - [do not use; will be deprecated] create role

   """
   class RoleArgs(GQLArgsSet, GQLObject):
      role: NonNull_RoleCreateInput

   _args: RoleArgs


   type: Role

class createRole(GQLMutation):
   """
   createRole - Create a role 

   """
   class RoleArgs(GQLArgsSet, GQLObject):
      role: NonNull_RoleCreateInput

   _args: RoleArgs


   type: Role

class deprecatedDeleteRole(GQLMutation):
   """
   deprecatedDeleteRole - [do not use; will be deprecated] delete role

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      roleId: ID

   _args: AnyArgs


   type: Any

class deleteRole(GQLMutation):
   """
   deleteRole - Delete Role 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_list[NonNull_ID]

   _args: boolArgs


   type: bool

class createSecretData(GQLMutation):
   """
   createSecretData - [will be deprecated; do not use] Create an API secret

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: createSecretDataInput

   _args: AnyArgs


   type: Any

class updateBaseUrl(GQLMutation):
   """
   updateBaseUrl - [do not use; will be deprecated] use updateTargetGroups

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: updateBaseUrlInput

   _args: boolArgs


   type: bool

class createSpotlight(GQLMutation):
   """
   createSpotlight - Creates a spotlight on an API listing

   """
   class SpotlightArgs(GQLArgsSet, GQLObject):
      spotlight: NonNull_SpotlightCreateInput

   _args: SpotlightArgs


   type: Spotlight

class updateSpotlight(GQLMutation):
   """
   updateSpotlight - Updates an existing spotlight on an API listing

   """
   class SpotlightArgs(GQLArgsSet, GQLObject):
      spotlight: NonNull_SpotlightUpdateInput

   _args: SpotlightArgs


   type: Spotlight

class deleteSpotlight(GQLMutation):
   """
   deleteSpotlight - Delete a spotlight connected to an API

   """
   class boolArgs(GQLArgsSet, GQLObject):
      spotlight: NonNull_SpotlightDeleteInput

   _args: boolArgs


   type: bool

class deleteSubscriptions(GQLMutation):
   """
   deleteSubscriptions - Delete a range of subscriptions by aray of IDs

   """
   class boolArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[NonNull_ID]

   _args: boolArgs


   type: bool

class deleteSubscription(GQLMutation):
   """
   deleteSubscription - Delete a single API subscription by ID

   """
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class createSubscription(GQLMutation):
   """
   createSubscription - Create a new API subscription

   """
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      input: NonNull_SubscriptionCreateInput

   _args: BillingSubscriptionArgs


   type: BillingSubscription

class updateTargetGroups(GQLMutation):
   """
   updateTargetGroups - Updates the target URL on 1 API version

   """
   class TargetGroupArgs(GQLArgsSet, GQLObject):
      targetGroups: NonNull_list_TargetGroupUpdateInput[NonNull_TargetGroupUpdateInput]

   _args: TargetGroupArgs


   type: TargetGroup

class removeTeamUserFromAllOrgTeams(GQLMutation):
   """
   removeTeamUserFromAllOrgTeams - remove user from the organization

   """
   class boolArgs(GQLArgsSet, GQLObject):
      orgId: NonNull_int
      email: NonNull_str

   _args: boolArgs


   type: bool

class updateTeamUser(GQLMutation):
   """
   updateTeamUser - Add/Remove team for user

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: TeamUserUpdateInput

   _args: boolArgs


   type: bool

class updateUserRoles(GQLMutation):
   """
   updateUserRoles - Update the role of user

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: UserRolesUpdateInput

   _args: boolArgs


   type: bool

class editTeam(GQLMutation):
   """
   editTeam - Edit a team 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: EditTeamInput

   _args: boolArgs


   type: bool

class addUserToTeams(GQLMutation):
   """
   addUserToTeams - Adds organization users to teams 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      userId: NonNull_int
      teamIds: NonNull_list[int]

   _args: boolArgs


   type: bool

class deleteTeam(GQLMutation):
   """
   deleteTeam - Delete team

   """
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class createTeam(GQLMutation):
   """
   createTeam - Create a team

   """
   class TeamArgs(GQLArgsSet, GQLObject):
      input: NonNull_TeamCreateInput

   _args: TeamArgs


   type: Team

class updateTeam(GQLMutation):
   """
   updateTeam - Updates team

   """
   class TeamArgs(GQLArgsSet, GQLObject):
      input: NonNull_TeamUpdateInput

   _args: TeamArgs


   type: Team

class updateTransactions(GQLMutation):
   """
   updateTransactions - Update transactions payout status

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: updateTransactionInput

   _args: boolArgs


   type: bool

class createTransformations(GQLMutation):
   """
   createTransformations - Create a new API verison transformation

   """
   class TransformationArgs(GQLArgsSet, GQLObject):
      transformations: NonNull_list_TransformationCreateInput[NonNull_TransformationCreateInput]

   _args: TransformationArgs


   type: Transformation

class updateTransformations(GQLMutation):
   """
   updateTransformations - Update API version transformations

   """
   class TransformationArgs(GQLArgsSet, GQLObject):
      transformations: NonNull_list_TransformationUpdateInput[NonNull_TransformationUpdateInput]

   _args: TransformationArgs


   type: Transformation

class deleteTransformations(GQLMutation):
   """
   deleteTransformations - delete transformation from the api version 

   """
   class DeletedTransformationArgs(GQLArgsSet, GQLObject):
      transformations: NonNull_list[NonNull_ID]

   _args: DeletedTransformationArgs


   type: DeletedTransformation

class createTutorial(GQLMutation):
   """
   createTutorial - Creates a tutorial on an API listing

   """
   class TutorialArgs(GQLArgsSet, GQLObject):
      tutorial: NonNull_TutorialCreateInput

   _args: TutorialArgs


   type: Tutorial

class updateTutorial(GQLMutation):
   """
   updateTutorial - Updates an existing tutorial on an API listing

   """
   class TutorialArgs(GQLArgsSet, GQLObject):
      tutorial: NonNull_TutorialUpdateInput

   _args: TutorialArgs


   type: Tutorial

class deleteTutorial(GQLMutation):
   """
   deleteTutorial - Removes an existing tutorial on an API listing

   """
   class boolArgs(GQLArgsSet, GQLObject):
      tutorial: NonNull_TutorialDeleteInput

   _args: boolArgs


   type: bool

class phoneAuthSetup(GQLMutation):
   """
   phoneAuthSetup - setting up phone authentication ( 2fa flow)

   """
   class PhoneVerificationArgs(GQLArgsSet, GQLObject):
      phoneNumber: NonNull_str

   _args: PhoneVerificationArgs


   type: PhoneVerification

class phoneAuthSetupVerify(GQLMutation):
   """
   phoneAuthSetupVerify - verifying phone authentication setup

   """
   class boolArgs(GQLArgsSet, GQLObject):
      code: NonNull_str
      token: NonNull_str

   _args: boolArgs


   type: bool

class authenticateUsingPhone(GQLMutation):
   """
   authenticateUsingPhone - Authenticates the user using phone code 

   """
   class PhoneVerificationArgs(GQLArgsSet, GQLObject):
      phoneId: NonNull_ID

   _args: PhoneVerificationArgs


   type: PhoneVerification

class authenticateUsingPhoneVerify(GQLMutation):
   """
   authenticateUsingPhoneVerify - Verifies that the phone setup succeeded ( by the user sending a code + token)

   """
   class boolArgs(GQLArgsSet, GQLObject):
      code: NonNull_str
      token: NonNull_str

   _args: boolArgs


   type: bool

class deletePhoneNumber(GQLMutation):
   """
   deletePhoneNumber - Delete user phone number

   """
   class boolArgs(GQLArgsSet, GQLObject):
      phoneId: NonNull_int

   _args: boolArgs


   type: bool

class generateRecoveryCodes(GQLMutation):
   """
   generateRecoveryCodes - Generate a recovery codes for MFA 

   """
   type: list_RecoveryCode[RecoveryCode]

class regenerateRecoveryCodes(GQLMutation):
   """
   regenerateRecoveryCodes - generates recovery codes part of setting up 2fa to a user

   """
   type: list_RecoveryCode[RecoveryCode]

class markRecoveryCodeAsUsed(GQLMutation):
   """
   markRecoveryCodeAsUsed - authenticates the user using recovery code ( 2fa flow )

   """
   class boolArgs(GQLArgsSet, GQLObject):
      code: NonNull_str

   _args: boolArgs


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
   class boolArgs(GQLArgsSet, GQLObject):
      code: NonNull_str

   _args: boolArgs


   type: bool

class authenticateUsingApp(GQLMutation):
   """
   authenticateUsingApp - Authenticates the user using google auth app 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      code: NonNull_str

   _args: boolArgs


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
   class boolArgs(GQLArgsSet, GQLObject):
      input: UserInvitesInput

   _args: boolArgs


   type: bool

class createUserInvitesV2(GQLMutation):
   """
   createUserInvitesV2 - [do not use; will be deprecated] Invite users to organization

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: UserInvitesCreateInput

   _args: boolArgs


   type: bool

class acceptUserInvite(GQLMutation):
   """
   acceptUserInvite - Accepts user invite to organization 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      token: NonNull_str

   _args: boolArgs


   type: bool

class bulkDeleteUserInvitesV2(GQLMutation):
   """
   bulkDeleteUserInvitesV2 - Deletes users that are in pending mode from the organization 

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      emails: list[str]
      orgId: int

   _args: AnyArgs


   type: Any

class deleteUserInvites(GQLMutation):
   """
   deleteUserInvites - Used for deleting user/s that not yet confirmed the invitation

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_UserInvitesDeleteInput

   _args: AnyArgs


   type: Any

class bulkReactivateUserInvitesV2(GQLMutation):
   """
   bulkReactivateUserInvitesV2 - Reactivates users from the organizartion 

   """
   class boolArgs(GQLArgsSet, GQLObject):
      emails: list[str]
      orgId: int

   _args: boolArgs


   type: bool

class reactivateUserInvites(GQLMutation):
   """
   reactivateUserInvites - Used for activating user/s that was deactivated

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: NonNull_UserInvitesReactivateInput

   _args: boolArgs


   type: bool

class inviteUsersToTeams(GQLMutation):
   """
   inviteUsersToTeams - Adds an array of user IDs to a team at the time the Org is created

   """
   class boolArgs(GQLArgsSet, GQLObject):
      usersToInvite: Any
      orgId: NonNull_ID
      meta: Any

   _args: boolArgs


   type: bool

class saveUserApi(GQLMutation):
   """
   saveUserApi - Save an API as a favorite

   """
   class UserSavedApiArgs(GQLArgsSet, GQLObject):
      saveUserApi: SaveUserApi

   _args: UserSavedApiArgs


   type: UserSavedApi

class updateUserById(GQLMutation):
   """
   updateUserById - Update a set of attributes on a user by ID.

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      input: UpdateUserInput

   _args: AnyArgs


   type: Any

class updateUserPassword(GQLMutation):
   """
   updateUserPassword - Update the password of a user

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: UserPasswordInput

   _args: boolArgs


   type: bool

class deleteAll2faData(GQLMutation):
   """
   deleteAll2faData - Delete all 2FA data

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      userId: NonNull_str

   _args: AnyArgs


   type: Any

class updateUserEmail(GQLMutation):
   """
   updateUserEmail - Update the email address of a user

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      email: NonNull_str

   _args: AnyArgs


   type: Any

class verifyEmailCode(GQLMutation):
   """
   verifyEmailCode - Takes a verification code and returns a boolean

   """
   class boolArgs(GQLArgsSet, GQLObject):
      input: VerifyEmailCodeInput

   _args: boolArgs


   type: bool

class updateUser(GQLMutation):
   """
   updateUser - Updates user metadata / password 

   """
   class UserArgs(GQLArgsSet, GQLObject):
      input: NonNull_UserUpdateInput

   _args: UserArgs


   type: User

class createWorkflow(GQLMutation):
   """
   createWorkflow - Create a workflow

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      options: CreateWorkflowInput

   _args: AnyArgs


   type: Any

class createSignupApprovalWorkflow(GQLMutation):
   """
   createSignupApprovalWorkflow - Create a signup approval request

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      options: CreateSignupApprovalWorkflowInput

   _args: AnyArgs


   type: Any

class updateWorkflows(GQLMutation):
   """
   updateWorkflows - Change an entity's workflow

   """
   class AnyArgs(GQLArgsSet, GQLObject):
      options: UpdateWorkflowsInput

   _args: AnyArgs


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
