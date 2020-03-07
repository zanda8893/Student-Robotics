import robot
from sr.robot import *
import time

class claw(object):
    def __init__(self):
        self.clawTimerUp = 0
        self.grabTimer = 0
        self.clawUp = False
        self.grabbing = False
        self.grabbed = False
        self.R = Robot()

    def moveClawUp(self):
        if self.clawUp == False:
            R.motors[0].m1.power = 100
            self.clawTimerUp = time.time_ns() + 4*1000*1000
            self.clawUp = True

    def moterCheck(self):
        if time.time_ns() >= self.clawTimerUp():
            R.motors[0].m1.power = 0

    def moveClawDown(self):
        if self.clawUp == True:
            R.motors[0].m1.power = 100
            self.clawTimerUp = time.time_ns() + 4*1000*1000
            self.clawUp = False

    def grab():
        if self.grabbing == False
            R.moter[0].m1.power = 0
        elif self.grabbed == False:
            
