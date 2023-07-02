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

class list_ApiCertificateCreationResult(list, ApiCertificateCreationResult): pass

class NonNull_SaveApiDevelopersInput(SaveApiDevelopersInput): pass

class NonNull_CreateApiFavoritesInput(CreateApiFavoritesInput): pass

class NonNull_DeleteApiFavoritesInput(DeleteApiFavoritesInput): pass

class NonNull_ApiFollowerCreateInput(ApiFollowerCreateInput): pass

class NonNull_ApiFollowerDeleteInput(ApiFollowerDeleteInput): pass

class NonNull_ApiCreateFromSpecInput(ApiCreateFromSpecInput): pass

class NonNull_list_ApiCreateFromSpecInput(list, ApiCreateFromSpecInput): pass

class list_ApiSpecImportResult(list, ApiSpecImportResult): pass

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

class list_Authentication(list, Authentication): pass

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

class list_DeletedCategory(list, DeletedCategory): pass

class NonNull_CollectionUpdateInput(CollectionUpdateInput): pass

class NonNull_CollectionCreateInput(CollectionCreateInput): pass

class NonNull_list_UpdateCollectionsInput(list, UpdateCollectionsInput): pass

class NonNull_list_EntityAttribute(list, EntityAttribute): pass

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

class NonNull_ExternalGatewaySubscriptionCreateInput(ExternalGatewaySubscriptionCreateInput): pass

class NonNull_TargetGroupUpdateInput(TargetGroupUpdateInput): pass

class NonNull_list_TargetGroupUpdateInput(list, TargetGroupUpdateInput): pass

class NonNull_TeamCreateInput(TeamCreateInput): pass

class NonNull_TeamUpdateInput(TeamUpdateInput): pass

class NonNull_TransformationCreateInput(TransformationCreateInput): pass

class NonNull_list_TransformationCreateInput(list, TransformationCreateInput): pass

class NonNull_TransformationUpdateInput(TransformationUpdateInput): pass

class NonNull_list_TransformationUpdateInput(list, TransformationUpdateInput): pass

class list_DeletedTransformation(list, DeletedTransformation): pass

class NonNull_TutorialCreateInput(TutorialCreateInput): pass

class NonNull_TutorialUpdateInput(TutorialUpdateInput): pass

class NonNull_TutorialDeleteInput(TutorialDeleteInput): pass

class list_RecoveryCode(list, RecoveryCode): pass

class NonNull_UserInvitesDeleteInput(UserInvitesDeleteInput): pass

class NonNull_UserInvitesReactivateInput(UserInvitesReactivateInput): pass

class NonNull_UserUpdateInput(UserUpdateInput): pass

class createEventUrl(GQLMutation):
   class EventUrlArgs(GQLArgsSet, GQLObject):
      createDto: NonNull_EventUrlCreateInput

   _args: EventUrlArgs


   type: EventUrl

class updateEventUrl(GQLMutation):
   class EventUrlArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID
      updateDto: NonNull_EventUrlUpdateInput

   _args: EventUrlArgs


   type: EventUrl

