import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	if not ret: continue
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
