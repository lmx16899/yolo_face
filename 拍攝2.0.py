import cv2
from time import strftime
import os
labels = ['nomask','mask','3']
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, frame = cap.read()
    cv2.imshow('get pic', frame)
    keyb = cv2.waitKey(100) & 0xFF
    if keyb == 27:
        break
    elif keyb == ord('0') or keyb == ord('1') or keyb == ord('2'):
        print(keyb - 48)
        systime = strftime("%H%M%S")
        imgname = os.path.join('images/', labels[keyb - 48] + '.' + systime + '.jpg')
        cv2.imwrite(imgname, frame)
cap.release()
cv2.destroyAllWindows()
