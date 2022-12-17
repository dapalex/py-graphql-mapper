from enum import Enum

class EnvConfigType(Enum):
   number = 'number'
   string = 'string'
   boolean = 'boolean'
   object = 'object'

class Brand(Enum):
   default = 'default'
   rakuten = 'rakuten'

class EventUrlSortables(Enum):
   ID = 'ID'
   URL = 'URL'

class Order(Enum):
   """
   Order - Order options

   """
   DESC = 'DESC' ##Descending
   ASC = 'ASC' ##Ascending

class GatewayInstanceSorting(Enum):
   ID = 'ID'
   DNS = 'DNS'
   TYPE = 'TYPE'
   DEPLOYMENT_KEY = 'DEPLOYMENT_KEY'
   SERVICE_STATUS = 'SERVICE_STATUS'
   STATUS = 'STATUS'

class GatewayTemplateSorting(Enum):
   ID = 'ID'
   NAME = 'NAME'
   DESCRIPTION = 'DESCRIPTION'
   URL_PATTERN = 'URL_PATTERN'

class GatewayTemplateParamsSortingFieldName(Enum):
   ID = 'ID'
   CODE_TEMPLATE_ID = 'CODE_TEMPLATE_ID'
   PARAM_NAME = 'PARAM_NAME'
   PARAM_VALUE = 'PARAM_VALUE'
   PARAM_DESCRIPTION = 'PARAM_DESCRIPTION'
   STATUS = 'STATUS'

class AdminAuditLogSortables(Enum):
   CREATED_AT = 'CREATED_AT'

class EventLogSortables(Enum):
   CREATED_AT = 'CREATED_AT'

class GatewayType(Enum):
   RapidAPI = 'RapidAPI'
   Apigee = 'Apigee'
   Kong = 'Kong'
   WSO2 = 'WSO2'

class MessageKey(Enum):
   MISSING_KEY = 'MISSING_KEY'
   BLOCKED_USER = 'BLOCKED_USER'
   DISABLED_ENDPOINT = 'DISABLED_ENDPOINT'
   MISSING_REQUIRED_PARAM = 'MISSING_REQUIRED_PARAM'
   UNKNOWN_PARAMS = 'UNKNOWN_PARAMS'
   APP_LIMIT_API_ERROR = 'APP_LIMIT_API_ERROR'
   API_GATEWAY_ERROR = 'API_GATEWAY_ERROR'
   QUOTA_THROTTLED = 'QUOTA_THROTTLED'
   QUOTA_REACHED = 'QUOTA_REACHED'
   INVALID_KET = 'INVALID_KET'
   API_MISSING = 'API_MISSING'
   NOT_SUBSCRIBED = 'NOT_SUBSCRIBED'
   RATE_LIMIT = 'RATE_LIMIT'
   GENERIC_ERROR = 'GENERIC_ERROR'

class AlertStatus(Enum):
   Enabled = 'Enabled'
   Disabled = 'Disabled'

class Channel(Enum):
   Email = 'Email'
   SMS = 'SMS'

class Condition(Enum):
   gt = 'gt'
   gte = 'gte'
   lt = 'lt'
   lte = 'lte'
   eq = 'eq'

class time(Enum):
   second = 'second'
   minute = 'minute'
   hour = 'hour'
   day = 'day'

class ApiCertificatePublicKeySignatureAlgorithm(Enum):
   RSA_ENCRYPTION = 'RSA_ENCRYPTION'

class ApiCertificateSortingFieldName(Enum):
   CREATED_AT = 'CREATED_AT'

class ApiDeveloperStatus(Enum):
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class ApiFollowerSortingFieldName(Enum):
   ID = 'ID'
   FOLLOWER_ID = 'FOLLOWER_ID'
   API_ID = 'API_ID'
   CREATED_AT = 'CREATED_AT'

class ApiSpecType(Enum):
   OPENAPI = 'OPENAPI'
   POSTMAN_COLLECTION = 'POSTMAN_COLLECTION'

