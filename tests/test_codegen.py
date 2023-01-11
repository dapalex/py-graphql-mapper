import sys
import os
import pathlib
import unittest


sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

from .gdbc_unittest import (run_fetch_gdbc_schema, run_fetch_gdbc_schema_no_desc)
from .gh_unittest import (run_fetch_gh_schema, run_fetch_gh_schema_no_desc)
from .ra_unittest import (run_fetch_ra_schema, run_fetch_ra_schema_no_desc)

class TestCodegen(unittest.TestCase):

    def testgdbcSchema(self):
      return run_fetch_gdbc_schema()

    def testgdbcschema_no_desc(self):
      return run_fetch_gdbc_schema_no_desc()

    def testGithubMutationTypesFromschema_no_desc(self):
      return run_fetch_gh_schema_no_desc()

    def testGithubMutationTypes(self):
      return run_fetch_gh_schema()

    def testrapidapiTestSchemaAndTypes_nodesc(self):
      return run_fetch_ra_schema_no_desc()

    def testrapidapiTestSchemaAndTypes(self):
      return run_fetch_ra_schema()
