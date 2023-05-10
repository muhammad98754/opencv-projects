import cv2 as cv
import numpy as np

img=cv.imread("lena.jpg")
print(img.dtype)

mask=np.zeros(img.shape[:2],np.uint8)
print(mask.dtype)
cv.circle(mask,(200,100),50,255,-1)

ands=cv.bitwise_and(img,img,mask=mask)
print(ands.dtype)
stacks=np.hstack([img,ands])
cv.imshow("window",stacks)
cv.waitKey(0)
cv.destroyAllWindows()
