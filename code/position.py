from sr.robot import *
import deg
import math
import robot_obj
from robot_obj import R
from safediv import *

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Position(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Position(self.x-other.x,self.y-other.y)
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __repr__(self):
        return self.__str__()
    def dist(self,p):
        return math.sqrt((self.x-p.x)**2+(self.y-p.y)**2)
    def rotate(self,angle):
        #rotate point anticlockwise about origin
        x = self.x
        y = self.y
        self.x = x * deg.cos(angle) - y * deg.sin(angle)
        self.y = x * deg.sin(angle) + y * deg.cos(angle)
        return self
    def onPlatform(self):
        if self.x < 5750/2-600:
            return False
        if self.x > 5750/2+600:
            return False
        if self.y < 5750/2-600:
            return False
        if self.y > 5750/2+600:
            return False
        return True

import markers
from conversions import *

"""
These functions shouldn't be needed if SR fix the simulator
"""

#apply a polynomial to the point to correct errors
def polyDistance(d):
    d = d/1000

    d *= 1000
    return p

def wtf(rp,side):
    d = 0
    if side % 2:
        d = rp.x
    else:
        d = rp.y
    if side == 1 or side == 2:
        d = 5750 - d

    magic_number = 110 + 100 * (d / 5750)
    #print("Magic",magic_number)
    if side==0:
        rp.x += magic_number
    elif side==1:
        rp.y -= magic_number
    elif side==2:
        rp.x -= magic_number
    else:
        rp.y += magic_number

    return rp

#returns corrected orientation
def wtf2(pol,orient):
    if math.fabs(orient - pol) > 90:
        print("Correcting!")
        return (orient + 180) % 360
    return orient

camera_distance = 5.2

#returns a list containing the Position and angle of the robot
def findInfoMarker(marker):
    global camera_distance
    #angle between normal to marker and line between marker and robot
    ang = marker.orientation.rot_y - marker.centre.polar.rot_y
    #coordinates of marker
    mp = markers.markerCoordinate(marker)
    #angle of marker (measured CCW from positive x-axis)
    ma = markers.markerAngle(marker)
    d = marker.dist * 1000 #convert to mm
    #position of robot relative to marker
    p = Position(d*deg.cos(ang),d*deg.sin(ang))

    #robot angle, robot position
    orient = wtf2(marker.centre.polar.rot_y,marker.orientation.rot_y)
    ra = (orient + ma + 180) % 360
    rp = mp + p.rotate(ma)

    """
    cd = camera_distance
    rp -= Position(cd * deg.cos(ra),cd * deg.sin(ra))
    """

    rp = wtf(rp,markers.markerSide(marker))
    if marker.info.code == 6:
        print("Or {0} ma {1} ra {2}".format(marker.orientation.rot_y,ma,ra))
    #print("Pos: {0} Ang: {2} Code: {1}".format(toSimCoords(rp),marker.info.code,ra))
    return [rp,ra]

#gets an average over several markers
#returns None if there were no arena markers
def findPosition(markers):
    total = [Position(0,0),0] #position, angle
    n = 0
    for m in markers:
        if m.info.marker_type != MARKER_ARENA:
            continue

        x = findInfoMarker(m)
        total[0] = total[0] + x[0]
        total[1] = total[1] + x[1]
        n += 1

    if n==0:
        return None
    p = Position(total[0].x / n,total[0].y / n)
    a = total[1] / (n)
    return [p,a]

#does markers and position
def getPosition():
    markers = robot_obj.R.see()
    return findPosition(markers)

#perpendicular distance of p from line (start,end)
def perpDist(start,end,p):
    a1 = deg.atan(safeDiv(end.y-start.y,end.x-start.x))
    a2 = deg.atan(safeDiv(p.y-start.y,p.x-start.x))
    a = a1 - a2
    d = p.dist(start)
    opp = d * deg.sin(a)
    return math.fabs(opp)

#True if a line through p can be drawn perpendicular to (start,end)
def perpBetween(start,end,p):
    m = -safeDiv(end.x-start.x,end.y-start.y)
    c = p.y - p.x * m
    sAbove = (start.y > m*start.x + c)
    eAbove = (end.y > m*end.x + c)
    return sAbove != eAbove

#distance of p from start parallel to (start,end)
def paraDist(start,end,p):
    a1 = deg.atan(safeDiv(end.y-start.y,end.x-start.x))
    a2 = deg.atan(safeDiv(p.y-start.y,p.x-start.x))
    a = a1 - a2
    d = p.dist(start)
    opp = d * deg.cos(a)
    return opp

#bearing of end from start
def anglePts(start,end):
    ang = deg.atan(safeDiv(end.y-start.y,end.x-start.x))
    if start.x > end.x:
        ang = (ang+180) % 360
    elif start.x == end.x:
        if end.y > start.y:
            ang = 90
        elif end.y < start.y:
            ang = -90
        else:
            ang = 0
    return ang

#gets difference between angles between -180 and 180
def getAngleDiff(a,ta):
    diff = (a - ta)
    while diff < -180:
        diff += 360
    while diff > 180:
        diff -= 360
    return diff

#translate a position from zone 0 to zone
def translateToZone(p,zone=None):
    if zone is None:
        zone = R.zone
    for i in range(zone):
        p = Position(p.y,5750-p.x) #rotate clockwise
    return p.x,p.y

#convert a bearing from zone 0 to zone
def bearingToZone(a,zone=None):
    if zone is None:
        zone = R.zone
    return (a - 90*zone) % 360
