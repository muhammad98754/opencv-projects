import cv2 as cv
import numpy as np


img=np.zeros([512,512,3],np.uint8)
points=np.array([[0,0],[200,400],[500,30]])
#cv.polylines(img,points[np.newaxis,:,:],True,(0,0,255),5)
cv.fillPoly(img,points[np.newaxis,:,:],(0,255,0))
cv.imshow("window",img)
cv.waitKey(0)
cv.destroyAllWindows()
