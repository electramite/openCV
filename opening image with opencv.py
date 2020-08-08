import cv2

var = cv2.imread('img.jpg', -1)  # -1 flag because we are going to load img as it is includng channels
cv2.imshow('name of the window', var)
while True:

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()