import drive, robot_obj, conversions, orienting


def convert(zone):
    if zone == 0:
         p1 = conversions.fromSimCoords() #Position 1
         pC1 = conversions.fromSimCoords(Position(-p.x,-p.y)) #Position cube 1
    if zone == 1:
         p1 = conversions.fromSimCoords(Position(p.x,-p.y))
         pC1 = conversions.fromSimCoords(Position(-p.x,-p.y))
    if zone == 2:
         p1 = conversions.fromSimCoords(Position(p.x,p.y))
         pC1 = conversions.fromSimCoords(Position(-p.x,-p.y))
    if zone == 3:
         p1 = conversions.fromSimCoords(Position(-p.x,p.y))
         pC1 = conversions.fromSimCoords(Position(-p.x,-p.y))


def getCube(c):
    og_Rp = position.findPosition(robot_obj.R.see())
    if c == (code=32,color=MARKER_TOKEN_GOLD,p=Position(3775,3775),a=0) or p == (code=33,color=MARKER_TOKEN_GOLD,p=Position(3775,1975),a=0) or p == (code=34,color=MARKER_TOKEN_GOLD,p=Position(1975,1975),a=0) or p == (code=35,color=MARKER_TOKEN_GOLD,p=Position(1975,3775),a=0):
        print("Rotate")
        drive.driveRotateToAngle(0)
        robot_obj.R.sleep(0.9)
        drive.driveStraightSync(50,2.35)
        drive.driveRotateAngle(90)
        drive.driveRotateToAngle(89)
        robot_obj.R.sleep(0.9)
        drive.driveStraightSync(60,1.7)
        orienting.approachCube()
        if robot_obj.R.ruggeduinos[0].digital_read(4) == False:
            drive.driveStraightSync(-30,2)
            route.goToPointStraight(og_Rp)
            goToCube(p)
