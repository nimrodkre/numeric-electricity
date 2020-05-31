import math
import cylinders

def distance(point1, point2):
    return math.sqrt(math.pow(point1[0] - point2[0], 2) +
                     math.pow(point1[1] - point2[1], 2))
class ElectricField:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
    def __str__(self):
        print(f"x={self.x}, y={self.y}, z={self.z}")

def derivitive(table):
    delta=1/SCALE
    derTable=np.empty( (SCALE,SCALE), dtype=ElectricField)
    # calculate derivitive by x hat.
    for i in range(SCALE):
        for j in range(SCALE-1):
            derTable[j][i].x=(table[j+1][i]-table[j][i])/delta
    #calculate derivitive by y hat.
    for i in range(SCALE):
        for j in range(SCALE-1):
            derTable[i][j].y=(table[i][j]-table[i][j])/delta
    # zero Z hat values
    for i in range(SCALE):
        for j in range(SCALE):
            derTable[i][j].z=0