import robot_obj
import time
import threading

lifting_time = 1

lift_lock = threading.Lock()

lift_is_raised = 0

#set lift motor power
def setLift(x):
    robot_obj.R.motors[1].m1.power = x
    
#asynchronously raise lift
def raiseLift():
    thr = threading.Thread(target=raiseLiftSync)
    thr.start()

#asynchronously lower lift
def lowerLift():
    thr = threading.Thread(target=lowerLiftSync)
    thr.start()

#synchronously raise lift
def raiseLiftSync():
    global lift_lock,lift_is_raised
    lift_lock.acquire()
    if lift_is_raised:
        lift_lock.release()
        return
    lift_is_raised = True
    setLift(100)
    robot_obj.R.sleep(lifting_time)
    setLift(0)
    lift_lock.release()    

#synchronously lower lift
def lowerLiftSync():
    global lift_lock,lift_is_raised
    lift_lock.acquire()
    if not lift_is_raised:
        lift_lock.release()
        return
    lift_is_raised = False
    setLift(-100)
    robot_obj.R.sleep(lifting_time)
    setLift(0)
    lift_lock.release()

#wait for lift to finish moving, then return liftedness
def liftIsRaised():
    global lift_lock
    lift_lock.acquire()
    x = lift_is_raised
    lift_lock.release()
    return x

#returns true if the lift has finished moving (either direction)
def liftIsFinished():
    global lift_lock
    return not lift_lock.locked()

#wait for lift to finish moving (either direction)
def waitOnLift():
    global lift_lock
    lift_lock.acquire()
    lift_lock.release()
    
