# py-graphql-mapper - Test

Tests have been made using:

- GeoDB Cities GraphQL API
- Github GraphQL API
- rapidapi GraphQL API


In order to launch the tests locally an API key has to be set for:

 * GeoDBCities API [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/consts.py), available with a free subscription at https://rapidapi.com/wirefreethought/api/geodb-cities-graphql/
* Github API [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/consts.py), available with a free subscription at https://github.com
* RapidAPI API [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/consts.py), available with a free subscription at https://rapidapi.com/ApiPlaygroundTestRapidapi/api/graphql-rapidapi-test/


## Queries

| Scenario | Description | Test case |
|:---------|:-----------|:----------:|
| Querying a simple object type | Create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response <br> _Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests_ | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstquery/simple_obj_test.py)|
| Querying a simple object type using arguments as literal values | Create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response <br> _Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests_ | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstquery/simple_obj_args_literal_test.py) |
| Querying a simple object type using arguments and variables | Create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response <br> _Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests_ | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstquery/simple_obj_args_vars_test.py) |
| Querying a simple object type changing the visibility of fields | Create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response <br> _Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests_ | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstquery/simple_obj_viewchange_test.py) |
| Querying a connection | Create a GraphQL Query to fetch a GraphQL connection type and build the python class instance containing the data from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstquery/connobj_test.py) |
| Querying a connection using arguments as literal values | Create a GraphQL Query to fetch a GraphQL connection type using Args as literal values and build the python class instance containing the data from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstquery/connobj_args_literal_test.py) |
| Querying a connection using arguments and variables | Create a GraphQL Query to fetch a GraphQL connection type using Args and Variables and build the python class instance containing the data from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstquery/connobj_args_vars_test.py) |
| Querying a connection changing the visibility of fields | Create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response <br> _Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests_ | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstquery/connobj_viewchange__test.py) |
| Querying a composed object | Create a GraphQL Query to fetch a GraphQL connection type using Args and Variables and build the python class instance containing the data from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstquery/complex_obj_test.py) |

Further queries can be found [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/unittests.py)

## Mutations

| Scenario | Description | Test case |
|:---------|:-----------:|----------:|
| Executing a mutation with arguments as literal values | create a GraphQL Mutation to modify a GraphQL type and builds the python class instance containing the payload received from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstmutation/mutation_t_est.py) |
| Executing a mutation manually created using only _pygqlmap_ with arguments as literal values | create a GraphQL Mutation to mutate a GraphQL type and builds the python class instance containing the payload received from the response | [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/tstmutation/manual_mutation_test.py) |


Further tests can be found [here](https://github.com/dapalex/py-graphql-mapper/blob/main/tests/unittests.py)