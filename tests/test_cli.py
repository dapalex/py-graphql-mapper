
# import sys
# import os
# import pathlib


# sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
# sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

from .geoDBCitiesApiUnitTest import (runDownloadCommandgdbcApiBySchemaFileRelPath, runDownloadCommandGeoDBCitiesBySchemaFileRelPath, 
                                     runGenerateCommandGeoDBCitiesByApiRelPath)
from .githubApiUnitTest import (runDownloadCommandGithubBySchemaFileRelPath, runGenerateCommandGithubByApiAbsPath)
from .helpUnitTest import runGeneratorCommandHelp
from .rapidApiUnitTest import (runDownloadCommandRapidApiBySchemaFileRelPath, runGenerateCommandRapidApiByApiAbsPath)


runGeneratorCommandHelp()
runDownloadCommandgdbcApiBySchemaFileRelPath()
runDownloadCommandGeoDBCitiesBySchemaFileRelPath()
runGenerateCommandGeoDBCitiesByApiRelPath()
runDownloadCommandGithubBySchemaFileRelPath()
runGenerateCommandGithubByApiAbsPath()
runGenerateCommandGeoDBCitiesByApiRelPath()
runDownloadCommandRapidApiBySchemaFileRelPath()
runGenerateCommandRapidApiByApiAbsPath()
