from tests.tstquery.manual_query_fragment_test import run_manual_query_fragment
from .gh_unittest import (run_add_comment_mutation_literal,
                               run_gh_create_issue_mutation_literal, run_gh_create_issue_mutation_vars,
                               run_gh_create_proj_mutation_literal, run_gh_create_proj_mutation_vars,
                               run_gh_delete_proj_mutation_literal, run_gh_delete_proj_mutation_vars,
                               run_gh_delete_projectV2_mutation_literal, run_gh_delete_projectV2_mutation_vars,
                               run_gh_update_repo_mutation_literal, run_gh_update_repo_mutation_vars, run_gh_licenses_query_with_list)
from .ra_unittest import (run_ra_create_gateway_instance_mutation_literal, run_ra_create_gateway_instance_mutation_vars,
                          run_ra_admin_audit_logs_query_literal,run_ra_admin_audit_logs_query_vars, run_ra_eventTypes_query_with_list,
                          run_ra_create_transformations_mutation_literal, run_ra_create_transformations_mutation_vars,
                          run_ra_edit_user_alert_mutation_literal, run_ra_edit_user_alert_mutation_vars, run_ra_extensions_query_with_list)
from .unittests import (run_gdbc_complex_obj_viewchange_vars, run_gdbc_complex_obj_viewchange_args_vars,
                        run_gdbc_complex_obj_args_vars, run_gdbc_complex_obj_args_literal,
                        run_gdbc_complex_obj_args_literal_2, run_gdbc_nested_object, run_gdbc_nested_obj_viewchange,
                        run_gdbc_nested_obj_viewchange_args_vars, run_gdbc_nested_obj_args_vars,
                        run_gdbc_nested_obj_args_literal, run_gdbc_obj_composed_args, run_gdbc_nested_obj_with_list)
from .re_unittest import (run_re_version_literal, run_re_version_vars, run_re_allcoops)
from .tstquery.complex_obj_test import run_gdbc_complex_obj
from .tstquery.connobj_args_literal_test import run_gdbc_connobj_args_literal
from .tstquery.connobj_args_vars_test import run_gdbc_connobj_args_vars
from .tstquery.connobj_viewchange_test import run_gdbc_connobj_viewchange
from .tstquery.connobj_test import run_gdbc_connobj
from .tstquery.manual_obj_test import run_generated_data
from .tstquery.simple_obj_test import run_simple_obj
from .tstquery.simple_obj_args_literal_test import run_simple_obj_args_literal
from .tstquery.simple_obj_args_vars_test import run_simple_args_vars
from .tstquery.simple_obj_viewchange_test import run_simple_obj_viewchange
from .tstmutation.manual_mutation_test import run_gh_insert_mutation_literal
from .tstmutation.mutation_test import run_gh_update_mutation_literal
from .args_params_unittest import (run_complex_obj_args_literal, run_complex_obj_args_vars, run_complex_obj_viewchange_args_literal,
                                   run_complex_obj_viewchange_args_vars, run_nested_obj_args_literal,
                                   run_nested_obj_args_vars, run_obj_composed_args_literal, run_obj_composed_args_vars, run_add_comment_mutation_args_literal,
                                   run_add_comment_mutation_args_vars)
from .ra_args_params_unittest import (run_ra_admin_audit_logs_query_args_literal, run_ra_admin_audit_logs_query_args_vars,
                                      run_ra_create_gateway_instance_mutation_args_literal, run_ra_create_gateway_instance_mutation_args_vars,
                                      run_ra_create_transformations_mutation_args_literal, run_ra_create_transformations_mutation_args_vars,
                                      run_ra_edit_user_alert_mutation_args_literal, run_ra_edit_user_alert_mutation_args_vars)

# class TestMapper(unittest.TestCase):

##################### QUERIES EXECUTION - START ##############################

def test_re_version_literal():
  return run_re_version_literal()

def test_re_version_vars():
  return run_re_version_vars()

def test_re_allcoops():
  return run_re_allcoops()

def test_manual_query_fragment():
  return run_manual_query_fragment()

#GeoDBCitiesAPI SAMPLES - START
def testGeneratedDataAsGQLObject():
  return run_generated_data()

