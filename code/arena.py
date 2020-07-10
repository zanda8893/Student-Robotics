import math
import deg
from sr.robot import *
from robot_obj import R
import position
from position import Position
import cube
from cube import Cube
from conversions import *

"""
Intersection code copied from geeksforgeeks.org
"""

# Given three colinear points p, q, r, the function checks if
# point q lies on line segment 'pr'
def onSegment(p, q, r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False

def orientation(p, q, r):
    # 0 : Colinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
        return 1
    elif (val < 0):
        return 2
    else:
        return 0

# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.
def linesIntersect(l1,l2):
    p1,q1,p2,q2 = l1[0],l1[1],l2[0],l2[1]
    # Find the 4 orientations required for
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True

    # Special Cases
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True
    return False

def pathHitsPlatform(start,end,minDist):
    a,b = 5750/2-600-minDist,5750/2+600+minDist
    poss = [Position(a,a),Position(a,b),Position(b,b),Position(b,a)]
    for i in range(4):
        l = (poss[i],poss[(i+1) % 4])
        #print(start,end,l)
        if linesIntersect((start,end),l):
            #print("A")
            return True
    return False

def cubeInZone(cube,zone):
    t = 0
    if zone == 0:
        t = cube.x + cube.y
    elif zone == 1:
        t = cube.x + (5750 - cube.y)
    elif zone == 2:
        t = (5750 - cube.x) + (5750 - cube.y)
    else:
        t = (5750 - cube.x) + cube.y
    return t < 2500

def sortPts(pts,p,end):
    pts.sort(key=lambda pt:position.perpDist(p,end,pt))
    return pts

#closest the centre of the robot can get to the centre of
#the cube to avoid contact
robot_cube_distance = 450
#closest the centre of the robot can get to the platform
robot_platform_distance = 300

class Arena():
    def __init__(self):
        self.cubeList = [
            Cube(code=32,color=MARKER_TOKEN_GOLD,p=Position(3775,3775),a=0),
            Cube(code=33,color=MARKER_TOKEN_GOLD,p=Position(3775,1975),a=0),
            Cube(code=34,color=MARKER_TOKEN_GOLD,p=Position(1975,1975),a=0),
            Cube(code=35,color=MARKER_TOKEN_GOLD,p=Position(1975,3775),a=0),
            Cube(code=36,color=MARKER_TOKEN_GOLD,p=Position(2875,2455),a=0),
            Cube(code=37,color=MARKER_TOKEN_GOLD,p=Position(3295,2875),a=0),
            Cube(code=38,color=MARKER_TOKEN_GOLD,p=Position(2455,2875),a=0),
            Cube(code=39,color=MARKER_TOKEN_GOLD,p=Position(2875,3295),a=0),
            Cube(code=40,color=MARKER_TOKEN_SILVER,p=Position(3195,3195),a=0),
            Cube(code=41,color=MARKER_TOKEN_SILVER,p=Position(3195,2555),a=0),
            Cube(code=42,color=MARKER_TOKEN_SILVER,p=Position(2555,2555),a=0),
            Cube(code=43,color=MARKER_TOKEN_SILVER,p=Position(2555,3195),a=0),
            Cube(code=44,color=MARKER_TOKEN_SILVER,p=Position(4175,2875),a=45),
            Cube(code=45,color=MARKER_TOKEN_SILVER,p=Position(1575,2875),a=45),
            Cube(code=46,color=MARKER_TOKEN_SILVER,p=Position(2875,4175),a=45),
            Cube(code=47,color=MARKER_TOKEN_SILVER,p=Position(2875,1575),a=45)
        ]

    def __str__(self):
        s = ""
        for c in self.cubeList:
            s += c.__str__() + "\n"
        return s

    def __repr__(self):
        return self.__str__()

    def addCube(self,newCube):
        return
    """
        if newCube.code == 33:
            print("CUBE 33: {0}".format(toSimCoords(newCube.p)))
        found = False
        for i in range(len(self.cubeList)):
            cube = self.cubeList[i]
            if cube.code == newCube.code:
                found = True
                self.cubeList[i] = newCube
                

        if found != True:
            print("Cube {0} detected at {1}!".format(newCube.code,toSimCoords(newCube.p)))
            self.cubeList.append(newCube)
    """
    def addMarkers(self,markers,rp=None,ra=None):
        if rp is None or ra is None:
            r = position.findPosition(markers)
            if r is None:
                return
            rp = r[0]
            ra = r[1]
        rx = rp.x
        ry = rp.y
        for m in markers:
            if m.info.marker_type == MARKER_ARENA:
                continue
            c = Cube(m,rx,ry,ra)
            self.addCube(c)

    def getNearest(self,p,col,t=6,n=0,inZone=False):
        #col=colour, t=time since seeing cube, n=nth furthest (0=closest)
        l = []
        for ind in range(len(self.cubeList)):
            cube = self.cubeList[ind]
            if cube.color != col:
                continue
            if R.time() - cube.ts > t:
                continue
            if cubeInZone(cube,R.zone) != inZone:
                continue
            l.append(self.cubeList[ind])
        l.sort(key=lambda c: c.p.dist(p))
        if len(l) <= n:
            return None
        return l[n]

    def getCubeById(self,cubeId):
        for c in self.cubeList:
            if c.code == cubeId:
                return c
        return None

    def removeCube(self,code):
        for i in range(len(self.cubeList)):
            if self.cubeList[i].code == code:
                self.cubeList.pop(i)
                return True
        return False

    def pathClear(self,start,end):
        global robot_cube_distance,robot_platform_distance
        for cube in self.cubeList:
            if cube.hitsPath(start,end,robot_cube_distance):
                #print("Failing due to cube",cube)
                return False
        if pathHitsPlatform(start,end,robot_platform_distance):
            #print("Failing due to platform")
            return False
        return True

    def ptClear(self,p,minDist):
        if p.x < minDist or p.x > 5750-minDist:
            return False
        if p.y < minDist or p.y > 5750-minDist:
            return False
        if p.onPlatform():
            return False
        for c in self.cubeList:
            if c.p.dist(p) < minDist:
                return False
        return True

    def getRoutePts(self,p,target=None,lim=5,tlim=15):
        #tlim is the time since seeing the cube
        global robot_cube_distance
        pts = []
        platform_margin = 160
        for cube in self.cubeList:
            if cube.p.onPlatform():
                continue
            if R.time() - cube.ts <= tlim:
                pts += cube.getRoutePts(p,robot_cube_distance+50)
        poss = (5750/2-600-platform_margin,5750/2+600+platform_margin)
        for x in poss:
            for y in poss:
                pts.append(Position(x,y))
        if not target is None:
            pts = sortPts(pts,p,target)
        i = 0
        ret = []
        for pt in pts:
            if len(ret) >= lim:
                break
            if self.pathClear(p,pt):
                ret.append(pt)
            #else:
                #print("Point {0} isn't clear".format(pt))
        print("Potential route points:",ret)
        return ret

A = Arena()
