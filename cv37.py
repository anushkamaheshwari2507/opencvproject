## for making the lower resolution pyramid
import cv2

img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]
for i in range(4):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)
cv2.imshow('original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
