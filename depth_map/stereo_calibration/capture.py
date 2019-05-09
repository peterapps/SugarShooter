import cv2

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
fps = 10

# TODO: Use more stable identifiers
left = cv2.VideoCapture(0)
right = cv2.VideoCapture(1)

# Increase the resolution
left.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
left.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
left.set(cv2.CAP_PROP_FPS, fps)
right.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
right.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
right.set(cv2.CAP_PROP_FPS, fps)

# Use MJPEG to avoid overloading the USB 2.0 bus at this resolution
left.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
right.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

while True:
    retL, frameL = left.read()
    retR, frameR = right.read()
    if not (retL and retR): continue
    cv2.imshow('left', frameL)
    cv2.imshow('right', frameR)

    k = cv2.waitKey(1)
    if k == ord('c'):
        cv2.imwrite('left.jpg', frameL)
        cv2.imwrite('right.jpg', frameR)
    if k == ord('q'):
        break


left.release()
right.release()
cv2.destroyAllWindows()
