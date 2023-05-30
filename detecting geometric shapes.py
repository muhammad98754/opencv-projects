import cv2 as cv
import numpy as np


def funct(x):
    print(x)

cv.namedWindow("window")
cv.createTrackbar("value","window",0,255,funct)

img = cv.imread("OIP (2).jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gg=cv.getTrackbarPos("value","window")
_, th = cv.threshold(gray, 240, 255, 0)
contours,hierarchy=cv.findContours(th,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    #print(approx)
    cv.drawContours(img, [approx], 0, (0, 0, 0), 5)

    x = approx.ravel()[0]
    y = approx.ravel()[1]






    if len(approx) == 3:

        cv.putText(img, "traingle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)
        aspectratio = float(w) / h
        if aspectratio >= .95 and aspectratio <= .95:

            cv.putText(img, "square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))





    elif len(approx) == 5:
        cv.putText(img, "pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv.putText(img, "star", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv.putText(img, "circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
cv.imshow("window",img)
cv.waitKey(0)

cv.destroyAllWindows()
