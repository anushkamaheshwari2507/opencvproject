##lower and upper resolutions of any image
import cv2

img = cv2.imread('lena.jpg')
lr = cv2.pyrDown(img)
lr1 = cv2.pyrDown(lr)
ur = cv2.pyrUp(lr1)
cv2.imshow('image1', lr)
cv2.imshow('image2', lr1)
cv2.imshow('imag3', ur)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
