import cv2 as cv
import numpy as np

img=cv.imread("messi5.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img1=cv.imread("img.png",0)
res=cv.matchTemplate(gray,img1,cv.TM_CCOEFF_NORMED)
#print(res)
w,h=img1.shape[::-1]
threshold=0.95
loc=np.where(res>=threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0),2)

cv.imshow("widnow",img)

cv.waitKey(0)
cv.destroyAllWindows()
