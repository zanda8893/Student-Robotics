import ultrasound
import time

while True:
    print(ultrasound.getDistance(0),ultrasound.getDistance(1))
    time.sleep(1)
