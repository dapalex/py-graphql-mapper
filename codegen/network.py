from pygqlmap.network import GQLResponse, send_http_request
from .src.sp_builder import SchemaBuilder, SchemaTypeBuilder
from .src.sp_schema import GQLSchema, SCType

def fetch_schema_response(url, httpHeaders, query):
    try:
        payload = { "query": query }
        response = send_http_request(url, payload, httpHeaders)
    except Exception as ex:
        raise ex

    return GQLSchemaResponse(response)

def fetch_schema_obj(url, headers, query):
    gql_response = fetch_schema_response(url, headers, query)
    gql_response.map_gqldata_to_obj()
    gql_response.print_msg_out()
    return gql_response.result_obj

class GQLSchemaResponse(GQLResponse):

    def map_gqldata_to_obj(self, mapped_py_obj = None,  build_sctype = None):
        """_summary_

        Args:
            includeDeprecated (bool, optional): Decides if deprecated values are to be included.
                                                Defaults to True.

        Returns:
            _type_: _description_
        """

        if self.data:
            for root_obj in self.data.keys():
                if root_obj == '__schema': #check self.data type
                    builder = SchemaBuilder()
                    self.result_obj = builder.build(self.data, GQLSchema())
                elif root_obj == '__type': #check self.data  type
                    builder = SchemaTypeBuilder()
                    self.result_obj = builder.build(self.data, SCType())
                else:
                    self.result_obj = None