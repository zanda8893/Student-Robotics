import deg
import route
import position
import arena

position_distance = 150
preposition_distance = 150 #distance to travel from pre to pos
collision_distance = 280
platform_stop_dist = 10

def possiblePrePositions(cube):
    ret = []
    d = position_distance + preposition_distance
    for ang in (0,90,180,270):
        x = d * deg.sin(cube.a + ang)
        y = d * deg.cos(cube.a + ang)
        p = Position(x,y) + cube.p
        if arena.A.ptClear(p,collision_distance):
            ret.append((p,(ang + cube.a)%360))
    return ret

def getPrePositionOther(cube,p):
    pts = possiblePrePositions(cube)
    pts.sort(key=lambda pt:pt[0].dist(p))
    return pts[0]

def getPrePositionPlatform(cube):
    p = cube.p - Position(5750/2,5750/2)
    ang = 0 #angle that the robot should be at
    prep = Position(5750/2,5750/2)
    if p.x >= 0 and math.fabs(p.y) < p.x:
        ang = 180
    elif p.y >= 0 and p.y > math.fabs(p.x):
        ang = 270
    elif p.x < 0 and math.fabs(p.y) < -p.x:
        ang = 0
    elif p.y < 0 and -p.y > math.fabs(p.x):
        ang = 90
    d = preposition_distance + platform_stop_dist + 600
    prep = prep - Position(d * deg.cos(ang),d * deg.sin(ang))
    return (prep,ang)
    
def getPrePosition(cube,p):
    if cube.p.onPlatform():
        return getPrePositionPlatform(cube)
    else:
        return getPrePositionOther(cube,p)

sec_per_deg = 0.1
def setOrientation(a,tol=10):
    global sec_per_deg
    rotate_power = 30
    while True:
        p,curr = position.getPosition()
        diff = getAngleDiff(curr,a)
        if math.fabs(diff) <= tol:
            return True
        t = math.fabs(diff) * sec_per_deg
        if diff < 0:
            rotate_power *= -1
        drive.driveRotateSync(rotate_power,t)

drive_power = 50
def driveDist(d,timeout=10):
    global drive_power
    p0,a = positions.getPosition()
    drive.driveStraight(drive_power)
    t0 = robot_obj.R.time()
    while True:
        p1 = position.getPosition()
        if p1.dist(p0) > d:
            drive.driveStraight(0)
            return True
        if robot_obj.R.time() - t0 > timeout:
            drive.driveStraight(0)
            return False
        
def goToCube(cubeId,currPos):
    global preposition_distance
    cube = arena.A.getCubeById(cubeId)
    pre_p,pre_a = getPrePosition(cube,currPos)
    if cube.p.onPlatform():
        lift.raiseLift()
    else:
        lift.lowerLift()
    claw.openClaw()
    res = route.goToPointSync(pre_p)
    if not res:
        return False
    setOrientation(pre_a)
    return driveStraight(preposition_distance)
