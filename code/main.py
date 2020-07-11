#Main loop

#~~ = Yet to be implimented/written

#Imports
import lift, claw, position, route_new, route, robot_obj,dropping, drive
from arena import A
from sr.robot import *

count = 0

while True:
    #Start
    #Look for markers
    count = count + 1
    if count == 1:
        robot_obj.R.sleep(2)
        markers = robot_obj.R.see()
        print("See")
        #Find robot position
        #Rp = Robot coordinates, Ra = Robot angle
        print("pos",markers)
        start_Rp,start_Ra = position.findPosition(markers)
        #Find nearest cube
        #colour either MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER
        #print("get near")
        print("test2")
        cube = A.getNearest(start_Rp,MARKER_TOKEN_GOLD)
        print(cube,"test")
        print("test1")
        route_new.getCube(cube)
        robot_obj.R.sleep(1)
        claw.openClaw()
        drive.driveStraightSync(-40,3)
        drive.driveRotateToAngle(0)
        A.removeCube(cube)

        print("Done")
        #End
    elif count== 2:
        route_new.getCube2()
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
