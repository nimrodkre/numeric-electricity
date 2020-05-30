import matplotlib
import relecasation
import sys

EPSILON = 1 / 1000
CIRCLE_ERROR = 2
L = 1
r = L / 5
d = 3 * L / 10
PI0 = 1
PI_CYCLINDER = 2 * PI0
X_SCALE = 100
Y_SCALE = 100
CIRCLE1_COORDINATES = ((3*L*X_SCALE/10) + X_SCALE/2, 0)
CIRCLE2_COORDINATES = ((-3*L*X_SCALE/10) + X_SCALE/2, 0)


def print_table(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print (table[i][j], end=" ")
        print("")

def init_table(table):
    # initialize the values in side boundaries
    for y in range(Y_SCALE):
        table[0][y] = (-1) * PI0
        table[X_SCALE - 1][y] = PI0

    # initialize the values in up down boundaries
    for x in range(X_SCALE):
        table[x][0] = round(PI0 * x / L / Y_SCALE - L /2, 2)
        table[x][Y_SCALE - 1] = round(PI0 * x / L / Y_SCALE - L / 2, 2)

    # init the circle1
    for x in range(X_SCALE):
        for y in range(Y_SCALE):
            print(relecasation.distance((x, y), CIRCLE1_COORDINATES))
            if relecasation.distance((x, y), CIRCLE1_COORDINATES) < r:
                table[x][y] = PI_CYCLINDER
            if relecasation.distance((x, y), CIRCLE2_COORDINATES) < r:
                table[x][y] = PI_CYCLINDER



def build_potential_table():
    table = [0] * Y_SCALE
    for i in range(len(table)):
        table[i] = [0] * X_SCALE
    init_table(table)
    print_table(table)


if __name__ == '__main__':
    build_potential_table()
