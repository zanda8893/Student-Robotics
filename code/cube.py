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
        #NOTE: technically it should be 100, but this seems to be an error
        self.x -= deg.sin(self.a) * 200
        self.y -= deg.cos(self.a) * 200

        self.__updateP()
        
        self.color = marker.info.marker_type
        self.code = marker.info.code

    def __updateP(self):
        self.p = Position(self.x,self.y)
        
    #functions that define how the cube is printed
    def __str__(self):
        return "x: {0}  y: {1}  col: {2}".format(self.x,self.y,self.color)

    def __repr__(self):
        return self.__str__()

    def hitsPath(self,start,end,minDist):
        d = position.perpDist(start,end,self.p)
        ds = self.p.dist(start)
        de = self.p.dist(end)
        return min(d,ds,de) < minDist

    #tuple of potential route points
    def getRoutePts(self,p,minDist):
        cube_margin = 120
        cube_path_margin = 100
        
        d = p.dist(self.p)
        r = cube_path_margin + minDist
        da = deg.acos(r/d)
        vec = self.p - p
        a = deg.atan(vec.y/vec.x)
        p1 = self.p + Position(cube_margin+minDist,0).rotate(a+da)
        p2 = self.p + Position(cube_margin+minDist,0).rotate(a-da)
        return [p1,p2]

