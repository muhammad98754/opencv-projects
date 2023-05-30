import cv2 as cv
import numpy as np
points=[]
BLACK = (0, 0, 255)
WHITE = (255,0,0 )
RED = (0, 255, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)
CYAN = (255,0,0 )
MAGENTA = (0, 255, 0)
YELLOW = (0, 255, 255)
colors = [BLACK,WHITE,RED,GREEN,BLUE,CYAN,MAGENTA,YELLOW]
img=np.zeros([512,512,3],np.uint8)
def funct1(x):
    pass

def funct2(x):
    pass

def funct3(event,x,y,flags,param):
    #img = np.zeros([512,512, 3], np.uint8)

    thick=cv.getTrackbarPos("thickness","window")
    colors_new=cv.getTrackbarPos("color","window")


    if flags==1:
        points.append((x, y))
        print(points)


        cv.polylines(img, np.array([points]),False, colors[colors_new], thick)

        cv.imshow("window", img)



img=np.zeros([512,512,3],np.uint8)


cv.imshow("window",img)
cv.createTrackbar("thickness","window",0,10,funct1)
cv.createTrackbar("color","window",0,7,funct2)
cv.setMouseCallback("window",funct3)
cv.waitKey(0)
cv.destroyAllWindows()
