import matplotlib
import math
import calculations
import sys

EPSILON = 1 / 1000
SCALE = 20
CIRCLE_ERROR = 2
L = 1 * SCALE
r = L / 5
d = 3 * L / 10
PI0 = 1
PI_CYCLINDER = 2 * PI0


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
    CIRCLE1 = (d, SCALE / 2 - 1)
    CIRCLE2 = (SCALE - d, SCALE / 2 - 1)
    for y in range(SCALE):
        for x in range(SCALE):
            if round(calculations.distance(CIRCLE1, (x, y))) == r:
                table[y][x] = 1
            if round(calculations.distance(CIRCLE2, (x, y))) == r:
                table[y][x] = 1



def build_potential_table():
    table = [0] * SCALE
    for i in range(len(table)):
        table[i] = [0] * SCALE
    init_table(table)
    print_table(table)


if __name__ == '__main__':
    build_potential_table()
