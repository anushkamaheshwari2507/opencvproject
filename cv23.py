##for adding two images of same size otherwise resize the images
import cv2

img = cv2.imread('butterfly.jpg')
img2 = cv2.imread('apple.jpg')
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
dst = cv2.add(img, img2)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
