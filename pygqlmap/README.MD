# py-graphql-mapper - pygqlmap

## Introduction

This document explains in detail how the pygqlmap library works.


## Table of Contents

1. [Installation](#installation)
2. [Creation of a mappable python object](#creation-of-a-mappable-python-object)
    1. [GQLObject](#gqlobject)
    2. [GQLConnection](#gqlconnection)
        1. [GQLEdges](#gqledges)
3. [GQLOperation](#gqloperation)
    1. [Query](#query)
    2. [Mutation](#mutation)
    3. [Arguments management](#arguments-management)
        1. [GQLArgs](#gqlargs)
    4. [Dynamic visibility of fields](#dynamic-visibility-of-fields)
4. [Parsing of a response](#parsing-of-a-response)
    1. [GQLResponse](#gqlresponse)
5. [Scalar types mapping](#scalar-types-mapping)


## Installation

This module can be installed launching the following command from the main folder

```
python setupPyGqlMap.py install
```

The functionalities of this package will be available under _pygqlmap_ module name.


## Creation of a mappable python object

### GQLObject

*GQLObject* is the base class needed in order to create a python class representing a GraphQL object.

Example:

```python
from pygqlmap.components import GQLObject

class myCustomObject(GQLObject): 
    myString: str
    myCode: int
    myList: list
    
    def __init__():
        self.myString = ''
        self.myCode = 0
        self.myList = []

        super().__init__()
```

Requirements for the class definition:

* Inheriting _GQLObject_ class
* Fields must be:
    * statically declared 
* *\_\_init\_\_* function has to be implemented. Within:
    * Primitive fields (int, float, str, ...) must be initialized with a dummy value (the value will be ignored)
    * Fields being GQLObject or GQLConnection types must be instantiated
    * *super().\_\_init\_\_()* must be called (at the end of the function)
* If the class is the root GraphQL object of a query its name has to match the name expected by the GraphQL server.

The example above will be able to generate the following GraphQL object

```
myCustomObject {
    myString
    myCode
    myList
}
```

A use case can be seen [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectTest.py) 

Note: further developments should be able to avoid the implementation of *__init__* function.


### GQLConnection

*GQLConnection* is the base class needed in order to create a python class representing a GraphQL Connection.

Example using *myCustomObject* from above:

```python
from pygqlmap.components import GQLConnection, GQLEdges

class MyConnection(GQLConnection): 
    
    def __init__(self):
        super().__init__(GQLEdges(myCustomObject())) 
```

Requirements for the creation:

* Inheriting GQLConnection class
* *\_\_init\_\_* function has to be implemented. Within:
    * *super().\_\_init\_\_()* must be called passing _[GQLEdges](#gqledges)_ object as parameter 
* If the class is the root GraphQL object of a query its name has to match the name expected by the GraphQL server.

The example above will correspond to the following GraphQL object

```
MyConnection {
    totalCount
    edges {
        cursor
        node {
            myString
            myCode
            myList
        }
    }
}
```

A use case can be seen [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/connectionObjectTest.py) 


#### GQLEdges

This class is in charge of managing the internal structure of a connection automatically.
It takes the node object as parameter in the constructor, the parameter can be omitted if retrieving the node is not necessary.

```python
...
GQLEdges(myCustomObject())
...
```

The construction above will be able to reproduce the current structure

```
edges {
        cursor
        node {
            myString
            myCode
            myList
        }
}
```

Currently the Connection structure is internally managed, with the next developments the management of connections should become more flexible and straightforward. 


## GQLOperation

GQLOperation is the object in charge of composing a GraphQL query or mutation.

### Query

Example:

```python
from pygqlmap.enums import OperationType
from pygqlmap.components import GQLOperation

query = GQLOperation(OperationType.query, MyConnection, 'myQuery')

print(query.exportGqlSource)
```

The constructor requires the following parameters:

* operationType: Enum *OperationType* (Query)
* dataType: the [python class](#gqlobject) or the [python connection class](#gqlconnection) expected from the response

Optional parameters are:

* operationName: string used to give a name to the operation
* logProgress: boolean activating basic logs of the GQL generation progress

The _MyConnection_ object will be available in the field _obj_ (_query.obj_)

The function *exportGqlSource* will generate the following GraphQL syntax:

```
query myQuery {
    MyConnection {
        totalCount
        edges {
            cursor
            node {
                myString
                myCode
                myList
            }
        }
    }  
}
```

Example using _requests_:

```python
response = request("POST", graphQLServerUrl, json={ "query": query.exportGqlSource }, headers=headers)
```

Use cases can be seen [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/) 


### Mutation

Supposed a GQLObject _updateRepository_ created for a mutation

```python

class Repository(GQLObject):
    ....content of Repository....

class updateRepository(GQLObject):
    clientMutationId: str
    repository: Repository
    
    def __init__(self):
        self.clientMutationId = ''
        self.repository = Repository()
        super().__init__()
```

Similarly to queries the creation of a mutation would be:

```python
from pygqlmap.enums import OperationType, ArgType
from pygqlmap.components import GQLOperation, GQLArgsSet

coreMutation = GQLOperation(OperationType.mutation, updateRepository, operationName='myManualMutationUpdateRepository', logProgress=True)

argsUpdateRepository = GQLArgsSet()
argsUpdateRepository.addArg("input", { 'repositoryId': "someID", 'hasIssuesEnabled': False })

coreMutation.setArgs([argsUpdateRepository], ArgType.LiteralValues)

response = request("POST", graphQLServerUrl, json={ "query": query.exportGqlSource }, headers=headers)
```

The function *exportGqlSource* will generate the following GraphQL syntax:

```
mutation myManualUpdateRepository  { 
    updateRepository(input:  { repositoryId: "R_kgDOH7MI4g", hasIssuesEnabled: false } ) { 
        clientMutationId     
        repository   { 
            ....content of Repository....
        } 
    } 
}
```

Note: Next developments shall allow the usage of automatically generated classes for the queries and mutations

Use cases can be seen [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstmutation/) 


### Arguments management

Arguments can be added to a _GQLOperation_, these can be done through _GQLArgs_ and added through _setArgs_ function.

Example:

```python
from pygqlmap.enums import OperationType, ArgType
from pygqlmap.components import GQLOperation, GQLArgsSet

query = GQLOperation(OperationType.query, myCustomObject, 'myQuery')

args = GQLArgsSet()

args.addArg(argKey='myCode', argValue=3)
args.addArg(argKey='myString', argValue='MTE=')

query.setArgs(args, ArgType.Variables)

print(query.exportGqlSource)
print(query.exportGqlVariables)
```

_exportGqlSource_ will generate the following GraphQL object:

```
query myQuery($myCode: Int, $myString: String) { 
    myCustomObject(myCode: $myCode, myString: $myString) {
        myString
        myCode
        myList
    }
}
```

and _exportGqlVariables_ the following variables:

```
{
    "myCode": 3,
    "myString": "MTE="
}
```

Example using _requests_:

```python
request("POST", graphQLUrl, json={ "query": query.exportGqlSource, "variables": query.exportGqlVariables }, headers=headers)
```

Note: Right now Arguments as Variables are not supported for mutations

Use cases for queries can be seen here:
[Object with arguments as literal values](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectArgs_LiteralValuesTest.py) 
[Object with arguments and variables ](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectArgs_VariablesTest.py) 
[Connection with arguments and variables](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/connectionObjectArgs_VariablesTest.py)  
[Connection with arguments as literal values](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/connectionobjectArgs_LiteralValuesTest.py) 


#### GQLArgs

*GQLArgs* is the container of a set of arguments.

The following code, using *ArgType.LiteralValues*

```python
from pygqlmap.enums import OperationType, ArgType
from pygqlmap.components import GQLOperation, GQLArgsSet
from pygqlmap.gqlTypes import ID

query = GQLOperation(OperationType.query, countries, 'myCountriesQuery')
argsRegion = GQLArgsSet('countries.edges.node.region')
argsRegion.addArg('code', ID("CN"))
query.setArgs([argsRegion], ArgType.LiteralValues)

response = request("POST", graphQLUrl, json={ "query": query.exportGqlSource, "variables": query.exportGQLVariables }, headers=headers)
```

The corresponding GraphQL sintax will be:

```
query myCountriesQuery {
    countries {
        totalCount
        edges {
            cursor
            node {
                region(code: "CN"){
                    code
                    some
                    else
                }
                myString
                myCode
                myList
            }
        }
    }  
}
```

The constructor takes the following parameter:

* location: it represents the path (passed in dot notation) where the args will be located within the query.
If the location is root there is no need to pass the parameter.

Arguments can be added to _GQLArgs_ using the function _addArg_ which takes a _GQLArg_ object as parameter.

_setArgs_ function requires the following parameters:

* argSets: a list of [GQLArg] objects
* argsType: a value from the enum [ArgType](#arg)
    * EmbeddedArgs: argument values will be directly inserted within the query 
    * Variables: argument keys in the query, argument values in variables

Use case involving the objects in the example can be seen [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/complexObjectTest.py) 


Following the same ...... using ArgType.Variables:

```python
.......
argsSet = GQLArgsSet()
argsSet.addArg('dryRun', False)
query.setArgs(argsSet, ArgType.Variables)

response = requests.request('POST', url=githubUrl, 
                            json= { "query": query.exportGqlSource, "variables": query.exportGQLVariables }, 
                            headers=githubHeaders)
.......
```

The corresponding GraphQL sintax will be:

```
query myQuery($myString: String) {
    MyConnection {
        totalCount
        edges {
            cursor
            node(myString: $myString) {
                myString
                myCode
                myList
            }
        }
    }  
}
```

with variables

```
{
    "myString": "CNY"
}
```

An use case can be seen [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectArgs_VariablesTest.py) 


~~~~~~~~~~It is also possible removing arguments from a created GQLArgs calling *removeArg*~~~~~~~~~~~~


### Dynamic visibility of fields

For an operation it is possible to hide fields of a GQLObject if no needed.

Given a python object created in this way:

```python
from pgqlmCore import GQLObject

class myNestedObject(GQLObject):
    fieldA: str
    fieldB: int

    def __init__():
        self.fieldA = ''
        self.fieldB = 0

        super().__init__()

class myCustomObject(GQLObject): 
    myString: str
    myCode: int
    myNestedfield: myNestedObject
    
    def __init__():
        self.myString = ''
        self.myCode = 0
        self.myNestedObject = myNestedObject()

        super().__init__()
```
The mapped GraphQL version of a query would be

```
query {
    myCustomObject {
        myString
        myCode
        myNestedfield {
            fieldA
            fieldB
        }
    }
}
```

It is possible to 'temporarily' hide unnecessary fields, this can be done using *setShow* function:

With the following code

```python
from pgqlmCore.enums import OperationType
from pgqlmCore.gqlTypes import GQLOperation

query = GQLOperation(OperationType.query, MyConnection, 'myQuery')
query.setShow('myCustomObject.myCode', False)
query.setShow('myCustomObject.myNestedfield.fieldB', False)
query.exportGqlSource
```

the mapped GraphQL version of _query_ would become

```
query myQuery{
    myCustomObject {
        myString
        myNestedfield {
            fieldA
        }
    }
}
```

hiding _myCode_ and _fieldB_.

An use case can be seen [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectChangeVisibilityTest.py) 


## Parsing of a response

Responses received from a GraphQL server can be automatically converted into a python object declared for the query through _mapGQLDataToObj_ function


```python
    from pgqlmCore import GQLResponse
    ....
    response = request("POST", graphQLServerUrl, json=json={ "query": query.exportGqlSource }, headers=headers)

    gqlResponse = GQLResponse(response)
    gqlResponse.mapGQLDataToObj(query.obj)

    gqlResponse.printMessageOutput()
    print('resultObject: ' + str(gqlResponse.resultObject))
```

To parse the GraphQL response:

* Instantiate a [GQLResponse](#gqlresponse) python object passing the response received from the server

* Call mapGQLDataToObj function passing the _obj_ field within query object that has been used for the communication with the server (or alternatively an empty instance of the class).

_printMessageOutput_ function will print the outcome of the request


### GQLResponse

The purpose of GQLResponse object is managing the responses received from a GraphQL server.

The constructor requires the following parameter:

* response: the response received after a POST request to a GraphQL server

The function *mapGQLDataToObj* maps all the information from the HTTP response to the relating python object.
It requires the following parameter:

* queryObject: the python object that has been created for the [GQLOperation](#gqloperation)

Optional parameter:

* buildType: enum *BuildingType* defining how the response will be parsed (right now available only the *Standard* value):
    * Standard: GQLObject fields set to be hidden when the query gets generated will be present with value None
    * CreateNewClass: creates a new class type following the content of the response (not implemented yet)
    * AlterClass: creates a new class following the data within the response (not implemented yet)


## Scalar types mapping

So far the following GraphQL scalar types are being mapped to python types:

* Int -> int
* String -> str
* Boolean -> bool
* Float -> float
* ID -> ID class (_pgqlmCore.gqlTypes.ID_)
