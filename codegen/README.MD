# py-graphql-mapper - Generator

## Introduction

This module automatically generates python classes corresponding to schema GraphQL types, moreover it can save a GraphQL schema in json format.
The generator can be launched through [command line](#usage-via-command-line) or [programmatically](#usage-programmatically).


## Table of Contents

1. [Functionalities](#functionalities)
    1. [Usage programmatically](#usage-programmatically)
    2. [Usage via command line](#usage-via-command-line)
        1. [JSON args file](#json-args-file)
2. [Using the generated files](#using-the-generated-files)


## Functionalities

Two functionalities are available:

1) Generating python classes from a schema
2) Downloading a schema from a GraphQL server API


## Usage programmatically

The class in charge of the generation is _CodeGenerator_, which takes a json schema as input and produces python files containing the mapped GraphQL schema types.

If a json version of the schema is not yet available first step is obtaining it, this can be done passing the API Url and HTTP headers to _fetch_schema_obj_ which will query the GraphQL API server:

```python
from codegen.network import fetch_schema_obj
from codegen.queryPresets import QUERY_SCHEMA_AND_TYPES

schemaObject = fetch_schema_obj(<graphQLUrl>, <HTTPHeaders dictionary>, QUERY_SCHEMA_AND_TYPES)
```

If a json schema is already available _build_schema_ can be used:

```python
from codegen.generator import build_schema

schema_obj = build_schema(schema_json_str)
```

Obtained the schema object the following function _CodeGenerator.generate_code_ has to be called:

```python
from codegen.generator import CodeGenerator
from codegen.queryPresets import QUERY_SCHEMA_AND_TYPES

CodeGenerator.generate_code(schema_obj, folder='test\\output\\github\\', log_progress=False, add_desc=True)
```

Required parameters:

* schema_obj: the schema as python object
* folder: the destination folder where the created python files will be saved

Optional parameters:

* log_progress: makes the generation verbose (default false)
* add_desc: boolean telling if descriptions have to be added to the generated classes (default true)

_generate_code_ function will create the following python files containing the GraphQL schema objects as python classes:

* scalars.py -> GraphQL scalar types as python type aliases
* enums.py -> GraphQL enum types as Enum classes
* gql_types.py -> GraphQL object types as classes
* gql_simple_types.py -> GraphQL object types as classes not using other object types
* queries.py -> GraphQL query types as classes and an Enum 'Queries' having query names as name and query classes as value
* mutations.py -> mutation classes and an Enum 'Mutations' having mutation names as name and mutation classes as value
* type_refs.py -> Only in case of objects containing recursive references this file will contain references to their types


## Usage via command line

### Generation

Classes can be generated alternatively using the CLI command:

```
pgmcodegen generate ./gdbc -apiArgs ./generatorArgs.json -v
```

This command will generate python files in _./gdbc/_ using the [information](#json-args-file) given in _./generatorArgs.json_.


### Download of a schema as json file

Example of schema retrieval command:

```
pgmcodegen download ./cmd_output/Github/schema.json -apiArgs ./downloaderArgs.json
```

This command will create the file in _./cmd_output/Github/schema.json_ containing the schema in json version using the [information](#json-args-file) given in _./downloaderArgs.json_.


A few examples can be seen [here](#https://github.com/dapalex/py-graphql-mapper/blob/main/tests/gdbc_unittest.py#L9) and [here](#https://github.com/dapalex/py-graphql-mapper/blob/main/tests/gh_unittest.py#L13)


#### JSON args file

This file is used by the generator command line interface, it contains:

```python
{
    "addDescToGeneratedFiles": "True", # boolean telling if descriptions have to be added to the generated classes (strongly advised to be True)
    ##USED FOR QUERYING A GRAPHQL SERVER
    "apiURL": "https://mygraphqlapi.com/v2", # URL of the GraphQL server to query
    "httpHeaders": { # HTTP Headers necessary to query the GraphQL server
        "Authorization": "bearer abcdef12345678",
        "additionalHeader-content-type": "application/json"
    },
    ##USED FOR GENERATE COMMAND USING A SCHEMA FILE
    "schemaFile": "./cmd_output/rapidapi/schema.json" # location of the json version of schema file
}
```

_apiURL_, _httpHeaders_ and  _schemaFile_ are mutually exclusive.

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
from pygqlmap.gql_types import ID

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
```

then _export_gql_source_ will be able to create the following GraphQL syntax:

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

my_mutation = MycreateProjectMutation()
my_mutation.name = 'MycreateProjectMutation'

response = request("POST", graphQLServerUrl, json=json={ "query": my_mutation.export_gql_source }, headers=headers)
gqlResponse = GQLResponse(response)

print('Result object: ' + stringifyresult(gqlResponse.result_obj))
```

It is possible to create python classes manually (for a customized version for instance) as well only using pygqlmap module.