from drive import *
from robot_obj import R
from sr.robot import *
import claw

driveRotateAngle(45)
driveStraightSync(60,2)
driveRotateAngle(-90)
driveStraightSync(60,2)
claw.grabClawSync()
driveRotateAngle(45)
driveStraightSync(-60,3)
