from random import sample
from test_images import *
import os

#dump()

exposure=0.1*10**6

#random_file = "jsons/"+sample(os.listdir('jsons'), 1)[0]

random_plant = "jsons/"+sample(['plant2.json', 'plant.json'], 1)[0]

#dump()
file = random_plant
#file='jsons/plant2.json'
#file=random_file
