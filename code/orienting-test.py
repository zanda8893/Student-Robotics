import orienting
from robot_obj import R
import position
from position import Position


p,a = position.getPosition()
print(orienting.getPre(p,Position(1975,1975),0))
print(orienting.getPre(p,Position(2455,2875),45))

"""
while True:
    orienting.approachCube()
    print("Waiting...")
    R.sleep(3)
    print("Done waiting")
"""
