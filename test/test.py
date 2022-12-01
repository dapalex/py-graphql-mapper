
import sys
import os
import pathlib

sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))

import asyncio
from utils import waitForInput
from pgqlmCoreTest.tstquery.connectionObjectTest import testConnectionObject
from pgqlmCoreTest.tstquery.connectionObjectChangeVisibilityTest import testConnectionObjectVisibility
from pgqlmCoreTest.tstquery.connectionObjectArgs_VariablesTest import testConnectionObjectArgs_Variables
from pgqlmCoreTest.tstquery.connectionobjectArgs_LiteralValuesTest import testConnectionObjectArgs_LiteralValues
from pgqlmCoreTest.tstquery.simpleObjectArgs_LiteralValuesTest import testSimpleObjectArgs_LiteralValues
from pgqlmCoreTest.tstquery.simpleObjectArgs_VariablesTest import testSimpleObjectArgs_Variables
from pgqlmCoreTest.tstquery.simpleObjectChangeVisibilityTest import testSimpleObjectVisibility
from pgqlmCoreTest.tstquery.complexObjectTest import testComplexObject
from pgqlmCoreTest.tstquery.simpleObjectTest import testSimpleObject
from pgqlmCoreTest.tstmutation.mutationUpdateTest import testMutationUpdateLiteralValues
from pgqlmCoreTest.tstmutation.mutationInsertTest import testMutationInsertLiteralValues

from pgqlmCoreTest.unitTest import *

lockOutput = input('Do you want to pause at each test? (Y/N) ')


# CORE - START
#SAMPLE TESTS - START
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
##SAMPLE TESTS - END

#FURTHER TESTS
asyncio.run(testNestedObjectWithArgsAndVariables()) 
waitForInput(lockOutput)
asyncio.run(testNestedObjectWithLiteralValueArgs())
waitForInput(lockOutput)
asyncio.run(testNestedObjectShowChange())
waitForInput(lockOutput)
asyncio.run(testComplexObjectWithLiteralValueArgs())
waitForInput(lockOutput)
asyncio.run(testComplexObjectWithArgsAndVariables()) 
waitForInput(lockOutput)
asyncio.run(testComplexObjectShowChange())
waitForInput(lockOutput)
asyncio.run(testComplexObjectWithLiteralValueArgs2())
waitForInput(lockOutput)
asyncio.run(testNestedObjectShowChangeWithArgsAndVariables())
waitForInput(lockOutput)
asyncio.run(testNestedObjectWithLiteralValueArgsAndCursorPaginationArgs())
waitForInput(lockOutput)
asyncio.run(testComplexObjectShowChangeWithArgsAndVariables()) 
waitForInput(lockOutput)
asyncio.run(testComplexObjectWithLiteralValueArgs2WithLog()) 
waitForInput(lockOutput)
asyncio.run(testObjectWithComposedArgs()) 
waitForInput(lockOutput)
##Geo DB Cities - END

#CORE - END