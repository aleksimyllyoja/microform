import noise
from random import random, choice, randint, uniform, seed
from utils import *
from math import *
import cv2

sq2 = sqrt(2)

def _r():
    image = create_image()
    z = random()

    l = 2 #uniform(1, 3)

    o = randint(2, 4)
    b = randint(-100, 100)
    p = uniform(-20, 20)

    for x in range(128):
        for y in range(128):

            d = sqrt(((x-128/2.0)/127)**2+((y-128/2.0)/127)**2)

            v = noise.pnoise3(
                x/127, y/127, z,
                octaves=o,
                persistence=p,
                lacunarity=l,
                base=b,
            )

            v = (1+v)/2
            k = max(0, ((d-.8)**2)*4)
            k = v*k*256
            image.putpixel((x, y), int(k))

    image = np.array(image)
    ret1, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    return th1

def m(src):
    operation = choice([
        cv2.bitwise_not,
        #cv2.bitwise_or,
        #cv2.bitwise_xor
    ])
    if random() > 0.5:
        i2 = _r()
        src = operation(src, src, mask=i2)

    return src

def r():
    i1 = _r()
    for i in range(randint(0, 2)):
        i1 = m(i1)
    return Image.fromarray(i1)

if __name__ == '__main__':
    #seed(10)
    show_many([r]*5**2)
