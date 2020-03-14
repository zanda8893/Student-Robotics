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

    def addCube(self,newCube):
        for cube in self.cubeList:
            if cube.id == newCube.id:
                found = True
        if found != True:
            self.cubeList.append(newCube)

    def robotPos(self,marker):
        global camaraPos
        markerType = marker.info.maker_type()
        if markerType != "MARKER_ARENA":
            addCube(Cube(marker,rx,ry,ra))
        else:
            markerNum = marker.info.code()
            if markerNum < 7:
                ty = 5750
                tx = (markerNum+1)*718
                self.ra = 90+marker.oriantation.rot_y()+maker.polar.rot_y()
                self.rx = tx+marker.info.dist()*math.sin(3.1415*marker.info.oriantation()/180)
                seff.ry = ty-marker.info.dist()*math.cos(3.1415*marker.info.oriantation()/180)
            elif markerNum < 14:
                ty = (14-markerNum)*718
                tx = 5750
                self.ra = marker.oriantation.rot_y()+maker.polar.rot_y()
                self.rx = tx-marker.info.dist()*math.cos(3.1415*marker.info.oriantation()/180)
                self.ry = ty-marker.info.dist()*math.sin(3.1415*marker.info.oriantation()/180)
            elif markerNum < 21:
                ty = 0
                tx = (21-markerNum)*718
                self.ra = 270+marker.oriantation.rot_y()+maker.polar.rot_y()
                self.rx = tx-marker.info.dist()*math.sin(3.1415*marker.info.oriantation()/180)
                self.ry = ty+marker.info.dist()*math.cos(3.1415*marker.info.oriantation()/180)
            else:
                ty = (markerNum-20)*718
                tx = 0
                self.ra = 180+marker.oriantation.rot_y()+maker.polar.rot_y()
                self.rx = tx+marker.info.dist()*math.cos(3.1415*marker.info.oriantation()/180)
                self.ry = ty+marker.info.dist()*math.sin(3.1415*marker.info.oriantation()/180)
            self.rx = self.rx-camaraPos[0]*math.sin(3.1415*self.ra/180)-camaraPos[1]*math.cos(3.1415*self.ra/180)
            self.ry = self.ry-camaraPos[1]*math.sin(3.1415*self.ra/180)-camaraPos[0]*math.cos(3.1415*self.ra/180)

    def closeCube(self):
        smallDist=10000
        closeCube=""
        for cube in self.cubeList:
            dist = ((cube.x-self.rx)**2+(cube.y-self.ry)**2)**0.5
            if smallDist > dist:
                smallDist = dist
                closeCube = cube
        return closeCube
