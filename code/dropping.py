

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
    x = 1.44
    y = 1.44

    if Zone == 0:
        x = -x
        y = -y

    if Zone == 1:
        x = x
        y = -y

    if Zone == 2:
        x = x
        y = y

    if Zone == 3:
        x = -x
        y = y
        
