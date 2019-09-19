from utils import *
from math import pi
from random import randint

def test_1(show=False):
    paths = []
    w = W/8.0

    paths.append(circle(w*2, 30, w))
    paths.append(circle(w*6, 34, w*1.3, 3, pi/6.0))

    paths.append(circle(w*2, 90, w*1.2, 4))
    paths.append(circle(w*6, 90, w*1.3, 5, -pi/2.0))

    return plot_paths(paths, show=show)

def test_2():
    paths = []

    paths.append([[0, 0], [127, 0]])
    paths.append([[127, 0], [127, 127]])
    paths.append([[127, 127], [0, 127]])
    paths.append([[0, 127], [0, 0]])
    paths.append([[0, 127], [0, 0]])

    paths.append([[0, 0], [127, 127]])
    paths.append([[0, 127], [127, 0]])

    return plot_paths(paths, show=True)

def test_3():
    image = create_image()

    for x in range(0, W):
        v = int(255/127.0*x)
        image = plot_paths_on_image([[[x, 0], [x, 127]]], image, color=(v,v,v))

    show_image(image)

def test_4():
    image = create_image()

    for i in range(40):
        x = randint(0, 127)
        y = randint(0, 127)
        image[y, x] = (255, 255, 255)

    show_image(image)

def test_5():
    image = create_image()

    for y in range(0, 128):
        for x in range((int(400/(y+1))+1)%127, 128, int(400/(y+1))+1):
            image[y, x] = (255, 255, 255)

    show_image(image)

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
