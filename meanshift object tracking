import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap=cv.VideoCapture("slow_traffic_small.mp4")

#take first frame of video
ret,frame=cap.read()

print(frame.shape)
#setup initial location of window
x,y,w,h=300,200,100,50
trackwindow=(x,y,w,h)
#set up ROI for tracking
roi=frame[y:y+h,x:x+w]
hsv_roi=cv.cvtColor(roi,cv.COLOR_BGR2HSV)
mask=cv.inRange(hsv_roi,np.array([0.,60.,32.]),np.array([180.,255.,255.]))
roi_hist=cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
cv.imshow("roi",roi_hist)

#set up termination criteria ,either 10 iteration or move by atleast 1 pt
term_crit=(cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_COUNT,10,1)

while True:
    ret,frame=cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst=cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
    #apply mean shift to get new loaction
    ret,trackwindow=cv.meanShift(dst,trackwindow,term_crit)
    #draw it on image

    x,y,w1,h1=trackwindow
    final_image=cv.rectangle(frame,(x,y),(x+w1,y+h1),255,3)

    cv.imshow("window",final_image)
    cv.imshow("dst", dst)


    if cv.waitKey(1)== ord("q"):
        break


cap.release()
cv.destroyAllWindows()


