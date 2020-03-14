from sr.robot import *
import time as time

class claw(object):
    def __init__(self):
        self.clawTimerUp = 0
        self.grabTimer = 0
        self.clawUp = False
        self.grabbing = False
        self.grabbed = False
        self.R = Robot()

        self.R.ruggeduino_set_handler_by_fwver("SRcustom",Ruggeduino)
        self.R.init()
        self.R.wait_start()

    def buttonPressed(self):
        self.R.ruggeduinos[0].pin_mode(2, INPUT_PULLUP)
        if self.R.ruggeduinos[0].digital_read(2) == False:
            self.R.moters.m0.power = 0

    def moveClawUp(self):
        if self.clawUp == False:
            self.R.motors[0].m1.power = 100
            self.clawTimerUp = time()+4
            self.clawUp = True

    def moterCheck(self):
        if time()>= self.clawTimerUp():
            self.R.motors[0].m1.power = 0

    def moveClawDown(self):
        if self.clawUp == True:
            self.R.motors[0].m1.power = 100
            self.clawTimerUp = time() + 4
            self.clawUp = False

    def grab(self):
        self.R.moters[0].m0.power = 10
