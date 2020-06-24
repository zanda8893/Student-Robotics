#import robot_obj
import time
import threading

drive_active = False

#must be held to set the drive
drive_lock = threading.Lock()

#signalled when current state is to be overridden
override_cond = threading.Condition(drive_lock)

#set drive - do not use from outside this file
def setDrive(l,r):
    print("Setting drive to {0},{1} at {2}".format(l,r,time.time()))
    #robot_obj.R.motors[0].m0.power = l
    #robot_obj.R.motors[0].m1.power = r

#drive in a striaght line for t seconds
#negative t means it sets the power indefinitely
def driveStraightSync(power,t):
    global drive_lock,override_cond

    if not override_cond.locked():
        override_cond.acquire()
        
    drive_active = True
    override_cond.notify_all() 
    
    setDrive(power,power)

    res = True
    if t < 0:
        override_cond.wait() #run indefinitely (until overridden)
    else:
        #wait until another thread sets the drive or timeout
        res = override_cond.wait(timeout=t)

    if not res: #timed out
        setDrive(0,0)
        drive_active = False
        inactive_cond.notify_all()
        
    override_cond.release()
    
#drive in a straight line in the background
def driveStraight(power,t=-1):
    global drive_lock
    drive_lock.acquire()
    while drive_active == False:
        inactive_cond.wait()
    drive_active = True
    override_cond.notify_all()

    setDrive(power,power)
    res = True
    if t < 0:
        override_cond.wait()
    else:
        res = override_cond.wait(timeout=t)

    
    thr = threading.Thread(target=driveStraightSync,args=(power,t))
    thr.start()

#rotate anticlockwise at power p synchronously
def driveRotateSync(power,t):
    global drive_lock,override_cond
    drive_lock.acquire()
    override_cond.notify_all()
    setDrive(power,-power)

    res = True
    if t < 0:
        override_cond.wait()
    else:
        res = override_cond.wait(timeout=t)

    if not res:
        setDrive(0,0)
    drive_lock.release()


#rotate anticlockwise asynchronously
def driveRotate(power,t=-1):
    thr = threading.Thread(target=driveRotateSync,args=(power,t))
    thr.start()

#wait for drive to finish
def waitDrive():
    pass
