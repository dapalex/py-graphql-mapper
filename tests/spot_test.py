
import abc
from datetime import datetime
import sys
import os
import pathlib
import logging as logger
import requests




sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))

from pygqlmap.gql_operations import GQLQuery

from tests.output.re_nodesc.queries import version
from tests.utils import stringifyresult
from tests.output.github.gql_types import AddCommentInput
# from output.github.queries import rateLimit
from codegen.generator import CodeGenerator
# from datetime import datetime
from codegen.network import fetch_schema_obj
from codegen.query_presets import QUERY_SCHEMA_AND_TYPES
from pygqlmap.enums import ArgType
from pygqlmap.gql_types import ID, NonNull_ID
from pygqlmap.network import GQLResponse
from consts import GDBC_HEADERS, GDBC_URL
# from output.gdbc.gql_simple_types import Currency
# from output.gdbc.queries import currencies
from consts import *
# from output.github.gql_types import AddCommentInput
# from output.gdbc.queries import country
# from output.gdbc.gql_types import DisplayOptions
# from output.rapidapi.gql_simple_types import JYWXC_name_Field

def run_re_version_vars():
    logger.debug('\n\nRunning run_re_version_vars...')
    query = version()
    # query._args.first = 3
    # query._args.after = 'Mg=='
    query.name = 'myVersionQuery'

    query._args_type = ArgType.VARIABLES

    try:
        logger.debug('gqlSource GQL version: ' + query.export_gql_source)

        response = requests.request('POST', url=RE_URL,
                                    json={ "query": query.export_gql_source, "variables": query.export_gqlvariables },
                                    headers=RE_HEADERS)
        gqlResponse = GQLResponse(response)

        gqlResponse.print_msg_out()
        gqlResponse.map_gqldata_to_obj(query.type)
        logger.info('result object: ' + stringifyresult(gqlResponse.result_obj))
    except Exception as ex:
        raise ex

    logger.debug("End of run_re_version_vars")

run_re_version_vars()