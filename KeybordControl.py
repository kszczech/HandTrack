import Gesture as g
import time
import keyboard as pag

#bind build
#[[bind,mode]]
def binds():
    f = open("binds.txt", "r")
    lines = f.readlines()
    bind = []
    j = 0
    for i in lines:
        line = i.split()
        line[1] = int(line[1])
        line.append(j)
        j += 1
        bind.append(line)
    f.close()
    return bind

def keyboardOutput(handsig1, handsig2, binds):
    if handsig2 == None:
        if handsig1 != None:
            if binds[handsig1][0] != "nic" and binds[handsig1][1] == 1:
                pag.send(binds[handsig1][0])
            elif binds[handsig1][0] != "nic" and binds[handsig1][1] == 0:
                pag.press(binds[handsig1][0])
    elif handsig1 == handsig2:
        pass
    elif handsig1 != handsig2:
        if handsig1 != None and handsig2 != None and binds[handsig2][0] != "nic":
            pag.release(binds[handsig2][0])

            if binds[handsig1][0] != "nic" and binds[handsig1][1] == 1:
                pag.send(binds[handsig1][0])
            elif binds[handsig1][0] != "nic" and binds[handsig1][1] == 0:
                pag.press(binds[handsig1][0])













