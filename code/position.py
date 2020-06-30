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



#returns a list containing the Position and angle of the robot
def findInfoMarker(marker):
    ang = marker.orientation.rot_y - marker.centre.polar.rot_y
    mp = markers.markerCoordinate(marker)
    ma = markers.markerAngle(marker)
    d = marker.centre.polar.length * 1000 #convert to mm
    #cam_p = Position(1000*marker.center.world.x,1000*marker.center.world.z)
    p = Position(d*deg.cos(ang),d*deg.sin(ang))
    print("      angle: {0}".format(ang))
    
    ra = (ang + ma + 180) % 360
    rp = mp + p.rotate(ma)
    
    return [rp,ra]
    

def findPosition(markers):
    total = [Position(0,0),0] #position, angle
    n = 0
    for m in markers:
        if m.info.marker_type != MARKER_ARENA:
            continue
        n += 1
        x = findInfoMarker(m)
        print("   Info {0}: {1}".format(n,x))
        total[0] = total[0] + x[0]
        total[1] = total[1] + x[1]
    if n==0:
        return None
    p = Position(total[0].x / n,total[0].y / n)
    a = total[1] / n
    return [p,a]
