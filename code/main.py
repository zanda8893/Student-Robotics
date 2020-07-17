#Main loop

import  drive
import position, route_new

route_new.getNthCube(0)
route_new.getNthCube(1)
route_new.getNthCube(2)
route_new.getNthCube(3)
drive.driveRotateToAngle(position.bearingToZone(225))
drive.driveStraightSync(-50,100)
#route_new.getNthCube(4)

drive.kill()

print("And on the seventh day...")

exit()
