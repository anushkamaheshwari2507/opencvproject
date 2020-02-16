## importing matplot library
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('apple.jpg', 1)
cv2.imshow('image', img)
##USING CVTCOLOR U CAN ALSO MAKE MATPLOTLIB IMAGE AS COLORED IMAGE
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
## fro representing the image without any coordinates
plt.xticks([])
plt.yticks([])
plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
