from utils import *
from math import pi
from random import randint

tests = []
def d_(f):
    tests.append(f)
    return f

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
def test_5(show=False):
    image = create_image()

    for y in range(0, 128):
        for x in range((int(400/(y+1))+1)%127, 128, int(400/(y+1))+1):
            image.putpixel((x, y), 255)

    if show: show_image(image)
    return image

#@d_
def test_6(show=False):
    image = create_image()
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, 127, 127), fill='white')
    return image


def load_img(filename, show=False):
    return Image.open('src/'+filename).convert('L')

@d_
def face(): return load_img('face.png')

@d_
def plant(): return load_img('plant.png')

@d_
def plant2(): return load_img('plant2.png')

def dump():
    import json
    t = lambda x: int(x/16.0)

    for tf in tests:
        print(tf.__name__)
        l = map(lambda xs: list(map(t, xs)), np.array(tf()).tolist())
        json.dump(list(l), open('jsons/'+tf.__name__+'.json', 'w'))

if __name__ == '__main__':
    dump()
