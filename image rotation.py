import cv2 as cv
import numpy as np

def funct(x):
    M=cv.getRotationMatrix2D(center,x,1)

    rotated=cv.warpAffine(img,M,(w,h))
    cv.imshow("window",rotated)






img=cv.imread("lena.jpg")
h,w=img.shape[:2]
center=[w/2,h/2]





cv.imshow("window",img)
cv.createTrackbar("angle","window",0,180,funct)
cv.waitKey(0)
cv.destroyAllWindows()


