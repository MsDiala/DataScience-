"""""
Image Statistics: Given a gray scale image (8 bpp), you are expected to create a 
.net 6 class that loads an image, 
and calculate the image statistics 
(mean, standard deviation, minimum and maximum gray value) 
without using any third party library.
"""""
import cv2
  
# Load the input image
class ImageStats:
    def __init__(self, image_path):
        img = cv2.imread('pexels-rodolfo-clix-922610.png')
        self.image_path = image_path
        
        
        # Load image as a binary file
        with open(image_path, 'rb') as f:
            data = f.read()
        
        # Parse image header to get the width and height
        self.width = int.from_bytes(data[18:22], byteorder='little')
        self.height = int.from_bytes(data[22:26], byteorder='little')
        
        # Extract pixel data as a list of integers
        global pixel_data 
        pixel_data = []
        (row, col) = img.shape[0:2]
  
# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
        for i in range(row):
            for j in range(col):
                pixel_value = int.from_bytes(data[26 + j:27 + j], byteorder='little')
                pixel_data.append(pixel_value) 

                # Find the average of the BGR pixel values
                img[i, j] = sum(img[i, j]) * 0.33
        

    def mean(self):
        return sum(pixel_data) / len(pixel_data)
    
    def std_dev(self):
        mean = self.mean()
        var = sum((x - mean) ** 2 for x in pixel_data) / len(pixel_data)
        return var ** 0.5
    
    def min_value(self):
        return min(pixel_data)
    
    def max_value(self):
        return max(pixel_data)

# Create an instance of the ImageStats class for the example image
image_stats=ImageStats('pexels-rodolfo-clix-922610.png')

# # Calculate the mean, standard deviation, minimum and maximum gray value of the image
mean = image_stats.mean()
std_dev = image_stats.std_dev()
min_value = image_stats.min_value()
max_value = image_stats.max_value()

# Print the results
print(f"Mean: {mean}")
print(f"Standard deviation: {std_dev}")
print(f"Minimum gray value: {min_value}")
print(f"Maximum gray value: {max_value}")
