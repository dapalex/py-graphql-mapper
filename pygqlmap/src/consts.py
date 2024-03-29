from pygqlmap.gql_types import ID

PRIMITIVES = (int, str, bool, float, type(None))

GQL_BUILTIN = (int, str, bool, float, type(None), ID)

STRING_PRIMITIVES = ('int', 'str', 'bool', 'float', 'NoneType')

STRING_GQL_BUILTIN = ('int', 'str', 'bool', 'float', 'None', 'ID')

STRING_GQLLIST_BUILTIN = ('int', 'str', 'bool', 'float', 'None', 'ID', 'Any')

COMMA_CONCAT = ', '

ARGS_DECLARE = '_args'

NON_NULL_PREFIX = 'NonNull_'

GQLLIST_PREFIX = 'list_'

ARGUED_SIGNATURE_SUFFIX = '_Field'