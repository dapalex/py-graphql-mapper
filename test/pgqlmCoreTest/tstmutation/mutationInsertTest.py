
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
from pygqlmap import GQLObject
from pygqlmap.gqlTypes import ID
from utils import ManageException

class Repository(GQLObject):
    allowUpdateBranch: bool
    autoMergeAllowed: bool ##NON NULL
    
    def __init__(self):
        self.allowUpdateBranch = False
        self.autoMergeAllowed = False
        super().__init__()

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
   
    def __init__(self):
        self.body = ''
        self.bodyHTML = ''
        self.bodyText = ''  
        self.answerChosenAt = ''
        self.createdAt = ''
        self.id = ID()
        self.locked = False
        self.createdViaEmail = False
        self.databaseId = -1
        self.includesCreatedEdit = False
        self.lastEditedAt = ''
        self.number = -1
        self.publishedAt = ''
        self.resourcePath = '' 
        self.title = ''
        self.updatedAt = '' 
        self.url = ''
        self.upvoteCount = -1
        self.viewerCanDelete = False
        self.viewerCanUpvote = False
        self.viewerCanReact = False
        self.viewerCanSubscribe = False
        self.viewerCanUpdate = False
        self.viewerDidAuthor = False
        self.viewerHasUpvoted = False
        self.repository = Repository()
        super().__init__()
        
class CreateTeamDiscussionInput(GQLObject):
    teamId: ID ##NON NULL
    title: str ##NON NULL
    body: str ##NON NULL
    private: bool
    clientMutationId: str

class createDiscussion(GQLObject):
    clientMutationId: str
    discussion: Discussion

    def __init__(self):
        self.clientMutationId = ''
        self.discussion = Discussion() 
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

async def testMutationInsertLiteralValues(): 
    print('\n\nRunning testMutationInsertLiteralValues...')
##STEP 2
    from pygqlmap import GQLOperation
    from pygqlmap.enums import OperationType
    
    mutation = GQLOperation(OperationType.mutation, createDiscussion, operationName='myCreateDiscussion')
##
    
##STEP 3
    from pygqlmap import GQLArgsSet
    from pygqlmap.enums import ArgType

    argsMutation = GQLArgsSet()
    argsMutation.addArg("input", { "repositoryId": 'R_kgDOIOMoaA', "title": 'My Title', 'body': 'Some text to give info', 'categoryId': 'DIC_kwDOIOMoaM4CR_eD', 'clientMutationId': 'Client1' })
    
    mutation.setArgs([argsMutation], ArgType.LiteralValues)
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
        
    print("End of testMutationInsertLiteralValues")
