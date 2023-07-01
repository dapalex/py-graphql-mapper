from typing import Generic, Union, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from typing import NewType
from .gql_simple_types import *
from .enums import *
from .scalars import *
from .type_refs import *

class Location(GQLObject):
   """
   Location - Location GPS latitude/longitude coordinates

   latitude - DD.DDDD from -90 to 90

   longitude - DD.DDDD from -180 to 180

   """
   latitude: float
   longitude: float

class DisplayOptions(GQLObject):
   """
   DisplayOptions - How the results should be rendered

   asciiMode - Whether to display results using ASCII-only characters

   language - What language to display the results in

   """
   asciiMode: bool
   language: Language

class ConnectionPageInfo(GQLObject):
   """
   ConnectionPageInfo - Info about the current connection page slice

   startCursor - The opaque id of the cursor representing the index of the first element in this page

   endCursor - The opaque id of the cursor representing the index of the last element in this page

   hasNextPage - Whether there are more pages in the results

   hasPreviousPage - Whether there are previous pages in the results

   """
   startCursor: str
   endCursor: str
   hasNextPage: bool
   hasPreviousPage: bool

class TimeZoneEdge(GQLObject):
   """
   TimeZoneEdge - When paging time-zones, wraps a time-zone node together with the cursor referencing its position in the results

   cursor - The cursor id referencing the position of this node in the results

   node - The node value

   """
   cursor: str
   node: TimeZone

class NonNull_list_TimeZoneEdge(list, TimeZoneEdge): pass

class TimeZonesConnection(GQLObject):
   """
   TimeZonesConnection - A pageable view into time-zone results

   totalCount - The total number of results

   edges - The edges in the current page of results

   pageInfo - Info about the current page of results

   """
   totalCount: int
   edges: NonNull_list_TimeZoneEdge[TimeZoneEdge]
   pageInfo: ConnectionPageInfo

class NonNull_list_GQLObject(list, GQLObject): pass

class CountryPopulatedPlacesConnection(GQLObject):
   """
   CountryPopulatedPlacesConnection - A pageable view into country populated-place results

   totalCount - The total number of results

   edges - The edges in the current page of results

   pageInfo - Info about the current page of results

   """
   totalCount: int
   edges: NonNull_list_GQLObject[GQLObject] ## Circular Reference for PopulatedPlaceEdge
   pageInfo: ConnectionPageInfo

class TQKCF_RegionPopulatedPlacesConnection_Field(Generic[RegionPopulatedPlacesConnection]):
   """
   TQKCF_RegionPopulatedPlacesConnection_Field - Find populated places in this region

   """
   class RegionPopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject):
      """
      namePrefix - Only places whose names start with this prefix. If language is set, the prefix will be matched on the name as it appears in that language.

      namePrefixDefaultLangResults - When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested.

      minPopulation - Only places having at least this population

      maxPopulation - Only places having no more than this population

      timeZoneIds - Only places in these time-zones

      types - Only places for these types

      sort - How to sort place results
Format: ±SORT_FIELD,±SORT_FIELD
where SORT_FIELD = elevation | name | population

      first - How many results to retrieve from the beginning (or after the 'after' cursor, if specified)

      after - The cursor id after which to get results

      last - How many results to retrieve from the end (or before the 'before' cursor, if specified)

      before - The cursor id before which to get results

      includeDeleted - Whether to include any places marked deleted

      """
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
      includeDeleted: IncludeDeletedFilterType

   _args: RegionPopulatedPlacesConnectionArgs



class CountryRegion(GQLObject):
   """
   CountryRegion - A region in a country. This could be a state, province, district, or otherwise major political division.

   fipsCode - The region FIPS 10-4 code

   isoCode - The region ISO-3166 code

   wikiDataId - The region WikiData id

   name - The region name

   capital - The region's capital city

   containingRegion - The region this region is in, if any

   country - The region's country

   numPopulatedPlaces - The number of populated places in this region

   populatedPlaces - Find populated places in this region

   """
   fipsCode: ID
   isoCode: ID
   wikiDataId: ID
   name: str
   capital: str
   containingRegion: NewType('CountryRegion', GQLObject) ## Circular Reference for CountryRegion
   country: NewType('Country', GQLObject) ## Circular Reference for Country
   numPopulatedPlaces: int
   populatedPlaces: TQKCF_RegionPopulatedPlacesConnection_Field ## Circular Reference for RegionPopulatedPlacesConnection

class CountryRegionEdge(GQLObject):
   """
   CountryRegionEdge - When paging regions, wraps a region node together with the cursor referencing its position in the results

   cursor - The cursor id referencing the position of this node in the results

   node - The node value

   """
   cursor: str
   node: CountryRegion

