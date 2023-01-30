from .utils import get_dot_notation_info, is_none_or_builtin_primitive
import logging as logger

class FSTree():
    def __init__(self, obj, fieldName: str = None):
        self.name =  fieldName if fieldName else obj.__class__.__name__
        if hasattr(obj, 'fieldsshow'):
            self._fieldsshow = obj._fieldsshow
            for field in obj.fieldsshow.keys():
                objField = getattr(obj, field)
                if is_none_or_builtin_primitive(objField): continue
                if not hasattr(self, 'children'): self.children = []
                self.children.append(FSTree(objField, field))

    def set_fieldshow(self, fieldName: str, show: bool):
        info = get_dot_notation_info(fieldName)
        path = info[0]
        field = info[1]

        if len(path) == 0:
            logger.info('trying to hide the entire object...')
            return

        attrContainer = self.findBranchContainer(path)
        if field in attrContainer._fieldsshow.keys():
            attrContainer._fieldsshow[field] = show
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
