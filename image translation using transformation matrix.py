import cv2 as cv
import numpy as np

def funct(x):
    M=np.array([[1, 0, x], [0, 1, x]],np.float32)

    translated=cv.warpAffine(img,M,(w,h))
    cv.imshow("window",translated)






img=cv.imread("lena.jpg")
w,h=img.shape[:2]
center=[w/2,h/2]





cv.imshow("window",img)
cv.createTrackbar("angle","window",0,180,funct)
cv.waitKey(0)
cv.destroyAllWindows()


