from gqlTypes import GQLConnection, GQLEdges, GQLObject

plainNestedQuery="""query Currencies {  currencies(first: 10, after: "Mg==") {  totalCount    edges {      cursor      node {        countryCodes        code        symbol      }    }    pageInfo {      startCursor      endCursor      hasNextPage      hasPreviousPage    }  }}"""

# plainNestedVariables={
#   "first": 10,
#   "after": "Mg=="
# }

plainNestedQueryWVar="""query currencies($first: Int, $after: String) {
  currencies(first: $first, after: $after) {
    totalCount
    edges {
      cursor
      node {
        countryCodes
        code
        symbol
      }
    }
    pageInfo {
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
    }
  }
}"""

plainNestedVariables={
   "first": 10,
   "after": "Mg=="
}

plainComplexQueryWVar = """query countries ($code: ID){  countries {    totalCount    edges {      cursor      node {        code        callingCode        wikiDataId        capital        name        currencyCodes        flagImageUri        numRegions        region(code:$code) {          fipsCode          isoCode          wikiDataId          name          capital          country {            code            callingCode            wikiDataId            capital            name            currencyCodes            flagImageUri            numRegions          }          numPopulatedPlaces          populatedPlaces {            totalCount          }        }        regions {          totalCount          edges {            cursor          }          pageInfo {            startCursor            endCursor            hasNextPage            hasPreviousPage          }        }      }    }    pageInfo {      startCursor      endCursor      hasNextPage      hasPreviousPage    }  }}"""

plainComplexVariables ="""{ "code": "VN" }"""

class currency(GQLObject): 
    countryCodes: list
    code: str
    symbol: str
    
    def __init__(self):
        self.countryCodes = []
        self.code = ''
        self.symbol = ''
        super().__init__()

class currencies(GQLConnection): 
    
    def __init__(self):
        super().__init__(GQLEdges(currency())) 
    