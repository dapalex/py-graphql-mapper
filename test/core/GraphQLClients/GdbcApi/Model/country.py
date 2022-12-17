from pygqlmap.components import GQLObject
from pygqlmap.gqlTypes import ID

class Country(GQLObject):
    code: ID ##ID non-null
    callingCode: str ##non-null
    wikiDataId: ID ##ID non-null
    capital: str
    name: str ##non-null
    currencyCodes: list ##of str
    flagImageUri: str ##non-null
    numRegions: int ##non-null
    
    # def __init__(self):
    #     self.code = ''
    #     self.callingCode = ''
    #     self.wikiDataId = ''
    #     self.name = ''
    #     self.currencyCodes = []
    #     self.flagImageUri = ''
    #     self.numRegions = -1
    #     self.capital = ''
    #     super().__init__()
    
from .countryRegion import countryRegion
from .countryRegions import countryRegions

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
     
    # def __init__(self):
    #     self.code = ''
    #     self.callingCode = ''
    #     self.wikiDataId = ''
    #     self.name = ''
    #     self.currencyCodes = []
    #     self.flagImageUri = ''
    #     self.numRegions = -1
    #     self.capital = ''
    #     self.region = countryRegion()
    #     self.regions = countryRegions()
    #     super().__init__() 
