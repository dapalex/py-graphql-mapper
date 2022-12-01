
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


    STEP 1: Define the python class corresponding to the GraphQL connection type and 'currency' corresponding the the connection node within the query 
"""
##STEP 1
from pygqlmap import GQLConnection, GQLEdges, GQLObject
from utils import ManageException

class User(GQLObject):
    anyPinnableItems: bool ##NON NULL
    avatarUrl: str ##NON NULL
    bio: str
    bioHTML: str ##NON NULL

    def __init__(self):
        self.avatarUrl = ''
        self.anyPinnableItems = False 
        self.bioHTML = ''  
        self.bio = '' 
        super().__init__()
        
class PageInfo(GQLObject):
    endCursor: str
    hasNextPage: bool ##NON NULL
    hasPreviousPage: bool ##NON NULL
    startCursor: str
   
    def __init__(self):
        self.endCursor = ''
        self.hasNextPage = False 
        self.hasPreviousPage = False 
        self.startCursor = '' 
        super().__init__()

class UserConnection(GQLConnection):
  
    def __init__(self):
        super().__init__(GQLEdges(User())) 
        

class RepositoryCodeownersError(GQLObject):
    column: int ##NON NULL
    kind: str ##NON NULL
    line: int ##NON NULL
    message: str ##NON NULL
    path: str ##NON NULL
    source: str ##NON NULL
    suggestion: str
   
    def __init__(self):
        self.kind = ''
        self.column = -1 
        self.message = ''
        self.line = -1 
        self.path = ''
        self.suggestion = ''
        self.source = ''
        super().__init__()
        
class RepositoryCodeowners(GQLObject):
    errors: RepositoryCodeownersError
    
    def __init__(self):
        self.errors = RepositoryCodeownersError()
        super().__init__()
    
class Repository(GQLObject):
    allowUpdateBranch: bool
    assignableUsers: UserConnection ##NON NULL
    autoMergeAllowed: bool ##NON NULL
    codeowners: RepositoryCodeowners
    
    def __init__(self):
        self.allowUpdateBranch = False
        self.assignableUsers = UserConnection()
        self.autoMergeAllowed = False
        self.codeowners = RepositoryCodeowners()
        super().__init__()
        

class updateRepository(GQLObject):
    clientMutationId: str
    repository: Repository
    
    def __init__(self):
        self.clientMutationId = ''
        self.repository = Repository()
        super().__init__()

##

"""
    STEP 2: Instantiate GQLOperation class representing the GraphQL mutation 
    STEP 3: Instantiate GQLArgs object structure with argument type as LiteralValues
    STEP 4: Query the GraphQL server
    STEP 5: Pass the response received to the GQLResponse constructor
    STEP 6: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: The object within gqlResponse.resultObject will contain the data from the GraphQL server
"""

import requests
from consts import githubUrl, githubHeaders

async def testMutationUpdateLiteralValues(): 
    print('\n\nRunning testMutationUpdateLiteralValues...')
##STEP 2
    from pygqlmap import GQLOperation
    from pygqlmap.enums import OperationType
    
    mutation = GQLOperation(OperationType.mutation, updateRepository, operationName='myManualUpdateRepository')
##
    
##STEP 3
    from pygqlmap import GQLArgsSet
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
        gqlResponse.mapGQLDataToObj(mutation.obj)
##
        
##RESULT
        print('resultObject: ' + str(gqlResponse.resultObject))
##
    except Exception as ex:
        ManageException('executeQuery FAILED - ' + ex.args[0])
        
    print("End of testMutationUpdateLiteralValues")
