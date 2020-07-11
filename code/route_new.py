import drive, robot_obj, conversions, orienting, position, claw, route

xh = 100
yh = 750

x = 1900
y = 1400
a = 90

x1 = 2350
y1 = 4425

if robot_obj.R.zone != 0:
     position.translateToZone(position.Position(x,y),robot_obj.R.zone)


def getCube(c):
    og_Rp = position.findPosition(robot_obj.R.see())
    if c.code >= 32 and c.code <= 35:
        print("Rotate")
        route.goToPointStraight(og_Rp[0],position.Position(x,y))
        drive.driveRotateAngle(a)
        drive.driveRotateToAngle(a)
        robot_obj.R.sleep(0.9)
        orienting.approachCube()
        claw.grabClawSync()
        Rp = position.findPosition(robot_obj.R.see())
        route.goToPointStraight(Rp[0],position.Position(xh,yh))
        if robot_obj.R.ruggeduinos[0].digital_read(5) == False:
            drive.driveStraightSync(-30,2)
            Rp = position.findPosition(robot_obj.R.see())
            route.goToPointStraight(Rp[0],og_Rp)
            getCube(c)
    else:
        route.goToPointStraight(og_Rp[0],position.Position(x1,y1))
