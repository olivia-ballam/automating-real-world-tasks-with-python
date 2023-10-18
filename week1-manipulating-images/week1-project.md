# Week 1 Project
## Project Problem Statement 

You'll need to write a script that processes a bunch of images. It turns out that your company is in the process of updating its website, and the cintractor has been hired to create some new icon graphics for the site. Howver, the contrator has delivered the final designs abd they're in the wrong format, rotated 90° and too large. You’re unable to get in contact with the designers and your own deadline is approaching fast. You’ll need to use Python to get these images ready for launch!

So, how will you do this? You'll need to go through a folder full of images and operate with each of them. On each image, you'll use PIL methods like the ones we saw in the examples, and then write the new images in the right place.

## What you'll do

Use the Python Imaging Library to do the following **batch** of images:

- Open an image 
- Rotate an image 
- Resize an image 
- Save an image in a specific format in separate directory


### Install Pillow 

Python Imaging Library (Known as Pillow in newer versions) is a library in Python that adds support for opening, manipulating, and saving lots of different image file formats. 

Pillow offers serveral standard procedures for image manipulation. These include:

- Per-pixel manipulation
- Masking and transparency handling
- Image filtering, such as bluring, contouring, smoothing and edge finding
- Image enhancing, like sharpening and adjusting brightness, contrast or colour
- Adding text to images (and much more!)

We can use the following command to install the pillow library. 

```
pip3 install pillow
```

### Writing a Python Script

The script will need to perform the following operations. 

- Iterate through each file in the folder:
    - Rotate the image 90° clockwise
    - Resize the image from 192x192 to 128x128
    - Save the image to a new folder (/opt/icons/) in .jpeg format


#### scale_convert_images.py



