import os
from pprint import pprint
from pygqlmap.network import GQLResponse, httpRequest
from codegen.network import fetchSchemaObject
from codegen.generator import CodeGenerator
from codegen.queryPresets import querySchemaAndTypes
from consts import rapidApiHeaders, rapidApiUrl
from utils import ManageException

def runDownloadCommandRapidApiBySchemaFileRelPath():
    print('\nRunning runDownloadCommandRapidApiBySchemaFileRelPath...')
    command = "pygqlcodegen download ./tests/commandsOutput/RapidApi/schema.json -apiArgs ./test/GraphQLClients/RapidApi/downloaderArgs.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runDownloadCommandRapidApiBySchemaFileRelPath")
    
def runGenerateCommandRapidApiByApiAbsPath():
    print('\nRunning runGenerateCommandRapidApiByApiAbsPath...')
    command = "pygqlcodegen generate ./tests/commandsOutput/RapidApi -v -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/RapidApi/generatorArgs.json" #command to be executed
    print("Launching: " + command)
    
    res = os.system(command)
    print("End of runGenerateCommandRapidApiByApiAbsPath")
    
def fetchRapidApiTestSchemaAndTypes(): 
    print('\nRunning fetchRapidApiTestSchemaAndTypes...')
    
    try:
        gqlSchema = fetchSchemaObject(rapidApiUrl, rapidApiHeaders, querySchemaAndTypes)
        
        if gqlSchema:
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='tests\\output\\RapidApi\\', logProgress=True)
            print('Python types generated')
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!!' + ex.args[0])
            
    print("End of fetchRapidApiTestSchemaAndTypes")
  
def fetchRapidApiTestSchemaAndTypesNoDesc(): 
    print('\nRunning fetchRapidApiTestSchemaAndTypesNoDesc...')
    
    try:
        gqlSchema = fetchSchemaObject(rapidApiUrl, rapidApiHeaders, querySchemaAndTypes)
        
        if gqlSchema:
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='tests\\output\\RapidApiNoDesc\\', addDescription=False, logProgress=True)
            print('Python types generated')
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!!' + ex.args[0])
            
    print("End of fetchRapidApiTestSchemaAndTypesNoDesc")

def RunRapidApiCreateTransformationsMutation():
    print('\nRunning RunRapidApiCreateTransformationsMutation...')
    try:
        print('Creating mutation python object...')
        from .output.RapidApi.gqlTypes import TransformationCreateInput, TransformationActionType, TransformationType, TransformationConditionType
        from .output.RapidApi.mutations import Mutations

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
        
        print('Inserting python mutation input data...')
        
        mutation._args.transformations = [input1, input2]
        
        pprint(mutation.exportGqlSource)
        
        print('Calling GraphQL Server......')
        response = httpRequest(url=rapidApiUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=rapidApiHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        
        gqlResponse.mapGQLDataToObj(mutation.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunRapidApiCreateTransformationsMutation")
    
def RunRapidApiCreateGatewayInstanceMutation():
    print('\nRunning RunRapidApicreateGatewayInstanceMutation...')
    try:
        print('Creating mutation python object...')
        from .output.RapidApi.gqlTypes import GatewayInstanceCreateInput, GatewayConfigurationCreateInput, GatewayCustomMessageCreateInput, MessageKey, GatewayType
        from .output.RapidApi.mutations import Mutations

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
        
        pprint(mutation.exportGqlSource)
        
        print('Calling GraphQL Server......')
        response = httpRequest(url=rapidApiUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=rapidApiHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        
        gqlResponse.mapGQLDataToObj(mutation.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunRapidApicreateGatewayInstanceMutation")
  
  
def RunRapidApiEditUserAlertMutation():
    print('\nRunning RunRapidApiEditUserAlertMutation...')
    try:
        print('Creating mutation python object...')
        from .output.RapidApi.gqlTypes import editUserAlertInput, Channel, Condition, AlertStatus, time
        from .output.RapidApi.mutations import Mutations

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
        
        print('Calling GraphQL Server......')
        response = httpRequest(url=rapidApiUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=rapidApiHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        
        gqlResponse.mapGQLDataToObj(mutation.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunRapidApiEditUserAlertMutation")
    

def testAdminAuditLogs():
    print('\nRunning testAdminAuditLogs...')
    try:
        # from .output.github.gqlTypes import UpdateRepositoryInput
        from .output.RapidApi.queries import Queries
        from .output.RapidApi.gqlTypes import AdminAuditLogSortablesInput, AdminAuditLogSortablesSortingField  
        from .output.RapidApi.enums import Order, AdminAuditLogSortables 
        
        print('Creating mutation python object...')
        query = Queries.adminAuditLogs.value()
        print('Inserting python mutation input data...')
        
        query._args.orderBy = AdminAuditLogSortablesInput()
        field1 = AdminAuditLogSortablesSortingField()
        field1.fieldName = AdminAuditLogSortables.CREATED_AT
        field1.order = Order.ASC
        field2 = AdminAuditLogSortablesSortingField()
        field2.fieldName = AdminAuditLogSortables.CREATED_AT
        field2.order = Order.DESC
        query._args.orderBy.sortingFields = [field1, field2]
        
        print('Creating GQLOperation for mutation...')
        # myMutation = GQLOperation(OperationType.mutation, dataType=mutation, operationName='MyUpdateRepositoryMutation')
        pprint(query.exportGqlSource)
            
        response = httpRequest(url=rapidApiUrl, 
                                    json= { "query": query.exportGqlSource }, 
                                    headers=rapidApiHeaders) 
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        
        gqlResponse.mapGQLDataToObj(query.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testAdminAuditLogs")
