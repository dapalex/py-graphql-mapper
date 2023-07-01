from typing import Generic, List
from pygqlmap.components import GQLArgsSet, GQLObject
from pygqlmap.gql_types import *
from pygqlmap.src.arg_builtin import *
from .enums import *
from .scalars import *
from .type_refs import *

class IITIY_distance_Field(ArguedFloat):
   class floatArgs(GQLArgsSet, GQLObject):
      toPlaceId: ID
      distanceUnit: DistanceUnit

   _args: floatArgs



class TimeZone(GQLObject):
   id: ID
   name: str
   rawUtcOffsetHours: int
   dateTime: str
   time: str

class Locale(GQLObject):
   code: ID
   name: str

class Currency(GQLObject):
   countryCodes: NonNull_list[ID]
   code: ID
   symbol: str
