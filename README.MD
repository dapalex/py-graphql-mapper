# py-graphql-mapper [![Python package](https://github.com/dapalex/py-graphql-mapper/actions/workflows/python-package.yml/badge.svg)](https://github.com/dapalex/py-graphql-mapper/actions/workflows/python-package.yml)   [![Pyhon-GraphQL Mapping Test](https://github.com/dapalex/py-graphql-mapper/actions/workflows/test-map.yml/badge.svg)](https://github.com/dapalex/py-graphql-mapper/actions/workflows/test-map.yml)   [![Code Generation Test](https://github.com/dapalex/py-graphql-mapper/actions/workflows/test-codegen.yml/badge.svg)](https://github.com/dapalex/py-graphql-mapper/actions/workflows/test-codegen.yml)

A python library to interact with GraphQL APIs with no need of hardcoded strings.

## Introduction

This library act as a mapper between python and GraphQL languages for a GraphQL client allowing a code-first approach when calling a GraphQL API server.
It translates GraphQL entities into python objects and viceversa in order to avoid working with massive "copy&paste"s.

The package does not use any third-party libraries, it relies only on python 3 standard libraries. 


## Table of Contents

1. [Usage in a nutshell](#usage-in-a-nutshell)
    1. [Installation](#installation)
    2. [Generate python code from schema](#generate-python-code-from-schema)
    3. [Execution of a query](#execution-of-a-query)
    4. [Retrieval of a response](#retrieval-of-a-response)


## Usage in a nutshell

### Installation

The following command will install the library:

```
python setup.py install
```


### Generate python code from schema

To generate the code execute the following command:

```
pygqlcodegen generate ./pathToOutputFolder -apiArgs ./pathToArgsFile/generatorArgs.json
```

This command requires a json file containing the parameters necessary to get the GraphQL schema to parse

![image](https://github.com/dapalex/py-graphql-mapper/blob/main/docs/cli_args_nutshell.png)


In the output folder there will be the following python files:

* enums.py
* scalars.py
* gqlSimpleTypes.py
* gqlTypes.py
* circularRefs.py
* queries.py
* mutations.py

Some generated code obtained from [Github GraphQL API](https://github.com/dapalex/py-graphql-mapper/blob/main/test/output/github), [Rapid GraphQL API](https://github.com/dapalex/py-graphql-mapper/blob/main/test/output/RapidApi) and [GeoDBCities API](https://github.com/dapalex/py-graphql-mapper/blob/main/test/output/GeoDBCities)

More command options available [here](https://github.com/dapalex/py-graphql-mapper/blob/main/codegen/README.MD)


### Execution of a query

Choose the query class you want to use from the generated file queries.py (or a mutation from mutations.py):

```python
from .output.GeoDBCities.queries import currencies

myCurrenciesQuery = currencies()
```
populate the necessary information to execute the query:

```python
myCurrenciesQuery._args.last = 7
myCurrenciesQuery._args.before = 'MTE='
```
Call _exportGqlSource_ property to pass the payload to the HTTP request:

```python
import requests

response = requests.request('POST', url='https://geodb-cities-graphql.p.rapidapi.com/', 
                            json= { "query": myCurrenciesQuery.exportGqlSource }, 
                            headers={
                                    "content-type": "application/json",
                                        "X-RapidAPI-Key": '123402mmri02fni230iif32jr420', 
                                        "X-RapidAPI-Host": "geodb-cities-graphql.p.rapidapi.com"
                                    }
                            )
```

More details [here](https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap/README.MD#executing-an-operation)


### Retrieval of a response

Obtained the response from the GraphQL API the following code will map the json payload received into the python object

```python
from pgqlmCore.network import GQLResponse

gqlResponse = GQLResponse(response)

gqlResponse.mapGQLDataToObj(myCurrenciesQuery.type)

print('resultObject: ' + str(gqlResponse.resultObject))
```

The mapped response from the GraphQL server will be available within _gqlResponse_ object: _gqlResponse.resultObject_

More details [here](https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap/README.MD#parsing-of-a-response)



A suite of use cases [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/README.MD#L110)
