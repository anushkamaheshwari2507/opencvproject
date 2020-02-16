##for setting events
import cv2

event = [i for i in dir(cv2) if 'EVENT' in i]
print(event)


def click_events(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        ##for another event
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ' , ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (255, 255, 255), 2)
        cv2.imshow('image', img)
        ##for any black image coordinates can be found ny using numpy


##img = np.zeros((512,512,3), np.uint8)
##coordinates can also be found of any image
img = cv2.imread('Screenshot (96).png')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()
