#import cv2
import cv2

#load faceCascade 
# Load the classifier
# the xml file contains features data so we can compare it to the live data , the feature here is the human face 

face_cascade = cv2.CascadeClassifier('Problem#1/haarcascade_frontalface_default.xml')


# Load the input image
img = cv2.imread('Problem#1/Family_Nieuw.jpg')

# Detect faces in the image
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    img[y:y+h , x:x+w] = cv2.medianBlur(img[y:y+h , x:x+w],35)


if img is None:
    print("Could not find or read the image file.")
else:
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()