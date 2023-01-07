
import os

def runGeneratorCommandHelp():
    print('\nRunning runGeneratorCommandHelp...')
    command = "CodeGenerator -h" #command to be executed
    print("Launching: " + command)
    
    ret = os.system(command)
    print("End of runGeneratorCommandHelp")
    