import drive, robot_obj, conversions, orienting, position, claw, route, lift

xh = 100
yh = 750
ah = 225

x = 1850
y = 700
a = 90

x1 = 2000
y1 = 3300
ah2 = 245

x2 = 3300
y2 = 2000
ah3 = 210

x3 = 700
y3 = 1850

x4 = 3400


if robot_obj.R.zone != 0:
     x,y = position.translateToZone(position.Position(x,y),robot_obj.R.zone)
     a = bearingToZone(a)
     xh,yh = position.translateToZone(position.Position(xh,yh),robot_obj.R.zone)
     ah = bearingToZone(ah)
     x1, y1 = position.translateToZone(position.Position(x1,y1),robot_obj.R.zone)
     ah2 = bearingToZone(ah2)
     x2, y2 = position.translateToZone(position.Position(x2,y2),robot_obj.R.zone)
     ah3 = bearingToZone(ah3)
     x3, y3 = position.translateToZone(position.Position(x3,y3),robot_obj.R.zone)
     x4, y4 = position.translateToZone(position.Position(x4,y4),robot_obj.R.zone)


def getCube(c):
    og_Rp = position.findPosition(robot_obj.R.see())
    if c.code >= 32 and c.code <= 35:
        print("Rotate")
        route.goToPointStraight(og_Rp[0],position.Position(x,y))
        drive.driveRotateAngle(a)
        drive.driveRotateToAngle(a)
        robot_obj.R.sleep(0.9)
        route.goToPointStraight(og_Rp[0],position.Position(x,y+650))
        orienting.approachCube()
        claw.grabClawSync()
        drive.driveRotateToAngle(ah)
        drive.driveStraightSync(40,10)
        if robot_obj.R.ruggeduinos[0].digital_read(5) == False:
            print("Get cube failed")
            drive.driveStraightSync(-30,2)
            Rp = position.findPosition(robot_obj.R.see())
            route.goToPointStraight(Rp[0],og_Rp)
            getCube(c)

def getCube2():
    robot_obj.R.sleep(1)
    og_Rp = position.findPosition(robot_obj.R.see())
    route.goToPointStraight(og_Rp[0],position.Position(x,y))
    og_Rp = position.findPosition(robot_obj.R.see())
    route.goToPointStraight(og_Rp[0],position.Position(x1,y1))
    drive.driveRotateToAngle(90)
    orienting.approachCube()
    claw.grabClawSync()
    drive.driveRotateToAngle(ah2)
    drive.driveStraightSync(40,10)

def getCube3():
    robot_obj.R.sleep(1)
    og_Rp = position.findPosition(robot_obj.R.see())
    route.goToPointStraight(og_Rp[0],position.Position(x3,y3))
    og_Rp = position.findPosition(robot_obj.R.see())
    route.goToPointStraight(og_Rp[0],position.Position(x2,y2))
    orienting.approachCube()
    claw.grabClawSync()
    drive.driveRotateToAngle(ah3)
    drive.driveStraightSync(30,13)

def getCube4():
    robot_obj.R.sleep(1)
    og_Rp = position.findPosition(robot_obj.R.see())
    route.goToPointStraight(og_Rp[0],position.Position(x3,y3))
    og_Rp = position.findPosition(robot_obj.R.see())
    route.goToPointStraight(og_Rp[0],position.Position(x2,y2))
    drive.driveStraightSync(60,2)
    og_Rp = position.findPosition(robot_obj.R.see())
    route.goToPointStraight(og_Rp[0],position.Position(x4,y1))
    orienting.approachCube()
    claw.grabClawSync()
    og_Rp = position.findPosition(robot_obj.R.see())
    route.goToPointStraight(og_Rp[0],position.Position(x2,y2))
    drive.driveRotateToAngle(ah3)
    drive.driveStraightSync(40,10)
