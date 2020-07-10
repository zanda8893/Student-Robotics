from robot_obj import R

"""
sensor:
0 = front left
1 = front right
2 = left
3 = right
4 = back left
5 = back right

Only measures up to 300mm
"""
def getDistance(sensor):
    return R.ruggeduinos[0].analogue_read(sensor) * 1000
