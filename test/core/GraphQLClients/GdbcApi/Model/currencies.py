
from GraphQLClients.GdbcApi.Model.currency import currency
from pygqlmap.components import GQLConnection, GQLEdges


class currencies(GQLConnection): 
    
    def __init__(self):
        super().__init__(GQLEdges(currency())) 
    