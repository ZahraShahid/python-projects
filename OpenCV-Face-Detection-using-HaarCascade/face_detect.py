#import cv2
import cv2 as cv

#read image
img = cv.imread('happy-kid.jpg')
cv.imshow("Kid Image",img)

#read group image
#group = cv.imread('school-boys.jpg')
#cv.imshow("Group of Boys",group)


#function to rescale images
def rescaleFrame(frame,scale=0.2):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
#rescale image
resized_image = rescaleFrame(img)
cv.imshow("Resized Image",resized_image)

#rescale group image
#resized_image = rescaleFrame(group)
# cv.imshow("Resized Image",resized_image)


#convert Image to Gray
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)

#Read Face HaarCascade Classfier 
haar_cascade = cv.CascadeClassifier('haar_faces.xml')

#detects the face
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=4)

#print the number of faces detected
print(f'Number of faces found = {len(face_rect)}')

#To draw a rectangle around each detected face
for (x,y,w,h) in face_rect:
    cv.rectangle(resized_image, (x,y),(x+w,y+h), (0,255,0), thickness=2)


#print final image
cv.imshow('Detected Faces',resized_image)

cv.waitKey(0)