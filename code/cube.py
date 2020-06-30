import math
from sr.robot import *
from robot_obj import R
import deg
import position

class Cube():
    def __init__(self,marker,rx,ry,ra):
        self.x = rx + deg.cos(ra - marker.rot_y) * marker.dist*1000
        self.y = ry + deg.sin(ra - marker.rot_y) * marker.dist*1000
        self.a = (marker.orientation.rot_y + ra) % 360
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
    robot_x,robot_y,robot_a = x[0].x,x[0].y,x[1]
    for m in markers:
        #make cube, print cube
        c = Cube(m,robot_x,robot_y,robot_a)
        print("Code: {0}  {1}".format(m.info.code,c))
