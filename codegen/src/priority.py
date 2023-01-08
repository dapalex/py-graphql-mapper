class PriorElement():
    name: str
    schemaType: any
    codeList: list

    def __init__(self, name, schemaType, codeList):
        self.name = name
        self.schemaType = schemaType
        self.codeList = codeList


class ExtractionResults():
    queryClasses: dict
    queriesEnumClass: dict
    mutationClasses: dict
    mutationsEnumClass:  dict
    simpleTypeClasses: dict
    typeClasses: dict
    enumClasses: dict
    scalarDefinitions: dict
    circularRefs: dict

    def __init__(self):
        self.scalarDefinitions = {}
        self.enumClasses = {}
        self.simpleTypeClasses = {}
        self.typeClasses = {}
        self.queryClasses = {}
        self.queriesEnumClass = {}
        self.mutationClasses = {}
        self.mutationsEnumClass = {}
        self.circularRefs = {}
