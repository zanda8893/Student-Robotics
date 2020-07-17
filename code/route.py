import position
from position import Position
import threading
from drive import *
from robot_obj import R
import deg
import math,random
from safediv import *
"""
Functions you're allowed to use:
goToPoint(p) - asynchronously go to p (represented by Position class)
goToPointSync(p) - same as goToPoint() but synchronous
arrived() - True if goToPoint() has arrived
wait() - wait for all routing to finish
         returns 1 for done and -1 for error
error() - true if an error has been encountered

Note: calling goToPoint() or goToPointSync() while a route is
already being followed will override the current route
"""

drive_power = 50

def offRoute(p,prev,nex,route=None):
    max_dev = 80
    if position.perpDist(prev,nex,p) <= max_dev:
        return False
    if route is None:
        return True
    for i in range(len(route)-1):
        p1 = route[i]
        p2 = route[i+1]
        if position.perpBetween(p1,p2,p) and position.perpDist(p1,p2,p) <= max_dev:
            return False
        if p1.dist(p) <= max_dev or p2.dist(p) <= max_dev:
            return False
    return True

def arrivedPt(p,prev,nex):
    arrived_tol = 10
    if position.paraDist(prev,nex,p) > prev.dist(nex) - arrived_tol:
        return True
    return False

def checkAngleSync(a,prev,nex,p=drive_power):
    max_angle_dev = 10
    ta = position.anglePts(prev,nex)
    diff = position.getAngleDiff(ta,a)
    if math.fabs(diff) > max_angle_dev:
        driveRotateToAngle(ta)
    driveStraight(p)
        
#0 for success
def goToPointStraight(prev,nex,timeout=15,p=drive_power):
    
    lastPt = prev
    init = prev
    t0 = R.time()
    pos_ts = R.time()
    to_cnt = 0
    while True:
        if R.time() > t0 + timeout:
            print("Timeout1!")
            driveStraightSync(-30,2)
            return 1
        m = R.see()
        cp = position.findPosition(m)
        if cp is None:
            if R.time() > pos_ts + 3:
                print("Timeout2!")
                if to_cnt < 3:
                    driveStraightSync(-30,2)
                else:
                    driveStraightSync(30,2)
                    to_cnt = 0
                pos_ts = R.time()
                t0 += 4
                to_cnt += 1
            continue
        
        if init is None:
            init = cp[0]
            
        if arrivedPt(cp[0],init,nex):
            driveStraight(0)
            return 0
        
        if cp[0].dist(nex) > 500 or lastPt is None:
            lastPt = cp[0]
            
        if lastPt is None:
            continue
        
        checkAngleSync(cp[1],lastPt,nex,p)
        pos_ts = R.time()
        
