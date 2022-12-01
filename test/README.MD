# py-graphql-mapper - Test

Tests have been made using:

- GeoDB Cities GraphQL API
- Github GraphQL API
- RapidApi GraphQL API

*requests* library has been used for the HTTP requests to the GraphQL server.

In order to launch the tests API keys for the following GraphQL servers are required, these can be obtained signing up to [RapidAPI](#https://rapidapi.com/) then subscribing to the relating APIS:


* GeoDBCities API: available with a free subscription at https://rapidapi.com/wirefreethought/api/geodb-cities-graphql/

* Github API: available with a free subscription at https://rapidapi.com/rapidapi/api/github-graphql2/

* RapidAPI API: available with a free subscription at https://rapidapi.com/ApiPlaygroundTestRapidapi/api/graphql-rapidapi-test/

The API keys can be then inserted [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/consts.py)


## Use cases/tests

Following use cases to show how the library works.

### Queries

| Scenario | Description | Test case |
|:---------|:-----------|:----------:|
| Querying a simple object type | Create a GraphQL query to fetch a simple GraphQL type and build the python class instance containing the data from the response  | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectTest.py)|
| Querying a simple object type using arguments as literal values | Create a GraphQL Query to fetch a simple GraphQL type with arguments as literal values and build the python class instance containing the data from the response  | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectArgs_LiteralValuesTest.py)|
| Querying a simple object type using arguments and variables | Create a GraphQL query to fetch a simple GraphQL type with arguments and variables and build the python class instance containing the data from the response  | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectArgs_VariablesTest.py)|
| Querying a simple object type changing the visibility of fields | Create a GraphQL query to fetch a simple GraphQL type with some fields hidden and build the python class instance containing the data from the response  | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectChangeVisibilityTest.py)|
| Querying a connection | Create a GraphQL Query to fetch a GraphQL connection type and build the python class instance containing the data from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstquery/connectionObjectTest.py)|
| Querying a connection using arguments as literal values | Create a GraphQL query to fetch a GraphQL connection type with arguments as literal values and build the python class instance containing the data from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstquery/connectionobjectArgs_LiteralValuesTest.py)|
| Querying a connection using arguments and variables | Create a GraphQL Query to fetch a GraphQL connection type with arguments and variables and build the python class instance containing the data from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstquery/connectionObjectArgs_VariablesTest.py)|
| Querying a connection changing the visibility of fields | Create a GraphQL query to fetch a simple GraphQL type with some fields hidden and build the python class instance containing the data from the response  | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstquery/connectionObjectChangeVisibilityTest.py)|
| Querying a composed object | Create a GraphQL Query to fetch a GraphQL connection type with arguments and variables and with some fields hidden and build the python class instance containing the data from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstquery/complexObjectTest.py)|


### Mutations

| Scenario | Description | Test case |
|:---------|:-----------:|----------:|
| Executing a mutation with arguments as literal values | create a GraphQL mutation to alter a simple GraphQL type and builds the python class instance containing the data from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstmutation/mutationInsertTest.py) <br> [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/tstmutation/mutationUpdateTest.py)|



Further tests can be found [here](https://github.com/dapalex/py-graphql-mapper/blob/main/test/pgqlmCoreTest/unitTest.py)

