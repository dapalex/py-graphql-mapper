from typing import Generic, Union
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gqlTypes import ID
from pygqlmap.src.gqlArgBuiltin import *
from typing import NewType
from .gqlSimpleTypes import *
from .enums import *
from .scalars import *
from .circularRefs import *

class Location(GQLObject):
   latitude: float
   longitude: float

class DisplayOptions(GQLObject):
   asciiMode: bool
   language: Language

class ConnectionPageInfo(GQLObject):
   startCursor: str ##NON NULL
   endCursor: str ##NON NULL
   hasNextPage: bool ##NON NULL
   hasPreviousPage: bool ##NON NULL

class TimeZoneEdge(GQLObject):
   cursor: str ##NON NULL
   node: TimeZone ##NON NULL

class TimeZonesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: TimeZoneEdge ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL

class WSZCWpopulatedPlaces_RegionPopulatedPlacesConnection_Field(Generic[RegionPopulatedPlacesConnection]):
   class RegionPopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject): 
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
      includeDeleted: IncludeDeletedFilterType

   _args: RegionPopulatedPlacesConnectionArgs



class CountryRegion(GQLObject):
   fipsCode: ID
   isoCode: ID ##NON NULL
   wikiDataId: ID
   name: str ##NON NULL
   capital: str
   country: NewType('Country', GQLObject) ##NON NULL ## Circular Reference for Country
   numPopulatedPlaces: int
   populatedPlaces: WSZCWpopulatedPlaces_RegionPopulatedPlacesConnection_Field ## Circular Reference for RegionPopulatedPlacesConnection

class CountryRegionEdge(GQLObject):
   cursor: str ##NON NULL
   node: CountryRegion ##NON NULL

class CountryRegionsConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: CountryRegionEdge ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL

class UEFXDregion_CountryRegion_Field(CountryRegion):
   class CountryRegionArgs(GQLArgsSet, GQLObject): 
      code: ID

   _args: CountryRegionArgs



class FGKUEregions_CountryRegionsConnection_Field(CountryRegionsConnection):
   class CountryRegionsConnectionArgs(GQLArgsSet, GQLObject): 
      namePrefix: str
      namePrefixDefaultLangResults: bool
      first: int
      after: str
      last: int
      before: str

   _args: CountryRegionsConnectionArgs



class Country(GQLObject):
   code: ID ##NON NULL
   callingCode: str ##NON NULL
   wikiDataId: ID ##NON NULL
   capital: str
   name: str ##NON NULL
   currencyCodes: str ##NON NULL
   flagImageUri: str ##NON NULL
   numRegions: int ##NON NULL
   region: UEFXDregion_CountryRegion_Field
   regions: FGKUEregions_CountryRegionsConnection_Field

class NearbyPopulatedPlacesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: NewType('PopulatedPlaceEdge', GQLObject) ##NON NULL ## Circular Reference for PopulatedPlaceEdge
   pageInfo: ConnectionPageInfo ##NON NULL

class IQILInearbyPopulatedPlaces_NearbyPopulatedPlacesConnection_Field(NearbyPopulatedPlacesConnection):
   class NearbyPopulatedPlacesConnectionArgs(GQLArgsSet, GQLObject): 
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
      includeDeleted: IncludeDeletedFilterType

   _args: NearbyPopulatedPlacesConnectionArgs



class PopulatedPlace(GQLObject):
   id: ID ##NON NULL
   wikiDataId: ID
   name: str ##NON NULL
   placeType: PopulatedPlaceType ##NON NULL
   elevationMeters: int
   latitude: float
   longitude: float
   population: int ##NON NULL
   timezone: str ##NON NULL
   country: Country ##NON NULL
   region: CountryRegion
   distance: MSQFVdistance_distance_Field
   locatedIn: NewType('PopulatedPlace', GQLObject) ## Circular Reference for PopulatedPlace
   nearbyPopulatedPlaces: IQILInearbyPopulatedPlaces_NearbyPopulatedPlacesConnection_Field
   deleted: bool ##NON NULL

class PopulatedPlaceEdge(GQLObject):
   cursor: str ##NON NULL
   node: PopulatedPlace ##NON NULL

class RegionPopulatedPlacesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: PopulatedPlaceEdge ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL

class PopulatedPlacesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: PopulatedPlaceEdge ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL

class LocaleEdge(GQLObject):
   cursor: str ##NON NULL
   node: Locale ##NON NULL

class LocalesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: LocaleEdge ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL

class CurrencyEdge(GQLObject):
   cursor: str ##NON NULL
   node: Currency ##NON NULL

class CurrenciesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: CurrencyEdge ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL

class CountryEdge(GQLObject):
   cursor: str ##NON NULL
   node: Country ##NON NULL

class CountriesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: CountryEdge ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL
