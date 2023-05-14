import cv2 as cv #importing opencv library
import numpy as np #importing numpy library

define_cascade=cv.CascadeClassifier("haarcascade_frontalface_default (1).xml") #define the classifier first,here it is a face classifier
#classifiers can be downloaded from github
img=cv.imread("lena.jpg") #load the image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #classifiers will work with grayscale image thats why we convert the original image to grayscale image
faces = define_cascade.detectMultiScale(gray, 1.1, 4) #detect the faces

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)



cv.imshow("window", img)



cv.waitKey(0)
cv.destroyAllWindows()
