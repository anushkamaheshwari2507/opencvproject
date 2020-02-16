## for creating the binary image
import cv2 as cv

img = cv.imread('lena.jpg', 2)
cv.imshow('image', img)
x, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
cv.imshow('binary image', th1)
cv.waitKey(0)
cv.destroyAllWindows()
