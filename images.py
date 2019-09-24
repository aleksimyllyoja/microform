#!/usr/bin/env python3

from utils import *
from math import pi, sqrt, ceil
from random import randint
import argparse

IMAGES = []
def d_(f):
    IMAGES.append(f)
    return f

def load_img(filename, show=False):
    return Image.open('src/'+filename).convert('L')

@d_
def test_1(show=False):
    paths = []
    w = W/8.0

    paths.append(circle(w*2, 30, w))
    paths.append(circle(w*6, 34, w*1.3, 3, pi/6.0))

    paths.append(circle(w*2, 90, w*1.2, 4))
    paths.append(circle(w*6, 90, w*1.3, 5, -pi/2.0))

    return plot_paths(paths, show=show)

@d_
def test_2(show=False):
    paths = []

    paths.append([[0, 0], [127, 0]])
    paths.append([[127, 0], [127, 127]])
    paths.append([[127, 127], [0, 127]])
    paths.append([[0, 127], [0, 0]])
    paths.append([[0, 127], [0, 0]])

    paths.append([[0, 0], [127, 127]])
    paths.append([[0, 127], [127, 0]])

    return plot_paths(paths, show=show)

@d_
def test_3(show=False):
    image = create_image()

    for x in range(0, randint(2, 10)):
        x0 = randint(0, 127)
        y0 = randint(0, 127)
        x1 = randint(0, 127)
        y1 = randint(0, 127)
        image = plot_paths_on_image([[[x0, y0], [x1, y1]]], image)

    if show: show_image(image)
    return image

@d_
def test_4(show=False):
    image = create_image()

    for i in range(40):
        x = randint(0, 127)
        y = randint(0, 127)
        image.putpixel((x, y), 255)

    if show: show_image(image)
    return image

@d_
def test_6(show=False):
    image = create_image()
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, 127, 127), outline='white')
    return image

@d_
def plant(): return load_img('plant.png')

@d_
def plant3(): return load_img('plant3.png')

@d_
def plant4(): return load_img('plant4.png')

@d_
def plant5(): return load_img('plant5.png')

@d_
def plant6(): return load_img('plant6.png')

def show():
    h = round(sqrt(len(IMAGES)))
    w = ceil(len(IMAGES)/h)

    img = Image.new('L', (h*128, h*128))
    i=0
    for x in range(h):
        for y in range(w):
            i+=1
            if i<len(IMAGES):
                img.paste(IMAGES[i](), (x*128, y*128))
    img.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--show', action='store_true', default=False)

    args = parser.parse_args()

    if args.dump: dump()
    if args.show: show()
