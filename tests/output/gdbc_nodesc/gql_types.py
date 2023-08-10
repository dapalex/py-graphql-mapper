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

class list_TimeZoneEdge(list, TimeZoneEdge): pass

class TimeZonesConnection(GQLObject):
   totalCount: int
   edges: list_TimeZoneEdge[TimeZoneEdge]
   pageInfo: ConnectionPageInfo

class list_GQLObject(list, GQLObject): pass

class CountryPopulatedPlacesConnection(GQLObject):
   totalCount: int
   edges: list_GQLObject[GQLObject] ## Circular Reference for PopulatedPlaceEdge
   pageInfo: ConnectionPageInfo

class INYWV_RegionPopulatedPlacesConnection_Field(Generic[RegionPopulatedPlacesConnection]):
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
   containingRegion: NewType('CountryRegion', GQLObject) ## Circular Reference for CountryRegion
   country: NewType('Country', GQLObject) ## Circular Reference for Country
   numPopulatedPlaces: int
   populatedPlaces: INYWV_RegionPopulatedPlacesConnection_Field ## Circular Reference for RegionPopulatedPlacesConnection

class CountryRegionEdge(GQLObject):
   cursor: str
   node: CountryRegion

class list_CountryRegionEdge(list, CountryRegionEdge): pass

class CountryRegionsConnection(GQLObject):
   totalCount: int
   edges: list_CountryRegionEdge[CountryRegionEdge]
   pageInfo: ConnectionPageInfo

class DCGDO_CountryPopulatedPlacesConnection_Field(CountryPopulatedPlacesConnection):
   class CountryPopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject):
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



class XMBWA_CountryRegion_Field(CountryRegion):
   class CountryRegionArgs(GQLArgsSet, GQLObject):
      code: ID

   _args: CountryRegionArgs



class CFNUJ_CountryRegionsConnection_Field(CountryRegionsConnection):
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
   currencyCodes: list[str]
   flagImageUri: str
   numRegions: int
   populatedPlaces: DCGDO_CountryPopulatedPlacesConnection_Field
   region: XMBWA_CountryRegion_Field
   regions: CFNUJ_CountryRegionsConnection_Field

class NearbyPopulatedPlacesConnection(GQLObject):
   totalCount: int
   edges: list_GQLObject[GQLObject] ## Circular Reference for PopulatedPlaceEdge
   pageInfo: ConnectionPageInfo

class TRREB_NearbyPopulatedPlacesConnection_Field(NearbyPopulatedPlacesConnection):
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
   distance: IXUFU_distance_Field
   locatedIn: NewType('PopulatedPlace', GQLObject) ## Circular Reference for PopulatedPlace
   nearbyPopulatedPlaces: TRREB_NearbyPopulatedPlacesConnection_Field
   deleted: bool

class PopulatedPlaceEdge(GQLObject):
   cursor: str
   node: PopulatedPlace

class list_PopulatedPlaceEdge(list, PopulatedPlaceEdge): pass

class RegionPopulatedPlacesConnection(GQLObject):
   totalCount: int
   edges: list_PopulatedPlaceEdge[PopulatedPlaceEdge]
   pageInfo: ConnectionPageInfo

class PopulatedPlacesConnection(GQLObject):
   totalCount: int
   edges: list_PopulatedPlaceEdge[PopulatedPlaceEdge]
   pageInfo: ConnectionPageInfo

class LocaleEdge(GQLObject):
   cursor: str
   node: Locale

class list_LocaleEdge(list, LocaleEdge): pass

class LocalesConnection(GQLObject):
   totalCount: int
   edges: list_LocaleEdge[LocaleEdge]
   pageInfo: ConnectionPageInfo

class CurrencyEdge(GQLObject):
   cursor: str
   node: Currency

class list_CurrencyEdge(list, CurrencyEdge): pass

class CurrenciesConnection(GQLObject):
   totalCount: int
   edges: list_CurrencyEdge[CurrencyEdge]
   pageInfo: ConnectionPageInfo

class CountryEdge(GQLObject):
   cursor: str
   node: Country

class list_CountryEdge(list, CountryEdge): pass

class CountriesConnection(GQLObject):
   totalCount: int
   edges: list_CountryEdge[CountryEdge]
   pageInfo: ConnectionPageInfo
