# Face Detection and Blurring with OpenCV

### Prerequisites

- Python: This code is written in Python, so you need to have Python installed on your computer to run it. You can download Python from the official website [Python Installation](https://www.python.org/downloads/).

- OpenCV: This code uses the OpenCV library, so you need to have OpenCV installed on your computer to run it. You can follow the instructions for your operating system to install OpenCV: [OpenCV setup tutorial](https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html)
  If OpenCV is not already installed, you can install it using pip by running the following command in the terminal/command prompt:
  `pip install opencv-python`



## - Blure Faces in an Image (imgFaceBlur.py)

### Introduction

This code uses the OpenCV library to detect human faces in an image. The code loads a pre-trained classifier "haarcascade_frontalface_default.xml" and applies it to an input image. The classifier uses Haar cascades, a machine learning object detection method, to detect faces in the image. The code then draws rectangles around the detected faces and applies a median blur to them.


### Required Files

- Code file: Save the code in a .py file.

- Image file: The code takes an image file as input. The input image file should be in the same directory as the code file. The code uses the following line to load the image file:
  `img = cv2.imread('Problem#1/Family_Nieuw.jpg')`
  Make sure to change the file path to the location of your input image file.

- Haar Cascade Classifier file: The code uses a pre-trained classifier "haarcascade_frontalface_default.xml" to detect faces in the image. This file should be in the same directory as the code file. The code uses the following line to load the classifier file:
  `face_cascade = cv2.CascadeClassifier('Problem#1/haarcascade_frontalface_default.xml')`
  Make sure to change the file path to the location of your classifier file.

### Running the Code

- 1. Open a terminal or command prompt and navigate to the directory where the .py file is saved.

- 2. Run the code by typing python filename.py where "filename" is the name of the .py file.
  `python filename.py`

- 3. The code will display the input image with rectangles drawn around the detected faces and with a median blur applied to the faces.

### Code Explanation

- Importing the OpenCV library: The first line imports the OpenCV library using the following code:
`import cv2`

- Loading the Haar Cascade Classifier: The code loads the "haarcascade_frontalface_default.xml" classifier using the following code:
`face_cascade = cv2.CascadeClassifier('Problem#1/haarcascade_frontalface_default.xml')`
This classifier is used to detect faces in the input image.

- Loading the Input Image: The input image is loaded using the following code:
`img = cv2.imread('Problem#1/Family_Nieuw.jpg')`
The cv2.imread() function takes the file path of the input image as an argument and returns the image as a matrix.

- Detecting Faces in the Image: The code uses the `face_cascade.detectMultiScale()` method to detect faces in the image. 
  This method takes the input image as an argument and returns a list of rectangles that surround the detected faces. The following parameters are used in this method:
  - `scaleFactor`: The factor by which the `img` is resized. A value of `1.1` means that the `img` is resized by 10%.
  - `minNeighbors`: The number of neighbors a region needs to have to be considered a face.
  - `minSize`: The minimum size of the face to be detected.

- Drawing Rectangles around the Faces: The code uses the cv2.rectangle() function to draw rectangles around the faces. The function takes the following arguments:
  - `img`: The input image where the rectangles are drawn.
  - `(x, y)`: The top-left corner of the rectangle.
  - `(x+w, y+h)`: The bottom-right corner of the rectangle.
  - `(255, 0, 0)`: The color of the rectangle, represented as a tuple of red, green, and blue (RGB) values.
  - `2`: The thickness of the rectangle.

- Blurring the Faces: The code uses the cv2.medianBlur() function to apply a median blur to the faces. The function takes the following arguments:
  - `img[y:y+h , x:x+w]`: The region of the image where the median blur is applied, defined by the rectangles drawn around the faces.
  - `35`: The size of the blur.

- Displaying the Image: The code uses the `cv2.imshow()` function to display the image. The function takes the following arguments:
  - `'Image'`: The name of the window that displays the image.
  - `img`: The image to be displayed.

- Waiting for Key Press: The code uses the `cv2.waitKey(0)` function to wait for a key press.
- Destroying All Windows: The code uses the `cv2.destroyAllWindows()` function to close all windows when the program is finished.

## - Faces in a video (vidFaceBlur.py)

### Introduction

This code is used to detect human faces from a live video feed from a webcam and blurs the detected faces in real-time.

### Running the Code

- 1. Open a terminal or command prompt and navigate to the directory where the .py file is saved.

- 2. Run the code by typing python filename.py where "filename" is the name of the .py file.
  `python filename.py`

- 3. The code will open a window displaying the live video feed from your webcam. The webcam captures the video in real-time and the code will detect and blur any human faces in the frame.
  

### Code Explanation

- Importing the OpenCV library: The first line imports the OpenCV library using the following code:
`import cv2`

- Loading the Haar Cascade Classifier: The code loads the "haarcascade_frontalface_default.xml" classifier using the following code:
`face_cascade = cv2.CascadeClassifier('Problem#1/haarcascade_frontalface_default.xml')`
which is used to detect human faces in the video frame.

- Opens a live video feed from the webcam using the `cv2.VideoCapture(0)` method, where `0` is the index of the default camera (i.e. the webcam).
  
- A `while` loop is used to continuously read the video frames from the webcam.
  
- Within the loop, the current frame is first converted to a grayscale image, as grayscale images are more accurate for feature scaling.
  
- The grayscale image is then passed through the Haar Cascade Classifier to detect human faces in the frame. The detectMultiScale method returns the face dimensions `(x, y, width, height)`.

- A rectangle is drawn around the detected face and the face is blurred using the `cv2.medianBlur` method.

- The processed frame is then displayed in a window using the `cv2.imshow` method.

- The loop continues until the `q` key is pressed on the keyboard, at which point the program stops and the webcam is released.


Note: The code is well-commented and each line of code has been explained to make it easier to understand what the code is doing.




