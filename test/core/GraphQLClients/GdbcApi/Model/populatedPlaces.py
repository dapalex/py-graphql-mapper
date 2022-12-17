from pygqlmap.components import GQLObject

class PopulatedPlaces(GQLObject):
    totalCount: int
    
    def __init__(self):
        self.totalCount = 0
        super().__init__()  