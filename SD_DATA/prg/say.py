import kernel.console as console

def PRG_INIT(args):
    if(len(args) < 2):
        console.writeline("ERROR: Invalid number of arguments.")
        return
    else:
        say = args
        del say[0]
        console.writeline(' '.join([str(a) for a in say]))
