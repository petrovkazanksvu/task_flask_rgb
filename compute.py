from PIL import Image
import numpy as np


def define_color(image_name):
    """
    Define dominate color(RGB)
    Use PIL for open image, numpy for compute dominate color
    :param image_name: str
    :return: correct word from list('red', 'green', 'blue')
    """
    red_image = Image.open(image_name)
    red_image = red_image.convert("RGB")
    arr = np.asarray(red_image)
    average_color_values = np.mean(np.mean(arr, axis=0), axis=0)
    list_color = ["red", "green", "blue"]
    return list_color[np.argmax(average_color_values)]


