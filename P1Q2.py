from random import *
import math
import time

def calculateDistance(p,q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

def calculateMouseSpeed(x,y):
    dist = calculateDistance(x,y)
    return dist / timestamp

w = 1280
h = 800
first = (0,0)
second = (0,0)
timestamp = 0

timestamp = time.time()
first = ((randint(0,w-1), randint(0,h-1)))
print first
time.sleep(1)
second = ((randint(0,w-1), randint(0,h-1)))
print second
timestamp = time.time() - timestamp

print "Time taken : ", timestamp

print "Mouse Speed : ", calculateMouseSpeed(first,second)

