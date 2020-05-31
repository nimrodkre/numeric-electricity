from matplotlib import pyplot
import calculations
import numpy as np

EPSILON = 1 / 1000
SCALE = 100
CIRCLE_ERROR = 2
L = 1 * SCALE
r = L / 5
d = 3 * L / 10
PI0 = 1
PI_CYCLINDER = 2 * PI0


def color_table(table):
    fig = pyplot.figure()
    ax = fig.gca()
    X = np.arange(-1, 1.02, 2 / SCALE)
    Y = np.arange(-1, 1.02, 2 / SCALE)
    X, Y = np.meshgrid(X, Y)
    Z = table
    surf = pyplot.pcolormesh(X, Y, Z)
    pyplot.show()


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
    CIRCLE2 = (SCALE - d , SCALE / 2 - 1)
    circle_points = []
    for y in range(SCALE):
        for x in range(SCALE):
            if round(calculations.distance(CIRCLE1, (x, y))) <= r - 10:
                table[y][x] = PI_CYCLINDER
                circle_points.append((x, y))
            if round(calculations.distance(CIRCLE2, (x, y))) <= r - 10:
                table[y][x] = PI_CYCLINDER
                circle_points.append((x, y))
    return circle_points


def fill_table(table, circle_points):
    DELTA_X = 1 / SCALE
    DELTA_Y = 1 / SCALE
    new_table = np.zeros((SCALE, SCALE))
    # initialize the values in up boundaries
    for y in range(SCALE):
        new_table[0][y] = round(PI0 * y / L - L / SCALE, 2)
        new_table[SCALE - 1][y] = round(PI0 * y / L - L / SCALE, 2)

    # initialize the values in side boundaries
    for x in range(SCALE):
        new_table[x][0] = (-1) * PI0
        new_table[x][SCALE - 1] = PI0
    for y in range(1, SCALE - 1):
        for x in range(1, SCALE - 1):
            if (x, y) not in circle_points:
                new_table[y][x] = 0.5 * (DELTA_Y ** 2 * (
                        table[y][x + 1] + table[y][
                    x - 1]) + DELTA_X ** 2 * (table[y + 1][x] + table[y - 1][
                    x]))
                new_table[y][x] /= (DELTA_X ** 2 + DELTA_Y ** 2)
            else:
                new_table[y][x] = table[y][x]
    return new_table


def build_potential_table():
    table = np.zeros((SCALE, SCALE))
    circle_points = init_table(table)
    for i in range(500):
        print(i)
        table = fill_table(table, circle_points)
    color_table(table)


if __name__ == '__main__':
    build_potential_table()
