import pygame
from time import sleep

# Must be run with sudo when over SSH

pygame.display.init()
pygame.joystick.init()

# Tester for Logitech Extreme 3D Pro
joystick = pygame.joystick.Joystick(0)
joystick.init()

while True:
	pygame.event.get()
	x = joystick.get_axis(0)
	y = -joystick.get_axis(1)
	z = joystick.get_axis(2)
	lock = -joystick.get_axis(3)
	lock = 0 if lock < 0 else 1 
	trigger = joystick.get_button(0)
	print('\n' * 25)
	print('X: {:.3f}'.format(x))
	print('Y: {:.3f}'.format(y))
	print('Z: {:.3f}'.format(z))
	print('Lock: {:.3f}'.format(lock))
	print('Trigger: {}'.format(trigger))
	sleep(0.1)
