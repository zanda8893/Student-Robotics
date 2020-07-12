#Main loop

import  drive
from robot_obj import R
import lift, claw, position, route_new, route, robot_obj, dropping
from arena import A
from sr.robot import *

drive.driveRotateAngle(40)
drive.acceleration(100)
drive.driveStraight(100)
R.sleep(1.5)
drive.stopping()

count = 0

route_new.getNthCube(1)
route_new.getNthCube(0)
route_new.getNthCube(2)
route_new.getNthCube(1)
print("And on the seventh day...")
exit()


while True:
    #Start
    #Look for markers
    count = count +1
    if count == 1:
        markers = robot_obj.R.see()
        print("See")
        #Find robot position
        #Rp = Robot coordinates, Ra = Robot angle
        print("pos")
        start_Rp,start_Ra = position.findPosition(markers)
        #Find nearest cube
        #colour either MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER
        #print("get near")
        #print("test2")
        #cube = A.getNearest(start_Rp,MARKER_TOKEN_GOLD)
        #print(cube,"test")
        #print("test1")
        route_new.getCube2()
        robot_obj.R.sleep(0.5)
        claw.openClaw()
        drive.driveStraightSync(-40,3)
        #A.removeCube(cube)

        print("Done")
        #End
    elif count== 2:
        route_new.getCube()
        claw.openClaw()
        drive.driveStraightSync(-40,3)
        drive.driveRotateToAngle(0)
    elif count == 3:
        route_new.getCube3()
        claw.openClaw()
        drive.driveStraightSync(-40,3)
        drive.driveRotateAngle(180)
        drive.driveRotateToAngle(0)
    else:
        route_new.getCube4()
        claw.openClaw()
        drive.driveStraightSync(-40,3)
        drive.driveRotateAngle(180)
        drive.driveRotateToAngle(0)
