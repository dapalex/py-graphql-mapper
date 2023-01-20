from pygqlmap.network import GQLResponse
import requests
from codegen.network import fetch_schema_obj
from codegen.generator import CodeGenerator
from codegen.query_presets import QUERY_SCHEMA_AND_TYPES
from .consts import RAPIDAPI_HEADERS, RAPIDAPI_URL
import logging as logger

def run_ra_create_transformations_mutation_args_literal():
    logger.info('\nRunning run_ra_create_transformations_mutation_args_literal...')
    try:
        logger.info('Creating mutation python object...')
        from .output.rapidapi.gql_types import TransformationCreateInput, TransformationActionType, TransformationType, TransformationConditionType
        from .output.rapidapi.mutations import Mutations

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

        mutation = Mutations.createTransformations.value(transformations=[input1, input2])

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
        raise ex

    logger.info("End of run_ra_create_transformations_mutation_args_literal")

def run_ra_create_transformations_mutation_args_vars():
    logger.info('\nRunning run_ra_create_transformations_mutation_args_vars...')
    try:
        logger.info('Creating mutation python object...')
        from .output.rapidapi.gql_types import TransformationCreateInput, TransformationActionType, TransformationType, TransformationConditionType
        from .output.rapidapi.mutations import Mutations

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

        mutation = Mutations.createTransformations.value(transformations=[input1, input2])

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
        raise ex

    logger.info("End of run_ra_create_transformations_mutation_args_vars")

def run_ra_create_gateway_instance_mutation_args_literal():
    logger.info('\nRunning run_ra_create_gateway_instance_mutation_args_literal...')
    try:
        logger.info('Creating mutation python object...')
        from .output.rapidapi.gql_types import GatewayInstanceCreateInput, GatewayConfigurationCreateInput, GatewayCustomMessageCreateInput, MessageKey, GatewayType
        from .output.rapidapi.mutations import Mutations

        mut_cd = GatewayInstanceCreateInput()
        mut_cd.apiGatewayCodeTemplateId = 12314
        mut_cd.dns = 'mydomain.com'
        mut_cd.configurations = GatewayConfigurationCreateInput()
        mut_cd.configurations.allowHttpTraffic = False
        mut_cd.configurations.gatewayDefaultTimeOut = 100
        mut_cd.configurations.limitRequestSize = 154000
        mut_cd.customMessages = []
        gcmci = GatewayCustomMessageCreateInput()
        gcmci.messageKey = MessageKey.API_MISSING
        gcmci.messageValue = 'Message'
        gcmci2 = GatewayCustomMessageCreateInput()
        gcmci2.messageKey = MessageKey.APP_LIMIT_API_ERROR
        gcmci2.messageValue = 'Message2'
        mut_cd.customMessages.extend([gcmci, gcmci2])
        mut_cd.dns = 'myDns'
        mut_cd.isDefault = False
        mut_cd.type = GatewayType.Kong

        mutation = Mutations.createGatewayInstance.value(createDto=mut_cd)

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
        raise ex

    logger.info("End of run_ra_create_gateway_instance_mutation_args_literal")

def run_ra_create_gateway_instance_mutation_args_vars():
    logger.info('\nRunning run_ra_create_gateway_instance_mutation_args_vars...')
    try:
        logger.info('Creating mutation python object...')
        from .output.rapidapi.gql_types import GatewayInstanceCreateInput, GatewayConfigurationCreateInput, GatewayCustomMessageCreateInput, MessageKey, GatewayType
        from .output.rapidapi.mutations import Mutations

        mut_cd = GatewayInstanceCreateInput()
        mut_cd.apiGatewayCodeTemplateId = 12314
        mut_cd.dns = 'mydomain.com'
        mut_cd.configurations = GatewayConfigurationCreateInput()
        mut_cd.configurations.allowHttpTraffic = False
        mut_cd.configurations.gatewayDefaultTimeOut = 100
        mut_cd.configurations.limitRequestSize = 154000
        mut_cd.customMessages = []
        gcmci = GatewayCustomMessageCreateInput()
        gcmci.messageKey = MessageKey.API_MISSING
        gcmci.messageValue = 'Message'
        gcmci2 = GatewayCustomMessageCreateInput()
        gcmci2.messageKey = MessageKey.APP_LIMIT_API_ERROR
        gcmci2.messageValue = 'Message2'
        mut_cd.customMessages.extend([gcmci, gcmci2])
        mut_cd.dns = 'myDns'
        mut_cd.isDefault = False
        mut_cd.type = GatewayType.Kong

        mutation = Mutations.createGatewayInstance.value(createDto=mut_cd)

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
        raise ex

    logger.info("End of run_ra_create_gateway_instance_mutation_args_vars")

