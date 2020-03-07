import math
from sr.robot import *


class Cube():
    def __init__(self,marker,rx,ry,ra):
            self.x = rx + (math.cos(ra + (p.polar.rot_y * 3.1415)/180) * p.polar.length)
            self.y = ry + (math.sin(ra + (p.polar.rot_y * 3.1415)/180) * p.polar.length)
            self.bearing = p.orientation.rot_y - (90 - p.polar.rot_y - ra)
            self.color = marker.info.marker_type

    def dist(self,x,y,rx,ry):
        dist = ((rx-x)**2 + (ry-y)**2)**0.5
