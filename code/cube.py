import math
from sr.robot import *
from robot_obj import R
import deg
from position import Position
import position
import conversions

class Cube():
    #From marker: marker,rx,ry,ra
    #From known: code,color,p,a
    def __init__(self,*args,**kwargs):
        if 'code' in kwargs:
            self.code,self.color = kwargs['code'],kwargs['color']
            self.p,self.a = kwargs['p'],kwargs['a']
            self.x,self.y,self.ts = self.p.x,self.p.y,R.time()
            return
        elif len(args) >= 4:
            marker = args[0]
            rx = args[1]
            ry = args[2]
            ra = args[3]
        else:
            return
        #ra is the robot's angle, measured anticlockwise from x-axis
        
        #ra - marker.rot_y is the angle between the x-axis and the
        #line between the cube and the robot

        #ra - marker.orientation.rot_y is the anticlockwise angle
        #between the negative x-axis and the normal to the marker

        #self.a is the anticlockwise angle between the marker's normal
        #and the positive x-axis

        d = marker.dist * 1000
        self.a = (ra - marker.orientation.rot_y + 180) % 360
        self.x = rx + deg.sin(ra - marker.rot_y) * d
        self.y = ry + deg.cos(ra - marker.rot_y) * d

        p = conversions.toSimCoords(Position(self.x,self.y))
        print("Before correction: {0} {1}".format(p,self.a))
        #apply corrections to x and y due to size of cube
        #NOTE: technically it should be 100, but this seems to be an error
        self.x -= deg.sin(self.a) * 100
        self.y -= deg.cos(self.a) * 100

        self.__updateP()
        print("After correction:",conversions.toSimCoords(self.p))
        self.color = marker.info.marker_type
        self.code = marker.info.code
        self.ts = R.time()

    def __updateP(self):
        self.p = Position(self.x,self.y)
        
    #functions that define how the cube is printed
    def __str__(self):
        return "p: {0}  code: {1}  col: {2}".format(conversions.toSimCoords(self.p),self.code,self.color)

    def __repr__(self):
        return self.__str__()

    def hitsPath(self,start,end,minDist):
        d = position.perpDist(start,end,self.p)
        ds = self.p.dist(start)
        de = self.p.dist(end)
        if position.perpBetween(start,end,self.p):
            return d < minDist
        return min(ds,de) < minDist

    #tuple of potential route points
    #minDist is the minimum distance between cube and robot centres
    def getRoutePts(self,p,minDist):
        rdiff = 10
        ang = deg.acos(minDist/(minDist + rdiff))
        d = p.dist(self.p)
        r = minDist
        da = 0
        if r <= d:
            da = deg.acos(r/d)
        da += ang
        vec = p - self.p
        a = deg.atan(vec.y/vec.x)
        p1 = self.p + Position(minDist+rdiff,0).rotate(a+da)
        p2 = self.p + Position(minDist+rdiff,0).rotate(a-da)
        return [p1,p2]

