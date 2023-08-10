from pygqlmap.gql_types import *

String = str ##The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

ID = ID ##The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.

Boolean = bool ##The `Boolean` scalar type represents `true` or `false`.

DateTime = str ##The `DateTime` scalar type represents a DateTime - value as specified by - [iso8601](https://en.wikipedia.org/wiki/ISO_8601).

Float = float ##The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

Int = int ##The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

Date = str ##The `Date` scalar type represents a Date - value as specified by - [iso8601](https://en.wikipedia.org/wiki/ISO_8601).

BigInt = str ##The `BigInt` scalar type represents non-fractional whole numeric values. - `BigInt` is not constrained to 32-bit like the `Int` type and thus is a less - compatible type.

Decimal = str ##The `Decimal` scalar type represents a python Decimal.

JSONString = str ##Allows use of a JSON String for input / output from the GraphQL schema. -  - Use of this type is *not recommended* as you lose the benefits of having a defined, static - schema (one of the key benefits of GraphQL).

Upload = str ##Create scalar that ignores normal serialization/deserialization, since - that will be handled by the multipart request spec

GenericScalar = str ##The `GenericScalar` scalar type represents a generic - GraphQL scalar value that could be: - String, Boolean, Int, Float, List or Object.
