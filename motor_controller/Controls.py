import pygame

class Controls:
	def __init__(self):
		pygame.display.init()
		pygame.joystick.init()
		self.joystick = pygame.joystick.Joystick(0)
		self.joystick.init()
		self.x = 0
		self.y = 0
		self.z = 0
		self.lock = 0
		self.trigger = 0
	def update(self):
		pygame.event.get()
		self.x = self.joystick.get_axis(0)
		self.y = -self.joystick.get_axis(1)
		self.z = self.joystick.get_axis(2)
		lock = -self.joystick.get_axis(3)
		self.lock = 0 if lock < 0 else 1
		self.trigger = self.joystick.get_button(0)
