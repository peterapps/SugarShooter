import cv2
import numpy as np
import os

class HandDetector:
	def __init__(self):
		dir = os.path.dirname(os.path.realpath(__file__)) + '/'
		# Load Haar cascade
		self.cascade = cv2.CascadeClassifier(dir + 'cascades/palm_v4.xml')
		# Load distance calibration for hand
		data = dict()
		f = open(dir + 'calibration.txt')
		lines = f.readlines()
		for line in lines:
			key, val = line[:-1].split('=')
			data[key] = float(val)
		self.calibration = data
	
	def get_hands(self, frame):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('gray', gray)
		boxes = self.cascade.detectMultiScale(gray, 1.3, 5)
		# Normalize coordinates
		coords = []
		height, width = frame.shape[:2]
		for (x,y,w,h) in boxes:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			coord = dict()
			coord['x'] = (x + w/2) / width * 2 - 1
			coord['y'] = (y + h/2) / height * 2 - 1
			coord['w'] = w / width
			coord['h'] = h / height
			coords.append(coord)
		return frame, coords
	
	def get_position(self, frame, debug = False):
		frame, boxes = self.get_hands(frame)
		if (len(boxes) == 0): # No hands recognized
			return frame, None
		coord = boxes[0] # For now, just use the first hand seen
		# Interpret calibration data
		n_w = coord['w']
		n_h = coord['h']
		n_x = coord['x']
		n_y = coord['y']
		cal_dist = self.calibration['distance']
		cal_n_w = self.calibration['normalized_width']
		cal_n_h = self.calibration['normalized_height']
		# Calculate position
		x = n_x * self.calibration['width'] / n_w
		y = n_y * self.calibration['height'] / n_h
		dist = cal_dist * n_w / cal_n_w
		# Print debugging info
		if debug:
			print('')
			print('Normalized x: {}'.format(n_x))
			print('Normalized y: {}'.format(n_y))
			print('Normalized width: {}'.format(n_w))
			print('Normalized height: {}'.format(n_h))
			#print('Horizontal shift (m): {}'.format(x))
			#print('Vertical shift (m): {}'.format(y))
			#print('Distance (m): {}'.format(dist))
		return frame, (x, y, dist)
		
		