from pygqlmap import GQLQuery
from pygqlmap.components import GQLOperationArgs
from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class country(GQLQuery):
   class CountryArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL
      displayOptions: DisplayOptions

   _args: CountryArgs


   type: Country

class countries(GQLQuery):
   class CountriesConnectionArgs(GQLArgsSet, GQLObject): 
      currencyCode: str
      namePrefix: str
      namePrefixDefaultLangResults: bool
      first: int
      after: str
      last: int
      before: str
      displayOptions: DisplayOptions

   _args: CountriesConnectionArgs


   type: CountriesConnection

class currencies(GQLQuery):
   class CurrenciesConnectionArgs(GQLArgsSet, GQLObject): 
      countryId: ID
      first: int
      after: str
      last: int
      before: str

   _args: CurrenciesConnectionArgs


   type: CurrenciesConnection

class distanceBetween(GQLQuery):
   class floatArgs(GQLArgsSet, GQLObject): 
      fromPlaceId: ID ##NON NULL
      toPlaceId: ID ##NON NULL
      distanceUnit: DistanceUnit

   _args: floatArgs


   type: float

class locales(GQLQuery):
   class LocalesConnectionArgs(GQLArgsSet, GQLObject): 
      first: int
      after: str
      last: int
      before: str

   _args: LocalesConnectionArgs


   type: LocalesConnection

class populatedPlace(GQLQuery):
   class PopulatedPlaceArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL
      displayOptions: DisplayOptions

   _args: PopulatedPlaceArgs


   type: PopulatedPlace

class populatedPlaces(GQLQuery):
   class PopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject): 
      location: Location
      radius: float
      distanceUnit: DistanceUnit
      countryIds: ID ##LIST
      excludedCountryIds: ID ##LIST
      namePrefix: str
      namePrefixDefaultLangResults: bool
      minPopulation: int
      maxPopulation: int
      timeZoneIds: ID ##LIST
      types: str ##LIST
      sort: str
      first: int
      after: str
      last: int
      before: str
      displayOptions: DisplayOptions
      includeDeleted: IncludeDeletedFilterType

   _args: PopulatedPlacesConnectionArgs


   type: PopulatedPlacesConnection

class timeZone(GQLQuery):
   class TimeZoneArgs(GQLArgsSet, GQLObject): 
      id: ID ##NON NULL

   _args: TimeZoneArgs


   type: TimeZone

class timeZones(GQLQuery):
   class TimeZonesConnectionArgs(GQLArgsSet, GQLObject): 
      first: int
      after: str
      last: int
      before: str

   _args: TimeZonesConnectionArgs


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
