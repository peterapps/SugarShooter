import cv2
import hand

cap = cv2.VideoCapture(1)

cWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
height = 480
width = int(cWidth * height / cHeight)

detector = hand.HandDetector()

while True:
	ret, frame = cap.read()
	if not ret: continue
	
	frame = cv2.resize(frame, (width, height))
	
	frame, pos = detector.get_position(frame, True)
	
	cv2.imshow('frame', frame)
	
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()