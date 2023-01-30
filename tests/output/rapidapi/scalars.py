from pygqlmap.gql_types import *

String = str ##The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

Boolean = bool ##The `Boolean` scalar type represents `true` or `false`.

ID = ID ##The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.

Int = int ##The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

DateTime = str ##Our custom date scalar

Float = float ##The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

Any = str ##Dynamic type, returns a value as is.

Upload = str ##The `Upload` scalar type represents a file upload.

name = str
