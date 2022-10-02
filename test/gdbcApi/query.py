# from typing import TypedDict
# from .Model.common import DistanceUnit, DisplayOptions, Location, IncludeDeletedFilterType
# from .Model.timeZones import TimeZonesConnection
# from .Model.timeZone import TimeZone
# from .Model.populatedPlaces import PopulatedPlacesConnection
# from .Model.populatedPlace import PopulatedPlace
# from .Model.locales import LocalesConnection
# from .Model.currencies import CurrenciesConnection
# from .Model.countries import CountriesConnection
# from .Model.country import Country
# from .args import *

# class Query(Type):
#     timeZone = Field(TimeZone,
#         args={ 'id': non_null(ID) }) ## include first: Int, after: String, last: Int, before: String
#     timeZones = Field(TimeZonesConnection,
#         args={ **connection_args() }) ## include first: Int, after: String, last: Int, before: String
#     populatedPlaces = Field(PopulatedPlacesConnection,
#         args={ 'location': Location,
#         # 'latitude': Location.latitude,
#         # 'longitude': Location.longitude,
#             'radius': Float,
#             'distanceUnit': DistanceUnit,
#             'countryIds': list_of(ID),
#             'excludedCountryIds': list_of(ID),
#             'namePrefix': String,
#             'namePrefixDefaultLangResults': Boolean,
#             'minPopulation': Int,
#             'maxPopulation': Int,
#             'timeZoneIds': list_of(ID),
#             'types': list_of(String),
#             'sort': String,
#             **connection_args(),
#             'displayOptions': DisplayOptions,
#             'includeDeleted': IncludeDeletedFilterType }) ## include first: Int, after: String, last: Int, before: String
#     populatedPlace = Field(PopulatedPlace,
#         args={ 'id': ID, 
#                 'displayOptions': DisplayOptions }) ## include first: Int, after: String, last: Int, before: String
#     locales = Field(LocalesConnection,
#         args={ **connection_args() }) ## include first: Int, after: String, last: Int, before: String
#     distanceBetween = Field(Float,
#         args={ 'fromPlaceId': ID,
#                 'toPlaceId': ID,
#                 'distanceUnit': DistanceUnit }) ## include first: Int, after: String, last: Int, before: String
#     currencies = Field(CurrenciesConnection,
#         args={'countryId': ID,
#             **connection_args() }) ## include first: Int, after: String, last: Int, before: String
#     country = Field(Country,
#         args={ 'id': ID,
#                 'displayOptions': DisplayOptions }) ## include first: Int, after: String, last: Int, before: String
#     countries = Field(CountriesConnection,
#         args={  'currencyCode': String,
#                 'namePrefix': String,
#                 'namePrefixDefaultLangResults': Boolean,
#                 **connection_args(),
#                 'displayOptions': DisplayOptions }) ## include first: Int, after: String, last: Int, before: String
