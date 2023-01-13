from pygqlmap.gql_types import ID

PRIMITIVES = (int, str, bool, float, type(None))

GQL_BUILTIN = (int, str, bool, float, type(None), ID)

STRING_PRIMITIVES = ('int', 'str', 'bool', 'float', 'NoneType')

COMMA_CONCAT = ', '

ARGS_DECLARE = '_args'

ARGUED_SIGNATURE_SUFFIX = '_Field'