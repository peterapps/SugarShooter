from gpiozero import PWMOutputDevice, Servo, DigitalOutputDevice
from time import sleep

talon = PWMOutputDevice(pin=12, frequency=500)
#talon = Servo(pin=12)
#talon = DigitalOutputDevice(pin=12)

while True:
	val = float(input("Enter a value: "))
	talon.value = val
	#talon.on()
	#sleep(2.0/1000)
	#talon.off()
