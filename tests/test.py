
import sys
import os
import pathlib


sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

# from help_unittest import run_generator_cmd_help
# from test_cli import (run_download_cmd_gdbc_file_rel, run_generate_cmd_ra_api_abs, run_download_cmd_ra_file_rel,
#                                     run_generate_cmd_gdbc_api_rel, run_download_cmd_gh_file_rel, run_generate_cmd_gh_api_abs)
from gdbc_unittest import (run_fetch_gdbc_schema, run_fetch_gdbc_schema_no_desc)
from gh_unittest import (run_gh_add_comment_mutation,
                               run_gh_create_issue_mutation, run_gh_create_proj_mutation, run_gh_delete_proj_mutation,
                               run_gh_delete_proj_v2_mutation, run_gh_update_repo_mutation, run_fetch_gh_schema, run_fetch_gh_schema_no_desc)
from ra_unittest import ( run_ra_create_gateway_instance_mutation,
                              run_ra_create_transformations_mutation, run_ra_edit_user_alert_mutation,
                              run_ra_admin_audit_logs, run_fetch_ra_schema, run_fetch_ra_schema_no_desc)


###################### CODE GENERATION - START ##############################

# cleanOutput(OutputType.SCHEMAS)
run_fetch_gdbc_schema()
run_fetch_gdbc_schema()
run_fetch_gdbc_schema_no_desc()
run_fetch_gh_schema_no_desc()
run_fetch_gh_schema()
run_fetch_ra_schema_no_desc()
run_fetch_ra_schema()

#gdbc API - START
#gdbc API - END

###################### COMMAND LINE INTERFACE - START ##############################
# cleanOutput(OutputType.COMMANDS)

# run_generator_cmd_help()
# run_download_cmd_gdbc_file_rel()
# run_generate_cmd_gdbc_api_rel()
# run_download_cmd_gh_file_rel()
# run_generate_cmd_gh_api_abs()
# run_generate_cmd_gdbc_api_rel()
# run_download_cmd_ra_file_rel()
# run_generate_cmd_ra_api_abs()
###################### COMMAND LINE INTERFACE - END ##############################

###################### CODE GENERATION - END ##############################

###################### QUERIES EXECUTION - START ##############################
from unittests import (run_gdbc_complex_obj_viewchange, run_gdbc_complex_obj_viewchange_args_vars,
                        run_gdbc_complex_obj_args_vars, run_gdbc_complex_obj_args_literal,
                        run_gdbc_complex_obj_args_literal_2, runNestedObject, run_gdbc_nested_obj_viewchange,
                        run_gdbc_nested_obj_viewchange_args_vars, run_gdbc_nested_obj_args_vars,
                        run_gdbc_nested_obj_args_literal, run_gdbc_obj_composed_args)
from tstquery.complex_obj_test import run_gdbc_complex_obj
from tstquery.connobj_args_literal_test import run_gdbc_connobj_args_literal
from tstquery.connobj_args_vars_test import run_gdbc_connobj_args_vars
from tstquery.connobj_view_change_test import run_gdbc_connobj_viewchange
from tstquery.connobj_test import run_gdbc_connobj
from tstquery.manual_obj_test import runGeneratedDataAsGQLObject
from tstquery.simple_obj_test import run_simple_obj
from tstquery.simple_obj_args_literal_test import run_simple_objargs_literal
from tstquery.simple_obj_args_vars_test import run_simple_args_vars
from tstquery.simple_obj_view_change_test import runSimpleOobj_viewchange
from tstmutation.manual_mutation_test import run_gh_insert_literal_mutation
from tstmutation.mutation_test import run_gh_update_literal_mutation

runGeneratedDataAsGQLObject()
run_simple_obj()
run_simple_objargs_literal()
run_simple_args_vars()
runSimpleOobj_viewchange()
run_gdbc_connobj()
run_gdbc_connobj_viewchange()
run_gdbc_connobj_args_vars()
run_gdbc_connobj_args_literal()

run_gdbc_complex_obj()

# # #FURTHER runS
run_gdbc_nested_obj_args_literal()
run_gdbc_nested_obj_viewchange()
run_gdbc_complex_obj_args_literal()
run_gdbc_complex_obj_args_literal_2()
run_gdbc_obj_composed_args()
run_gdbc_complex_obj_viewchange()
run_gdbc_nested_obj_viewchange_args_vars()
run_gdbc_complex_obj_viewchange_args_vars()
run_gdbc_nested_obj_args_vars()
run_gdbc_complex_obj_args_vars()
#Geo DB Cities - END

###################### QUERIES EXECUTION - END ##############################

###################### MUTATIONS EXECUTION - START ##############################

run_gh_update_literal_mutation()
run_gh_insert_literal_mutation()

#GITHUB API - START
run_gh_add_comment_mutation()
run_gh_update_repo_mutation()
run_gh_delete_proj_mutation()
run_gh_delete_proj_v2_mutation()
run_gh_create_issue_mutation()
run_gh_create_proj_mutation()
#GITHUB - END

#RapidAPI - START
run_ra_admin_audit_logs()
run_ra_create_transformations_mutation()
run_ra_create_gateway_instance_mutation()
run_ra_edit_user_alert_mutation()
#RapidAPI - END

###################### MUTATIONS EXECUTION - END ##############################