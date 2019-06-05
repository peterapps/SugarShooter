from Peter import *
from Controls import Controls
from time import sleep

joy = Controls()

sol = DoubleSolenoid(21, 20, 16, 13, 26, 19)
pan = Motor(25, 24, 23)
tilt = Motor(17, 22, 27)

trigger_timer = 0
trigger_bool = False

while True:
	joy.update()
	pan.set(joy.z)
	tilt.set(joy.y)
	if joy.trigger == 1:
		trigger_bool = True
	if trigger_bool:
		if trigger_timer < 0.5:
			sol.set(1)
		elif trigger_timer < 0.8:
			sol.set(-1)
		else:
			sol.set(0)
			trigger_timer = 0
			trigger_bool = False
		trigger_timer += 0.1
	sleep(0.1)
