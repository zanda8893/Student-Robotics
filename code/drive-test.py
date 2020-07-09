from drive import *
from robot_obj import R

#Tests done

def timestamp(s):
    print(s + " at {0}".format(R.time()))

timestamp("A")
driveStraight(60)
timestamp("B")
driveStraight(0)
timestamp("C")

kill()
