from dataclasses import asdict
from components import GQLList
from enums import BuildingType
from gqlTypes import GQLEdges
from logger import Logger
from utils import getClassName, popListElementByRef #uhm

class Builder():
    """  for internal use only    """
    buildType: BuildingType
    logProgress: bool
    
    def __init__(self, buildType: BuildingType, logProgress: bool = False):
        self.buildType = buildType
        self.logProgress = logProgress
        
    def buildPyObject(self, input, queryObject: any):
        """  for internal use only    """
        
        if self.logProgress: Logger.logInfoMessage('Started building of python object: ' + getClassName(queryObject))
        
        if type(queryObject) == GQLList:
            print('management of list')
        if type(queryObject) == GQLEdges:
            item = input.popitem()
            
            ##building response using query object, query object has to be cleaned
            popListElementByRef(queryObject, queryObject.sampleElement)
            
            for inputElement in item[1]:
                newObjElement = type(queryObject.sampleElement)()
                newObjElement.copyFieldsShow(queryObject.sampleElement.fieldsShow)
                if hasattr(queryObject.sampleElement, 'sampleNode'):
                    self.setPyFields(inputElement, newObjElement, queryObject.sampleElement.sampleNode)
                else:
                    self.setPyFields(inputElement, newObjElement)
                queryObject.append(newObjElement)
        else: 
            item = input.popitem() ##extract the KV pair containing object name and content
            self.setPyFields(item[1], queryObject)
        
        return queryObject

    def setPyFields(self, input, queryObject, customObject=None):
        """  for internal use only    """
        newObjDict = queryObject.__dataclass_fields__ ##maybe asdict better
        attrToDel = []
        
        for el in newObjDict:
            if self.logProgress: Logger.logInfoMessage('Started building of field: ' + el)
            
            if (hasattr(input, el) or el in input.keys()) and (el in queryObject.fieldsShow.keys() and queryObject.fieldsShow[el]):
                attrType = type(getattr(queryObject, el))
                if attrType == int or attrType == str or attrType == float or attrType == bool or attrType == list:
                    self.setFieldValue(queryObject, el, input[el])
                else:
                    attribute = getattr(queryObject, el)
                    if attribute == None:
                        attribute = type(customObject)()
                    if input[el]:
                        setattr(queryObject, el, self.buildPyObject({ el: input[el] }, attribute))   #, newObject
                    else:
                        self.setFieldValue(queryObject, el, input[el])
            #if the attribute is not present in the content there is no reason to keep the field
            #check anyway fieldsShow
            # elif el in queryObject.fieldsShow.keys() and not queryObject.fieldsShow[el]: 
            #     self.cleanValue(queryObject, el, attrToDel)
            else: 
                self.cleanValue(queryObject, el, attrToDel)
                       
        for a in attrToDel:
            if a in queryObject.__dict__.keys():
                if self.buildType == BuildingType.Standard:
                    attr = getattr(queryObject, a)
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
            if self.logProgress: 
                Logger.logErrorMessage('Setting value of: ' + attr + ' failed')
                Logger.logErrorMessage(str(ex))
            print(str(ex))
            
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