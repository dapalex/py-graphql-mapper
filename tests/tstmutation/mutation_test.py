
"""
    USE CASE DESCRIPTION:
    This test shows how to create a GraphQL Mutation using arguments as Literal Values to UPDATE a GraphQL record and build the python class instance containing the data from the response

    Mutation to reproduce:

    mutation myManualUpdateRepository  {
        updateRepository ( input: { repositoryId: "R_kgDOH7MI4g", hasIssuesEnabled: false }  )
        {
            clientMutationId
            repository   {
                allowUpdateBranch
                assignableUsers(first: 1)  {
                    edges    {
                        cursor
                        node   {
                            anyPinnableItems
                            avatarUrl
                            bio
                            bioHTML
                        }
                    }
                    totalCount
                    pageInfo   {
                        startCursor
                        endCursor
                        hasNextPage
                        hasPreviousPage
                    }
                }
                autoMergeAllowed
                codeowners   {
                    errors
                    {
                        column
                        kind
                        line
                        message
                        path
                        source
                        suggestion
                    }
                }
            }
        }
    }


    STEP 1: Instantiate GQLOperation class representing the GraphQL mutation
    STEP 2: Instantiate GQLArgs object structure with argument type as LITERAL_VALUES
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call map_gqldata_to_obj() function to obtain the python class with data from GraphQL server

    RESULT: The object within gqlResponse.result_obj will contain the data from the GraphQL server
"""

import requests
from ..consts import GITHUB_URL, GITHUB_HEADERS
from ..output.github.mutations import updateRepository
from ..output.github.gql_types import Package, UpdateRepositoryInput
import logging as logger
from ..utils import stringifyresult

def run_gh_update_mutation_literal():
    logger.debug('\n\nRunning run_gh_update_mutation_literal...')
##STEP 2
    mutation = updateRepository()
    mutation.name = 'myManualUpdateRepository'
##

##STEP 3
    mutationInput = UpdateRepositoryInput()
    mutationInput.repositoryId = "R_kgDOH7MI4g"
    mutationInput.hasIssuesEnabled = False
    mutation._args.input = mutationInput

    mutation.type.repository.assignableUsers._args.first = 5

    mutation.type.repository.branchProtectionRules = type(mutation.type.repository.branchProtectionRules)(number=1, first=1, after='')
    mutation.type.repository.discussion._args.number = 1
    mutation.type.repository.discussionCategory._args.slug = 'slug'
    mutation.type.repository.environment._args.name = 'envName'
    mutation.type.repository.label._args.name = 'lblName'
    mutation.type.repository.milestone._args.number = 2
    package = Package()
    package.version._args.version = '1.1.1'
    mutation.type.repository.packages.nodes = [package]
    mutation.type.repository.project._args.number = 1
    mutation.type.repository.refs._args.refPrefix = 'ref'
    mutation.type.repository.release._args.tagName = 'tagX'

    mutation.type.repository.packages.edges.node.version._args.version = '1'
    mutation.type.repository.deployKeys._args.first = 3
    mutation.type.repository.deployments._args.first = 5


    try:
        logger.debug('Query GQL syntax: ' + mutation.export_gql_source)
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
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
##
    except Exception as ex:
        raise ex

    logger.debug("End of run_gh_update_mutation_literal")
