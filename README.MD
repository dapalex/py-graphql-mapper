# py-graphql-mapper

## Introduction

This library act as a mapper between python and GraphQL languages for a GraphQL client allowing a code-first approach when fetching data against a GraphQL server.
The objective is to translate GraphQL entities into python objects and viceversa in order to simplify as much as possible the creation of GraphQL operations and retrieval of GraphQL responses avoiding massive "copy&paste" work.

The package does not use any third-party libraries, it relies only on python 3 standard libraries. 


## Table of Contents

1. [Usage in a nutshell](#usage-in-a-nutshell)
    1. [From GraphQL object type to python class](#from-graphql-object-type-to-python-class)
    2. [Usage of python class for Query generation](#usage-of-python-class-for-query-generation)
    3. [Retrieval of a response](#retrieval-of-a-response)
    4. [Execution of a mutation](#execution-of-a-mutation)
2. [Installation](#installation)
3. [Final words](#final-words)


## Usage in a nutshell

### From GraphQL object type to python class

Given a GraphQL object type

```
myCustomObject {
    myString
    myCode
    myList
}
```

The following class definition will be able to reproduce object

```python
from pygqlmap.components import GQLObject

class myCustomObject(GQLObject): 
    myString: str
    myCode: int
    myList: list
```

More details [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/pygqlmap/README.MD#creation-of-a-mappable-python-object)

### Usage of python class for Query generation

Given a GraphQL query

```
query myQuery {
    myCustomObject(myString: "CNY") {
        myString
        myCode
        myList
    }
}
```

The following GQLOperation instantiation will be able to reproduce the query

```python
from pygqlmap.components import GQLOperation, GQLArgsSet
from pygqlmap.enums import OperationType, ArgType
from pygqlmap.gqlTypes import ID

query = GQLOperation(OperationType.query, myCustomObject, 'myQuery')

argsCntrs = GQLArgsSet()
argsCntrs.addArg('myString', ID('CNY'))
query.setArgs(argsCntrs, ArgType.LiteralValues)

print(query.exportGqlSource)
```

The property _exportGqlSource_ will generate the above GraphQL query

Example of querying using *requests* library:

```python
response = request("POST", "<graphQLServerUrl>", json={ "query": query.exportGqlSource }, headers=<headers>)
```

More details [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/pygqlmap/README.MD#gqloperation)

A suite of use cases [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/README.MD#L11)

### Retrieval of a response

With the following python code

```python
from pgqlmCore.network import GQLResponse

gqlResponse = GQLResponse(response)

gqlResponse.mapGQLDataToObj(query.obj)

print('resultObject: ' + str(gqlResponse.resultObject))
```

The response from the GraphQL server will be mapped in _gqlResponse_ object: _gqlResponse.resultObject_ will contain the object _myCustomObject_ defined

More details [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/pygqlmap/README.MD#parsing-of-a-response)


### Execution of a mutation

Mutations can be executed in two ways:

```python
from pygqlmap.enums import OperationType, ArgType
from pygqlmap.components import GQLOperation, GQLArgsSet

coreMutation = GQLOperation(OperationType.mutation, updateRepository, operationName='myManualMutationUpdateRepository', logProgress=True)

argsUpdateRepository = GQLArgsSet()
argsUpdateRepository.addArgs({ 'repositoryId': "R_kgDOHasdI4g", 'hasIssuesEnabled': False })

coreMutation.setArgs([argsUpdateRepository], ArgType.LiteralValues)

query = GQLOperation(OperationType.mutation, myCustomObject, 'myMutation')
response = request("POST", graphQLServerUrl, json={ "query": query.exportGqlSource }, headers=headers)
```

A suite of use cases [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/README.MD#L110)

## Installation

The functionalities described above require the installation of pygqlmap package. From the repo main folder:

```
python setupPyGqlMap install
```

More details [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/pygqlmap/README.MD#installation)

