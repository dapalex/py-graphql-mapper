
import os
import logging as logger

def runGeneratorCommandHelp():
    logger.info('\nRunning runGeneratorCommandHelp...')
    command = "CodeGenerator -h" #command to be executed
    logger.info("Launching: " + command)

    ret = os.system(command)
    logger.info("End of runGeneratorCommandHelp")
