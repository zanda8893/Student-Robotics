import time
import random
"""
this is a rough first attempt which shouldn't work
"""
class move():
	"""
	the general movement methods for the robot
	they are programmed here for easy access and to
	make it easier when implementing new ideas
	# TODO: add proper moter commands for starting and stoping to robit code branch
	"""
	"""
	this class is working on the assumption that we dont have any sensors updating the position
	once we have sensors, we can update this to get more accurete movement
	"""
	def forward(self, distance):
		#move forward code
		print("Forward class")
		print("moving",distance)
		sleep = distance / 2.2 #convert the distance into time s = d / t
		if sleep < 0: #time.sleep doent work with negative numbers so this make the numbers positive
			sleep = 0 - sleep
		moters = True #power the moters
		time.sleep(sleep)
		moters = False #stop the moters
		print("moved",distance)

	def backward(self, distance):
		#might not need this. we could use a negative number in the move.forward() function
		print("Backwards class")
		print("moving",distance)
		sleep = distance / 2.2 #convert the distance into time s = d / t (number=filler)
		if sleep < 0: #time.sleep doent work with negative numbers so this make the numbers positive
			sleep = 0 - sleep
		moters = True #power the moters in reverse
		time.sleep(sleep)
		moters = False #stop the moters
		print("moved",distance)

	def right(self, angle):
		print("right class")
		print("turning", angle, "clockwise")
		sleep = angle / 2.2 #convert the angle into time using, s = d / t (filler number)
		if sleep < 0: #time.sleep doent work with negative numbers so this make the numbers positive
			sleep = 0 - sleep
		left_moters = True #rurns right
		right_moters = False
		time.sleep(sleep)
		left_moters = False #stop the moters
		right_moters = False
		print("turned",angle , "clockwise")

	def left(self, angle):
		print("left class")
		print("turning", angle, "counterclockwise")
		sleep = angle / 2.2 #convert the angle into time using, s = d / t(numberr=filler)
		if sleep < 0: #time.sleep doent work with negative numbers so this make the numbers positive
			sleep = 0 - sleep
		left_moters = False #turns left
		right_moters = True
		time.sleep(sleep)
		left_moters = False #stop the moters
		right_moters = False
		print("turned",angle , "counterclockwise")

class sensor():
	"""
	docstring for Sensors.
	"""
	def camara(self, arg):
		pass


move = move()
test = 6
move.forward(test)
move.right(test)

#move.forward(input())
