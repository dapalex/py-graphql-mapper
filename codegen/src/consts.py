
from os import path

classSignature = "class %s(GQLObject)"
interfaceSignature = "class %s(%s)"
arguedClassSignature = "class %s(%s)"
querySignature = "class %s(GQLQuery)"
mutationSignature = "class %s(GQLMutation)"
enumSignature = "class %s(Enum)"
scalarSignature = "%s = %s"
templateFolder = path.dirname(__file__) + '\\templates\\'