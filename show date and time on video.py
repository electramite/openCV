import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture(0)

cap.set(3, 1280) # 3 for CAP_PROP_FRAME_WIDTH
cap.set(4, 720) # 4 for CAP_PROP_FRAME_HEIGHT

while cap.isOpened():
    ret, frame = cap.read()

    text = "width:" + str(cap.get(3)) + " height:" + str(cap.get(4)) + " date:" + str(datetime.datetime.now())
    frame = cv2.putText(frame, text, (12,45), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,255), 2)
    cv2.imshow("name", frame)

    if cv2.waitKey(1) & 0xFF == 27 :
        break
cap.release()
cv2.destroyAllWindows()