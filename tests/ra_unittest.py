from pygqlmap.network import GQLResponse
import requests
from codegen.network import fetch_schema_obj
from codegen.generator import CodeGenerator
from codegen.query_presets import QUERY_SCHEMA_AND_TYPES
from .consts import RAPIDAPI_HEADERS, RAPIDAPI_URL
import logging as logger

def run_fetch_ra_schema():
    logger.info('\nRunning run_fetch_ra_schema...')

    try:
        gqlSchema = fetch_schema_obj(RAPIDAPI_URL, RAPIDAPI_HEADERS, QUERY_SCHEMA_AND_TYPES)

        if gqlSchema:
            logger.info('Generating python types from GraphQL data...')
            CodeGenerator.generate_code(gqlSchema, folder='tests\\output\\rapidapi\\', log_progress=True)
            logger.info('Python types generated')
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!!' + ex.args[0])

    logger.info("End of run_fetch_ra_schema")

def run_fetch_ra_schema_no_desc():
    logger.info('\nRunning run_fetch_ra_schema_no_desc...')

    try:
        gqlSchema = fetch_schema_obj(RAPIDAPI_URL, RAPIDAPI_HEADERS, QUERY_SCHEMA_AND_TYPES)

        if gqlSchema:
            logger.info('Generating python types from GraphQL data...')
            CodeGenerator.generate_code(gqlSchema, folder='tests\\output\\rapidapi_nodesc\\', add_desc=False, log_progress=True)
            logger.info('Python types generated')
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!!' + ex.args[0])

    logger.info("End of run_fetch_ra_schema_no_desc")

