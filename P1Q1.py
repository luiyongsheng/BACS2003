import math

def volume(r,h):
    v = math.pi*(r**2)*h
    return v

r = 0
h = 0
V = 0

r = input("Enter radius : ")
h = input("Enter height : ")

V = volume(r,h)

print "\nVolume : %.2f" %V
