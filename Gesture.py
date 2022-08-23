import cv2
import numpy as np
import math

class FingerDetect():

    def __init__(self, lmlist, show = False):

        x = 0.06 #module for beter workig
        self.lmlist = lmlist
        self.finger_list = []
        if lmlist:
            wrist_x, wrist_y = self.lmlist[1][0][1], self.lmlist[1][0][2]
            indb_x, indb_y = self.lmlist[1][5][1], self.lmlist[1][5][2]
            self.hand_x, self.hand_y = int((wrist_x + indb_x)/2), int((wrist_y + indb_y)/2)
            self.def_len = math.hypot(indb_x - wrist_x, indb_y - wrist_y)
            self.def_len = (self.def_len*x)+self.def_len
             # thumb, index, middle, ring, pinky
            for i in range(4,24,4): #sprawdzanie palców
                x, y = self.lmlist[1][i][1], self.lmlist[1][i][2]
                fing_len = math.hypot(x - wrist_x, y - wrist_y)

                if fing_len > self.def_len:
                    self.finger_list.append(1)
                else:
                    self.finger_list.append(0)

    def fingerCounter(self):

        x = 0
        for i in self.finger_list:
            x += i
        return x

    def fingerUp(self):
        positions = []
        dict = {0: "kciuk", 1: "wskazujacy", 2: "srodkowy", 3: "serdeczny", 4: "maly"}
        for i in range(5):
            if self.finger_list[i]== 1:
                positions.append(dict[i]+" gora")
            else:
                positions.append(dict[i]+" dol")
        return positions

    def gesture(self):
        if len(self.finger_list) != 0:
            len_im = abs(self.lmlist[1][8][1] - self.lmlist[1][12][1])  # length from index to middle
            len_mr = abs(self.lmlist[1][12][1] - self.lmlist[1][16][1])  # length from middle to ring
            len_rp = abs(self.lmlist[1][16][1] - self.lmlist[1][20][1])  # length from ring to pinky
            default = self.def_len * 0.2
            if self.finger_list[1] == 1 and self.finger_list[2] == 1 and self.finger_list[3] == 1 and self.finger_list[4] == 1:
                if len_im > default and len_mr > default and len_rp > default:
                    #print("otwarta 5 palcow")
                    return 1
                else:
                    #print("zamknieta 5 palcow")
                    return 2
            elif self.finger_list[1] == 1 and self.finger_list[2] == 1 and self.finger_list[3] == 0 and self.finger_list[4] == 0:
                if len_im > default:
                    #print("otwarta 2 palce")
                    return 3
                else:
                    #print("zamknieta 2 palce")
                    return 4
            elif self.finger_list[1] == 1 and self.finger_list[2] == 1 and self.finger_list[3] == 1 and self.finger_list[4] == 0:
                if len_im > default and len_mr > default:
                    #print("otwarta 3 palce")
                    return 5
                else:
                    #print("zamknieta 3 palce")
                    return 6
            elif self.finger_list[1] == 1 and self.finger_list[2] == 0 and self.finger_list[3] == 0 and self.finger_list[4] == 1:
                #print("metal")
                return 7
            elif self.finger_list[1] == 0 and self.finger_list[2] == 0 and self.finger_list[3] == 0 and self.finger_list[4] == 1:
                #print("telefon")
                return 8
            elif self.finger_list[1] == 1 and self.finger_list[2] == 1 and self.finger_list[3] == 0 and self.finger_list[4] == 1:
                #print("3 palce odstep")
                return 9
            elif self.finger_list[1] == 0 and self.finger_list[2] == 0 and self.finger_list[3] == 0 and self.finger_list[4] == 0:
                #print("zamknieta")
                return 0

        else:
            pass

    def gesture_mouse(self):
        if len(self.finger_list) != 0:
            len_im = abs(self.lmlist[1][8][1] - self.lmlist[1][12][1])  # length from index to middle
            len_mr = abs(self.lmlist[1][12][1] - self.lmlist[1][16][1])  # length from middle to ring
            len_rp = abs(self.lmlist[1][16][1] - self.lmlist[1][20][1])  # length from ring to pinky
            default = self.def_len * 0.2
            print(self.finger_list)
            if self.finger_list[1] == 1 and self.finger_list[2] == 1 and self.finger_list[3] == 1 and self.finger_list[4] == 1 and self.finger_list[0] == 1:
                #otwarta
                return 0
            elif self.finger_list[1] == 0 and self.finger_list[2] == 0 and self.finger_list[3] == 0 and self.finger_list[4] == 0:
                #print("zamknieta")
                return 1
            elif self.finger_list[1] == 1 and self.finger_list[2] == 1 and self.finger_list[3] == 1 and self.finger_list[4] == 1 and self.finger_list[0] == 0:
                #otwarta z zamknietym kciukiem
                return 2
    def x_pos(self):
        return int(self.hand_x)

    def y_pos(self):
        return int(self.hand_y)





