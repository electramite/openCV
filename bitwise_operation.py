import cv2
import numpy as np
img1 = np.zeros((512,512),np.uint8) # creating a black image with numpy zeros method
img2 = np.zeros((512,512),np.uint8)

img1 = cv2.rectangle(img1, (200,0), (312,130), (255,255,255), -1)
img1 = cv2.line(img1, (256,200), (256,300), (255,255,255), 20)

img2 = cv2.circle(img2, (256,56), 56, (255,255,255), -1)
img2 = cv2.line(img2, (206,250), (306,250), (255,255,255), 20)

img2 = cv2.bitwise_not(img2)
bitAnd = cv2.bitwise_and(img2,img1)
bitOr = cv2.bitwise_or(img2,img1)
bitXor = cv2.bitwise_xor(img2,img1)

cv2.imshow("and", bitAnd)
cv2.imshow("or", bitOr)
cv2.imshow("xor", bitXor)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()