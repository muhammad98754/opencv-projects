import cv2 as cv
import numpy as np

points=[]
def mouse(event, x, y, flags, param):
    #img = np.zeros((100, 500, 3), np.uint8)
    if flags==1:
        points.append((x,y))
        if len(points)>=2:
            cv.line(img, points[-2], points[-1], (0, 0, 255), 5)
            cv.imshow('window', img)
            print(points)
            points.clear()

img = np.zeros((100, 500, 3), np.uint8)

cv.imshow('window', img)
cv.setMouseCallback('window', mouse)
cv.waitKey(0)
cv.destroyAllWindows()
