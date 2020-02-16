##for setting the width and heigth of any particular frame
import cv2

cap = cv2.VideoCapture(0);
##saving the capturing video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('anu.avi', fourcc, 20.0, (640, 480))
cap.set(3, 400);
cap.set(4, 400);
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while (True):
    ret, frame = cap.read()
    ##for capturing the video on gray scale
    ## gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
