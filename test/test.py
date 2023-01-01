
import sys
import os
import pathlib


sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

import asyncio
from utils import OutputType, waitForInput, cleanOutput
from geoDBCitiesApiUnitTest import runDownloadCommandgdbcApiBySchemaFileRelPath
from githubApiUnitTest import (runDownloadCommandGithubBySchemaFileRelPath, RunGithubAddCommentMutation, 
                               RunGithubCreateIssueMutation, RunGithubCreateProjectMutation, RunGithubDeleteProjectMutation, 
                               RunGithubDeleteProjectV2Mutation, RunGithubUpdateRepositoryMutation)
from helpUnitTest import runGeneratorCommandHelp
from rapidApiUnitTest import (runDownloadCommandRapidApiBySchemaFileRelPath, RunRapidApiCreateGatewayInstanceMutation, 
                              RunRapidApiCreateTransformationsMutation, RunRapidApiEditUserAlertMutation, 
                              testAdminAuditLogs)

from geoDBCitiesApiUnitTest import fetchGeoDBCitiesSchema, fetchGeoDBCitiesSchemaNoDesc
from githubApiUnitTest import fetchGithubMutationTypes, fetchGithubMutationTypesFromSchemaNoDesc
from rapidApiUnitTest import fetchRapidApiTestSchemaAndTypes, fetchRapidApiTestSchemaAndTypesNoDesc


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

#COMMANDS - START
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
#COMMANDS - END

#GENERATOR - END

from unitTest import (testComplexObjectShowChange, testComplexObjectShowChangeWithArgsAndVariables, 
                        testComplexObjectWithArgsAndVariables, testComplexObjectWithLiteralValueArgs, 
                        testComplexObjectWithLiteralValueArgs2, testNestedObject, testNestedObjectShowChange, 
                        testNestedObjectShowChangeWithArgsAndVariables, testNestedObjectWithArgsAndVariables, 
                        testNestedObjectWithLiteralValueArgs, testObjectWithComposedArgs)
from tstquery.complexObjectTest import testComplexObject
from tstquery.connectionobjectArgs_LiteralValuesTest import testConnectionObjectArgs_LiteralValues
from tstquery.connectionObjectArgs_VariablesTest import testConnectionObjectArgs_Variables
from tstquery.connectionObjectChangeVisibilityTest import testConnectionObjectVisibility
from tstquery.connectionObjectTest import testConnectionObject
from tstquery.manuallyCreatedObjectTest import testGeneratedDataAsGQLObject
from tstquery.simpleObjectTest import testSimpleObject
from tstquery.simpleObjectArgs_LiteralValuesTest import testSimpleObjectArgs_LiteralValues
from tstquery.simpleObjectArgs_VariablesTest import testSimpleObjectArgs_Variables
from tstquery.simpleObjectChangeVisibilityTest import testSimpleObjectVisibility
from tstmutation.manuallyCreatedMutationInsertTest import testMutationInsertLiteralValues
from tstmutation.mutationUpdateTest import testMutationUpdateLiteralValues

#SAMPLE TESTS - START
asyncio.run(testGeneratedDataAsGQLObject())
waitForInput(lockOutput)
asyncio.run(testSimpleObject())
waitForInput(lockOutput)
asyncio.run(testSimpleObjectArgs_LiteralValues())
waitForInput(lockOutput)
asyncio.run(testSimpleObjectArgs_Variables())
waitForInput(lockOutput)
asyncio.run(testSimpleObjectVisibility())
waitForInput(lockOutput)

asyncio.run(testConnectionObject())
waitForInput(lockOutput)
asyncio.run(testConnectionObjectVisibility())
waitForInput(lockOutput)
asyncio.run(testConnectionObjectArgs_Variables())
waitForInput(lockOutput)
asyncio.run(testConnectionObjectArgs_LiteralValues())
waitForInput(lockOutput)

asyncio.run(testComplexObject())
waitForInput(lockOutput)

asyncio.run(testMutationUpdateLiteralValues()) 
waitForInput(lockOutput)
asyncio.run(testMutationInsertLiteralValues()) 
waitForInput(lockOutput)
# ##SAMPLE TESTS - END

# #FURTHER TESTS
asyncio.run(testNestedObjectWithLiteralValueArgs())
waitForInput(lockOutput)
asyncio.run(testNestedObjectShowChange())
waitForInput(lockOutput)
asyncio.run(testComplexObjectWithLiteralValueArgs())
waitForInput(lockOutput)
asyncio.run(testComplexObjectWithLiteralValueArgs2())
waitForInput(lockOutput)
asyncio.run(testObjectWithComposedArgs()) 
waitForInput(lockOutput)
asyncio.run(testComplexObjectShowChange())
waitForInput(lockOutput)
asyncio.run(testNestedObjectShowChangeWithArgsAndVariables())
waitForInput(lockOutput)
asyncio.run(testComplexObjectShowChangeWithArgsAndVariables()) 
waitForInput(lockOutput)
asyncio.run(testNestedObjectWithArgsAndVariables()) 
waitForInput(lockOutput)
asyncio.run(testComplexObjectWithArgsAndVariables()) 
waitForInput(lockOutput)
#Geo DB Cities - END

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
asyncio.run(testAdminAuditLogs()) 
waitForInput(lockOutput)
asyncio.run(RunRapidApiCreateTransformationsMutation())
waitForInput(lockOutput)
asyncio.run(RunRapidApiCreateGatewayInstanceMutation())
waitForInput(lockOutput)
asyncio.run(RunRapidApiEditUserAlertMutation())
waitForInput(lockOutput)
#RapidAPI - END

#CORE - END