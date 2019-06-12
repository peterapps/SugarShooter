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

class ControlsKey:
	def __init__(self):
		pygame.init()
		pygame.display.init()
		self.x = 0
		self.y = 0
		self.z = 0
		self.lock = 0
		self.trigger = 0
	def update(self):
		pygame.event.get()
		keys = pygame.key.get_pressed()
		# Pan
		if keys[pygame.K_LEFT]: self.x = 1
		elif keys[pygame.K_RIGHT]: self.x = -1
		else: self.x = 0
		# Tilt
		if keys[pygame.K_UP]: self.y = 1
		elif keys[pygame.K_DOWN]: self.y = -1
		else: self.y = 0
		# Trigger
		if keys[pygame.K_SPACE]: self.trigger = 1
		else: self.trigger = 0
