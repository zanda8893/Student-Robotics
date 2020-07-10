#Main loop

#~~ = Yet to be implimented/written

#Imports
import lift, claw, position, route_new, route, robot_obj
from arena import A



#Start

#Set claw and lift to known positions


#Look for markers
markers = robot_obj.R.see()
print("See")
#Find robot position
#Rp = Robot coordinates, Ra = Robot angle
print("pos")
start_Rp,start_Ra = position.findPosition(markers)
#print("arena")
#A.addMarkers(markers,Rp,Ra)

#Find nearest cube
#colour either MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER
#print("get near")
#cube = A.getNearest(Rp,MARKER_TOKEN_GOLD)

route_new.goToCube("test")
claw.grabClaw()
robot_obj.R.sleep(1)
Rp = position.findPosition(robot_obj.R.see())
if Rp is None:
    print("Pos Failed")
else:
    route.goToPointStraight(Rp[0],start_Rp)

print("Done")
#End
