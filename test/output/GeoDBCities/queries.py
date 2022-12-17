from .gqlTypes import *
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *

class country(GQLObject):
   """
   country - Look up a country

   """
   class Args(): 
      """
      id - An ISO-3166 country code or WikiData id

      displayOptions - How to display the results

      """
      id: ID ##NON NULL
      displayOptions: DisplayOptions

   _args: Args


   type: Country

class countries(GQLObject):
   """
   countries - Find countries, filtering by optional criteria. If no criteria are set, you will get back all known countries.

   """
   class Args(): 
      """
      currencyCode - Only countries supporting this currency

      namePrefix - Only countries whose names start with this prefix. If language is set, the prefix will be matched on the name as it appears in that language.

      namePrefixDefaultLangResults - When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested.

      first - How many results to retrieve from the beginning (or after the 'after' cursor, if specified)

      after - The cursor id after which to get results

      last - How many results to retrieve from the end (or before the 'before' cursor, if specified)

      before - The cursor id before which to get results

      displayOptions - How to display the results

      """
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
   """
   currencies - Find currencies, filtering by optional criteria. If no criteria are set, you will get back all known currencies.

   """
   class Args(): 
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

   _args: Args


   type: CurrenciesConnection

distanceBetween = float

class locales(GQLObject):
   """
   locales - Get all known locales

   """
   class Args(): 
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

   _args: Args


   type: LocalesConnection

class populatedPlace(GQLObject):
   """
   populatedPlace - Look up a populated place

   """
   class Args(): 
      """
      id -  A place id (either native id or Wikidata ID)

      displayOptions - How to display the results

      """
      id: ID ##NON NULL
      displayOptions: DisplayOptions

   _args: Args


   type: PopulatedPlace

class populatedPlaces(GQLObject):
   """
   populatedPlaces - Find populated places, filtering by optional criteria. If no criteria are set, you will get back all known places.

   """
   class Args(): 
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

      sort - How to sort place results
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

   _args: Args


   type: PopulatedPlacesConnection

class timeZone(GQLObject):
   """
   timeZone - Look up a time-zone

   """
   class Args(): 
      id: ID ##NON NULL

   _args: Args


   type: TimeZone

class timeZones(GQLObject):
   """
   timeZones - Get all known time-zones

   """
   class Args(): 
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
