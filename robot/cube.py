import math
class Cube():
    def __init__(self,marker,rx,ry,ra):
        self.x = rx + (marker.dist * math.sin(math.radians(ra + p.polar.rot_y)))
        self.y = ry + (marker.dist * math.cos(math.radians(ra + p.polar.rot_y)))
        self.bearing = p.orientation.rot_y - (90 - p.polar.rot_y - ra)
        self.color = marker.info.marker_type
        self.id = marker.info.code
