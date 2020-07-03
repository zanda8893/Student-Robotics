#test file
import position
import robot_obj
from conversions import *

while True:
    markers = robot_obj.R.see()
    for m in markers:
        d = m.centre.world.z
        print("  Distance to {0} is {1}".format(m.info.code,d))
    print(toSimCoords(position.findPosition(markers)[0]))
    robot_obj.R.sleep(1)

    
