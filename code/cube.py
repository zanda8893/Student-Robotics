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

        self.__updateP()
        
        self.color = m.info.marker_type

    def __updateP(self):
        self.p = Position(self.x,self.y)
        
    #functions that define how the cube is printed
    def __str__(self):
        return "x: {0}  y: {1}  col: {2}".format(self.x,self.y,self.color)

    def __repr__(self):
        return self.__str__()

    def hitsPath(start,end,minDist):
        p = Position(self.x,self.y)
        d = position.perpDist(start,end,p)
        return d < minDist

    #tuple of potential route points
    def getRoutePts(self,p,minDist):
        cube_margin = 120
        
        d = p.dist(self.p)
        r = cube_margin + minDist
        da = deg.acos(r/d)
        vec = self.p - p
        a = deg.atan(vec.y/vec.x)
        p1 = self.p + Position(r,0).rotate(a+da)
        p2 = self.p + Position(r,0).rotate(a-da)
        return [p1,p2]

