import math
def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x < y:
        return y
    else:
        return x


def max_of_three(x, y, z):
    if x < y and y < z: 
     return z
    elif x < y and y > z:
     return y
    else:
        return x

