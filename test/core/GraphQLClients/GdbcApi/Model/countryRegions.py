from pygqlmap.components import GQLConnection, GQLEdges

class countryRegions(GQLConnection):
    
    def __init__(self):
        super().__init__(GQLEdges()) 
    