import lift
import robot_obj

#Done tests

print("Started at {0}".format(robot_obj.R.time()))
lift.raiseLift()
print(lift.liftIsFinished())
lift.waitOnLift()
print("Finished at {0}".format(robot_obj.R.time()))
lift.lowerLift()
print(lift.liftIsFinished())
lift.waitOnLift()
