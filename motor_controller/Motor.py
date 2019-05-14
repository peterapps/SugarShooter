from gpiozero import PWMOutputDevice, DigitalOutputDevice

# Class for the L298N motor controller board
class Motor:
	def __init__(self, enable_pin, in1_pin, in2_pin):
		self.enable = PWMOutputDevice(pin=enable_pin, frequency=500)
		self.in1 = DigitalOutputDevice(pin=in1_pin)
		self.in2 = DigitalOutputDevice(pin=in2_pin)

	def set(self, speed):
		self.enable.value = abs(speed)
		if speed > 0:
			self.in1.on()
			self.in2.off()
		elif speed < 0:
			self.in1.off()
			self.in2.on()
		else:
			self.in1.off()
			self.in2.off()

