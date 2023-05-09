import cv2 as cv
import numpy as np
RED = (0, 0, 255)
pts = [(0, 0), (400, 400), (400, 10)]
img =  np.zeros((500, 500, 3), np.uint8)
cv.polylines(img, np.array(pts)[np.newaxis,:,:], True, RED, 5)
print(np.array([[[0,0],[400,400],[400,10]]]))
cv.imshow('window', img)
cv.waitKey(0)
cv.destroyAllWindows()
