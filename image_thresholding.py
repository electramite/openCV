import cv2
import numpy as np
img = cv2.imread('gredient.png', 0)

_, th1 = cv2.threshold(img, 27, 155, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 27, 155, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

cv2.imshow("img",img)
cv2.imshow("BINRY", th1)
cv2.imshow("BINARY_INV", th2)
cv2.imshow("TRUNC", th3)
cv2.imshow("TOZERO", th4 )
cv2.waitKey(0)
cv2.destroyAllWindows()
