from cube import *
from sr.robot import *
from robot_obj import R
import conversions
import position


def getP():
    global p1,p2
    p1 = p1 + Position(800,0)
    p2 = p2 + Position(0,800)
    return (p1,p2)
def initP():
    global p1,p2
    p1.x=1
    p1.y=0
    p2.x=0
    p2.y=0
    
while True:
    markers = R.see()
    #use the arena markers to calculate robot's x,y,angle
    x = position.findPosition(markers)
    print("Position: {0}".format(conversions.toSimCoords(x[0])))
    robot_x,robot_y,robot_a = 500,500,x[1]
    for m in markers:
        if m.info.marker_type == MARKER_ARENA:
            continue
     
        #make cube, print cube
        c = Cube(m,robot_x,robot_y,robot_a)
        """for i in range(100):
            ps,pe = Position(5750-57*i,0),Position(0,5750-57*i)
            print(ps,pe,c.hitsPath(ps,pe,100))
"""
        print(c.getRoutePts(Position(0,0),50))
        p = conversions.toSimCoords(Position(c.x,c.y))
        print("Code: {0} Position: {1} Angle: {2}".format(m.info.code,p,c.a))
    R.sleep(1)
