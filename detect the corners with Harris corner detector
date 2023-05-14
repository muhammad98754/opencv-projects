import cv2 as cv
import numpy as np

img=cv.imread("chessboard.png") #loading the chessboard image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #converting the image into grayscale mode

gray=np.float32(gray) #harris corner detector method takes the grayscale image in the float32 format
dst=cv.cornerHarris(gray,2,3,0.04)
dst=cv.dilate(dst,None) #dilating the output

img[dst > 0.01 * dst.max()] = [0,0,255] #reverting back to original image with optimal thrshold value


cv.imshow("window",img)

cv.waitKey(0)
cv.destroyAllWindows()
