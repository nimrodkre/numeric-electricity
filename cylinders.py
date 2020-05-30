import matplotlib
import math
import relecasation
import sys

EPSILON = 1 / 1000
SCALE = 100
CIRCLE_ERROR = 2
L = 1 * SCALE
r = L / 5 * SCALE
d = 3 * L / 10
PI0 = 1
PI_CYCLINDER = 2 * PI0

CIRCLE1_COORDINATES = ((3*L/10) + SCALE/2, 0)
CIRCLE2_COORDINATES = ((-3*L/10) + SCALE/2, 0)


def print_table(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
        print("")

def init_table(table):
    # initialize the values in side boundaries
    for y in range(SCALE):
        table[0][y] = (-1) * PI0
        table[SCALE - 1][y] = PI0

    # initialize the values in up down boundaries
    for x in range(SCALE):
        table[x][0] = round(PI0 * x / L - L /2 / SCALE, 2)
        table[x][SCALE - 1] = round(PI0 * x / L - L / 2 / SCALE, 2)

    # init the circle1
    for x in range(SCALE):
        for y in range(SCALE):
            if relecasation.distance(CIRCLE1_COORDINATES, (x, y)) == r * SCALE:
                table[x][y] = PI_CYCLINDER * 2



def build_potential_table():
    table = [0] * SCALE
    for i in range(len(table)):
        table[i] = [0] * SCALE
    init_table(table)
    print_table(table)


if __name__ == '__main__':
    build_potential_table()
