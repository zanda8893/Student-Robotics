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

weird_constant = 212
def wtf(rp,side):
    if side==0:
        rp.x += weird_constant
    elif side==1:
        rp.y -= weird_constant
    elif side==2:
        rp.x -= weird_constant
    else:
        rp.y += weird_constant
    return rp

#returns a list containing the Position and angle of the robot
def findInfoMarker(marker):
    #angle between normal to marker and line between marker and robot
    ang = marker.orientation.rot_y - marker.centre.polar.rot_y
    mp = markers.markerCoordinate(marker)
    ma = markers.markerAngle(marker)
    d = marker.centre.polar.length * 1000 #convert to mm
    #position of robot relative to marker
    p = Position(d*deg.cos(ang),d*deg.sin(ang))
    
    ra = (marker.orientation.rot_y + ma + 180) % 360
    rp = mp + p.rotate(ma)

    side = markers.markerSide(marker)
    rp = wtf(rp,side)
    
    #print("Robot angle: {0}, Robot position: {1}, d: {2}".format(ra,rp,d))
    #print("Angle: {0}, Code: {1}, Or: {2}, Pol: {3}".format(ang,marker.info.code,marker.orientation.rot_y,marker.centre.polar.rot_y))
    print("Pos: {0} Code: {1}".format(rp,marker.info.code))
    return [rp,ra]
    
#gets an average over several markers
#returns None if there were no arena markers
def findPosition(markers):
    total = [Position(0,0),0] #position, angle
    n = 0
    for m in markers:
        if m.info.marker_type != MARKER_ARENA:
            continue
        n += 1
        x = findInfoMarker(m)
        total[0] = total[0] + x[0]
        total[1] = total[1] + x[1]
    if n==0:
        return None
    p = Position(total[0].x / n,total[0].y / n)
    a = total[1] / n
    return [p,a]
