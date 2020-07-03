import cube
from sr.robot import *
from robot_obj import R
import conversions

while True:
    markers = R.see()
    #use the arena markers to calculate robot's x,y,angle
    x = position.findPosition(markers)
    print("Position: {0}".format(conversions.toSimCoords(x[0])))
    robot_x,robot_y,robot_a = x[0].x,x[0].y,x[1]
    for m in markers:
        if m.info.marker_type == MARKER_ARENA:
            print(m)
            """
        #make cube, print cube
        c = Cube(m,robot_x,robot_y,robot_a)
        p = conversions.toSimCoords(Position(c.x,c.y))
        print("Code: {0} Position: {1} Angle: {2}".format(m.info.code,p,c.a))"""
    R.sleep(1)
