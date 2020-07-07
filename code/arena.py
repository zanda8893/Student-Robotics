import math
import deg
from sr.robot import *
from robot_obj import R
import position
from position import Position
import cube
from cube import Cube

def orientation(p1,p2,p3):
    #clockise,anticlockwise,straight = 1,2,0
    val = (p2.y-p1.y)*(p3.x-p2.x) - (p2.x-p1.x)*(p3.y-p2.y)
    ret = 2
    if val==0:
        ret = 0
    if val > 0:
        ret = 1
    print(p1,p2,p3," Value:",ret)
    return ret

def linesIntersect(l1,l2):
    o1 = orientation(l1[0],l1[1],l2[0])
    o2 = orientation(l1[0],l1[1],l2[1])
    if o1 == 0 or o2 == 0:
        return True
    if o1 == o2:
        return False
    return True

def pathHitsPlatform(start,end,minDist):
    a,b = 5750/2-600-minDist,5750/2+600+minDist
    poss = [Position(a,a),Position(a,b),Position(b,b),Position(b,a)]
    for i in range(4):
        l = (poss[i],poss[(i+1) % 4])
        print(l)
        if linesIntersect((start,end),l):
            print("A")
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
robot_cube_distance = 300
#closest the centre of the robot can get to the platform
robot_plaform_distance = 200

class Arena():
    def __init__(self):
        self.cubeList = []

    def __str__(self):
        s = ""
        for c in self.cubeList:
            s += c.__str__() + "\n"
        return s

    def __repr__(self):
        return self.__str__()
    
    def addCube(self,newCube):
        found = False
        for i in range(len(self.cubeList)):
            cube = self.cubeList[i]
            if cube.code == newCube.code:
                found = True
                self.cubeList[i] = newCube
                
        if found != True:
            self.cubeList.append(newCube)

    def addMarkers(self,markers,rp=None,ra=None):
        if rp is None or ra is None:
            rp,ra = position.findPosition(markers)
        rx = 500#rp.x
        ry = 500#rp.y
        for m in markers:
            if m.info.marker_type == MARKER_ARENA:
                continue
            c = Cube(m,rx,ry,ra)
            self.addCube(c)
            
    def getNearest(self,p,col,t=6):
        #col=colour, t=time since seeing cube
        i = -1
        old = 100000
        for ind in range(len(self.cubeList)):
            cube = self.cubeList[ind]
            if cube.color != col:
                continue
            if R.time() - cube.ts > t:
                continue
            if cubeInZone(cube,R.zone):
                continue
            newD = math.dist((cube.x,cube.y),(p.x,p.y))
            if newD < old:
                old = newD
                i = ind
        if i >= 0:
            return self.cubeList[i]
        return None

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
        for cube in self.cubeList:
            if cube.hitsPath(start,end,robot_cube_distance):
                return False
        if pathHitsPlatform(start,end,robot_platform_distance):
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
            if c.p.dist < minDist:
                return False
        return True

    def getRoutePts(self,p,target=None,lim=5):
        pts = []
        platform_margin = 120
        for cube in self.cubeList:
            pts += cube.getRoutePts(p,robot_cube_distance)
        poss = (-600-platform_margin,600+platform_margin)
        for x in poss:
            for y in poss:
                pts.append(Position(x,y))
        if not target is None:
            pts = sortPts(pts,p,target)
        i = 0
        ret = []
        for pt in pts:
            if ret.length() >= lim:
                break
            if self.pathClear(p,pt):
                ret.append(pt)
        return ret

A = Arena()
