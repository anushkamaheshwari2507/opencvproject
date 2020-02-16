##for showing the width and height on the frame
import datetime

import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('anu.avi', fourcc, 20.0, (640, 480))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 3000)
cap.set(4, 3000)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'width' + str(cap.get(3)) + "  " + 'height' + str(cap.get(4))
        ##for showing current date and time
        time = 'time : ' + str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10, 20), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, time, (50, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
