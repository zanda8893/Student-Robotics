import deg
import route
import position
from position import Position
import arena
import math
import ultrasound
import drive
from robot_obj import R
from sr.robot import *

position_distance = 150
preposition_distance = 400 #distance to travel from pre to pos
collision_distance = 280
platform_stop_dist = 10

#curr=current position,pos=cube position,ang=cube angle (either 0 or 45)
#curr can be None, in which case a position is found automatically
def getPre(curr,pos,ang):
    global position_distance,preposition_distance,collision_distance
    poss = []
    d = position_distance + preposition_distance
    for a in (0,90,180,270):
        x = d * deg.sin(ang + a)
        y = d * deg.cos(ang + a)
        p = Position(x,y) + pos
        #if arena.A.ptClear(p,collision_distance):
        poss.append(p)

    if curr is None:
        cp = position.getPosition()
        if cp is None:
            curr = position.translateToZone(Position(0,0))
        else:
            curr = cp[0]

    poss.sort(key=lambda pt:pt.dist(curr))
    return poss[0]

def checkColor(color):
    markers = R.see()
    for m in markers:
        if m.dist * 1000 < 300 and not color is None:
            if m.info.marker_type == MARKER_ARENA:
                continue
            if math.fabs(m.rot_y) > 20:
                continue
            if m.info.marker_type != color:
                print(f"Exiting {m.dist} {m.info.marker_type}")
                return False
    return True

#true on success
def approachCube(color=MARKER_TOKEN_GOLD,timeout=5):
    min_dist = 80
    t0 = R.time()
    if not checkColor(color):
        return False
    i=1
    while R.time() < t0 + timeout:
        i += 1
        if not checkColor(color):
            drive.driveStraightSync(-20,2)
            return False
        leftd = ultrasound.getDistance(0)
        rightd = ultrasound.getDistance(1)
        print(f"Left {leftd} Right {rightd}")

        m = None
        if leftd is None and rightd is None:
            print("Straight")
            drive.driveStraight(20)
        elif leftd is None:
            print("Rotating CW")
            drive.drive(20,10,-1)
            m = rightd
        elif rightd is None:
            print("Rotating CCW")
            drive.drive(10,20,-1)
            m = leftd
        else:
            print("Straight slowly")
            drive.driveStraight(15)
            m = leftd

        if not m is None and m < min_dist:
            print("Stopping")
            drive.driveStraight(0)
            return True


    return False

def approachCubeCam(timeout=5):#
    cube = None
    closest = 1500
    foundClose = False
    centrePolarMatch = False
    print("approachCubeCam")
    t0 = R.time()
    while R.time() < t0 + timeout:
        markers = R.see()
        for m in markers:
            if foundClose == False:
                print("Check Marker")
                if m.dist * 1000 < closest and m.info.marker_type ==MARKER_TOKEN_GOLD:
                    print("Closest found")
                    closest = m.dist * 1000
                    code = m.info.code
                    foundClose = True
                    cube = m
                else:
                    print("Marker doesn't fit requirements. Distance:",m.dist * 1000,"Type:",m.info.marker_type)
            elif m.info.code == code:
                cube = m
        if cube.centre.polar.rot_y > -10 and cube.centre.polar.rot_y < 10:
            centrePolarMatch == True
        elif cube.centre.polar.rot_y > 0:
            print("Right",cube.centre.polar.rot_y)
            drive.drive(20,10,-1)
        elif cube.centre.polar.rot_y < 0:
            print("Left",cube.centre.polar.rot_y)
            drive.drive(10,20,-1)
        if centrePolarMatch == True:
            if cube.orientation.rot_y > -3 and cube.orientation.rot_y < 3:
                print("Stright")
                drive.driveStraight(20)
            elif cube.orientation.rot_y > 0:
                print("Right")
                drive.drive(20,10,-1)
            elif cube.orientation.rot_y < 0:
                print("Left")
                drive.drive(10,20,-1)
