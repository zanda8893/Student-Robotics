import math
import robot

class Arena():
    def __init__(self):
        self.cubeList = []
        self.rx = 0
        self.ry = 0
        self.ra = 0

    def addCube(self,newCube):
        for cube in self.cubeList:
            if cube == newCube:
                found = True
        if found != True:
            self.cubeList.append(newCube)

    def robotPos(self,marker):
        markerType = marker.info.maker_type()
        if markerType == "MARKER_ARENA":
            #markerNum = marker.info.code()
            markerNum = 0
            tx = 718
            ty = 5750
            self.rx = tx - marker.info.dist()*math.sin(3.1415*marker.info.oriantation()/180)
            seff.ry = ty - marker.info.dist()*math.cos(3.1415*marker.info.oriantation()/180)
