from pygqlmap import GQLQuery
from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class country(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL
      displayOptions: DisplayOptions

   _args: Args


   type: Country

class countries(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
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
   class Args(GQLArgsSet, GQLObject): 
      countryId: ID
      first: int
      after: str
      last: int
      before: str

   _args: Args


   type: CurrenciesConnection

class distanceBetween(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      fromPlaceId: ID ##NON NULL
      toPlaceId: ID ##NON NULL
      distanceUnit: DistanceUnit

   _args: Args


   type: float

class locales(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      first: int
      after: str
      last: int
      before: str

   _args: Args


   type: LocalesConnection

class populatedPlace(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL
      displayOptions: DisplayOptions

   _args: Args


   type: PopulatedPlace

class populatedPlaces(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
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
   class Args(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: Args


   type: TimeZone

class timeZones(GQLQuery):
   class Args(GQLArgsSet, GQLObject): 
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
