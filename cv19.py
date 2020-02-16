##for joining two points or for appending two points
import cv2
import numpy as np


def click_events(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 2)
            cv2.imshow('image', img)


img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()