class NonNull_list_CountryRegionEdge(list, CountryRegionEdge): pass

class CountryRegionsConnection(GQLObject):
   """
   CountryRegionsConnection - A pageable view into region results

   totalCount - The total number of results

   edges - The edges in the current page of results

   pageInfo - Info about the current page of results

   """
   totalCount: int
   edges: NonNull_list_CountryRegionEdge[CountryRegionEdge]
   pageInfo: ConnectionPageInfo

class GCMWQ_CountryPopulatedPlacesConnection_Field(CountryPopulatedPlacesConnection):
   """
   GCMWQ_CountryPopulatedPlacesConnection_Field - Find populated places in this country

   """
   class CountryPopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject):
      """
      namePrefix - Only places whose names start with this prefix. If language is set, the prefix will be matched on the name as it appears in that language.

      namePrefixDefaultLangResults - When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested.

      minPopulation - Only places having at least this population

      maxPopulation - Only places having no more than this population

      timeZoneIds - Only places in these time-zones

      types - Only places for these types

      sort - How to sort place results
Format: ±SORT_FIELD,±SORT_FIELD
where SORT_FIELD = elevation | name | population

      first - How many results to retrieve from the beginning (or after the 'after' cursor, if specified)

      after - The cursor id after which to get results

      last - How many results to retrieve from the end (or before the 'before' cursor, if specified)

      before - The cursor id before which to get results

      includeDeleted - Whether to include any places marked deleted

      """
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
      includeDeleted: IncludeDeletedFilterType

   _args: CountryPopulatedPlacesConnectionArgs



class IBYOD_CountryRegion_Field(CountryRegion):
   """
   IBYOD_CountryRegion_Field - Look up a region in this country

   """
   class CountryRegionArgs(GQLArgsSet, GQLObject):
      """
      code - An ISO-3166 or FIPS region code

      """
      code: ID

   _args: CountryRegionArgs



class NUAOR_CountryRegionsConnection_Field(CountryRegionsConnection):
   """
   NUAOR_CountryRegionsConnection_Field - Find regions in this country

   """
   class CountryRegionsConnectionArgs(GQLArgsSet, GQLObject):
      """
      namePrefix - Only regions whose names start with this prefix. If language is set, the prefix will be matched on the name as it appears in that language.

      namePrefixDefaultLangResults - When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested.

      sort - How to sort regions
Format: ±SORT_FIELD
where SORT_FIELD = fipsCode | isoCode | name

      first - How many results to retrieve from the beginning (or after the 'after' cursor, if specified)

      after - The cursor id after which to get results

      last - How many results to retrieve from the end (or before the 'before' cursor, if specified)

      before - The cursor id before which to get results

      """
      namePrefix: str
      namePrefixDefaultLangResults: bool
      sort: str
      first: int
      after: str
      last: int
      before: str

   _args: CountryRegionsConnectionArgs



class Country(GQLObject):
   """
   Country - A country

   code - The ISO-3166 country code

   callingCode - The country dialing prefix

   wikiDataId - The country WikiData id

   capital - The country's capital city

   name - The country name

   currencyCodes - A list of supported ISO-4217 currency codes

   flagImageUri - The country flag image

   numRegions - The number of regions in this country

   populatedPlaces - Find populated places in this country

   region - Look up a region in this country

   regions - Find regions in this country

   """
   code: ID
   callingCode: str
   wikiDataId: ID
   capital: str
   name: str
   currencyCodes: NonNull_list[str]
   flagImageUri: str
   numRegions: int
   populatedPlaces: GCMWQ_CountryPopulatedPlacesConnection_Field
   region: IBYOD_CountryRegion_Field
   regions: NUAOR_CountryRegionsConnection_Field

class NearbyPopulatedPlacesConnection(GQLObject):
   """
   NearbyPopulatedPlacesConnection - A pageable view into nearby populated-place results

   totalCount - The total number of results

   edges - The edges in the current page of results

   pageInfo - Info about the current page of results

   """
   totalCount: int
   edges: NonNull_list_GQLObject[GQLObject] ## Circular Reference for PopulatedPlaceEdge
   pageInfo: ConnectionPageInfo

class LSSIL_NearbyPopulatedPlacesConnection_Field(NearbyPopulatedPlacesConnection):
   """
   LSSIL_NearbyPopulatedPlacesConnection_Field - Find nearby populated places

   """
   class NearbyPopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject):
      """
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

      includeDeleted - Whether to include any places marked deleted

      """
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
      includeDeleted: IncludeDeletedFilterType

   _args: NearbyPopulatedPlacesConnectionArgs



