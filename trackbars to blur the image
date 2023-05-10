import cv2 as cv
import numpy as np

def funct(x):
    a=cv.getTrackbarPos("a","window")
    bb=cv.getTrackbarPos("a","window")
    blurr=cv.blur(img,(a,bb))
    cv.imshow("window",blurr)







img=cv.imread("lena.jpg")

cv.imshow("window",img)
cv.createTrackbar("a","window",1,10,funct)
cv.createTrackbar("b","window",1,10,funct)
cv.waitKey(0)
cv.destroyAllWindows()
