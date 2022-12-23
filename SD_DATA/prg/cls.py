import kernel.console as console

def PRG_INIT(args):
    if(len(args) != 1):
        console.writeline("ERROR: Invalid number of arguments.")
        return
    console.clear()
