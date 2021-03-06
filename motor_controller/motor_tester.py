from gpiozero import PWMOutputDevice, DigitalOutputDevice

# Motor 1
enable = PWMOutputDevice(pin=25, frequency=500)
in1 = DigitalOutputDevice(pin=24)
in2 = DigitalOutputDevice(pin=23)

def set_motor(speed):
	enable.value = abs(speed)
	if speed > 0:
		in1.on()
		in2.off()
	elif speed < 0:
		in1.off()
		in2.on()
	else:
		in1.off()
		in2.off()

# Ask for user input
while True:
	choice = float(input('Enter a speed: '))
	set_motor(choice)
