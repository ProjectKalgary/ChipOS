import os
import kernel.console as console

def PRG_INIT(args):
    if len(args) < 2:
        console.writeline("ERROR: Invalid number of arguments.")
        return
    elif args[1] + ".py" in os.listdir() or args[1] + ".mpy" in os.listdir():
        file = os.getcwd().replace("/", ".") + "." + args[1]
        file = file[4:]
        try:
            a = args
            del a[0]
            load = my_import(file)
            load.PRG_INIT(a)
        except Exception as e:
            console.writeline("PROGRAMERROR: " + str(e) + ".")
    else:
        console.writeline("ERROR: " + args[1] + ".py/.mpy doesn't exist.")

def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod
