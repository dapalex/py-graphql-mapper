
# import sys
# import os
# import pathlib

# sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
# sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

import unittest
from .githubApiUnitTest import (runGithubAddCommentMutation,
                               runGithubCreateIssueMutation, runGithubCreateProjectMutation, runGithubDeleteProjectMutation,
                               runGithubDeleteProjectV2Mutation, runGithubUpdateRepositoryMutation)
from .rapidApiUnitTest import (runRapidApiCreateGatewayInstanceMutation, runAdminAuditLogs,
                              runRapidApiCreateTransformationsMutation, runRapidApiEditUserAlertMutation)
from .unitTest import (runComplexObjectShowChange, runComplexObjectShowChangeWithArgsAndVariables,
                        runComplexObjectWithArgsAndVariables, runComplexObjectWithLiteralValueArgs,
                        runComplexObjectWithLiteralValueArgs2, runNestedObject, runNestedObjectShowChange,
                        runNestedObjectShowChangeWithArgsAndVariables, runNestedObjectWithArgsAndVariables,
                        runNestedObjectWithLiteralValueArgs, runObjectWithComposedArgs)
from .tstquery.complexObjectTest import runComplexObject
from .tstquery.connectionobjectArgs_LiteralValuesTest import runConnectionObjectArgs_LiteralValues
from .tstquery.connectionObjectArgs_VariablesTest import runConnectionObjectArgs_Variables
from .tstquery.connectionObjectChangeVisibilityTest import runConnectionObjectVisibility
from .tstquery.connectionObjectTest import runConnectionObject
from .tstquery.manuallyCreatedObjectTest import runGeneratedDataAsGQLObject
from .tstquery.simpleObjectTest import runSimpleObject
from .tstquery.simpleObjectArgs_LiteralValuesTest import runSimpleObjectArgs_LiteralValues
from .tstquery.simpleObjectArgs_VariablesTest import runSimpleObjectArgs_Variables
from .tstquery.simpleObjectChangeVisibilityTest import runSimpleObjectVisibility
from .tstmutation.manuallyCreatedMutationInsertTest import runMutationInsertLiteralValues
from .tstmutation.mutationUpdateTest import runMutationUpdateLiteralValues

class TestMapper(unittest.TestCase):

###################### QUERIES EXECUTION - START ##############################

    def testGeneratedDataAsGQLObject(self):
      return runGeneratedDataAsGQLObject()

    def testSimpleObject(self):
      return runSimpleObject()

    def testSimpleObjectArgs_LiteralValues(self):
      return runSimpleObjectArgs_LiteralValues()

    def testSimpleObjectArgs_Variables(self):
      return runSimpleObjectArgs_Variables()

    def testSimpleObjectVisibility(self):
      return runSimpleObjectVisibility()

    def testConnectionObject(self):
      return runConnectionObject()

    def testConnectionObjectVisibility(self):
      return runConnectionObjectVisibility()

    def testConnectionObjectArgs_Variables(self):
      return runConnectionObjectArgs_Variables()

    def testConnectionObjectArgs_LiteralValues(self):
      return runConnectionObjectArgs_LiteralValues()

###################### QUERIES EXECUTION - END ##############################

###################### MUTATIONS EXECUTION - START ##############################


#GITHUB API - START
    def testMutationUpdateLiteralValues(self):
      return runMutationUpdateLiteralValues()

    def testMutationInsertLiteralValues(self):
      return runMutationInsertLiteralValues()

    def testGithubAddCommentMutation(self):
      return runGithubAddCommentMutation()

    def testGithubUpdateRepositoryMutation(self):
      return runGithubUpdateRepositoryMutation()

    def testGithubDeleteProjectMutation(self):
      return runGithubDeleteProjectMutation()

    def testGithubDeleteProjectV2Mutation(self):
      return runGithubDeleteProjectV2Mutation()

    def testGithubCreateIssueMutation(self):
      return runGithubCreateIssueMutation()

    def testGithubCreateProjectMutation(self):
      return runGithubCreateProjectMutation()
#GITHUB - END

#RapidAPI - START

    def testAdminAuditLogs(self):
      return runAdminAuditLogs()

    def testRapidApiCreateTransformationsMutation(self):
      return runRapidApiCreateTransformationsMutation()

    def testRapidApiCreateGatewayInstanceMutation(self):
      return runRapidApiCreateGatewayInstanceMutation()

    def testRapidApiEditUserAlertMutation(self):
      return runRapidApiEditUserAlertMutation()
#RapidAPI - END

###################### MUTATIONS EXECUTION - END ##############################

# # #FURTHER TESTS
    def testComplexObject(self):
      return runComplexObject()
    def testNestedObject(self):
      return runNestedObject()
    def testNestedObjectWithLiteralValueArgs(self):
      return runNestedObjectWithLiteralValueArgs()
    def testNestedObjectShowChange(self):
      return runNestedObjectShowChange()
    def testComplexObjectWithLiteralValueArgs(self):
      return runComplexObjectWithLiteralValueArgs()
    def testComplexObjectWithLiteralValueArgs2(self):
      return runComplexObjectWithLiteralValueArgs2()
    def testObjectWithComposedArgs(self):
      return runObjectWithComposedArgs()
    def testComplexObjectShowChange(self):
      return runComplexObjectShowChange()
    def testNestedObjectShowChangeWithArgsAndVariables(self):
      return runNestedObjectShowChangeWithArgsAndVariables()
    def testComplexObjectShowChangeWithArgsAndVariables(self):
      return runComplexObjectShowChangeWithArgsAndVariables()
    def testNestedObjectWithArgsAndVariables(self):
      return runNestedObjectWithArgsAndVariables()
    def testComplexObjectWithArgsAndVariables(self):
      return runComplexObjectWithArgsAndVariables()
