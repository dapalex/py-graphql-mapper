from gqlTypes import GQLObject
from .populatedPlaces import populatedPlaces
from .country import country

class countryRegion(GQLObject):
    fipsCode: str
    isoCode: str
    wikiDataId: str
    name: str
    capital: str
    country: 'country'
    numPopulatedPlaces: int
    populatedPlaces: 'populatedPlaces'
    
    def __init__(self):
        self.fipsCode = ''
        self.isoCode = ''
        self.wikiDataId = ''
        self.name = ''
        self.capital = ''
        self.country = country()
        self.numPopulatedPlaces = -1
        self.populatedPlaces = populatedPlaces()
        super().__init__()  
        
        
