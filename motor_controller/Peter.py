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
# Using L298N
class DoubleSolenoid:
	def __init__(self, enA, inA1, inA2, enB, inB1, inB2):
		self.sol1 = Motor(enA, inA1, inA2)
		self.sol2 = Motor(enB, inB1, inB2)
	def set(self, dir):
		if dir == 1:
			self.sol1.set(1)
			self.sol2.set(0)
		elif dir == -1:
			self.sol1.set(0)
			self.sol2.set(1)
		else:
			self.sol1.set(0)
			self.sol2.set(0)

# Using Spike
class DoubleSolenoidSpike:
	def __init__(self, signal1, signal2):
		self.sol1 = PWMOutputDevice(pin=signal1, frequency=500)
		self.sol2 = PWMOutputDevice(pin=signal2, frequency=500)
	def set(self, dir):
		if dir == 1:
			self.sol1.value = 1.0
			self.sol2.value = 0.5
		elif dir == -1:
			self.sol1.value = 0.5
			self.sol2.value = 1.0
		else:
			self.sol1.value = 0.0
			self.sol2.value = 0.0
