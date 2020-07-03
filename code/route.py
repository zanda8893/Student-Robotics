import position
import arena

"""
Functions you're allowed to use:
goToPoint(p) - asynchronously go to p (represented by Position class)
goToPointSync(p) - same as goToPoint() but synchronous
arrived() - True if goToPoint() has arrived yet
wait() - wait for most recent route to finish

Note: calling goToPoint() or goToPointSync() while a route is
already being followed will override the current route
"""

def tryRoute(pts):
    if pts.length() < 2:
        return False
    for i in range(pts-1):
        p1 = pts[i]
        p2 = ptr[i + 2]
        if not arena.A.pathClear(p1,p2):
            return False
    return True




"""
#final route
points = []
#route for testing
__points = []
def findRoute(start,end):
    global points,__points
    #__points stores all decided-on points
    __points.append(start)
    p1,p2 = start,end
    if not arena.A.pathClear(p1,p2):
        angle = deg.atan((p2.y-p1.y)/(p2.x-p1.x))
        tp = arena.A.stopPoint(p1,p2)
        mvAng = (90 + angle) % 360
        for dev in range(0,500,10):
            vec = Position(dev * deg.sin(angle),dev * deg.cos(angle))
            tp1 = tp + vec
            tp2 = tp - vec
            if arena.A.pathClear(p1,tp1):
                stat = findRoute(
"""                    

        
        


















