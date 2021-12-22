from PIL import Image
import numpy as np


def define_color(image_name):
    red_image = Image.open(image_name)
    red_image = red_image.convert("RGB") # added this line
    arr = np.asarray(red_image)
    m = np.mean(arr, axis=0)
    b = np.mean(m, axis=0)
    list_color = ["red", "green", "blue"]
    return list_color[np.argmax(b)]

# image_n = "red.png"
#
# print(compute(image_n))

