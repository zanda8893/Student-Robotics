from conversions import *
from robot_obj import R
import drive,claw
from position import *

#number of spaces in previous list already used up
num_used_spaces = 0

#Gets location for cube depending on zone
def locationForCube():
    global num_used_spaces
    
    zone = R.zone
    pts = [Position(2.54,2.54),Position(1.84,2.54),
         Position(1.21,2.54),Position(2.54,1.93),
         Position(1.84,2),Position(2.54,1.2)]

    #Col is the number of cubes collected
    p = pts[num_used_spaces]

    #pc is the coords for the cube converted
    if zone == 0:
        pc = fromSimCoords(Position(-p.x,-p.y))
    if zone == 1:
        pc = fromSimCoords(Position(p.x,-p.y))
    if zone == 2:
        pc = fromSimCoords(Position(p.x,p.y))
    if zone == 3:
        pc = fromSimCoords(Position(-p.x,p.y))

    return pc

#Call this once a cube has been placed in the most recent location
def placeCube():
    global num_used_spaces
    num_used_spaces += 1

def dropCube():
    drive.driveRotateToAngle(bearingToZone(225))
    drive.driveStraightSync(40,1.5)
    claw.openClawSync()
    drive.driveStraightSync(-40,2)
    
