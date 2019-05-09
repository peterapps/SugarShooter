import numpy as np
import cv2
from time import sleep

frameL = cv2.imread('left.jpg')
frameR = cv2.imread('right.jpg')
cv2.imshow('left', frameL)
cv2.imshow('right', frameR)
imgL = cv2.pyrDown(frameL)  # downscale images for faster processing
imgR = cv2.pyrDown(frameR)

wnd = 'controls'
cv2.namedWindow(wnd)

ready = False

def update(*args):
    if not ready: return
    # disparity range is tuned for 'aloe' image pair
    window_size = cv2.getTrackbarPos('Window Size', wnd)
    min_disp = cv2.getTrackbarPos('Minimum disparity', wnd)
    num_disp = 112-min_disp
    stereo = cv2.StereoSGBM_create(minDisparity = min_disp,
        numDisparities = num_disp,
        blockSize = cv2.getTrackbarPos('Block size', wnd),
        P1 = cv2.getTrackbarPos('Smoothness 1', wnd) * 3*window_size**2,
        P2 = cv2.getTrackbarPos('Smoothness 2', wnd) * 3*window_size**2,
        disp12MaxDiff = cv2.getTrackbarPos('Allowed difference', wnd),
        uniquenessRatio = cv2.getTrackbarPos('Uniqueness', wnd),
        speckleWindowSize = cv2.getTrackbarPos('Speckle size', wnd),
        speckleRange = cv2.getTrackbarPos('Speckle range', wnd)
    )

    #print('computing disparity...')
    disp = stereo.compute(imgL, imgR).astype(np.float32) / 16.0

    #cv2.imshow('left', imgL)
    #cv2.imshow('right', imgR)
    result = (disp-min_disp) / num_disp
    cv2.imshow('disparity', result)
    sleep(1)
    if cv2.waitKey(1) == ord('q'):
        left.release()
        right.release()
        cv2.destroyAllWindows()
        exit(0)

cv2.createTrackbar('Window Size', wnd, 3, 15, update) # 3
cv2.createTrackbar('Minimum disparity', wnd, 0, 100, update) # 16
cv2.createTrackbar('Number of disparities', wnd, 0, 256, update) # 112
cv2.createTrackbar('Block size', wnd, 1, 32, update) # 16
cv2.createTrackbar('Smoothness 1', wnd, 1, 100, update) # 8
cv2.createTrackbar('Smoothness 2', wnd, 1, 100, update) # 32
cv2.createTrackbar('Allowed difference', wnd, -1, 50, update) # 1
cv2.createTrackbar('Uniqueness', wnd, 1, 20, update) # 10
cv2.createTrackbar('Speckle size', wnd, 0, 200, update) # 100
cv2.createTrackbar('Speckle range', wnd, 1, 200, update) # 32

cv2.setTrackbarPos('Window Size', wnd, 3)
cv2.setTrackbarPos('Minimum disparity', wnd, 16)
cv2.setTrackbarPos('Number of disparities', wnd, 112)
cv2.setTrackbarPos('Block size', wnd, 16)
cv2.setTrackbarPos('Smoothness 1', wnd, 8)
cv2.setTrackbarPos('Smoothness 2', wnd, 32)
cv2.setTrackbarPos('Allowed difference', wnd, 1)
cv2.setTrackbarPos('Uniqueness', wnd, 10)
cv2.setTrackbarPos('Speckle size', wnd, 100)
cv2.setTrackbarPos('Speckle range', wnd, 32)

ready = True
update()
while True:
    cv2.waitKey(1)