class deleteEventUrl(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: IDArgs


   type: ID

class upsertEventConfig(GQLMutation):
   class EventConfigArgs(GQLArgsSet, GQLObject):
      input: NonNull_EventConfigUpdateInput

   _args: EventConfigArgs


   type: EventConfig

class deleteEventConfig(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: IDArgs


   type: ID

class createGatewayInstance(GQLMutation):
   class GatewayInstanceArgs(GQLArgsSet, GQLObject):
      createDto: NonNull_GatewayInstanceCreateInput

   _args: GatewayInstanceArgs


   type: GatewayInstance

class updateGatewayInstance(GQLMutation):
   class GatewayInstanceArgs(GQLArgsSet, GQLObject):
      updateDto: NonNull_GatewayInstanceUpdateInput

   _args: GatewayInstanceArgs


   type: GatewayInstance

class deleteGatewayInstance(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: IDArgs


   type: ID

class createGatewayTemplate(GQLMutation):
   class GwTemplateArgs(GQLArgsSet, GQLObject):
      createDto: NonNull_GatewayTemplateCreateInput

   _args: GwTemplateArgs


   type: GwTemplate

class updateGatewayTemplate(GQLMutation):
   class GwTemplateArgs(GQLArgsSet, GQLObject):
      updateDto: NonNull_GatewayTemplateUpdateInput

   _args: GwTemplateArgs


   type: GwTemplate

class deleteGatewayTemplate(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: IDArgs


   type: ID

class createGatewayTemplateParam(GQLMutation):
   class GatewayTemplateParamArgs(GQLArgsSet, GQLObject):
      createDto: NonNull_GatewayTemplateParamsCreateInput

   _args: GatewayTemplateParamArgs


   type: GatewayTemplateParam

class updateEnvConfig(GQLMutation):
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
   class UserAlertArgs(GQLArgsSet, GQLObject):
      input: addUserAlertInput

   _args: UserAlertArgs


   type: UserAlert

class deleteUserAlerts(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject):
      input: NonNull_deleteUserAlertsInput

   _args: IDArgs


   type: list[ID]

class editUserAlert(GQLMutation):
   class UserAlertArgs(GQLArgsSet, GQLObject):
      input: NonNull_editUserAlertInput

   _args: UserAlertArgs


   type: UserAlert

class updateUserAlerts(GQLMutation):
   class UserAlertArgs(GQLArgsSet, GQLObject):
      input: NonNull_list_UserAlertUpdateInput[NonNull_UserAlertUpdateInput]

   _args: UserAlertArgs


   type: list_UserAlert[UserAlert]

class createApiCertificates(GQLMutation):
   class ApiCertificateCreationResultArgs(GQLArgsSet, GQLObject):
      certificates: NonNull_list_ApiCertificateCreateInput[NonNull_ApiCertificateCreateInput]

   _args: ApiCertificateCreationResultArgs


   type: list_ApiCertificateCreationResult[ApiCertificateCreationResult]

class deleteApiCertificates(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[ID]

   _args: boolArgs


   type: bool

class saveApiDevelopersToApi(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: NonNull_SaveApiDevelopersInput

   _args: boolArgs


   type: bool

class copyApiDevelopersFromVersion(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: CopyApiDevelopersInput

   _args: boolArgs


   type: bool

class createApiFavorites(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: NonNull_CreateApiFavoritesInput

   _args: boolArgs


   type: bool

class deleteApiFavorites(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: NonNull_DeleteApiFavoritesInput

   _args: boolArgs


   type: bool

class createApiFollowers(GQLMutation):
   class ApiFollowerArgs(GQLArgsSet, GQLObject):
      apiFollowers: NonNull_ApiFollowerCreateInput

   _args: ApiFollowerArgs


   type: ApiFollower

class deleteApiFollowers(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      apiFollowers: NonNull_ApiFollowerDeleteInput

   _args: boolArgs


   type: bool

class createApisFromSpecs(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject):
      creations: NonNull_list_ApiCreateFromSpecInput[NonNull_ApiCreateFromSpecInput]

   _args: ApiSpecImportResultArgs


   type: list_ApiSpecImportResult[ApiSpecImportResult]

class updateApisFromSpecs(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject):
      updates: NonNull_list_ApiUpdateFromSpecInput[NonNull_ApiUpdateFromSpecInput]

   _args: ApiSpecImportResultArgs


   type: list_ApiSpecImportResult[ApiSpecImportResult]

class createApisFromRapidOas(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject):
      creations: NonNull_list_ApiCreateFromRapidOasInput[NonNull_ApiCreateFromRapidOasInput]

   _args: ApiSpecImportResultArgs


   type: list_ApiSpecImportResult[ApiSpecImportResult]

class updateApisFromRapidOas(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject):
      updates: NonNull_list_ApiUpdateFromRapidOasInput[NonNull_ApiUpdateFromRapidOasInput]

   _args: ApiSpecImportResultArgs


   type: list_ApiSpecImportResult[ApiSpecImportResult]

class createApiVersions(GQLMutation):
   class ApiVersionArgs(GQLArgsSet, GQLObject):
      apiVersions: NonNull_list_ApiVersionCreateInput[NonNull_ApiVersionCreateInput]

   _args: ApiVersionArgs


   type: list_ApiVersion[ApiVersion]

class createGqlApiVersions(GQLMutation):
   class ApiVersionArgs(GQLArgsSet, GQLObject):
      gqlApiVersions: NonNull_list_GqlApiVersionCreateInput[NonNull_GqlApiVersionCreateInput]

   _args: ApiVersionArgs


   type: list_ApiVersion[ApiVersion]

class updateApiVersions(GQLMutation):
   class ApiVersionArgs(GQLArgsSet, GQLObject):
      apiVersions: NonNull_list_ApiVersionUpdateInput[NonNull_ApiVersionUpdateInput]

   _args: ApiVersionArgs


   type: list_ApiVersion[ApiVersion]

class createApiVersionBillingPlanVersion(GQLMutation):
   class ApiVersionBillingPlanVersionArgs(GQLArgsSet, GQLObject):
      input: createApiVersionBillingPlanVersionInput

   _args: ApiVersionBillingPlanVersionArgs


   type: ApiVersionBillingPlanVersion

class createApi(GQLMutation):
   class ApiArgs(GQLArgsSet, GQLObject):
      api: NonNull_ApiCreateInput

   _args: ApiArgs


   type: Api

class updateApi(GQLMutation):
   class ApiArgs(GQLArgsSet, GQLObject):
      api: NonNull_ApiUpdateInput

   _args: ApiArgs


   type: Api

class provisionSwaggerFiles(GQLMutation):
   class strArgs(GQLArgsSet, GQLObject):
      input: list_ProvisionApiFromFileInput[NonNull_ProvisionApiFromFileInput]

   _args: strArgs


   type: list[str]

class deleteApi(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class createApplicationAuthorization(GQLMutation):
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject):
      input: NonNull_AppAuthorizationCreateInput

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization

class updateApplicationAuthorization(GQLMutation):
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject):
      input: NonNull_AppAuthorizationUpdateInput

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization

class deleteApplicationAuthorization(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class addApplicationEnvironmentKey(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_AddApplicationEnvironmentKeyInput

   _args: AnyArgs


   type: Any

class editApplicationEnvironmentKey(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_EditApplicationEnviornmentKeyInput

   _args: AnyArgs


   type: Any

class deleteApplicationEnvironmentKey(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject):
      input: NonNull_DeleteApplicationEnvironmentKeyInput

   _args: IDArgs


   type: ID

class generateAssetUploadUrl(GQLMutation):
   class AssetArgs(GQLArgsSet, GQLObject):
      input: NonNull_GenerateAssetUploadUrlInput

   _args: AssetArgs


   type: Asset

class deleteAsset(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class updateAssetUploaded(GQLMutation):
   class AssetArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: AssetArgs


   type: Asset

class updateAsset(GQLMutation):
   class AssetArgs(GQLArgsSet, GQLObject):
      input: NonNull_AssetUpdateInput

   _args: AssetArgs


   type: Asset

class upsertAsyncApiConfiguration(GQLMutation):
   class AsyncApiConfigurationArgs(GQLArgsSet, GQLObject):
      asyncApiConfigurations: NonNull_list_AsyncApiConfigurationCreateInput[NonNull_AsyncApiConfigurationCreateInput]

   _args: AsyncApiConfigurationArgs


   type: list_AsyncApiConfiguration[AsyncApiConfiguration]

class upsertUserAttributes(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: UserAttributesInput

   _args: AnyArgs


   type: Any

class updateUserAttributeItem(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_ThemeUserAttributesInput

   _args: AnyArgs


   type: Any

class createAuthentications(GQLMutation):
   class AuthenticationArgs(GQLArgsSet, GQLObject):
      authentications: NonNull_list_AuthenticationCreateInput[NonNull_AuthenticationCreateInput]

   _args: AuthenticationArgs


   type: list_Authentication[Authentication]

class updateAuthentications(GQLMutation):
   class AuthenticationArgs(GQLArgsSet, GQLObject):
      authentications: NonNull_list_AuthenticationUpdateInput[NonNull_AuthenticationUpdateInput]

   _args: AuthenticationArgs


   type: list_Authentication[Authentication]

class createOrUpdateAPIVersionAuthentication(GQLMutation):
   class AuthenticationCreateOrUpdateResultArgs(GQLArgsSet, GQLObject):
      input: createAuthenticationInput

   _args: AuthenticationCreateOrUpdateResultArgs


   type: AuthenticationCreateOrUpdateResult

class createBillingFeature(GQLMutation):
   class BillingFeatureArgs(GQLArgsSet, GQLObject):
      createBillingFeature: createBillingFeature

   _args: BillingFeatureArgs


   type: BillingFeature

class updateBillingFeature(GQLMutation):
   class BillingFeatureArgs(GQLArgsSet, GQLObject):
      updateBillingFeature: updateBillingFeature

   _args: BillingFeatureArgs


   type: BillingFeature

class upsertBillingFeature(GQLMutation):
   class BillingFeatureArgs(GQLArgsSet, GQLObject):
      upsertBillingFeature: NonNull_upsertBillingFeatureInput

   _args: BillingFeatureArgs


   type: BillingFeature

class deleteBillingFeature(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      billingFeatureId: str

   _args: AnyArgs


   type: Any

class deleteBillingFeatures(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      billingFeatureIds: list[str]

   _args: AnyArgs


   type: Any

class createStripeCustomer(GQLMutation):
   class BillingInformationArgs(GQLArgsSet, GQLObject):
      input: CreateStripeCustomerInput

   _args: BillingInformationArgs


   type: BillingInformation

class updateStripeCustomer(GQLMutation):
   class BillingInformationArgs(GQLArgsSet, GQLObject):
      input: CreateStripeCustomerInput

   _args: BillingInformationArgs


   type: BillingInformation

class createStripeCustomerV2(GQLMutation):
   class BillingInformationArgs(GQLArgsSet, GQLObject):
      input: CreateStripeCustomerInput

   _args: BillingInformationArgs


   type: BillingInformation

class updateStripeCustomerV2(GQLMutation):
   class BillingInformationArgs(GQLArgsSet, GQLObject):
      input: CreateStripeCustomerInput

   _args: BillingInformationArgs


   type: BillingInformation

class deleteCustomerPaymentMethod(GQLMutation):
   type: bool

class upsertBillingItem(GQLMutation):
   class BillingItemArgs(GQLArgsSet, GQLObject):
      input: NonNull_BillingItemUpsertInput

   _args: BillingItemArgs


   type: BillingItem

class deleteBillingItems(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[NonNull_ID]

   _args: boolArgs


   type: bool

class deleteBillingPlans(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[NonNull_ID]

   _args: boolArgs


   type: bool

class updateAllowedPlanDevelopers(GQLMutation):
   class AllowedPlanDeveloperArgs(GQLArgsSet, GQLObject):
      input: AllowedPlanDevelopersUpdateInput

   _args: AllowedPlanDeveloperArgs


   type: list_AllowedPlanDeveloper[AllowedPlanDeveloper]

class editOrganizationInvoice(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: EditOrganizationInvoiceInput

   _args: boolArgs


   type: bool

class createBillingPlan(GQLMutation):
   class BillingPlanArgs(GQLArgsSet, GQLObject):
      billingPlan: NonNull_BillingPlanCreateInput

   _args: BillingPlanArgs


   type: BillingPlan

class updateBillingPlanMetadata(GQLMutation):
   class BillingPlanArgs(GQLArgsSet, GQLObject):
      billingPlan: NonNull_BillingPlanMetadataUpdateInput

   _args: BillingPlanArgs


   type: BillingPlan

class updateBillingPlanExtended(GQLMutation):
   class BillingPlanArgs(GQLArgsSet, GQLObject):
      billingPlan: NonNull_BillingPlanExtendedUpdateInput

   _args: BillingPlanArgs


   type: BillingPlan

class upsertBillingPlanAndVersion(GQLMutation):
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject):
      upsertBillingPlanAndVersionInput: NonNull_upsertBillingPlanAndVersionInput

   _args: BillingPlanVersionArgs


   type: BillingPlanVersion

class blockUsers(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: BlockedUserInput

   _args: boolArgs


   type: bool

class unblockUsers(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: BlockedUserInput

   _args: boolArgs


   type: bool

class createCategory(GQLMutation):
   class CategoryArgs(GQLArgsSet, GQLObject):
      category: NonNull_CategoryCreateInput

   _args: CategoryArgs


   type: Category

class updateCategory(GQLMutation):
   class CategoryArgs(GQLArgsSet, GQLObject):
      category: NonNull_CategoryUpdateInput

   _args: CategoryArgs


   type: Category

class deleteCategories(GQLMutation):
   class DeletedCategoryArgs(GQLArgsSet, GQLObject):
      categories: NonNull_list[NonNull_ID]

   _args: DeletedCategoryArgs


   type: list_DeletedCategory[DeletedCategory]

class deleteCollection(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class updateCollection(GQLMutation):
   class CollectionArgs(GQLArgsSet, GQLObject):
      input: NonNull_CollectionUpdateInput

   _args: CollectionArgs


   type: Collection

class createCollection(GQLMutation):
   class CollectionArgs(GQLArgsSet, GQLObject):
      input: NonNull_CollectionCreateInput

   _args: CollectionArgs


   type: Collection

class bulkUpdateCollections(GQLMutation):
   class CollectionArgs(GQLArgsSet, GQLObject):
      collections: NonNull_list_UpdateCollectionsInput[UpdateCollectionsInput]

   _args: CollectionArgs


   type: list_Collection[Collection]

class updateCollections(GQLMutation):
   class CollectionArgs(GQLArgsSet, GQLObject):
      collections: NonNull_list_UpdateCollectionsInput[UpdateCollectionsInput]

   _args: CollectionArgs


   type: list_Collection[Collection]

class postCommentV2(GQLMutation):
   class CommentArgs(GQLArgsSet, GQLObject):
      input: CommentCreateInput

   _args: CommentArgs


   type: Comment

class deleteCommentV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: CommentDeleteInput

   _args: AnyArgs


   type: Any

class updateCommentV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: CommentUpdateInput

   _args: AnyArgs


   type: Any

class postCommentV3(GQLMutation):
   class CommentArgs(GQLArgsSet, GQLObject):
      input: CommentCreateInput

   _args: CommentArgs


   type: Comment

class subscribeToPlan(GQLMutation):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      input: SubscribeInput

   _args: BillingSubscriptionArgs


   type: BillingSubscription

class unfollowUser(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: FollowInput

   _args: boolArgs


   type: bool

class followUser(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: FollowInput

   _args: boolArgs


   type: bool

class followApi(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: FollowApiInput

   _args: boolArgs


   type: bool

class unfollowApi(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: FollowApiInput

   _args: boolArgs


   type: bool

class sendMessage(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: SendMessageInput

   _args: boolArgs


   type: bool

class rateApi(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: RatingInput

   _args: AnyArgs


   type: Any

class upsertEntityMetadataBulk(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      entityId: ID
      entityAttributes: NonNull_list_EntityAttribute[EntityAttribute]

   _args: AnyArgs


   type: Any

class upsertEntityMetadata(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      entityMetadata: EntityMetadataInput

   _args: AnyArgs


   type: Any

class deleteIssueV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: IssueDeleteInput

   _args: AnyArgs


   type: Any

class updateIssueV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: IssueUpdateInput

   _args: AnyArgs


   type: Any

class deleteIssues(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: IssuesDeleteInput

   _args: AnyArgs


   type: Any

class postIssueV3(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: IssueCreateInputV2

   _args: AnyArgs


   type: Any

class updateOrCreateEndpointWithParameters(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: updateOrCreateEndpointWithParameters

   _args: AnyArgs


   type: Any

class updateEndpointEntity(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: updateEndpointEntity

   _args: AnyArgs


   type: Any

class deleteEndpoint(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      endpointId: str

   _args: AnyArgs


   type: Any

class deleteEndpoints(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      endpointIds: list[str]

   _args: AnyArgs


   type: Any

class updateEndpointsCollectionOrder(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      endpointsCollectionOrder: list_EndpointOrder[EndpointOrder]

   _args: AnyArgs


   type: Any

class createEndpointsGroups(GQLMutation):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject):
      groups: NonNull_list_EndpointsGroupCreateInput[NonNull_EndpointsGroupCreateInput]

   _args: EndpointsGroupArgs


   type: list_EndpointsGroup[EndpointsGroup]

class updateEndpointsGroups(GQLMutation):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject):
      groups: NonNull_list_EndpointsGroupUpdateInput[NonNull_EndpointsGroupUpdateInput]

   _args: EndpointsGroupArgs


   type: list_EndpointsGroup[EndpointsGroup]

class deleteEndpointsGroups(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[NonNull_ID]

   _args: IDArgs


   type: list[ID]

class duplicateNameCheck(GQLMutation):
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
   class boolArgs(GQLArgsSet, GQLObject):
      input: EntityRoleCreateInput

   _args: boolArgs


   type: bool

class upsertEntityRole(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: EntityRoleInput

   _args: boolArgs


   type: bool

class updateGraphQLSchema(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject):
      input: NonNull_UpdateGraphQLSchemaInput

   _args: IDArgs


   type: ID

class createHeadlinesPerApiId(GQLMutation):
   class strArgs(GQLArgsSet, GQLObject):
      createHeadlines: createHeadlines

   _args: strArgs


   type: str

class updateHeadlines(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      updateHeadlines: updateHeadlines

   _args: boolArgs


   type: bool

class createHeadlines(GQLMutation):
   class strArgs(GQLArgsSet, GQLObject):
      createHeadlines: createHeadlines

   _args: strArgs


   type: str

class followIssueV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: IssueFollowInputV2

   _args: AnyArgs


   type: Any

class updateKafkaConfiguration(GQLMutation):
   class KafkaConfigurationArgs(GQLArgsSet, GQLObject):
      input: UpdateKafkaConfigurationInput

   _args: KafkaConfigurationArgs


   type: KafkaConfiguration

class subscribeToKafkaTopic(GQLMutation):
   class SubscribeKafkaResponseArgs(GQLArgsSet, GQLObject):
      apiVersionId: NonNull_str
      topicName: NonNull_str
      options: NonNull_SubscribeOptions

   _args: SubscribeKafkaResponseArgs


   type: SubscribeKafkaResponse

class produceKafkaMessage(GQLMutation):
   class ProduceMessageResponseArgs(GQLArgsSet, GQLObject):
      message: NonNull_ProduceMessageInput

   _args: ProduceMessageResponseArgs


   type: list_ProduceMessageResponse[ProduceMessageResponse]

class postMessage(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      message: NonNull_MessageCreateInput

   _args: AnyArgs


   type: Any

class postMessageV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      message: NonNull_MessageCreateInput

   _args: AnyArgs


   type: Any

class updateThreadEntityStatus(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: ThreadEntityStatusUpdateInput

   _args: boolArgs


   type: bool

class markNotificationAsViewed(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: MarkNewNotificationAsViewedInput

   _args: boolArgs


   type: bool

class markNewNotificationAsRead(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: MarkNewNotificationsAsReadInput

   _args: boolArgs


   type: bool

class markNotificationsAsRead(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: MarkNotificationsAsReadInput

   _args: boolArgs


   type: bool

class updateOrganization(GQLMutation):
   class OrganizationArgs(GQLArgsSet, GQLObject):
      input: NonNull_OrganizationUpdateInput

   _args: OrganizationArgs


   type: Organization

class deleteOrganization(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class createOrganization(GQLMutation):
   class OrganizationArgs(GQLArgsSet, GQLObject):
      input: NonNull_OrganizationCreateInput

   _args: OrganizationArgs


   type: Organization

class createNewOrganizationV4(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: CreateNewOrganizationInputV4

   _args: AnyArgs


   type: Any

class generateResetPasswordToken(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      email: NonNull_str

   _args: AnyArgs


   type: Any

class resetUserPassword(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_ResetUserPasswordInput

   _args: AnyArgs


   type: Any

class deletePayoutInfo(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      userId: NonNull_ID

   _args: boolArgs


   type: bool

class addProject(GQLMutation):
   class ProjectArgs(GQLArgsSet, GQLObject):
      input: NonNull_AddProjectInput

   _args: ProjectArgs


   type: Project

class addProjectV2(GQLMutation):
   class ProjectArgs(GQLArgsSet, GQLObject):
      input: NonNull_AddProjectInput

   _args: ProjectArgs


   type: Project

class editProjectV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_EditProjectInput

   _args: AnyArgs


   type: Any

class deleteProject(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject):
      input: NonNull_DeleteProjectInput

   _args: IDArgs


   type: ID

class createProject(GQLMutation):
   class ProjectArgs(GQLArgsSet, GQLObject):
      project: NonNull_ProjectCreateInput

   _args: ProjectArgs


   type: Project

class updateProject(GQLMutation):
   class ProjectArgs(GQLArgsSet, GQLObject):
      project: NonNull_ProjectUpdateInput

   _args: ProjectArgs


   type: Project

class createProjectAllowedAPIs(GQLMutation):
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject):
      input: list_createProjectAllowedAPIInput[createProjectAllowedAPIInput]

   _args: ProjectAllowedAPIArgs


   type: list_ProjectAllowedAPI[ProjectAllowedAPI]

class updateProjectAllowedAPI(GQLMutation):
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject):
      input: updateProjectAllowedAPIInput

   _args: ProjectAllowedAPIArgs


   type: ProjectAllowedAPI

class deleteProjectAllowedAPIs(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: deleteProjectAllowedAPIsInput

   _args: boolArgs


   type: bool

class changeApiUsedVersion(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: changeApiUsedVersionInput

   _args: boolArgs


   type: bool

class createRapidReason(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject):
      rapidReasonInput: RapidReasonInput

   _args: IDArgs


   type: ID

class deprecatedUpdateRole(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      role: NonNull_RoleUpdateInput

   _args: AnyArgs


   type: Any

class updateRole(GQLMutation):
   class RoleArgs(GQLArgsSet, GQLObject):
      role: NonNull_RoleUpdateInput

   _args: RoleArgs


   type: Role

class deprecatedCreateRole(GQLMutation):
   class RoleArgs(GQLArgsSet, GQLObject):
      role: NonNull_RoleCreateInput

   _args: RoleArgs


   type: Role

class createRole(GQLMutation):
   class RoleArgs(GQLArgsSet, GQLObject):
      role: NonNull_RoleCreateInput

   _args: RoleArgs


   type: Role

class deprecatedDeleteRole(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      roleId: ID

   _args: AnyArgs


   type: Any

class deleteRole(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_list[NonNull_ID]

   _args: boolArgs


   type: bool

class createSecretData(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: createSecretDataInput

   _args: AnyArgs


   type: Any

class updateBaseUrl(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: updateBaseUrlInput

   _args: boolArgs


   type: bool

class createSpotlight(GQLMutation):
   class SpotlightArgs(GQLArgsSet, GQLObject):
      spotlight: NonNull_SpotlightCreateInput

   _args: SpotlightArgs


   type: Spotlight

class updateSpotlight(GQLMutation):
   class SpotlightArgs(GQLArgsSet, GQLObject):
      spotlight: NonNull_SpotlightUpdateInput

   _args: SpotlightArgs


   type: Spotlight

class deleteSpotlight(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      spotlight: NonNull_SpotlightDeleteInput

   _args: boolArgs


   type: bool

class deleteSubscriptions(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      ids: NonNull_list[NonNull_ID]

   _args: boolArgs


   type: bool

class deleteSubscription(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class createSubscription(GQLMutation):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      input: NonNull_SubscriptionCreateInput

   _args: BillingSubscriptionArgs


   type: BillingSubscription

class createExternalGatewayApiSubscription(GQLMutation):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject):
      input: NonNull_ExternalGatewaySubscriptionCreateInput

   _args: BillingSubscriptionArgs


   type: BillingSubscription

class updateTargetGroups(GQLMutation):
   class TargetGroupArgs(GQLArgsSet, GQLObject):
      targetGroups: NonNull_list_TargetGroupUpdateInput[NonNull_TargetGroupUpdateInput]

   _args: TargetGroupArgs


   type: list_TargetGroup[TargetGroup]

class removeTeamUserFromAllOrgTeams(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      orgId: NonNull_int
      email: NonNull_str

   _args: boolArgs


   type: bool

class updateTeamUser(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: TeamUserUpdateInput

   _args: boolArgs


   type: bool

class updateUserRoles(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: UserRolesUpdateInput

   _args: boolArgs


   type: bool

class editTeam(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: EditTeamInput

   _args: boolArgs


   type: bool

class addUserToTeams(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      userId: NonNull_int
      teamIds: NonNull_list[int]

   _args: boolArgs


   type: bool

class deleteTeam(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: boolArgs


   type: bool

class createTeam(GQLMutation):
   class TeamArgs(GQLArgsSet, GQLObject):
      input: NonNull_TeamCreateInput

   _args: TeamArgs


   type: Team

class updateTeam(GQLMutation):
   class TeamArgs(GQLArgsSet, GQLObject):
      input: NonNull_TeamUpdateInput

   _args: TeamArgs


   type: Team

class updateTransactions(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: updateTransactionInput

   _args: boolArgs


   type: bool

class createTransformations(GQLMutation):
   class TransformationArgs(GQLArgsSet, GQLObject):
      transformations: NonNull_list_TransformationCreateInput[NonNull_TransformationCreateInput]

   _args: TransformationArgs


   type: list_Transformation[Transformation]

class updateTransformations(GQLMutation):
   class TransformationArgs(GQLArgsSet, GQLObject):
      transformations: NonNull_list_TransformationUpdateInput[NonNull_TransformationUpdateInput]

   _args: TransformationArgs


   type: list_Transformation[Transformation]

class deleteTransformations(GQLMutation):
   class DeletedTransformationArgs(GQLArgsSet, GQLObject):
      transformations: NonNull_list[NonNull_ID]

   _args: DeletedTransformationArgs


   type: list_DeletedTransformation[DeletedTransformation]

class createTutorial(GQLMutation):
   class TutorialArgs(GQLArgsSet, GQLObject):
      tutorial: NonNull_TutorialCreateInput

   _args: TutorialArgs


   type: Tutorial

class updateTutorial(GQLMutation):
   class TutorialArgs(GQLArgsSet, GQLObject):
      tutorial: NonNull_TutorialUpdateInput

   _args: TutorialArgs


   type: Tutorial

class deleteTutorial(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      tutorial: NonNull_TutorialDeleteInput

   _args: boolArgs


   type: bool

class phoneAuthSetup(GQLMutation):
   class PhoneVerificationArgs(GQLArgsSet, GQLObject):
      phoneNumber: NonNull_str

   _args: PhoneVerificationArgs


   type: PhoneVerification

class phoneAuthSetupVerify(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      code: NonNull_str
      token: NonNull_str

   _args: boolArgs


   type: bool

class authenticateUsingPhone(GQLMutation):
   class PhoneVerificationArgs(GQLArgsSet, GQLObject):
      phoneId: NonNull_ID

   _args: PhoneVerificationArgs


   type: PhoneVerification

class authenticateUsingPhoneVerify(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      code: NonNull_str
      token: NonNull_str

   _args: boolArgs


   type: bool

class deletePhoneNumber(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      phoneId: NonNull_int

   _args: boolArgs


   type: bool

class generateRecoveryCodes(GQLMutation):
   type: list_RecoveryCode[RecoveryCode]

class regenerateRecoveryCodes(GQLMutation):
   type: list_RecoveryCode[RecoveryCode]

class markRecoveryCodeAsUsed(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      code: NonNull_str

   _args: boolArgs


   type: bool

class applicationAuthSetup(GQLMutation):
   type: str

class applicationAuthSetupVerify(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      code: NonNull_str

   _args: boolArgs


   type: bool

class authenticateUsingApp(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      code: NonNull_str

   _args: boolArgs


   type: bool

class deleteApplicationAuth(GQLMutation):
   type: bool

class createUserInvites(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: UserInvitesInput

   _args: boolArgs


   type: bool

class createUserInvitesV2(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: UserInvitesCreateInput

   _args: boolArgs


   type: bool

class acceptUserInvite(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      token: NonNull_str

   _args: boolArgs


   type: bool

class bulkDeleteUserInvitesV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      emails: list[str]
      orgId: int

   _args: AnyArgs


   type: Any

class deleteUserInvites(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: NonNull_UserInvitesDeleteInput

   _args: AnyArgs


   type: Any

class bulkReactivateUserInvitesV2(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      emails: list[str]
      orgId: int

   _args: boolArgs


   type: bool

class reactivateUserInvites(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: NonNull_UserInvitesReactivateInput

   _args: boolArgs


   type: bool

class inviteUsersToTeams(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      usersToInvite: Any
      orgId: NonNull_ID
      meta: Any

   _args: boolArgs


   type: bool

class saveUserApi(GQLMutation):
   class UserSavedApiArgs(GQLArgsSet, GQLObject):
      saveUserApi: SaveUserApi

   _args: UserSavedApiArgs


   type: UserSavedApi

class updateUserById(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      input: UpdateUserInput

   _args: AnyArgs


   type: Any

class updateUserPassword(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: UserPasswordInput

   _args: boolArgs


   type: bool

class deleteAll2faData(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      userId: NonNull_str

   _args: AnyArgs


   type: Any

class updateUserEmail(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      email: NonNull_str

   _args: AnyArgs


   type: Any

class verifyEmailCode(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject):
      input: VerifyEmailCodeInput

   _args: boolArgs


   type: bool

class updateUser(GQLMutation):
   class UserArgs(GQLArgsSet, GQLObject):
      input: NonNull_UserUpdateInput

   _args: UserArgs


   type: User

class createWorkflow(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      options: CreateWorkflowInput

   _args: AnyArgs


   type: Any

class createSignupApprovalWorkflow(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject):
      options: CreateSignupApprovalWorkflowInput

   _args: AnyArgs


   type: Any

class updateWorkflows(GQLMutation):
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
   createHeadlinesPerApiId = createHeadlinesPerApiId
   updateHeadlines = updateHeadlines
   createHeadlines = createHeadlines
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
   createExternalGatewayApiSubscription = createExternalGatewayApiSubscription
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
