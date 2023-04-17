# Exif Metadata Extraction from Images
This code demonstrates how to extract Exif metadata from an image in Python. Exif metadata contains information about the camera settings, such as aperture, shutter speed, ISO, as well as other details such as date and time, location, and more.

## Installation
This code uses the following libraries:

PIL
ExifRead (optional)

You can install these libraries using pip:

pip install pillow
pip install ExifRead

## Usage
There are two methods demonstrated in the code for extracting Exif metadata from an image:

## Method 1: Using PIL library
This method uses the PIL (Python Imaging Library) library to extract Exif data from an image. First, the image is opened using PIL.Image.open(). The _getexif() function is used to extract the Exif data from the image, and the TAGS dictionary is used to convert the numerical Exif tag IDs to human-readable tags.

## Method 2: Using ExifRead library
This method uses the ExifRead library to extract Exif data from an image. First, the image is opened as a binary file using open(). The process_file() function from the ExifRead library is used to extract the Exif data from the file. The resulting data is a dictionary-like object that can be used to access the various Exif tags.

## Conclusion
Using the above code, you can extract Exif metadata from an image in Python. Exif metadata can be used for a variety of purposes, such as identifying the camera settings used to capture an image, or retrieving location data from the image.