from dataclasses import dataclass
from pygqlmap.components import GQLOperation
from pygqlmap.enums import ArgType, OperationType
from pygqlmap.src.gql_init import _query_init, _mutation_init

class GQLQuery(GQLOperation):

    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = _query_init

    def __init__(self):
        if hasattr(self, 'args'):
            self._args = self.args
        super().__init__(OperationType.QUERY, self.type, ArgType.LITERAL_VALUES)

class GQLMutation(GQLOperation):

    def __init_subclass__(cls):
        cls = dataclass(cls)
        cls.__init__ = _mutation_init

    def __init__(self):
        if hasattr(self, 'args'):
            self._args = self.args
        super().__init__(OperationType.MUTATION, self.type, ArgType.LITERAL_VALUES)
