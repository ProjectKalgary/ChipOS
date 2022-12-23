import os
import kernel.console as console

def PRG_INIT(args):
    if(len(args) != 2):
        console.writeline("ERROR: Invalid number of arguments.")
        return
    elif args[1] in os.listdir() or args[1] == "." or args[1] == "..":
        if os.stat(os.getcwd() + "/" + args[1])[0] == 0x4000:
            os.chdir(args[1])
        else:
            console.writeline("FILEERROR: " + args[1] + " is not a directory.")
    else:
        console.writeline("FILEERROR: " + args[1] + " doesn't exist.")
