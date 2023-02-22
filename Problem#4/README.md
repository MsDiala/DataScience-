# Image Statistics
The code calculates the mean, standard deviation, minimum and maximum gray values of an input image. It uses the OpenCV library to load the image and extract its header information, such as its width and height.

## Running the Code

- Ensure that you have OpenCV installed on your system. You can install it using pip, a Python package manager, by running the following command in your terminal:
`pip install opencv-python`

- Save the code to a file named image_stats.py.

- Save an image you want to analyze to the same directory as the image_stats.py file.

- In your terminal, navigate to the directory where the image_stats.py file and your image are saved.

- Run the code using the following command:
`python image_stats.py`
This will print out the mean, standard deviation, minimum, and maximum gray values of the image.

## Importing Libraries
The first line of the code imports the cv2 library, which is the OpenCV library for Python. This library is used for reading and manipulating image data.

## Load the input image
The ImageStats class is defined, which takes an image path as input. Inside the class, the cv2.imread function is used to read the input image file. Then, the image path is stored in the self.image_path variable for future reference.

The input image is also loaded as a binary file using the open function with the 'rb' mode, which allows reading binary files. The image data is then read using the read function and stored in the data variable.

The width and height of the image are then extracted from the image header using the int.from_bytes function, which takes the byte string representing the value and the byte order and returns the integer value.

The pixel data is then extracted from the binary file and stored as a list of integers in the pixel_data variable. The shape of the input image is also extracted to determine the number of rows and columns.

The for loop then iterates through each pixel in the image and extracts the pixel value using the int.from_bytes function. The pixel values are then appended to the pixel_data list. The BGR pixel values are also averaged and assigned to the pixel in the img array to convert the input image to grayscale.

ImageStats class methods
The ImageStats class has four methods for calculating the mean, standard deviation, minimum and maximum gray values of the image.

The mean method calculates the mean value of the pixel_data list using the sum function and the len function.

The std_dev method calculates the standard deviation of the pixel_data list using the mean value calculated by the mean method. The variance is calculated using a list comprehension that subtracts the mean from each value in the pixel_data list, squares the result, and takes the sum of the squared differences. The variance is then square rooted to obtain the standard deviation.

The min_value method returns the minimum value in the pixel_data list using the min function.

The max_value method returns the maximum value in the pixel_data list using the max function.

## Calculate Image Statistics
An instance of the ImageStats class is created using the input image path.

The mean, standard deviation, minimum, and maximum gray values of the image are then calculated using the mean, std_dev, min_value, and max_value methods of the ImageStats class, respectively. The results are stored in mean, std_dev, min_value, and max_value variables, respectively.

## Print Image Statistics
Finally, the mean, standard deviation, minimum and maximum gray values of the image are printed to the console using the print function and formatted string literals.