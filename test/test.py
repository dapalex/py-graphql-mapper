import sys, os
 
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'pygraphqlmapper'))
print(sys.path)
import asyncio
from unitTest import * 

# wrapper = redirectOutputToFile('Test.log')

asyncio.run(testPlainNestedQueryCurrencies())
asyncio.run(testPlainComplexQueryCountries())
asyncio.run(testNestedObject())
asyncio.run(testComplexObject())
asyncio.run(testNestedObjectShowChange())
asyncio.run(testComplexObjectShowChange())
asyncio.run(testNestedObjectWithArgsAndVariables()) 
asyncio.run(testNestedObjectWithEmbeddedArgs())
asyncio.run(testComplexObjectWithArgsAndVariables()) 
asyncio.run(testComplexObjectWithEmbeddedArgs())
asyncio.run(testComplexObjectWithEmbeddedArgs2())
asyncio.run(testNestedObjectShowChangeWithArgsAndVariables())
asyncio.run(testNestedObjectWithEmbeddedArgsAndCursorPaginationArgs())
asyncio.run(testComplexObjectShowChangeWithArgsAndVariables()) 
asyncio.run(testComplexObjectWithEmbeddedArgs2WithLog()) 

# restoreOutput(wrapper)
