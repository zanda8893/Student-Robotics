#Main loop

#~~ = Yet to be implimented/written

#Imports
import lift, claw, position #, route
from robot_obj import R
from arena import A


while True:
    #Start

    #Set claw and lift to known possitions
    claw.openClaw()
    lift.raiseLift()

    #Look for markers
    markers = R.see()

    #~~Arena function for importing marker data into cube class~~Joe

    #Find robot possition
    Rp,Ra = position.findPosition(markers) #Rp = Robot coordinates, a = Robot angle

    #Find nearest cube
    Cp, Cc = A.getNearest(p,"MARKER_TOKEN_GOLD") #Cp = Cube possition, Cc= Cube colour. Possible colours: MARKER_TOKEN_GOLD, MARKER_TOKEN_SILVER

    #Go to nearest cube
    route.goToPoint(Cp)
    #Wait to arrive
    if wait() ==1:
        continue
    else:
        #~~Code for routing error~~

    #~~oriente to cube angle~~Joe

    """~~
    if cubeHigh(Cp):
        claw.grabClawSync()
    else:
        lift.lowerLiftSync()
        claw.grabClawSync()
    """#~~

    #Hp = Home possition ~~find place for cube~~Luka

    #Go to Hp
    route.goToPoint(Cp)
    #Wait to arrive
    if wait() ==1:
        continue
    else:
        #~~Code for routing error~~
    claw.openClaw()

    #End
