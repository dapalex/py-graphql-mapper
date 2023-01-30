from typing import List
from pygqlmap import GQLQuery
from .gql_types import *
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

class country(GQLQuery):
   """
   country - Look up a country

   """
   class CountryArgs(GQLArgsSet, GQLObject):
      """
      id - An ISO-3166 country code or WikiData id

      displayOptions - How to display the results

      """
      id: NonNull_ID
      displayOptions: DisplayOptions

   _args: CountryArgs


   type: Country

class countries(GQLQuery):
   """
   countries - Find countries, filtering by optional criteria. If no criteria are set, you will get back all known countries.

   """
   class CountriesConnectionArgs(GQLArgsSet, GQLObject):
      """
      currencyCode - Only countries supporting this currency

      namePrefix - Only countries whose names start with this prefix. If language is set, the prefix will be matched on the name as it appears in that language.

      namePrefixDefaultLangResults - When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested.

      sort - How to sort countries
Format: ±SORT_FIELD
where SORT_FIELD = code | name

      first - How many results to retrieve from the beginning (or after the 'after' cursor, if specified)

      after - The cursor id after which to get results

      last - How many results to retrieve from the end (or before the 'before' cursor, if specified)

      before - The cursor id before which to get results

      displayOptions - How to display the results

      """
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
   """
   currencies - Find currencies, filtering by optional criteria. If no criteria are set, you will get back all known currencies.

   """
   class CurrenciesConnectionArgs(GQLArgsSet, GQLObject):
      """
      countryId - Currencies for this country id

      first - How many results to retrieve from the beginning (or after the 'after' cursor, if specified)

      after - The cursor id after which to get results

      last - How many results to retrieve from the end (or before the 'before' cursor, if specified)

      before - The cursor id before which to get results

      """
      countryId: ID
      first: int
      after: str
      last: int
      before: str

   _args: CurrenciesConnectionArgs


   type: CurrenciesConnection

class distanceBetween(GQLQuery):
   """
   distanceBetween - Get the distance between any two places

   """
   class floatArgs(GQLArgsSet, GQLObject):
      """
      fromPlaceId - From some place

      toPlaceId - To some place

      distanceUnit - The unit of distance to use

      """
      fromPlaceId: NonNull_ID
      toPlaceId: NonNull_ID
      distanceUnit: DistanceUnit

   _args: floatArgs


   type: float

class locales(GQLQuery):
   """
   locales - Get all known locales

   """
   class LocalesConnectionArgs(GQLArgsSet, GQLObject):
      """
      first - How many results to retrieve from the beginning (or after the 'after' cursor, if specified)

      after - The cursor id after which to get results

      last - How many results to retrieve from the end (or before the 'before' cursor, if specified)

      before - The cursor id before which to get results

      """
      first: int
      after: str
      last: int
      before: str

   _args: LocalesConnectionArgs


   type: LocalesConnection

class populatedPlace(GQLQuery):
   """
   populatedPlace - Look up a populated place

   """
   class PopulatedPlaceArgs(GQLArgsSet, GQLObject):
      """
      id -  A place id (either native id or Wikidata ID)

      displayOptions - How to display the results

      """
      id: NonNull_ID
      displayOptions: DisplayOptions

   _args: PopulatedPlaceArgs


   type: PopulatedPlace

class populatedPlaces(GQLQuery):
   """
   populatedPlaces - Find populated places, filtering by optional criteria. If no criteria are set, you will get back all known places.

   """
   class PopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject):
      """
      location - Only places near this location

      radius - The location radius within which to find places

      distanceUnit - The unit of distance to use

      countryIds - Only places in these countries

      excludedCountryIds - Only places NOT in these countries

      namePrefix - Only places whose names start with this prefix. If language is set, the prefix will be matched on the name as it appears in that language.

      namePrefixDefaultLangResults - When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested.

      minPopulation - Only places having at least this population

      maxPopulation - Only places having no more than this population

      timeZoneIds - Only places in these time-zones

      types - Only places for these types

      sort - How to sort places
Format: ±SORT_FIELD,±SORT_FIELD
where SORT_FIELD = countryCode | elevation | name | population

      first - How many results to retrieve from the beginning (or after the 'after' cursor, if specified)

      after - The cursor id after which to get results

      last - How many results to retrieve from the end (or before the 'before' cursor, if specified)

      before - The cursor id before which to get results

      displayOptions - How to display the results

      includeDeleted - Whether to include any places marked deleted

      """
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

   _args: PopulatedPlacesConnectionArgs


   type: PopulatedPlacesConnection

class timeZone(GQLQuery):
   """
   timeZone - Look up a time-zone

   """
   class TimeZoneArgs(GQLArgsSet, GQLObject):
      id: NonNull_ID

   _args: TimeZoneArgs


   type: TimeZone

class timeZones(GQLQuery):
   """
   timeZones - Get all known time-zones

   """
   class TimeZonesConnectionArgs(GQLArgsSet, GQLObject):
      """
      first - How many results to retrieve from the beginning (or after the 'after' cursor, if specified)

      after - The cursor id after which to get results

      last - How many results to retrieve from the end (or before the 'before' cursor, if specified)

      before - The cursor id before which to get results

      """
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
