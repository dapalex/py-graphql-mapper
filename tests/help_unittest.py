
import os
import logging as logger

def run_generator_cmd_help():
    logger.info('\nRunning run_generator_cmd_help...')
    command = "CodeGenerator -h" #command to be executed
    logger.info("Launching: " + command)

    ret = os.system(command)
    logger.info("End of run_generator_cmd_help")
