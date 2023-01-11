import json
import logging as logger
from .src.extractor import Extractor
from .src.printer import Printer
from .src.sp_builder import SchemaBuilder
from .src.sp_schema import GQLSchema

def build_schema(schemaString: GQLSchema):
    myBuilder = SchemaBuilder()
    return myBuilder.build(json.loads(schemaString), GQLSchema())

class CodeGenerator():

    def generate_code(schemaObj, folder, log_progress: bool = False, add_desc: bool = True):
        try:
            if log_progress: logger.info('Initializing Extractor...')
            extractor = Extractor(schemaObj, log_progress, add_desc)
            if log_progress: logger.info('Extracting schema...')
            extractedData = extractor.extract_schema_code()
            if log_progress: logger.info('Generating python code...')
            printer = Printer(extractedData)
            if log_progress: logger.info('Saving python files in ' + folder + '...')
            printer.save_files(folder)

            #CLEANING
            del extractor
            del printer
        except Exception as ex:
            raise ex

