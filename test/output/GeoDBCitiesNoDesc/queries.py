from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class country(GQLObject):
   class Args(): 
      id: ID ##NON NULL
      displayOptions: DisplayOptions

   _args: Args


   type: Country

class countries(GQLObject):
   class Args(): 
      currencyCode: str
      namePrefix: str
      namePrefixDefaultLangResults: bool
      first: int
      after: str
      last: int
      before: str
      displayOptions: DisplayOptions

   _args: Args


   type: CountriesConnection

class currencies(GQLObject):
   class Args(): 
      countryId: ID
      first: int
      after: str
      last: int
      before: str

   _args: Args


   type: CurrenciesConnection

distanceBetween = float

class locales(GQLObject):
   class Args(): 
      first: int
      after: str
      last: int
      before: str

   _args: Args


   type: LocalesConnection

class populatedPlace(GQLObject):
   class Args(): 
      id: ID ##NON NULL
      displayOptions: DisplayOptions

   _args: Args


   type: PopulatedPlace

class populatedPlaces(GQLObject):
   class Args(): 
      location: Location
      radius: float
      distanceUnit: DistanceUnit
      countryIds: list[ID]
      excludedCountryIds: list[ID]
      namePrefix: str
      namePrefixDefaultLangResults: bool
      minPopulation: int
      maxPopulation: int
      timeZoneIds: list[ID]
      types: list[str]
      sort: str
      first: int
      after: str
      last: int
      before: str
      displayOptions: DisplayOptions
      includeDeleted: IncludeDeletedFilterType

   _args: Args


   type: PopulatedPlacesConnection

class timeZone(GQLObject):
   class Args(): 
      id: ID ##NON NULL

   _args: Args


   type: TimeZone

class timeZones(GQLObject):
   class Args(): 
      first: int
      after: str
      last: int
      before: str

   _args: Args


   type: TimeZonesConnection


class Queries(Enum):
   country = country
   countries = countries
   currencies = currencies
   distanceBetween = distanceBetween
   locales = locales
   populatedPlace = populatedPlace
   populatedPlaces = populatedPlaces
   timeZone = timeZone
   timeZones = timeZones
