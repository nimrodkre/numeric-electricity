import matplotlib
from matplotlib import pyplot
import math
import calculations
import sys
import numpy as np

EPSILON = 1 / 1000
SCALE = 10
CIRCLE_ERROR = 2
L = 1 * SCALE
r = L / 5
d = 3 * L / 10
PI0 = 1
PI_CYCLINDER = 2 * PI0

def color_table(table):
    pyplot.streamplot()

def print_table(table):
    for i in table:
        print(i)


def init_table(table):
    # initialize the values in up boundaries
    for y in range(SCALE):
        table[0][y] = round(PI0 * y / L - L / SCALE, 2)
        table[SCALE - 1][y] = round(PI0 * y / L - L / SCALE, 2)

    # initialize the values in side boundaries
    for x in range(SCALE):
        table[x][0] = (-1) * PI0
        table[x][SCALE - 1] = PI0

    # init the circle1
    CIRCLE1 = (d, SCALE / 2 - 1)
    CIRCLE2 = (SCALE - d, SCALE / 2 - 1)
    for y in range(SCALE):
        for x in range(SCALE):
            if round(calculations.distance(CIRCLE1, (x, y))) <= r:
                table[y][x] = 1
            if round(calculations.distance(CIRCLE2, (x, y))) <= r:
                table[y][x] = 1


def fill_table(table):
    DELTA_X = 1 / SCALE
    DELTA_Y = 1 / SCALE
    new_table = [0] * SCALE
    for i in range(len(table)):
        new_table[i] = [0] * SCALE

    for i in range(1, len(table) - 1):
        for j in range(1, len(table[0]) - 1):
            new_table[i][j] = 0.5 * (DELTA_Y ** 2 * (
                        table[i + 1][j] + table[i - 1][
                    j]) + DELTA_X ** 2 * (table[i][j + 1] + table[i][
                j - 1]))
            new_table[i][j] /= (DELTA_X ** 2 + DELTA_Y ** 2)
    return new_table


def build_potential_table():
    table = np.zeros(SCALE)
    init_table(table)
    print_table(table)
    new_table = fill_table(table)
    print_table(new_table)


if __name__ == '__main__':
    build_potential_table()
