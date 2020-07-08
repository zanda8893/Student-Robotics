from arena import *
import cube
from cube import Cube
from sr.robot import *
import position
import conversions
"""
class Cube():
    def __init__(self):
        self.x=0
        self.y=0
"""

def test1():
    l1 = (Position(0,0),Position(80,100))
    l2 = (Position(60,0),Position(5,40))
    l3 = (Position(50,0),Position(0,35))

    l4 = (Position(2800,0),Position(2900,2700))
    l5 = (Position(2200,2200),Position(3000,2200))
    print("L1 + L2 {0}".format(linesIntersect(l1,l2)))
    print("L1 + L3 {0}".format(linesIntersect(l1,l3)))
    print("L2 + L3 {0}".format(linesIntersect(l2,l3)))
    print("L4 + L5 {0}".format(linesIntersect(l4,l5)))    

def test2():
    a = [Position(10,10),Position(10,5600),Position(5600,5600),
         Position(5600,10)]
    for p in a:
        c = Cube()
        c.x = p.x
        c.y = p.y
        for i in range(4):
            print(cubeInZone(c,i))

def test3():
    l1 = (Position(2800,0),Position(2900,2600)) #True
    l2 = (Position(5000,0),Position(0,5000)) #True
    l3 = (Position(4500,0),Position(0,4500)) #False
    l4 = (Position(2500,5),Position(5,2500)) 
    for l in (l1,l2,l3,l4):
        print(l,A.pathClear(l[0],l[1]))

def test4():
    pts = [Position(5,30),Position(0,5)]
    p = Position(30,30)
    end = Position(25,25)
    print(sortPts(pts,p,end))

def test5():
    p = Position(500,500)
    markers = R.see()
    A.addMarkers(markers)
    print(A)
    R.sleep(5)
    markers = R.see()
    A.addMarkers(markers)
    print(A)
    c = A.getNearest(p,MARKER_TOKEN_GOLD)
    print("Nearest gold: ",c)
    c = A.getNearest(p,MARKER_TOKEN_SILVER)
    print("Nearest silver: ",c)
    c = A.getCubeById(45)
    print("ID 45: ",c)
    A.removeCube(45)
    print(A)

def prList(l):
    for i in l:
        print(conversions.toSimCoords(i))

def test6():
    p = Position(500,500)
    markers = R.see()
    A.addMarkers(markers)
    print(A)
    pts = [Position(1950,1950),Position(1850,1850)]
    for pt in pts:
        print(conversions.toSimCoords(pt),A.ptClear(pt,80))
    print("-----------")
    prList(A.getRoutePts(p))
    prList(A.getRoutePts(p,Position(1000,1000)))

    
test6()
test3()
