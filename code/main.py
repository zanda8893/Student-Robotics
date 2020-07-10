#Main loop

#~~ = Yet to be implimented/written

#Imports
import lift, claw, position, route_new
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
    print("See")
    #Find robot position
    #Rp = Robot coordinates, Ra = Robot angle
    print("pos")
    Rp,Ra = position.findPosition(markers)
    #print("arena")
    #A.addMarkers(markers,Rp,Ra)

    #Find nearest cube
    #colour either MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER
    #print("get near")
    #cube = A.getNearest(Rp,MARKER_TOKEN_GOLD)

    #print(cube)
    """
    if cube.p.onPlatform():
        lift.raiseLift()
    else:
        lift.lowerLift()
    """
    #print(cube.code)
    #Go to nearest cube
    #~~res = orienting.goToCube(cube.code)
    route_new.goToCube("test")

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
