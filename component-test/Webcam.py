from sr.robot import *
'''
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
'''
class robit():
    def __init__(self, arg):
        self.R = Robot()R = Robot()
        super(robit, self).__init__()
        self.arg = arg

    def setWheels(self,a,b):
        self.R.motors[0].m0.power = a
        R.motors[0].m1.power = -b

    def see(self):
        markers = R.see()
            if len(markers) < 1:
                setWheels(100,-100)


'''
camara scans stuff
store deets
wheels look at deets
'''
robit = robit()
