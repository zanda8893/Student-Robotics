from drive import *
from robot_obj import R

#Tests done

def timestamp(s):
    print(s + " at {0}".format(R.time()))

init()

timestamp("A")
driveStraight(50,3)
timestamp("B")
print(driveDone())
R.sleep(0.5)
driveStraight(-50,1)
driveWait()
timestamp("C")

timestamp("D")
driveRotate(50,1)
timestamp("E")
print(driveDone())
driveWait()
timestamp("F")

kill()
