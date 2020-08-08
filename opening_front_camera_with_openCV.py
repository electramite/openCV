import cv2
cap = cv2.VideoCapture(0) # device index is 0 here. change this in case if web cam is not opening

while True:
        ret, frame = cap.read() #this will return true if frame is available and output will save in frame var
     # ret stores true(if webcam opened) frame stores the output

      # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert color to gray
      # cv2.imshow('name of the window', gray)

        cv2.imshow('name of the window', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break
cap.release() # you need to release the capture event after exiting the loop
cv2.destroyAllWindows()
