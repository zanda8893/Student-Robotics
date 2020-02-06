import math

class Cube():
    def __init__(self,marker,rx,ry,ra):
            self.x = rx + (math.cos(ra + p.polar.rot_y) * p.polar.length)
            self.y = ry + (math.sin(ra + p.polar.rot_y) * p.polar.length)
            self.bearing = p.orientation.rot_y - (90 - p.polar.rot_y - ra)
            self.color = marker.info.marker_type
            self.dist = p.polar.length
