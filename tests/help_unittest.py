
import os
import logging as logger

def run_generator_cmd_help():
    logger.debug('\nRunning run_generator_cmd_help...')
    command = "CodeGenerator -h" #command to be executed
    logger.debug("Launching: " + command)

    ret = os.system(command)
    logger.debug("End of run_generator_cmd_help")
