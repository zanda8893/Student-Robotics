#test file
from position import *
import robot_obj
from conversions import *

#Tests done (though waiting for position fix)

"""
start = Position(0,0)
end = Position(100,75)

pts = [Position(200,150),Position(50,37.5),Position(0,100),Position(50,50)]

for p in pts:
    print("PerpDist {0} PerpBeteen {1} ParaDist {2}".format(perpDist(start,end,p),perpBetween(start,end,p),paraDist(start,end,p)))
"""



while True:
    markers = robot_obj.R.see()
    """
    for m in markers:
        d = m.centre.world.z
        print("  Distance to {0} is {1}".format(m.info.code,d))
    """
    print(toSimCoords(findPosition(markers)[0]))
    robot_obj.R.sleep(1)

    
