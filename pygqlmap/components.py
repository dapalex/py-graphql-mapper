import copy
from dataclasses import asdict, dataclass, field
import inspect

from .src.components import GQLCPPageInfo, GQLEdge, FSTree
from .src.base import GQLList, FieldsShow, GQLExporter, GQLBaseArgsSet
from .src.consts import commaConcat
from .src.utils import addTupleUniqueElement, getDotNotationInfo, getClassName, mergeTupleUniqueElements
from .enums import ArgType, OperationType
from .src.translator import Translate

class GQLOperationArgs(GQLBaseArgsSet):
    location: str
    arguments: dict[str, dict]
    
    def setArgKey(self, fieldName, fieldValue):
        output = '$' + Translate.toGraphQLFieldName(fieldName)
        if not fieldValue is None: output += ': ' + Translate.toGraphQLType(fieldValue)
        output += commaConcat
        return output
    
    @property
    def updateArg(self, key, value):
        """Updates an existing argument

        Args:
            key: name of the argument
            value: value of the argument, it can be a scalar mapped type or a dict for structured objects

        Raises:
            Exception: if key not present
            Exception: if key not valid
        """
        try:
            if key in self.arguments[self.location].keys():
                    self.arguments[self.location][key] = value
            else:
                raise Exception("Key not present") 
        except:
            raise Exception("Key not valid")            
    
    @property
    def exportGQLArgKeys(self):
        """ For internal use only """
        output = ''
        try: 
            for argSet in self.arguments.values():
                for argKey, argValue in argSet.arguments.items():
                    try:  
                        output += self.setArgKey(argKey, argValue)
                    except:
                        raise Exception('Issue exporting arg key for: ' + argKey, argValue)
        except Exception as ex:
            raise Exception('Issue with items exporting arg keys: ' + ex.args[0])

        return output

    @property
    def exportGQLVariables(self):
        """Return the json variables to send to a server

        Returns:
            str: json variables exported 
        """
        output = ''
        try: 
            for argSet in self.arguments.values():
                for argKey, argValue in argSet.arguments.items():
                    try: 
                        output += ', ' if output.startswith('{') else '{ '
                        output += '\"' + Translate.toGraphQLFieldName(argKey) +  '\"' 
                        
                        if not argValue is None:  output += ': ' + Translate.toGraphQLValue(argValue)
                    except:
                        raise Exception('Issue exporting variable for: ' + argKey, argValue)
        except:
            raise Exception('Issue with items exporting variable')
        
        output += ' }'
        return output

class GQLArgsSet(GQLBaseArgsSet):

    def __init__(self, location=''):
        self.location = location
        super().__init__()
    
    def setArgKey(self, fieldName, fieldValue):
        """ For internal use only """
        output = Translate.toGraphQLFieldName(fieldName) + ': $' + Translate.toGraphQLFieldName(fieldName) 
        output += commaConcat
        return output
    
    def addArg(self, argKey, argValue):
        """Add a single argument in the argument set

        Args:
            argKey: name of the argument
            argValue: value of the argument, it can be a scalar mapped type or a dict for structured objects

        Raises:
            Exception: if the argument name is already present
        """
        if not argKey in self.arguments.keys():
            self.arguments.update({ argKey : argValue })
        else:
            raise Exception('argument name: ' + argKey + ' already present!')

    def addArgs(self, args: dict):
        """_summary_

        Args:
            args (dict): _description_
        """
        self.arguments.update(args)

    def removeArg(self, key):
        """ Not tested yet """
        if not self.arguments:
            raise Exception('No arguments')
        self.arguments.pop(key)

    @property
    def exportGQLArgsAndValues(self):
        """ For internal use only """
        output = ''
        
        try: 
            for argKey, argValue in self.arguments.items():
                try:
                    output += Translate.toGraphQLFieldName(argKey)
                    output += ': ' + Translate.toGraphQLValue(argValue)
                    output += commaConcat 
                except:
                    raise Exception('Issue exporting arg and value for: ' + argKey, argValue)
        except:
            raise Exception('Issue with items exporting args and values')

        output = output.removesuffix(commaConcat)

        return output

@dataclass
class GQLObject(FieldsShow, GQLExporter): 
      
    def __init_subclass__(cls):
        cls = dataclass(cls)
        
    def __post_init__(self, logProgress: bool = False):
        self.initFieldsShow()
        self.logProgress = logProgress
    
    def setArgs(self, args: GQLArgsSet, argsType: ArgType):
        """ For internal use only """
        self._args = args
        self._argsType = argsType
     
class GQLEdges(GQLList):
    """ For internal use only """
    
    def __init__(self, sampleNode=None):
        edge = GQLEdge()
        if sampleNode:
            edge.setNodeType(sampleNode)
        else:
            edge.fieldsShow['node'] = False
        super().__init__(edge)
        self.prepareEmptyStructure()
    
    def prepareEmptyStructure(self):
        """ For internal use only """
        edge = self.sampleElement
        if hasattr(edge, 'sampleNode'):
            edge.node = edge.sampleNode
        self.append(edge)
        
