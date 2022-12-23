import os
import kernel.console as c

def PRG_INIT(args):
    if len(args) != 2:
        c.writeline("ERROR: Invalid number of arguments.")
        return
    elif args[1] in os.listdir():
        if ".protectdir" in os.listdir():
            c.writeline("FILEERROR: Directory is protected.")
        else:
            if os.stat(os.getcwd() + "/" + args[1])[0] == 0x4000:
                try:
                    os.rmdir(args[1])
                except Exception as e:
                    c.writeline("FILEERROR: " + str(e) + ".")
            else:
                try:
                    os.remove(args[1])
                except Exception as e:
                    c.writeline("FILEERROR: " + str(e) + ".")
    else:
        c.writeline("FILEERROR: "+args[1]+" does not exist in "+str(os.getcwd()) + ".")
