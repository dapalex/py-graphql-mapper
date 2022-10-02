import enum
from src import ID, GQLObject 
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from populatedPlace import populatedPlace
    from country import country
    from countryRegion import countryRegion

class PopulatedPlaceType(enum.Enum):
    # A level-2 administrative division (for example, a county)
    ADM2 = 'ADM2',	
	# A city, town, or village
    CITY = 'CITY'

class populatedPlace(GQLObject):
    isoCode: ID
    wikiDataId: ID
    name: str
    placeType: PopulatedPlaceType
    elevationMeters: int
    latitude: float
    longitude: float
    population: int
	# The place timezone id
    timezone: str
    # The place's country
    country: 'country'
	# The place's region
    region: 'countryRegion'
	# The place containing this place, if any
    ### it will be populatedPlace class
    locatedIn: 'populatedPlace'
	# If this place has been marked deleted
    deleted = bool
	# The distance result from some location-based query
	# This field has two forms:
	# - As a property (e.g., place.distance), returns the distance as part of a query
    # returning places sorted by distance.
    # - As a function (e.g., place.distance(toPlaceId), returns the distance to the
	# specified place.
 
    def __init__(self, ):
        self.isoCode = ''
        self.wikiDataId = str
        self.name = ''
        self.placeType = PopulatedPlaceType.CITY
        self.elevationMeters = -1
        self.latitude = -1
        self.longitude = -1
        self.population = -1
        self.timezone = ''
        self.country = lambda: country()
        self.region = lambda: countryRegion()
        self.locatedIn = lambda: populatedPlace()
        self.deleted = False
        super().__init__() 
