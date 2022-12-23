import os
import kernel.console as console

def PRG_INIT(args):
    if(len(args) != 1):
        console.writeline("ERROR: Invalid number of arguments.")
        return
    folder = os.listdir()
    curdir = ["./", "../"]
    for file in folder:
        if os.stat(os.getcwd() + "/" + file)[0] == 0x4000:
            curdir.append(file + "/")
        else:
            curdir.append(file)
    console.writeline(str(curdir))
