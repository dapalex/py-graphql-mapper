from typing import List
from pygqlmap import GQLQuery
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

class country(GQLQuery):
   class CountryArgs(GQLArgsSet, GQLObject): 
      id: NonNull_ID
      displayOptions: DisplayOptions

   _args: CountryArgs


   type: Country

class countries(GQLQuery):
   class CountriesConnectionArgs(GQLArgsSet, GQLObject): 
      currencyCode: str
      namePrefix: str
      namePrefixDefaultLangResults: bool
      sort: str
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
      fromPlaceId: NonNull_ID
      toPlaceId: NonNull_ID
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
      id: NonNull_ID
      displayOptions: DisplayOptions

   _args: PopulatedPlaceArgs


   type: PopulatedPlace

class populatedPlaces(GQLQuery):
   class PopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject): 
      location: Location
      radius: float
      distanceUnit: DistanceUnit
      countryIds: List[ID]
      excludedCountryIds: List[ID]
      namePrefix: str
      namePrefixDefaultLangResults: bool
      minPopulation: int
      maxPopulation: int
      timeZoneIds: List[ID]
      types: List[str]
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
      id: NonNull_ID

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
