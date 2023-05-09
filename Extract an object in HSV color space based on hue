import cv2 as cv
import numpy as np
img = cv.imread('lena.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
def trackbar(x):
    lower = (x, 30, 30)
    upper = (x + 5, 250, 250)
    mask = cv.inRange(hsv, lower, upper)
    img2 = cv.bitwise_and(img, img, mask=mask)
    cv.imshow('window', img2)

cv.imshow('window', img)
cv.createTrackbar('hue', 'window', 0, 179, trackbar)
cv.waitKey(0)
cv.destroyAllWindows()
