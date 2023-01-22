from typing import TypeVar, List
from pygqlmap.components import GQLObject
from pygqlmap.gql_types import ID

NonNull_int = int
NonNull_float = float
NonNull_bool = bool
NonNull_str = str
NonNull_List = List
NonNull_ID = ID


RegionPopulatedPlacesConnection = TypeVar('RegionPopulatedPlacesConnection', bound=GQLObject)
