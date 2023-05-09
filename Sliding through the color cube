import cv2 as cv
import numpy as np
def trackbar(x):

    img[:, :, 2] = x
    print(img)

    cv.imshow('window', img)
img = np.zeros((256, 256, 3), dtype=np.uint8)
print(img)
print('d')
for i in range(256):

    img[i,:,0]=i
    img[:, i, 1] = i


cv.imshow('window', img)
cv.createTrackbar('red', 'window', 0, 255, trackbar)
cv.waitKey(0)
cv.destroyAllWindows()
