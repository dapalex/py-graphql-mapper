from typing import List
from pygqlmap import GQLMutation
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *


NonNull_EventUrlCreateInput = EventUrlCreateInput

NonNull_EventUrlUpdateInput = EventUrlUpdateInput

NonNull_EventConfigUpdateInput = EventConfigUpdateInput

NonNull_GatewayInstanceCreateInput = GatewayInstanceCreateInput

NonNull_GatewayInstanceUpdateInput = GatewayInstanceUpdateInput

NonNull_GatewayTemplateCreateInput = GatewayTemplateCreateInput

NonNull_GatewayTemplateUpdateInput = GatewayTemplateUpdateInput

NonNull_GatewayTemplateParamsCreateInput = GatewayTemplateParamsCreateInput

NonNull_EnvConfigUpdateInput = EnvConfigUpdateInput

NonNull_deleteUserAlertsInput = deleteUserAlertsInput

NonNull_editUserAlertInput = editUserAlertInput

NonNull_UserAlertUpdateInput = UserAlertUpdateInput

NonNull_ApiCertificateCreateInput = ApiCertificateCreateInput

NonNull_SaveApiDevelopersInput = SaveApiDevelopersInput

NonNull_CreateApiFavoritesInput = CreateApiFavoritesInput

NonNull_DeleteApiFavoritesInput = DeleteApiFavoritesInput

NonNull_ApiFollowerCreateInput = ApiFollowerCreateInput

NonNull_ApiFollowerDeleteInput = ApiFollowerDeleteInput

NonNull_ApiCreateFromSpecInput = ApiCreateFromSpecInput

NonNull_ApiUpdateFromSpecInput = ApiUpdateFromSpecInput

NonNull_ApiCreateFromRapidOasInput = ApiCreateFromRapidOasInput

NonNull_ApiUpdateFromRapidOasInput = ApiUpdateFromRapidOasInput

NonNull_ApiVersionCreateInput = ApiVersionCreateInput

NonNull_GqlApiVersionCreateInput = GqlApiVersionCreateInput

NonNull_ApiVersionUpdateInput = ApiVersionUpdateInput

NonNull_ApiCreateInput = ApiCreateInput

NonNull_ApiUpdateInput = ApiUpdateInput

NonNull_ProvisionApiFromFileInput = ProvisionApiFromFileInput

NonNull_AppAuthorizationCreateInput = AppAuthorizationCreateInput

NonNull_AppAuthorizationUpdateInput = AppAuthorizationUpdateInput

NonNull_AddApplicationEnvironmentKeyInput = AddApplicationEnvironmentKeyInput

NonNull_EditApplicationEnviornmentKeyInput = EditApplicationEnviornmentKeyInput

NonNull_DeleteApplicationEnvironmentKeyInput = DeleteApplicationEnvironmentKeyInput

NonNull_GenerateAssetUploadUrlInput = GenerateAssetUploadUrlInput

NonNull_AssetUpdateInput = AssetUpdateInput

NonNull_AsyncApiConfigurationCreateInput = AsyncApiConfigurationCreateInput

NonNull_ThemeUserAttributesInput = ThemeUserAttributesInput

NonNull_AuthenticationCreateInput = AuthenticationCreateInput

NonNull_AuthenticationUpdateInput = AuthenticationUpdateInput

NonNull_upsertBillingFeatureInput = upsertBillingFeatureInput

NonNull_BillingItemUpsertInput = BillingItemUpsertInput

NonNull_BillingPlanCreateInput = BillingPlanCreateInput

NonNull_BillingPlanMetadataUpdateInput = BillingPlanMetadataUpdateInput

NonNull_BillingPlanExtendedUpdateInput = BillingPlanExtendedUpdateInput

NonNull_upsertBillingPlanAndVersionInput = upsertBillingPlanAndVersionInput

NonNull_CategoryCreateInput = CategoryCreateInput

NonNull_CategoryUpdateInput = CategoryUpdateInput

NonNull_CollectionUpdateInput = CollectionUpdateInput

NonNull_CollectionCreateInput = CollectionCreateInput

NonNull_EndpointsGroupCreateInput = EndpointsGroupCreateInput

