import kernel.console as c
import kernel.utils as u
import os
import io
import time

def editor(f, args):
    c.settextmode(0)
    line = 1
    temp = u.copy(f)

    if len(temp) == 0:
        temp = [" "]

    for i in range(len(temp)):
        if temp[i] == "\n":
            temp[i] = temp[i].replace("\n", " ")
        else:
            temp[i] = temp[i].replace("\n", "")

    fmem = u.copy(temp)
    vmem = []
    command = [""]

    for i in range(33):
        fmem.append("")

    app = True
    while app:
        if command[0] == "" and len(command) == 1:
            time.sleep(0)
        elif command[0] == "q" and len(command) == 1:
            return
        elif command[0] == "g" and len(command) == 2:
            if int(command[1]) <= len(temp) and int(command[1]) - 1 >= 0:
                line = int(command[1])
        elif command[0] == "w" and len(command) >= 1:
            del command[0]
            if len(command) == 0:
                temp[line-1] = " "
            else:
                temp[line-1] = ' '.join([str(a) for a in command])
        elif command[0] == "i" and len(command) >= 2:
            if int(command[1]) > len(temp):
                for i in range(int(command[1]) - len(temp) - 1):
                    temp.append(" ")
            ins = u.copy(command)
            del ins[0]
            del ins[0]
            if len(ins) == 0:
                ins.append(" ")
            temp.insert(int(command[1]), ' '.join([str(a) for a in ins]))
        elif command[0] == "s" and len(command) == 1:
            file = io.open(args[1], "w")
            for lin in temp:
                file.write('%s\n' % lin)
            file.close()
        elif command[0] == "d" and len(command) == 1:
            if line == 1:
                temp[line - 1] == " "
            else:
                del temp[line - 1]
                line -= 1

        fmem = u.copy(temp)
        for i in range(33):
            fmem.append("")

        vmem = updatevmem(line, fmem, command)
        c.customupdate(vmem)
        time.sleep(.2)
        cmd = input(":")
        command = cmd.split(" ")
        if len(command) >= 1:
            command[0] = command[0].lower()

def updatevmem(line, fmem, command):
    vmem = []

    vmem.append(str(line) + ":>" + fmem[line - 1])
    for i in range(32):
        if not(i == 0):
            if fmem[line-1+i] == "":
                vmem.append(" ")
            else:
                vmem.append(str(line + i) + ":--" + fmem[line-1+i])
    vmem.append("-"*243)
    vmem.append(":" + ' '.join([str(a) for a in command]))
    return vmem

def PRG_INIT(args):
    if(len(args) != 2):
        c.writeline("ERROR: Invalid number of arguments.")
        return
    elif args[1] in os.listdir():
        if os.stat(os.getcwd() + "/" + args[1])[0] == 0x4000:
            c.writeline("FILEERROR: " + args[1] + " is a directory.")
        else:
            file = io.open(args[1], "rt")
            lines = file.readlines()
            file.close()
            editor(lines, args)

    else:
        c.writeline("FILEERROR: "+args[1]+" does not exist in "+str(os.getcwd()) + ".")

