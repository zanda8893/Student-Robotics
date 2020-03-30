from sr.robot import *

class TheRealRuggeduino(Ruggeduino):
    def setupUltrasound(pulsePin,echoPin):
        with self.lock:
            self.command('s'+self._encode_pin(pulsePin)+self._encode_pin(echoPin))
    def getDistance():
        with self.lock:
            d = int(self.command('u'))
            if d > 400:
                return False
            else:
                return d