class PopulatedPlace(GQLObject):
   """
   PopulatedPlace - A place with some population of inhabitants

   id - The place native id

   wikiDataId - The place WikiData id

   name - The place name

   placeType - The place type

   elevationMeters - The place elevation (meters) above sea level

   latitude - The place latittude (-90.0 to 90.0)

   longitude - The place longitude (-180.0 to 180.0)

   population - The place population

   timezone - The place timezone id

   country - The place's country

   region - The place's region

   distance - The distance result from some location-based query
This field has two forms:
- As a property (e.g., place.distance), returns the distance as part of a query returning places sorted by distance.
- As a function (e.g., place.distance(toPlaceId), returns the distance to the specified place.

   locatedIn - The place containing this place, if any

   nearbyPopulatedPlaces - Find nearby populated places

   deleted - If this place has been marked deleted

   """
   id: ID
   wikiDataId: ID
   name: str
   placeType: PopulatedPlaceType
   elevationMeters: int
   latitude: float
   longitude: float
   population: int
   timezone: str
   country: Country
   region: CountryRegion
   distance: CKXYT_distance_Field
   locatedIn: NewType('PopulatedPlace', GQLObject) ## Circular Reference for PopulatedPlace
   nearbyPopulatedPlaces: LSSIL_NearbyPopulatedPlacesConnection_Field
   deleted: bool

class PopulatedPlaceEdge(GQLObject):
   """
   PopulatedPlaceEdge - When paging populated places, wraps a place node together with the cursor referencing its position in the results

   cursor - The cursor id referencing the position of this node in the results

   node - The node value

   """
   cursor: str
   node: PopulatedPlace

class NonNull_list_PopulatedPlaceEdge(list, PopulatedPlaceEdge): pass

class RegionPopulatedPlacesConnection(GQLObject):
   """
   RegionPopulatedPlacesConnection - A pageable view into regional populated-place results

   totalCount - The total number of results

   edges - The edges in the current page of results

   pageInfo - Info about the current page of results

   """
   totalCount: int
   edges: NonNull_list_PopulatedPlaceEdge[PopulatedPlaceEdge]
   pageInfo: ConnectionPageInfo

class PopulatedPlacesConnection(GQLObject):
   """
   PopulatedPlacesConnection - A pageable view into populated-place results

   totalCount - The total number of results

   edges - The edges in the current page of results

   pageInfo - Info about the current page of results

   """
   totalCount: int
   edges: NonNull_list_PopulatedPlaceEdge[PopulatedPlaceEdge]
   pageInfo: ConnectionPageInfo

class LocaleEdge(GQLObject):
   """
   LocaleEdge - When paging locales, wraps a locale node together with the cursor referencing its position in the results

   cursor - The cursor id referencing the position of this node in the results

   node - The node value

   """
   cursor: str
   node: Locale

class NonNull_list_LocaleEdge(list, LocaleEdge): pass

class LocalesConnection(GQLObject):
   """
   LocalesConnection - A pageable view into locale results

   totalCount - The total number of results

   edges - The edges in the current page of results

   pageInfo - Info about the current page of results

   """
   totalCount: int
   edges: NonNull_list_LocaleEdge[LocaleEdge]
   pageInfo: ConnectionPageInfo

class CurrencyEdge(GQLObject):
   """
   CurrencyEdge - When paging currencies, wraps a currency node together with the cursor referencing its position in the results

   cursor - The cursor id referencing the position of this node in the results

   node - The node value

   """
   cursor: str
   node: Currency

class NonNull_list_CurrencyEdge(list, CurrencyEdge): pass

class CurrenciesConnection(GQLObject):
   """
   CurrenciesConnection - A pageable view into currency results

   totalCount - The total number of results

   edges - The edges in the current page of results

   pageInfo - Info about the current page of results

   """
   totalCount: int
   edges: NonNull_list_CurrencyEdge[CurrencyEdge]
   pageInfo: ConnectionPageInfo

class CountryEdge(GQLObject):
   """
   CountryEdge - When paging countries, wraps a country node together with the cursor referencing its position in the results

   cursor - The cursor id referencing the position of this node in the results

   node - The node value

   """
   cursor: str
   node: Country

class NonNull_list_CountryEdge(list, CountryEdge): pass

class CountriesConnection(GQLObject):
   """
   CountriesConnection - A pageable view into country results

   totalCount - The total number of results

   edges - The edges in the current page of results

   pageInfo - Info about the current page of results

   """
   totalCount: int
   edges: NonNull_list_CountryEdge[CountryEdge]
   pageInfo: ConnectionPageInfo
