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
        # List images in specified path
        directory = os.listdir(path)
        for image in directory:
            # Loop through images in directory
            if image.endswith(".tiff"):
                name = image.split(".")[0]
                with Image.open(os.path.join(path, image)) as im:
                    # Rotate, resize, and save the image to save_path with specified file format. 
                    im.rotate(rotate).resize(resize).save(f"{save_path}{name}.{format}")
    except Exception as e:
        print(f"ERROR {e}")
#path = "images/"
#save_path = "/opt/icons/"
path = "/Users/oball/automating-real-world-tasks-with-python/week1-manipulating-images/testing_images"
save_path = "/Users/oball/automating-real-world-tasks-with-python/week1-manipulating-images"
rotate, resize, format = [90, (128, 128), "jpeg"]
rotate_scale_convert_images(path, rotate, resize, format, save_path)



