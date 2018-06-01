from random import *
import math
import time

w = 1280
h = 800
totalDistance = 0
speed = 0
timestamp = 0

coordinatesList = []

def distance(p1,p2):    
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) # use **2 to improve performance

timestamp = time.time()
for x in range(0,10):
    rw = randint(1,w)
    rh = randint(1,h)
    coordinatesList.append((rw,rh))
    print(coordinatesList[x])
    totalDistance += distance(coordinatesList[x-1], coordinatesList[x])
    time.sleep(1)

timestamp = time.time() - timestamp

print('\nTotal distance travelled : ', totalDistance)
print('Time taken: ',timestamp)
print('Average speed: ', totalDistance / timestamp)
