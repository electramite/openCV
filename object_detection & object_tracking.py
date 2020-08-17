import cv2
import numpy as np

def nothing(x):
    pass
cap = cv2.VideoCapture(0)

cv2.namedWindow("track")

cv2.createTrackbar("l_H", "track", 0, 255, nothing)
cv2.createTrackbar("l_S", "track", 0, 255, nothing)
cv2.createTrackbar("l_V", "track", 0, 255, nothing)
cv2.createTrackbar("u_H", "track", 255, 255, nothing)
cv2.createTrackbar("u_S", "track", 255, 255, nothing)
cv2.createTrackbar("u_V", "track", 255, 255, nothing)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("l_H", "track")
    l_s = cv2.getTrackbarPos("l_s", "track")
    l_v= cv2.getTrackbarPos("l_v", "track")

    u_h = cv2.getTrackbarPos("u_H", "track")
    u_s = cv2.getTrackbarPos("u_S", "track")
    u_v = cv2.getTrackbarPos("u_V", "track")


    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow('res', res)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()