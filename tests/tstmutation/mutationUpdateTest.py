
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

"""

##

"""
    STEP 1: Instantiate GQLOperation class representing the GraphQL mutation 
    STEP 2: Instantiate GQLArgs object structure with argument type as LiteralValues
    STEP 3: Query the GraphQL server
    STEP 4: Pass the response received to the GQLResponse constructor
    STEP 5: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: The object within gqlResponse.resultObject will contain the data from the GraphQL server
"""

from pygqlmap.network import httpRequest
from ..consts import githubUrl, githubHeaders
from ..output.github.mutations import updateRepository
from ..output.github.gqlTypes import UpdateRepositoryInput
from ..utils import ManageException

def testMutationUpdateLiteralValues(): 
    print('\n\nRunning testMutationUpdateLiteralValues...')
##STEP 2
    mutation = updateRepository()
    mutation.name = 'myManualUpdateRepository'
##
    
##STEP 3
    from pygqlmap.components import GQLArgsSet
    from pygqlmap.enums import ArgType

    mutationInput = UpdateRepositoryInput()
    mutationInput.repositoryId = "R_kgDOH7MI4g"
    mutationInput.hasIssuesEnabled = False
    mutation._args.input = mutationInput
    
    mutation.type.repository.assignableUsers._args.first = 1
    
    mutation.type.repository.discussion._args.number = 1
    mutation.type.repository.discussionCategory._args.slug = 'slug'
    mutation.type.repository.environment._args.name = 'envName'
    mutation.type.repository.label._args.name = 'lblName'
    mutation.type.repository.milestone._args.number = 2
    mutation.type.repository.packages.edges.node.version._args.version = '1.2.1'
    mutation.type.repository.packages.nodes.version._args.version = '1.1.1'
    mutation.type.repository.project._args.number = 1
    mutation.type.repository.refs._args.refPrefix = 'ref'
    mutation.type.repository.release._args.tagName = 'tagX'
    
    
    
    try:
        print('Query GQL syntax: ' + mutation.exportGqlSource)
##

##STEP 4
        response = httpRequest(url=githubUrl, 
                                    json= { "query": mutation.exportGqlSource }, 
                                    headers=githubHeaders)
##
                
##STEP 5
        from pygqlmap.network import GQLResponse
        
        gqlResponse = GQLResponse(response)
##
        
        gqlResponse.printMessageOutput()
        
##STEP 6
        gqlResponse.mapGQLDataToObj(mutation.type)
##
        
##RESULT
        print('resultObject: ' + str(gqlResponse.resultObject))
##
    except Exception as ex:
        raise ex #ManageException('executeQuery FAILED - ' + ex.args[0])
        
    print("End of testMutationUpdateLiteralValues")
