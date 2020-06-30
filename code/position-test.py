#test file
import position
import robot_obj

while True:
    markers = robot_obj.R.see()
    print(position.findPosition(markers))
    robot_obj.R.sleep(1)

    
