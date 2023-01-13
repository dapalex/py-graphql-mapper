import unittest
from .gh_unittest import (run_gh_add_comment_mutation,
                               run_gh_create_issue_mutation, run_gh_create_proj_mutation, run_gh_delete_proj_mutation,
                               run_gh_delete_proj_v2_mutation, run_gh_update_repo_mutation)
from .ra_unittest import (run_ra_create_gateway_instance_mutation, run_ra_admin_audit_logs,
                              run_ra_create_transformations_mutation, run_ra_edit_user_alert_mutation)
from .unittests import (run_gdbc_complex_obj_viewchange, run_gdbc_complex_obj_viewchange_args_vars,
                        run_gdbc_complex_obj_args_vars, run_gdbc_complex_obj_args_literal,
                        run_gdbc_complex_obj_args_literal_2, runNestedObject, run_gdbc_nested_obj_viewchange,
                        run_gdbc_nested_obj_viewchange_args_vars, run_gdbc_nested_obj_args_vars,
                        run_gdbc_nested_obj_args_literal, run_gdbc_obj_composed_args)
from .tstquery.complex_obj_test import run_gdbc_complex_obj
from .tstquery.connobj_args_literal_test import run_gdbc_connobj_args_literal
from .tstquery.connobj_args_vars_test import run_gdbc_connobj_args_vars
from .tstquery.connobj_viewchange_test import run_gdbc_connobj_viewchange
from .tstquery.connobj_test import run_gdbc_connobj
from .tstquery.manual_obj_test import runGeneratedDataAsGQLObject
from .tstquery.simple_obj_test import run_simple_obj
from .tstquery.simple_obj_args_literal_test import run_simple_objargs_literal
from .tstquery.simple_obj_args_vars_test import run_simple_args_vars
from .tstquery.simple_obj_viewchange_test import runSimpleOobj_viewchange
from .tstmutation.manual_mutation_test import run_gh_insert_literal_mutation
from .tstmutation.mutation_test import run_gh_update_literal_mutation
from .args_params_unittest import (run_complex_obj_args_literal, run_complex_obj_args_vars, run_complex_obj_viewchange,
                                   run_complex_obj_viewchange_args_vars, run_gh_add_comment_mutation, run_nested_obj_args_literal,
                                   run_nested_obj_args_vars, run_obj_composed_args)


class TestMapper(unittest.TestCase):

##################### QUERIES EXECUTION - START ##############################

  def testGeneratedDataAsGQLObject(self):
    return runGeneratedDataAsGQLObject()

  def test_simple_obj(self):
    return run_simple_obj()

  def test_simple_objargs_literal(self):
    return run_simple_objargs_literal()

  def test_simple_args_vars(self):
    return run_simple_args_vars()

  def testSimpleOobj_viewchange(self):
    return runSimpleOobj_viewchange()

  def test_gdbc_connobj(self):
    return run_gdbc_connobj()

  def test_gdbc_connobj_viewchange(self):
    return run_gdbc_connobj_viewchange()

  def test_gdbc_connobj_args_vars(self):
    return run_gdbc_connobj_args_vars()

  def test_gdbc_connobj_args_literal(self):
    return run_gdbc_connobj_args_literal()

###################### QUERIES EXECUTION - END ##############################

###################### MUTATIONS EXECUTION - START ##############################


#GITHUB API - START
  def test_gh_update_literal_mutation(self):
    return run_gh_update_literal_mutation()

  def test_gh_insert_literal_mutation(self):
    return run_gh_insert_literal_mutation()

  def testGithubAddCommentMutation(self):
    return run_gh_add_comment_mutation()

  def test_gh_update_repo_mutation(self):
    return run_gh_update_repo_mutation()

  def test_gh_delete_proj_mutation(self):
    return run_gh_delete_proj_mutation()

  def test_gh_delete_proj_v2_mutation(self):
    return run_gh_delete_proj_v2_mutation()

  def test_gh_create_issue_mutation(self):
    return run_gh_create_issue_mutation()

  def test_gh_create_proj_mutation(self):
    return run_gh_create_proj_mutation()
#GITHUB - END

#RapidAPI - START

  def test_ra_admin_audit_logs(self):
    return run_ra_admin_audit_logs()

  def test_ra_create_transformations_mutation(self):
    return run_ra_create_transformations_mutation()

  def test_ra_create_gateway_instance_mutation(self):
    return run_ra_create_gateway_instance_mutation()

  def test_ra_edit_user_alert_mutation(self):
    return run_ra_edit_user_alert_mutation()
#RapidAPI - END

# ###################### MUTATIONS EXECUTION - END ##############################

# # # #FURTHER TESTS
  def test_gdbc_complex_obj(self):
    return run_gdbc_complex_obj()
  def testNestedObject(self):
    return runNestedObject()
  def test_gdbc_nested_obj_args_literal(self):
    return run_gdbc_nested_obj_args_literal()
  def test_gdbc_nested_obj_viewchange(self):
    return run_gdbc_nested_obj_viewchange()
  def test_gdbc_complex_obj_args_literal(self):
    return run_gdbc_complex_obj_args_literal()
  def test_gdbc_complex_obj_args_literal_2(self):
    return run_gdbc_complex_obj_args_literal_2()
  def test_gdbc_obj_composed_args(self):
    return run_gdbc_obj_composed_args()
  def test_gdbc_complex_obj_viewchange(self):
    return run_gdbc_complex_obj_viewchange()
  def test_gdbc_nested_obj_viewchange_args_vars(self):
    return run_gdbc_nested_obj_viewchange_args_vars()
  def test_gdbc_complex_obj_viewchange_args_vars(self):
    return run_gdbc_complex_obj_viewchange_args_vars()
  def test_gdbc_nested_obj_args_vars(self):
    return run_gdbc_nested_obj_args_vars()
  def test_gdbc_complex_obj_args_vars(self):
    return run_gdbc_complex_obj_args_vars()


###################### ARGUMENTS AS FUNCTION PARAMETERS - START ##############################

  def test_complex_obj_viewchange(self):
        return run_complex_obj_viewchange()

  def test_nested_obj_args_vars(self):
    return run_nested_obj_args_vars()

  def test_nested_obj_args_literal(self):
    return run_nested_obj_args_literal()

  def test_complex_obj_args_literal(self):
    return run_complex_obj_args_literal()

  def test_complex_obj_args_vars(self):
    return run_complex_obj_args_vars()

  def test_complex_obj_viewchange_args_vars(self):
    return run_complex_obj_viewchange_args_vars()

  def test_obj_composed_args(self):
    return run_obj_composed_args()

  def test_gh_add_comment_mutation(self):
    return run_gh_add_comment_mutation()


##################### ARGUMENTS AS FUNCTION PARAMETERS - END ##############################
