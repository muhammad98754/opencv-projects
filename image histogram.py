import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("lena.jpg",0)

#img=np.zeros([200,200],np.uint8)
#cv.rectangle(img,(0,100),(200,200),255,-1)
#cv.rectangle(img,(0,50),(100,100),127,-1)

#b,g,r=cv.split(img)



hist=cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
#plt.hist(b.ravel(),256,[0,256])
#plt.hist(g.ravel(),256,[0,256])
#plt.hist(r.ravel(),256,[0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
