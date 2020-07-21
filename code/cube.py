import math
from sr.robot import *
from robot_obj import R
import deg
from position import Position
import position
import conversions
import drive

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
            raise TypeError
        #ra is the robot's angle, measured anticlockwise from x-axis
        
        #ra - marker.rot_y is the angle between the x-axis and the
        #line between the cube and the robot

        #ra - marker.orientation.rot_y is the anticlockwise angle
        #between the negative x-axis and the normal to the marker

        #self.a is the anticlockwise angle between the marker's normal
        #and the positive x-axis
        #print("\n\n--------------------")
        d = marker.dist * 1000
        orient = position.wtf2(marker.rot_y,marker.orientation.rot_y)
        #print(f"Marker distance {d} orientation {marker.orientation.rot_y}")
        self.a = (ra - orient + 180) % 360
        #print(f"Marker angle {self.a}")
        adiff = ra - marker.rot_y
        #print(f"Adiff {adiff}")
        self.x = rx + deg.sin(adiff) * d
        self.y = ry + deg.cos(adiff) * d

        p = conversions.toSimCoords(Position(self.x,self.y))
        #print("Before correction: {0} {1}".format(p,self.a))
        #apply corrections to x and y due to size of cube
        self.x -= deg.sin(self.a) * 180
        self.y -= deg.cos(self.a) * 180

        self.__updateP()
        #print("After correction:",conversions.toSimCoords(self.p))
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

def getNumCode(code):
    order = [34,35,32,33]
    if not code in order:
        return -1
    i = order.index(code)
    i = (i - R.zone) % 4
    nums = [0,1,3,2]
    return nums[i]
    
expected_pts = [Position(1975,1975),Position(1975,3775),
                Position(3775,1975),Position(3775,3775)]


codes1 = [34,35,32,33]
codes2 = [38,39,37,36]
codes = [codes1[R.zone],
         codes1[(R.zone+1)%4],
         codes1[(R.zone+3)%4],
         codes2[R.zone],
         codes2[(R.zone+3)%4]]

def getNthCode(n):
    global codes
    return codes[n]

#Takes a relative cube n and determines if it is present
#If the cube is present, 1 is returned
#If the cube is visible but in the wrong place, -1 is returned
#If the cube is not visible, 0 is returned
#It is the caller's responsibility to orient the robot so it
#should be able to see the cube
def nthCubePositionCorrect(n,pos):
    global codes
    mks = R.see()
    code = getNthCode(n)
    for m in mks:
        if m.info.marker_type == MARKER_ARENA:
            continue
        c = Cube(m)
        if c.code == code:
            if c.p.dist(pos) < 120:
                return 1,c.p.dist(pos)
            return -1,c.p.dist(pos)
    return 0,0
