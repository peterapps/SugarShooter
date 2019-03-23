import cv2
import hand
from networktables_dummy import NetworkTables

cap = cv2.VideoCapture(1)

detector = hand.HandDetector()

NetworkTables.initialize(server='10.0.41.2')
sd = NetworkTables.getTable('SmartDashboard')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('appsrc ! videoconvert ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5800', fourcc, 30, (640, 480))

while True:
	ret, frame = cap.read()
	if not ret: continue
	
	frame = cv2.resize(frame, (width, height))
	
	frame, pos = detector.get_position(frame, True)
	
	sd.putNumber('horizontal_shift', pos[0])
	sd.putNumber('vertical_shift', pos[1])
	sd.putNumber('distance', pos[2])
	
	out.write(frame)
	
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()