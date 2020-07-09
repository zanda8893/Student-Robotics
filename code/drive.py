import robot_obj
import time
import threading

"""
Functions you're allowed to use:
kill() - should be called when the entire code exits
driveStraightSync(power,t) - drive straight at power ~power~ for t seconds
driveStraight(power,t) - as above but asynchronously.
                         Negative t makes it drive indefinitely
driveRotateSync(power,t) - same as driveStraightSync() but rotates
driveRotate(power,t) - same as driveStraight() but rotates
driveDone() - True if drive not pending turn-off (ie either stopped or
              moving indefinitely)
driveWait() - returns once the drive has finished (note that it returns
              immediately if the drive is moving indefinitely)
"""

#must be held to set the drive
drive_lock = threading.Lock()

#time at which to turn off motors, negative if never
stop_time = -1
stop_lock = threading.Lock()
stop_cond = threading.Condition(stop_lock)

#stop_lock must be held to access killed
killed = False

#set drive - do not use from outside this file
def setDrive(l,r):
    #print("Setting drive to {0},{1} at {2}".format(l,r,time.time()))
    robot_obj.R.motors[0].m0.power = l
    robot_obj.R.motors[0].m1.power = r

def watchStopTime():
    global stop_cond,stop_time,drive_lock,killed
    stop_cond.acquire()
    while not killed:
        if stop_time > 0 and time.time() >= stop_time:
            drive_lock.acquire()
            setDrive(0,0)
            drive_lock.release()
            stop_time = -1
            stop_cond.notify_all()
        else:
            if stop_time > 0:
                stop_cond.wait(timeout=(stop_time - time.time()))
            else:
                stop_cond.wait()
    stop_cond.release()

def kill():
    global stop_cond,drive_lock,killed
    stop_cond.acquire()
    drive_lock.acquire()
    setDrive(0,0)
    killed = True
    stop_cond.notify_all()
    drive_lock.release()
    stop_cond.release()
    
def driveWait():
    global stop_cond,stop_time
    stop_cond.acquire()
    while stop_time >= 0:
        stop_cond.wait()
    stop_cond.release()

def drive(left,right,t):
    global drive_lock,stop_cond,stop_time

    stop_cond.acquire()
    
    drive_lock.acquire()
    setDrive(left,right)
    drive_lock.release()

    if t >= 0:
        stop_time = time.time() + t
        stop_cond.notify_all()
    else:
        stop_time = -1
        stop_cond.notify_all()

    stop_cond.release()

    
#drive in a striaght line for t seconds
#negative t means it sets the power indefinitely
def driveStraightSync(power,t):
    drive(power,power,t)
    driveWait()
    
#drive in a straight line in the background
def driveStraight(power,t=-1):
    drive(power,power,t)

def driveRotateSync(power,t):
    drive(-power,power,t)
    driveWait()

#rotate anticlockwise asynchronously
def driveRotate(power,t=-1):
    drive(-power,power,t)

#true if all asynchronnous operations have finished
def driveDone():
    global stop_cond,stop_time
    stop_cond.acquire()
    ret = False
    if stop_time < 0:
        ret = True
    stop_cond.release()
    return ret

def init():
    wst = threading.Thread(target=watchStopTime)
    wst.start()

init()
