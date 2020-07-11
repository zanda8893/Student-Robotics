import drive, robot_obj, conversions, orienting, position, claw, route, lift
from position import Position

#xh = 100
#yh = 750
ah = 225
posh = Position(100,750)

#x = 1975
#y = 700
a = 90
pos = Position(1975,700)

#x1 = 1975
#y1 = 3300
ah2 = 245
pos1 = Position(1975,3300)

#x2 = 3300
#y2 = 1975
ah3 = 210
pos2 = Position(3300,1975)

#x3 = 700
#y3 = 1850
pos3 = Position(700,1850)

#x4 = 3800
#y4 = 1000
ah4 = 165
pos4 = Position(3800,1000)

if robot_obj.R.zone != 0:
     pos = position.translateToZone(pos)
     a = position.bearingToZone(a)
     posh = position.translateToZone(posh)
     ah = position.bearingToZone(ah)
     pos1 = position.translateToZone(pos1)
     ah2 = position.bearingToZone(ah2)
     pos2 = position.translateToZone(pos2)
     ah3 = position.bearingToZone(ah3)
     pos3 = position.translateToZone(pos3)
     pos4 = position.translateToZone(pos4)


def getCube(c):
    og_Rp = position.findPosition(robot_obj.R.see())
    if og_Rp is None:
         return False
    if c.code >= 32 and c.code <= 35:
        #print("Rotate")
        #print(type(og_Rp[0]),type(pos))
        route.goToPointStraight(og_Rp[0],pos)
        drive.driveRotateAngle(a)
        drive.driveRotateToAngle(a)
        robot_obj.R.sleep(0.5)
        route.goToPointStraight(og_Rp[0],pos+Position(0,750).rotate(-90*robot_obj.R.zone))
        orienting.approachCube()
        claw.grabClawSync()
        drive.driveRotateToAngle(ah)
        drive.driveStraightSync(40,5)
        """
        if robot_obj.R.ruggeduinos[0].digital_read(5) == False:
            print("Get cube failed")
            drive.driveStraightSync(-30,2)
            Rp = position.findPosition(robot_obj.R.see())
            route.goToPointStraight(Rp[0],og_Rp)
            getCube(c)
        """

def getCube2():
    robot_obj.R.sleep(1)
    og_Rp = position.findPosition(robot_obj.R.see())
    if og_Rp is None:
         return False
    route.goToPointStraight(og_Rp[0],pos)
    og_Rp = position.findPosition(robot_obj.R.see())
    if og_Rp is None:
         return False
    route.goToPointStraight(og_Rp[0],pos1)
    drive.driveRotateToAngle(90)
    orienting.approachCube()
    claw.grabClawSync()
    drive.driveRotateToAngle(ah2)
    drive.driveStraightSync(40,8)

def getCube3():
    robot_obj.R.sleep(1)
    og_Rp = position.findPosition(robot_obj.R.see())
    if og_Rp is None:
         return False
    route.goToPointStraight(og_Rp[0],pos3)
    og_Rp = position.findPosition(robot_obj.R.see())
    if og_Rp is None:
         return False
    route.goToPointStraight(og_Rp[0],pos2)
    orienting.approachCube()
    claw.grabClawSync()
    drive.driveRotateToAngle(ah3)
    drive.driveStraightSync(30,13)


def getCube4():
    robot_obj.R.sleep(1)
    og_Rp = position.findPosition(robot_obj.R.see())
    if og_Rp is None:
         return False
    route.goToPointStraight(og_Rp[0],pos3)
    og_Rp = position.findPosition(robot_obj.R.see())
    if og_Rp is None:
         return False
    route.goToPointStraight(og_Rp[0],pos2)
    drive.driveRotateToAngle(0)
    drive.driveStraightSync(60,2)
    og_Rp = position.findPosition(robot_obj.R.see())
    if og_Rp is None:
         return False
    route.goToPointStraight(og_Rp[0],position.Position(pos4.x,pos1.y))
    drive.driveRotateToAngle(90)
    orienting.approachCube()
    claw.grabClawSync()
    drive.driveStraight(40,3)
    og_Rp = position.findPosition(robot_obj.R.see())
    if og_Rp is None:
         return False
    route.goToPointStraight(og_Rp[0],pos4)
    drive.driveRotateToAngle(ah4)
    drive.driveStraightSync(40,10)