@dataclass
class GQLConnection(FieldsShow):
    edges: field(default_factory=GQLEdges, init=True)
    totalCount: field(default_factory=int, init=True) = 0
    pageInfo: field(default_factory=GQLCPPageInfo, init=True) = GQLCPPageInfo()
    gqlExportedArgsTuple = ()
    
    def __init_subclass__(cls):
        cls = dataclass(cls)
    
    def __post_init__(self):
        self.initFieldsShow()
        self.gqlExportedArgsTuple = ()
        
    def setArgs(self, args: GQLArgsSet, argsType: ArgType):
        """ For internal use only """
        self._args = args
        self._argsType = argsType
     
    def findContainer(self, path):
        """ For internal use only """
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
       
    @property
    def exportGqlSource(self):  
        """Return the GraphQL syntax for the current connection

        Returns:
            str: GraphQL Query exported 
        """
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
                            gqlSource, tempExportedArgsTuple = currentList[i].exportGqlSource
                            self.gqlExportedArgsTuple = mergeTupleUniqueElements(self.gqlExportedArgsTuple, tempExportedArgsTuple)
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
            if self._argsType == ArgType.LiteralValues:
                    gqlArgs = '(' + self._args.exportGQLArgsAndValues + ')'
            elif self._argsType == ArgType.Variables:
                    gqlArgs = '(' + self._args.exportGQLArgKeys + ')'
            self.gqlExportedArgsTuple = addTupleUniqueElement(self.gqlExportedArgsTuple, gqlArgs)
           
        gqlResult = gqlArgs + Translate.graphQLize(str(outputGqlDict), self.gqlExportedArgsTuple)
        
        return gqlResult, self.gqlExportedArgsTuple
      
class GQLOperation(GQLExporter): 
    name: str
    operationType: OperationType
    obj: any 
    
    def __init__(self, operationType: OperationType, dataType, operationName: str = '', logProgress: bool = False):
        """_summary_

        Args:
            operationType (OperationType): _description_
            dataType (_type_): _description_
            hasArgsAsInput (bool, optional): _description_. Defaults to True.
            name (str, optional): _description_. Defaults to 'myQuery'.
            logProgress (bool, optional): _description_. Defaults to False.

        Raises:
            Exception: _description_
        """
        self.name = operationName
        
        self.operationType = operationType
        self.obj = dataType() 
        self.fieldsShowTree = FSTree(self.obj)
        self.logProgress = logProgress
    
    def setShow(self, keys: str or list[str], isVisible: bool):
        """_summary_

        Args:
            keys (strorlist[str]): GraphQL field path or list of GraphQL field paths
            isVisible (bool): set visibility (default at true)

        Raises:
            Exception: _description_
        """
        kType = type(keys)
        if kType == str:
            self.fieldsShowTree.setFieldShow(keys, isVisible)
        elif kType == list:
            print('list of keys with same value')
            for key in keys:
                self.fieldsShowTree.setFieldShow(key, isVisible)
        else:
            raise Exception('setShow accepts only ''str'' or ''list'' types') ##why not throwing?
    
    def setArgs(self, argSets: GQLArgsSet, argsType: ArgType):
        """Integrates arguments into the operation
        """
        
        self._args = GQLOperationArgs()
        if hasattr(argSets, '__iter__'): 
            for mainArgs in argSets:
                self._args.arguments.update({ mainArgs.location: mainArgs })
        else:
            self._args.arguments = { argSets.location: argSets }
            
        self._argsType = argsType
            
        if hasattr(argSets, '__iter__'): 
            for args in argSets:
                self.injectArgsSet(args, argsType)
        else:
            self.injectArgsSet(argSets, argsType)
            
    def injectArgsSet(self, args, argsType):
        """ For internal use only """
        for locationKey, argsSet in self._args.arguments.items():
            attrContainer = self.obj
            
            if locationKey:
                    owner = getDotNotationInfo(locationKey)
                    if owner[0]:
                        while owner[0] and (pathStep := owner[0].pop(0)):
                            if pathStep == getClassName(self.obj): continue
                            if pathStep == 'edges': attrContainer = attrContainer.findContainer(owner[0])
                            else: attrContainer = getattr(attrContainer, pathStep)
                                
                        attrContainer = getattr(attrContainer, owner[1])
                    
            attrContainer.setArgs(copy.deepcopy(argsSet), argsType)
     
    @property
    def exportGqlSource(self):
        """Return the GraphQL syntax for the current operation

        Returns:
            str: GraphQL Query exported 
        """
        prefix = self.operationType.name + ' ' + self.name + ' ' 
        self.obj.logProgress = self.logProgress
        
        if hasattr(self, '_args'):
            if self._argsType == ArgType.Variables:
                prefix += '(' + self._args.exportGQLArgKeys + ')'
        return prefix + ' { ' + getClassName(self.obj) + self.obj.exportGqlSource[0] + ' } '
    