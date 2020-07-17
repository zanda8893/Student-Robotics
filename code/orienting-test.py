import orienting
from robot_obj import R
import position
from position import Position
import claw,lift



while True:
    lift.raiseLift()
    claw.openClawSync()
    lift.waitOnLift()
    orienting.approachCubeCam(38,20)
    print("Waiting...")
    R.sleep(3)
    print("Done waiting")
