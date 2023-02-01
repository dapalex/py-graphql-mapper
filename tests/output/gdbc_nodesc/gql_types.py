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
   latitude: float
   longitude: float

class DisplayOptions(GQLObject):
   asciiMode: bool
   language: Language

class ConnectionPageInfo(GQLObject):
   startCursor: str
   endCursor: str
   hasNextPage: bool
   hasPreviousPage: bool

class TimeZoneEdge(GQLObject):
   cursor: str
   node: TimeZone

class TimeZonesConnection(GQLObject):
   totalCount: int
   edges: TimeZoneEdge
   pageInfo: ConnectionPageInfo

class MUAZP_RegionPopulatedPlacesConnection_Field(Generic[RegionPopulatedPlacesConnection]):
   class RegionPopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject):
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
   fipsCode: ID
   isoCode: ID
   wikiDataId: ID
   name: str
   capital: str
   country: NewType('Country', GQLObject) ## Circular Reference for Country
   numPopulatedPlaces: int
   populatedPlaces: MUAZP_RegionPopulatedPlacesConnection_Field ## Circular Reference for RegionPopulatedPlacesConnection

class CountryRegionEdge(GQLObject):
   cursor: str
   node: CountryRegion

class CountryRegionsConnection(GQLObject):
   totalCount: int
   edges: CountryRegionEdge
   pageInfo: ConnectionPageInfo

class STGQW_CountryRegion_Field(CountryRegion):
   class CountryRegionArgs(GQLArgsSet, GQLObject):
      code: ID

   _args: CountryRegionArgs



class YCJHK_CountryRegionsConnection_Field(CountryRegionsConnection):
   class CountryRegionsConnectionArgs(GQLArgsSet, GQLObject):
      namePrefix: str
      namePrefixDefaultLangResults: bool
      sort: str
      first: int
      after: str
      last: int
      before: str

   _args: CountryRegionsConnectionArgs



class Country(GQLObject):
   code: ID
   callingCode: str
   wikiDataId: ID
   capital: str
   name: str
   currencyCodes: str
   flagImageUri: str
   numRegions: int
   region: STGQW_CountryRegion_Field
   regions: YCJHK_CountryRegionsConnection_Field

class NearbyPopulatedPlacesConnection(GQLObject):
   totalCount: int
   edges: NewType('PopulatedPlaceEdge', GQLObject) ## Circular Reference for PopulatedPlaceEdge
   pageInfo: ConnectionPageInfo

class YIUSU_NearbyPopulatedPlacesConnection_Field(NearbyPopulatedPlacesConnection):
   class NearbyPopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject):
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
   distance: BJKCR_distance_Field
   locatedIn: NewType('PopulatedPlace', GQLObject) ## Circular Reference for PopulatedPlace
   nearbyPopulatedPlaces: YIUSU_NearbyPopulatedPlacesConnection_Field
   deleted: bool

class PopulatedPlaceEdge(GQLObject):
   cursor: str
   node: PopulatedPlace

class RegionPopulatedPlacesConnection(GQLObject):
   totalCount: int
   edges: PopulatedPlaceEdge
   pageInfo: ConnectionPageInfo

class PopulatedPlacesConnection(GQLObject):
   totalCount: int
   edges: PopulatedPlaceEdge
   pageInfo: ConnectionPageInfo

class LocaleEdge(GQLObject):
   cursor: str
   node: Locale

class LocalesConnection(GQLObject):
   totalCount: int
   edges: LocaleEdge
   pageInfo: ConnectionPageInfo

class CurrencyEdge(GQLObject):
   cursor: str
   node: Currency

class CurrenciesConnection(GQLObject):
   totalCount: int
   edges: CurrencyEdge
   pageInfo: ConnectionPageInfo

class CountryEdge(GQLObject):
   cursor: str
   node: Country

class CountriesConnection(GQLObject):
   totalCount: int
   edges: CountryEdge
   pageInfo: ConnectionPageInfo
