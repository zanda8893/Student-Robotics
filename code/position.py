from sr.robot import *
import deg

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
    def rotate(self,angle):
        #rotate point anticlockwise about origin
        x = self.x
        y = self.y
        self.x = x * deg.cos(angle) - y * deg.sin(angle)
        self.y = x * deg.sin(angle) + y * deg.cos(angle)
        return self
        
import markers
from conversions import *

"""
These functions shouldn't be needed if SR fix the simulator

#apply a polynomial to the point to correct errors
def polyDistance(d):
    d = d/1000
    d = 0.0049 * d**2 + 0.966 * d - 0.198 - d
    d *= 1000
    return p

def wtf(rp,side):
    adj = 0
    if side % 2:
        adj = polyDistance(rp.y)
    else:
        adj = polyDistance(rp.x)
        
    if side==0:
        rp.x += adj
    elif side==1:
        rp.y -= adj
    elif side==2:
        rp.x -= adj
    else:
        rp.y += adj
        
    return rp
"""

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
    d = (d**2 - camera_2_marker_h**2)**0.5 #compensate for h diff
    #position of robot relative to marker
    p = Position(d*deg.cos(ang),d*deg.sin(ang))
    
    #robot angle, robot position
    ra = (marker.orientation.rot_y + ma + 180) % 360
    rp = mp + p.rotate(ma)

    cd = camera_distance
    rp -= Position(cd * deg.cos(ra),cd * deg.sin(ra))

    #print("Pos: {0} Code: {1}".format(toSimCoords(rp),marker.info.code))
    return [rp,ra]
    
#gets an average over several markers
#returns None if there were no arena markers
def findPosition(markers):
    total = [Position(0,0),0] #position, angle
    nx,ny = 0,0
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
    a = total[1] / (nx)
    return [p,a]

#does markers and position
def getPosition():
    markers = robot_obj.R.see()
    return findPosition(markers)

#perpendicular distance of p from line (start,end)
def perpDist(start,end,p):
    a1 = deg.atan((end.y-start.y)/(end.x-start.x))
    a2 = deg.atan((p.y-start.y)/(p.x-start.x))
    a = a1 - a2
    d = p.dist(start)
    opp = d * deg.sin(a)
    return math.fabs(opp)

#True if a line through p can be drawn perpendicular to (start,end)
def perpBetween(start,end,p):
    m = -1 / ((end.y-start.y)/(end.x-start.x))
    c = p.y - p.x * m
    sAbove = (start.y > m*start.x + c)
    eAbove = (end.y > m*end.x + c)
    return sAbove != eAbove

#distance of p from start parallel to (start,end)
def paraDist(start,end,p):
    a1 = deg.atan((end.y-start.y)/(end.x-start.x))
    a2 = deg.atan((p.y-start.y)/(p.x-start.x))
    a = a1 - a2
    d = p.dist(start)
    opp = d * deg.cos(a)
    return opp
