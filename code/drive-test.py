from drive import *
from robot_obj import R

#Tests done

def timestamp(s):
    print(s + " at {0}".format(R.time()))

#driveStraightSync(30,1.5)
driveRotateToAngle(90)
    
kill()
