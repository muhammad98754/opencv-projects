import cv2 as cv
import numpy as np
img = cv.imread("lena.jpg")


hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
hstack=np.hstack([img,hsv,lab])



cv.imshow("window",hstack)
cv.waitKey(0)
cv.destroyAllWindows()
