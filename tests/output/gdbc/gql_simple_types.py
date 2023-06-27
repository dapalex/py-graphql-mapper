from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class CKXYT_distance_Field(ArguedFloat):
   """
   CKXYT_distance_Field - The distance result from some location-based query
This field has two forms:
- As a property (e.g., place.distance), returns the distance as part of a query returning places sorted by distance.
- As a function (e.g., place.distance(toPlaceId), returns the distance to the specified place.

   """
   class floatArgs(GQLArgsSet, GQLObject):
      """
      toPlaceId - The distance to this place

      distanceUnit - The unit of distance to use

      """
      toPlaceId: ID
      distanceUnit: DistanceUnit

   _args: floatArgs



class TimeZone(GQLObject):
   """
   TimeZone - A time-zone

   """
   id: ID
   name: str
   rawUtcOffsetHours: int
   dateTime: str
   time: str

class Locale(GQLObject):
   """
   Locale - A regional locale representing some country/language combination

   """
   code: ID
   name: str

class Currency(GQLObject):
   """
   Currency - A country currency

   """
   countryCodes: NonNull_list[ID]
   code: ID
   symbol: str
