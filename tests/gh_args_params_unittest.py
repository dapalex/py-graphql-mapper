from datetime import datetime
from pprint import pprint
from pygqlmap.network import GQLResponse
import requests
from codegen.network import fetch_schema_obj
from codegen.generator import CodeGenerator
from codegen.query_presets import QUERY_SCHEMA_AND_TYPES
from .consts import GITHUB_HEADERS, GITHUB_URL
import logging as logger

def run_gh_add_comment_mutation():
    logger.info('\nRunning run_gh_add_comment_mutation... - stack limit for recursion depth')
    try:
        logger.info('Creating mutation python object...')
        from .output.github.mutations import Mutations #, ProjectV2Order, ProjectV2OrderField

        mutation = Mutations.addComment.value()
        # restoreOutput(wrapper)
        logger.info('Inserting python mutation input data...')

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
        logger.info(mutation.export_gql_source)
        # restoreOutput(wrapper)

        logger.info('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL, json={ "query": mutation.export_gql_source }, headers=GITHUB_HEADERS)
        logger.info('Response Received')
        gqlResponse = GQLResponse(response)

       # gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of run_gh_add_comment_mutation")

def run_gh_update_repo_mutation():
    logger.info('\nRunning Run_gh_update_repo_mutation...')
    try:
        from .output.github.mutations import Mutations

        logger.info('Creating mutation python object...')
        mutation = Mutations.updateRepository.value()
        logger.info('Inserting python mutation input data...')

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
        mutation.type.repository.assignableUsers._args.first = 1
        mutation.type.repository.assignableUsers._args.after = ''

        logger.info('Creating GQLOperation for mutation...')
        logger.info(mutation.export_gql_source)

        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        gqlResponse = GQLResponse(response)

       # gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of Run_gh_update_repo_mutation")

def run_gh_create_proj_mutation():
    logger.info('\nRunning Run_gh_create_proj_mutation...')
    try:
        logger.info('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import CreateProjectInput

        mutation = Mutations.createProject.value()
        logger.info('Inserting python mutation input data...')
        mutation.input = CreateProjectInput()

        mutation._args.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
        mutation._args.input.name = "Test create project from Mutation" + datetime.now().ctime()
        mutation._args.input.repositoryIds = ["R_kgDOH7MI4g"]

        mutation.name = 'MycreateProjectMutation'

        mutation.type.project.columns._args.first = 1
        mutation.type.project.columns._args.after = ''
        mutation.type.project.owner.projects._args.first = 1
        mutation.type.project.owner.projects._args.after = ''

        logger.info(mutation.export_gql_source)

        logger.info('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.info('Response Received')
        gqlResponse = GQLResponse(response)
       # gqlResponse.print_msg_out()

        if hasattr(gqlResponse.data, 'createProject') and hasattr(gqlResponse.data['createProject'], 'project'):
            with open('projectsCreated.log', 'a') as logProjCreated:
                logProjCreated.write(gqlResponse.data['createProject']['project']['id'] + '\n')

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of Run_gh_create_proj_mutation")

def run_gh_delete_proj_mutation():
    logger.info('\nRunning Run_gh_delete_proj_mutation...')
    try:

        logger.info('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import DeleteProjectInput

        mutation = Mutations.deleteProject.value()
        logger.info('Inserting python mutation input data...')
        mutation._args.input = DeleteProjectInput()

        mutation._args.input.projectId = "projId"

        logger.info(mutation.export_gql_source)

        logger.info('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.info('Response Received')
        gqlResponse = GQLResponse(response)

       # gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of Run_gh_delete_proj_mutation")

def runGithubCreateProjectV2Mutation():
    logger.info('\nRunning RunGithubCreateProjectV2Mutation...')
    try:
        logger.info('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import CreateProjectV2Input

        mutation = Mutations.createProjectV2.value()
        logger.info('Inserting python mutation input data...')
        mutation.input = CreateProjectV2Input()

        mutation._args.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
        mutation._args.input.title = "Test create issue from Mutation" + datetime.now().ctime()

        logger.info(mutation.export_gql_source)

        logger.info('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.info('Response Received')
        gqlResponse = GQLResponse(response)

       # gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of RunGithubCreateProjectV2Mutation")

def run_gh_delete_proj_v2_mutation():
    logger.info('\nRunning Run_gh_delete_proj_v2_mutation...')
    try:
        logger.info('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import DeleteProjectV2ItemInput

        mutation = Mutations.deleteProjectV2Item.value()
        logger.info('Inserting python mutation input data...')
        mutation._args.input = DeleteProjectV2ItemInput()

        mutation._args.input.projectId = "projId"
        mutation._args.input.itemId = "itemId"

        logger.info(mutation.export_gql_source)

        logger.info('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.info('Response Received')
        gqlResponse = GQLResponse(response)

       # gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of Run_gh_delete_proj_v2_mutation")

def run_gh_create_issue_mutation():
    logger.info('\nRunning Run_gh_create_issue_mutation...')
    try:
        logger.info('Creating mutation python object...')
        from .output.github.mutations import Mutations
        from .output.github.gql_types import CreateIssueInput

        mutation = Mutations.createIssue.value()
        logger.info('Inserting python mutation input data...')
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
        logger.info(mutation.export_gql_source)

        logger.info('Calling GraphQL Server......')
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
        logger.info('Response Received')
        gqlResponse = GQLResponse(response)

       # gqlResponse.print_msg_out()

        gqlResponse.map_gqldata_to_obj(mutation.type)
        logger.info('Result object: ' + str(gqlResponse.result_obj))
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED!! - ' + ex.args[0])

    logger.info("End of Run_gh_create_issue_mutation")
