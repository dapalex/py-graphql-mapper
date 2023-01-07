
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


    STEP 1: Instantiate the class representing the GraphQL query 
    STEP 2: Set the arguments
    STEP 3: Call setShow function of GQLOperation class to set the visibility of chosen fields (path to declare with dot notation)
    STEP 4: Query the GraphQL server
    STEP 5: Pass the response received to the GQLResponse constructor
    STEP 6: Call mapGQLDataToObj() function to obtain the python class with data from GraphQL server
    
    RESULT: 
        a) The request toward the GraphQL server will not have the hidden fields
        b) The request toward the GraphQL server will have the query with arguments 'currencyCode' and 'code' 
        b) The python class instance obtained from the response will not have the hidden fields
"""

from pygqlmap.network import httpRequest
from ..consts import gdbcHeaders, gdbcUrl
# from ..utils import ManageException
from ..output.GeoDBCities.queries import countries

def testComplexObject(): 
    print('\n\nRunning testComplexObject...')
##STEP 1
    query = countries()
    query.name = 'myCountriesQuery'
##
    
##STEP 2
    query._args.currencyCode = 'USD'
    query.type.edges.node.region._args.code = "AK"
##

##STEP 3
    query.setShow('countries.edges.node.callingCode', False)
    query.setShow('countries.edges.node.currencyCodes', False)
    query.setShow('countries.edges.node.regions.pageInfo.hasNextPage', False)
    query.setShow('currencies.pageInfo.hasNextPage', False)
##

##RESULT a) and b)
    print('Query GQL syntax: ' + query.exportGqlSource)
##

##STEP 4
    try:
        response = httpRequest(gdbcUrl, 
                                     { "query": query.exportGqlSource }, 
                                    gdbcHeaders)
##
        
##STEP 5
        from pygqlmap.network import GQLResponse
        
        gqlResponse = GQLResponse(response)
##
        
        gqlResponse.printMessageOutput()
        
##STEP 6
        gqlResponse.mapGQLDataToObj(query.type)
##
        
##RESULT c)
        print('resultObject: ' + str(gqlResponse.resultObject))
##

    except Exception as ex:
        raise ex #ManageException('!!executeQuery FAILED!! - ' + ex.args[0])
        
    print("End of testComplexObject")
