import math
from sr.robot import *
import cube

camaraPos = (200,-50)
class Arena():
    def __init__(self):
        self.cubeList = []
        self.rx = 0
        self.ry = 0
        self.ra = 0
        self.R = Robot()

    def robotPosAverage(self, markerList):
        markerType = marker.info.maker_type()
        ArenaList = []
        for marker in markerList
            if markerType != "MARKER_ARENA":
                addCube(Cube(marker,self.rx,self.ry,self.ra))
            else:
                ArenaList.append(marker)
        posList = []
        totalrx = 0
        totalry = 0
        totalra = 0
        for marker in ArenaList:
            pos = robotPos(marker)
            posList.append(pos)
            totalrx += pos[0]
            totalry += pos[1]
            totalra += pos[3]
        self.rx = totalrx / len(posList)
        self.ry = totalry / len(posList)
        self.ra = totalra / len(posList)

    def addCube(self,newCube):
        for cube in self.cubeList:
            if cube.id == newCube.id:
                found = True
        if found != True:
            self.cubeList.append(newCube)

    def robotPos(self,marker):
        global camaraPos
        markerNum = marker.info.code()
        if markerNum < 7:
            ty = 5750
            tx = (markerNum+1)*718
            ra = 90+marker.oriantation.rot_y()+maker.polar.rot_y()
            rx = tx+marker.info.dist()*math.sin(3.1415*marker.info.oriantation()/180)
            ry = ty-marker.info.dist()*math.cos(3.1415*marker.info.oriantation()/180)
        elif markerNum < 14:
            ty = (14-markerNum)*718
            tx = 5750
            ra = marker.oriantation.rot_y()+maker.polar.rot_y()
            rx = tx-marker.info.dist()*math.cos(3.1415*marker.info.oriantation()/180)
            ry = ty-marker.info.dist()*math.sin(3.1415*marker.info.oriantation()/180)
        elif markerNum < 21:
            ty = 0
            tx = (21-markerNum)*718
            ra = 270+marker.oriantation.rot_y()+maker.polar.rot_y()
            rx = tx-marker.info.dist()*math.sin(3.1415*marker.info.oriantation()/180)
            ry = ty+marker.info.dist()*math.cos(3.1415*marker.info.oriantation()/180)
        else:
            ty = (markerNum-20)*718
            tx = 0
            ra = 180+marker.oriantation.rot_y()+maker.polar.rot_y()
            rx = tx+marker.info.dist()*math.cos(3.1415*marker.info.oriantation()/180)
            ry = ty+marker.info.dist()*math.sin(3.1415*marker.info.oriantation()/180)
        rx = rx-camaraPos[0]*math.sin(3.1415*ra/180)-camaraPos[1]*math.cos(3.1415*ra/180)
        ry = ry-camaraPos[1]*math.sin(3.1415*ra/180)-camaraPos[0]*math.cos(3.1415*ra/180)
        return [rx,ry,ra]

    def closeCube(self):
        smallDist=10000
        closeCube=""
        for cube in self.cubeList:
            dist = ((cube.x-self.rx)**2+(cube.y-self.ry)**2)**0.5
            if smallDist > dist:
                smallDist = dist
                closeCube = cube
        return closeCube
