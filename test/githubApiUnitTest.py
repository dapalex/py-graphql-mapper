from datetime import datetime
import os
from pprint import pprint
import requests

from consts import githubHeaders, githubUrl
from pygqlmap.network import GQLResponse
from codegen.network import fetchSchemaObject
from codegen.generator import CodeGenerator
from codegen.queryPresets import querySchemaAndTypes
from utils import ManageException, redirectOutputToFile, restoreOutput

async def runDownloadCommandGithubBySchemaFileRelPath():
    print('\nRunning runDownloadCommandGithubBySchemaFileRelPath...')
    command = "CodeGenerator download ./commandsOutput/Github/schema.json -apiArgs ./test/GraphQLClients/GithubApi/downloaderArgs.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runDownloadCommandGithubBySchemaFileRelPath")
    
async def runGenerateCommandGithubByApiAbsPath():
    print('\nRunning runGenerateCommandGithubByApiAbsPath...')
    command = "CodeGenerator generate ./commandsOutput/Github -v -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/GithubApi/generatorArgs.json" #command to be executed
    print("Launching: " + command)
    
    res = os.system(command)
    print("End of runGenerateCommandGithubByApiAbsPath")
    
async def fetchGithubMutationTypes(): 
    print('\nRunning fetchGithubMutationTypes...')
    
    try:
        print('Calling GraphQL Server...')
        gqlSchema = fetchSchemaObject(githubUrl, githubHeaders, querySchemaAndTypes)
        print('Response Received')
        
        if gqlSchema:
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='test\\output\\github\\', logProgress=True, addDescription=True)

            print('Python types generated')
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of fetchGithubMutationTypes")

async def fetchGithubMutationTypesFromSchemaNoDesc(): 
    print('\nRunning fetchGithubMutationTypesNoDesc...')
    
    try:
        print('Calling GraphQL Server...')
        gqlSchema = fetchSchemaObject(githubUrl, githubHeaders, querySchemaAndTypes)
        print('Response Received')
        
        if gqlSchema:
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='test\\output\\githubNoDesc\\', logProgress=True, addDescription=False)

            print('Python types generated')
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of fetchGithubMutationTypesNoDesc")

