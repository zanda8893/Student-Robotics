import drive
from robot_obj import *
import route_new,route
from position import *

route_new.getNthCube(0)
route.goToPointStraight(None,Position(1800,1800))
#drive.driveStraightSync(40,2)
#drive.driveRotateAngle(180)
drive.driveRotateToAngle(225)
drive.driveStraight(-60)
