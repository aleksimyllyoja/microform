from random import sample
from images import *
import os

def filter_images(ls):
    return list(filter(lambda x: x.__name__ in ls, IMAGES))

def sample_from(ls):
    return sample(filter_images(ls), 1)[0]

exposure=0.13*10**6

plants = sample_from(['plant', 'plant3', 'plant4', 'plant5', 'plant6'])

source = plants
#source = white_circle
