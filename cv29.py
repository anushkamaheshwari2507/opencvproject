## for adaptive thresholding
import cv2

img = cv2.imread('Screenshot (96).png', 0)
img = cv2.resize(img, (255, 255))
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("image1", img)
cv2.imshow("image", th1)
cv2.imshow("3", th2)
cv2.waitKey(0)
cv2.destroyAllWindows()
