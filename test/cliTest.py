
# import sys
# import os
# import pathlib


# sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
# sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

import asyncio
from .geoDBCitiesApiUnitTest import (runDownloadCommandgdbcApiBySchemaFileRelPath, runDownloadCommandGeoDBCitiesBySchemaFileRelPath, 
                                     runGenerateCommandGeoDBCitiesByApiRelPath)
from .githubApiUnitTest import (runDownloadCommandGithubBySchemaFileRelPath, runGenerateCommandGithubByApiAbsPath)
from .helpUnitTest import runGeneratorCommandHelp
from .rapidApiUnitTest import (runDownloadCommandRapidApiBySchemaFileRelPath, runGenerateCommandRapidApiByApiAbsPath)


asyncio.run(runGeneratorCommandHelp())
asyncio.run(runDownloadCommandgdbcApiBySchemaFileRelPath())
asyncio.run(runDownloadCommandGeoDBCitiesBySchemaFileRelPath())
asyncio.run(runGenerateCommandGeoDBCitiesByApiRelPath())
asyncio.run(runDownloadCommandGithubBySchemaFileRelPath())
asyncio.run(runGenerateCommandGithubByApiAbsPath())
asyncio.run(runGenerateCommandGeoDBCitiesByApiRelPath())
asyncio.run(runDownloadCommandRapidApiBySchemaFileRelPath())
asyncio.run(runGenerateCommandRapidApiByApiAbsPath())
