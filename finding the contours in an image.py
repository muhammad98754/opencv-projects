import cv2 as cv
import numpy as np

img=cv.imread("opencv-logo-white.png")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,th=cv.threshold(gray,127,255,0)

contours,hierarchy=cv.findContours(th,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(len(contours))
cv.drawContours(img,contours,-1,(0,255,0),3)
cv.imshow("window",img)
cv.waitKey(0)
cv.destroyAllWindows()