class ApiSpecImportWarningType(Enum):
   PROP_NOT_ALLOWED = 'PROP_NOT_ALLOWED'
   MIN_NUMBER_VALUE_EXCEEDED = 'MIN_NUMBER_VALUE_EXCEEDED'
   MIN_EXCLUSIVE_NUMBER_VALUE_EXCEEDED = 'MIN_EXCLUSIVE_NUMBER_VALUE_EXCEEDED'
   MIN_OBJECT_PROP_COUNT_EXCEEDED = 'MIN_OBJECT_PROP_COUNT_EXCEEDED'
   MAX_OBJECT_PROP_COUNT_EXCEEDED = 'MAX_OBJECT_PROP_COUNT_EXCEEDED'
   MIN_ARRAY_ITEM_COUNT_EXCEEDED = 'MIN_ARRAY_ITEM_COUNT_EXCEEDED'
   FORMAT_MISMATCH = 'FORMAT_MISMATCH'
   ARRAY_DUPLICATE_ITEMS_NOT_ALLOWED = 'ARRAY_DUPLICATE_ITEMS_NOT_ALLOWED'
   HAS_DUPLICATE_ENDPOINTS = 'HAS_DUPLICATE_ENDPOINTS'
   UNKNOWN = 'UNKNOWN'

class ApiSpecImportProcessIssueSeverity(Enum):
   """
   ApiSpecImportProcessIssueSeverity - Indicates the severity of an individual import process issue.
In the event an import process for **creating a brand new API** encounters one or more issues marked as `ERROR` - the API would *not* be created (will be cleared off as soon as the process is finished).

   """
   WARNING = 'WARNING'
   ERROR = 'ERROR'

class StatsGroupBy(Enum):
   api = 'api'
   project = 'project'
   date = 'date'

class VersionStatus(Enum):
   DRAFT = 'DRAFT'
   ACTIVE = 'ACTIVE'
   DEPRECATED = 'DEPRECATED'

class apiSubTypeEnum(Enum):
   rest = 'rest'
   graphql = 'graphql'
   kafka = 'kafka'
   soap = 'soap'

class ApiStatus(Enum):
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class ApiPricing(Enum):
   FREE = 'FREE'
   PAID = 'PAID'
   FREEMIUM = 'FREEMIUM'

class ApiType(Enum):
   http = 'http'
   kafka = 'kafka'
   async_ = 'async'

class SchemaValidationUnknownAttributePolicy(Enum):
   BLOCK = 'BLOCK'
   STRIP = 'STRIP'
   PASSTHROUGH = 'PASSTHROUGH'

class ApiImportFileFormat(Enum):
   openapi = 'openapi'
   postman_collection = 'postman_collection'

class ApiSortingFieldName(Enum):
   NAME = 'NAME'
   VISIBILITY = 'VISIBILITY'
   CREATED_AT = 'CREATED_AT'
   UPDATED_AT = 'UPDATED_AT'

class ApiVisibility(Enum):
   PUBLIC = 'PUBLIC'
   PRIVATE = 'PRIVATE'

class GqlSchemaSourceType(Enum):
   introspection = 'introspection' ##make an introspection call to the api server to get the schema definition
   SDL = 'SDL' ##schema definition language
   schemaAST = 'schemaAST' ##AST representation of the schema

class AppAuthorizationType(Enum):
   RAPIDAPI = 'RAPIDAPI'
   OAUTH2 = 'OAUTH2'

class AuthorizationGrantType(Enum):
   CLIENT_CREDENTIALS = 'CLIENT_CREDENTIALS'
   AUTHORIZATION_CODE = 'AUTHORIZATION_CODE'

class AppAuthorizationStatus(Enum):
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class AuthorizationType(Enum):
   RAPIDAPI = 'RAPIDAPI'
   OAUTH2 = 'OAUTH2'

class EnvironmentName(Enum):
   Testing = 'Testing'
   Production = 'Production'

class AuthenticationType(Enum):
   NO_AUTH = 'NO_AUTH'
   RAPID = 'RAPID'
   BASIC = 'BASIC'
   HEADER = 'HEADER'
   QUERY = 'QUERY'
   OAUTH2 = 'OAUTH2'

class GrantType(Enum):
   CLIENT_CREDENTIALS = 'CLIENT_CREDENTIALS'
   AUTHORIZATION_CODE = 'AUTHORIZATION_CODE'

class SeparatorType(Enum):
   SPACE = 'SPACE'
   COMMA = 'COMMA'

class ClientAuthenticationType(Enum):
   HEADER = 'HEADER'
   BODY = 'BODY'

class BillingFeatureStatus(Enum):
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class BillingPlanType(Enum):
   MONTHLY = 'MONTHLY'
   PERUSE = 'PERUSE'

