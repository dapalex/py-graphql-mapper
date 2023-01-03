# py-graphql-mapper - Test

THIS DOCUMENT IS UNDER REVIEW

Tests have been made using:

- GeoDB Cities GraphQL API
- Github GraphQL API
- RapidApi GraphQL API

*requests* library has been used for the HTTP requests to the GraphQL server.

In order to launch the tests an API key has to be set 
 * GeoDBCities API [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/GdbcApi/consts.py), available with a free subscription at https://rapidapi.com/wirefreethought/api/geodb-cities-graphql/
* Github API [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/GithubApi/consts.py), available with a free subscription at https://rapidapi.com/wirefreethought/api/geodb-cities-graphql/
* RapidAPI API [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/RapidApi/consts.py), available with a free subscription at https://rapidapi.com/wirefreethought/api/geodb-cities-graphql/


## Queries

| Scenario | Description | Test case |
|:---------|:-----------|:----------:|
| Querying a simple object type | Create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response <br> _Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests_ | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectTest.py)|

| Querying a simple object type using arguments as literal values | Create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response <br> _Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests_ | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectArgs_LiteralValuesTest.py)|

| Querying a simple object type using arguments and variables | Create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response <br> _Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests_ | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectArgs_VariablesTest.py)|

| Querying a simple object type changing the visibility of fields | Create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response <br> _Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests_ | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/simpleObjectChangeVisibilityTest.py)|

| Querying a connection | Create a GraphQL Query to fetch a GraphQL connection type and build the python class instance containing the data from the response | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/connectionObjectTest.py)|

| Querying a connection using arguments as literal values | Create a GraphQL Query to fetch a GraphQL connection type using Args as literal values and build the python class instance containing the data from the response | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/connectionobjectArgs_LiteralValuesTest.py)|

| Querying a connection using arguments and variables | Create a GraphQL Query to fetch a GraphQL connection type using Args and Variables and build the python class instance containing the data from the response | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/connectionObjectArgs_VariablesTest.py)|

| Querying a connection changing the visibility of fields | Create a GraphQL Query to fetch a simple GraphQL type and build the python class instance containing the data from the response <br> _Note: This is only for descriptive purposes, the GraphQL server involved does not expose such a query, for real-world cases see other tests_ | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/connectionObjectChangeVisibilityTest.py)|

| Querying a composed object | Create a GraphQL Query to fetch a GraphQL connection type using Args and Variables and build the python class instance containing the data from the response | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/complexObjectTest.py)|


Further queries can be found [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstquery/unitTest.py)|

## Mutations

| Scenario | Description | Test case |
|:---------|:-----------:|----------:|
| Executing a mutation with arguments as literal values | create a GraphQL Query to fetch a simple GraphQL type and builds the python class instance containing the data from the response | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstmutation/mutationInsertTest.py)|
| Executing a mutation with arguments as literal values | create a GraphQL Query to fetch a simple GraphQL type and builds the python class instance containing the data from the response | [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/tstmutation/mutationUpdateTest.py)|


Further tests can be found [here](https://github.com/dapalex/PyGraphQLHelper/blob/main/test/pgqlmCoreTest/unitTest.py)|


~~~~~~~~~~REMOVE API KEYS~~~~~~~~~~~~~~~
