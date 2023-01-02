import json
from pygqlmap.src.logger import Logger
from .src.extractor import Extractor
from .src.printer import Printer
from .src.spBuilder import SchemaBuilder
from .src.spSchema import GQLSchema
   
def buildSchema(schemaString: GQLSchema):
    myBuilder = SchemaBuilder()
    return myBuilder.build(json.loads(schemaString), GQLSchema())

class CodeGenerator():
    
    def generateCode(schemaObj, folder, customTypes: dict = {}, logProgress: bool = False, addDescription: bool = True):
        try:
            if logProgress: Logger.logInfoMessage('Initializing Extractor...')
            extractor = Extractor(schemaObj, customTypes, logProgress, addDescription)
            if logProgress: Logger.logInfoMessage('Extracting schema...')
            extractedData = extractor.extractSchemaCode()
            if logProgress: Logger.logInfoMessage('Generating python code...')
            printer = Printer(extractedData)
            if logProgress: Logger.logInfoMessage('Saving python files in ' + folder + '...')
            printer.saveFiles(folder)
            
            #CLEANING
            del extractor
            del printer
        except Exception as ex:
            raise ex
    
