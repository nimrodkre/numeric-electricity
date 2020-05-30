import math


def distance(point1, point2):
    return math.sqrt(math.pow(point1[0] - point2[0], 2) +
                     math.pow(point1[1] - point2[1], 2))