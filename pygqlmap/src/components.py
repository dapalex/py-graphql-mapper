
from dataclasses import dataclass, field
import inspect
from .utils import getClassName, getDotNotationInfo, isNoneOrBuiltinPrimitive
from .base import FieldsShow, GQLExporter


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
class GQLEdge(FieldsShow, GQLExporter):
    cursor: field(default_factory=str, init=True) = ''
    node: field(init=True) = None

    def __post_init__(self, logProgress: bool = False):
        self.initFieldsShow()
        self.logProgress = logProgress
        
    def setNodeType(self, sampleNode):
        self.sampleNode = sampleNode
    
class FSTree():
    def __init__(self, obj, fieldName: str = None):
        if list in inspect.getmro(type(obj)):
            self.name = fieldName if fieldName else 'dummyList'
            if hasattr(obj, 'fieldsShow'):
                self.fieldsShow = obj.fieldsShow
            for element in obj:
                if isNoneOrBuiltinPrimitive(element): continue
                if hasattr(element, 'fieldsShow'):
                    if not hasattr(element, 'children'): self.children = []
                    self.children.append(FSTree(element))
        else:
            self.name =  fieldName if fieldName else getClassName(obj)
            if hasattr(obj, 'fieldsShow'):
                self.fieldsShow = obj.fieldsShow
                for field in obj.fieldsShow.keys():
                    objField = getattr(obj, field)
                    if isNoneOrBuiltinPrimitive(objField): continue
                    if not hasattr(self, 'children'): self.children = []
                    self.children.append(FSTree(objField, field))
        
    #  ##connection stuff......
    # def getFSEdgeContainer(self):
    #     for childBranch in self.children:
    #         if childBranch.name == 'GQLEdge':
    #             return childBranch       
          
    def setFieldShow(self, property: str, show: bool):
        info = getDotNotationInfo(property)
        path = info[0]
        field = info[1]
        
        if len(path) == 0:
            print('trying to hide the entire object...')
            return
        
        attrContainer = self.findBranchContainer(path)
        if field in attrContainer.fieldsShow.keys():
            attrContainer.fieldsShow[field] = show
        else: 
            raise Exception('field ' + field + ' not found!')
       
    def findBranchContainer(self, path: str):
        attrContainer = self
        
        while len(path):
            field = path.pop(0)
            if attrContainer.name == field: ##container object
                continue
            for child in attrContainer.children:
                if child.name == field:  
                    attrContainer = child
        return attrContainer
        