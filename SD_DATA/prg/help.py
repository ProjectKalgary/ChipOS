import kernel.console as console
import kernel.registry as r

def PRG_INIT(args):
    if(len(args) != 1):
        console.writeline("ERROR: Invalid number of arguments")
        return
    devi = r.get("deviceinfo")
    cmds = cmdsort()
    console.writeline(devi[0] + " " + devi[1] + " Help Menu:")
    for entry in cmds:
        console.writeline(entry)

def cmdsort():
    cmds = []
    cmds.append("help - brings you here....duh")
    cmds.append("uname - lists system information")
    cmds.append("cls - clears screen")
    cmds.append("dir - lists contents of current directory")
    cmds.append("cd [dir] - changes directory to [dir]")
    cmds.append("say [message] - types [message] to console")
    cmds.append("py [python code] - executes [python code]")
    cmds.append("del [file/dir] - deletes [file/dir]")
    cmds.append("mkdir [dir] - creates directory [dir]")
    cmds.append("read [file] - reads contents of [file] to console")
    cmds.append("write [file] [data] - writes [data] to [file]")
    cmds.append("addf [file] [data] - appends [data] to the end of [file]")
    cmds.append("run [file] [args] - runs [file] as program with [args]")
    cmds.append("cmdfile [file] - runs [file] as if it were typed in the console")
    cmds.append("exit - exits current console")
    cmds.append("pim [file] - opens [file] in PIM (text editor)")
    cmds.sort()
    return cmds
