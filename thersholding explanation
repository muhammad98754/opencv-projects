import cv2 as cv
import numpy as np


img=cv.imread("lena.jpg")
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,img1=cv.threshold(img,127,200,cv.THRESH_BINARY) #all pixel values < 127 set to 0. and all pixel values >127 set to 200
ret,img2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV) #all pixel values < 127 set to 255. and all pixel values >127 set to 0
ret,img3=cv.threshold(img,127,200,cv.THRESH_TRUNC) #all pixel values < 127 remain the same as before. and all pixel values >127 set to 127
ret,img4=cv.threshold(img,127,200,cv.THRESH_TOZERO) #all pixel values < 127 set to 0. and all pixel values >127  remain the same as before
ret,img5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)  #all pixel values < 127 remain the same as before. and all pixel values  >127 set to 0






cv.imshow("window",img1)
cv.imshow("img2",img2)
cv.imshow("img3",img3)
cv.imshow("img4",img4)
cv.imshow("img5",img5)
cv.waitKey(0)
cv.destroyAllWindows()
