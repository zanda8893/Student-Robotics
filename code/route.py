from position.py import Position


def targetStraightLine(s,e,corner):
    if corner == 0:
        cornerPos = Position(1500,1500)
        if s.x < cornerPos.x and e.x < cornerPos.x:
            return True
        if s.y < cornerPos.y and e.y < cornerPos.y:
            return True
        if cornerPos.y-s.y > (cornerPos.x-s.x)*(e.y-s.y)/(e.x-s.x):
            return True
        return False
    if corner == 0:
        cornerPos = Position(1500,1500)
        if s.x < cornerPos.x and e.x < cornerPos.x:
            return True
        if s.y < cornerPos.y and e.y < cornerPos.y:
            return True
        if cornerPos.y-s.y > (cornerPos.x-s.x)*(e.y-s.y)/(e.x-s.x):
            return True
        return False
    if corner == 0:
        cornerPos = Position(1500,1500)
        if s.x < cornerPos.x and e.x < cornerPos.x:
            return True
        if s.y < cornerPos.y and e.y < cornerPos.y:
            return True
        if cornerPos.y-s.y > (cornerPos.x-s.x)*(e.y-s.y)/(e.x-s.x):
            return True
        return False
    if corner == 0:
        cornerPos = Position(1500,1500)
        if s.x < cornerPos.x and e.x < cornerPos.x:
            return True
        if s.y < cornerPos.y and e.y < cornerPos.y:
            return True
        if cornerPos.y-s.y > (cornerPos.x-s.x)*(e.y-s.y)/(e.x-s.x):
            return True
        return False

def getIntermediatePoint(corner){
    if corner==0:
        return Position(1000,1000)
    if corner==1:
        return Position(1000,1000)
    if corner==2:
        return Position(1000,1000)
    if corner==3:
        return Position(1000,1000)
}


class Route():
    def __init__(self):
        self.points = []
        pass
    def setRoute(self,currentPos,targetPos,corner):
        self.points.clear()
        if targetStraightLine(currentPos,targetPos,corner):
            self.points.append(targetPos)
        else:
            self.points.append(getIntermediatePoint(corner))
            self.points.append(targetPos)
    def followRoute(self,currentPos,orientation): #returns left and right motor speeds
        p = self.points[0]
        if (currentPos.x-p.x)**2 + (currentPos.y-p.y)**2 < 50**2:
            if len(self.points) <= 1:
                return 0,0
            self.points.remove(0)
            p = self.points[0]
        a = math.atan((p.y-currentPos.y)/(p.x-currentPos.x))*180/math.pi
        angleOff = orientation-a
        while angleOff>360:
            angleOff -= 360
        while angleOff<0:
            angleOff += 360

        if angleOff > 20 and angleOff < 180:
            return 20,-20
        if angleOff < 20:
            return 100,100-angleOff*2.5
        if angleOff > 340:
            return 100-angleOff*2.5,100
        else:
            return -20,20


















//
