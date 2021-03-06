from drive import *
from robot_obj import R
from sr.robot import *
import claw,lift
import orienting
import position
from position import *
import route


curr,a = position.getPosition()
p = orienting.getPre(curr,translateToZone(Position(1975,1975)),0)

route.goToPointStraight(curr,p)
driveRotateToAngle(position.anglePts(p,translateToZone(Position(1975,1975))))
orienting.approachCube()
claw.grabClawSync()
lift.raiseLiftSync()
driveRotateToAngle(position.bearingToZone(45))
driveStraightSync(-50,3)
