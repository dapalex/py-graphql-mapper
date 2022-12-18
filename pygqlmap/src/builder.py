from abc import abstractmethod
from .base import GQLList
from .enums import BuildingType
# from ..components import GQLEdges
from ..gqlTypes import ID
from .logger import Logger
from .utils import getClassName, popListElementByRef #uhm
from .consts import primitives

class Builder():
    @abstractmethod
    def build(self, input, pyObject):
        pass

class QueryBuilder(Builder, Logger):
    """  for internal use only    """
    buildType: BuildingType
    logProgress: bool
    
    def __init__(self, buildType: BuildingType, logProgress: bool = False):
        self.buildType = buildType
        self.logProgress = logProgress
        
        super().__init__()
        
    def build(self, input, pyObject: any):
        """  for internal use only    """
        
        try:
            if self.logProgress: Logger.logInfoMessage('Started building of python object: ' + getClassName(pyObject))
            
            if type(pyObject) == GQLList:
                print('management of list')
            # if type(pyObject) == GQLEdges:
            #     item = input.popitem()
                
            #     ##building response using query object, query object has to be cleaned
            #     popListElementByRef(pyObject, pyObject.sampleElement)
                
            #     for inputElement in item[1]:
            #         newObjElement = type(pyObject.sampleElement)()
            #         newObjElement.copyFieldsShow(pyObject.sampleElement.fieldsShow)
            #         if hasattr(pyObject.sampleElement, 'sampleNode'):
            #             self.setPyFields(inputElement, newObjElement, pyObject.sampleElement.sampleNode)
            #         else:
            #             self.setPyFields(inputElement, newObjElement)
            #         pyObject.append(newObjElement)
            else: 
                item = input.popitem() ##extract the KV pair containing object name and content
                self.setPyFields(item[1], pyObject)
            
        except Exception as ex:
            Logger.logErrorMessage('Building of python object failed - ' + ex.args[0]) 
            
        return pyObject

    def setPyFields(self, input, opObject, customObject=None):
        """  for internal use only    """
        newObjDict = opObject.__dataclass_fields__ ##maybe asdict better
        attrToDel = []
        
        for el in newObjDict:
            try:
                if self.logProgress: Logger.logInfoMessage('Started building of field: ' + el)
                
                if (hasattr(input, el) or el in input.keys()) and (el in opObject.fieldsShow.keys() and opObject.fieldsShow[el]):
                    attrType = type(getattr(opObject, el))
                    if attrType in primitives or attrType == ID or attrType == list:
                        self.setFieldValue(opObject, el, input[el])
                    else:
                        attribute = getattr(opObject, el)
                        if attribute == None:
                            attribute = type(customObject)()
                        if input[el]:
                            setattr(opObject, el, self.build({ el: input[el] }, attribute))   #, newObject
                        else:
                            self.setFieldValue(opObject, el, input[el])
                else: 
                    self.cleanValue(opObject, el, attrToDel)
                    
            except Exception as ex:
                Logger.logErrorMessage('Setting value for element ' + el + ' failed - ' + ex.args[0]) 
                        
        for a in attrToDel:
            if a in opObject.__dict__.keys():
                if self.buildType == BuildingType.Standard:
                    attr = getattr(opObject, a)
                    del attr
                elif self.buildType == BuildingType.AlterClass:
                    print('delete attribute from class')
                else:
                    print('should do nothing in new object')

    def setFieldValue(self, obj, attr, value):
        """  for internal use only    """
        if self.logProgress: Logger.logInfoMessage('Setting value of: ' + attr)
        try:
            if obj.fieldsShow:
                if obj.fieldsShow[attr]:
                    if self.buildType == BuildingType.Standard or self.buildType == BuildingType.AlterClass:
                        setattr(obj, attr, value)
                    else:
                        print('new object management')
        except Exception as ex:
            Logger.logErrorMessage('Setting value of: ' + attr + ' failed - ' + ex.args[0])
            
    def cleanValue(self, object, field, attrToDel):
        if self.logProgress: Logger.logInfoMessage('Cleaning value of: ' + field)
        """  for internal use only    """
        if self.buildType == BuildingType.Standard:
            setattr(object, field, None)
        elif self.buildType == BuildingType.AlterClass:
            print('alter class to delete field')
            attrToDel.append(field)
        elif self.buildType == BuildingType.CreateNewClass:
            print('do nothing in new class')
        else:
            raise Exception('buildType not assigned')     
