from pygqlmap import GQLObject

class populatedPlaces(GQLObject):
    totalCount: int
    
    def __init__(self):
        self.totalCount = 0
        super().__init__()  