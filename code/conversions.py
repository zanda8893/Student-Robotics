from position import Position

#convert single ordinate to competition value
def toSimOrd(x):
    return (x - 5750/2) / 1000

#convert Position from our coordinates to simulator coordinates
def toSimCoords(p):
    return Position(toSimOrd(p.x),toSimOrd(p.y))

#convert single ordinate from simulator version to our version
def fromSimOrd(x):
    return 5750/2 + (1000 * x)

#convert simulator coordinates to our coordinates
def fromSimCoords(p):
    return Position(fromSimOrd(p.x),fromSimOrd(p.y))
