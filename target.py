class target:

    def __init__(self):
        position = []
        nextpossition = []

    def update(currentor, targetor, self): #Takes current orientation of the robot/target relative to area
        if currentor == targetor:
            return 0
        else:
            adjustment = currentor - targetor
            if adjustment < 0:
                R.motors[0].m0.power = motors.currentleft-adjustment #Motor 0 presumed left
            elif adjustment > 0:
                R.motors[1].m0.power = motors.currentright-adjustment #Motor 1 presumed right
            return 0

    def getDistence(currentpos, targetpos, self):
