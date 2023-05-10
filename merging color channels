import cv2 as cv
import numpy as np

img=cv.imread("lena.jpg")
print(img.shape[:2])

a=np.zeros((img.shape[0],img.shape[1]),np.uint8)


b,g,r=cv.split(img)



blue=cv.merge([b,a,a])
green=cv.merge([a,b,a])
red=cv.merge([a,a,b])
aa=np.hstack([blue,green,red])



cv.imshow("window",aa)
cv.waitKey(0)
cv.destroyAllWindows()
