import robot_obj
import time
import threading

releasing_time = 1

claw_lock = threading.Lock()

claw_is_closed = False

#set claw motor power
def setClaw(x):
    robot_obj.R.motors[1].m0.power = x

#returns true when it doesn't timeout
def stopClawOnPress(timeout=-1):
    global claw_lock
    t0 = robot_obj.R.time()
    x = False
    while True:
        x = robot_obj.R.ruggeduinos[0].digital_read(4)
        if x:
            break
        elif (robot_obj.R.time()-t0 > timeout) and timeout >= 0:
            break
        else:
            robot_obj.R.sleep(0.02)
    setClaw(0)
    return x

#closes claw asynchronously
def grabClaw():
    thr = threading.Thread(target=grabClawSync)
    thr.start()

#opens claw asynchronously
def openClaw():
    thr = threading.Thread(target=openClawSync)
    thr.start()

#closes claw synchronously
def grabClawSync():
    global claw_lock,claw_is_closed
    claw_lock.acquire()
    if not claw_is_closed:
        claw_lock.release()
        return
    claw_is_closed = True
    robot_obj.R.motors[1].m0.power = 100
    stopClawOnPress()
    claw_lock.release()

#opens claw synchronously
def openClawSync():
    global claw_lock,claw_is_closed
    claw_lock.acquire()
    if claw_is_closed:
        claw_lock.release()
        return
    claw_is_closed = False
    setClaw(-100)
    robot_obj.R.sleep(releasing_time)
    setClaw(0)
    claw_lock.release()

#wait for claw to stop moving, then return clampedness
def clawIsClamped():
    global claw_lock
    claw_lock.acquire()
    x = claw_is_closed
    claw_lock.release()
    return x

#returns true if claw has finished moving
def clawIsFinished():
    global claw_lock
    return not claw_lock.locked()

#wait for claw to finish moving
def waitOnClaw():
    global claw_lock
    claw_lock.acquire()
    claw_lock.release()

