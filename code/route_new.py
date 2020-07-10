import drive, robot_obj, conversions


def convert(zone):
    if zone == 0:
         p = conversions.fromSimCoords(Position(-p.x,-p.y))
    if zone == 1:
         p = conversions.fromSimCoords(Position(p.x,-p.y))
    if zone == 2:
         p = conversions.fromSimCoords(Position(p.x,p.y))
    if zone == 3:
         p = conversions.fromSimCoords(Position(-p.x,p.y))


def getReturnCube(p):
    og_Rp = position.findPosition(robot_obj.R.see())
    if p == "test" or p == "test1" or p == "test2" or p == "test3":
        print("Rotate")
        drive.driveRotateToAngle(0)
        robot_obj.R.sleep(0.9)
        drive.driveStraightSync(50,2.35)
        drive.driveRotateAngle(90)
        drive.driveRotateToAngle(89)
        robot_obj.R.sleep(0.9)
        drive.driveStraightSync(60,2)
        if robot_obj.R.ruggeduinos[0].digital_read(4) == False:
            drive.driveStraightSync(-30,2)
            route.goToPointStraight(og_Rp)
            goToCube(p)
