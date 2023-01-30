from enum import Enum

class EnvConfigType(Enum):
   DEFAULT = None
   number = 'number'
   string = 'string'
   boolean = 'boolean'
   object = 'object'

class Brand(Enum):
   DEFAULT = None
   default = 'default'
   rakuten = 'rakuten'

class EventUrlSortables(Enum):
   DEFAULT = None
   ID = 'ID'
   URL = 'URL'

class Order(Enum):
   """
   Order - Order options

   """
   DEFAULT = None
   DESC = 'DESC' ##Descending
   ASC = 'ASC' ##Ascending

class GatewayInstanceSorting(Enum):
   DEFAULT = None
   ID = 'ID'
   DNS = 'DNS'
   TYPE = 'TYPE'
   DEPLOYMENT_KEY = 'DEPLOYMENT_KEY'
   SERVICE_STATUS = 'SERVICE_STATUS'
   STATUS = 'STATUS'

class GatewayTemplateSorting(Enum):
   DEFAULT = None
   ID = 'ID'
   NAME = 'NAME'
   DESCRIPTION = 'DESCRIPTION'
   URL_PATTERN = 'URL_PATTERN'

class GatewayTemplateParamsSortingFieldName(Enum):
   DEFAULT = None
   ID = 'ID'
   CODE_TEMPLATE_ID = 'CODE_TEMPLATE_ID'
   PARAM_NAME = 'PARAM_NAME'
   PARAM_VALUE = 'PARAM_VALUE'
   PARAM_DESCRIPTION = 'PARAM_DESCRIPTION'
   STATUS = 'STATUS'

class AdminAuditLogSortables(Enum):
   DEFAULT = None
   CREATED_AT = 'CREATED_AT'

class EventLogSortables(Enum):
   DEFAULT = None
   CREATED_AT = 'CREATED_AT'

class GatewayType(Enum):
   DEFAULT = None
   RapidAPI = 'RapidAPI'
   Apigee = 'Apigee'
   Kong = 'Kong'
   WSO2 = 'WSO2'

class MessageKey(Enum):
   DEFAULT = None
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
   DEFAULT = None
   Enabled = 'Enabled'
   Disabled = 'Disabled'

class Channel(Enum):
   DEFAULT = None
   Email = 'Email'
   SMS = 'SMS'

class Condition(Enum):
   DEFAULT = None
   gt = 'gt'
   gte = 'gte'
   lt = 'lt'
   lte = 'lte'
   eq = 'eq'

class time(Enum):
   DEFAULT = None
   second = 'second'
   minute = 'minute'
   hour = 'hour'
   day = 'day'

class ApiCertificatePublicKeySignatureAlgorithm(Enum):
   DEFAULT = None
   RSA_ENCRYPTION = 'RSA_ENCRYPTION'

class ApiCertificateSortingFieldName(Enum):
   DEFAULT = None
   CREATED_AT = 'CREATED_AT'

class ApiDeveloperStatus(Enum):
   DEFAULT = None
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class ApiFollowerSortingFieldName(Enum):
   DEFAULT = None
   ID = 'ID'
   FOLLOWER_ID = 'FOLLOWER_ID'
   API_ID = 'API_ID'
   CREATED_AT = 'CREATED_AT'

class ApiSpecType(Enum):
   DEFAULT = None
   OPENAPI = 'OPENAPI'
   POSTMAN_COLLECTION = 'POSTMAN_COLLECTION'

class ApiSpecImportWarningType(Enum):
   DEFAULT = None
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
   DEFAULT = None
   WARNING = 'WARNING'
   ERROR = 'ERROR'

class StatsGroupBy(Enum):
   DEFAULT = None
   api = 'api'
   project = 'project'
   date = 'date'

class VersionStatus(Enum):
   DEFAULT = None
   DRAFT = 'DRAFT'
   ACTIVE = 'ACTIVE'
   DEPRECATED = 'DEPRECATED'

class apiSubTypeEnum(Enum):
   DEFAULT = None
   rest = 'rest'
   graphql = 'graphql'
   kafka = 'kafka'
   soap = 'soap'

class ApiStatus(Enum):
   DEFAULT = None
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class ApiPricing(Enum):
   DEFAULT = None
   FREE = 'FREE'
   PAID = 'PAID'
   FREEMIUM = 'FREEMIUM'

class ApiType(Enum):
   DEFAULT = None
   http = 'http'
   kafka = 'kafka'
   async_ = 'async'

class SchemaValidationUnknownAttributePolicy(Enum):
   DEFAULT = None
   BLOCK = 'BLOCK'
   STRIP = 'STRIP'
   PASSTHROUGH = 'PASSTHROUGH'

class ApiImportFileFormat(Enum):
   DEFAULT = None
   openapi = 'openapi'
   postman_collection = 'postman_collection'

class ApiSortingFieldName(Enum):
   DEFAULT = None
   NAME = 'NAME'
   VISIBILITY = 'VISIBILITY'
   CREATED_AT = 'CREATED_AT'
   UPDATED_AT = 'UPDATED_AT'

