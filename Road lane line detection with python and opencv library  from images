#Road lane line detection with python and opencv library

import cv2 as cv  #import opencv library
import numpy as np #import numpy library
import matplotlib.pyplot as plt #import matplotlib library

#create a function to mask every region other than the region_of_interest
def region_of_interest(image,vertices):
    mask=np.zeros_like(image)
    #channel_count=image.shape[2] #retrive number of color channels
    match_mask_color=255
    cv.fillPoly(mask,vertices,match_mask_color)
    masked_image=cv.bitwise_and(image,mask)#return the image only where the mask pixel matches with the image
    return masked_image

#function to draw lines on edges
def drawlines(img,lines):
    img=np.copy(img)
    blank_image=np.zeros([img.shape[0],img.shape[1],3],np.uint8) #create blank image with same shape as that of original image
    for line in (lines):

        for x1,y1,x2,y2 in line:

            cv.line(blank_image,(x1,y1),(x2,y2),(255,0,0),4)
    img=cv.addWeighted(img,0.8,blank_image,0.2,0)
    return img






img=cv.imread("img_3.png")  #loading an image
img=cv.cvtColor(img,cv.COLOR_BGR2RGB) #convert the image to RGB color space for matplotlib

#next define the region of interest

#print(img1.shape) #finout the shape of image matrix
height=img.shape[0]   #define height of image
width=img.shape[1]   ##define width of image
print(height,width)

gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY) #convert the cropped image to grayscale for edge detection
cannyimage=cv.Canny(gray,100,200) #apply the Canny edge detection to find the edges


#define the region of interest
region_of_interest_vertices=[(0,height),(width/2,height/2),(width,height)]

cropped_image=region_of_interest(cannyimage,np.array([region_of_interest_vertices],np.int32))

#apply the probabilistic hough line transform to draw lines on the edges

lines=cv.HoughLinesP(cropped_image,rho=6,theta=np.pi/60,threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=25)
#print(lines)
final_image=drawlines(img,lines)

plt.imshow(final_image) #load the image using matplotlib
plt.show() #display the image using matplotlib


#cv.imshow("window",img)
cv.waitKey(0)
cv.destroyAllWindows()
