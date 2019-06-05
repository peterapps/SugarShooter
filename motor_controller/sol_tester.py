from Peter import *

#sol = DoubleSolenoid(2, 3)
sol = DoubleSolenoidOld(21, 20, 16, 13, 26, 19)

dir = True
while True:
	input("Press enter to swap")
	dir = not dir
	print("Now using {}".format(dir))
	sol.set(1 if dir else -1)
