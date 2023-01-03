# py-graphql-mapper - Generator

THIS DOCUMENT IS UNDER REVIEW

## Introduction

This module generates python classes corresponding to GraphQL objects present in a schema, secondarily can save a GraphQL schema in a json format.
The generator can be launched through [command line](#usage-via-command-line) or [programmatically](#usage-programmatically).

It depends on [pygqlmap](#https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap) module and uses requests for communications with GraphQL servers.


## Table of Contents

1. [Functionalities](#functionalities)
    1. [Usage programmatically](#usage-programmatically)
    2. [Usage via command line](#usage-via-command-line)
        1. [JSON args file](#json-args-file)
2. [Using the generated files](#using-the-generated-files)


## Functionalities 

Two functionalities are available:

1) Generate python classes from a schema
2) Download a schema from a GraphQL server API


## Usage programmatically

The class in charge of the generation is _CodeGenerator_.

First step is obtaining the schema object, this can be done:

* Querying the GraphQL server:

```python
from pgqlmGenerator.network import fetchSchemaObject
from pgqlmGenerator.queryPresets import querySchemaAndTypes

schemaObject = fetchSchemaObject(<graphQLUrl>, <HTTPHeaders dictionary>, querySchemaAndTypes)
```

* or passing a schema as JSON:
 
```python
from pgqlmGenerator.generator import buildSchema

schemaObject = buildSchema(schemaJsonString)
```

Obtained the schema the following CodeGenerator function has to be called:

```python
from pgqlmGenerator.generator import CodeGenerator
from pgqlmGenerator.queryPresets import querySchemaAndTypes

CodeGenerator.generateCode(schemaObject, folder='test\\output\\github\\', logProgress=False, addDescription=True)
```

Required parameters:

* schemaObj: the schema as python object
* folder: the destination folder where the created python files will be saved

Optional parameters:

* customTypes: dictionary containing the mapping of GraphQL scalar types with declaration different from the [standard GraphQL scalar types](https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap/README.MD#scalar-types-mapping)) (an example can be seen [here](https://github.com/dapalex/py-graphql-mapper/blob/main/cli_args.json))
* logProgress: makes the generation verbose
* addDescription: boolean telling if descriptions have to be added to the generated classes (strongly advised to be True)

_generateCode_ function will create the following python files containing the GraphQL schema objects as python classes:

* scalars.py -> GraphQL scalar types as python type aliases
* enums.py -> GraphQL enum types as Enum classes
* gqlTypes.py -> GraphQL object types as classes
* gqlSimpleTypes.py -> GraphQL object types as classes not using other object types
* queries.py -> GraphQL query types as classes and an Enum 'Queries' having query names as name and query classes as value
* mutations.py -> mutation classes and an Enum 'Mutations' having mutation names as name and mutation classes as value
* circularRefs.py -> Only in case of objects containing recursive references this file will contain references to their types


## Usage via command line

### Generation

Example of python classes generation command:

```
pygqlcodegen generate ./GeoDBCities -apiArgs ./generatorArgs.json -v
```

This command will generate python files in _./GeoDBCities/_ using the [information](#json-args-file) given in _./generatorArgs.json_.


### Download of a schema as json file 

Example of schema retrieval command:

```
pygqlcodegen download ./commandsOutput/Github/schema.json -apiArgs ./downloaderArgs.json
```

This command will create the file in _./commandsOutput/Github/schema.json_ containing the schema in json version using the [information](#json-args-file) given in _./downloaderArgs.json_.


A few examples can be seen [here](#https://github.com/dapalex/py-graphql-mapper/blob/main/test/geoDBCitiesApiUnitTest.py#L9) and [here](#https://github.com/dapalex/py-graphql-mapper/blob/main/test/githubApiUnitTest.py#L13)


#### JSON args file

This file is used by the generator command line interface, it contains:

```python
{
    "addDescToGeneratedFiles": "True", # boolean telling if descriptions have to be added to the generated classes (strongly advised to be True)
    "customTypes": { # dictionary containing scalar types not managed in the default mapping
        "myScalarTypeNameAsInt": "int",
        "myScalarTypeNameAsString": "str"
    },
    ##USED FOR QUERYING A GRAPHQL SERVER
    "apiURL": "https://mygraphqlapi.com/v2", # URL of the GraphQL server to query
    "httpHeaders": { # HTTP Headers necessary to query the GraphQL server
        "Authorization": "bearer abcdef12345678",
        "additionalHeader-content-type": "application/json"
    },
    ##USED FOR GENERATE COMMAND USING A SCHEMA FILE
    "schemaFile": "./commandsOutput/RapidApi/schema.json" # location of the json version of schema file
}
```


## Using the generated files

Classes generated in _mutations.py_ can be directly used for calling a GraphQL API.

Supposed a generated mutation

```python

class createProject(GQLMutation):
   """

   input - Parameters for CreateProject

   """
   class createProjectArgs(GQLArgsSet, GQLObject): 
      """
      input - Parameters for AbortQueuedMigrations

      """
      input: CreateProjectInput ##NON NULL

   _args: createProjectArgs ##NON NULL
   type: CreateProjectPayload

```

having as input the following generated class

```python
from pygqlmap.gqlTypes import ID

class CreateProjectInput():
   """

   ownerId - The owner ID to create the project under.

   name - The name of project.

   body - The description of project.

   template - The name of the GitHub-provided template.

   repositoryIds - A list of repository IDs to create as linked repositories for the project

   clientMutationId - A unique identifier for the client performing the mutation.

   """
   ownerId: ID ##NON NULL
   name: str ##NON NULL
   body: str
   template: ProjectTemplate
   repositoryIds: list[ID] ##NON NULL
   clientMutationId: str

```

The mutation class can be instantiated and defined

```python
from .output.github.mutations import Mutations
from .output.github.types import CreateProjectInput

mutation = Mutations.createProject.value()

mutation.input.ownerId = 'MDQ6VXNlcjkxMzk2ODM3'
mutation.input.name = "Test create project from Mutation" + datetime.now().ctime()
mutation.input.repositoryIds = ["R_kgDOH7MI4g"]

mutation._customPayload = '{ project { id } }'

```

_exportGqlSource_ will generate the following:

```
mutation MycreateProjectMutation  { 
    createProject ( input: { ownerId: "MDQ6VXNlcjkxMzk2ODM3", name: "Test create project from MutationMon Nov 21 10:19:09 2022", repositoryIds: ["R_kgDOH7MI4g"] }  )  {  
        project { 
            id 
        } 
    }  
} 
```

Then executed using [pygqlmap](#https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap/README.MD)

```python
from pygqlmap.network import GQLResponse

myMutation = MycreateProjectMutation()
myMutation.name = 'MycreateProjectMutation'

response = request("POST", graphQLServerUrl, json=json={ "query": myMutation.exportGqlSource }, headers=headers)
gqlResponse = GQLResponse(response)
gqlResponse.printMessageOutput()
    
print('resultObject: ' + str(gqlResponse.resultObject))
```
