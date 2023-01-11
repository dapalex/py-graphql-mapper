from abc import abstractmethod
import logging as logger
from .enums import BuildingType
from ..gql_types import ID
from .utils import get_class_name
from .consts import PRIMITIVES

class Builder():
    @abstractmethod
    def build(self, dataInput, pyObject):
        pass

class QueryBuilder(Builder):
    """  for internal use only    """
    build_sctype: BuildingType
    log_progress: bool

    def __init__(self, build_sctype: BuildingType, log_progress: bool = False):
        self.build_sctype = build_sctype
        self.log_progress = log_progress

        super().__init__()

    def build(self, inputDict: dict, pyObject: any):
        """  for internal use only    """

        try:
            if self.log_progress: logger.info('Started building of python object: ' + get_class_name(pyObject))
            item = inputDict.popitem() ##extract the KV pair containing object name and content

            if not item[1] == None:
                self.set_py_fields(item[1], pyObject)
            else:
                logger.info(item[0] + ' has no content')

        except Exception as ex:
            logger.error('Building of python object failed - ' + ex.args[0])

        return pyObject

    def set_py_fields(self, dataInput, opObject, customObject=None):
        """  for internal use only    """
        newObjDict = opObject.__dataclass_fields__ ##maybe asdict better
        attrToDel = []

        for el in newObjDict:
            try:
                if self.log_progress: logger.info('Started building of field: ' + el)

                if  (not el in opObject.fieldsshow.keys() or not opObject.fieldsshow[el]):
                    if self.log_progress: logger.warning('Field ' + el + ' in ' + opObject + 'not present in fields_show')
                    continue

                if (hasattr(dataInput, el) or el in dataInput.keys()):
                    attrType = type(getattr(opObject, el))
                    if attrType in PRIMITIVES or attrType == ID or attrType == list:
                        self.set_py_field_value(opObject, el, dataInput[el])
                    else:
                        attribute = getattr(opObject, el)
                        if attribute == None:
                            attribute = type(customObject)()
                        if dataInput[el]:
                            if isinstance(dataInput[el], list):
                                setattr(opObject, el, [])
                                listObjectElement = getattr(opObject, el)
                                for subEl in dataInput[el]:
                                    subElObject = attrType()
                                    self.set_py_fields(subEl, subElObject)
                                    listObjectElement.append(subElObject)
                            else:
                                setattr(opObject, el, self.build({ el: dataInput[el] }, attribute))   #, newObject
                        else:
                            self.set_py_field_value(opObject, el, dataInput[el])
                else:
                    self.clean_py_value(opObject, el, attrToDel)

            except Exception as ex:
                logger.error('Setting value for element ' + el + ' failed - ' + ex.args[0])

        for a in attrToDel:
            if a in opObject.__dict__.keys():
                if self.build_sctype == BuildingType.STANDARD:
                    attr = getattr(opObject, a)
                    del attr
                elif self.build_sctype == BuildingType.ALTERCLASS:
                    logger.info('delete attribute from class')
                else:
                    logger.info('should do nothing in new object')

    def set_py_field_value(self, obj, attr, value):
        """  for internal use only    """
        if self.log_progress: logger.info('Setting value of: ' + attr)
        try:
            if obj.fieldsshow:
                if obj.fieldsshow[attr]:
                    if self.build_sctype == BuildingType.STANDARD or self.build_sctype == BuildingType.ALTERCLASS:
                        setattr(obj, attr, value)
                    else:
                        logger.info('new object management')
        except Exception as ex:
            logger.error('Setting value of: ' + attr + ' failed - ' + ex.args[0])

    def clean_py_value(self, obj, field, attrToDel):
        """  for internal use only    """
        if self.log_progress: logger.info('Cleaning value of: ' + field)
        if self.build_sctype == BuildingType.STANDARD:
            setattr(obj, field, None)
        elif self.build_sctype == BuildingType.ALTERCLASS:
            logger.info('alter class to delete field')
            attrToDel.append(field)
        elif self.build_sctype == BuildingType.CREATENEWCLASS:
            logger.info('do nothing in new class')
        else:
            raise Exception('build_sctype not assigned')
