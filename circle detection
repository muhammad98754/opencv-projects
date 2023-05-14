import cv2 as cv
import numpy as np

img=cv.imread("smarties.png")
img1=img.copy()
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray=cv.medianBlur(gray,5)

circles=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

detected_circles=np.uint16(np.around(circles))
print(detected_circles)

for (x,y,r) in detected_circles[0,:]:
    cv.circle(img1,(x,y),r,(0,255,0),3)

cv.imshow("window",img1)
cv.waitKey(0)
cv.destroyAllWindows()
