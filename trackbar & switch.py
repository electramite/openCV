import cv2
import numpy as np

def nothing(): # creating a callback function
     print(x)

img = np.zeros((300,700,3), np.uint8) # creating a black image with numpy zeros method

cv2.namedWindow("image")
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)
switch = '0:off\n 1:on'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    b = cv2.getTrackbarPos('B', 'image') # storing readings of the trackbar
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0: # if switch will off then black image will be displayed
        img[:] = [0] # all the 3 channels of the img will 0
    else: # if switch will on then color of the image will be shown accordingly
        img[:] = [b,g,r] # fetching the readings to the 3 channels of img
    cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()