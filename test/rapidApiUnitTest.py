import os
from pprint import pprint
from pygqlmap.enums import OperationType
from pygqlmap.components import GQLOperation
from pygqlmap.network import GQLResponse
import requests
from codegen.network import fetchSchemaObject
from codegen.generator import CodeGenerator
from codegen.queryPresets import querySchemaAndTypes
from consts import rapidApiHeaders, rapidApiUrl
from utils import ManageException

async def runDownloadCommandRapidApiBySchemaFileRelPath():
    print('\nRunning runDownloadCommandRapidApiBySchemaFileRelPath...')
    command = "CodeGenerator download ./commandsOutput/RapidApi/schema.json -apiArgs ./test/GraphQLClients/RapidApi/downloaderArgs.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runDownloadCommandRapidApiBySchemaFileRelPath")
    
async def runGenerateCommandRapidApiByApiAbsPath():
    print('\nRunning runGenerateCommandRapidApiByApiAbsPath...')
    command = "CodeGenerator generate ./commandsOutput/RapidApi -v -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/RapidApi/generatorArgs.json" #command to be executed
    print("Launching: " + command)
    
    res = os.system(command)
    print("End of runGenerateCommandRapidApiByApiAbsPath")
    
async def fetchRapidApiTestSchemaAndTypes(): 
    print('\nRunning fetchRapidApiTestSchemaAndTypes...')
    
    try:
        gqlSchema = fetchSchemaObject(rapidApiUrl, rapidApiHeaders, querySchemaAndTypes)
        
        if gqlSchema:
            # myCustomTypes = { 'Any': 'any',
            #                   'Upload': 'str',
            #                   'DateTime': 'str'}
            
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='test\\output\\RapidApi\\', logProgress=True)
            print('Python types generated')
    except Exception as ex:
        ManageException('executeQuery FAILED!!' + ex.args[0])
            
    print("End of fetchRapidApiTestSchemaAndTypes")
  
async def fetchRapidApiTestSchemaAndTypesNoDesc(): 
    print('\nRunning fetchRapidApiTestSchemaAndTypesNoDesc...')
    
    try:
        gqlSchema = fetchSchemaObject(rapidApiUrl, rapidApiHeaders, querySchemaAndTypes)
        
        if gqlSchema:
            # myCustomTypes = { 'Any': 'any',
            #                   'Upload': 'str',
            #                   'DateTime': 'str' }
            
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='test\\output\\RapidApiNoDesc\\', addDescription=False, logProgress=True)
            print('Python types generated')
    except Exception as ex:
        ManageException('executeQuery FAILED!!' + ex.args[0])
            
    print("End of fetchRapidApiTestSchemaAndTypesNoDesc")

async def RunRapidApiCreateTransformationsMutation():
    print('\nRunning RunRapidApiCreateTransformationsMutation...')
    try:
        print('Creating mutation python object...')
        from output.RapidApi.gqlTypes import TransformationCreateInput, TransformationActionType, TransformationType, TransformationConditionType
        from output.RapidApi.mutations import Mutations

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
        
        mutation.transformations = [input1, input2]
        
        print('Creating GQLOperation for mutation...')
        myMutation = GQLOperation(OperationType.mutation, inputFieldName='transformations', dataType=mutation, operationName='MyCreateTransformations')
        pprint(myMutation.exportGqlSource)
        
        print('Calling GraphQL Server......')
        response = requests.request('POST', url=rapidApiUrl, 
                                    json= { "query": myMutation.exportGqlSource }, 
                                    headers=rapidApiHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunRapidApiCreateTransformationsMutation")
    
async def RunRapidApiCreateGatewayInstanceMutation():
    print('\nRunning RunRapidApicreateGatewayInstanceMutation...')
    try:
        print('Creating mutation python object...')
        from output.RapidApi.gqlTypes import GatewayInstanceCreateInput, GatewayConfigurationCreateInput, GatewayCustomMessageCreateInput, MessageKey, GatewayType
        from output.RapidApi.mutations import Mutations

        mutation = Mutations.createGatewayInstance.value()
        
        mutation.createDto = GatewayInstanceCreateInput()
        mutation.createDto.apiGatewayCodeTemplateId = 12314
        mutation.createDto.configurations = GatewayConfigurationCreateInput()
        mutation.createDto.configurations.allowHttpTraffic = False
        mutation.createDto.configurations.gatewayDefaultTimeOut = 100
        mutation.createDto.configurations.limitRequestSize = 154000
        mutation.createDto.customMessages = []
        gcmci = GatewayCustomMessageCreateInput()
        gcmci.messageKey = MessageKey.API_MISSING
        gcmci.messageValue = 'Message'
        gcmci2 = GatewayCustomMessageCreateInput()
        gcmci2.messageKey = MessageKey.APP_LIMIT_API_ERROR
        gcmci2.messageValue = 'Message2'
        mutation.createDto.customMessages.append([gcmci, gcmci2])
        mutation.createDto.dns = 'myDns'
        mutation.createDto.isDefault = False
        mutation.createDto.type = GatewayType.Kong
        
        print('Inserting python mutation input data...')
        
        
        print('Creating GQLOperation for mutation...')
        myMutation = GQLOperation(OperationType.mutation, inputFieldName='createDto', dataType=mutation, operationName='MyCreateGatewayInstance')
        pprint(myMutation.exportGqlSource)
        
        print('Calling GraphQL Server......')
        response = requests.request('POST', url=rapidApiUrl, 
                                    json= { "query": myMutation.exportGqlSource }, 
                                    headers=rapidApiHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunRapidApicreateGatewayInstanceMutation")
  
  
async def RunRapidApiEditUserAlertMutation():
    print('\nRunning RunRapidApiEditUserAlertMutation...')
    try:
        print('Creating mutation python object...')
        from output.RapidApi.gqlTypes import editUserAlertInput, Channel, Condition, AlertStatus, time
        from output.RapidApi.mutations import Mutations

        mutation = Mutations.editUserAlert.value()
        
        mutation.input = editUserAlertInput()
        mutation.input.apiIds = [123,32,56,23]
        mutation.input.apiVersionsIds = [1,2,3,4]
        mutation.input.baseUrl = 'http://shutup.bettermyurl'
        mutation.input.billingPlansIds = [1,2,3,4]
        mutation.input.channel = Channel.Email
        mutation.input.condition = Condition.gte
        mutation.input.description = 'description baby'
        mutation.input.endpointHashes = ['FJWIR23jfjf43j2', 'd3jr4j3j43rf']
        mutation.input.endpointsIds = [123,32,56,23]
        mutation.input.id = 'sdasd'
        mutation.input.minNextAlertTime = 'tomorrow'
        mutation.input.name = 'go play soldier'
        mutation.input.status = AlertStatus.Enabled
        mutation.input.threshold = 23.45
        mutation.input.throttleInterval = time.hour
        mutation.input.throttlePeriod = 1
        mutation.input.timeInterval = time.second
        mutation.input.timePeriod = 10
        mutation.input.typeId = 124
        
        print('Inserting python mutation input data...')
        
        
        print('Creating GQLOperation for mutation...')
        myMutation = GQLOperation(OperationType.mutation, dataType=mutation, operationName='MyEditUserAlert')
        pprint(myMutation.exportGqlSource)
        
        print('Calling GraphQL Server......')
        response = requests.request('POST', url=rapidApiUrl, 
                                    json= { "query": myMutation.exportGqlSource }, 
                                    headers=rapidApiHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunRapidApiEditUserAlertMutation")