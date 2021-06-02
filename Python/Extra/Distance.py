import math

def calc_distance(x, y, x1, y1):
    return math.sqrt(math.pow(x-x1, 2)+ math.pow(y-y1, 2))

print(calc_distance(5, 5, 7, 2))