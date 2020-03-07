from sr.robot import *
#from button import buttonPressed
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
    while not buttonPressed():
        R.motors[1].m1.power = -50
    R.motors[1].m1.power = 0
    time.sleep(3)
    R.motors[1].m1.power = 50
    time.sleep(1)
    R.motors[1].m1.power = 0
    time.sleep(3)
