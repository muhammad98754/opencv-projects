#Face recognition with opencv with python

import cv2 as cv
import numpy as np
import os


########## KNN CODE ############
def distance(v1, v2):
    # Eucledian
    return np.sqrt(((v1 - v2) ** 2).sum())


def knn(train, test, k=5):
    dist = []

    for i in range(train.shape[0]):
        # Get the vector and label
        ix = train[i, :-1]
        iy = train[i, -1]
        # Compute the distance from test point
        d = distance(test, ix)
        dist.append([d, iy])
    # Sort based on distance and get top k
    dk = sorted(dist, key=lambda x: x[0])[:k]
    # Retrieve only the labels
    labels = np.array(dk)[:, -1]

    # Get frequencies of each label
    output = np.unique(labels, return_counts=True)
    # Find max frequency and corresponding label
    index = np.argmax(output[1])
    return output[0][index]


################################


cap=cv.VideoCapture(0) #opening the webcam
face_cascade=cv.CascadeClassifier("haarcascade_frontalface_alt.xml") #imported the haar cascade classifier for face recognition
skip=0
face_data=[] #in this list we store each face data
dataset_path="./face_dataset/" #faces will be stored in a folder named face_dataset

labels = []
class_id = 0
names = {}
file_name=input("enter the name of person:") #enter the name of person to console

# Dataset prepration
for fx in os.listdir(dataset_path):
	if fx.endswith('.npy'):
		names[class_id] = fx[:-4]
		data_item = np.load(dataset_path + fx)
		face_data.append(data_item)

		target = class_id * np.ones((data_item.shape[0],))
		class_id += 1
		labels.append(target)

face_dataset = np.concatenate(face_data, axis=0)
face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))
print(face_labels.shape)
print(face_dataset.shape)

trainset = np.concatenate((face_dataset, face_labels), axis=1)
print(trainset.shape)

font = cv.FONT_HERSHEY_SIMPLEX


while True:
    ret,frame=cap.read() #reading the frame
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY) #convert the BGR frames to grayscale image
    faces=face_cascade.detectMultiScale(gray_frame,1.3,5) #this method used for object detection
    if len(faces)==0:
        continue
    #print(faces)
    k=1
    faces=sorted(faces,key=lambda x: x[2]*x[3],reverse=True) #this ensures largest face is selected first
    skip+=1
    #print(faces)
    for face in faces[:1]: #This loop iterates over the first face (largest face) in the sorted list.
        x,y,w,h=face
        offset=5 #to slightly expand the face region.
        face_offset=frame[y-offset:y+h+offset,x-offset:x+w+offset] #extracts the face region
        face_selection=cv.resize(face_offset,(100,100))
        out = knn(trainset, face_selection.flatten())

        # Draw rectangle in the original image
        cv.putText(frame, names[int(out)], (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        if skip % 10 ==0:
            face_data.append(face_selection) # resized face region is added to the face_data list.
            print(len(face_data))
        cv.imshow(str(k),face_selection)




        k+=1
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) #creating a rectangular box over face
    cv.imshow("faces",frame)
    if cv.waitKey(1) == ord("q"):
        break
face_data=np.array(face_data) #convert the list into numpy array for KNN algorithm
face_data=face_data.reshape([face_data.shape[0],-1])
print(face_data.shape)
np.save(dataset_path+file_name,face_data) #data set saved
print("dataset saved at {}".format(dataset_path+file_name+".npy"))


cap.release()
cv.destroyAllWindows()

























