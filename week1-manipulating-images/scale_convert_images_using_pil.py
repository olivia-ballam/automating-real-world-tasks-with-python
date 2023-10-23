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

    Raises: 
        FileNotFoundError: If the specified 'path' or 'save_path' does not exists. 
    """
    try:
        
        directory = os.listdir(path)
        for image in directory:
            # Loop through images in directory
            directory, name = os.path.join(path, image), image.split(".")[0]
            with Image.open(directory).convert() as im:
                # Rotate, resize, and save the image to save_path with specified file format. 
                im.rotate(rotate).resize(resize).save(f"{save_path}{name}.{format}")
    except FileNotFoundError as e:
        print(f"ERROR: {e}")

path = "home/student-04-c7572b35d99b@linux-instance/images/"
save_path = "/opt/icons/"
rotate, resize, format = [90, (128, 128), "jpeg"]
rotate_scale_convert_images(path, rotate, resize, format, save_path)



