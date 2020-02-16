##for making the random color window
import cv2
import numpy as np


def click_events(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = [x, y, 0]
        green = [x, y, 1]
        red = [x, y, 2]
        cv2.circle(img, (x, y), 3, (255, 255, 255), -1)
        colorimage = np.zeros([512, 512, 3], np.uint8)
        colorimage[:] = [blue, green, red]
        cv2.imshow('color', colorimage)


img = cv2.imread('Screenshot (96).png')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()
