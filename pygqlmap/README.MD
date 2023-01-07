# pygqlmap

*THIS DOCUMENT IS UNDER REVIEW*

## Introduction

This document explains in detail how the core of the mapping works.
This module can be used to manually create python classes corresponding to a GraphQL type (or a customized version).

## Table of Contents

1. [Creation of a mappable python object](#creation-of-a-mappable-python-object)
    1. [GQLObject](#gqlobject)
2. [Creation of a operation](#creation-of-an-operation)
    1. [GQLQuery](#gqlquery)
    2. [GQLMutation](#qglmutation)
        1. [Arguments management](#arguments-management)
3. [Dynamic visibility of fields](#dynamic-visibility-of-fields)
4. [Parsing of a response](#parsing-of-a-response)
    1. [GQLResponse](#gqlresponse)


## Creation of a mappable python object

In order yo create a python class representing a GraphQL object _GQLObject_ class has to be inherited.

### GQLObject

*GQLObject* is the base class needed in order to create a python class representing a GraphQL object.

Example:

```python
from pygqlmap.components import GQLObject

class myCustomObject(GQLObject): 
    myString: str
    myCode: int
    myList: list
```

Requirements for the class definition:

* Inheriting _GQLObject_ class
* Fields must be statically declared 

The example above will be able to generate the following GraphQL object

```
myCustomObject {
    myString
    myCode
    myList
}
```

A use case can be seen [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/tstquery/simpleObjectTest.py) 


### Adding arguments 

If arguments are needed a field '_args' must be added to the created class. 

Given the example above

```python
from pygqlmap.components import GQLObject

class myCustomObject(GQLObject): 
    myString: str
    myCode: int
    myList: list
    _args: MyArgs
```

The definition of this field must be a class:
    * Inheriting from _GQLArgsSet_ and _GQLObject_
    * With fields statically declared 

```python
from pygqlmap.components import GQLObject

class MyArgs(GQLArgsSet, GQLObject): 
    firstArg: str
    secondArg: ID
```

Instantiating the classes and calling _exportGqlSource_ property

```python
myObj = myCustomObject()
myObj._args.firstArg = 'myArgument'
myObj._args.secondArg = ID('myID')

myObj.exportGqlSource
```

the following GraphQL object will be generated

```
myCustomObject(firstArg: "myArgument", secondArg: "myID") {
    myString
    myCode
    myList
}
```


## Creation of an operation

GraphQL Operations can be mapped in the same way as for GraphQL types above. In this case _GQLQuery_ class for a query or _GQLMutation_ for a mutation has to be inherited.

### GQLQuery

GQLQuery is the base class in charge of composing a GraphQL query.

Example:

```python
from pygqlmap.components import GQLObject

class CountriesConnection(GQLObject):
   totalCount: int ##NON NULL
   edges: CountryEdge ##NON NULL
   pageInfo: ConnectionPageInfo ##NON NULL

class CountriesArguments(GQLArgsSet, GQLObject):
    currencyCode: str
    namePrefix: str
    
class countries(GQLQuery):
   _args: CountriesArguments
   type: CountriesConnection
   
```

The creation of the operation requires:

* Inheriting _GQLQuery_/_GQLMutation_ class
* Declaring a field 'type' representing the content of the query
* If arguments are needed a field '_args' has to be declared. The class representing its type has to:
    * Inherit from _GQLArgsSet_ and _GQLObject_
    * Fields must be statically declared 

The base class can be customized further with these optional definitions:

* name: string used to give a name to the operation
* _argsType: how the arguments will be exported (default - literal values)

Instantiating the class and calling _exportGqlSource_ property

```python
from pygqlmap.enums import ArgType

myQuery = countries()
myQuery._args.currencyCode = 'USD'
myQuery._args.namePrefix = "unit"

myQuery.name = 'myFirstQuery'
myQuery._argsType = ArgType.Variables
myQuery.exportGqlSource
```

will generate the following GraphQL syntax:

```
query myFirstQuery ($currencyCode: String, $namePrefix: String){
    countries(currencyCode: $currencyCode, namePrefix: $namePrefix) {
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

Calling the relating GraphQL API server (example using _requests_):

```python
response = request("POST", graphQLServerUrl, json={ "query": query.exportGqlSource }, headers=headers)
```

Use cases can be seen [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/tstquery/) 


### GQLMutation

As per _GQLQuery_ GQLMutation is the base class in charge of composing a GraphQL mutation.

Supposed a GQLObject _updateRepository_ created for a mutation

```python

class Repository(GQLObject):
    ....content of Repository....

class updateRepository(GQLMutation):
    clientMutationId: str
    repository: Repository
```

Similarly to queries the creation of a mutation would be:

```python
coreMutation = updateRepository()
coreMutation.name = 'myManualMutationUpdateRepository'

coreMutation._args._input.repositoryId = "someID"
coreMutation._args._input.hasIssuesEnabled = False

response = request("POST", graphQLServerUrl, json={ "query": coreMutation.exportGqlSource }, headers=headers)
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

Use cases can be seen [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/tstmutation/) 


### Arguments management

Arguments can be added to a mapped operation, these can be done creating a class inheriting from _GQLArgsSet_ and _GQLObject_.

Example:

```python
from pygqlmap.enums import ArgType

query = myCustomQUery()
query.name = 'myQuery'

query._args.myCode = 3
query._args.myID = ID('MTE=')

query._argsType = ArgType.Variables

print(query.exportGqlSource)
print(query.exportGqlVariables)
```

_exportGqlSource_ will generate the following GraphQL object:

```
query myQuery($myCode: Int, $myID: ID) { 
    myCustomObject(myCode: $myCode, myID: $myID) {
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
    "myID": "MTE="
}
```

Example using _requests_:

```python
request("POST", graphQLUrl, json={ "query": query.exportGqlSource, "variables": query.exportGqlVariables }, headers=headers)
```

Note: Right now Arguments as Variables are not supported for mutations

Use cases for queries can be seen here:
[Object with arguments as literal values](https://github.com/dapalex/py-graphql-mapper/blob/main/test/tstquery/simpleObjectArgs_LiteralValuesTest.py) 
[Object with arguments and variables ](https://github.com/dapalex/py-graphql-mapper/blob/main/test/tstquery/simpleObjectArgs_VariablesTest.py) 
[Connection with arguments and variables](https://github.com/dapalex/py-graphql-mapper/blob/main/test/tstquery/connectionObjectArgs_VariablesTest.py)  
[Connection with arguments as literal values](https://github.com/dapalex/py-graphql-mapper/blob/main/test/tstquery/connectionobjectArgs_LiteralValuesTest.py) 


## Dynamic visibility of fields

For an operation it is possible to hide fields of a GQLObject if no needed.

Given a python object created in this way:

```python
from pgqlmCore import GQLObject

class myNestedObject(GQLObject):
    fieldA: str
    fieldB: int

class myCustomObject(GQLQuery): 
    myString: str
    myCode: int
    myNestedfield: myNestedObject
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
query = MyConnection()
query.name = 'myQuery'
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

An use case can be seen [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/tstquery/simpleObjectChangeVisibilityTest.py) 


## Parsing of a response

Responses received from a GraphQL server can be automatically converted into a python object declared for the query through _mapGQLDataToObj_ function


```python
    from pgqlmCore import GQLResponse
    ....
    response = request("POST", graphQLServerUrl, json=json={ "query": query.exportGqlSource }, headers=headers)

    gqlResponse = GQLResponse(response)
    gqlResponse.mapGQLDataToObj(query.type)

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

* queryObject: the python object that has been created for the [operation](#creation-of-an-operation)

Optional parameter:

* buildType: enum *BuildingType* defining how the response will be parsed (right now available only the *Standard* value):
    * Standard: GQLObject fields set to be hidden when the query gets generated will be present with value None
    * CreateNewClass: creates a new class type following the content of the response (not implemented yet)
    * AlterClass: creates a new class following the data within the response (not implemented yet)

