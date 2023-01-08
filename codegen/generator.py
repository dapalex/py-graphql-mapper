import json
import logging as logger
from .src.extractor import Extractor
from .src.printer import Printer
from .src.spBuilder import SchemaBuilder
from .src.spSchema import GQLSchema

def buildSchema(schemaString: GQLSchema):
    myBuilder = SchemaBuilder()
    return myBuilder.build(json.loads(schemaString), GQLSchema())

class CodeGenerator():

    def generateCode(schemaObj, folder, logProgress: bool = False, addDescription: bool = True):
        try:
            if logProgress: logger.info('Initializing Extractor...')
            extractor = Extractor(schemaObj, logProgress, addDescription)
            if logProgress: logger.info('Extracting schema...')
            extractedData = extractor.extractSchemaCode()
            if logProgress: logger.info('Generating python code...')
            printer = Printer(extractedData)
            if logProgress: logger.info('Saving python files in ' + folder + '...')
            printer.saveFiles(folder)

            #CLEANING
            del extractor
            del printer
        except Exception as ex:
            raise ex

