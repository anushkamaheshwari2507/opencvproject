## for homogeneous filtering out the image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Screenshot (96).png', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5, 5), np.float32) / 25
##for filtering
dst = cv2.filter2D(img, -1, kernel)
##for bluring
blur = cv2.blur(img, (5, 5), kernel)
## for gaussian blur method
gblur = cv2.GaussianBlur(img, (5, 5), 0)
## for median filter method
median = cv2.medianBlur(img, 5)
## for bilateral filter method
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
title = ['imgage', '2D CONVOLUTION', 'BLUR', 'gaussian blur', 'median filter', 'Bilateral filter']
images = [img, dst, blur, gblur, median, bilateral]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
