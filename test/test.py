
import sys
import os
import pathlib

sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))

import asyncio
from utils import OutputType, waitForInput, cleanOutput
from geoDBCitiesApiUnitTest import *
from githubApiUnitTest import *
from helpUnitTest import runGeneratorCommandHelp
from rapidApiUnitTest import *

lockOutput = input('Do you want to pause at each test? (Y/N) ')

#GENERATOR - START
# cleanOutput(OutputType.SCHEMAS)
# asyncio.run(fetchGeoDBCitiesSchema())
# waitForInput(lockOutput)
# asyncio.run(fetchGeoDBCitiesSchemaNoDesc())
# waitForInput(lockOutput)
# asyncio.run(fetchGithubMutationTypesFromSchemaNoDesc())
# waitForInput(lockOutput)
# asyncio.run(fetchGithubMutationTypes())
# waitForInput(lockOutput)
# asyncio.run(fetchRapidApiTestSchemaAndTypesNoDesc())
# waitForInput(lockOutput)
# asyncio.run(fetchRapidApiTestSchemaAndTypes())
# waitForInput(lockOutput)

#GeoDBCities API - START
#GeoDBCities API - END

# #COMMANDS - START
# cleanOutput(OutputType.COMMANDS)

# asyncio.run(runGeneratorCommandHelp())
# waitForInput(lockOutput)
# asyncio.run(runDownloadCommandgdbcApiBySchemaFileRelPath())
# waitForInput(lockOutput)
# asyncio.run(runDownloadCommandGeoDBCitiesBySchemaFileRelPath())
# waitForInput(lockOutput)
# asyncio.run(runGenerateCommandGeoDBCitiesByApiRelPath())
# waitForInput(lockOutput)
# asyncio.run(runDownloadCommandGithubBySchemaFileRelPath())
# waitForInput(lockOutput)
# asyncio.run(runGenerateCommandGithubByApiAbsPath())
# waitForInput(lockOutput)
# asyncio.run(runGenerateCommandGeoDBCitiesByApiRelPath())
# waitForInput(lockOutput)
# asyncio.run(runDownloadCommandRapidApiBySchemaFileRelPath())
# waitForInput(lockOutput)
# asyncio.run(runGenerateCommandRapidApiByApiAbsPath())
# waitForInput(lockOutput)
# #COMMANDS - END

#GENERATOR - END

from unitTest import *
# from tstquery.complexObjectTest import *
# from tstquery.connectionobjectArgs_LiteralValuesTest import *
# from tstquery.connectionObjectArgs_VariablesTest import *
# from tstquery.connectionObjectChangeVisibilityTest import *
# from tstquery.connectionObjectTest import *
# from tstquery.generatedDataAsObjectTest import *
# from tstquery.simpleObjectTest import *
# from tstquery.simpleObjectArgs_LiteralValuesTest import *
# from tstquery.simpleObjectArgs_VariablesTest import *
# from tstquery.simpleObjectChangeVisibilityTest import *
# from tstmutation.mutationInsertTest import *
# from tstmutation.mutationUpdateTest import *

# CORE - START
# #SAMPLE TESTS - START
# asyncio.run(testGeneratedDataAsGQLObject())
# waitForInput(lockOutput)
# asyncio.run(testSimpleObject())
# waitForInput(lockOutput)
# asyncio.run(testSimpleObjectArgs_LiteralValues())
# waitForInput(lockOutput)
# asyncio.run(testSimpleObjectArgs_Variables())
# waitForInput(lockOutput)
# asyncio.run(testSimpleObjectVisibility())
# waitForInput(lockOutput)

# asyncio.run(testConnectionObject())
# waitForInput(lockOutput)
# asyncio.run(testConnectionObjectVisibility())
# waitForInput(lockOutput)
# asyncio.run(testConnectionObjectArgs_Variables())
# waitForInput(lockOutput)
# asyncio.run(testConnectionObjectArgs_LiteralValues())
# waitForInput(lockOutput)

# asyncio.run(testComplexObject())
# waitForInput(lockOutput)

# asyncio.run(testMutationUpdateLiteralValues()) 
# waitForInput(lockOutput)
# asyncio.run(testMutationInsertLiteralValues()) 
# waitForInput(lockOutput)
# ##SAMPLE TESTS - END

#FURTHER TESTS
# asyncio.run(adminAuditLogsMutation()) 
# waitForInput(lockOutput)
asyncio.run(testNestedObjectWithLiteralValueArgs())
waitForInput(lockOutput)
asyncio.run(testNestedObjectShowChange())
waitForInput(lockOutput)
asyncio.run(testComplexObjectWithLiteralValueArgs())
waitForInput(lockOutput)
asyncio.run(testComplexObjectShowChange())
waitForInput(lockOutput)
asyncio.run(testComplexObjectWithLiteralValueArgs2())
waitForInput(lockOutput)
asyncio.run(testObjectWithComposedArgs()) 
waitForInput(lockOutput)
# asyncio.run(testNestedObjectShowChangeWithArgsAndVariables())
# waitForInput(lockOutput)
# asyncio.run(testComplexObjectShowChangeWithArgsAndVariables()) 
# waitForInput(lockOutput)
# asyncio.run(testNestedObjectWithArgsAndVariables()) 
# waitForInput(lockOutput)
# asyncio.run(testComplexObjectWithArgsAndVariables()) 
# waitForInput(lockOutput)
##Geo DB Cities - END

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
waitForInput(lockOutput)
#GITHUB - END

#RapidAPI - START
asyncio.run(RunRapidApiCreateTransformationsMutation())
waitForInput(lockOutput)
asyncio.run(RunRapidApiCreateGatewayInstanceMutation())
waitForInput(lockOutput)
asyncio.run(RunRapidApiEditUserAlertMutation())
waitForInput(lockOutput)
#RapidAPI - END

#CORE - END