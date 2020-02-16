## for cropping the image
import cv2

img = cv2.imread('box_in_scene.png')
image = img[10:120, 200:300]
cv2.imshow('image1', img)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
