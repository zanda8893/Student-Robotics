#Main loop

#~~ = Yet to be implimented/written

#Imports
import lift, claw, position, route
from robot_obj import R
from arena import A
from sr.robot import *


while True:
    #Start

    #Set claw and lift to known positions
    claw.openClawSync()
    lift.raiseLiftSync()

    #Look for markers
    markers = R.see()

    #Find robot position
    #Rp = Robot coordinates, Ra = Robot angle
    Rp,Ra = position.findPosition(markers)
    A.addMarkers(markers,Rp,Ra)

    #Find nearest cube
    #colour either MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER
    cube = A.getNearest(Rp,MARKER_TOKEN_GOLD)

    print(cube)

    if cube.p.onPlatform():
        lift.raiseLift()
    else:
        lift.lowerLift()

    #Go to nearest cube
    #res = orienting.goToCube(cube.code)
    route.goToPointSync(cube.code)

    """
    if not res:
        #~~Code for routing error~~
        pass
    """

    claw.grabClawSync()

    #Hp = Home position ~~find place for cube~~Luka

    #Go to Hp
    route.goToPoint(Cp)
    #Wait to arrive
    if wait() ==1:
        continue
    #else:
        #~~Code for routing error~~

    claw.openClaw()

    #End
