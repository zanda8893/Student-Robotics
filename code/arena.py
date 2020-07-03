import math
import robot
import position
from position import Position
import cube

def pathHitsCube(start,end,cube,minDist):
    p = Position(cube.x,cube.y)
    d = position.perpDist(start,end,p)
    return d < minDist

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

    def removeCube(self,code):
        for i in range(self.cubeList.length()):
            if self.cubeList[i].code == code:
                self.cubeList.pop(i)
                return True
        return False
    
    def pathClear(start,end):
        for cube in self.cubeList:
            if pathHitsCube(start,end,cube,robot_cube_distance):
                return False
        if pathHitsPlatform(start,end,robot_platform_distance):
            return False
        return True

A = Arena()
