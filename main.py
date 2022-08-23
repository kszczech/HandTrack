import HandTrackingModule as htm
import cv2
import numpy as np
import Gesture as g
import KeybordControl as kc
import MouseControl as mc
import time
import pyautogui as pag

#video conf
wCam, hCam = 640, 480
frameR = 100

pusty = np.zeros((640,500,3),np.uint8)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, wCam)
cap.set(4, hCam)
ptime = 0
detector = htm.handDetector(detectionCon=0.75, trackCon=0.6)

#signal control
rhandsig1 = None
rhandsig2 = None
lhandsig1 = None
lhandsig2 = None

#binds
binds = kc.binds()

#dealay
wait = 0
wait_conf = 10

prex = 0
prey = 0
x = 0
y = 0

print(binds)

while True:

    pusty = np.zeros((640, 500, 3), np.uint8)
    success1, img = cap.read()
    img = cv2.flip(img,1)
    cv2.rectangle(img,(frameR,frameR), (wCam-frameR, hCam-frameR), (255,0,0),1)
    detector.findHands(img,True)
    list_0 = detector.findPosition(img, 0, False)
    list_1 = detector.findPosition(img, 1, False)
    if len(list_0) != 0:
        wait = 0
        if list_0[0] == '"Left"':
            list_l = list_0
            list_r = list_1
        elif list_0[0] == '"Right"':
            list_r = list_0
            list_l = list_1

        hand_r = g.FingerDetect(list_r)
        hand_l = g.FingerDetect(list_l)

        rhandsig1 = hand_r.gesture()
        lhandsig1 = hand_l.gesture_mouse()

        kc.keyboardOutput(rhandsig1,rhandsig2,binds)
        x, y = mc.mouseOutput(hand_l, lhandsig1, lhandsig2, prex, prey, frameR)
        prex, prey = x, y
        #print(hand_l.finger_list)
        rhandsig2 = rhandsig1
        lhandsig2 = lhandsig1


    wait += 1
    cv2.imshow("image", img)
    cv2.imshow("pusty", pusty)

    cv2.waitKey(1)
