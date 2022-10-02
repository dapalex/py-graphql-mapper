import enum
# # from graphql import Connection
# from graphql.type import String, Int, Type, list_of, Boolean, Float, Field, Arg, Enum, BaseType, non_null

# class Location(BaseType): 
#     # DD.DDDD from -90 to 90
# 	latitude = Field(float, graphql_name='latitude', args={'latitude': Arg(Float)})
# 	# latitude: Float
# 	# DD.DDDD from -180 to 180
# 	longitude = Field(float, graphql_name='longitude', args={'longitude': Arg(Float)})
# 	# longitude: Float

class IncludeDeletedFilterType(enum.Enum): 
	__choices__ = ('ALL', 'SINCE_YESTERDAY', 'SINCE_LAST_WEEK', 'NONE')
    # All data, regardless of if/when marked deleted
	ALL = 'ALL',
	# Only data not marked deleted before yesterday
	SINCE_YESTERDAY = 'SINCE_YESTERDAY',
	# Only data not marked deleted before last week
	SINCE_LAST_WEEK = 'SINCE_LAST_WEEK',
	# Only data not marked deleted
	NONE = 'NONE'

# class DistanceUnit(Enum): 
# 	__choices__ = ('KM', 'MI')
#     # # Kilometers
#     # KM = 0,	
# 	# # Miles
#     # MI = 1

# class Language(Enum): 
# 	__choices__ = ('DE', 'EN', 'ES', 'FR', 'IT', 'PT', 'PT_BR', 'RU')
#     # # German
#     # DE = 0,	
# 	# # English
#     # EN = 1,	
# 	# # Spanish
#     # ES = 2,	
#     # # French
#     # FR = 3,	
# 	# # Italian
#     # IT = 4,	
# 	# # Portuguese
#     # PT = 5,	
# 	# # Portuguese (Brazil)
#     # PT_BR = 6,	
# 	# # Russian
#     # RU = 7

# class GDBCEdge(Type):
#     cursor: Field(non_null(String), graphql_name='cursor')

# class GDBCConnection(Connection):
#     totalCount: Field(non_null(Int), graphql_name='totalCount')
#     edges: Field(non_null(list_of(GDBCEdge)), graphql_name='edges')
#     ##pageInfo already included with Connection type

# class DisplayOptions(Type):
# 	# Whether to display results using ASCII-only characters
# 	asciiMode: Boolean
	
# 	# What language to display the results in
# 	language: Language

