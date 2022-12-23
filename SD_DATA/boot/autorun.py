import os
import kernel.console as console
import kernel.registry as registry

def PRG_INIT(args):
    registry.set("gd", args[0])
    registry.set("deviceinfo", args[1])
    registry.set("kernelinfo", args[2])
    console.setgd(args[0])
    console.writeline("Loading...")
    if not('prg' in os.listdir("/sd")):
        console.setrgb(0xFF, 0x00, 0x00)
        console.writeline("SYSTEMERROR: prg directory not found.")
    elif not('cmd.py' in os.listdir("/sd/prg")):
        console.setrgb(0xFF, 0x00, 0x00)
        console.writeline("SYSTEMERROR: cmd.py file not found.")
    else:
        import prg.cmd as cmd
        console.clear()
        cmd.PRG_INIT(["cmd"])
