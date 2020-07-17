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
    markers.sort(key=lambda m:m.dist)
    if len(markers) == 0:
        return True #assume it is correct if no markers are visible
    if markers[0].info.marker_type != color:
        print("Ugh! A silver! I didn't ask for a _silver_!!!")
        print(markers[0].info.code)
        return False
    """
    for m in markers:
        if m.dist * 1000 < 300 and not color is None:
            if m.info.marker_type == MARKER_ARENA:
                continue
            if math.fabs(m.rot_y) > 20:
                continue
            if m.info.marker_type != color:
                print(f"Exiting {m.dist} {m.info.marker_type}")
                return False
    """
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

def lineUpToCubeCam(code,timeout=5,t0=R.time()):
    while R.time() < t0 + timeout:
        markers = R.see()
        for m in markers:
            if m.info.code == code:
                mk = m
                break
        if mk is None:
            return False

def approachCubeCam(code,timeout=10):
    min_dist = 140
    s_per_deg = 0.2
    mk = None
    print("approachCubeCam")
    t0 = R.time()

    while R.time() < t0 + timeout:
        markers = R.see()
        for m in markers:
            if m.info.code == code:
                mk = m
                break
        if mk is None:
            return False
        print("Dist:",mk.dist*1000)
        left = ultrasound.getDistance(0)
        right = ultrasound.getDistance(1)
        print("US",left,right)
        print("Switch",R.ruggeduinos[0].digital_read(2))
        if not left is None and not right is None:
            if min(left,right) < 60 or mk.dist < 0.145 or R.ruggeduinos[0].digital_read(2):
                #R.sleep(0.5)
                drive.driveStraight(0)
                return True
        if mk.rot_y > -0.5 and mk.rot_y < 0.5:
            print("Straight")
            drive.driveStraight(20)
        elif mk.rot_y > 0:
            print("Right")
            drive.drive(15,10,-1)
        elif mk.rot_y < 0:
            print("Left")
            drive.drive(10,15,-1)

    print("Timed out!")
    return False
