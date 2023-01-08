from datetime import datetime
from pprint import pprint
from pygqlmap.network import GQLResponse, httpRequest
from codegen.network import fetchSchemaObject
from codegen.generator import CodeGenerator
from codegen.queryPresets import querySchemaAndTypes
from .consts import githubHeaders, githubUrl
# from .utils import ManageException

def fetchGithubMutationTypes():
    print('\nRunning fetchGithubMutationTypes...')

    try:
        print('Calling GraphQL Server...')
        gqlSchema = fetchSchemaObject(githubUrl, githubHeaders, querySchemaAndTypes)
        print('Response Received')

        if gqlSchema:
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='tests\\output\\github\\', logProgress=True, addDescription=True)

            print('Python types generated')
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    print("End of fetchGithubMutationTypes")

def fetchGithubMutationTypesFromSchemaNoDesc():
    print('\nRunning fetchGithubMutationTypesNoDesc...')

    try:
        print('Calling GraphQL Server...')
        gqlSchema = fetchSchemaObject(githubUrl, githubHeaders, querySchemaAndTypes)
        print('Response Received')

        if gqlSchema:
            print('Generating python types from GraphQL data...')
            CodeGenerator.generateCode(gqlSchema, folder='tests\\output\\githubNoDesc\\', logProgress=True, addDescription=False)

            print('Python types generated')
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    print("End of fetchGithubMutationTypesNoDesc")

