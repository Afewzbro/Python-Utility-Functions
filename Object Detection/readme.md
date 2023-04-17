# Object Detection using ImageAI
This is a Python code that uses the ImageAI library to detect objects in an image.

## Requirements
imageai
tensorflow
## Installation
You can install imageai and tensorflow using pip package manager:


pip install imageai tensorflow
You also need to download the pre-trained model file resnet50_coco_best_v2.0.1.h5 from the official ImageAI GitHub repository and save it in your project directory.

## Usage
1. Import necessary libraries:
2. Set the path of the pre-trained model file:
3. Use detectObjectsFromImage() method to detect objects in an image:
4. Loop through the detected objects and print their names and probability percentages:
5. Display the output image using IPython.display.Image:

## Note
The input image file should be in the same directory as the Python file.
The output image file will be saved in the same directory as the Python file.