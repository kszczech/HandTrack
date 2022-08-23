import Gesture as g
import pyautogui as pag
import numpy as np

def mouseOutput(hand,handsig1, handsig2, prex, prey, rCam, wCam=640, hCam=480):

    try:
        wScr, hScr = pag.size()
        smoth = 2

        hand_x = hand.x_pos()
        hand_y = hand.y_pos()
        x = int(np.interp(hand_x, (rCam,wCam-rCam), (0,wScr)))
        y = int(np.interp(hand_y, (rCam, hCam-rCam), (0, hScr)))

        x = prex + (x - prex) / smoth
        y = prey + (y - prey) / smoth
        print(x,y)
        if handsig1 == 0 and handsig2 == 2:
            pag.mouseUp(button='right')
        if handsig1 == 0 and handsig2 == 1:
            pag.mouseUp()

        if handsig1 == 0 and handsig2 == handsig1: #otwarta
            pag.moveTo(x,y)
            print("otwarta")
        elif handsig1 == 1 : #zamknietaac
            pag.mouseDown()
            pag.moveTo(x,y)
            print("zamknieta")
        elif handsig1 == 2 : #kciuka
            pag.moveTo(x, y)
            pag.mouseDown(button='right')
            print("kciuk")
        return x, y
    except:
        return prex, prey



