from pygqlmap.components import GQLObject
from .populatedPlaces import PopulatedPlaces
from .country import Country

class countryRegion(GQLObject):
    fipsCode: str
    isoCode: str
    wikiDataId: str
    name: str
    capital: str
    country: Country
    numPopulatedPlaces: int
    populatedPlaces: PopulatedPlaces
    
    # def __init__(self):
    #     self.fipsCode = ''
    #     self.isoCode = ''
    #     self.wikiDataId = ''
    #     self.name = ''
    #     self.capital = ''
    #     self.country = Country()
    #     self.numPopulatedPlaces = -1
    #     self.populatedPlaces = PopulatedPlaces()
    #     super().__init__()  
        
        
