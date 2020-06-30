#test file
import position
import robot_obj

while True:
    markers = robot_obj.R.see()
    print(findPosition(markers))
    robot_obj.R.sleep(1)

    
