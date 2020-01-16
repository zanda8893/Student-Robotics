from sr.robot import *
R = Robot()
def setWheels(a,b):
    R.motors[0].m0.power = a
    R.motors[0].m1.power = -b

while True:
    markers = R.see()
    print "I can see", len(markers), "markers:"
    if len(markers) < 1:
        setWheels(100,-100)
    else:
        m = markers[0]
        if m.info.marker_type == MARKER_ARENA:
            print " - Marker #{0} is {1} metres away".format( m.info.code, m.dist )
        if m.dist >= 0.5:
            setWheels(100,100)
        else:
            setWheels(0,0)
