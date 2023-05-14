#Background Subtraction Methods (subtracting the foreground from background frames to detect moving objects)

import cv2 as cv
import numpy as np

cap=cv.VideoCapture("vtest.avi")
#kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3)) #define the kernel
#fgbg=cv.bgsegm.createBackgroundSubtractorMOG() #background subtraction method
#fgbg=cv.createBackgroundSubtractorMOG2(detectShadows=False)
#fgbg=cv.bgsegm.createBackgroundSubtractorGMG()
fgbg=cv.createBackgroundSubtractorKNN(detectShadows=False)
while True:
    _,frame=cap.read()

    fgmask=fgbg.apply(frame) # getting foreground mask
    #fgmask=cv.morphologyEx(fgmask,cv.MORPH_OPEN,kernel) #apply morphological opening method to reduce the noises



    cv.imshow("window",frame)
    cv.imshow("fgmask", fgmask)

    if cv.waitKey(1)==ord("q"):
        break



cap.release()
cv.destroyAllWindows()
