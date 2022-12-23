import kernel.console as console
import kernel.registry as r

def PRG_INIT(args):
    if(len(args) != 1):
        console.writeline("ERROR: Invalid number of arguments")
        return
    devi = r.get("deviceinfo")
    kinf = r.get("kernelinfo")

    btlgf = open("/boot_out.txt", "rt")
    btlg = btlgf.read()
    btlgf.close()

    console.writeline("System Info: " + devi[0] + " " + devi[1])
    console.writeline("Kernel Info: " + kinf[0] + " " + kinf[1])
    console.writeline("Boot Info: " + btlg)
    console.writeline("")
