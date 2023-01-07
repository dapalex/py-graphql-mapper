
import sys
import os
import pathlib

sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

from .githubApiUnitTest import (RunGithubAddCommentMutation,
                               RunGithubCreateIssueMutation, RunGithubCreateProjectMutation, RunGithubDeleteProjectMutation, 
                               RunGithubDeleteProjectV2Mutation, RunGithubUpdateRepositoryMutation)
from .rapidApiUnitTest import (RunRapidApiCreateGatewayInstanceMutation, testAdminAuditLogs,
                              RunRapidApiCreateTransformationsMutation, RunRapidApiEditUserAlertMutation)
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

testGeneratedDataAsGQLObject())
testSimpleObject())
testSimpleObjectArgs_LiteralValues())
testSimpleObjectArgs_Variables())
testSimpleObjectVisibility())

testConnectionObject())
testConnectionObjectVisibility())
testConnectionObjectArgs_Variables())
testConnectionObjectArgs_LiteralValues())

testComplexObject()

# # #FURTHER TESTS
testNestedObject())
testNestedObjectWithLiteralValueArgs())
testNestedObjectShowChange())
testComplexObjectWithLiteralValueArgs())
testComplexObjectWithLiteralValueArgs2())
testObjectWithComposedArgs()) 
testComplexObjectShowChange())
testNestedObjectShowChangeWithArgsAndVariables())
testComplexObjectShowChangeWithArgsAndVariables()) 
testNestedObjectWithArgsAndVariables()) 
testComplexObjectWithArgsAndVariables()) 
#Geo DB Cities - END

###################### QUERIES EXECUTION - END ##############################

###################### MUTATIONS EXECUTION - START ##############################

testMutationUpdateLiteralValues()) 
testMutationInsertLiteralValues()) 

#GITHUB API - START
RunGithubAddCommentMutation())
RunGithubUpdateRepositoryMutation())
RunGithubDeleteProjectMutation())
RunGithubDeleteProjectV2Mutation())
RunGithubCreateIssueMutation())
RunGithubCreateProjectMutation())
#GITHUB - END

#RapidAPI - START
testAdminAuditLogs()) 
RunRapidApiCreateTransformationsMutation())
RunRapidApiCreateGatewayInstanceMutation())
RunRapidApiEditUserAlertMutation())
#RapidAPI - END

###################### MUTATIONS EXECUTION - END ##############################