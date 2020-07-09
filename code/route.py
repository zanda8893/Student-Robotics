import position
import arena
from arena import A
from tree import Tree
import threading
from drive import *
from robot_obj import R
import deg
import math
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

drive_power = 60

def tryRoute(pts):
    if len(pts) < 2:
        return False
    for i in range(pts-1):
        p1 = pts[i]
        p2 = ptr[i + 2]
        if not arena.A.pathClear(p1,p2):
            return False
    return True

#looks for potential child points that could be on route
def exploreBranch(tree,node,end):
    pos = tree.getData(node)
    if arena.A.pathClear(pos,end):
        n = tree.addNode(node,end)
        return n

    #potential points that the route might go through
    pts = arena.A.getRoutePts(tree.getData(node),target=end,lim=5)
    #print("Route pts",pts)
    for pt in pts:
        tree.addNode(node,pt)

    return -1

def findRoute(start,end):
    tree = Tree(start)
    max_depth = 10
    for i in range(max_depth):
        leaves = tree.leaves()
        for l in leaves:
            res = exploreBranch(tree,l,end)
            if res >= 0:
                npath = tree.pathToNode(res)
                path = [tree.getData(n) for n in npath]
                return path
    return None

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
    arrived_tol = 40
    if position.paraDist(prev,nex,p) > prev.dist(nex) - arrived_tol:
        return True
    return False

route_tid = 0
route_done = 0 #0=not done,-1=error,1=done
route_lock = threading.Lock()
override_cond = threading.Condition(route_lock)
done_cond = threading.Condition(route_lock)

def getAngleDiff(a,ta):
    diff = (ta - a)
    if diff < -180:
        diff += 360
    if diff > 180:
        diff -= 360
    return diff

def rotateFromDiff(diff):
    global override_cond
    diff = getAngleDiff(0,diff)
    s_per_deg = 0.05
    rotate_speed = 20
    if diff < 0:
        rotate_speed *= -1
    t = math.fabs(diff) * s_per_deg
    driveRotate(rotate_speed,t)
    t0 = R.time()
    while R.time() < t0 + t:
        override_cond.wait(timeout=t*0.8)
    

def checkAngleSync(a,prev,nex):
    global drive_power,override_cond,route_tid
    max_angle_dev = 10
    dev_low_wm = 6
    ta = deg.atan(safeDiv(nex.y-prev.y,nex.x-prev.x))
    diff = getAngleDiff(a,ta)
    if math.fabs(diff) > max_angle_dev:
        print("Wonky!")
        while math.fabs(diff) > dev_low_wm:
            rotateFromDiff(diff)
            if route_tid != threading.get_ident():
                return
            m = R.see()
            A.addMarkers(m)
            cp = position.findPosition(m)
            if cp is None:
                continue
            a = cp[1]
            diff = getAngleDiff(a,ta)
    driveStraight(drive_power)

#0 for success, 1 for needs reroute
def goToPointStraight(prev,nex):
    while True:
        m = R.see()
        A.addMarkers(m)
        cp = position.findPosition(m)
        if cp is None:
            continue
        if arrivedPt(cp[0],prev,nex):
            driveStraight(0)
            return 0
        if offRoute(cp[0],prev,nex):
            driveStraight(0)
            return 1
        checkAngleSync(cp[1],prev,nex)
   
#returns route
def beginRouting(p):
    global route_lock,route_tid,override_cond
    global route_done,done_cond
    route_lock.acquire()

    route_done = 0
    route_tid = threading.get_ident()
    override_cond.notify_all()
    driveStraight(0)

    m = R.see()
    A.addMarkers(m)
    cp = position.findPosition(m)
    if cp is None:
        route_done = -1
        done_cond.notify_all()
        route_lock.release()
        return None

    start,ang = cp[0],cp[1]
    curr = start

    route = findRoute(start,p)
    if route is None or len(route) < 2:
        route_done = -1
        done_cond.notify_all()
        route_lock.release()
        return False
    
def goToPointSync(p):
    

    i = 0
    prev = route[i]
    nex = route[i+1]

    driveStraight(drive_power)

    while True:        
        if offRoute(curr,prev,nex,route):
            print("Off route!")
            driveSraight(0)
            route = findRoute(start,p)
            i = 0

        if arrivedPt(curr,prev,nex):
            print("Arrived!")
            i += 1

        if len(route) <= i+1:
            print("Finished!")
            break

        prev,nex = route[i],route[i+1]
        checkAngleSync(ang,prev,nex)

        override_cond.wait(timeout=0.1) #opportunity for override
        
        if route_tid != threading.get_ident():
            route_lock.release()
            return False

        m = R.see()
        curr,ang = position.findPosition(m)
        A.addMarkers(m)
        

    route_done = 1
    done_cond.notify_all()
    route_lock.release()
    return True

def goToPoint(p):
    thr = threading.Thread(target=goToPointSync,args=(p))
    thr.start()

def wait():
    global done_cond,route_done
    done_cond.acquire()
    while route_done == 0:
        done_cond.wait()
    ret = route_done
    done_cond.release()
    return ret

def arrived():
    global done_cond,route_done
    done_cond.acquire()
    ret = route_done==1
    done_cond.release()
    return ret

def error():
    global done_cond,route_done
    done_cond.acquire()
    ret = route_done==-1
    done_cond.release()
    return ret
