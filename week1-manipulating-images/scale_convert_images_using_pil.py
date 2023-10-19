#! /usr/bin/env python3

import os
from PIL import Image

def rotate_scale_convert_images(path, rotate, resize, format, save_path):
    """
    Rotate, scale and convert images from specified directory.

    Args:
        path (str): Path to directory containing images to convert.
        rotate (int): Rotation angle in degrees. 
        resize (tuple(int, int)): Dimensions for resizing images (width, height).
        format (str): Image file format extension (e.g. "jepg", "png").
        save_path (str): Path to save the converted images. 
    """
    try:
        
        directory = os.listdir(path)
        for image in directory:
            if image != ".DS_Store":
                im = Image.open(os.path.join(path, image).convert("RGB"))
                im.rotate(rotate).resize(resize).convert("RGB").save("{0}{1}".format(path, image.split(".")[0]), format)

    except Exception as e:
        print(f"ERROR {e}")

path = "images/"
save_path = "/opt/icons/"
rotate, resize, format = [90, (128, 128), "JPEG"]
rotate_scale_convert_images(path, rotate, resize, format, save_path)



# TODO ERROR cannot write mode LA as JPEG