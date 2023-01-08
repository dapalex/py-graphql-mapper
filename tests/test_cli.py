import sys
import os
import pathlib


sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

import unittest
from .helpUnitTest import runGeneratorCommandHelp
import logging as logger


class TestCLI(unittest.TestCase):

    def testGeneratorCommandHelp(self):
      return runGeneratorCommandHelp()

    def testDownloadCommandgdbcApiBySchemaFileRelPath(self):
      return runDownloadCommandgdbcApiBySchemaFileRelPath()

    def testGenerateCommandGeoDBCitiesBySchemaFileRelPath(self):
      return runGenerateCommandGeoDBCitiesBySchemaFileRelPath()

    def testGenerateCommandGeoDBCitiesByApiRelPath(self):
      return runGenerateCommandGeoDBCitiesByApiRelPath()

    # def testDownloadCommandGithubBySchemaFileRelPath(self):
    #   return runDownloadCommandGithubBySchemaFileRelPath()

    # def testGenerateCommandGithubByApiAbsPath(self):
    #   return runGenerateCommandGithubByApiAbsPath()

    def testGenerateCommandGithubBySchemaFile(self):
      return runGenerateCommandGithubBySchemaFile()

    def testDownloadCommandRapidApiBySchemaFileRelPath(self):
      return runDownloadCommandRapidApiBySchemaFileRelPath()

    def testGenerateCommandRapidApiByApiAbsPath(self):
      return runGenerateCommandRapidApiByApiAbsPath()



def runDownloadCommandgdbcApiBySchemaFileRelPath():
    logger.info('\nRunning runDownloadCommandGithubBySchemaFileRelPath...')
    command = "pgmcodegen download ./tests/commandsOutput/Github/schema.json -apiArgs ./tests/cliInput/GdbcApi/downloaderArgs.json -v" #command to be executed
    logger.info("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.info("End of runDownloadCommandGithubBySchemaFileRelPath")

def runGenerateCommandGeoDBCitiesBySchemaFileRelPath():
    logger.info('\nRunning runGenerateCommandGeoDBCitiesBySchemaFileRelPath...')
    command = "pgmcodegen generate ./tests/commandsOutput/GeoDBCities -apiArgs tests/cliInput/GdbcApi/schema.json -v" #command to be executed
    logger.info("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.info("End of runGenerateCommandGeoDBCitiesBySchemaFileRelPath")

def runGenerateCommandGeoDBCitiesByApiRelPath():
    logger.info('\nRunning runGenerateCommandGeoDBCitiesByApiRelPath...')
    command = "pgmcodegen generate ./tests/commandsOutput/GeoDBCities -apiArgs ./tests/cliInput/gdbcApi/generatorArgs.json -v" #command to be executed
    logger.info("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.info("End of runGenerateCommandGeoDBCitiesByApiRelPath")


def runDownloadCommandGithubBySchemaFileRelPath():
    logger.info('\nRunning runDownloadCommandGithubBySchemaFileRelPath...')
    command = "pgmcodegen download ./tests/commandsOutput/Github/schema.json -apiArgs ./tests/cliInput/GithubApi/downloaderArgs.json -v" #command to be executed
    logger.info("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.info("End of runDownloadCommandGithubBySchemaFileRelPath")

def runGenerateCommandGithubByApiAbsPath():
    logger.info('\nRunning runGenerateCommandGithubByApiAbsPath...')
    command = "pgmcodegen generate ./tests/commandsOutput/Github -v -apiArgs ./tests/cliInput/GithubApi/generatorArgs.json -v" #command to be executed
    logger.info("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.info("End of runGenerateCommandGithubByApiAbsPath")

def runGenerateCommandGithubBySchemaFile():
    logger.info('\nRunning runGenerateCommandGithubByApiAbsPath...')
    command = "pgmcodegen generate ./tests/commandsOutput/Github -v -apiArgs ./tests/cliInput/GithubApi/generatorArgs.json -v" #command to be executed
    logger.info("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.info("End of runGenerateCommandGithubByApiAbsPath")

def runDownloadCommandRapidApiBySchemaFileRelPath():
    logger.info('\nRunning runDownloadCommandRapidApiBySchemaFileRelPath...')
    command = "pgmcodegen download ./tests/commandsOutput/RapidApi/schema.json -apiArgs ./tests/cliInput/RapidApi/downloaderArgs.json -v" #command to be executed
    logger.info("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.info("End of runDownloadCommandRapidApiBySchemaFileRelPath")

def runGenerateCommandRapidApiByApiAbsPath():
    logger.info('\nRunning runGenerateCommandRapidApiByApiAbsPath...')
    command = "pgmcodegen generate ./tests/commandsOutput/RapidApi -v -apiArgs ./tests/cliInput/RapidApi/generatorArgs.json -v" #command to be executed
    logger.info("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.info("End of runGenerateCommandRapidApiByApiAbsPath")
