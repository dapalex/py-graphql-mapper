import argparse
import json
import os
import pathlib
import sys
# import logging as logger
from .query_presets import *
from .network import fetch_schema_response
from .generator import CodeGenerator, build_schema
from .src.sp_schema import GQLSchema
from .src.utils import get_valid_folder

def main():
    try:

        my_parser = argparse.ArgumentParser(description = """Welcome to the python-graphql mutations generator""")
        my_parser.add_argument('command', type=str, help='the requested command')
        my_parser.add_argument('destPath', type=str, help='the destination path of mutation classes')

        args = my_parser.parse_args(sys.argv[1:3])

        commandParser = argparse.ArgumentParser()
        commandParser.add_argument('-v', '--verbose', action='store_true')
        commandParser.add_argument('-apiArgs', type=str, help='path of the args file', required=False)

        if args.command == 'generate':
            commandParser.add_argument('-schemaFile', type=str, help='path of the args file', required=False)

        commandArgs = commandParser.parse_args(sys.argv[3:])

        if args.command == 'generate':
            generate_py_code(commandArgs, args.destPath)
        elif args.command == 'download':
            save_json_schema(commandArgs, args.destPath)
        else:
            raise argparse.ArgumentTypeError('Invalid command')

    except Exception as ex:
        print(str(ex.args))
        exit(-1)

def save_json_schema(args, destination):
    try:
        if hasattr(args, 'apiArgs') and args.apiArgs:
            if args.verbose: print('Checking args file...')
            argsFilePath = pathlib.Path(args.apiArgs).absolute()
            if args.verbose: print('args file path -> ' + str(argsFilePath))
            try:
                if args.verbose: print('Reading args file...')
                with open(str(argsFilePath), 'r') as argsFile:
                    arguments = json.load(argsFile)
            except Exception as ex:
                print('saveJsonSchema arg opening error: ' + str(ex.args))
                exit(-1)

            if args.verbose: print(arguments)

            if 'apiURL' in arguments.keys() and arguments['apiURL']:
                httpHeaders = arguments['httpHeaders'] if 'httpHeaders' in arguments.keys() else None
                if args.verbose: print('Fetching schema from server...')
                schemaResponse = fetch_schema_response(arguments['apiURL'], httpHeaders, QUERY_SCHEMA_AND_TYPES)

                parentFolder = pathlib.Path(destination).parent
                outputFolder = get_valid_folder(str(parentFolder))
                fileName = pathlib.Path(destination).name
                outputFile = os.path.join(outputFolder, fileName)
                if args.verbose: print('Saving Schema...')
                with open(outputFile, 'w') as schemaFile:
                    schemaFile.write(json.dumps(schemaResponse.data, indent=2))

    except Exception as ex:
        print('saveJsonSchema error: ' + str(ex.args))
        exit(-1)

def generate_py_code(args, destPath):
    try:
        schemaObject: GQLSchema = None

        if destPath:
            if args.verbose: print('Checking destination folder...')

            input_path = get_valid_folder(destPath)

        if args.verbose: print('Parsing command...')

        if hasattr(args, 'apiArgs') and args.apiArgs:
            if args.verbose: print('Checking args file...')
            argsFilePath = pathlib.Path(args.apiArgs).absolute()
            if args.verbose: print('args file path -> ' + str(argsFilePath))
            try:
                if args.verbose: print('Reading args file...')
                with open(str(argsFilePath), 'r') as argsFile:
                    arguments = json.load(argsFile)

                if args.verbose: print(arguments)
            except Exception as ex:
                print('generatePythonCode -  arg opening error: ' + str(ex.args))
                exit(-1)

        add_desc =  arguments['addDescToGeneratedFiles'] if 'addDescToGeneratedFiles' in arguments.keys() else True

        schemaObject = extract_schema_obj(arguments, args.verbose)

        if args.verbose: print('Generating mutations...') #, end="\r")
        CodeGenerator.generate_code(schemaObject, input_path, log_progress=args.verbose, add_desc=add_desc)
    except Exception as ex:
        print('generatePythonCode error: ' + str(ex.args))
        exit(-1)

def extract_schema_obj(arguments, verbose):
    try:
        if 'apiURL' in arguments.keys() and arguments['apiURL']:
            httpHeaders = arguments['httpHeaders'] if 'httpHeaders' in arguments.keys() else None
            if verbose: print('Fetching schema from server...')
            schemaResponse = fetch_schema_response(arguments['apiURL'], httpHeaders, QUERY_SCHEMA_AND_TYPES)
            if verbose: print('Mapping response...')
            schemaResponse.map_gqldata_to_obj()

            return schemaResponse.result_obj

        elif 'schemaFile' in arguments.keys() and arguments['schemaFile']:
            if verbose: print('Extracting schema from file...')
            parentFolder = pathlib.Path(arguments['schemaFile']).parent
            outputFolder = get_valid_folder(str(parentFolder))
            if verbose: print('output folder: ' + str(outputFolder))
            fileName = pathlib.Path(arguments['schemaFile']).name
            if verbose: print('file name: ' + str(fileName))
            outputFilePath = os.path.join(outputFolder, fileName)
            if verbose: print('output destination: ' + str(outputFilePath))
            with open(outputFilePath, 'r') as wrapper:
                schemaString = wrapper.read()

            if verbose: print('Creating schema object...')
            return build_schema(schemaString)

    except Exception as ex:
        print('extractSchemaObject error: ' + str(ex.args))
        exit(-1)

    if verbose: print('Schema not extracted!')
    return None

if __name__ == '__main__':
    print('python-graphql mapper code generator 0.3.0')
    main()