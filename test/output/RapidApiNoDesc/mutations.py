from pygqlmap import GQLMutation
from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *


class createEventUrl(GQLMutation):
   class EventUrlArgs(GQLArgsSet, GQLObject): 
      createDto: EventUrlCreateInput ##NON NULL

   _args: EventUrlArgs


   type: EventUrl ##NON NULL

class updateEventUrl(GQLMutation):
   class EventUrlArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL
      updateDto: EventUrlUpdateInput ##NON NULL

   _args: EventUrlArgs


   type: EventUrl ##NON NULL

class deleteEventUrl(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: IDArgs


   type: ID ##NON NULL

class upsertEventConfig(GQLMutation):
   class EventConfigArgs(GQLArgsSet, GQLObject): 
      input: EventConfigUpdateInput ##NON NULL

   _args: EventConfigArgs


   type: EventConfig ##NON NULL

class deleteEventConfig(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: IDArgs


   type: ID ##NON NULL

class createGatewayInstance(GQLMutation):
   class GatewayInstanceArgs(GQLArgsSet, GQLObject): 
      createDto: GatewayInstanceCreateInput ##NON NULL

   _args: GatewayInstanceArgs


   type: GatewayInstance ##NON NULL

class updateGatewayInstance(GQLMutation):
   class GatewayInstanceArgs(GQLArgsSet, GQLObject): 
      updateDto: GatewayInstanceUpdateInput ##NON NULL

   _args: GatewayInstanceArgs


   type: GatewayInstance ##NON NULL

class deleteGatewayInstance(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: IDArgs


   type: ID ##NON NULL

class createGatewayTemplate(GQLMutation):
   class GwTemplateArgs(GQLArgsSet, GQLObject): 
      createDto: GatewayTemplateCreateInput ##NON NULL

   _args: GwTemplateArgs


   type: GwTemplate ##NON NULL

class updateGatewayTemplate(GQLMutation):
   class GwTemplateArgs(GQLArgsSet, GQLObject): 
      updateDto: GatewayTemplateUpdateInput ##NON NULL

   _args: GwTemplateArgs


   type: GwTemplate ##NON NULL

class deleteGatewayTemplate(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: IDArgs


   type: ID ##NON NULL

class createGatewayTemplateParam(GQLMutation):
   class GatewayTemplateParamArgs(GQLArgsSet, GQLObject): 
      createDto: GatewayTemplateParamsCreateInput ##NON NULL

   _args: GatewayTemplateParamArgs


   type: GatewayTemplateParam ##NON NULL

class updateEnvConfig(GQLMutation):
   class EnvConfigArgs(GQLArgsSet, GQLObject): 
      envConfig: EnvConfigUpdateInput ##NON NULL

   _args: EnvConfigArgs


   type: EnvConfig ##NON NULL

class resetEnvConfig(GQLMutation):
   class EnvConfigArgs(GQLArgsSet, GQLObject): 
      id: int ##NON NULL

   _args: EnvConfigArgs


   type: EnvConfig ##NON NULL

class addUserAlert(GQLMutation):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      input: addUserAlertInput

   _args: UserAlertArgs


   type: UserAlert ##NON NULL

class deleteUserAlerts(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject): 
      input: deleteUserAlertsInput ##NON NULL

   _args: IDArgs


   type: ID ##NON NULL

class editUserAlert(GQLMutation):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      input: editUserAlertInput ##NON NULL

   _args: UserAlertArgs


   type: UserAlert ##NON NULL

class updateUserAlerts(GQLMutation):
   class UserAlertArgs(GQLArgsSet, GQLObject): 
      input: UserAlertUpdateInput ##NON NULL ##LIST

   _args: UserAlertArgs


   type: UserAlert ##NON NULL

class createApiCertificates(GQLMutation):
   class ApiCertificateCreationResultArgs(GQLArgsSet, GQLObject): 
      certificates: ApiCertificateCreateInput ##NON NULL ##LIST

   _args: ApiCertificateCreationResultArgs


   type: ApiCertificateCreationResult ##NON NULL

class deleteApiCertificates(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      ids: ID ##NON NULL ##LIST

   _args: boolArgs


   type: bool ##NON NULL

class saveApiDevelopersToApi(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: SaveApiDevelopersInput ##NON NULL

   _args: boolArgs


   type: bool

class copyApiDevelopersFromVersion(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: CopyApiDevelopersInput

   _args: boolArgs


   type: bool

class createApiFavorites(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: CreateApiFavoritesInput ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class deleteApiFavorites(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: DeleteApiFavoritesInput ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class createApiFollowers(GQLMutation):
   class ApiFollowerArgs(GQLArgsSet, GQLObject): 
      apiFollowers: ApiFollowerCreateInput ##NON NULL

   _args: ApiFollowerArgs


   type: ApiFollower ##NON NULL

class deleteApiFollowers(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      apiFollowers: ApiFollowerDeleteInput ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class createApisFromSpecs(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject): 
      creations: ApiCreateFromSpecInput ##NON NULL ##LIST

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult ##NON NULL

class updateApisFromSpecs(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject): 
      updates: ApiUpdateFromSpecInput ##NON NULL ##LIST

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult ##NON NULL

class createApisFromRapidOas(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject): 
      creations: ApiCreateFromRapidOasInput ##NON NULL ##LIST

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult ##NON NULL

class updateApisFromRapidOas(GQLMutation):
   class ApiSpecImportResultArgs(GQLArgsSet, GQLObject): 
      updates: ApiUpdateFromRapidOasInput ##NON NULL ##LIST

   _args: ApiSpecImportResultArgs


   type: ApiSpecImportResult ##NON NULL

class createApiVersions(GQLMutation):
   class ApiVersionArgs(GQLArgsSet, GQLObject): 
      apiVersions: ApiVersionCreateInput ##NON NULL ##LIST

   _args: ApiVersionArgs


   type: ApiVersion ##NON NULL

class createGqlApiVersions(GQLMutation):
   class ApiVersionArgs(GQLArgsSet, GQLObject): 
      gqlApiVersions: GqlApiVersionCreateInput ##NON NULL ##LIST

   _args: ApiVersionArgs


   type: ApiVersion ##NON NULL

class updateApiVersions(GQLMutation):
   class ApiVersionArgs(GQLArgsSet, GQLObject): 
      apiVersions: ApiVersionUpdateInput ##NON NULL ##LIST

   _args: ApiVersionArgs


   type: ApiVersion ##NON NULL

class createApiVersionBillingPlanVersion(GQLMutation):
   class ApiVersionBillingPlanVersionArgs(GQLArgsSet, GQLObject): 
      input: createApiVersionBillingPlanVersionInput

   _args: ApiVersionBillingPlanVersionArgs


   type: ApiVersionBillingPlanVersion

class createApi(GQLMutation):
   class ApiArgs(GQLArgsSet, GQLObject): 
      api: ApiCreateInput ##NON NULL

   _args: ApiArgs


   type: Api ##NON NULL

class updateApi(GQLMutation):
   class ApiArgs(GQLArgsSet, GQLObject): 
      api: ApiUpdateInput ##NON NULL

   _args: ApiArgs


   type: Api ##NON NULL

class provisionSwaggerFiles(GQLMutation):
   class strArgs(GQLArgsSet, GQLObject): 
      input: ProvisionApiFromFileInput ##NON NULL ##LIST

   _args: strArgs


   type: str ##LIST

class deleteApi(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class createApplicationAuthorization(GQLMutation):
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject): 
      input: AppAuthorizationCreateInput ##NON NULL

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization ##NON NULL

class updateApplicationAuthorization(GQLMutation):
   class ApplicationAuthorizationArgs(GQLArgsSet, GQLObject): 
      input: AppAuthorizationUpdateInput ##NON NULL

   _args: ApplicationAuthorizationArgs


   type: ApplicationAuthorization ##NON NULL

class deleteApplicationAuthorization(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class addApplicationEnvironmentKey(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      input: AddApplicationEnvironmentKeyInput ##NON NULL

   _args: AnyArgs


   type: Any

class editApplicationEnvironmentKey(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      input: EditApplicationEnviornmentKeyInput ##NON NULL

   _args: AnyArgs


   type: Any

class deleteApplicationEnvironmentKey(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject): 
      input: DeleteApplicationEnvironmentKeyInput ##NON NULL

   _args: IDArgs


   type: ID

class generateAssetUploadUrl(GQLMutation):
   class AssetArgs(GQLArgsSet, GQLObject): 
      input: GenerateAssetUploadUrlInput ##NON NULL

   _args: AssetArgs


   type: Asset ##NON NULL

class deleteAsset(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class updateAssetUploaded(GQLMutation):
   class AssetArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: AssetArgs


   type: Asset

class updateAsset(GQLMutation):
   class AssetArgs(GQLArgsSet, GQLObject): 
      input: AssetUpdateInput ##NON NULL

   _args: AssetArgs


   type: Asset

class upsertAsyncApiConfiguration(GQLMutation):
   class AsyncApiConfigurationArgs(GQLArgsSet, GQLObject): 
      asyncApiConfigurations: AsyncApiConfigurationCreateInput ##NON NULL ##LIST

   _args: AsyncApiConfigurationArgs


   type: AsyncApiConfiguration ##NON NULL

class upsertUserAttributes(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      input: UserAttributesInput

   _args: AnyArgs


   type: Any

class updateUserAttributeItem(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      input: ThemeUserAttributesInput ##NON NULL

   _args: AnyArgs


   type: Any

class createAuthentications(GQLMutation):
   class AuthenticationArgs(GQLArgsSet, GQLObject): 
      authentications: AuthenticationCreateInput ##NON NULL ##LIST

   _args: AuthenticationArgs


   type: Authentication ##NON NULL

class updateAuthentications(GQLMutation):
   class AuthenticationArgs(GQLArgsSet, GQLObject): 
      authentications: AuthenticationUpdateInput ##NON NULL ##LIST

   _args: AuthenticationArgs


   type: Authentication ##NON NULL

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
      upsertBillingFeature: upsertBillingFeatureInput ##NON NULL

   _args: BillingFeatureArgs


   type: BillingFeature

class deleteBillingFeature(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      billingFeatureId: str

   _args: AnyArgs


   type: Any

class deleteBillingFeatures(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      billingFeatureIds: str ##LIST

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
      input: BillingItemUpsertInput ##NON NULL

   _args: BillingItemArgs


   type: BillingItem

class deleteBillingItem(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: AnyArgs


   type: Any

class deleteBillingItems(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      ids: ID ##NON NULL ##LIST

   _args: boolArgs


   type: bool ##NON NULL

class deleteBillingPlans(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      ids: ID ##NON NULL ##LIST

   _args: boolArgs


   type: bool

class updateAllowedPlanDevelopers(GQLMutation):
   class AllowedPlanDeveloperArgs(GQLArgsSet, GQLObject): 
      input: AllowedPlanDevelopersUpdateInput

   _args: AllowedPlanDeveloperArgs


   type: AllowedPlanDeveloper ##LIST

class editOrganizationInvoice(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: EditOrganizationInvoiceInput

   _args: boolArgs


   type: bool

class createBillingPlan(GQLMutation):
   class BillingPlanArgs(GQLArgsSet, GQLObject): 
      billingPlan: BillingPlanCreateInput ##NON NULL

   _args: BillingPlanArgs


   type: BillingPlan

class updateBillingPlanMetadata(GQLMutation):
   class BillingPlanArgs(GQLArgsSet, GQLObject): 
      billingPlan: BillingPlanMetadataUpdateInput ##NON NULL

   _args: BillingPlanArgs


   type: BillingPlan

class updateBillingPlanExtended(GQLMutation):
   class BillingPlanArgs(GQLArgsSet, GQLObject): 
      billingPlan: BillingPlanExtendedUpdateInput ##NON NULL

   _args: BillingPlanArgs


   type: BillingPlan

class upsertBillingPlanAndVersion(GQLMutation):
   class BillingPlanVersionArgs(GQLArgsSet, GQLObject): 
      upsertBillingPlanAndVersionInput: upsertBillingPlanAndVersionInput ##NON NULL

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
      category: CategoryCreateInput ##NON NULL

   _args: CategoryArgs


   type: Category ##NON NULL

class updateCategory(GQLMutation):
   class CategoryArgs(GQLArgsSet, GQLObject): 
      category: CategoryUpdateInput ##NON NULL

   _args: CategoryArgs


   type: Category ##NON NULL

class deleteCategories(GQLMutation):
   class DeletedCategoryArgs(GQLArgsSet, GQLObject): 
      categories: ID ##NON NULL ##LIST

   _args: DeletedCategoryArgs


   type: DeletedCategory ##NON NULL

class deleteCollection(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: boolArgs


   type: bool

class updateCollection(GQLMutation):
   class CollectionArgs(GQLArgsSet, GQLObject): 
      input: CollectionUpdateInput ##NON NULL

   _args: CollectionArgs


   type: Collection

class createCollection(GQLMutation):
   class CollectionArgs(GQLArgsSet, GQLObject): 
      input: CollectionCreateInput ##NON NULL

   _args: CollectionArgs


   type: Collection

class bulkUpdateCollections(GQLMutation):
   class CollectionArgs(GQLArgsSet, GQLObject): 
      collections: UpdateCollectionsInput ##NON NULL ##LIST

   _args: CollectionArgs


   type: Collection ##LIST

class updateCollections(GQLMutation):
   class CollectionArgs(GQLArgsSet, GQLObject): 
      collections: UpdateCollectionsInput ##NON NULL ##LIST

   _args: CollectionArgs


   type: Collection ##LIST

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
      entityAttributes: EntityAttribute ##NON NULL ##LIST

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
      endpointIds: str ##LIST

   _args: AnyArgs


   type: Any

class updateEndpointsCollectionOrder(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      endpointsCollectionOrder: EndpointOrder ##LIST

   _args: AnyArgs


   type: Any

class createEndpointsGroups(GQLMutation):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject): 
      groups: EndpointsGroupCreateInput ##NON NULL ##LIST

   _args: EndpointsGroupArgs


   type: EndpointsGroup ##NON NULL

class updateEndpointsGroups(GQLMutation):
   class EndpointsGroupArgs(GQLArgsSet, GQLObject): 
      groups: EndpointsGroupUpdateInput ##NON NULL ##LIST

   _args: EndpointsGroupArgs


   type: EndpointsGroup ##NON NULL

class deleteEndpointsGroups(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject): 
      ids: ID ##NON NULL ##LIST

   _args: IDArgs


   type: ID ##NON NULL

class duplicateNameCheck(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: DuplicateNameCheckInput

   _args: boolArgs


   type: bool

class createEntityMetadata(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      entityMetadata: EntityMetadataInput ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class updateEntityMetadata(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      entityMetadata: EntityMetadataInput ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

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
      input: UpdateGraphQLSchemaInput ##NON NULL

   _args: IDArgs


   type: ID ##NON NULL

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
      apiVersionId: str ##NON NULL
      topicName: str ##NON NULL
      options: SubscribeOptions ##NON NULL

   _args: SubscribeKafkaResponseArgs


   type: SubscribeKafkaResponse

class produceKafkaMessage(GQLMutation):
   class ProduceMessageResponseArgs(GQLArgsSet, GQLObject): 
      message: ProduceMessageInput ##NON NULL

   _args: ProduceMessageResponseArgs


   type: ProduceMessageResponse ##LIST

class postMessage(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      message: MessageCreateInput ##NON NULL

   _args: AnyArgs


   type: Any

class postMessageV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      message: MessageCreateInput ##NON NULL

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
      input: OrganizationUpdateInput ##NON NULL

   _args: OrganizationArgs


   type: Organization

class deleteOrganization(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class createOrganization(GQLMutation):
   class OrganizationArgs(GQLArgsSet, GQLObject): 
      input: OrganizationCreateInput ##NON NULL

   _args: OrganizationArgs


   type: Organization ##NON NULL

class createNewOrganizationV4(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      input: CreateNewOrganizationInputV4

   _args: AnyArgs


   type: Any

class generateResetPasswordToken(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      email: str ##NON NULL

   _args: AnyArgs


   type: Any

class resetUserPassword(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      input: ResetUserPasswordInput ##NON NULL

   _args: AnyArgs


   type: Any

class deletePayoutInfo(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      userId: ID ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class addProject(GQLMutation):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      input: AddProjectInput ##NON NULL

   _args: ProjectArgs


   type: Project

class addProjectV2(GQLMutation):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      input: AddProjectInput ##NON NULL

   _args: ProjectArgs


   type: Project

class editProjectV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      input: EditProjectInput ##NON NULL

   _args: AnyArgs


   type: Any

class deleteProject(GQLMutation):
   class IDArgs(GQLArgsSet, GQLObject): 
      input: DeleteProjectInput ##NON NULL

   _args: IDArgs


   type: ID

class createProject(GQLMutation):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      project: ProjectCreateInput ##NON NULL

   _args: ProjectArgs


   type: Project

class updateProject(GQLMutation):
   class ProjectArgs(GQLArgsSet, GQLObject): 
      project: ProjectUpdateInput ##NON NULL

   _args: ProjectArgs


   type: Project ##LIST

class createProjectAllowedAPIs(GQLMutation):
   class ProjectAllowedAPIArgs(GQLArgsSet, GQLObject): 
      input: createProjectAllowedAPIInput ##LIST

   _args: ProjectAllowedAPIArgs


   type: ProjectAllowedAPI ##LIST

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
      role: RoleUpdateInput ##NON NULL

   _args: AnyArgs


   type: Any

class updateRole(GQLMutation):
   class RoleArgs(GQLArgsSet, GQLObject): 
      role: RoleUpdateInput ##NON NULL

   _args: RoleArgs


   type: Role ##NON NULL

class deprecatedCreateRole(GQLMutation):
   class RoleArgs(GQLArgsSet, GQLObject): 
      role: RoleCreateInput ##NON NULL

   _args: RoleArgs


   type: Role ##NON NULL

class createRole(GQLMutation):
   class RoleArgs(GQLArgsSet, GQLObject): 
      role: RoleCreateInput ##NON NULL

   _args: RoleArgs


   type: Role ##NON NULL

class deprecatedDeleteRole(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      roleId: ID

   _args: AnyArgs


   type: Any

class deleteRole(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL ##LIST

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
      spotlight: SpotlightCreateInput ##NON NULL

   _args: SpotlightArgs


   type: Spotlight ##NON NULL

class updateSpotlight(GQLMutation):
   class SpotlightArgs(GQLArgsSet, GQLObject): 
      spotlight: SpotlightUpdateInput ##NON NULL

   _args: SpotlightArgs


   type: Spotlight ##NON NULL

class deleteSpotlight(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      spotlight: SpotlightDeleteInput ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class deleteSubscriptions(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      ids: ID ##NON NULL ##LIST

   _args: boolArgs


   type: bool

class deleteSubscription(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: boolArgs


   type: bool

class createSubscription(GQLMutation):
   class BillingSubscriptionArgs(GQLArgsSet, GQLObject): 
      input: SubscriptionCreateInput ##NON NULL

   _args: BillingSubscriptionArgs


   type: BillingSubscription ##NON NULL

class updateTargetGroups(GQLMutation):
   class TargetGroupArgs(GQLArgsSet, GQLObject): 
      targetGroups: TargetGroupUpdateInput ##NON NULL ##LIST

   _args: TargetGroupArgs


   type: TargetGroup ##NON NULL

class removeTeamUserFromAllOrgTeams(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      orgId: int ##NON NULL
      email: str ##NON NULL

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
      userId: int ##NON NULL
      teamIds: int ##NON NULL ##LIST

   _args: boolArgs


   type: bool

class deleteTeam(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: boolArgs


   type: bool

class createTeam(GQLMutation):
   class TeamArgs(GQLArgsSet, GQLObject): 
      input: TeamCreateInput ##NON NULL

   _args: TeamArgs


   type: Team

class updateTeam(GQLMutation):
   class TeamArgs(GQLArgsSet, GQLObject): 
      input: TeamUpdateInput ##NON NULL

   _args: TeamArgs


   type: Team

class updateTransactions(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: updateTransactionInput

   _args: boolArgs


   type: bool

class createTransformations(GQLMutation):
   class TransformationArgs(GQLArgsSet, GQLObject): 
      transformations: TransformationCreateInput ##NON NULL ##LIST

   _args: TransformationArgs


   type: Transformation ##NON NULL

class updateTransformations(GQLMutation):
   class TransformationArgs(GQLArgsSet, GQLObject): 
      transformations: TransformationUpdateInput ##NON NULL ##LIST

   _args: TransformationArgs


   type: Transformation ##NON NULL

class deleteTransformations(GQLMutation):
   class DeletedTransformationArgs(GQLArgsSet, GQLObject): 
      transformations: ID ##NON NULL ##LIST

   _args: DeletedTransformationArgs


   type: DeletedTransformation ##NON NULL

class createTutorial(GQLMutation):
   class TutorialArgs(GQLArgsSet, GQLObject): 
      tutorial: TutorialCreateInput ##NON NULL

   _args: TutorialArgs


   type: Tutorial

class updateTutorial(GQLMutation):
   class TutorialArgs(GQLArgsSet, GQLObject): 
      tutorial: TutorialUpdateInput ##NON NULL

   _args: TutorialArgs


   type: Tutorial

class deleteTutorial(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      tutorial: TutorialDeleteInput ##NON NULL

   _args: boolArgs


   type: bool ##NON NULL

class phoneAuthSetup(GQLMutation):
   class PhoneVerificationArgs(GQLArgsSet, GQLObject): 
      phoneNumber: str ##NON NULL

   _args: PhoneVerificationArgs


   type: PhoneVerification

class phoneAuthSetupVerify(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      code: str ##NON NULL
      token: str ##NON NULL

   _args: boolArgs


   type: bool

class authenticateUsingPhone(GQLMutation):
   class PhoneVerificationArgs(GQLArgsSet, GQLObject): 
      phoneId: ID ##NON NULL

   _args: PhoneVerificationArgs


   type: PhoneVerification

class authenticateUsingPhoneVerify(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      code: str ##NON NULL
      token: str ##NON NULL

   _args: boolArgs


   type: bool

class deletePhoneNumber(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      phoneId: int ##NON NULL

   _args: boolArgs


   type: bool

class generateRecoveryCodes(GQLMutation):
   type: RecoveryCode ##LIST

class regenerateRecoveryCodes(GQLMutation):
   type: RecoveryCode ##LIST

class markRecoveryCodeAsUsed(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      code: str ##NON NULL

   _args: boolArgs


   type: bool

class applicationAuthSetup(GQLMutation):
   type: str

class applicationAuthSetupVerify(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      code: str ##NON NULL

   _args: boolArgs


   type: bool

class authenticateUsingApp(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      code: str ##NON NULL

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
      token: str ##NON NULL

   _args: boolArgs


   type: bool

class bulkDeleteUserInvitesV2(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      emails: str ##LIST
      orgId: int

   _args: AnyArgs


   type: Any

class deleteUserInvites(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      input: UserInvitesDeleteInput ##NON NULL

   _args: AnyArgs


   type: Any

class bulkReactivateUserInvitesV2(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      emails: str ##LIST
      orgId: int

   _args: boolArgs


   type: bool

class reactivateUserInvites(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: UserInvitesReactivateInput ##NON NULL

   _args: boolArgs


   type: bool

class inviteUsersToTeams(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      usersToInvite: Any
      orgId: ID ##NON NULL
      meta: Any

   _args: boolArgs


   type: bool

class saveUserApi(GQLMutation):
   class UserSavedApiArgs(GQLArgsSet, GQLObject): 
      saveUserApi: SaveUserApi

   _args: UserSavedApiArgs


   type: UserSavedApi ##NON NULL

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
      userId: str ##NON NULL

   _args: AnyArgs


   type: Any

class updateUserEmail(GQLMutation):
   class AnyArgs(GQLArgsSet, GQLObject): 
      email: str ##NON NULL

   _args: AnyArgs


   type: Any

class verifyEmailCode(GQLMutation):
   class boolArgs(GQLArgsSet, GQLObject): 
      input: VerifyEmailCodeInput

   _args: boolArgs


   type: bool

class updateUser(GQLMutation):
   class UserArgs(GQLArgsSet, GQLObject): 
      input: UserUpdateInput ##NON NULL

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