NonNull_EndpointsGroupUpdateInput = EndpointsGroupUpdateInput

NonNull_EntityMetadataInput = EntityMetadataInput

NonNull_UpdateGraphQLSchemaInput = UpdateGraphQLSchemaInput

NonNull_SubscribeOptions = SubscribeOptions

NonNull_ProduceMessageInput = ProduceMessageInput

NonNull_MessageCreateInput = MessageCreateInput

NonNull_OrganizationUpdateInput = OrganizationUpdateInput

NonNull_OrganizationCreateInput = OrganizationCreateInput

NonNull_ResetUserPasswordInput = ResetUserPasswordInput

NonNull_AddProjectInput = AddProjectInput

NonNull_EditProjectInput = EditProjectInput

NonNull_DeleteProjectInput = DeleteProjectInput

NonNull_ProjectCreateInput = ProjectCreateInput

NonNull_ProjectUpdateInput = ProjectUpdateInput

NonNull_RoleUpdateInput = RoleUpdateInput

NonNull_RoleCreateInput = RoleCreateInput

NonNull_SpotlightCreateInput = SpotlightCreateInput

NonNull_SpotlightUpdateInput = SpotlightUpdateInput

NonNull_SpotlightDeleteInput = SpotlightDeleteInput

NonNull_SubscriptionCreateInput = SubscriptionCreateInput

NonNull_TargetGroupUpdateInput = TargetGroupUpdateInput

NonNull_TeamCreateInput = TeamCreateInput

NonNull_TeamUpdateInput = TeamUpdateInput

NonNull_TransformationCreateInput = TransformationCreateInput

NonNull_TransformationUpdateInput = TransformationUpdateInput

NonNull_TutorialCreateInput = TutorialCreateInput

NonNull_TutorialUpdateInput = TutorialUpdateInput

NonNull_TutorialDeleteInput = TutorialDeleteInput

NonNull_UserInvitesDeleteInput = UserInvitesDeleteInput

NonNull_UserInvitesReactivateInput = UserInvitesReactivateInput

NonNull_UserUpdateInput = UserUpdateInput

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


   type: ID

class editUserAlert(GQLMutation):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      input: NonNull_editUserAlertInput

   _args: UserAlertArgs


   type: UserAlert

class updateUserAlerts(GQLMutation):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      input: NonNull_List[NonNull_UserAlertUpdateInput]

   _args: UserAlertArgs


   type: UserAlert

class createApiCertificates(GQLMutation):
   class ApiCertificateCreationResultArgs(GQLArgsSet, GQLObject): 
      certificates: NonNull_List[NonNull_ApiCertificateCreateInput]

   _args: ApiCertificateCreationResultArgs


   type: ApiCertificateCreationResult