class CategoryLanguage(Enum):
   EN_US = 'EN_US'
   FR_FR = 'FR_FR'
   ES_ES = 'ES_ES'
   DE_DE = 'DE_DE'
   IT_IT = 'IT_IT'
   JA_JP = 'JA_JP'
   KO_KR = 'KO_KR'
   RU_RU = 'RU_RU'
   HI_IN = 'HI_IN'
   HE_IL = 'HE_IL'
   NL_NL = 'NL_NL'
   TR_TR = 'TR_TR'
   UK_UA = 'UK_UA'
   ZH_CN = 'ZH_CN'
   PT_BR = 'PT_BR'

class CategorySortingFieldName(Enum):
   ID = 'ID'
   NAME = 'NAME'
   WEIGHT = 'WEIGHT'
   CREATED_AT = 'CREATED_AT'
   UPDATED_AT = 'UPDATED_AT'

class OrderDirection(Enum):
   desc = 'desc'
   asc = 'asc'
   DESC = 'DESC'
   ASC = 'ASC'

class HttpMethod(Enum):
   GET = 'GET'
   POST = 'POST'
   PUT = 'PUT'
   DELETE = 'DELETE'
   PATCH = 'PATCH'
   HEAD = 'HEAD'

class Resolution(Enum):
   seconds = 'seconds'
   minutes = 'minutes'
   hours = 'hours'
   days = 'days'
   months = 'months'
   years = 'years'

class TransactionPaymentStatus(Enum):
   paid = 'paid'
   partially_refunded = 'partially_refunded'
   refunded = 'refunded'
   declined = 'declined'
   pending = 'pending'

class Locale(Enum):
   EN = 'EN'
   FR = 'FR'
   ES = 'ES'
   DE = 'DE'
   IT = 'IT'
   JA = 'JA'
   KO = 'KO'
   RU = 'RU'
   HI = 'HI'
   NL = 'NL'
   TR = 'TR'
   UK = 'UK'
   ZH = 'ZH'
   PT = 'PT'
   HE = 'HE'

class Visibility(Enum):
   PUBLIC = 'PUBLIC'
   PRIVATE = 'PRIVATE'

class DeletionStatus(Enum):
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class SortingFieldOrder(Enum):
   ASC = 'ASC'
   DESC = 'DESC'

class ConsumersType(Enum):
   ALL = 'ALL'
   FREE = 'FREE'
   PAID = 'PAID'

class ApiEndpointHttpMethod(Enum):
   GET = 'GET'
   POST = 'POST'
   PUT = 'PUT'
   PATCH = 'PATCH'
   DELETE = 'DELETE'

class EntityType(Enum):
   Organization = 'Organization'
   Team = 'Team'
   User = 'User'

class EntityMetadataSortingFieldName(Enum):
   ID = 'ID'
   ENTITY_ID = 'ENTITY_ID'
   ATTRIBUTE_NAME = 'ATTRIBUTE_NAME'
   ATTRIBUTE_VALUE = 'ATTRIBUTE_VALUE'

class EntityRoleSortingFieldName(Enum):
   ID = 'ID'

class GRAPH_QL_SCHEMA_STATUS(Enum):
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class SchemaType(Enum):
   AVRO = 'AVRO'
   PROTOBUF = 'PROTOBUF'
   JSON = 'JSON'

class Compression(Enum):
   gzip = 'gzip'
   snappy = 'snappy'
   lz4 = 'lz4'
   zstd = 'zstd'

class MessageType(Enum):
   support = 'support'
   announcement = 'announcement'

class EntityStatusFlag(Enum):
   none = 'none'
   read = 'read'
   archived = 'archived'
   starred = 'starred'

class UnsubscribeReasons(Enum):
   SWITCH_PLAN = 'SWITCH_PLAN'
   TEMPORARY_USE = 'TEMPORARY_USE'
   BAD_FEATURES = 'BAD_FEATURES'
   BUGS = 'BUGS'
   ALTERNATIVE_API = 'ALTERNATIVE_API'
   EXPENSIVE = 'EXPENSIVE'
   OTHER = 'OTHER'

class RapidReasonsEvents(Enum):
   UNSUBSCRIBE = 'UNSUBSCRIBE'

class RequestLogsOrderBy(Enum):
   requestId = 'requestId'
   projectId = 'projectId'
   api = 'api'
   apiId = 'apiId'
   endpoint = 'endpoint'
   httpMethod = 'httpMethod'
   period = 'period'
   apiLatency = 'apiLatency'
   callTime = 'callTime'
   originIp = 'originIp'
   originCountry = 'originCountry'
   engineError = 'engineError'
   httpStatus = 'httpStatus'
   reqHeadersSize = 'reqHeadersSize'
   resHeadersSize = 'resHeadersSize'
   reqBodySize = 'reqBodySize'
   resBodySize = 'resBodySize'

