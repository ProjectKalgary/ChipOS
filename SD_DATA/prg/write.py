import io
import os
import kernel.console as console

def PRG_INIT(args):
    if len(args) < 3:
        console.writeline("ERROR: Invalid number of arguments.")
        return
    elif args[1] in os.listdir():
        console.writeline("FILEERROR: " + args[1] + " already exists.")
    elif '.protectdir' in os.listdir():
        console.writeline("FILERROR: Directory is protected.")
    else:
        cont = args
        del cont[0]
        if cont[0] == ".protectdir":
            console.writeline("FILEERROR: Cannot create .protectdir file")
        else:
            try:
                f = io.open(args[0], "w")
                del cont[0]
                f.write(' '.join([str(a) for a in cont]).replace("\\n", "\n").replace("\\t", "    "))
                f.close()
            except Exception as e:
                console.writeline("FILEERROR: " + e + ".")
