from codegen.src.base_class import SchemaTypeManager

class PriorElement():
    name: str
    schemaType: SchemaTypeManager
    codeList: list

    def __init__(self, name, schemaType, codeList):
        self.name = name
        self.schemaType = schemaType
        self.codeList = codeList


class ExtractionResults():
    query_classes: dict
    queries_enum_class: dict
    mutation_classes: dict
    mutations_enum_class:  dict
    simple_type_classes: dict
    type_classes: dict
    enum_classes: dict
    scalar_defs: dict
    type_refs: dict

    def __init__(self):
        self.scalar_defs = {}
        self.enum_classes = {}
        self.simple_type_classes = {}
        self.type_classes = {}
        self.query_classes = {}
        self.queries_enum_class = {}
        self.mutation_classes = {}
        self.mutations_enum_class = {}
        self.type_refs = {}
