import cv2 as cv #importing opencv library
import numpy as np #importing numpy library

define_cascade_face=cv.CascadeClassifier("haarcascade_frontalface_default (1).xml") #define the classifier first,here it is a face classifier
define_cascade_eye=cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml") # define the eye classifier for eye detection
#classifiers can be downloaded from github
#img=cv.imread("lena.jpg") #load the image
cap=cv.VideoCapture(0) #load the video using device index
while True:
    _, img = cap.read() #load the frame by frame
    gray = cv.cvtColor(img,
                       cv.COLOR_BGR2GRAY)  # classifiers will work with grayscale image thats why we convert the original image to grayscale image
    faces = define_cascade_face.detectMultiScale(gray, 1.1, 4)  # detecting the faces in the image


    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3) #draw the rectangle around the faces
        roi_gray=gray[y:y+h,x:x+w] #finding the gray scale region of ineterst
        roi_color = img[y:y + h, x:x + w]  # finding the colored region of interest
        eyes = define_cascade_eye.detectMultiScale(roi_gray)  # detecting the eyes in the image
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 3)  # draw the rectangle around the eyes


    cv.imshow("window", img) #show the original image with detected faces using Haar cascade classifier

    if cv.waitKey(1)==ord("q"):
        break



cv.waitKey(0)
cv.destroyAllWindows()
