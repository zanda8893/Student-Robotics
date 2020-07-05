import robot_obj
import time
import threading

"""
Functions you are allowed to use:
raiseLift() - raises lift asynchronously
lowerLift() - lowers lift asynchronously
raiseLiftSync() - raises lift synchronously
lowerLiftSync() - lowers lift synchronously
liftIsRaised() - True if lift is raised, false otherwise
                 Waits for the lift to finish before returning
liftIsFinished() - True if the lift has finished moving, False otherwise
waitOnLift() - wait until the lift has finished moving
"""

lifting_time = 0.3

lift_lock = threading.Lock()

lift_is_raised = 0

#set lift motor power
def setLift(x):
    robot_obj.R.motors[1].m0.power = x

#synchronously raise lift
def raiseLiftSync():
    global lift_lock,lift_is_raised
    lift_lock.acquire()
    if lift_is_raised:
        lift_lock.release()
        return
    lift_is_raised = True
    setLift(-100)
    robot_obj.R.sleep(lifting_time)
    setLift(0)
    lift_lock.release()    

#asynchronously raise lift
def raiseLift():
    thr = threading.Thread(target=raiseLiftSync)
    thr.start()

#synchronously lower lift
def lowerLiftSync():
    global lift_lock,lift_is_raised
    lift_lock.acquire()
    if not lift_is_raised:
        lift_lock.release()
        return
    lift_is_raised = False
    setLift(100)
    robot_obj.R.sleep(lifting_time)
    setLift(0)
    lift_lock.release()

#asynchronously lower lift
def lowerLift():
    thr = threading.Thread(target=lowerLiftSync)
    thr.start()

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
    
