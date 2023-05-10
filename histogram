import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

img=cv.imread("lena.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
histograms=cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title("histogram")
plt.xlabel("bins")
plt.ylabel("pixels")
plt.xlim([0,256])
plt.ylim([0,3000])
plt.plot(histograms)


plt.show()



cv.waitKey(0)
cv.destroyAllWindows()
