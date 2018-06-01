from random import *
import math
import time

w = 1280
h = 800
distance = 0
speed = 0

coordinatesList = []

def distance(p1,p2):    
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) # use **2 to improve performance

for x in range(0,10):
    rw = randint(1,w)
    rh = randint(1,h)
    coordinatesList.append((rw,rh))
    print(coordinatesList[x])
    time.sleep(1)

print(distance(coordinatesList[0], coordinatesList[1]))

