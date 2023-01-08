
import copy
from pygqlmap.src.builder import Builder
from .spSchema import GQLSchema, SCArg, SCType, SCDirective, SCField, SCEnumValue, SCInterface, SCInputField, SCOperationType,  SCArgType, SCOfType,  SCFieldType

class SchemaTypeBuilder(Builder):

    def build(self, dataInput, pyObject):
        inputType = dataInput['__type']

        pyObject = SchemaTypeBuilder.buildType(inputType)

        return pyObject

    def buildTypes(dataInput):
        types = {}
        for typeInput in dataInput:
            types.update({ typeInput["name"]: SchemaTypeBuilder.buildType(typeInput) })

        return types

    def buildType(dataInput):
        schemaType = SCType()
        if not dataInput: return None
        try:

            while len(dataInput.items()) > 0:
                try:
                    inputField = dataInput.popitem()
                    if inputField[0] == 'ofType':
                        schemaType.ofType = SchemaTypeBuilder.buildOfType(inputField[1]) if inputField[1] else None
                    elif inputField[0] == 'fields':
                        # type.fields = SchemaTypeBuilder.buildTypeFields(inputField[1]) if inputField[1] else None
                        schemaType.fields = list(map(SchemaTypeBuilder.buildTypeField, inputField[1])) if inputField[1] else None
                    elif inputField[0] == 'interfaces':
                        # type.interfaces = SchemaTypeBuilder.buildTypeInterfaces(inputField[1]) if inputField[1] else None
                        schemaType.interfaces =list(map(SchemaTypeBuilder.buildTypeInterface, inputField[1])) if inputField[1] else None
                    elif inputField[0] == 'enumValues':
                        # type.enumValues = SchemaTypeBuilder.buildTypeEnumValues(inputField[1]) if inputField[1] else None
                        schemaType.enumValues =list(map(SchemaTypeBuilder.buildTypeEnumValue, inputField[1])) if inputField[1] else None
                    elif inputField[0] == 'possibleTypes':
                        schemaType.possibleTypes = SchemaTypeBuilder.buildTypes(inputField[1]) if inputField[1] else None
                    elif inputField[0] == 'inputFields':
                        schemaType.inputFields = SchemaTypeBuilder.buildInputFields(inputField[1]) if inputField[1] else None
                    else:
                        setattr(schemaType, inputField[0], inputField[1])
                except Exception as ex:
                    raise Exception("Error during extraction of inputField" + ' - ' + ex.args[0])
        except Exception as ex:
            raise Exception("Exception during Schema Type building" + ' - ' + ex.args[0])

        return schemaType

    def buildOfType(dataInput):
        field = SCOfType()

        try:
            while len(dataInput.items()) > 0:
                fieldField = dataInput.popitem()
                if fieldField[0] == 'ofType' and fieldField[1]: ##SKIPPING NON NULL MANAGEMENT, it will be back!
                    return  SchemaTypeBuilder.buildOfType(fieldField[1])
                else:
                    setattr(field, fieldField[0], fieldField[1])

        except Exception as ex:
            raise Exception("Exception during OfType building" + ' - ' + ex.args[0])

        return field

    def buildFieldType(dataInput):
        field = SCFieldType()

        try:
            while len(dataInput.items()) > 0:
                fieldField = dataInput.popitem()
                if fieldField[0] == 'ofType':
                    field.ofType = SchemaTypeBuilder.buildOfType(fieldField[1]) if fieldField[1] else None
                else:
                    setattr(field, fieldField[0], fieldField[1])

        except Exception as ex:
            raise Exception("Exception during Field Type building" + ' - ' + ex.args[0])

        return field

    def buildTypeField(dataInput):
        field = SCField()

        try:

            while len(dataInput.items()) > 0:
                fieldField = dataInput.popitem()
                if fieldField[0] == 'args':
                    field.args = SchemaTypeBuilder.buildArgsOrInputFields(fieldField[1], False) if fieldField[1] else None
                elif fieldField[0] == 'type':
                    field.type = SchemaTypeBuilder.buildFieldType(fieldField[1])
                else:
                    setattr(field, fieldField[0], fieldField[1])

        except Exception as ex:
            raise Exception("Exception during Type Field building" + ' - ' + ex.args[0])

        return field

    def buildTypeInterface(dataInput):
        interface = SCInterface()

        try:

            while len(dataInput.items()) > 0:
                enumValue = dataInput.popitem()
                setattr(interface, enumValue[0], enumValue[1])

        except Exception as ex:
            raise Exception("Exception during Type Interface building" + ' - ' + ex.args[0])

        return interface

    def buildArgsOrInputFields(dataInput, isInputField):
        args = []
        for inputArg in dataInput:
            obj = SCInputField() if isInputField else SCArg()
            while len(inputArg.items()) > 0:
                inputArgField = inputArg.popitem()
                setattr(obj, inputArgField[0], SchemaTypeBuilder.buildArgType(inputArgField[1]) if inputArgField[0] == 'type' else inputArgField[1])

            currentObj = copy.deepcopy(obj)
            args.append(currentObj)
        return args

    def buildInputFields(dataInput):
        return SchemaTypeBuilder.buildArgsOrInputFields(dataInput, True)

    def buildArgType(dataInput):
        field = SCArgType()

        try:
            while len(dataInput.items()) > 0:
                fieldField = dataInput.popitem()
                setattr(field, fieldField[0], SchemaTypeBuilder.buildArgType(fieldField[1]) if fieldField[0] == 'ofType' and fieldField[1] else fieldField[1])

        except Exception as ex:
            raise Exception("Exception during Arg Type building" + ' - ' + ex.args[0])

        return field

    def buildTypeEnumValue(dataInput):
        scEnumValue = SCEnumValue()

        try:

            while len(dataInput.items()) > 0:
                enumValue = dataInput.popitem()
                setattr(scEnumValue, enumValue[0], enumValue[1])

        except Exception as ex:
            raise Exception("Exception during Type Enum Value building" + ' - ' + ex.args[0])

        return scEnumValue

class SchemaBuilder(Builder):

    def build(self, dataInput, pyObject: GQLSchema):
        inputSchema = dataInput['__schema']

        while len(inputSchema.items()) > 0:
            data = inputSchema.popitem()
            if data[0] == 'queryType' or data[0] == 'mutationType' or data[0] == 'subscriptionType':
                if data[1]:
                    operationType = getattr(pyObject, data[0])
                    operationType = SCOperationType()
                    operationType.name = data[1]['name']
                    setattr(pyObject, data[0], operationType)
            if data[0] == 'types':
                pyObject.types = SchemaTypeBuilder.buildTypes(data[1]) if data[1] else None
            if data[0] == 'directives':
                # pyObject.directives = self.buildDirectives(data[1]) if data[1] else None
                pyObject.directives = list(map(self.buildDirective, data[1])) if data[1] else None

        return pyObject

    def buildDirective(self, dataInput):
        directive = SCDirective()
        while len(dataInput.items()) > 0:
            inputField = dataInput.popitem()
            setattr(directive, inputField[0], SchemaTypeBuilder.buildArgsOrInputFields(inputField[1], False) if inputField[0] == 'args' else inputField[1])

        return directive