class RoleLevel(Enum):
   ORGANIZATION = 'ORGANIZATION'
   USER_ENVIRONMENT = 'USER_ENVIRONMENT'
   USER_ORGANIZATION = 'USER_ORGANIZATION'
   USER_TEAM = 'USER_TEAM'
   TEAM_ENVIRONMENT = 'TEAM_ENVIRONMENT'

class RoleSortingFieldName(Enum):
   NAME = 'NAME'

class SearchApiSortingFieldName(Enum):
   ByRelevance = 'ByRelevance'
   ByAlphabetical = 'ByAlphabetical'
   ByUpdatedAt = 'ByUpdatedAt'
   installsAllTime = 'installsAllTime'

class SearchCollectionSortingFieldName(Enum):
   id = 'id'
   title = 'title'
   slugifiedKey = 'slugifiedKey'
   weight = 'weight'
   thumbnail = 'thumbnail'
   shortDescription = 'shortDescription'
   type = 'type'

class SecretParameterPlacement(Enum):
   QUERY = 'QUERY'
   HEADER = 'HEADER'

class SpotlightType(Enum):
   link = 'link'
   link_pdf = 'link_pdf'
   file_pdf = 'file_pdf'

class SpotlightFieldName(Enum):
   id = 'id'
   type = 'type'
   apiId = 'apiId'
   spotlightURL = 'spotlightURL'
   status = 'status'
   slugifiedName = 'slugifiedName'
   thumbnailURL = 'thumbnailURL'
   title = 'title'
   description = 'description'
   weight = 'weight'
   published = 'published'
   updatedAt = 'updatedAt'
   createdAt = 'createdAt'

class LoadBalancingStrategy(Enum):
   RANDOM = 'RANDOM'
   GEO_IP = 'GEO_IP'

class TransformationConditionType(Enum):
   IGNORE = 'IGNORE'
   OVERWRITE = 'OVERWRITE'

class TransformationActionType(Enum):
   ADD = 'ADD'
   REMOVE = 'REMOVE'
   REMAP = 'REMAP'
   METHOD = 'METHOD'
   PATH = 'PATH'
   BASE_URL = 'BASE_URL'

class TransformationValueType(Enum):
   VARIABLE = 'VARIABLE'
   STATIC = 'STATIC'
   TEMPLATE = 'TEMPLATE'

class TransformationMethodType(Enum):
   POST = 'POST'
   GET = 'GET'
   PUT = 'PUT'
   DELETE = 'DELETE'
   PATCH = 'PATCH'

class TransformationType(Enum):
   REQUEST = 'REQUEST'
   RESPONSE = 'RESPONSE'

class TransformationSortingFieldName(Enum):
   ID = 'ID'
   CREATED_AT = 'CREATED_AT'
   UPDATED_AT = 'UPDATED_AT'

class TutorialType(Enum):
   API_TUTORIAL = 'API_TUTORIAL'

class TutorialFieldName(Enum):
   id = 'id'
   slugifiedName = 'slugifiedName'
   apiId = 'apiId'
   apiVersion = 'apiVersion'
   authorId = 'authorId'
   published = 'published'
   title = 'title'
   content = 'content'
   thumbnailURL = 'thumbnailURL'
   publishedDate = 'publishedDate'
   readTime = 'readTime'
   type = 'type'
   createdAt = 'createdAt'
   updatedAt = 'updatedAt'

class UsageResolution(Enum):
   """
   UsageResolution - Specifing a `UsageResolution` unit does not affect the overall request counts retrieved; they are calculated solely per the provided time range.
`UsageResolution` is merely just for grouping counts.

   """
   seconds = 'seconds'
   minutes = 'minutes'
   hours = 'hours'
   days = 'days'
   months = 'months'
   years = 'years'

class WorkflowStatus(Enum):
   OPEN = 'OPEN'
   APPROVED = 'APPROVED'
   REJECTED = 'REJECTED'

class WorkflowTopic(Enum):
   PublishAPI = 'PublishAPI'
   RequestAccessPlan = 'RequestAccessPlan'
   SignupRequestApproval = 'SignupRequestApproval'
   JoinOrganization = 'JoinOrganization'

class SignupApprovalWorkflowTopic(Enum):
   SignupRequestApproval = 'SignupRequestApproval'