def test_simple_obj():
  return run_simple_obj()

def test_simple_objargs_literal():
  return run_simple_obj_args_literal()

def test_simple_args_vars():
  return run_simple_args_vars()

def test_simple_obj_viewchange():
  return run_simple_obj_viewchange()

def test_gdbc_connobj():
  return run_gdbc_connobj()

def test_gdbc_connobj_viewchange():
  return run_gdbc_connobj_viewchange()

def test_gdbc_connobj_args_vars():
  return run_gdbc_connobj_args_vars()

def test_gdbc_connobj_args_literal():
  return run_gdbc_connobj_args_literal()
#GeoDBCitiesAPI SAMPLES - END

#GeoDBCitiesAPI - START
def test_gdbc_complex_obj():
  return run_gdbc_complex_obj()

def test_gdbc_nested_object():
  return run_gdbc_nested_object()

def test_gdbc_nested_obj_args_literal():
  return run_gdbc_nested_obj_args_literal()

def test_gdbc_nested_obj_viewchange():
  return run_gdbc_nested_obj_viewchange()

def test_gdbc_complex_obj_args_literal():
  return run_gdbc_complex_obj_args_literal()

def test_gdbc_complex_obj_args_literal_2():
  return run_gdbc_complex_obj_args_literal_2()

def test_gdbc_obj_composed_args():
  return run_gdbc_obj_composed_args()

def test_gdbc_complex_obj_viewchange():
  return run_gdbc_complex_obj_viewchange_vars()

def test_gdbc_nested_obj_viewchange_args_vars():
  return run_gdbc_nested_obj_viewchange_args_vars()

def test_gdbc_complex_obj_viewchange_args_vars():
  return run_gdbc_complex_obj_viewchange_args_vars()

def test_gdbc_nested_obj_args_vars():
  return run_gdbc_nested_obj_args_vars()

def test_gdbc_complex_obj_args_vars():
  return run_gdbc_complex_obj_args_vars()
#GeoDBCitiesAPI - END

#RapidAPI - START
def test_ra_admin_audit_logs_query_literal():
  return run_ra_admin_audit_logs_query_literal()

def test_ra_admin_audit_logs_query_vars():
  return run_ra_admin_audit_logs_query_vars()
#RapidAPI - END

###################### QUERIES EXECUTION - END ##############################

###################### MUTATIONS EXECUTION - START ##############################


#GITHUB API - START

def test_gh_licenses_query_with_list():
  return run_gh_licenses_query_with_list();

def test_gh_update_mutation_literal():
  return run_gh_update_mutation_literal()

def test_gh_insert_mutation_literal():
  return run_gh_insert_mutation_literal()

def test_gh_add_comment_mutation_literal():
  return run_add_comment_mutation_literal()

def test_gh_update_repo_mutation_literal():
  return run_gh_update_repo_mutation_literal()

def test_gh_update_repo_mutation_vars():
  return run_gh_update_repo_mutation_vars()

def test_gh_delete_proj_mutation_literal():
  return run_gh_delete_proj_mutation_literal()

def test_gh_delete_proj_mutation_vars():
  return run_gh_delete_proj_mutation_vars()

def test_gh_delete_proj_v2_mutation_literal():
  return run_gh_delete_projectV2_mutation_literal()

def test_gh_delete_proj_v2_mutation_vars():
  return run_gh_delete_projectV2_mutation_vars()

def test_gh_create_issue_mutation_literal():
  return run_gh_create_issue_mutation_literal()

def test_gh_create_issue_mutation_vars():
  return run_gh_create_issue_mutation_vars()

def test_gh_create_proj_mutation_literal():
  return run_gh_create_proj_mutation_literal()

def test_gh_create_proj_mutation_vars():
  return run_gh_create_proj_mutation_vars()
#GITHUB - END

#RapidAPI - START

def test_ra_extensions_query_with_list():
  return run_ra_extensions_query_with_list()

def test_ra_eventTypes_query_with_list():
  return run_ra_eventTypes_query_with_list()

def test_ra_create_transformations_mutation_literal():
  return run_ra_create_transformations_mutation_literal()

