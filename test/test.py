
import sys
import os
import pathlib

sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
# sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).parent.absolute()) + '\\PyGraphQLHelper')

import asyncio
from utils import OutputType, waitForInput, cleanOutput
from geoDBCitiesApiUnitTest import *
from githubApiUnitTest import *
from helpUnitTest import runGeneratorCommandHelp
from rapidApiUnitTest import *

# from pygqlGenerator.src.compScalarTypes import TypedFloat
# myFloat = TypedFloat("my argument")
# myFloat = 13.5

# print(myFloat)
# print(myFloat._args)

lockOutput = input('Do you want to pause at each test? (Y/N) ')

#GENERATOR - START
cleanOutput(OutputType.SCHEMAS)
asyncio.run(fetchGeoDBCitiesSchema())
waitForInput(lockOutput)
asyncio.run(fetchGeoDBCitiesSchemaNoDesc())
waitForInput(lockOutput)
wrapper = redirectOutputToFile('logrecurs.log')
asyncio.run(fetchGithubMutationTypesFromSchemaNoDesc())
restoreOutput(wrapper)
waitForInput(lockOutput)
asyncio.run(fetchGithubMutationTypes())
waitForInput(lockOutput)
asyncio.run(fetchRapidApiTestSchemaAndTypesNoDesc())
waitForInput(lockOutput)
asyncio.run(fetchRapidApiTestSchemaAndTypes())
waitForInput(lockOutput)

#GITHUB API - START
asyncio.run(RunGithubAddCommentMutation())
waitForInput(lockOutput)
asyncio.run(RunGithubUpdateRepositoryMutation())
waitForInput(lockOutput)
asyncio.run(RunGithubDeleteProjectMutation())
waitForInput(lockOutput)
asyncio.run(RunGithubDeleteProjectV2Mutation())
waitForInput(lockOutput)
asyncio.run(RunGithubCreateIssueMutation())
waitForInput(lockOutput)
asyncio.run(RunGithubCreateProjectMutation())
#GITHUB - END

#RapidAPI - START
asyncio.run(RunRapidApiCreateTransformationsMutation())
waitForInput(lockOutput)
asyncio.run(RunRapidApiCreateGatewayInstanceMutation())
waitForInput(lockOutput)
asyncio.run(RunRapidApiEditUserAlertMutation())
waitForInput(lockOutput)
#RapidAPI - END

#GeoDBCities API - START
#GeoDBCities API - END

#COMMANDS - START
cleanOutput(OutputType.COMMANDS)

asyncio.run(runGeneratorCommandHelp())
waitForInput(lockOutput)
asyncio.run(runDownloadCommandgdbcApiBySchemaFileRelPath())
waitForInput(lockOutput)
asyncio.run(runDownloadCommandGeoDBCitiesBySchemaFileRelPath())
waitForInput(lockOutput)
asyncio.run(runGenerateCommandGeoDBCitiesByApiRelPath())
waitForInput(lockOutput)
asyncio.run(runDownloadCommandGithubBySchemaFileRelPath())
waitForInput(lockOutput)
asyncio.run(runGenerateCommandGithubByApiAbsPath())
waitForInput(lockOutput)
asyncio.run(runGenerateCommandGeoDBCitiesByApiRelPath())
waitForInput(lockOutput)
asyncio.run(runDownloadCommandRapidApiBySchemaFileRelPath())
waitForInput(lockOutput)
asyncio.run(runGenerateCommandRapidApiByApiAbsPath())
waitForInput(lockOutput)
#COMMANDS - END

#GENERATOR - END