def run_ra_edit_user_alert_mutation_args_literal():
    logger.info('\nRunning run_ra_edit_user_alert_mutation_args_literal...')
    try:
        logger.info('Creating mutation python object...')
        from .output.rapidapi.gql_types import editUserAlertInput, Channel, Condition, AlertStatus, time
        from .output.rapidapi.mutations import Mutations

        eua_input = editUserAlertInput()
        eua_input.apiIds = [123,32,56,23]
        eua_input.apiVersionsIds = [1,2,3,4]
        eua_input.baseUrl = 'http://shut.betterthisurl'
        eua_input.billingPlansIds = [1,2,3,4]
        eua_input.channel = Channel.Email
        eua_input.condition = Condition.gte
        eua_input.description = 'description 2'
        eua_input.endpointHashes = ['FJWIR23jfjf43j2', 'd3jr4j3j43rf']
        eua_input.endpointsIds = [123,32,56,23]
        eua_input.id = 'sdasd'
        eua_input.minNextAlertTime = 'tomorrow'
        eua_input.name = 'new Name for Tomorrow'
        eua_input.status = AlertStatus.Enabled
        eua_input.threshold = 23.45
        eua_input.throttleInterval = time.hour
        eua_input.throttlePeriod = 1
        eua_input.timeInterval = time.second
        eua_input.timePeriod = 10
        eua_input.typeId = 124

        mutation = Mutations.editUserAlert.value(input=eua_input)

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
        raise ex

    logger.info("End of run_ra_edit_user_alert_mutation_args_literal")

def run_ra_edit_user_alert_mutation_args_vars():
    logger.info('\nRunning run_ra_edit_user_alert_mutation_args_vars...')
    try:
        logger.info('Creating mutation python object...')
        from .output.rapidapi.gql_types import editUserAlertInput, Channel, Condition, AlertStatus, time
        from .output.rapidapi.mutations import Mutations

        eua_input = editUserAlertInput()
        eua_input.apiIds = [123,32,56,23]
        eua_input.apiVersionsIds = [1,2,3,4]
        eua_input.baseUrl = 'http://shut.betterthisurl'
        eua_input.billingPlansIds = [1,2,3,4]
        eua_input.channel = Channel.Email
        eua_input.condition = Condition.gte
        eua_input.description = 'description 2'
        eua_input.endpointHashes = ['FJWIR23jfjf43j2', 'd3jr4j3j43rf']
        eua_input.endpointsIds = [123,32,56,23]
        eua_input.id = 'sdasd'
        eua_input.minNextAlertTime = 'tomorrow'
        eua_input.name = 'new Name for Tomorrow'
        eua_input.status = AlertStatus.Enabled
        eua_input.threshold = 23.45
        eua_input.throttleInterval = time.hour
        eua_input.throttlePeriod = 1
        eua_input.timeInterval = time.second
        eua_input.timePeriod = 10
        eua_input.typeId = 124

        mutation = Mutations.editUserAlert.value(input=eua_input)

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
        raise ex

    logger.info("End of run_ra_edit_user_alert_mutation_vars")

def run_ra_admin_audit_logs_query_args_literal():
    logger.info('\nRunning run_ra_edit_user_alert_mutation_args_vars...')
    try:
        from .output.rapidapi.queries import Queries
        from .output.rapidapi.gql_types import AdminAuditLogSortablesInput, AdminAuditLogSortablesSortingField
        from .output.rapidapi.enums import Order, AdminAuditLogSortables

        orderby_input = AdminAuditLogSortablesInput()
        field1 = AdminAuditLogSortablesSortingField()
        field1.fieldName = AdminAuditLogSortables.CREATED_AT
        field1.order = Order.ASC
        field2 = AdminAuditLogSortablesSortingField()
        field2.fieldName = AdminAuditLogSortables.CREATED_AT
        field2.order = Order.DESC
        orderby_input.sortingFields = [field1, field2]

        logger.info('Creating mutation python object...')
        query = Queries.adminAuditLogs.value(orderBy=orderby_input)

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
        raise ex

    logger.info("End of run_ra_admin_audit_logs_query_args_literal")

def run_ra_admin_audit_logs_query_args_vars():
    logger.info('\nRunning run_ra_admin_audit_logs_query_args_vars...')
    try:
        from .output.rapidapi.queries import Queries
        from .output.rapidapi.gql_types import AdminAuditLogSortablesInput, AdminAuditLogSortablesSortingField
        from .output.rapidapi.enums import Order, AdminAuditLogSortables

        orderby_input = AdminAuditLogSortablesInput()
        field1 = AdminAuditLogSortablesSortingField()
        field1.fieldName = AdminAuditLogSortables.CREATED_AT
        field1.order = Order.ASC
        field2 = AdminAuditLogSortablesSortingField()
        field2.fieldName = AdminAuditLogSortables.CREATED_AT
        field2.order = Order.DESC
        orderby_input.sortingFields = [field1, field2]

        logger.info('Creating mutation python object...')
        query = Queries.adminAuditLogs.value(orderBy=orderby_input)

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
        raise ex

    logger.info("End of run_ra_admin_audit_logs_query_args_vars")
