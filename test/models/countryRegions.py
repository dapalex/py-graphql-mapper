from gqlTypes import GQLConnection, GQLEdges


# @dataclasses.dataclass
class countryRegions(GQLConnection):
    
    def __init__(self):
        super().__init__(GQLEdges()) 
    