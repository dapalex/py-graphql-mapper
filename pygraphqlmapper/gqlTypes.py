import copy
from dataclasses import asdict, dataclass, field
import inspect
from components import FSTree, GQLList, FieldsShow, GQLExporter, GQLBaseArgs
from enums import ArgLocation, ArgType, OperationType
from utils import getDotNotationInfo, graphQLize, getClassName

class ID(str):
    def isascii(self):
        return super().isascii()
    
class GQLArg():
    name: str
    value: any
    
    def __init__(self, name, value):
        self.name = name
        self.value = value

class GQLArgs(GQLBaseArgs):

    def __init__(self, location=None):
        super().__init__(location)
    
    def addArg(self, arg: GQLArg):
        self.arguments.append(arg)

    def removeArg(self, key):
        if not self.arguments:
            raise Exception('No arguments')
        self.arguments.pop(key)

class GQLPaginationArgs(GQLBaseArgs):

    def __init__(self):
        self.append(('after', ''))
        self.append(('before', ''))
        self.append(('first', 0))
        self.append(('last', 0))

@dataclass
class GQLCPPageInfo(FieldsShow, GQLExporter):
    startCursor: field(default_factory=int, init=True) = 0
    endCursor: field(default_factory=int, init=True) = 0
    hasNextPage: field(default_factory=bool, init=True) = True
    hasPreviousPage: field(default_factory=bool, init=True) = True
    
    def __post_init__(self, logProgress: bool = False):
        self.initFieldsShow()
        self.logProgress = logProgress
        
@dataclass
class GQLObject(FieldsShow, GQLExporter): 
      
    def __init_subclass__(cls):
        cls = dataclass(cls)
        
    def __post_init__(self, logProgress: bool = False):
        self.initFieldsShow()
        self.logProgress = logProgress
    
    def setArgs(self, args: GQLArgs, argsType: ArgType):
        self._args = args
        self._args.scope = ArgLocation.Data
        self._argsType = argsType
     
@dataclass
class GQLEdge(FieldsShow, GQLExporter):
    cursor: field(default_factory=str, init=True) = ''
    node: field(init=True) = None

    def __post_init__(self, logProgress: bool = False):
        self.initFieldsShow()
        self.logProgress = logProgress
        
    def setNodeType(self, sampleNode):
        self.sampleNode = sampleNode
    
class GQLEdges(GQLList):
    
    def __init__(self, sampleNode=None):
        edge = GQLEdge()
        if sampleNode:
            edge.setNodeType(sampleNode)
        else:
            edge.fieldsShow['node'] = False
        super().__init__(edge)
        self.prepareEmptyStructure()
    
    def prepareEmptyStructure(self):
        edge = self.sampleElement
        if hasattr(edge, 'sampleNode'):
            edge.node = edge.sampleNode
        self.append(edge)
        
