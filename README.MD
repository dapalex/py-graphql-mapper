[![Python package](https://github.com/dapalex/py-graphql-mapper/actions/workflows/python-package.yml/badge.svg)](https://github.com/dapalex/py-graphql-mapper/actions/workflows/python-package.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/280533e425784f7da9ecb0f6e529886b)](https://www.codacy.com/gh/dapalex/py-graphql-mapper/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dapalex/py-graphql-mapper&amp;utm_campaign=Badge_Grade)
--------------------------------------------------------------------------------
# py-graphql-mapper
[![Code Generation Test](https://github.com/dapalex/py-graphql-mapper/actions/workflows/test-codegen.yml/badge.svg)](https://github.com/dapalex/py-graphql-mapper/actions/workflows/test-codegen.yml)
[![Pyhon-GraphQL Mapping Test](https://github.com/dapalex/py-graphql-mapper/actions/workflows/test-map.yml/badge.svg)](https://github.com/dapalex/py-graphql-mapper/actions/workflows/test-map.yml)

A python library to interact with GraphQL APIs with no need of hardcoded strings.

## Introduction

This library acts as a mapper between python and GraphQL languages for GraphQL clients, allowing a code-first approach when calling a GraphQL API server.
It translates GraphQL entities into python objects and viceversa in order to avoid working with massive "copy&paste"s.

This document contains a quick overview of the functionalities, for more details and options you can read here:

* Code Generation: https://github.com/dapalex/py-graphql-mapper/blob/main/codegen/README.MD
* Core Mapper: https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap/README.MD


The package does not use any third-party libraries, it relies only on python 3 (3.10+) standard libraries.


## Usage in a nutshell

### Installation

Available in PyPI, the following command will install the library:

```
pip install py-graphql-mapper
```


### Generate python code from schema

To generate the code execute the following command:

```
pygqlcodegen generate ./pathToOutputFolder -apiArgs ./pathToArgsFile/generatorArgs.json
```

This command requires a json file containing the parameters needed to get the GraphQL schema

![image](https://github.com/dapalex/py-graphql-mapper/blob/main/docs/cli_args_nutshell.png)


In the output folder there will be the following python files:

* enums.py
* scalars.py
* gqlSimpleTypes.py
* gqlTypes.py
* circularRefs.py
* queries.py
* mutations.py

The following links show code generated using the library [Github GraphQL API](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/output/github), [Rapid GraphQL API](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/output/RapidApi) and [GeoDBCities API](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/output/GeoDBCities)

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

(example using _requests_ library)
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

Obtained the response from the GraphQL API the following code will map the received json payload into the python object

```python
from pygqlmap.network import GQLResponse

gqlResponse = GQLResponse(response)

gqlResponse.mapGQLDataToObj(myCurrenciesQuery.type)

print('resultObject: ' + str(gqlResponse.resultObject))
```

The mapped response from the GraphQL server will be available within _gqlResponse_ object: _gqlResponse.resultObject_

More details [here](https://github.com/dapalex/py-graphql-mapper/blob/main/pygqlmap/README.MD#parsing-of-a-response)



A suite of use cases [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/README.MD)
