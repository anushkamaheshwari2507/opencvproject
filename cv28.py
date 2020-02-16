##for thresholding the images
import cv2

img = cv2.imread('apple.jpg')
x, th1 = cv2.threshold(img, 127, 225, cv2.THRESH_BINARY)
x, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
x, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
x, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
x, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("image", img)
cv2.imshow("image1", th1)
cv2.imshow("image2", th2)
cv2.imshow("image3", th3)
cv2.imshow("image4", th4)
cv2.imshow("image5", th5)
cv2.waitKey(0)
cv2.destroyAllWindows()
