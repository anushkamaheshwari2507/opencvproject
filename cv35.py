## for applying canny edge operation on the images
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('chessboard.png', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
canny = cv2.Canny(img, 100, 200)
title = ['img', 'canny']
image = [img, canny]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(image[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
