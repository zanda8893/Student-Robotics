import math
from robot_obj import R
import position
from position import Position
import cube

def orientation(p1,p2,p3):
    #clockise,anticlockwise,straight = 1,2,0
    m = (p1.y-p2.y)/(p1.x-p2.x)
    c = p1.y - m*p1.x
    if p3.y > m*p3.x + c:
        return 2
    if p3.y == m*p3.x + c:
        return 0
    return 1

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
    l = (Position(a,a),Position(b,b))
    if linesIntersect((start,end),l):
        return True
    l = (Position(a,b),Position(b,a))
    if linesIntersect((start,end),l):
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
    return pts.sort(key=lambda pt:perpDist(p,end,pt))

#closest the centre of the robot can get to the centre of
#the cube to avoid contact
robot_cube_distance = 300
#closest the centre of the robot can get to the platform
robot_plaform_distance = 200

class Arena():
    def __init__(self):
        self.cubeList = []

    def addCube(self,newCube):
        for cube in self.cubeList:
            if cube.code == newCube.code:
                found = True
        if found != True:
            self.cubeList.append(newCube)

    def getNearest(self,p,col):
        i = -1
        old = 100000
        for ind in range(self.cubeList.length()):
            cube = self.cubeList[ind]
            if cube.color != col:
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

    def getCubeById(cubeId):
        for c in self.cubeList:
            if c.code == cubeId:
                return c
        return None

    def removeCube(self,code):
        for i in range(self.cubeList.length()):
            if self.cubeList[i].code == code:
                self.cubeList.pop(i)
                return True
        return False

    def pathClear(start,end):
        for cube in self.cubeList:
            if cube.hitsPath(start,end,robot_cube_distance):
                return False
        if pathHitsPlatform(start,end,robot_platform_distance):
            return False
        return True

    def ptClear(p,minDist):
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

    def getRoutePts(p,target=None,lim=5):
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
