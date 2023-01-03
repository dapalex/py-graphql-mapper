import sys
import os
import pathlib


sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

import asyncio
from .geoDBCitiesApiUnitTest import (fetchGeoDBCitiesSchema, fetchGeoDBCitiesSchemaNoDesc)
from .githubApiUnitTest import (fetchGithubMutationTypes, fetchGithubMutationTypesFromSchemaNoDesc)
from .rapidApiUnitTest import (fetchRapidApiTestSchemaAndTypes, fetchRapidApiTestSchemaAndTypesNoDesc)


asyncio.run(fetchGeoDBCitiesSchema())
asyncio.run(fetchGeoDBCitiesSchemaNoDesc())
asyncio.run(fetchGithubMutationTypesFromSchemaNoDesc())
asyncio.run(fetchGithubMutationTypes())
asyncio.run(fetchRapidApiTestSchemaAndTypesNoDesc())
asyncio.run(fetchRapidApiTestSchemaAndTypes())
