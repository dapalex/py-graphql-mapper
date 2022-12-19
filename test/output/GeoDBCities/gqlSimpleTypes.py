from typing import Generic
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gqlTypes import ID
from pygqlmap.src.gqlArgBuiltin import *
from .enums import *
from .scalars import *

class distanceField(ArguedFloat):
   """
   distanceField - The distance result from some location-based query
This field has two forms:
- As a property (e.g., place.distance), returns the distance as part of a query returning places sorted by distance.
- As a function (e.g., place.distance(toPlaceId), returns the distance to the specified place.

   """
   class Args(GQLArgsSet, GQLObject): 
      """
      toPlaceId - The distance to this place

      distanceUnit - The unit of distance to use

      """
      toPlaceId: ID
      distanceUnit: DistanceUnit

   _args: Args



class TimeZone(GQLObject):
   """
   TimeZone - A time-zone

   """
   id: ID ##NON NULL
   name: str ##NON NULL
   rawUtcOffsetHours: int ##NON NULL
   dateTime: str ##NON NULL
   time: str ##NON NULL

class Locale(GQLObject):
   """
   Locale - A regional locale representing some country/language combination

   """
   code: ID ##NON NULL
   name: str ##NON NULL

class Currency(GQLObject):
   """
   Currency - A country currency

   """
   countryCodes: ID ##NON NULL
   code: ID ##NON NULL
   symbol: str ##NON NULL
