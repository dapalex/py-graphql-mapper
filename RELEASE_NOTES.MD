py-graphql-mapper Release Update

Release notes version: 1.1.1

Release date: Jul. 2, 2023

Changes

* Query types not recognition not anymore based on the conventional "Query" string definition but checking *__schema -> QueryType -> name* definition

Bug fixes

* Queries having payload as list return only 1 element of the list: the issue has been solved, also the list type will not show anymore the element type fields

Release notes version: 1.1.0

Release date: Feb. 10, 2023

Features

* Assignment of arguments through parameters: other than using _arg object to set the arguments, now it is possible to assign arguments also using kwargs during construction of the parent object.

Bug fixes

* Check for NonNullability types: nonnull types will be recognized when using arguments and variables (setting ! in GraphQL syntax).

Breaking changes:

Implemented Pythonic naming convention.
The following signatures have changed:

| Old | New |
|:---------|:-----------|
| fetchSchemaObject | fetch_schema_obj |
| querySchemaAndTypes | QUERY_SCHEMA_AND_TYPES |
| gqlTypes | gql_types |
| gqlArgBuiltin | arg_builtin |
| gqlOperations | gql_operations |
| exportGqlSource | export_gql_source |
| exportGQLVariables | export_gqlvariables |
| printMessageOutput | print_msg_out |
| mapGQLDataToObj | map_gqldata_to_obj |
| setShow | set_show |
| resultObject | result_obj |
| _argsType | _args_type |
| LiteralValues | LITERAL_VALUES |
| Variables | VARIABLES |


Release notes version: 1.0.0

Release note date: Jan. 8, 2023

Overview

A python library to call a GraphQL API without using hardcoded strings.
Stable version allowing mapping of queries and mutations

