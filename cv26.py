## for applying the bitwise operartions on images of gray scale
import cv2
import numpy as np

img = np.zeros((255, 255, 3), np.uint8)
img = cv2.rectangle(img, (0, 0), (125, 125), (255, 255, 255), -1)
img2 = cv2.imread('chessboard.png')
img2 = cv2.resize(img2, (255, 255))
cv2.imshow("abhi", img2)
bitAND = cv2.bitwise_and(img, img2)
bitNOT = cv2.bitwise_not(img2)
bitOR = cv2.bitwise_or(img, img2)
bitXOR = cv2.bitwise_xor(img, img2)
cv2.imshow("anu", img)
cv2.imshow("img", bitAND)
cv2.imshow("img1", bitNOT)
cv2.imshow("img2", bitOR)
cv2.imshow("img3", bitXOR)
cv2.waitKey(0)
cv2.destroyAllWindows()
