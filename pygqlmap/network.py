import json
from urllib import request
from urllib.error import HTTPError
import logging as logger
from .src.builder import ResultBuilder
from .src.enums import BuildingType

def send_http_request(api_url, payload, httpHeaders):
    try:
        body = json.dumps(payload, indent=2).encode('ascii')
        req = request.Request(api_url, data=body)
        for http_header_key, http_header_val in httpHeaders.items():
            req.add_header(http_header_key, http_header_val)

        with request.urlopen(req) as response:
            response.text = response.read().decode('utf-8')
            response.ok = response.status == 200
            return response
    except HTTPError as ex:
        raise Exception(str(ex.status) + ' - ' + ex.reason)
    except Exception as ex:
        raise Exception(str(ex.args[0]))

class GQLResponse():
    http_response = None
    json_response = None
    errors = None
    data = None
    result_obj = None
    log_progress: bool= None

    def __init__(self, response: str, log_progress: bool = False):
        self.http_response = response
        self.json_response = json.loads(response.text)
        self.log_progress = log_progress

        if isinstance(self.json_response, dict):
            if "errors" in self.json_response.keys():
                self.errors = self.json_response["errors"]
            if "data" in self.json_response.keys():
                self.data = self.json_response["data"]

    def map_gqldata_to_obj(self, mapped_py_obj,  build_type: BuildingType = BuildingType.STANDARD):
        """Maps the json response to a python object and saves it in result_obj field

        Args:
            mappedPyObject (_type_, optional): python object mapped from a GraphQL type
                                               A reference can be found in the GQLOperation object created as <queryObject>.type
            build_sctype (BuildingType, optional): Options not yet implemented. Defaults to BuildingType.STANDARD.
        """
        if hasattr(self, 'data') and self.data:
            if not hasattr(mapped_py_obj, '__dataclass_fields__'):#it is a primitive
                self.result_obj = self.data.popitem()[1]
            else:
                myBuilder = ResultBuilder(build_type, self.log_progress)
                self.result_obj = myBuilder.build(self.data, mapped_py_obj)
        else:
            self.result_obj = None

    def print_msg_out(self):
        """!This function works with built-in python module urllib3 and requests library

        Raises:
            Exception: HTTP status code != 200
            Exception: Presence of errors in the json response
            Exception: Missing errors and data in the json response
        """
        if hasattr(self.http_response, 'status'):
            status = self.http_response.status
        else:
            status = self.http_response.status_code
        logger.info('Network result: ' + 'OK' if self.http_response.ok else 'KO')
        logger.info('HTTP code: ' + str(status))

        if status != 200:
            error = 'HTTP Error: ' + self.http_response.text
            logger.error(error)
            raise Exception(error)
        else:
            if hasData :=(hasattr(self, 'data') and self.data):
                logger.info('Data returned: ')
                logger.info(json.dumps(self.data, indent=2))

            if hasErrors :=(hasattr(self, 'errors') and self.errors):
                err_out = ''
                for error in self.errors:
                    err_out += str(error) + '\n'
                err_out += '\n'
                logger.error('Response Errors: ' + err_out)

            if not hasData and not hasErrors:
                raise Exception('Inconsistent response: ' + self.http_response.text)
