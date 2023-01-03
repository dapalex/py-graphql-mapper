
from os import path
import pathlib

classSignature = "class %s(GQLObject)"
interfaceSignature = "class %s(%s)"
arguedClassSignature = "class %s(%s)"
querySignature = "class %s(GQLQuery)"
mutationSignature = "class %s(GQLMutation)"
enumSignature = "class %s(Enum)"
scalarSignature = "%s = %s"
templateFolder = str(pathlib.Path(path.dirname(__file__), 'templates').absolute())