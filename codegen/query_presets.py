QUERY_TYPE_REF = """
                    fragment TypeRef on __Type {
                    kind
                    name
                    ofType {
                        kind
                        name
                        ofType {
                        kind
                        name
                        ofType {
                            kind
                            name
                            ofType {
                            kind
                            name
                            ofType {
                                kind
                                name
                                ofType {
                                kind
                                name
                                ofType {
                                    kind
                                    name
                                }
                                }
                            }
                            }
                        }
                        }
                    }
                    }"""

QUERY_TYPE_DETAILS = """
                    fragment FullType on __Type {
                    kind
                    name
                    description
                    fields(includeDeprecated: true) {
                        name
                        description
                        args { ...InputValue }
                        type { ...TypeRef }
                        isDeprecated
                        deprecationReason
                    }
                    inputFields { ...InputValue }
                    interfaces { ...TypeRef }
                    enumValues(includeDeprecated: true) { name description isDeprecated deprecationReason }
                    possibleTypes { ...TypeRef }
                    }

                    fragment InputValue on __InputValue {
                    name
                    description
                    type { ...TypeRef }
                    defaultValue
                    }
""" + QUERY_TYPE_REF

QUERY_TYPE = "query { __type(name: \"%s\") { name kind description fields { name } } }"

QUERY_SCHEMA_BASIC =  """query IntrospectionQuery {
                    __schema {
                        queryType { name }
                        mutationType { name }
                        subscriptionType { name }
                        types { kind name description }
                        directives {
                        name
                        description
                        locations
                        args { name description defaultValue }
                        }
                    }
                }"""

QUERY_SCHEMA_MUTATION_TYPE = """query {
  __schema {
    mutationType {
      name
      fields {
        name
        args {
          name
          defaultValue
          type {
            ...TypeRef
          }
        }
      }
    }
  }
}
""" + QUERY_TYPE_REF

QUERY_SCHEMA_AND_TYPES = """query IntrospectionQuery {
                    __schema {
                        queryType { name }
                        mutationType { name }
                        subscriptionType { name }
                        types { ...FullType }
                        directives {
                        name
                        description
                        locations
                        args { ...InputValue }
                        }
                    }
                    }
""" + QUERY_TYPE_DETAILS

QUERY_TYPE_MUTATION = """query introspectionMutationType {
  __type(name: "Mutation") {
    ...FullType
  }
}
""" + QUERY_TYPE_DETAILS
