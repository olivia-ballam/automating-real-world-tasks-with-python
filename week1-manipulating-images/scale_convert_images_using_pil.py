#! /usr/bin/env python3

import os
from PIL import Image

def rotate_scale_convert_images(path, save_path, rotate, resize, convert, format):
    """Rotate, scale and convert images from specified directory."""
    try:
        directory = os.listdir(path)
        for image in directory:
        # Loop through images in directory
            if image != ".DS_STORE":
                directory, name = os.path.join(path, image), image.split(".")[0]
                # Rotate, resize, convert and save the image.
                im = Image.open(os.path.join(directory,image))
                im.rotate(rotate).resize(resize).convert(convert).save(f"{save_path}{name}.{format}")
    except FileNotFoundError as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    
    path = "images/"
    save_path = "/opt/icons/"
    rotate, resize, convert, format = [-90, (128, 128), "RGB", "jpeg"]
    rotate_scale_convert_images(path, save_path, rotate, resize, convert, format)


