import io
import os
import kernel.console as console

def PRG_INIT(args):
    if len(args) < 2:
        console.writeline("ERROR: Invalid number of arguments.")
        return
    elif not(args[1] in os.listdir()):
        console.writeline("FILEERROR: " + args[1] + " doesn't exist.")
    elif '.protectdir' in os.listdir():
        console.writeline("FILERROR: Directory is protected.")
    else:
        cont = args
        del cont[0]
        try:
            f = io.open(args[0], "a")
            del cont[0]
            f.write(' '.join([str(a) for a in cont]).replace("\\n", "\n").replace("\\t", "    "))
            f.close()

        except Exception as e:
            console.writeline("FILEERROR: " + e + ".")
