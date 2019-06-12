from Peter import *
from Controls import *
from time import sleep
from gpiozero import PWMOutputDevice

joy = Controls()

sol = DoubleSolenoid(21, 20, 16, 13, 26, 19)
tilt = Motor(25, 24, 23)
pan = PWMOutputDevice(pin=12, frequency=500)

#comp = Compressor(12, 5)
#comp.start()

trigger_timer = 0
trigger_bool = False

while True:
	#comp.update()
	joy.update()
	if joy.z > 0.7: pan.value = 0.77
	elif joy.z < -0.7: pan.value = 0.68
	else: pan.value = 0
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
