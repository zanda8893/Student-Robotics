import lift
import robot_obj

#Done tests

while True:
    print("Lifting")
    lift.raiseLiftSync()
    print("Done")
    robot_obj.R.sleep(2)
    print("Lowering")
    lift.lowerLiftSync()
    print("Done")
    robot_obj.R.sleep(2)
