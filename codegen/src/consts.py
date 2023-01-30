
from os import path
import pathlib

CLASS_SIGNATURE = "class %s(GQLObject)"
INTERFACE_SIGNATURE = "class %s(%s)"
ARGUED_CLASS_SIGNATURE = "class %s(%s)"
QUERY_SIGNATURE = "class %s(GQLQuery)"
MUTATION_SIGNATURE = "class %s(GQLMutation)"
ENUM_SIGNATURE = "class %s(Enum)"
SCALAR_SIGNATURE = "%s = %s"
TYPEVAR_SIGNATURE = "%s = TypeVar('%s', bound=%s)"
EMPTY_CLASS_SIGNATURE = "class %s(%s): pass"
GQLLIST_SIGNATURE = "class %s(list, %s): pass"

NEWTYPE_DECLARATION = "NewType('%s', GQLObject)"
TEMPLATE_FOLDER = str(pathlib.Path(path.dirname(__file__), 'templates').absolute())
IMPORT_TEMPLATE = "from .%s import %s"

SCALARS_FILENAME = 'scalars'
ENUMS_FILENAME = 'enums'
TYPES_FILENAME = 'gql_types'
SIMPLE_TYPES_FILENAME = 'gql_simple_types'
MUTATIONS_FILENAME = 'mutations'
QUERIES_FILENAME = 'queries'
TYPE_REFS_FILENAME = 'type_refs'

PY_EXTENSION = '.py'
