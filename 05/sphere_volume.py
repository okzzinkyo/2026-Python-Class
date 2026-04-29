import math

def getSphereVolume(radius):
    v = (4 / 3) * math.pi * (radius ** 3)
    return v

r = float(input("구의 반지름은?"))
print(getSphereVolume(r))
