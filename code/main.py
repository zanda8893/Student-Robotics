
#initialize things
clawIsUp = False
eventTimer = -1 #used to time events

while True:
    if status == "IDLE":
        status = "CUBES_SEARCHING"
<<<<<<< HEAD
    elif status == "CUBES_SEARCHING":
=======
    else if status == "CUBES_SEARCHING":
        print("Searching for cubes...")
>>>>>>> b96f070ec5d3eb1f59eecc0771c15b6f57b3a0b4
        #search for markers
        if arena.availableCubes() == 0: #no available cubes
            print("Couldn't find any cubes")
            status = "CUBES_ROTATING"
            #---set motors to rotating slowly---
        else:
            print("Found a cube!")
            currentCube = arena.getBestCube()
            status = "CUBES_ROUTING"
<<<<<<< HEAD
    elif status == "CUBES_ROTATING":
=======
    else if status == "CUBES_ROTATING":
        print("Rotating in the hope of finding a cube...")
>>>>>>> b96f070ec5d3eb1f59eecc0771c15b6f57b3a0b4
        #stop motors
        time.sleep(0.1)
        #search for cubes
        if arena.availableCubes() != 0:
            print("Found a cube!")
            currentCube = arena.getBestCube()
            status = "CUBES_ROUTING"
            #---stop motors---
<<<<<<< HEAD
    elif status == "CUBES_ROUTING":
=======
    else if status == "CUBES_ROUTING":
        print("Trying to find a route to the cube")
>>>>>>> b96f070ec5d3eb1f59eecc0771c15b6f57b3a0b4
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
