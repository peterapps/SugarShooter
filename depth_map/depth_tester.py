import cv2
from time import sleep

capL = cv2.VideoCapture(0)
capR = cv2.VideoCapture(1)

for cap in [capL, capR]:
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)
	cap.set(cv2.CAP_PROP_FPS, 15)

sleep(2)


while True:
	ret1, imgL = capL.read()
	ret2, imgR = capR.read()
	if not ret1 or not ret2: continue
	cv2.imshow('left', imgL)
	cv2.imshow('right', imgR)

	imgL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
	imgR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

	stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
	disparity = stereo.compute(imgL, imgR)
	cv2.imshow('depth', disparity)
	if cv2.waitKey(1) == ord('q'):
		break

capL.release()
capR.release()
cv2.destroyAllWindows()
