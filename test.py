from sr.robot import *
import time


R = Robot.setup()

R.ruggeduino_set_handler_by_fwver("SRcustom",Ruggeduino);

R.init()

R.wait_start()


def buttonPressed():
    R.ruggeduinos[0].pin_mode(2, INPUT_PULLUP)

    if R.ruggeduinos[0].digital_read(2) == False:
        return True
    else:
        return False

while True:
    R.motors[1].m0.power = -100
    clawTimerUp = time.time() + 2
    while not buttonPressed():
        if time.time() >= clawTimerUp:
            R.motors[1].m0.power = 0
    while buttonPressed():
        pass
    R.motors[1].m0.power = 100
    clawTimerUp = time.time() + 2
    while not buttonPressed():
        if time.time() >= clawTimerUp:
            R.motors[1].m0.power = 0
    while buttonPressed():
        pass
