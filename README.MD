# py-graphql-mapper

## Introduction

This library acts as a mapper between python and GraphQL languages for a GraphQL client allowing a code-first approach when fetching data against a GraphQL server.
The objective is to integrate GraphQL entities into python language in order to simplify as much as possible the creation of GraphQL operations and retrieval of GraphQL responses avoiding massive "copy&paste" work.

The package does not use any third-party libraries, it relies only on python 3 standard libraries. 

This document gives an overview of the functionalities available in this packages, it is strongly advised to read the other documents in order to have a more thorough understanding.


## Table of Contents

1. [Usage in a nutshell](#usage-in-a-nutshell)
    1. [From GraphQL object type to python class](#from-graphql-object-type-to-mapped-python-class)
    2. [From mapped python class to generation of a query](#from-mapped-python-class-to-generation-of-a-query)
    2. [From mapped python class to generation of a mutation](#from-mapped-python-class-to-generation-of-a-mutation)
    3. [Retrieval of a response](#retrieval-of-a-response)
    4. [Execution of a mutation](#execution-of-a-mutation)
2. [Installation](#installation)
3. [Final words](#final-words)
    1. [Potential further implementations](#potential-further-implementations)


## Usage in a nutshell

### From GraphQL object type to mapped python class

Given a GraphQL object type

```
myCustomObject {
    myString
    myCode
    myList
}
```

The following class definition will be able to reproduce the GraphQL syntax for the object above

```python
from pygqlmap import GQLObject

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

More details [here](https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap/README.MD#creation-of-a-mappable-python-object)

### From mapped python class to generation of a query

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
from pygqlmap import GQLOperation, GQLArgsSet
from pygqlmap.enums import OperationType, ArgType
from pygqlmap.gqlTypes import ID

query = GQLOperation(OperationType.query, myCustomObject, 'myQuery')

argsCntrs = GQLArgsSet()
argsCntrs.addArg('myString', ID('CNY'))
query.setArgs(argsCntrs, ArgType.LiteralValues)

print(query.exportGqlSource)
```

The property _exportGqlSource_ in this case will generate the above GraphQL syntax

Example of querying using *requests* library:

```python
response = request("POST", "<graphQLServerUrl>", json={ "query": query.exportGqlSource }, headers=<headers>)
```

More details [here](https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap/README.MD#gqloperation)

A suite of use cases [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/README.MD#L23)


### From mapped python class to generation of a mutation

Given a GraphQL mutation

```
mutation myManualMutationUpdateRepository  { 
    updateRepository ( input: { repositoryId: "someID", hasIssuesEnabled: false }  ) 
    { 
        clientMutationId     
        repository   {
            allowUpdateBranch       
            autoMergeAllowed     
            codeowners   { 
                errors   
                { 
                    column     
                    kind     
                    line     
                    message     
                    path     
                    source     
                    suggestion  
                } 
            } 
}
```

The following GQLOperation instantiation will be able to reproduce the mutation

```python
from pygqlmap import GQLOperation, GQLArgsSet
from pygqlmap.enums import OperationType, ArgType

mutation = GQLOperation(OperationType.mutation, updateRepository, operationName='myManualMutationUpdateRepository', logProgress=True)

argsUpdateRepository = GQLArgsSet()
argsUpdateRepository.addArgs({ 'repositoryId': "someID", 'hasIssuesEnabled': False })

mutation.setArgs([argsUpdateRepository], ArgType.LiteralValues)

print(query.exportGqlSource)
```

The property _exportGqlSource_ in this case will generate the above GraphQL syntax

Example of querying using *requests* library:

```python
response = request("POST", "<graphQLServerUrl>", json={ "query": query.exportGqlSource }, headers=<headers>)
```

Some use cases [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/README.MD#L48)


### Retrieval of a response

With the following python code

```python
from pgqlmCore.network import GQLResponse

gqlResponse = GQLResponse(response)

gqlResponse.mapGQLDataToObj(query.obj)

print('resultObject: ' + str(gqlResponse.resultObject))
```

The response from the GraphQL server will be mapped in _gqlResponse_ object, _gqlResponse.resultObject_ will contain the mapped python object _myCustomObject_ previously defined

More details [here](https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap/README.MD#parsing-of-a-response)


## Installation

The functionalities described above require the installation of pygqlmap package. From the repo main folder:

```
python setupPyGqlMap install
```

More details [here](https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap/README.MD#installation)



## Final words

The development is in progress, so far the library allows the creation of basic queries and mutations (python language -> GraphQL language) and parsing of responses from a GraphQL server (GraphQL language -> python language):

### Potential further implementations

* CLI allowing to automatic generate python files containing mapped python classes \*_already in progress_\* (<u>mapping from a GraphQL object type to a python class WILL NOT BE NECESSARY ANYMORE<u>)

* Friendlier usage of library \*_already in progress_\* (e.g.: avoiding the necessity of implementing the init function for GQLObjects)

* Extending the mapping for more articulated 'scalar' types (e.g.: date, datetime, ...)

* Advanced management of arguments/input fields (non null, default, objects, ...)

* Usage of Aliases

* Usage of Fragments

* Usage of Directives

* more...


If you find this library useful and/or want the developments to proceed please [donate](https://github.com/sponsors/dapalex)