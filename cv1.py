##for reading any image
import cv2

img = cv2.imread('Screenshot (96).png', 1)
print(img)
cv2.imshow('image', img)
k = cv2.waitKey(9000)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    ##for writing an similar image with different name
    cv2.imwrite('anu_copy.png', img)
    cv2.destroyAllWindows()
