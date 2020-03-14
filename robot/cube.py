import math
class Cube():
    def __init__(self,marker,rx,ry,ra):
            self.x = rx + (math.sin(math.radians(ra + p.polar.rot_x)))
            self.y = ry + (math.cos(math.radians(ra + p.polar.rot_y)))
            self.bearing = p.orientation.rot_y - (90 - p.polar.rot_y - ra)
            self.color = marker.info.marker_type
            self.code = marker.info.code
    def distance(self,marker):
        marker.dist
