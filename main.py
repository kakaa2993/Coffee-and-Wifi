#!/usr/bin/python3

import random
import colorgram
import turtle

tim = turtle.Turtle()


def extract_colors_from_image():
    colors_list = []
    colors = colorgram.extract("image.jpg", 2**50)
    for i in range(len(colors)):
        red = colors[i].rgb.r
        green = colors[i].rgb.g
        blue = colors[i].rgb.b
        colors_list.append((red, green, blue))
    return colors_list


print(extract_colors_from_image())
