import drive, robot_obj, orienting
import claw, route, lift,cube,dropping
from position import *

"""
Order:
Nearest cube, far left, far right, mid left, mid right
"""
prepositions = [[translateToZone(Position(1300,1975))],
               [translateToZone(Position(550,3775)),   
               translateToZone(Position(1350,3775))],
               [translateToZone(Position(3775,550)),   
                translateToZone(Position(3775,1350))],
               [translateToZone(Position(1700,1300)),  
                translateToZone(Position(1700,2875)),
                translateToZone(Position(1300,2875))],
               [translateToZone(Position(1300,1700)),  
                translateToZone(Position(2875,1700)),
                translateToZone(Position(2875,1300))]]
#angles before approachCube
preangles = [bearingToZone(0),
             bearingToZone(0),
             bearingToZone(90),
             bearingToZone(0),
             bearingToZone(90)]
#sometimes the camera can't detect its orientation, meaning
#it can't properly go to the preangle
#anglehint hints at a likely angle that the robot will be at on
#arriving to the preposition
anglehint = [bearingToZone(45),
             bearingToZone(0),
             bearingToZone(270),
             bearingToZone(0),
             bearingToZone(270)
             ]
#angle to turn to after grabbing
#for platform cubes: reverses first, rotates _by_ angle not _to_ angle
afterangles = [bearingToZone(0),
               bearingToZone(135),
               bearingToZone(315),
               -90,
               90]
#lists of points to get home
homepositions = [[translateToZone(Position(1500,1500))],
                 [translateToZone(Position(795,3145)),
                  translateToZone(Position(1500,1500))],
                 [translateToZone(Position(3145,795)),
                  translateToZone(Position(1500,1500))],
                 [translateToZone(Position(1975,1975)),
                  translateToZone(Position(1500,1500))],
                 [translateToZone(Position(1975,1975)),
                  translateToZone(Position(1500,1500))]]
cubepositions = [translateToZone(Position(1975,1975)),
                 translateToZone(Position(1975,3775)),
                 translateToZone(Position(3775,1975)),
                 translateToZone(Position(2455,2875)),
                 translateToZone(Position(2875,2455))]

cubes_retrieved = [False,False,False,False,False]

def wiggleClaw():
     print("And breath in...")
     lift.raiseLift()
     claw.grabClawSync()
     claw.openClaw()
     print("...and breath out")
     R.sleep(0.6)
     lift.lowerLiftSync()
     claw.waitOnClaw()

def goToCube(n):
     res = False
     for p in prepositions[n]:
          res = route.goToPointStraight(None,p)
          if res > 0:
               print("goToCube failed!")
               return False

     drive.driveRotateToAngle(preangles[n],anglehint[n])
     
     mks = R.see()
     p = findPosition(mks)
     pre,c = None,None
     for mk in mks:
          if mk.code == cube.getNthCode(n):
               c = Cube(mk)
               pre = orienting.getPre(p,c.p,c.a)
               break
     if pre is None or c is None:
          return False

     
     return True

def goToCubePlat(n):
     res = False
     for p in prepositions[n]:
          res = route.goToPointStraight(None,p)
          if res > 0:
               print("goToCube failed!")
               return False

     drive.driveRotateToAngle(preangles[n],anglehint[n])

     return True

def returnHome(n,success=True):
     for p in homepositions[n]:
          route.goToPointStraight(None,p)
     if success:
          dropping.dropCube()
     
cnt = 0
def getNthCubeGround(n):
     global cnt

     res = goToCube(n)
     if not res:
          returnHome(n,False)
          return False
          
     if cnt >= 1:
          wiggleClaw()

     res = orienting.approachCube()
     if not res:
          returnHome(n,False)
          return False
          
     claw.grabClawSync()
     drive.driveRotateToAngle(afterangles[n])
     returnHome(n)
     cnt += 1
     
def getNthCubePlatform(n):
     res = goToCube(n)
     if not res:
          returnHome(n,False)
          return False

     claw.openClawSync()
     lift.raiseLiftSync()

     res = orienting.approachCubeCam(cube.getNthCode(n))
     if not res:
          returnHome(n,False)
          return False

     claw.grabClawSync()
     grabbed = R.ruggeduinos[0].digital_read(5)
     if not grabbed:
          returnHome(n,False)
          return False
     drive.driveStraightSync(-30,1.5)
     lift.lowerLiftSync()
     claw.openClawSync()
     drive.driveStraightSync(20,1)
     #lift.lowerLiftSync()
     claw.grabClawSync()
     """
     if grabbed and not R.ruggeduinos[0].digital_read(5):
          claw.openClawSync()
          drive.driveStraightSync(-30,1)
          lift.lowerLiftSync()
          
          res = orienting.approachCube()
          if not res:
               returnHome(n,False)
               return False
          drive.driveStraightSync(-30,1)
     """
     drive.driveRotateAngle(afterangles[n])
     returnHome(n)

def getNthCube(n):
     p = cubepositions[n]
     if p.onPlatform():
          getNthCubePlatform(n)
     else:
          getNthCubeGround(n)

def selectCube():
     #get current position
     cp = position.getPosition()
     if cp is None:
          for i in range(5):
               if not cubes_retrieved[i]:
                    return i
          return None
     chances = [0.9,0.8,0.8,0.5,0.5] #probability of being successful
     ang_stat = 0
     for i in (0,1,3,2,4):
          #rotate to position
          if i == 0:
               drive.driveRotateToAngle(bearingToZone(45),bearingToZone(0))
          if i == 1:
               drive.driveRotateToAngle(bearingToZone(70),bearingToZone(45))
          if i == 2:
               drive.driveRotateToAngle(bearingToZone(20),bearingToZone(70))

          #ignore retrieved cubes
          if cubes_retrieved[i]:
               chances[i] = 0
               continue
          
          x,d = cube.nthCubePositionCorrect(i,cubepositions[i])
          if x == 0:
               chances[i] *= 0.5
          if x == -1:
               chances[i] /= (1 + d*0.0008)

     #get biggest chance
     high = 0
     for i in range(5):
          if chances[i] > chances[high]:
               high = i

     return i


