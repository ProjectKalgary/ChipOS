import kernel.console as console

def PRG_INIT(args):
    if(len(args) < 2):
        console.writeline("ERROR: Invalid number of arguments.")
        return
    else:
        py = args
        del py[0]
        try:
            exec(' '.join([str(a) for a in py]))
        except Exception as e:
            console.writeline("PYERROR: " + str(e))