@dataclass
class GQLConnection(FieldsShow):
    edges: field(default_factory=GQLEdges, init=True)
    totalCount: field(default_factory=int, init=True) = 0
    pageInfo: field(default_factory=GQLCPPageInfo, init=True) = GQLCPPageInfo()
    
    def __init_subclass__(cls):
        cls = dataclass(cls)
        
    def __post_init__(self):
        self.initFieldsShow()
    
    def setArgs(self, args: GQLArgs, argsType: ArgType):
        # if not hasattr(self, '_args'):
        #     self._args = GQLArgs()
        self._args = args
        self._args.scope = ArgLocation.Data
        self._argsType = argsType
     
    def findContainer(self, path):
        attrContainer = self
        
        for p in path:
            if len(self.edges) > 0:
                attrContainer = self.edges[0]                  
            elif self.edges.sampleElement.sampleNode:
                if p == getClassName(self.edges.sampleElement.sampleNode):
                    attrContainer = self.edges.sampleElement.sampleNode
                else:
                    attrContainer = self.edges.sampleElement     
        
        return attrContainer
       
    def moveForward(self, first: int, after: str):
        self.args.first = first
        self.args.after = after
        
    def moveBackward(self, last: int, before: str):
        self.args.last = last
        self.args.before = before

    @property
    def exportGqlSource(self):        
        gqlDict = asdict(self)
        outputGqlDict = {}
                
        for field in gqlDict.keys():
            if self.fieldsShow[field]:
            #List management START
                if list in inspect.getmro(type(getattr(self, field))):
                    currentList = getattr(self, field)
                    innerList = []
                    for i in range(len(currentList)): #it will be 1
                        if GQLExporter in inspect.getmro(type(currentList[i])):
                            gqlSource, gqlArgsList = currentList[i].exportGqlSource
                            if gqlSource:
                                innerList.append(gqlSource)
                    
                    if innerList:
                        outputGqlDict[field] = innerList
                #List management END
                elif FieldsShow in inspect.getmro(type(getattr(self, field))):
                    outputGqlDict[field], gqlArgs = getattr(self, field).exportGqlSource
                else:
                    outputGqlDict[field] = gqlDict[field]
        
        gqlArgs = ''     
        if hasattr(self, '_args'):
            if self._argsType == ArgType.EmbeddedArgs:
                    gqlArgs = self._args.exportGQLArgsAndValues
            elif self._argsType == ArgType.Variables:
                    gqlArgs = self._args.exportGQLArgKeys
            if not gqlArgsList.__contains__(gqlArgs): gqlArgsList.append(gqlArgs)
            
        gqlResult = gqlArgs + graphQLize(str(outputGqlDict), gqlArgsList)
        
        return gqlResult, gqlArgsList
      
class GQLOperation(GQLExporter): 
    name: str
    operationType: OperationType
    data: any #object or connection, should implement FieldsShow
    
    def __init__(self, operationType: OperationType, dataType, name: str = 'myQuery', logProgress: bool = False):
        self.name = name
        self.operationType = operationType
        self.data = dataType()
        self.fieldsShowTree = FSTree(self.data)
        self.logProgress = logProgress
    
    def setShow(self, keys: str or list[str], value: bool):
        kType = type(keys)
        if kType == str:
            self.fieldsShowTree.setFieldShow(keys, value)
        elif kType == list:
            print('list of keys with same value')
            for key in keys:
                self.fieldsShowTree.setFieldShow(key, value)
        else:
            raise Exception('setShow accepts only ''str'' or ''list'' types') ##why not throwing?
    
    def setArgs(self, argSets: list[GQLArgs], argsType: ArgType):
        self._args = GQLArgs()
        self._args.arguments = [mainArgs.arguments for mainArgs in argSets] if hasattr(argSets, '__iter__') else argSets.arguments
        self._args.scope = ArgLocation.Operation
        self._argsType = argsType
        
        if hasattr(argSets, '__iter__'):
            for args in argSets:
                self.injectArgsSet(args, argsType)
        else:
            self.injectArgsSet(argSets, argsType)
            
    def injectArgsSet(self, args, argsType):
        """ For internal use only """
        attrContainer = self.data
        if args.location:
                owner = getDotNotationInfo(args.location)
                if owner[0]:
                    while owner[0] and (pathStep := owner[0].pop(0)):
                    # for pathStep in owner[0]:
                        if pathStep == getClassName(self.data):
                            continue
                        if pathStep == 'edges':
                            attrContainer = attrContainer.findContainer(owner[0])
                        else: 
                            attrContainer = getattr(attrContainer, pathStep)
                            
                    attrContainer = getattr(attrContainer, owner[1])
            
        attrContainer.setArgs(copy.deepcopy(args), argsType)
     
    @property
    def exportGqlSource(self):
        prefix = self.operationType.name + ' ' + self.name + ' ' 
        if hasattr(self, '_args'):
            if self._argsType == ArgType.Variables:
                prefix += self._args.exportGQLArgKeys
        self.data.logProgress = self.logProgress
        return prefix + ' { ' + getClassName(self.data) + self.data.exportGqlSource[0] + ' } '
        