async def RunGithubAddCommentMutation():
    print('\nRunning RunGithubAddCommentMutation... - stack limit for recursion depth')
    try:
        print('Creating mutation python object...')
        from output.github.mutations import Mutations

        mutation = Mutations.addComment.value()
        # restoreOutput(wrapper)
        print('Inserting python mutation input data...')
        
        mutation._args.input.subjectId = 'something'
        mutation._args.input.body = 'This is the body'
        mutation._args.input.clientMutationId = 'Me'
        print('Creating GQLOperation for mutation...')
        
        # wrapper = redirectOutputToFile('mutationCreated.log')
        print(mutation.exportGqlSource)
        # restoreOutput(wrapper)
        
        print('Calling GraphQL Server......')
        response = requests.request('POST', url=githubUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=githubHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunGithubAddCommentMutation")
    
async def RunGithubUpdateRepositoryMutation():
    print('\nRunning RunGithubUpdateRepositoryMutation...')
    try:
        # from output.github.gqlTypes import UpdateRepositoryInput
        from output.github.mutations import Mutations
        
        print('Creating mutation python object...')
        mutation = Mutations.updateRepository.value()
        print('Inserting python mutation input data...')
        
        mutation._args.input.repositoryId = "R_kgDOH7MI4g"
        mutation._args.input.hasIssuesEnabled = True
        mutation._args.input.hasWikiEnabled = True
        
        print('Creating GQLOperation for mutation...')
        # myMutation = GQLOperation(OperationType.mutation, dataType=mutation, operationName='MyUpdateRepositoryMutation')
        pprint(mutation.exportGqlSource)
            
        response = requests.request('POST', url=githubUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=githubHeaders) 
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunGithubUpdateRepositoryMutation")

async def RunGithubCreateProjectMutation():
    print('\nRunning RunGithubCreateProjectMutation...')
    try:
        print('Creating mutation python object...')
        from output.github.mutations import Mutations
        from output.github.gqlTypes import CreateProjectInput

        mutation = Mutations.createProject.value()
        print('Inserting python mutation input data...')
        mutation.input = CreateProjectInput()
        
        mutation._args.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
        mutation._args.input.name = "Test create project from Mutation" + datetime.now().ctime()
        mutation._args.input.repositoryIds = ["R_kgDOH7MI4g"]
        
        mutation._args._customPayload = '{ project { id } }'
        mutation.name = 'MycreateProjectMutation'
        
        pprint(mutation.exportGqlSource)
        
        print('Calling GraphQL Server......')
        response = requests.request('POST', url=githubUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=githubHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        gqlResponse.printMessageOutput()
        
        if hasattr(gqlResponse.data, 'createProject') and hasattr(gqlResponse.data['createProject'], 'project'):
            with open('projectsCreated.log', 'a') as logProjCreated:
                logProjCreated.write(gqlResponse.data['createProject']['project']['id'] + '\n')
                
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunGithubCreateProjectMutation")
    
async def RunGithubDeleteProjectMutation():
    print('\nRunning RunGithubDeleteProjectMutation...')
    try:
        
        # with open('projectsCreated.log', 'a') as logProjCreated:
        #     logProjCreated.write(gqlResponse.data['createProject']['project']['id'] + '\n')
            
        print('Creating mutation python object...')
        from output.github.mutations import Mutations
        from output.github.gqlTypes import DeleteProjectInput

        mutation = Mutations.deleteProject.value()
        print('Inserting python mutation input data...')
        mutation._args.input = DeleteProjectInput()
        
        mutation._args.input.projectId = "projId"
                
        pprint(mutation.exportGqlSource)
        
        print('Calling GraphQL Server......')
        response = requests.request('POST', url=githubUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=githubHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
    
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunGithubDeleteProjectMutation")
    
async def RunGithubCreateProjectV2Mutation():
    print('\nRunning RunGithubCreateProjectV2Mutation...')
    try:
        print('Creating mutation python object...')
        from output.github.mutations import Mutations
        from output.github.gqlTypes import CreateProjectV2Input

        mutation = Mutations.createProjectV2.value()
        print('Inserting python mutation input data...')
        mutation.input = CreateProjectV2Input()
        
        mutation._args.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
        mutation._args.input.title = "Test create issue from Mutation" + datetime.now().ctime()
        
        pprint(mutation.exportGqlSource)
        
        print('Calling GraphQL Server......')
        response = requests.request('POST', url=githubUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=githubHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunGithubCreateProjectV2Mutation")
    
async def RunGithubDeleteProjectV2Mutation():
    print('\nRunning RunGithubDeleteProjectV2Mutation...')
    try:
        print('Creating mutation python object...')
        from output.github.mutations import Mutations
        from output.github.gqlTypes import DeleteProjectV2ItemInput

        mutation = Mutations.deleteProjectV2Item.value()
        print('Inserting python mutation input data...')
        mutation._args.input = DeleteProjectV2ItemInput()
        
        mutation._args.input.projectId = "projId"
        mutation._args.input.itemId = "itemId"
        
        pprint(mutation.exportGqlSource)
        
        print('Calling GraphQL Server......')
        response = requests.request('POST', url=githubUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=githubHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
        
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunGithubDeleteProjectV2Mutation")
    
async def RunGithubCreateIssueMutation():
    print('\nRunning RunGithubCreateIssueMutation...')
    try:
        print('Creating mutation python object...')
        from output.github.mutations import Mutations
        from output.github.gqlTypes import CreateIssueInput

        mutation = Mutations.createIssue.value()
        print('Inserting python mutation input data...')
        mutation.input = CreateIssueInput()
        
        mutation._args.input.repositoryId = "R_kgDOH7MI4g"
        mutation._args.input.title = "Test create issue from Mutation" + datetime.now().ctime()
        mutation._args.input.assigneeIds = ["MDQ6VXNlcjkxMzk2ODM3"]
        mutation._args.input.labelIds = ['LA_kwDOIOMoaM8AAAABFmBXvg', 'LA_kwDOIOMoaM8AAAABFmBXvQ']
        mutation._args.input.projectIds = ['PRO_kwHOBXKa5c4A32ah']
        
        pprint(mutation.exportGqlSource)
        
        print('Calling GraphQL Server......')
        response = requests.request('POST', url=githubUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=githubHeaders) 
        print('Response Received')
        gqlResponse = GQLResponse(response)
        
        gqlResponse.printMessageOutput()
    
    except Exception as ex:
        ManageException('executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of RunGithubCreateIssueMutation")
    