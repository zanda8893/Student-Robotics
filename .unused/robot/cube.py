import math
from sr.robot import *
p = Point

class Cube():
    def __init__(self,marker,rx,ry,ra):
            self.x = rx + (math.sin(ra + p.polar.rot_x))
            self.y = ry + (math.cos(ra + p.polar.rot_y))
            self.bearing = p.orientation.rot_y - (90 - p.polar.rot_y - ra)
            self.color = marker.info.marker_type
