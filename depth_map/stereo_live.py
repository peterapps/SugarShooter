import numpy as np
import cv2

CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240
fps = 3

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
    #print('loading images...')
    retL, frameL = left.read()
    retR, frameR = right.read()
    if not (retL and retR): continue
    imgL = cv2.pyrDown(frameL)  # downscale images for faster processing
    imgR = cv2.pyrDown(frameR)

    # disparity range is tuned for 'aloe' image pair
    window_size = 3
    min_disp = 16
    num_disp = 256-min_disp
    stereo = cv2.StereoSGBM_create(minDisparity = min_disp,
        numDisparities = num_disp,
        blockSize = 16,
        P1 = 8*3*window_size**2,
        P2 = 32*3*window_size**2,
        disp12MaxDiff = 1,
        uniquenessRatio = 20,
        speckleWindowSize = 200,
        speckleRange = 200
    )

    #print('computing disparity...')
    disp = stereo.compute(imgL, imgR).astype(np.float32) / 16.0

    #cv2.imshow('left', imgL)
    #cv2.imshow('right', imgR)
    result = (disp-min_disp)/num_disp
    result = cv2.resize(result, (640, 480))
    cv2.imshow('disparity', result)

    if cv2.waitKey(1) == ord('q'):
        break


left.release()
right.release()
cv2.destroyAllWindows()
