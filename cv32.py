##for creating the mask images
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('butterfly.jpg', 0)
x, mask = cv2.threshold(img, 200, 300, cv2.THRESH_BINARY_INV)
##for dilating the images
kernel = np.ones((5, 2), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=2)
##for eroding the images
erosion = cv2.erode(mask, kernel, iterations=1)
## for opening the images
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
## for closing the iamges
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
## for gradient of image
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
## for crossing of image
crossing = cv2.morphologyEx(mask, cv2.MORPH_CROSS, kernel)
titles = ['img', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'crossing']
images = [img, mask, dilation, erosion, opening, closing, gradient, crossing]
for i in range(8):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
