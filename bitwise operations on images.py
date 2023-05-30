import cv2 as cv
import numpy as np

a=np.zeros([300,300],np.uint8)
b=np.copy(a)
rectangle=cv.rectangle(a,(150,150),(300,300),255,5)
circle=cv.circle(b,(200,200),50,255,5)
xors=cv.bitwise_xor(a,b)
ors=cv.bitwise_or(a,b)
ands=cv.bitwise_and(a,b)
res=np.hstack([xors,ands,ors])
cv.imshow("window",res)

cv.waitKey(0)
cv.destroyAllWindows()
