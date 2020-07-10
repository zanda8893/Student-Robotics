import drive
import robot_obj
#Co ordinates for cubes

"""s
drive.driveRotateAngle(0)
robot_obj.R.sleep(0.9)
drive.driveStraightSync(60,10)
robot_obj.R.sleep(0.9)
drive.driveRotateSync(50,0.7)
robot_obj.R.sleep(0.9)
drive.driveStraightSync(75,3.4)
"""





def goToCube(p):
    if p == "test":
        print("Rotate")
        drive.driveRotateAngle(-45)
