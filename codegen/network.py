from pygqlmap.network import GQLResponse, httpRequest
from .src.spBuilder import SchemaBuilder, SchemaTypeBuilder
from .src.spSchema import GQLSchema, SCType

def fetchSchemaResponse(url, httpHeaders, query):
    try:
        payload = { "query": query }
        response = httpRequest(url, payload, httpHeaders)
    except Exception as ex:
        raise ex

    return GQLSchemaResponse(response)

def fetchSchemaObject(url, headers, query):
    gqlResponse = fetchSchemaResponse(url, headers, query)
    gqlResponse.mapGQLDataToObj()
    gqlResponse.printMessageOutput()
    return gqlResponse.resultObject

class GQLSchemaResponse(GQLResponse):

    includeDeprecated: bool

    def mapGQLDataToObj(self, mappedPyObject = None,  buildType = None):
        """_summary_

        Args:
            includeDeprecated (bool, optional): Decides if deprecated values are to be included.
                                                Defaults to True.

        Returns:
            _type_: _description_
        """

        if self.data:
            for rootObject in self.data.keys():
                if rootObject == '__schema': #check self.data type
                    myBuilder = SchemaBuilder()
                    self.resultObject = myBuilder.build(self.data, GQLSchema())
                elif rootObject == '__type': #check self.data  type
                    myBuilder = SchemaTypeBuilder()
                    self.resultObject = myBuilder.build(self.data, SCType())
                else:
                    self.resultObject = None