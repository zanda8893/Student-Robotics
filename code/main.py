#Main loop

import  drive
from robot_obj import R
import lift, claw, position, route_new, route, robot_obj, dropping
from arena import A
from sr.robot import *

route_new.getNthCube(0)
route_new.getNthCube(3)
route_new.getNthCube(4)
route_new.getNthCube(1)
route_new.getNthCube(2)

drive.kill()

print("And on the seventh day...")

exit()
