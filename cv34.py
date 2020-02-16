## for creating the laplacian image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('chessboard.png', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
## laplacian method
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
lap = np.uint8(np.absolute(lap))
##sobel method
sobel1 = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel2 = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel1 = np.uint8(np.absolute(sobel1))
sobel2 = np.uint8(np.absolute(sobel2))
##sobelcombined method
sobelcom = cv2.bitwise_or(sobel1, sobel2)
title = ['image', 'laplacian', 'sobelx', 'sobely', 'sobelcombined']
image = [img, lap, sobel1, sobel2, sobelcom]
for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(image[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
