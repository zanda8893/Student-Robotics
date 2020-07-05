import claw
import robot_obj

#Test completed

claw.grabClaw()
print("A")
print(claw.clawIsFinished())
claw.waitOnClaw()
print("B")
"""
robot_obj.R.sleep(1)
claw.grabClawSync()
print("C")
"""
robot_obj.R.sleep(1)
claw.openClaw()
print("D")
print(claw.clawIsFinished())
claw.waitOnClaw()
print("E")
"""
robot_obj.R.sleep(1)
claw.openClawSync()
print("F")
"""
