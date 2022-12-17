
""" 
    USE CASE DESCRIPTION: 
    This test shows how to create a GraphQL Query to fetch a GraphQL complex type (made of objects, connections, and scalar fields) combining arguments usage as literal values
    with visibility usage for chosen fields, and finally build the python class instance containing the data from the response
    
    Query to reproduce:
    
    query myCountriesQuery  { 
        countries(currencyCode: "USD") { 
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
                    region(code: "AK") { 
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
from enum import Enum
from typing import NewType
from pygqlmap.gqlTypes import ID
from pygqlmap.components import GQLObject
from utils import ManageException

class PopulatedPlaceType(Enum):
   ADM2 = 'ADM2' ##A level-2 administrative division (for example, a county)
   CITY = 'CITY' ##A city, town, or village


class Language(Enum):
   DE = 'DE' ##German
   EN = 'EN' ##English
   ES = 'ES' ##Spanish
   FR = 'FR' ##French
   IT = 'IT' ##Italian
   PT = 'PT' ##Portuguese
   PT_BR = 'PT_BR' ##Portuguese (Brazil)
   RU = 'RU' ##Russian

class DisplayOptions(GQLObject):
   asciiMode: bool
   language: Language

class ConnectionPageInfo(GQLObject):
   startCursor: str ##NON NULL
   endCursor: str ##NON NULL
   hasNextPage: bool ##NON NULL
   hasPreviousPage: bool ##NON NULL

class Country(GQLObject):
   code: ID ##NON NULL
   callingCode: str ##NON NULL
   wikiDataId: ID ##NON NULL
   capital: str
   name: str ##NON NULL
   currencyCodes: str ##NON NULL
   flagImageUri: str ##NON NULL
   numRegions: int ##NON NULL
   
class CountryRegion(GQLObject):
   fipsCode: ID
   isoCode: ID ##NON NULL
   wikiDataId: ID
   name: str ##NON NULL
   capital: str
   country: Country ##NON NULL ## Circular Reference for Country
   numPopulatedPlaces: int ##NON NULL
   populatedPlaces: NewType('RegionPopulatedPlacesConnection', GQLObject) ## Circular Reference for RegionPopulatedPlacesConnection

class CountryRegionsConnection(GQLObject):
   totalCount: int ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL

class CountryNode(GQLObject):
   code: ID ##NON NULL
   callingCode: str ##NON NULL
   wikiDataId: ID ##NON NULL
   capital: str
   name: str ##NON NULL
   currencyCodes: str ##NON NULL
   flagImageUri: str ##NON NULL
   numRegions: int ##NON NULL
   region: CountryRegion
   regions: CountryRegionsConnection

class CountryEdge(GQLObject):
   cursor: str ##NON NULL
   node: CountryNode ##NON NULL

class CountriesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: CountryEdge ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL

class PopulatedPlace(GQLObject):
   id: ID ##NON NULL
   wikiDataId: ID
   name: str ##NON NULL
   placeType: PopulatedPlaceType ##NON NULL
   elevationMeters: int
   latitude: float
   longitude: float
   population: int ##NON NULL
   timezone: str ##NON NULL
   country: Country ##NON NULL
   region: CountryRegion
   distance: float
   deleted: bool ##NON NULL
   locatedIn: NewType('PopulatedPlace', GQLObject) ## Circular Reference for PopulatedPlace

class countries(GQLObject):
   type: CountriesConnection
   currencyCode: str
   namePrefix: str
   namePrefixDefaultLangResults: bool
   first: int
   after: str
   last: int
   before: str
   displayOptions: DisplayOptions

class PopulatedPlaceEdge(GQLObject):
   cursor: str ##NON NULL
   node: PopulatedPlace ##NON NULL

class NearbyPopulatedPlacesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: PopulatedPlaceEdge ##NON NULL ## Circular Reference for PopulatedPlaceEdge
   pageInfo: ConnectionPageInfo ##NON NULL

class PopulatedPlaceEdge(GQLObject):
   cursor: str ##NON NULL
   node: PopulatedPlace ##NON NULL

class RegionPopulatedPlacesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: PopulatedPlaceEdge ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL

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
from pygqlmap.components import GQLArgsSet
from pygqlmap.enums import ArgType

async def testGeneratedDataAsGQLObject(): 
    print('\n\nRunning testGeneratedDataAsGQLObject...')
##STEP 2
    from pygqlmap.enums import OperationType
    from pygqlmap.components import GQLOperation
    
    query = GQLOperation(OperationType.query, CountriesConnection, operationName='myCountriesQuery', rootName='countries') 
##
    
##STEP 3
    argsCntrs = GQLArgsSet(location='countries')
    argsCntrs.addArg('currencyCode', 'USD')
    argsRegion = GQLArgsSet('countries.edges.node.region')
    argsRegion.addArg('code', "AZ")
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
        
    print("End of testGeneratedDataAsGQLObject")
