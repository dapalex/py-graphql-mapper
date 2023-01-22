from pygqlmap.gql_types import ID

Boolean = bool ##Built-in Boolean

Float = float ##Built-in Float

ID = ID ##Built-in ID

Int = int ##Built-in Int

String = str ##Built-in String

distance = float ##The distance result from some location-based query - This field has two forms: - - As a property (e.g., place.distance), returns the distance as part of a query returning places sorted by distance. - - As a function (e.g., place.distance(toPlaceId), returns the distance to the specified place.
