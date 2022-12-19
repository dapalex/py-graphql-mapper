from typing import Generic
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gqlTypes import ID
from pygqlmap.src.gqlArgBuiltin import *
from .enums import *
from .scalars import *

class distanceField(ArguedFloat):
   class Args(GQLArgsSet, GQLObject): 
      toPlaceId: ID
      distanceUnit: DistanceUnit

   _args: Args



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