def run_ra_create_transformations_mutation():
    logger.info('\nRunning Run_ra_create_transformations_mutation...')
    try:
        logger.info('Creating mutation python object...')
        from .output.rapidapi.gql_types import TransformationCreateInput, TransformationActionType, TransformationType, TransformationConditionType
        from .output.rapidapi.mutations import Mutations

        mutation = Mutations.createTransformations.value()

        input1 = TransformationCreateInput()
        input1.apiVersionId = 1
        input1.action = TransformationActionType.ADD
        input1.endpoints = ["myID"]
        input1.transformationType = TransformationType.REQUEST
        input1.condition = TransformationConditionType.IGNORE
        input1.targetPath = "."
        input1._from = "a"
        input1.target = "b"
        input1.value = "val"
        input1.plans = ["planID"]

        input2 = TransformationCreateInput()
        input2.apiVersionId = 1
        input2.action = TransformationActionType.REMOVE
        input2.endpoints = ["myID"]
        input2.transformationType = TransformationType.REQUEST
        input2.condition = TransformationConditionType.IGNORE
        input2.targetPath = "."
        input2._from = "a"
        input2.target = "b"
        input2.value = "val"
        input2.plans = ["planID"]

        logger.info('Inserting python mutation input data...')

        mutation._args.transformations = [input1, input2]

        logger.info(mutation.export_gql_source)

        logger.info('Calling GraphQL Server......')
        response = requests.request('POST', url=RAPIDAPI_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=RAPIDAPI_HEADERS)
        logger.info('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of Run_ra_create_transformations_mutation")

def run_ra_create_gateway_instance_mutation():
    logger.info('\nRunning run_ra_create_gateway_instance_mutation...')
    try:
        logger.info('Creating mutation python object...')
        from .output.rapidapi.gql_types import GatewayInstanceCreateInput, GatewayConfigurationCreateInput, GatewayCustomMessageCreateInput, MessageKey, GatewayType
        from .output.rapidapi.mutations import Mutations

        mutation = Mutations.createGatewayInstance.value()

        mutation._args.createDto = GatewayInstanceCreateInput()
        mutation._args.createDto.apiGatewayCodeTemplateId = 12314
        mutation._args.createDto.dns = 'mydomain.com'
        mutation._args.createDto.configurations = GatewayConfigurationCreateInput()
        mutation._args.createDto.configurations.allowHttpTraffic = False
        mutation._args.createDto.configurations.gatewayDefaultTimeOut = 100
        mutation._args.createDto.configurations.limitRequestSize = 154000
        mutation._args.createDto.customMessages = []
        gcmci = GatewayCustomMessageCreateInput()
        gcmci.messageKey = MessageKey.API_MISSING
        gcmci.messageValue = 'Message'
        gcmci2 = GatewayCustomMessageCreateInput()
        gcmci2.messageKey = MessageKey.APP_LIMIT_API_ERROR
        gcmci2.messageValue = 'Message2'
        mutation._args.createDto.customMessages.extend([gcmci, gcmci2])
        mutation._args.createDto.dns = 'myDns'
        mutation._args.createDto.isDefault = False
        mutation._args.createDto.type = GatewayType.Kong

        logger.info(mutation.export_gql_source)

        logger.info('Calling GraphQL Server......')
        response = requests.request('POST', url=RAPIDAPI_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=RAPIDAPI_HEADERS)
        logger.info('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of run_ra_create_gateway_instance_mutation")


def run_ra_edit_user_alert_mutation():
    logger.info('\nRunning Run_ra_edit_user_alert_mutation...')
    try:
        logger.info('Creating mutation python object...')
        from .output.rapidapi.gql_types import editUserAlertInput, Channel, Condition, AlertStatus, time
        from .output.rapidapi.mutations import Mutations

        mutation = Mutations.editUserAlert.value()

        mutation._args.input = editUserAlertInput()
        mutation._args.input.apiIds = [123,32,56,23]
        mutation._args.input.apiVersionsIds = [1,2,3,4]
        mutation._args.input.baseUrl = 'http://shut.betterthisurl'
        mutation._args.input.billingPlansIds = [1,2,3,4]
        mutation._args.input.channel = Channel.Email
        mutation._args.input.condition = Condition.gte
        mutation._args.input.description = 'description 2'
        mutation._args.input.endpointHashes = ['FJWIR23jfjf43j2', 'd3jr4j3j43rf']
        mutation._args.input.endpointsIds = [123,32,56,23]
        mutation._args.input.id = 'sdasd'
        mutation._args.input.minNextAlertTime = 'tomorrow'
        mutation._args.input.name = 'new Name for Tomorrow'
        mutation._args.input.status = AlertStatus.Enabled
        mutation._args.input.threshold = 23.45
        mutation._args.input.throttleInterval = time.hour
        mutation._args.input.throttlePeriod = 1
        mutation._args.input.timeInterval = time.second
        mutation._args.input.timePeriod = 10
        mutation._args.input.typeId = 124

        logger.info('Calling GraphQL Server......')
        response = requests.request('POST', url=RAPIDAPI_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=RAPIDAPI_HEADERS)
        logger.info('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of Run_ra_edit_user_alert_mutation")


def run_ra_admin_audit_logs():
    logger.info('\nRunning test_ra_admin_audit_logs...')
    try:
        # from .output.github.gql_types import UpdateRepositoryInput
        from .output.rapidapi.queries import Queries
        from .output.rapidapi.gql_types import AdminAuditLogSortablesInput, AdminAuditLogSortablesSortingField
        from .output.rapidapi.enums import Order, AdminAuditLogSortables

        logger.info('Creating mutation python object...')
        query = Queries.adminAuditLogs.value()
        logger.info('Inserting python mutation input data...')

        query._args.orderBy = AdminAuditLogSortablesInput()
        field1 = AdminAuditLogSortablesSortingField()
        field1.fieldName = AdminAuditLogSortables.CREATED_AT
        field1.order = Order.ASC
        field2 = AdminAuditLogSortablesSortingField()
        field2.fieldName = AdminAuditLogSortables.CREATED_AT
        field2.order = Order.DESC
        query._args.orderBy.sortingFields = [field1, field2]

        logger.info('Creating GQLOperation for mutation...')
        logger.info(query.export_gql_source)

        response = requests.request('POST', url=RAPIDAPI_URL,
                                    json={ "query": query.export_gql_source },
                                    headers=RAPIDAPI_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of test_ra_admin_audit_logs")
