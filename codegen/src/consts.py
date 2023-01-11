
from os import path
import pathlib

CLASS_SIGNATURE = "class %s(GQLObject)"
INTERFACE_SIGNATURE = "class %s(%s)"
ARGUED_CLASS_SIGNATURE = "class %s(%s)"
QUERY_SIGNATURE = "class %s(GQLQuery)"
MUTATION_SIGNATURE = "class %s(GQLMutation)"
ENUM_SIGNATURE = "class %s(Enum)"
SCALAR_SIGNATURE = "%s = %s"
TEMPLATE_FOLDER = str(pathlib.Path(path.dirname(__file__), 'templates').absolute())

SCALARS_FILENAME = 'scalars.py'
ENUMS_FILENAME = 'enums.py'
TYPES_FILENAME = 'gql_types.py'
SIMPLE_TYPES_FILENAME = 'gql_simple_types.py'
MUTATIONS_FILENAME = 'mutations.py'
QUERIES_FILENAME = 'queries.py'
CIRCULARREFS_FILENAME = 'circular_refs.py'