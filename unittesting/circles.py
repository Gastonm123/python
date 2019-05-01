from math import pi

def circle_area(radius):
    if type(radius) not in (int, float):
        raise TypeError("Not supported types for the function")
    if radius < 0:
        raise ValueError("Negative value not supported")
    return pi * (radius ** 2)
