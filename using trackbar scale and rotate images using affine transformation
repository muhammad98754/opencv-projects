import cv2 as cv
import numpy as np

def funct(x):
    M = cv.getRotationMatrix2D(center, x, 1)

    rotated = cv.warpAffine(img, M, (w,h))

    cv.imshow("window", rotated)

def funct1(x):
    M = cv.getRotationMatrix2D(center, 0, x )

    scaled = cv.warpAffine(img, M, (w, h))
    cv.imshow("window", scaled)



img = cv.imread("lena.jpg")

img=cv.resize(img,(700,100))
print(img.shape)
print(img)
h,w=img.shape[:2]
print(h,w)
center=(w/2,h/2)




cv.imshow("window",img)
cv.createTrackbar("angle","window",0,180,funct)
cv.createTrackbar("scale","window",0,10,funct1)
cv.waitKey(0)
cv.destroyAllWindows()
