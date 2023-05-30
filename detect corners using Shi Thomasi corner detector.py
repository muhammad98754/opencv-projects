#detect corners using Shi Thomasi corner detector(we can control the number of corners to detect)

import cv2 as cv
import numpy as np

img=cv.imread("pic1.png") #loading the image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #converting the image into grayscale mode

corners=cv.goodFeaturesToTrack(gray,100,0.01,10)
corners=np.intp(corners)  #converting the corner to integer values

for i in corners:
    x,y=i.ravel()
    cv.circle(img,(x,y),3,255,-1)

cv.imshow("window",img)

cv.waitKey(0)
cv.destroyAllWindows()
