'''
 # @ Author: Antoine Deligny
 # @ Create Time: 2019-11-24 14:57:49
 # @ Description:
 '''

import math
from typing import Tuple
import sys


class MatrixTransformer:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.result_x = 0
        self.result_y = 0

    def translation(self, i: int, j: int) -> None:
        print(f"Translation by the vector ({i}, {j})")
        matrix = [
            [1.00, 0.00, i],
            [0.00, 1.00, j],
            [0.00, 0.00, 1.00]
        ]
        self.transform(matrix)

    def homothety(self, i: int, j: int) -> None:
        print(f"Homothety by the ratios {i} and {j}")
        matrix = [
            [i, 0.00, 0.00],
            [0.00, j, 0.00],
            [0.00, 0.00, 1.00]
        ]
        self.transform(matrix)

    def rotation(self, angle: int) -> None:
        a = math.radians(angle)
        print(f"Rotation at a {angle} degree angle")
        matrix = [
            [math.cos(a), -math.sin(a), 0.00],
            [math.sin(a), math.cos(a), 0.00],
            [0.00, 0.00, 1.00]
        ]
        self.transform(matrix)

    def symmetry(self, angle: int) -> None:
        a = math.radians(angle)
        print(f"Symmetry about an axis inclined with an angle of {angle} degrees")
        matrix = [
            [math.cos(2 * a), math.sin(2 * a), 0.00],
            [math.sin(2 * a), -math.cos(2 * a), 0.00],
            [0.00, 0.00, 1.00]
        ]
        self.transform(matrix)

    def transform(self, matrix: list) -> None:
        self.result_x = matrix[0][0] * self.x + matrix[0][1] * self.y + matrix[0][2]
        self.result_y = matrix[1][0] * self.x + matrix[1][1] * self.y + matrix[1][2]
        print(f"({self.x},{self.y}) => ({self.result_x:.2f},{self.result_y:.2f})")


if __name__ == "__main__":
    if len(sys.argv) != 5 and len(sys.argv) != 6:
        exit(84)

    x_val = int(sys.argv[1])
    y_val = int(sys.argv[2])
    transformer = MatrixTransformer(x_val, y_val)

    if sys.argv[3] == "-t" and len(sys.argv) == 6:
        i_val = int(sys.argv[4])
        j_val = int(sys.argv[5])
        transformer.translation(i_val, j_val)

    elif sys.argv[3] == "-h" and len(sys.argv) == 6:
        i_val = int(sys.argv[4])
        j_val = int(sys.argv[5])
        transformer.homothety(i_val, j_val)

    elif sys.argv[3] == "-r" and len(sys.argv) == 5:
        angle_val = int(sys.argv[4])
        transformer.rotation(angle_val)

    elif sys.argv[3] == "-s" and len(sys.argv) == 5:
        angle_val = int(sys.argv[4])
        transformer.symmetry(angle_val)
