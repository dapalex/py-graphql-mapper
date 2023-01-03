
import sys
import os
import pathlib


sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

import asyncio
from .geoDBCitiesApiUnitTest import (runDownloadCommandgdbcApiBySchemaFileRelPath, runDownloadCommandGeoDBCitiesBySchemaFileRelPath, 
                                     runGenerateCommandGeoDBCitiesByApiRelPath, fetchGeoDBCitiesSchema, fetchGeoDBCitiesSchemaNoDesc)
from .githubApiUnitTest import (runDownloadCommandGithubBySchemaFileRelPath, RunGithubAddCommentMutation, runGenerateCommandGithubByApiAbsPath,
                               RunGithubCreateIssueMutation, RunGithubCreateProjectMutation, RunGithubDeleteProjectMutation, 
                               RunGithubDeleteProjectV2Mutation, RunGithubUpdateRepositoryMutation, fetchGithubMutationTypes, fetchGithubMutationTypesFromSchemaNoDesc)
from .helpUnitTest import runGeneratorCommandHelp
from .rapidApiUnitTest import (runDownloadCommandRapidApiBySchemaFileRelPath, RunRapidApiCreateGatewayInstanceMutation, 
                              RunRapidApiCreateTransformationsMutation, RunRapidApiEditUserAlertMutation, runGenerateCommandRapidApiByApiAbsPath,
                              testAdminAuditLogs, fetchRapidApiTestSchemaAndTypes, fetchRapidApiTestSchemaAndTypesNoDesc)


###################### CODE GENERATION - START ##############################

# cleanOutput(OutputType.SCHEMAS)
asyncio.run(fetchGeoDBCitiesSchema())
asyncio.run(fetchGeoDBCitiesSchemaNoDesc())
asyncio.run(fetchGithubMutationTypesFromSchemaNoDesc())
asyncio.run(fetchGithubMutationTypes())
asyncio.run(fetchRapidApiTestSchemaAndTypesNoDesc())
asyncio.run(fetchRapidApiTestSchemaAndTypes())

#GeoDBCities API - START
#GeoDBCities API - END

###################### COMMAND LINE INTERFACE - START ##############################
# cleanOutput(OutputType.COMMANDS)

asyncio.run(runGeneratorCommandHelp())
asyncio.run(runDownloadCommandgdbcApiBySchemaFileRelPath())
asyncio.run(runDownloadCommandGeoDBCitiesBySchemaFileRelPath())
asyncio.run(runGenerateCommandGeoDBCitiesByApiRelPath())
asyncio.run(runDownloadCommandGithubBySchemaFileRelPath())
asyncio.run(runGenerateCommandGithubByApiAbsPath())
asyncio.run(runGenerateCommandGeoDBCitiesByApiRelPath())
asyncio.run(runDownloadCommandRapidApiBySchemaFileRelPath())
asyncio.run(runGenerateCommandRapidApiByApiAbsPath())
###################### COMMAND LINE INTERFACE - END ##############################

###################### CODE GENERATION - END ##############################

###################### QUERIES EXECUTION - START ##############################
from .unitTest import (testComplexObjectShowChange, testComplexObjectShowChangeWithArgsAndVariables, 
                        testComplexObjectWithArgsAndVariables, testComplexObjectWithLiteralValueArgs, 
                        testComplexObjectWithLiteralValueArgs2, testNestedObject, testNestedObjectShowChange, 
                        testNestedObjectShowChangeWithArgsAndVariables, testNestedObjectWithArgsAndVariables, 
                        testNestedObjectWithLiteralValueArgs, testObjectWithComposedArgs)
from .tstquery.complexObjectTest import testComplexObject
from .tstquery.connectionobjectArgs_LiteralValuesTest import testConnectionObjectArgs_LiteralValues
from .tstquery.connectionObjectArgs_VariablesTest import testConnectionObjectArgs_Variables
from .tstquery.connectionObjectChangeVisibilityTest import testConnectionObjectVisibility
from .tstquery.connectionObjectTest import testConnectionObject
from .tstquery.manuallyCreatedObjectTest import testGeneratedDataAsGQLObject
from .tstquery.simpleObjectTest import testSimpleObject
from .tstquery.simpleObjectArgs_LiteralValuesTest import testSimpleObjectArgs_LiteralValues
from .tstquery.simpleObjectArgs_VariablesTest import testSimpleObjectArgs_Variables
from .tstquery.simpleObjectChangeVisibilityTest import testSimpleObjectVisibility
from .tstmutation.manuallyCreatedMutationInsertTest import testMutationInsertLiteralValues
from .tstmutation.mutationUpdateTest import testMutationUpdateLiteralValues

asyncio.run(testGeneratedDataAsGQLObject())
asyncio.run(testSimpleObject())
asyncio.run(testSimpleObjectArgs_LiteralValues())
asyncio.run(testSimpleObjectArgs_Variables())
asyncio.run(testSimpleObjectVisibility())

asyncio.run(testConnectionObject())
asyncio.run(testConnectionObjectVisibility())
asyncio.run(testConnectionObjectArgs_Variables())
asyncio.run(testConnectionObjectArgs_LiteralValues())

asyncio.run(testComplexObject())

# # #FURTHER TESTS
asyncio.run(testNestedObjectWithLiteralValueArgs())
asyncio.run(testNestedObjectShowChange())
asyncio.run(testComplexObjectWithLiteralValueArgs())
asyncio.run(testComplexObjectWithLiteralValueArgs2())
asyncio.run(testObjectWithComposedArgs()) 
asyncio.run(testComplexObjectShowChange())
asyncio.run(testNestedObjectShowChangeWithArgsAndVariables())
asyncio.run(testComplexObjectShowChangeWithArgsAndVariables()) 
asyncio.run(testNestedObjectWithArgsAndVariables()) 
asyncio.run(testComplexObjectWithArgsAndVariables()) 
#Geo DB Cities - END

###################### QUERIES EXECUTION - END ##############################

###################### MUTATIONS EXECUTION - START ##############################

asyncio.run(testMutationUpdateLiteralValues()) 
asyncio.run(testMutationInsertLiteralValues()) 

#GITHUB API - START
asyncio.run(RunGithubAddCommentMutation())
asyncio.run(RunGithubUpdateRepositoryMutation())
asyncio.run(RunGithubDeleteProjectMutation())
asyncio.run(RunGithubDeleteProjectV2Mutation())
asyncio.run(RunGithubCreateIssueMutation())
asyncio.run(RunGithubCreateProjectMutation())
#GITHUB - END

#RapidAPI - START
asyncio.run(testAdminAuditLogs()) 
asyncio.run(RunRapidApiCreateTransformationsMutation())
asyncio.run(RunRapidApiCreateGatewayInstanceMutation())
asyncio.run(RunRapidApiEditUserAlertMutation())
#RapidAPI - END

###################### MUTATIONS EXECUTION - END ##############################