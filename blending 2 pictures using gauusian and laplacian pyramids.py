import cv2 as cv
import numpy as np

img1=cv.imread("apple.jpg")
img2=cv.imread("orange.jpg")

#create gaussian pyramids

g1=img1.copy()
g2=img2.copy()

gp1=[g1]
gp2=[g2]

for i in range(6):
    g1=cv.pyrDown(g1)
    gp1.append(g1)
    g2=cv.pyrDown(g2)
    gp2.append(g2)



#create laplacian pyramid
lp1=[gp1[5]]
lp2=[gp2[5]]
for i in range(5,0,-1):

    s=cv.pyrUp(gp1[i])
    laplacian=cv.subtract(gp1[i-1],s)
    lp1.append(laplacian)

    s=cv.pyrUp(gp2[i])
    laplacian=cv.subtract(gp2[i-1],s)
    lp2.append(laplacian)



#image blending

blend_pyramid=[]
for lap1,lap2 in zip(lp1,lp2):
    height,width,channels=lap1.shape
    blend_pyramid.append(np.hstack([lap1[:,0:width//2],lap2[:,width//2:]]))

#from the blended pyramids we reconstruct the final image by add()

reconstruct=blend_pyramid[0]
for i in range(1,6):
    reconstruct=cv.pyrUp(reconstruct)
    reconstruct=cv.add(reconstruct,blend_pyramid[i])


cv.imshow("window",reconstruct)


cv.waitKey(0)
cv.destroyAllWindows()
