
import cv2

#load faceCascade 
# the xml file contains features data so we can compare it to the live data , the feature here is the human face 

face_cascade = cv2.CascadeClassifier('Problem#1/haarcascade_frontalface_default.xml')


#create the variable that will recall the input from the webcam 
video = cv2.VideoCapture(0)


#create the while loop so we can extraxt the video , creating slideshow of images which is video 
while True:
    #create two var check and frame , crete video.read so we can read the img data in the video and then storing it in the frame var 
    check,frame = video.read()
    
    #convert the colored img into greyscale img >> why >> cuz grey scale image is more accurate for feature scaling 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # color bgr which is blue green red to grey
    
    #find out wheather if there is a face in the img or not by comparing the img from the cam with xml 
    face = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    #Face dimentions are x,y,w,h such that w : width , h:height 
    
    for x,y,w,h in face:
        #draw a rectangle on our face 
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
        #blure the detected face 
        img[y:y+h , x:x+w] = cv2.medianBlur(img[y:y+h , x:x+w],35)
        
    #disply the frame
    cv2.imshow("Blur !!!",frame)
    key = cv2.waitKey(1)
    #if we want to close it 
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


    
