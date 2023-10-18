#!usr/bin/env python3

import os
from PIL import Image

def scale_convert_images(path, rotate, resize, format, new_path):

    directory = os.listdir(path)
    for image in directory:
        directory, name = os.path.join(path, image), image.split(".")[0]
        with Image.open(directory) as im:
            im.rotate(rotate).resize(resize).save(f"{new_path}{name}{format}")


#path = "home/{username}/images/"
new_path = "/opt/icons/"
rotate, resize, format = [90, (128, 128), ".jpeg"]
path = "/Users/oball/automating-real-world-tasks-with-python/week1-manipulating-images/testing-images/"
scale_convert_images(path, rotate, resize, format, path)

