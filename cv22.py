##for print the coordinates any other place
import cv2


def click_events(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', img)


img = cv2.imread('Screenshot (96).png')
eye = img[943:283, 1049:363]
img[356:242, 486:362] = eye
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()
