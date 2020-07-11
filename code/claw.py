import robot_obj
import time
import threading

"""
Functions you're allowed to use:
grabClaw() - clamps claw asynchronously
openClaw() - opens claw asynchronously
grabClawSync() - clamps claw synchronously
openClawSync() - opens claw synchronously
clawIsClamped() - wait until claw has finished moving, then 
                  return true if the claw is clamped
clawIsFinished() - True if the claw has finished
waitOnClaw() - returns once the claw has finished moving
"""

releasing_time = 1

claw_lock = threading.Lock()

claw_is_closed = False

#set claw motor power
def setClaw(x):
    robot_obj.R.motors[1].m1.power = x

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
    #setClaw(0)
    return x

#closes claw synchronously
def grabClawSync():
    global claw_lock,claw_is_closed
    claw_lock.acquire()
    if claw_is_closed:
        claw_lock.release()
        return
    claw_is_closed = True
    setClaw(-100)
    print("Started at {0}".format(robot_obj.R.time()))    
    stopClawOnPress(timeout=1)
    print("Stopped at {0}".format(robot_obj.R.time()))
    claw_lock.release()

#closes claw asynchronously
def grabClaw():
    thr = threading.Thread(target=grabClawSync)
    thr.start()
    
#opens claw synchronously
def openClawSync():
    global claw_lock,claw_is_closed
    claw_lock.acquire()
    if not claw_is_closed:
        claw_lock.release()
        return
    claw_is_closed = False
    setClaw(100)
    robot_obj.R.sleep(releasing_time)
    setClaw(0)
    claw_lock.release()

#opens claw asynchronously
def openClaw():
    thr = threading.Thread(target=openClawSync)
    thr.start()
    
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

