
from pygqlmap import GQLObject


class currency(GQLObject): 
    countryCodes: list
    code: str
    symbol: str
    
    def __init__(self):
        self.countryCodes = []
        self.code = ''
        self.symbol = ''
        super().__init__()
