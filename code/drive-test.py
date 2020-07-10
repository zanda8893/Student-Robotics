from drive import *
from robot_obj import R

#Tests done

def timestamp(s):
    print(s + " at {0}".format(R.time()))

#driveStraightSync(60,0.5)
driveRotateAngle(30)
    
kill()
