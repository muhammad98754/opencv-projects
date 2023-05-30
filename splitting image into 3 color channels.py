import cv2 as cv
import numpy as np

img=cv.imread("lena.jpg")

b,g,r=cv.split(img)

a=np.hstack([b,g,r])



cv.imshow("window",a)
cv.waitKey(0)
cv.destroyAllWindows()
