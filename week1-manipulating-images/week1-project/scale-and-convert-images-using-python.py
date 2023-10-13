
"""
Automating Real-World Tasks With Python
Week 1 - Scale and Convert Images Using Pythom
"""

import os 
import sys

from PIL import Image

def rotate_scale_convert_image():
   
    # create image object
    with Image.open("fox.png") as im_obj:

        print(im_obj)

rotate_scale_convert_image()

