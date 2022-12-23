import io
import os
import kernel.console as c

def PRG_INIT(args):
    if len(args) != 2:
        c.writeline("ERROR: Invalid number of arguments.")
        return
    elif args[1] in os.listdir():
        if os.stat(os.getcwd() + "/" + args[1])[0] == 0x4000:
            c.writeline("FILEERROR: " + args[1] + " is a directory.")
        else:
            file = io.open(args[1], "rt")
            lines = file.readlines()
            file.close()
            for line in lines:
                c.writeline(str(line))
    else:
        c.writeline("FILEERROR: "+args[1]+" does not exist in "+str(os.getcwd()) + ".")
