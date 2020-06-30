#get the edge on which the marker lies
#edge n is the edge clockwise of zone n
#returns None if the marker isn't an arena marker
def markerSide(marker):
    if marker.info.code > 27:
        return None
    if marker.info.code < 0:
        return None
    return marker.info.code // 7

#returns x or y coordinate of arena marker
#returns x if on side 1 or 3
#returns y if on side 0 or 2
def markerOrdinate(marker):
    n = marker.info.code % 7
    #first term and common difference
    a = 5750 / 8
    d = 5750 / 8
    if marker.info.code > 13:
        n = 6 - n
    return a + d*n

#position of marker
def markerCoordinate(marker):
    from position import Position
    ordinate = markerOrdinate(marker)
    other = 0
    if marker.info.code > 6 and marker.info.code < 21:
        other = 5750
    if markerSide(marker) % 2:
        return Position(ordinate,other)
    else:
        return Position(other,ordinate)

#angle, as viewed from above, of the marker's normal
#to the x-axis going anticlockwise
def markerAngle(marker):
    ms = markerSide(marker)
    if ms is None:
        return None
    return (-90 * ms) % 360


"""
#Test

class Info():
    def __init__(self,c):
        self.code = c
class Marker():
    def __init__(self,c):
        self.info = Info(c)
        

for i in range(30):
    m = Marker(i)
    print("Marker {0} has angle {1}".format(i,markerCoordinate(m)))
"""
