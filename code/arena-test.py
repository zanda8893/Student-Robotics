from arena import *
import cube
from sr.robot import *
import position

class Cube():
    def __init__(self):
        self.x=0
        self.y=0

def test1():
    l1 = (Position(0,0),Position(80,100))
    l2 = (Position(60,0),Position(5,30))
    l3 = (Position(50,0),Position(0,35))
    print("L1 + L2 {0}".format(linesIntersect(l1,l2)))
    print("L1 + L3 {0}".format(linesIntersect(l1,l3)))
    print("L2 + L3 {0}".format(linesIntersect(l2,l3)))

def test2():
    a = [Position(10,10),Position(10,5600),Position(5600,5600),
         Position(5600,10)]
    for p in a:
        c = Cube()
        c.x = p.x
        c.y = p.y
        for i in range(4):
            print(cubeInZone(c,i))
test2()
