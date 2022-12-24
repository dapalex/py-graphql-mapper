
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

import requests
from consts import githubUrl, githubHeaders
from output.github.mutations import updateRepository
from test.utils import ManageException

async def testMutationUpdateLiteralValues(): 
    print('\n\nRunning testMutationUpdateLiteralValues...')
##STEP 2
    from pygqlmap.enums import OperationType
    from pygqlmap.components import GQLOperation
    
    mutation = GQLOperation(OperationType.mutation, updateRepository, operationName='myManualUpdateRepository')
##
    
##STEP 3
    from pygqlmap.components import GQLArgsSet
    from pygqlmap.enums import ArgType

    argsMutation = GQLArgsSet()
    argsMutation.addArg("input", { 'repositoryId': "R_kgDOH7MI4g", 'hasIssuesEnabled': False })
    
    argsSetAssUsers = GQLArgsSet("repository.assignableUsers")
    argsSetAssUsers.addArg('first', 1)
    
    mutation.setArgs([argsMutation, argsSetAssUsers], ArgType.LiteralValues)
    try:
        print('Query GQL syntax: ' + mutation.exportGqlSource)
##

##STEP 4
        response = requests.request('POST', url=githubUrl, 
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
        ManageException('executeQuery FAILED - ' + ex.args[0])
        
    print("End of testMutationUpdateLiteralValues")
