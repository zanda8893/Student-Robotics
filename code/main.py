
#initialize things
clawIsUp = False
eventTimer = -1 #used to time events

while True:
    if status == "IDLE":
        status = "CUBES_SEARCHING"
    elif status == "CUBES_SEARCHING":
        #search for markers
        if arena.availableCubes() == 0: #no available cubes
            status = "CUBES_ROTATING"
            #---set motors to rotating slowly---
        else:
            currentCube = arena.getBestCube()
            status = "CUBES_ROUTING"
    elif status == "CUBES_ROTATING":
        #stop motors
        time.sleep(0.1)
        #search for cubes
        if arena.availableCubes() != 0:
            currentCube = arena.getBestCube()
            status = "CUBES_ROUTING"
            #---stop motors---
    elif status == "CUBES_ROUTING":
        route.setRoute(arena.getCurrentPosition(),currentCube.position,corner);
        if currentCube.isRaised() and not clawIsUp:
            clawIsUp = True
            status = "CLAW_LIFTING"
        elif not currentCube.isRaised() and clawIsUp:
            clawIsUp = False
            status = "CLAW_LIFTING"
        else:
            status = "GOING_TO_CUBE"
    elif status == "CLAW_LIFTING":
        if clawIsUp and currTime-eventTimer>2500: #been >2.5s and claw lifting
            #stop lift motor
            status = "GOING_TO_CUBE"
        elif currTime-eventTimer>2000 and not clawIsUp: #been >2s and claw lowering
            #stop lift motor
            status = "GOING_TO_CUBE"
    elif status == "GOING_TO_CUBE":
        #search for markers
        m0,m1 = route.followRoute(arena.currentPos,arena.currOrientation)
        if m0 == 0 and m1 == 0:
            status = "CLAW_GRABBING"
            eventTimer = currTime
            #start grabbing
        #set motors
    elif status == "CLAW_GRABBING":










#