class ApiVisibility(Enum):
   DEFAULT = None
   PUBLIC = 'PUBLIC'
   PRIVATE = 'PRIVATE'

class GqlSchemaSourceType(Enum):
   DEFAULT = None
   introspection = 'introspection' ##make an introspection call to the api server to get the schema definition
   SDL = 'SDL' ##schema definition language
   schemaAST = 'schemaAST' ##AST representation of the schema

class AppAuthorizationType(Enum):
   DEFAULT = None
   RAPIDAPI = 'RAPIDAPI'
   OAUTH2 = 'OAUTH2'

class AuthorizationGrantType(Enum):
   DEFAULT = None
   CLIENT_CREDENTIALS = 'CLIENT_CREDENTIALS'
   AUTHORIZATION_CODE = 'AUTHORIZATION_CODE'

class AppAuthorizationStatus(Enum):
   DEFAULT = None
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class AuthorizationType(Enum):
   DEFAULT = None
   RAPIDAPI = 'RAPIDAPI'
   OAUTH2 = 'OAUTH2'

class EnvironmentName(Enum):
   DEFAULT = None
   Testing = 'Testing'
   Production = 'Production'

class AuthenticationType(Enum):
   DEFAULT = None
   NO_AUTH = 'NO_AUTH'
   RAPID = 'RAPID'
   BASIC = 'BASIC'
   HEADER = 'HEADER'
   QUERY = 'QUERY'
   OAUTH2 = 'OAUTH2'

class GrantType(Enum):
   DEFAULT = None
   CLIENT_CREDENTIALS = 'CLIENT_CREDENTIALS'
   AUTHORIZATION_CODE = 'AUTHORIZATION_CODE'

class SeparatorType(Enum):
   DEFAULT = None
   SPACE = 'SPACE'
   COMMA = 'COMMA'

class ClientAuthenticationType(Enum):
   DEFAULT = None
   HEADER = 'HEADER'
   BODY = 'BODY'

class BillingFeatureStatus(Enum):
   DEFAULT = None
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class BillingPlanType(Enum):
   DEFAULT = None
   MONTHLY = 'MONTHLY'
   PERUSE = 'PERUSE'

class CategoryLanguage(Enum):
   DEFAULT = None
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
   DEFAULT = None
   ID = 'ID'
   NAME = 'NAME'
   WEIGHT = 'WEIGHT'
   CREATED_AT = 'CREATED_AT'
   UPDATED_AT = 'UPDATED_AT'

class OrderDirection(Enum):
   DEFAULT = None
   desc = 'desc'
   asc = 'asc'
   DESC = 'DESC'
   ASC = 'ASC'

class HttpMethod(Enum):
   DEFAULT = None
   GET = 'GET'
   POST = 'POST'
   PUT = 'PUT'
   DELETE = 'DELETE'
   PATCH = 'PATCH'
   HEAD = 'HEAD'

class Resolution(Enum):
   DEFAULT = None
   seconds = 'seconds'
   minutes = 'minutes'
   hours = 'hours'
   days = 'days'
   months = 'months'
   years = 'years'

class TransactionPaymentStatus(Enum):
   DEFAULT = None
   paid = 'paid'
   partially_refunded = 'partially_refunded'
   refunded = 'refunded'
   declined = 'declined'
   pending = 'pending'

class Locale(Enum):
   DEFAULT = None
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
   DEFAULT = None
   PUBLIC = 'PUBLIC'
   PRIVATE = 'PRIVATE'

class DeletionStatus(Enum):
   DEFAULT = None
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class SortingFieldOrder(Enum):
   DEFAULT = None
   ASC = 'ASC'
   DESC = 'DESC'

class ConsumersType(Enum):
   DEFAULT = None
   ALL = 'ALL'
   FREE = 'FREE'
   PAID = 'PAID'

class ApiEndpointHttpMethod(Enum):
   DEFAULT = None
   GET = 'GET'
   POST = 'POST'
   PUT = 'PUT'
   PATCH = 'PATCH'
   DELETE = 'DELETE'

class EntityType(Enum):
   DEFAULT = None
   Organization = 'Organization'
   Team = 'Team'
   User = 'User'

class EntityMetadataSortingFieldName(Enum):
   DEFAULT = None
   ID = 'ID'
   ENTITY_ID = 'ENTITY_ID'
   ATTRIBUTE_NAME = 'ATTRIBUTE_NAME'
   ATTRIBUTE_VALUE = 'ATTRIBUTE_VALUE'

class EntityRoleSortingFieldName(Enum):
   DEFAULT = None
   ID = 'ID'

class GRAPH_QL_SCHEMA_STATUS(Enum):
   DEFAULT = None
   ACTIVE = 'ACTIVE'
   DELETED = 'DELETED'

