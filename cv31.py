##for using the thresholding with the use of matplotlib
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('apple.jpg', 0)
x, th1 = cv2.threshold(img, 50, 200, cv2.THRESH_BINARY)
x, th2 = cv2.threshold(img, 50, 200, cv2.THRESH_BINARY_INV)
x, th3 = cv2.threshold(img, 200, 300, cv2.THRESH_TRUNC)
x, th4 = cv2.threshold(img, 200, 300, cv2.THRESH_TOZERO)
x, th5 = cv2.threshold(img, 200, 300, cv2.THRESH_TOZERO_INV)

title = ['original image', 'THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
    plt.show()
