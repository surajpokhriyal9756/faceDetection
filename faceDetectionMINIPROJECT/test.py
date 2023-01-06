# pip install opencv-python
#haarcascade_frontalface_default.xml

import cv2

cascade_face = cv2.CascadeClassifier('fdc.xml')

cap = cv2.VideoCapture(0)

while True:
    rect , img= cap.read()
    print(rect)
    g = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    f=cascade_face.detectMultiScale(g,1.3,5)

    for(x,y,w,h) in f:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)


    cv.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()