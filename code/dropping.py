

spaces = [] #TODO: fill in with spaces
#number of spaces in previous list already used up
num_used_spaces = 0

#Find a suitable location to place the next cube for zone 0
def locationForCubeZone0():
    pass

#Translate the position depending on the zone
#e.g. (300,200) -> (300,5750-200) for zone 1
def transformLocationToZone(zone):
    pass

#Gets location for cube depending on zone
def locationForCube():
    Zone = R.zone
    xc = 2.66
    yc = 2.66
    xb = 1.44
    yb = 1.44

    if Zone == 0:
        xc = -xc
        yc = -yc
        xb = -xb
        yb = -yb

        x= random.uniform(xb,xc)
        y= random.uniform(yb,yc)
        goToPoint(x,y)

    if Zone == 1:
        xc = xc
        yc = -yc
        xb = xb
        yb = -yb

        x= random.uniform(xb,xc)
        y= random.uniform(yb,yc)
        goToPoint(x,y)

    if Zone == 2:
        xc = xc
        yc = yc
        xb = xb
        yb = yb

        x= random.uniform(xb,xc)
        y= random.uniform(yb,yc)
        goToPoint(x,y)

    if Zone == 3:
        xc = -xc
        yc = yc
        xb = -xb
        yb = yb

        x= random.uniform(xb,xc)
        y= random.uniform(yb,yc)
        goToPoint(x,y)
