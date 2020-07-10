import orienting
from robot_obj import R


while True:
    orienting.approachCube()
    print("Waiting...")
    R.sleep(3)
    print("Done waiting")
