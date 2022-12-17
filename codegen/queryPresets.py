queryTypeRef = """
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

queryTypeDetails = """
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
""" + queryTypeRef
                    
queryType = "query { __type(name: \"%s\") { name kind description fields { name } } }"

querySchemaBasic =  """query IntrospectionQuery {
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

querySchemaMutationType = """query {
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
""" + queryTypeRef

querySchemaAndTypes = """query IntrospectionQuery {
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
""" + queryTypeDetails

queryTypeMutation = """query introspectionMutationType {
  __type(name: "Mutation") {
    ...FullType
  }
}
""" + queryTypeDetails
