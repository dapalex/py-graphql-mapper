from enum import Enum

class DistanceUnit(Enum):
   """
   DistanceUnit - The unit of distance to use when considering a distance arg (for example, in location-related criteria)

   """
   DEFAULT = None
   KM = 'KM' ##Kilometers
   MI = 'MI' ##Miles

class IncludeDeletedFilterType(Enum):
   """
   IncludeDeletedFilterType - What level of stale data is ok to pull

   """
   DEFAULT = None
   ALL = 'ALL' ##All data, regardless of if/when marked deleted
   SINCE_YESTERDAY = 'SINCE_YESTERDAY' ##Only data not marked deleted before yesterday
   SINCE_LAST_WEEK = 'SINCE_LAST_WEEK' ##Only data not marked deleted before last week
   NONE = 'NONE' ##Only data not marked deleted

class Language(Enum):
   """
   Language - The languages currently supported

   """
   DEFAULT = None
   DE = 'DE' ##German
   EN = 'EN' ##English
   ES = 'ES' ##Spanish
   FR = 'FR' ##French
   IT = 'IT' ##Italian
   PT = 'PT' ##Portuguese
   PT_BR = 'PT_BR' ##Portuguese (Brazil)
   RU = 'RU' ##Russian

class PopulatedPlaceType(Enum):
   """
   PopulatedPlaceType - The populated-place types currently supported

   """
   DEFAULT = None
   ADM2 = 'ADM2' ##A level-2 administrative division (for example, a county)
   CITY = 'CITY' ##A city, town, or village
