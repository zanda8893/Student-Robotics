from sr.robot import *
R = Robot()

from button import *

def close():
    while buttonPressed():
        R.motors[1].m1.power = 100

    while not buttonPressed():
        R.motors[1].m1.power = 0

def open():
    while not buttonPressed():
        R.motors[1].m1.power = -100

    while buttonPressed():
        R.motors[1].m1.power = 0
