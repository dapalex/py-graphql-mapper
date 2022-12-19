from pygqlmap.components import GQLOperationArgs, GQLQuery
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class country(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL
      displayOptions: DisplayOptions

   _args: Args


   type: Country

class countries(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
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

class currencies(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      countryId: ID
      first: int
      after: str
      last: int
      before: str

   _args: Args


   type: CurrenciesConnection

distanceBetween = float

class locales(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      first: int
      after: str
      last: int
      before: str

   _args: Args


   type: LocalesConnection

class populatedPlace(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL
      displayOptions: DisplayOptions

   _args: Args


   type: PopulatedPlace

class populatedPlaces(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
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

class timeZone(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: TimeZone

class timeZones(GQLQuery):
   class Args(GQLOperationArgs, GQLObject): 
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