class SchemaType(Enum):
   DEFAULT = None
   AVRO = 'AVRO'
   PROTOBUF = 'PROTOBUF'
   JSON = 'JSON'

class Compression(Enum):
   DEFAULT = None
   gzip = 'gzip'
   snappy = 'snappy'
   lz4 = 'lz4'
   zstd = 'zstd'

class MessageType(Enum):
   DEFAULT = None
   support = 'support'
   announcement = 'announcement'

class EntityStatusFlag(Enum):
   DEFAULT = None
   none = 'none'
   read = 'read'
   archived = 'archived'
   starred = 'starred'

class UnsubscribeReasons(Enum):
   DEFAULT = None
   SWITCH_PLAN = 'SWITCH_PLAN'
   TEMPORARY_USE = 'TEMPORARY_USE'
   BAD_FEATURES = 'BAD_FEATURES'
   BUGS = 'BUGS'
   ALTERNATIVE_API = 'ALTERNATIVE_API'
   EXPENSIVE = 'EXPENSIVE'
   OTHER = 'OTHER'

class RapidReasonsEvents(Enum):
   DEFAULT = None
   UNSUBSCRIBE = 'UNSUBSCRIBE'

class RequestLogsOrderBy(Enum):
   DEFAULT = None
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
   DEFAULT = None
   ORGANIZATION = 'ORGANIZATION'
   USER_ENVIRONMENT = 'USER_ENVIRONMENT'
   USER_ORGANIZATION = 'USER_ORGANIZATION'
   USER_TEAM = 'USER_TEAM'
   TEAM_ENVIRONMENT = 'TEAM_ENVIRONMENT'

class RoleSortingFieldName(Enum):
   DEFAULT = None
   NAME = 'NAME'

class SearchApiSortingFieldName(Enum):
   DEFAULT = None
   ByRelevance = 'ByRelevance'
   ByAlphabetical = 'ByAlphabetical'
   ByUpdatedAt = 'ByUpdatedAt'
   installsAllTime = 'installsAllTime'

class SearchCollectionSortingFieldName(Enum):
   DEFAULT = None
   id = 'id'
   title = 'title'
   slugifiedKey = 'slugifiedKey'
   weight = 'weight'
   thumbnail = 'thumbnail'
   shortDescription = 'shortDescription'
   type = 'type'

class SecretParameterPlacement(Enum):
   DEFAULT = None
   QUERY = 'QUERY'
   HEADER = 'HEADER'

class SpotlightType(Enum):
   DEFAULT = None
   link = 'link'
   link_pdf = 'link_pdf'
   file_pdf = 'file_pdf'

class SpotlightFieldName(Enum):
   DEFAULT = None
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
   DEFAULT = None
   RANDOM = 'RANDOM'
   GEO_IP = 'GEO_IP'

class TransformationConditionType(Enum):
   DEFAULT = None
   IGNORE = 'IGNORE'
   OVERWRITE = 'OVERWRITE'

class TransformationActionType(Enum):
   DEFAULT = None
   ADD = 'ADD'
   REMOVE = 'REMOVE'
   REMAP = 'REMAP'
   METHOD = 'METHOD'
   PATH = 'PATH'
   BASE_URL = 'BASE_URL'

class TransformationValueType(Enum):
   DEFAULT = None
   VARIABLE = 'VARIABLE'
   STATIC = 'STATIC'
   TEMPLATE = 'TEMPLATE'

class TransformationMethodType(Enum):
   DEFAULT = None
   POST = 'POST'
   GET = 'GET'
   PUT = 'PUT'
   DELETE = 'DELETE'
   PATCH = 'PATCH'

class TransformationType(Enum):
   DEFAULT = None
   REQUEST = 'REQUEST'
   RESPONSE = 'RESPONSE'

class TransformationSortingFieldName(Enum):
   DEFAULT = None
   ID = 'ID'
   CREATED_AT = 'CREATED_AT'
   UPDATED_AT = 'UPDATED_AT'

class TutorialType(Enum):
   DEFAULT = None
   API_TUTORIAL = 'API_TUTORIAL'

class TutorialFieldName(Enum):
   DEFAULT = None
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
   DEFAULT = None
   seconds = 'seconds'
   minutes = 'minutes'
   hours = 'hours'
   days = 'days'
   months = 'months'
   years = 'years'

class WorkflowStatus(Enum):
   DEFAULT = None
   OPEN = 'OPEN'
   APPROVED = 'APPROVED'
   REJECTED = 'REJECTED'

class WorkflowTopic(Enum):
   DEFAULT = None
   PublishAPI = 'PublishAPI'
   RequestAccessPlan = 'RequestAccessPlan'
   SignupRequestApproval = 'SignupRequestApproval'
   JoinOrganization = 'JoinOrganization'
   RequestApplicationAuthorization = 'RequestApplicationAuthorization'

class SignupApprovalWorkflowTopic(Enum):
   DEFAULT = None
   SignupRequestApproval = 'SignupRequestApproval'
