##for making line on any image
import cv2

imp = cv2.imread('Screenshot (96).png', 1)
##just for creating lines between image coordinates matrix
imp = cv2.line(imp, (0, 0), (900, 900), (255, 0, 0), 10)
##for making arrowed line
imp = cv2.arrowedLine(imp, (0, 0), (750, 750), (255, 0, 0), 10)
cv2.imshow('imgage', imp)
cv2.waitKey(0)
cv2.destroyAllWindows()