def runGithubAddCommentMutation():
    print('\nRunning RunGithubAddCommentMutation... - stack limit for recursion depth')
    try:
        print('Creating mutation python object...')
        from .output.github.mutations import Mutations #, ProjectV2Order, ProjectV2OrderField

        mutation = Mutations.addComment.value()
        # restoreOutput(wrapper)
        print('Inserting python mutation input data...')

        mutation._args.input.subjectId = 'something'
        mutation._args.input.body = 'This is the body'
        mutation._args.input.clientMutationId = 'Me'
        mutation.type.commentEdge.node.repository.discussion._args.number = 3
        mutation.type.commentEdge.node.repository.discussionCategory._args.slug = 'slug'
        mutation.type.commentEdge.node.repository.environment._args.name = 'envName'
        mutation.type.commentEdge.node.repository.refs._args.refPrefix = 'pref'
        mutation.type.commentEdge.node.repository.release._args.tagName = 'aTag'
        mutation.type.commentEdge.node.repository.label._args.name = 'aName'
        mutation.type.commentEdge.node.repository.milestone._args.number = 0
        mutation.type.commentEdge.node.repository.packages._args.repositoryId = 'ghjk'
        mutation.type.commentEdge.node.repository.packages.nodes.version._args.version = '2'
        mutation.type.commentEdge.node.repository.packages.edges.node.version._args.version = '2.6'
        mutation.type.commentEdge.node.repository.project._args.number = 1

        # wrapper = redirectOutputToFile('mutationCreated.log')
        print(mutation.exportGqlSource)
        # restoreOutput(wrapper)

        print('Calling GraphQL Server......')
        response = httpRequest(githubUrl, { "query": mutation.exportGqlSource }, githubHeaders)
        print('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()

        gqlResponse.mapGQLDataToObj(mutation.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    print("End of RunGithubAddCommentMutation")

def runGithubUpdateRepositoryMutation():
    print('\nRunning RunGithubUpdateRepositoryMutation...')
    try:
        from .output.github.mutations import Mutations

        print('Creating mutation python object...')
        mutation = Mutations.updateRepository.value()
        print('Inserting python mutation input data...')

        mutation._args.input.repositoryId = "R_kgDOH7MI4g"
        mutation._args.input.hasIssuesEnabled = True
        mutation._args.input.hasWikiEnabled = True
        'mutation', 'updateRepository', 'repository', 'discussion'
        mutation.type.repository.discussion._args.number = 1
        mutation.type.repository.discussionCategory._args.slug = "1"
        mutation.type.repository.environment._args.name = "nm"
        mutation.type.repository.label._args.name = "nmLbl"
        mutation.type.repository.milestone._args.number = 2
        mutation.type.repository.packages.edges.node.version._args.version = "v3"
        mutation.type.repository.packages.nodes.version._args.version = "v13"
        mutation.type.repository.project._args.number = 4
        mutation.type.repository.refs._args.refPrefix = 'pref'
        mutation.type.repository.release._args.tagName = 'tagE'
        mutation.type.repository.branchProtectionRules._args.first = 1
        mutation.type.repository.branchProtectionRules._args.after = ''

        print('Creating GQLOperation for mutation...')
        pprint(mutation.exportGqlSource)

        response = httpRequest(githubUrl,
                                     { "query": mutation.exportGqlSource },
                                    githubHeaders)
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()

        gqlResponse.mapGQLDataToObj(mutation.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    print("End of RunGithubUpdateRepositoryMutation")

def runGithubCreateProjectMutation():
    print('\nRunning RunGithubCreateProjectMutation...')
    try:
        print('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gqlTypes import CreateProjectInput

        mutation = Mutations.createProject.value()
        print('Inserting python mutation input data...')
        mutation.input = CreateProjectInput()

        mutation._args.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
        mutation._args.input.name = "Test create project from Mutation" + datetime.now().ctime()
        mutation._args.input.repositoryIds = ["R_kgDOH7MI4g"]

        mutation.name = 'MycreateProjectMutation'

        mutation.type.project.columns._args.first = 1
        mutation.type.project.columns._args.after = ''
        mutation.type.project.owner.projects._args.first = 1
        mutation.type.project.owner.projects._args.after = ''

        pprint(mutation.exportGqlSource)

        print('Calling GraphQL Server......')
        response = httpRequest(githubUrl,
                                     { "query": mutation.exportGqlSource },
                                    githubHeaders)
        print('Response Received')
        gqlResponse = GQLResponse(response)
        gqlResponse.printMessageOutput()

        if hasattr(gqlResponse.data, 'createProject') and hasattr(gqlResponse.data['createProject'], 'project'):
            with open('projectsCreated.log', 'a') as logProjCreated:
                logProjCreated.write(gqlResponse.data['createProject']['project']['id'] + '\n')

        gqlResponse.mapGQLDataToObj(mutation.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    print("End of RunGithubCreateProjectMutation")

def runGithubDeleteProjectMutation():
    print('\nRunning RunGithubDeleteProjectMutation...')
    try:

        print('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gqlTypes import DeleteProjectInput

        mutation = Mutations.deleteProject.value()
        print('Inserting python mutation input data...')
        mutation._args.input = DeleteProjectInput()

        mutation._args.input.projectId = "projId"

        pprint(mutation.exportGqlSource)

        print('Calling GraphQL Server......')
        response = httpRequest(githubUrl,
                                     { "query": mutation.exportGqlSource },
                                    githubHeaders)
        print('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()

        gqlResponse.mapGQLDataToObj(mutation.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    print("End of RunGithubDeleteProjectMutation")

def runGithubCreateProjectV2Mutation():
    print('\nRunning RunGithubCreateProjectV2Mutation...')
    try:
        print('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gqlTypes import CreateProjectV2Input

        mutation = Mutations.createProjectV2.value()
        print('Inserting python mutation input data...')
        mutation.input = CreateProjectV2Input()

        mutation._args.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
        mutation._args.input.title = "Test create issue from Mutation" + datetime.now().ctime()

        pprint(mutation.exportGqlSource)

        print('Calling GraphQL Server......')
        response = httpRequest(githubUrl,
                                     { "query": mutation.exportGqlSource },
                                    githubHeaders)
        print('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()

        gqlResponse.mapGQLDataToObj(mutation.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    print("End of RunGithubCreateProjectV2Mutation")

def runGithubDeleteProjectV2Mutation():
    print('\nRunning RunGithubDeleteProjectV2Mutation...')
    try:
        print('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gqlTypes import DeleteProjectV2ItemInput

        mutation = Mutations.deleteProjectV2Item.value()
        print('Inserting python mutation input data...')
        mutation._args.input = DeleteProjectV2ItemInput()

        mutation._args.input.projectId = "projId"
        mutation._args.input.itemId = "itemId"

        pprint(mutation.exportGqlSource)

        print('Calling GraphQL Server......')
        response = httpRequest(githubUrl,
                                     { "query": mutation.exportGqlSource },
                                    githubHeaders)
        print('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()

        gqlResponse.mapGQLDataToObj(mutation.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    print("End of RunGithubDeleteProjectV2Mutation")

def runGithubCreateIssueMutation():
    print('\nRunning RunGithubCreateIssueMutation...')
    try:
        print('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gqlTypes import CreateIssueInput

        mutation = Mutations.createIssue.value()
        print('Inserting python mutation input data...')
        mutation.input = CreateIssueInput()

        mutation._args.input.repositoryId = "R_kgDOH7MI4g"
        mutation._args.input.title = "Test create issue from Mutation" + datetime.now().ctime()
        mutation._args.input.assigneeIds = ["MDQ6VXNlcjkxMzk2ODM3"]
        mutation._args.input.labelIds = ['LA_kwDOIOMoaM8AAAABFmBXvg', 'LA_kwDOIOMoaM8AAAABFmBXvQ']
        mutation._args.input.projectIds = ['PRO_kwHOBXKa5c4A32ah']

        mutation.type.issue.repository.discussion._args.number = 1
        mutation.type.issue.repository.discussionCategory._args.slug = "1"
        mutation.type.issue.repository.environment._args.name = "nm"
        mutation.type.issue.repository.label._args.name = "nmLbl"
        mutation.type.issue.repository.milestone._args.number = 2
        mutation.type.issue.repository.packages.edges.node.version._args.version = "v3"
        mutation.type.issue.repository.packages.nodes.version._args.version = "v13"
        mutation.type.issue.repository.project._args.number = 4
        mutation.type.issue.repository.refs._args.refPrefix = 'pref'
        mutation.type.issue.repository.release._args.tagName = 'tagE'


        mutation.type.issue.comments.edges.node.repository.discussion._args.number = 3
        mutation.type.issue.comments.edges.node.repository.discussionCategory._args.slug = 'slug'
        mutation.type.issue.comments.edges.node.repository.environment._args.name = 'envName'
        mutation.type.issue.comments.edges.node.repository.refs._args.refPrefix = 'pref'
        mutation.type.issue.comments.edges.node.repository.release._args.tagName = 'aTag'
        mutation.type.issue.comments.edges.node.repository.label._args.name = 'aName'
        mutation.type.issue.comments.edges.node.repository.milestone._args.number = 0
        mutation.type.issue.comments.edges.node.repository.packages._args.repositoryId = 'ghjk'
        mutation.type.issue.comments.edges.node.repository.packages.nodes.version._args.version = '2'
        mutation.type.issue.comments.edges.node.repository.packages.edges.node.version._args.version = '2.6'
        mutation.type.issue.comments.edges.node.repository.project._args.number = 1

        mutation.type.issue.comments.nodes.repository.discussion._args.number = 3
        mutation.type.issue.comments.nodes.repository.discussionCategory._args.slug = 'slug'
        mutation.type.issue.comments.nodes.repository.environment._args.name = 'envName'
        mutation.type.issue.comments.nodes.repository.refs._args.refPrefix = 'pref'
        mutation.type.issue.comments.nodes.repository.release._args.tagName = 'aTag'
        mutation.type.issue.comments.nodes.repository.label._args.name = 'aName'
        mutation.type.issue.comments.nodes.repository.milestone._args.number = 0
        mutation.type.issue.comments.nodes.repository.packages._args.repositoryId = 'ghjk'
        mutation.type.issue.comments.nodes.repository.packages.nodes.version._args.version = '2'
        mutation.type.issue.comments.nodes.repository.packages.edges.node.version._args.version = '2.6'
        mutation.type.issue.comments.nodes.repository.project._args.number = 1
        pprint(mutation.exportGqlSource)

        print('Calling GraphQL Server......')
        response = httpRequest(githubUrl,
                                     { "query": mutation.exportGqlSource },
                                    githubHeaders)
        print('Response Received')
        gqlResponse = GQLResponse(response)

        gqlResponse.printMessageOutput()

        gqlResponse.mapGQLDataToObj(mutation.type)
        print('resultObject: ' + str(gqlResponse.resultObject))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    print("End of RunGithubCreateIssueMutation")
