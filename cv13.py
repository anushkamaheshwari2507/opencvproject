##for making geomectric shapes
import cv2
import numpy as np

img = cv2.imread('Screenshot (96).png', 1)
##for making the whole image as black
img = np.zeros([512, 512, 3], np.uint8)
##for making rectangle in image with different starting and ending coordinates
img = cv2.rectangle(img, (0, 0), (300, 300), (0, 0, 255), 10)
##for filling the rectangle completely
img = cv2.rectangle(img, (0, 0), (300, 300), (0, 0, 255), -1)
## for making circle in image with different starting and ending coordinates
img = cv2.circle(img, (300, 300), 34, (0, 255, 0), -1)
## for writing text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'anushka', (300, 300), font, 4, (255, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
