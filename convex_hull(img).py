import cv2
import numpy as np
img = cv2.imread('hand.jpg', 0)
#img1 = np.zeros([512,512,3], np.uint8)
img = cv2.resize(img, (512, 512))
ret, th = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
cnt, her = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
hull = [cv2.convexHull(c) for c in cnt]
ges = cv2.drawContours(img, hull, -1, (255,0,0))
#cv2.drawContours(img1, cnt, -1, (255,0,0))
cv2.imshow('hand', img)
cv2.imshow('thresh', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
