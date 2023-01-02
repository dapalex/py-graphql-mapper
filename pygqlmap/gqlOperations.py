from dataclasses import dataclass
from pygqlmap.components import GQLOperation
from pygqlmap.enums import ArgType, OperationType
from pygqlmap.src.gqlInit import queryInit, mutationInit

class GQLQuery(GQLOperation):
    
    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = queryInit

    def __init__(self):
        if hasattr(self, 'args'):
            self._args = self.args
        super().__init__(OperationType.query, self.type, ArgType.LiteralValues)

class GQLMutation(GQLOperation):
    
    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = mutationInit
        
    def __init__(self):
        if hasattr(self, 'args'):
            self._args = self.args
        super().__init__(OperationType.mutation, self.type, ArgType.LiteralValues)
    