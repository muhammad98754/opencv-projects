import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

img=cv.imread("lena.jpg")
split=cv.split(img)
channels=["b","g","r"]

for i,j in zip(split,channels):
    aa=cv.calcHist([i],[0],None,[256],[0,256])
    #plt.figure()
    plt.xlim([0,256])
    plt.ylim([0,3000])
    plt.plot(aa,color=j)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
