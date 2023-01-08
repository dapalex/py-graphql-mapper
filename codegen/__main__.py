import argparse
import json
import os
import pathlib
import sys
# import logging as logger
from .queryPresets import *
from .network import fetchSchemaResponse
from .generator import CodeGenerator, buildSchema
from .src.spSchema import GQLSchema
from .src.utils import getValidFolder

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
            generatePythonCode(commandArgs, args.destPath)
        elif args.command == 'download':
            saveJsonSchema(commandArgs, args.destPath)
        else:
            raise argparse.ArgumentTypeError('Invalid command')

    except Exception as ex:
        print(str(ex.args))
        exit(-1)

def saveJsonSchema(args, destination):
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
                schemaResponse = fetchSchemaResponse(arguments['apiURL'], httpHeaders, querySchemaAndTypes)

                parentFolder = pathlib.Path(destination).parent
                outputFolder = getValidFolder(str(parentFolder))
                fileName = pathlib.Path(destination).name
                outputFile = os.path.join(outputFolder, fileName)
                if args.verbose: print('Saving Schema...')
                with open(outputFile, 'w') as schemaFile:
                    schemaFile.write(json.dumps(schemaResponse.data, indent=2))

    except Exception as ex:
        print('saveJsonSchema error: ' + str(ex.args))
        exit(-1)

def generatePythonCode(args, destPath):
    try:
        schemaObject: GQLSchema = None

        if destPath:
            if args.verbose: print('Checking destination folder...') 

            input_path = getValidFolder(destPath)

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

        addDescription =  arguments['addDescToGeneratedFiles'] if 'addDescToGeneratedFiles' in arguments.keys() else True

        schemaObject = extractSchemaObject(arguments, args.verbose)

        if args.verbose: print('Generating mutations...') #, end="\r")
        CodeGenerator.generateCode(schemaObject, input_path, logProgress=args.verbose, addDescription=addDescription)
    except Exception as ex:
        print('generatePythonCode error: ' + str(ex.args))
        exit(-1)
        
def extractSchemaObject(arguments, verbose):
    try:
        if 'apiURL' in arguments.keys() and arguments['apiURL']:
            httpHeaders = arguments['httpHeaders'] if 'httpHeaders' in arguments.keys() else None
            if verbose: print('Fetching schema from server...')
            schemaResponse = fetchSchemaResponse(arguments['apiURL'], httpHeaders, querySchemaAndTypes)
            if verbose: print('Mapping response...')
            schemaResponse.mapGQLDataToObj()

            return schemaResponse.resultObject

        elif 'schemaFile' in arguments.keys() and arguments['schemaFile']:
            if verbose: print('Extracting schema from file...')
            parentFolder = pathlib.Path(arguments['schemaFile']).parent
            outputFolder = getValidFolder(str(parentFolder))
            if verbose: print('output folder: ' + str(outputFolder))
            fileName = pathlib.Path(arguments['schemaFile']).name
            if verbose: print('file name: ' + str(fileName))
            outputFilePath = os.path.join(outputFolder, fileName)
            if verbose: print('output destination: ' + str(outputFilePath))
            with open(outputFilePath, 'r') as wrapper:
                schemaString = wrapper.read()

            if verbose: print('Creating schema object...')
            return buildSchema(schemaString)

    except Exception as ex:
        print('extractSchemaObject error: ' + str(ex.args))
        exit(-1)
        
    if verbose: print('Schema not extracted!')
    return None

if __name__ == '__main__':
    print('python-graphql mapper code generator 0.3.0')
    main()