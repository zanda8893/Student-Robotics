import drive, robot_obj, conversions, orienting, position, claw, route, lift
from position import *

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

#positions before approachCube
prepositions = [[translateToZone(Position(1300,1975))],
                [translateToZone(Position(1200,3750))],
                [translateToZone(Position(3300,1975))]]
#angles before approachCube
preangles = [bearingToZone(0),bearingToZone(0),bearingToZone(0)]
#angle to turn to after grabbing
afterangles = [bearingToZone(0),bearingToZone(90),bearingToZone(-45)]
#lists of points to get home
homepositions = [[translateToZone(Position(1000,1400))],
                 [translateToZone(Position(1100,2875)),
                  translateToZone(Position(1200,1200))],
                 [translateToZone(Position(3775,1000)),
                  translateToZone(Position(800,1600))]]
cubepositions = [translateToZone(Position(1975,1975)),
                 translateToZone(Position(1975,3775)),
                 translateToZone(Position(3775,1975))]

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

def wiggleClaw():
     print("And breath in...")
     lift.raiseLift()
     claw.grabClawSync()
     claw.openClaw()
     print("...and breath out")
     R.sleep(0.6)
     lift.lowerLiftSync()
     claw.waitOnClaw()
     
     
def getNthCube(n):
     for p in prepositions[n]:
          route.goToPointStraight(None,p)
     cp = getPosition()
     
     a = preangles[n]
                                   
     drive.driveRotateToAngle(a)

     wiggleClaw()
     
     orienting.approachCube()
     claw.grabClawSync()
     drive.driveRotateToAngle(afterangles[n])
     for p in homepositions[n]:
          route.goToPointStraight(None,p)
     claw.openClawSync()
     drive.driveStraight(-40,2)
     
def getCube():
    route.goToPointStraight(None,pos)
    drive.driveRotateAngle(90)
    drive.driveRotateToAngle(a)
    robot_obj.R.sleep(0.5)
    
    orienting.approachCube()
    claw.grabClawSync()
    drive.driveRotateToAngle(ah)
    drive.driveStraightSync(40,3)
"""
        if robot_obj.R.ruggeduinos[0].digital_read(5) == False:
            print("Get cube failed")
            drive.driveStraightSync(-30,2)
            Rp = position.findPosition(robot_obj.R.see())
            route.goToPointStraight(Rp[0],og_Rp)
            getCube(c)
        """

def getCube2():
    print("ooop")
    #robot_obj.R.sleep(1)
    lift.raiseLiftSync()
    lift.lowerLiftSync()
    route.goToPointStraight(None,translateToZone(Position(1335,3775)))
    drive.driveRotateToAngle(position.bearingToZone(0))
    orienting.approachCube()
    claw.grabClawSync()
    drive.driveRotateToAngle(bearingToZone(180))
    route.goToPointStraight(None,translateToZone(Position(1335,3775)))
    print("A")
    drive.driveRotateToAngle(bearingToZone(270))
    drive.driveStraightSync(40,5)

def getCube3():
    robot_obj.R.sleep(1)
    route.goToPointStraight(None,translateToZone(Position(1975,1950)))
    route.goToPointStraight(None,pos2)
    orienting.approachCube()
    claw.grabClawSync()
    drive.driveStraightSync(30,2)
    route.goToPointStraight(None,translateToZone(Position(1975,1975)))
    drive.driveRotateToAngle(bearingToZone(225))
    drive.driveStraightSync(40,3)

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
    drive.driveRotateToAngle(position.bearingToZone(90))
    orienting.approachCube()
    claw.grabClawSync()
    drive.driveStraight(40,3)
    og_Rp = position.findPosition(robot_obj.R.see())
    if og_Rp is None:
         return False
    route.goToPointStraight(og_Rp[0],pos4)
    drive.driveRotateToAngle(ah4)
    drive.driveStraightSync(40,10)
