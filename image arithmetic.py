import cv2 as cv
import numpy as np
img = cv.imread('lena.jpg')
print(img.shape)
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
M = np.ones(img.shape, dtype='uint8') *42
print(M.shape)
brighter = cv.add(img, M)
print(brighter)
darker = cv.subtract(img, M)
print(darker)
img2 = np.hstack([img, brighter, darker])
cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()
