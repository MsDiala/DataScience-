import pytest
from img import ImageStats 


#Test that the ImageStats constructor throws a FileNotFoundError if the image file does not exist:
def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        image_stats = ImageStats('nonexistent_image.bmp')
        
#Test that the ImageStats constructor correctly extracts the width and height of the image:
def test_width_and_height():
    image_stats = ImageStats('HightWidthTest.png')
    assert image_stats.width == 400
    assert image_stats.height == 300

#Test that the ImageStats constructor correctly extracts the pixel data of the image:
def test_pixel_data():
    image_stats = ImageStats('pexels-rodolfo-clix-922610.png')
    assert len(image_stats.pixel_data) == 120000
    assert image_stats.pixel_data[0] == 153
    assert image_stats.pixel_data[-1] == 226
#Test that the mean method returns the correct mean value of the image:
def test_mean():
    image_stats = ImageStats('pexels-rodolfo-clix-922610.png')
    assert image_stats.mean() == pytest.approx(170.8949, rel=1e-4)
#Test that the std_dev method returns the correct standard deviation of the image:
def test_std_dev():
    image_stats = ImageStats('pexels-rodolfo-clix-922610.png')
    assert image_stats.std_dev() == pytest.approx(44.3209, rel=1e-4)
#Test that the min_value method returns the correct minimum gray value of the image:
def test_min_value():
    image_stats = ImageStats('pexels-rodolfo-clix-922610.png')
    assert image_stats.min_value() == 0
#Test that the max_value method returns the correct maximum gray value of the image:
def test_max_value():
    image_stats = ImageStats('pexels-rodolfo-clix-922610.png')
    assert image_stats.max_value() == 255

