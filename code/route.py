import position
from position import Position
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

drive_power = 40

def tryRoute(pts):
    if len(pts) < 2:
        return False
    for i in range(pts-1):
        p1 = pts[i]
        p2 = pts[i + 1]
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
    pts = arena.A.getRoutePts(tree.getData(node),target=end,lim=10)
    for pt in pts:
        tree.addNode(node,pt)

    return -1


initial_tree = Tree(Position(1425,1425))
level_1_pts = [Position(1155,3225),Position(1585,2345),
               Position(3225,1155),Position(2345,1585)]

def findRoute(start,end):
    l = initial_tree.getAllNodes()
    l.sort(key=lambda n:initial_tree.getData(n).dist(start))
    snode = l[0]
    l.sort(key=lambda n:initial_tree.getData(n).dist(end))
    enode = l[0]
    route = [start]
    route += initial_tree.dataBetween(snode,enode)
    route.append(end)
    return route

def initTree():
    global initial_tree
    c = lambda p:position.translateToZone(p,R.zone)
    n1 = initial_tree.addNode(0,c(Position(1155,3225)))
    n2 = initial_tree.addNode(n1,c(Position(1935,3295)))
    n1 = initial_tree.addNode(0,c(Position(1585,2345)))

    n1 = initial_tree.addNode(0,c(Position(3225,1155)))
    n2 = initial_tree.addNode(n1,c(Position(3295,1935)))
    n1 = initial_tree.addNode(0,c(Position(2345,1585)))

initTree()

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

route_tid = 0
route_done = 0 #0=not done,-1=error,1=done
route_lock = threading.Lock()
override_cond = threading.Condition(route_lock)
done_cond = threading.Condition(route_lock)


def checkAngleSync(a,prev,nex):
    global drive_power
    max_angle_dev = 10
    ta = position.anglePts(prev,nex)
    diff = position.getAngleDiff(ta,a)
    if math.fabs(diff) > max_angle_dev:
        driveRotateToAngle(ta)
    driveStraight(drive_power)
#0 for success
def goToPointStraight(prev,nex,timeout=15):
    #print("Going to point",nex)
    lastPt = prev
    init = prev
    t0 = R.time()
    pos_ts = R.time()
    while True:
        if R.time() > t0 + timeout:
            print("Timeout1!")
            driveStraightSync(-30,3)
            return 1
        #t0 = R.time()
        m = R.see()
        #A.addMarkers(m)
        cp = position.findPosition(m)
        if cp is None:
            if R.time() > pos_ts + 3:
                print("Timeout2!")
                driveStraightSync(-30,3)
                pos_ts = R.time()
            continue
        if init is None:
            init = cp[0]
        #print("Current position {0}".format(cp))
        if arrivedPt(cp[0],init,nex):
            driveStraight(0)
            return 0
        if cp[0].dist(nex) > 500 or lastPt is None:
            lastPt = cp[0]
        if lastPt is None:
            continue
        checkAngleSync(cp[1],lastPt,nex)
        pos_ts = R.time()
        
#returns route
def beginRouting(p):
    global route_lock,route_tid,override_cond
    global route_done,done_cond
    route_lock.acquire()

    #init
    route_done = 0
    route_tid = threading.get_ident()
    override_cond.notify_all()
    driveStraight(0)

    #get position
    m = R.see()
    #A.addMarkers(m)
    cp = position.findPosition(m)
    if cp is None:
        route_done = -1
        done_cond.notify_all()
        route_lock.release()
        return None,curr,ang

    start,ang = cp[0],cp[1]
    curr = start

    route = findRoute(start,p)
    if route is None or len(route) < 2:
        route_done = -1
        done_cond.notify_all()
        route_lock.release()
        return None,curr,ang

    return route,curr,ang

def rotateUntilPos():
    curr = None
    while curr is None:
        m = R.see()
        A.addMarkers(m)
        cp = position.findPosition(m)
        if cp is None:
            driveRotate(20)
            continue
        curr,ang = cp[0],cp[1]
    driveStraight(0)
    return curr,ang

def goToPointSync(p):
    route,curr,ang = beginRouting(p)
    if route is None:
        print("Unable to find route!")
        return False

    i = 0
    prev = route[i]
    nex = route[i+1]

    ret = False
    #driveStraight(drive_power)
    checkAngleSync(ang,prev,nex)

    while True:
        res,curr,ang = goToPointStraight(prev,nex)
        if res == 1:
            curr,ang = rotateUntilPos()
            print("Rerouting!")
            route = findRoute(curr,p)
            print("Route:",route)
            if route is None or len(route) < 2:
                route_done = -1
                done_cond.notify_all()
                ret = False
                break
            print("Found new route!")
            i = 0
        elif res == 2:
            print("Interrupted!")
            ret = False
            break
        else:
            print("Arrived at intermediate pt!")
            i += 1

        if len(route) <= i+1:
            print("Finished!")
            route_done = 1
            ret = True
            done_cond.notify_all()
            break

        prev,nex = route[i],route[i+1]
    route_lock.release()
    return ret

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
