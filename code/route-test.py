import route
from position import Position
from sr.robot import *
from robot_obj import R
from arena import A


#markers = R.see()
#A.addMarkers(markers)

#t0 = R.time()
#print("Final",route.findRoute(Position(500,500),Position(5000,5000)))
#print("Time: ",R.time()-t0)

print(A)
res = route.goToPointSync(Position(2045,2875))
print("Finished",res)
