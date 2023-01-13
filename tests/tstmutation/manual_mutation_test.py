
"""
    USE CASE DESCRIPTION:
    This test shows how to create a GraphQL Mutation using arguments as Literal Values to CREATE a GraphQL record and build the python class instance containing the data from the response

    Mutation to reproduce:

    mutation myCreateDiscussion  {
        createDiscussion(input:  { repositoryId: "R_kgDOH7MI4g", title: "My Title", body: "Some text to give info", categoryId: 1, clientMutationId: "Client1" } ){
            clientMutationId
            discussion   {
                answerChosenAt
                body
                bodyHTML
                bodyText
                createdAt
                createdViaEmail
                databaseId
                id
                includesCreatedEdit
                lastEditedAt
                locked
                number
                publishedAt
                repository   {
                    allowUpdateBranch
                    autoMergeAllowed
                }
                resourcePath
                title
                updatedAt
                upvoteCount
                url
                viewerCanDelete
                viewerCanReact
                viewerCanSubscribe
                viewerCanUpdate
                viewerCanUpvote
                viewerDidAuthor
                viewerHasUpvoted
            }
        }
    }

    STEP 1: Define the python class corresponding to the GraphQL connection type and 'currency' corresponding the the connection node within the query
"""
##STEP 1
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_operations import GQLMutation
from pygqlmap.gql_types import ID
import logging as logger
import requests

class Repository(GQLObject):
    allowUpdateBranch: bool
    autoMergeAllowed: bool ##NON NULL

class Discussion(GQLObject):
    answerChosenAt: str
    body: str ##NON NULL
    bodyHTML: str ##NON NULL
    bodyText: str ##NON NULL
    createdAt: str ##NON NULL
    createdViaEmail: bool ##NON NULL
    databaseId: int
    id: ID ##NON NULL
    includesCreatedEdit: bool ##NON NULL
    lastEditedAt: str
    locked: bool ##NON NULL
    number: int ##NON NULL
    publishedAt: str
    repository: Repository ##NON NULL
    resourcePath: str ##NON NULL
    title: str ##NON NULL
    updatedAt: str ##NON NULL
    upvoteCount: int ##NON NULL
    url: str ##NON NULL
    viewerCanDelete: bool ##NON NULL
    viewerCanReact: bool ##NON NULL
    viewerCanSubscribe: bool ##NON NULL
    viewerCanUpdate: bool ##NON NULL
    viewerCanUpvote: bool ##NON NULL
    viewerDidAuthor: bool ##NON NULL
    viewerHasUpvoted: bool ##NON NULL

class CreateDiscussionInput(GQLObject):
   repositoryId: ID ##NON NULL
   title: str ##NON NULL
   body: str ##NON NULL
   categoryId: ID ##NON NULL
   clientMutationId: str

class CreateDiscussionContent(GQLObject):
    clientMutationId: str
    discussion: Discussion

class createDiscussion(GQLMutation):
   class CreateDiscussionArguments(GQLArgsSet, GQLObject):
      input: CreateDiscussionInput ##NON NULL

   _args: CreateDiscussionArguments

   type: CreateDiscussionContent
##

"""
    STEP 2: Instantiate GQLOperation class representing the GraphQL mutation
    STEP 3: Instantiate GQLArgs object structure with argument type as LITERAL_VALUES
    STEP 4: Query the GraphQL server
    STEP 5: Pass the response received to the GQLResponse constructor
    STEP 6: Call map_gqldata_to_obj() function to obtain the python class with data from GraphQL server

    RESULT: The object within gqlResponse.result_obj will contain the data from the GraphQL server
"""
from ..consts import GITHUB_URL, GITHUB_HEADERS

def run_gh_insert_literal_mutation():
    logger.info('\n\nRunning test_gh_insert_literal_mutation...')
##STEP 2
    mutation = createDiscussion()
    mutation.name = 'myCreateDiscussion'
##

##STEP 3
    from pygqlmap.enums import ArgType

    mutation._args_type = ArgType.LITERAL_VALUES
    mutation._args.input = CreateDiscussionInput()
    mutation._args.input.repositoryId = 'R_kgDOIOMoaA'
    mutation._args.input.title = 'My Title'
    mutation._args.input.body = 'Some text to give info'
    mutation._args.input.categoryId = 'DIC_kwDOIOMoaM4CR_eD'
    mutation._args.input.clientMutationId = 'Client1'

    try:
        logger.info('Query GQL syntax: ' + mutation.export_gql_source)
##

##STEP 4
        response = requests.request('POST', url=GITHUB_URL,
                                     json={ "query": mutation.export_gql_source },
                                    headers=GITHUB_HEADERS)
##

##STEP 5
        from pygqlmap.network import GQLResponse

        gqlResponse = GQLResponse(response)
##

        gqlResponse.print_msg_out()

##STEP 6
        gqlResponse.map_gqldata_to_obj(mutation.type)
##

##RESULT
        logger.info('Result object: ' + str(gqlResponse.result_obj))
##
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED - ' + ex.args[0])

    logger.info("End of test_gh_insert_literal_mutation")
