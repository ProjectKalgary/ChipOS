import os
import kernel.console as console

def PRG_INIT(args):
    if len(args) != 2:
        console.writeline("ERROR: Invalid number of arguments.")
        return
    elif args[1] in os.listdir():
        console.writeline("FILEERROR: " + args[1] + " already exists.")
    elif '.protectdir' in os.listdir():
        console.writeline("FILERROR: Directory is protected.")
    else:
        os.mkdir(args[1])