def test_ra_create_transformations_mutation_vars():
  return run_ra_create_transformations_mutation_vars()

#INCONSISTENT ERROR COMPARED TO SCHEMA
# def test_ra_create_gateway_instance_mutation_literal():
#   return run_ra_create_gateway_instance_mutation_literal()

#INCONSISTENT ERROR COMPARED TO SCHEMA
# def test_ra_create_gateway_instance_mutation_vars():
#   return run_ra_create_gateway_instance_mutation_vars()

def test_ra_edit_user_alert_mutation_literal():
  return run_ra_edit_user_alert_mutation_literal()

def test_ra_edit_user_alert_mutation_vars():
  return run_ra_edit_user_alert_mutation_vars()
#RapidAPI - END

# ###################### MUTATIONS EXECUTION - END ##############################

# # # #FURTHER TESTS
def test_gdbc_complex_obj():
  return run_gdbc_complex_obj()

def test_gdbc_nested_object():
  return run_gdbc_nested_object()

def test_gdbc_nested_obj_args_literal():
  return run_gdbc_nested_obj_args_literal()

def test_gdbc_nested_obj_viewchange():
  return run_gdbc_nested_obj_viewchange()

def test_gdbc_complex_obj_args_literal():
  return run_gdbc_complex_obj_args_literal()

def test_gdbc_complex_obj_args_literal_2():
  return run_gdbc_complex_obj_args_literal_2()

def test_gdbc_complex_obj_viewchange():
  return run_gdbc_complex_obj_viewchange_vars()

def test_gdbc_nested_obj_viewchange_args_vars():
  return run_gdbc_nested_obj_viewchange_args_vars()

def test_gdbc_complex_obj_viewchange_args_vars():
  return run_gdbc_complex_obj_viewchange_args_vars()

def test_gdbc_nested_obj_args_vars():
  return run_gdbc_nested_obj_args_vars()

def test_gdbc_complex_obj_args_vars():
  return run_gdbc_complex_obj_args_vars()

def test_gdbc_nested_obj_with_list():
  return run_gdbc_nested_obj_with_list()

###################### ARGUMENTS AS FUNCTION PARAMETERS - START ##############################

def test_nested_obj_args_literal():
  return run_nested_obj_args_literal()

def test_nested_obj_args_vars():
  return run_nested_obj_args_vars()

def test_complex_obj_args_literal():
  return run_complex_obj_args_literal()

def test_complex_obj_args_vars():
  return run_complex_obj_args_vars()

def test_complex_obj_viewchange_args_literal():
  return run_complex_obj_viewchange_args_literal()

def test_complex_obj_viewchange_args_vars():
  return run_complex_obj_viewchange_args_vars()

def test_obj_composed_args_literal():
  return run_obj_composed_args_literal()

def test_obj_composed_args_vars():
  return run_obj_composed_args_vars()

def test_gh_add_comment_mutation_args_literal():
  return run_add_comment_mutation_args_literal()

def test_gh_add_comment_mutation_args_vars():
  return run_add_comment_mutation_args_vars()

#RapidAPI - START
def test_ra_admin_audit_logs_query_args_literal():
  return run_ra_admin_audit_logs_query_args_literal()

def test_ra_admin_audit_logs_query_args_vars():
  return run_ra_admin_audit_logs_query_args_vars()

def test_ra_create_transformations_mutation_args_literal():
  return run_ra_create_transformations_mutation_args_literal()

def test_ra_create_transformations_mutation_args_vars():
  return run_ra_create_transformations_mutation_args_vars()

#def test_ra_create_gateway_instance_mutation_args_literal():
#  return run_ra_create_gateway_instance_mutation_args_literal()

#def test_ra_create_gateway_instance_mutation_args_vars():
#  return run_ra_create_gateway_instance_mutation_args_vars()

def test_ra_edit_user_alert_mutation_args_literal():
  return run_ra_edit_user_alert_mutation_args_literal()

def test_ra_edit_user_alert_mutation_args_vars():
  return run_ra_edit_user_alert_mutation_args_vars()
#RapidAPI - END


##################### ARGUMENTS AS FUNCTION PARAMETERS - END ##############################
