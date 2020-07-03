import math
from sr.robot import *
from robot_obj import R
import deg
from position import Position
import position
import conversions

class Cube():
    def __init__(self,marker,rx,ry,ra):
        #ra is the robot's angle, measured anticlockwise from x-axis
        
        #ra - marker.rot_y is the angle between the x-axis and the
        #line between the cube and the robot

        #ra - marker.orientation.rot_y is the anticlockwise angle
        #between the negative x-axis and the normal to the marker

        #self.a is the anticlockwise angle between the marker's normal
        #and the positive x-axis

        self.a = (ra - marker.orientation.rot_y + 180) % 360
        self.x = rx + deg.sin(ra - marker.rot_y) * marker.dist*1000
        self.y = ry + deg.cos(ra - marker.rot_y) * marker.dist*1000

        p = conversions.toSimCoords(Position(self.x,self.y))
        print("Before correction: {0}".format(p))
        #apply corrections to x and y due to size of cube
        self.x -= deg.cos(self.a) * 100
        self.y -= deg.sin(self.a) * 100
        
        self.color = m.info.marker_type

    #functions that define how the cube is printed
    def __str__(self):
        return "x: {0}  y: {1}  col: {2}".format(self.x,self.y,self.color)

    def __repr__(self):
        return self.__str__()
    

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
