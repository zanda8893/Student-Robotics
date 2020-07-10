import drive, robot_obj
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
        drive.driveRotateToAngle(0)
        robot_obj.R.sleep(0.9)
        drive.driveStraightSync(50,2.35)
        drive.driveRotateAngle(90)
        drive.driveRotateToAngle(89)
        robot_obj.R.sleep(0.9)
        drive.driveStraightSync(60,2)
        """
        if robot_obj.R.ruggeduinos[0].digital_read(4) == False:
            drive.driveStraightSync(-60,2)
            goToCube("test")
        else:
            pass
        """
