from typing import Generic
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gqlTypes import ID
from pygqlmap.src.gqlArgBuiltin import *
from .enums import *
from .scalars import *

class YUFHCdistance_distance_Field(ArguedFloat):
   class floatArgs(GQLArgsSet, GQLObject): 
      toPlaceId: ID
      distanceUnit: DistanceUnit

   _args: floatArgs



class TimeZone(GQLObject):
   id: ID ##NON NULL
   name: str ##NON NULL
   rawUtcOffsetHours: int ##NON NULL
   dateTime: str ##NON NULL
   time: str ##NON NULL

class Locale(GQLObject):
   code: ID ##NON NULL
   name: str ##NON NULL

class Currency(GQLObject):
   countryCodes: ID ##NON NULL
   code: ID ##NON NULL
   symbol: str ##NON NULL