class deleteApiCertificates(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      ids: NonNull_List[ID]

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
      creations: NonNull_List[NonNull_ApiCreateFromSpecInput]

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult

class updateApisFromSpecs(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject): 
      updates: NonNull_List[NonNull_ApiUpdateFromSpecInput]

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult

class createApisFromRapidOas(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject): 
      creations: NonNull_List[NonNull_ApiCreateFromRapidOasInput]

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult

class updateApisFromRapidOas(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject): 
      updates: NonNull_List[NonNull_ApiUpdateFromRapidOasInput]

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult

class createApiVersions(GQLMutation):
   class ApiVersionArgs(GQLArgsSet, GQLObject): 
      apiVersions: NonNull_List[NonNull_ApiVersionCreateInput]

   _args: ApiVersionArgs


   type: ApiVersion

class createGqlApiVersions(GQLMutation):
   class ApiVersionArgs(GQLArgsSet, GQLObject): 
      gqlApiVersions: NonNull_List[NonNull_GqlApiVersionCreateInput]

   _args: ApiVersionArgs


   type: ApiVersion

class updateApiVersions(GQLMutation):
   class ApiVersionArgs(GQLArgsSet, GQLObject): 
      apiVersions: NonNull_List[NonNull_ApiVersionUpdateInput]

   _args: ApiVersionArgs


   type: ApiVersion

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
      input: List[NonNull_ProvisionApiFromFileInput]

   _args: strArgs


   type: List[str]

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
      asyncApiConfigurations: NonNull_List[NonNull_AsyncApiConfigurationCreateInput]

   _args: AsyncApiConfigurationArgs


   type: AsyncApiConfiguration

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
      authentications: NonNull_List[NonNull_AuthenticationCreateInput]

   _args: AuthenticationArgs


   type: Authentication

class updateAuthentications(GQLMutation):
   class AuthenticationArgs(GQLArgsSet, GQLObject): 
      authentications: NonNull_List[NonNull_AuthenticationUpdateInput]

   _args: AuthenticationArgs


   type: Authentication

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
      billingFeatureIds: List[str]

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

class deleteBillingItem(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID

   _args: AnyArgs


   type: Any

class deleteBillingItems(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      ids: NonNull_List[NonNull_ID]

   _args: boolArgs


   type: bool

class deleteBillingPlans(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      ids: NonNull_List[NonNull_ID]

   _args: boolArgs


   type: bool

class updateAllowedPlanDevelopers(GQLMutation):
   class AllowedPlanDeveloperArgs(GQLArgsSet, GQLObject): 
      input: AllowedPlanDevelopersUpdateInput

   _args: AllowedPlanDeveloperArgs


   type: List[AllowedPlanDeveloper]

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
      categories: NonNull_List[NonNull_ID]

   _args: DeletedCategoryArgs


   type: DeletedCategory

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
      collections: NonNull_List[UpdateCollectionsInput]

   _args: CollectionArgs


   type: List[Collection]

class updateCollections(GQLMutation):
   class CollectionArgs(GQLArgsSet, GQLObject): 
      collections: NonNull_List[UpdateCollectionsInput]

   _args: CollectionArgs


   type: List[Collection]

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
      entityAttributes: NonNull_List[EntityAttribute]

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
      endpointIds: List[str]

   _args: AnyArgs


   type: Any

class updateEndpointsCollectionOrder(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      endpointsCollectionOrder: List[EndpointOrder]

   _args: AnyArgs


   type: Any

class createEndpointsGroups(GQLMutation):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject): 
      groups: NonNull_List[NonNull_EndpointsGroupCreateInput]

   _args: EndpointsGroupArgs


   type: EndpointsGroup

class updateEndpointsGroups(GQLMutation):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject): 
      groups: NonNull_List[NonNull_EndpointsGroupUpdateInput]

   _args: EndpointsGroupArgs


   type: EndpointsGroup

class deleteEndpointsGroups(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject): 
      ids: NonNull_List[NonNull_ID]

   _args: IDArgs


   type: ID

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

class createHeadlines(GQLMutation):
   class strArgs(GQLArgsSet, GQLObject): 
      createHeadlines: createHeadlines

   _args: strArgs


   type: str

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


   type: List[ProduceMessageResponse]

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


   type: List[Project]

class createProjectAllowedAPIs(GQLMutation):
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject): 
      input: List[createProjectAllowedAPIInput]

   _args: ProjectAllowedAPIArgs


   type: List[ProjectAllowedAPI]

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
      id: NonNull_List[NonNull_ID]

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
      ids: NonNull_List[NonNull_ID]

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

class updateTargetGroups(GQLMutation):
   class TargetGroupArgs(GQLArgsSet, GQLObject): 
      targetGroups: NonNull_List[NonNull_TargetGroupUpdateInput]

   _args: TargetGroupArgs


   type: TargetGroup

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
      teamIds: NonNull_List[int]

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
      transformations: NonNull_List[NonNull_TransformationCreateInput]

   _args: TransformationArgs


   type: Transformation

class updateTransformations(GQLMutation):
   class TransformationArgs(GQLArgsSet, GQLObject): 
      transformations: NonNull_List[NonNull_TransformationUpdateInput]

   _args: TransformationArgs


   type: Transformation

class deleteTransformations(GQLMutation):
   class DeletedTransformationArgs(GQLArgsSet, GQLObject): 
      transformations: NonNull_List[NonNull_ID]

   _args: DeletedTransformationArgs


   type: DeletedTransformation

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
   type: List[RecoveryCode]

class regenerateRecoveryCodes(GQLMutation):
   type: List[RecoveryCode]

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
      emails: List[str]
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
      emails: List[str]
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
