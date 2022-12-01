
""" 
    USE CASE DESCRIPTION: 
    This test shows how to create a GraphQL Query to fetch a GraphQL complex type (made of objects, connections, and scalar fields) combining arguments usage as literal values
    with visibility usage for chosen fields, and finally build the python class instance containing the data from the response
    
    Query to reproduce:
    
    query myCountriesQuery  { 
        countries { 
            edges { 
                cursor     
                node { 
                    code     
                    callingCode     
                    wikiDataId     
                    capital     
                    name     
                    currencyCodes       
                    flagImageUri     
                    numRegions     
                    region { 
                        fipsCode     
                        isoCode     
                        wikiDataId     
                        name     
                        capital     
                        country { 
                            code     
                            callingCode         (*)
                            wikiDataId     
                            capital     
                            name     
                            currencyCodes       (*)
                            flagImageUri     
                            numRegions  
                        }        
                        populatedPlaces { 
                            totalCount  
                        } 
                    }    
                    regions { 
                        edges { 
                            cursor  
                        }     
                        totalCount     
                        pageInfo { 
                            startCursor     
                            endCursor     
                            hasNextPage    (*) 
                            hasPreviousPage  
                        } 
                    } 
                } 
            }     
            totalCount     
            pageInfo { 
                startCursor     
                endCursor     
                hasNextPage      (*)
                hasPreviousPage  
            } 
        } 
    }


    STEP 1: Define the python classes corresponding to the GraphQL type within the query 
"""
##STEP 1
from pygqlmap import GQLConnection, GQLEdges, GQLObject
from pygqlmap.gqlTypes import ID
from utils import ManageException

class countries(GQLConnection):
    
    def __init__(self):
        super().__init__(GQLEdges(countryNode())) 
    
class countryRegions(GQLConnection):
    
    def __init__(self):
        super().__init__(GQLEdges()) 
    
class countryRegion(GQLObject):
    fipsCode: str
    isoCode: str
    wikiDataId: str
    name: str
    capital: str
    country: 'country'
    populatedPlaces: 'populatedPlaces'
    
    def __init__(self):
        self.fipsCode = ''
        self.isoCode = ''
        self.wikiDataId = ''
        self.name = ''
        self.capital = ''
        self.country = country()
        self.populatedPlaces = populatedPlaces()
        super().__init__()  
       
class countryNode(GQLObject):
    code: ID ##ID non-null
    callingCode: str ##non-null
    wikiDataId: ID ##ID non-null
    capital: str
    name: str ##non-null
    currencyCodes: list ##of str
    flagImageUri: str ##non-null
    numRegions: int ##non-null
    region: countryRegion
    regions: countryRegions
     
    def __init__(self):
        self.code = ''
        self.callingCode = ''
        self.wikiDataId = ''
        self.name = ''
        self.currencyCodes = []
        self.flagImageUri = ''
        self.numRegions = -1
        self.capital = ''
        self.region = countryRegion()
        self.regions = countryRegions()
        super().__init__() 

class populatedPlaces(GQLObject):
    totalCount: int
    
    def __init__(self):
        self.totalCount = 0
        super().__init__()  
         
class country(GQLObject):
    code: ID ##ID non-null
    callingCode: str ##non-null
    wikiDataId: ID ##ID non-null
    capital: str
    name: str ##non-null
    currencyCodes: list ##of str
    flagImageUri: str ##non-null
    numRegions: int ##non-null
    
    def __init__(self):
        self.code = ''
        self.callingCode = ''
        self.wikiDataId = ''
        self.name = ''
        self.currencyCodes = []
        self.flagImageUri = ''
        self.numRegions = -1
        self.capital = ''
        super().__init__()
    
##

"""
    STEP 2: Instantiate GQLOperation class representing the GraphQL query 
    STEP 3: Instantiate GQLArgs object structure with argument type as LiteralValues
    STEP 2: Call setShow function of GQLOperation class to set the visibility of chosen fields (path to declare with dot notation)
    STEP 5: Query the GraphQL server
    STEP 6: Pass the response received to the GQLResponse constructor
    STEP 7: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: 
        a) The request toward the GraphQL server will not have the hidden fields
        b) The request toward the GraphQL server will have the query with arguments 'currencyCode' and 'code' 
        b) The python class instance obtained from the response will not have the hidden fields
"""

import requests
from consts import gdbcHeaders, gdbcUrl
from pygqlmap import GQLArgsSet
from pygqlmap.enums import ArgType

async def testComplexObject(): 
    print('\n\nRunning testComplexObject...')
##STEP 2
    from pygqlmap import GQLOperation
    from pygqlmap.enums import OperationType
    
    query = GQLOperation(OperationType.query, countries, operationName='myCountriesQuery') 
##
    
##STEP 3
    argsCntrs = GQLArgsSet(location='countries')
    argsCntrs.addArg('currencyCode', 'USD')
    argsRegion = GQLArgsSet('countries.edges.node.region')
    argsRegion.addArg('code', "AK")
    query.setArgs([argsCntrs, argsRegion], ArgType.LiteralValues)
##

##STEP 4
    query.setShow('countries.edges.node.region.country.callingCode', False)
    query.setShow('countries.edges.node.region.country.currencyCodes', False)
    query.setShow('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.setShow('currencies.pageInfo.hasNextPage', False)
##

##RESULT a) and b)
    print('Query GQL syntax: ' + query.exportGqlSource)
##

##STEP 3
    try:
        response = requests.request('POST', url=gdbcUrl, 
                                    json= { "query": query.exportGqlSource }, 
                                    headers=gdbcHeaders)
##
        
##STEP 4
        from pygqlmap.network import GQLResponse
        
        gqlResponse = GQLResponse(response)
##
        
        gqlResponse.printMessageOutput()
        
##STEP 5
        gqlResponse.mapGQLDataToObj(query.obj)
##
        
##RESULT c)
        print('resultObject: ' + str(gqlResponse.resultObject))
##

    except Exception as ex:
        ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObject")
