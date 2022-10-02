# py-graphql-mapper

## Introduction

This library is meant to be a python-graphql mapper for a GraphQL client allowing a code-first approach when fetching data against a GraphQL server.
The aim is to simplify as much as possible the development of queries and retrieval of responses.

There are no third-party libraries involved, it relies only on python standard libraries (>=3.10.6). 

## Query Generation

Example using *requests* library:

```python
from src import OperationType, GQLOperation

query = GQLOperation(OperationType.query, myCustomObject, 'myQuery')
response = request("POST", graphQLServerUrl, json={ "query": query.exportGqlSource }, headers=headers)
```

To generate a GraphQL Query:

* Instantiate a [GQLOperation](#gqloperation) object
* Call *exportGQLSource* property of the object

The creation of *myCustomObject* can be seen below.

## Creation of a mappable python object

### GQLObject

*GQLObject* is the super class needed in order to create a python class representing a GraphQL object.

Example:

```python
from src import GQLObject

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

Requirements for the creation:

* Inheriting GQLObject class
* If the class is the root query field its name has to be the same as how the GraphQL server names it
* Fields must be:
    * statically declared 
* The builtin function *__init__* has to be implemented. Within this function:
    * Fields must be initialized with a dummy value (the value will be ignored)
    * At the end of the function *super().__init__()* must be called

The example above will correspond to the following GraphQL object

```
myCustomObject {
    myString
    myCode
    myList
}
```

A more complex object, containing nested objects and connections, can be seen [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/models/countries.py)

### GQLConnection

*GQLConnection* is the super class needed in order to create a python class representing a GraphQL Connection.

Example using *myCustomObject* from above:

```python
class MyConnection(GQLConnection): 
    
    def __init__(self):
        super().__init__(GQLEdges(myCustomObject())) 
```

Requirements for the creation:

* Inheriting GQLConnection class
* If the class is the root query field its name has to be the same as how the GraphQL server names it
* The builtin function __init__(self) has to be implemented. Within this function:
    * At the end of the function super().__init__() must be called passing as parameter the construction of GQLEdges object with the node python class as parameter.


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

## GQLOperation

GQLOperation is the object in charge of composing a GraphQL query ready to be sent to a GraphQL server.
The instantiation requires the following parameters:

* operationType: Enum *OperationType* containing:
    * Query
    * Mutation (not implemented yet)

* dataType: the python [class] (#gqlobject) or the python connection [class](#gqlconnection) created 

Optional parameters are:

* name: string used to give the query a name
* logProgress: boolean activating basic logs of the GQL generation progress

Example using MyConnection above:

```python
query = GQLOperation(OperationType.query, MyConnection, 'myQuery')

response = request("POST", graphQLServerUrl, json={ "query": query.exportGqlSource }, headers=headers)
```

The code above, through the function *exportGqlSource* will generate the following GraphQL object

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

#### Arguments management

Arguments can be added to a GQLOperation through the function *setArgs*.

```python
query = GQLOperation(OperationType.query, myCustomObject, 'myQuery')

args = GQLArgs()

args.addArg(GQLArg(name='myCode', value=3))
args.addArg(GQLArg(name='myString', value='MTE='))

query.setArgs(args, ArgType.Variables)
```

##### GQLArgs

*GQLArgs* is the container of a set of arguments.

Example of creation of arguments for a query using MyQuery and MyConnection from above.

Given the following GQL Query:

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

The following code, using *ArgType.EmbeddedArgs*

```python
query = GQLOperation(OperationType.query, MyConnection, 'myQuery')
argsCntrs = GQLArgs('MyConnection.edges.node')
argsCntrs.addArg(GQLArg('myString', 'CNY'))
query.setArgs([argsCntrs], ArgType.EmbeddedArgs)
```

will correspond to

```
query myQuery {
    MyConnection {
        totalCount
        edges {
            cursor
            node(myString: "CNY") {
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
If the location is root no location needs to be passed.

After the construction arguments can be added using the function *addArg* which takes a *GQLArg* object as parameter.

*setArgs* function requires the following parameters:

* argSets: a list of [GQLArg](#gqlargs) objects
* argsType: a value from the enum [ArgType](#arg)
    * EmbeddedArgs: argument values will be directly inserted within the query 
    * Variables: argument keys in the query, argument values in variables

Example using ArgType.Variables:

```python
...
query.setArgs([argsCntrs], ArgType.EmbeddedArgs)
...
response = request("POST", graphQLUrl, json={ "query": query.exportGqlSource, "variables": query.exportGQLVariables }, headers=headers)
```

will correspond to

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

It is also possible removing arguments from a created GQLArgs calling *removeArg*

#### Dynamic visibility of fields

In case it is needed to fetch lesser data than the original python object created it is possible to hide fields after the creation of the object.

Given some python object created like this:

```python

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

It is possible to generate a query hiding fields *myCode* and *fieldB*.
This can be done using *setShow* function:

```python
query = GQLOperation(OperationType.query, MyConnection, 'myQuery')
query.setShow('myCustomObject.myCode', False)
query.setShow('myCustomObject.myNestedfield.fieldB', False)
```

## Parsing of a response

Responses received from a GraphQL server can be automatically converted in the python object created for the query


```python
    response = request("POST", graphQLServerUrl, json=json={ "query": query.exportGqlSource }, headers=headers)

    gqlResponse = GQLResponse(response)
    gqlResponse.mapGQLDataToObj(query.data)

    print('resultObject: ' + str(gqlResponse.resultObject))
```

To parse the GraphQL response:

* Instantiate a [GQLResponse](#gqlresponse) python object passing the response received from the server

* Call mapGQLDataToObj function passing  query.data, the object that has been used for the communication with the server

### GQLResponse

The purpose of GQLResponse object is managing the responses received from a GraphQL server.

The constructor requires the following parameter:

* response: response received after a POST request to a GraphQL server

The function *mapGQLDataToObj* maps all the information from the HTTP response to the relating python object.
It requires the following parameter:

* queryObject: the python object that has been created for the [GQLOperation](#gqloperation)

Optional parameter:

* buildType: enum *BuildingType* defining how the response will be parsed (right now available only the *Standard* value):
    * Standard: GQLObject fields set to hidden will be present with value None when the response gets generated
    * CreateNewClass: creates a new class type following the content of the response (not implemented yet)
    * AlterClass: creates a new class following the data within the response (not implemented yet)

## Test

Tests have been made using GeoDB Cities API,
*requests* library has been used for the HTTP requests to the GraphQL server.
In order to launch the tests an API key has to be set [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/gdbcApi/consts.py), available with a free subscription at https://rapidapi.com/wirefreethought/api/geodb-cities-graphql/


## Final words

There are more functionalities in the library which have not been documented here, the development is still in progress.

This project is my first experience with python language and GraphQL APIs so please do not hesitate to reach me out for any correction or improvement, any kind of help is welcome and appreciated.

So far the library allows the creation of basic queries (python language -> GraphQL language) and parsing of responses from a GraphQL server (GraphQL language -> python language):

* Query operations
* Basic Arguments using variables
* Basic Arguments embedded in query

Not implemented nor tested yet:

* Management of arguments as non null or having a default
* Aliases
* Fragments
* Interfaces
* Directives
* Inline Fragments
* Meta fields
* Mutation operations
