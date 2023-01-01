
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
from pygqlmap.gqlOperations import GQLMutation
from pygqlmap.gqlTypes import ID
from utils import ManageException

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
    mutation = createDiscussion()
    mutation.name = 'myCreateDiscussion'
##
    
##STEP 3
    from pygqlmap.components import GQLArgsSet
    from pygqlmap.enums import ArgType

    mutation._argsType = ArgType.LiteralValues
    mutation._args.input = CreateDiscussionInput()
    mutation._args.input.repositoryId = 'R_kgDOIOMoaA'
    mutation._args.input.title = 'My Title'
    mutation._args.input.body = 'Some text to give info'
    mutation._args.input.categoryId = 'DIC_kwDOIOMoaM4CR_eD'
    mutation._args.input.clientMutationId = 'Client1'
    
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
        
    print("End of testMutationInsertLiteralValues")
