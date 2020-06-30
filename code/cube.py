import math
from sr.robot import *

R = Robot()
markers = R.see()

class Cube():
    def __init__(self,marker,rx,ry):
            self.x = rx + math.cos((ra) * d)
            self.y = ry + math.sin((ra) * d)
            self.color = m.info.marker_type

#robot coords in green zone
rx = -2.37503
ry = -2.37503

for m in markers:
    if m.info.marker_type != MARKER_ARENA:
        ra = math.radians(m.orientation.rot_y) + math.radians(m.orientation.rot_y)
        d = m.dist
        print('Color:',m.info.marker_type,'#:',m.info.code,'dist:',m.dist,'angle:',m.orientation.rot_y)
        print('x:',Cube(rx,ry,ra).x,'y:',Cube(rx,ry,ra).y)
