import random
import sys
from dataclasses import dataclass

import numpy as np

block = "█"
blank = " "


@dataclass
class position:
    x: int
    y: int
    path: bool


def display_matrix(matrix):
    """
    Visually displays a matrix
    """
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            val = matrix[x][y]
            if val == 0:
                sys.stdout.write(block)
            else:
                sys.stdout.write(blank)
        sys.stdout.write("\n")
    return


class SimpleMazeGenerator:
    def __init__(self, dimension: tuple):

        x = dimension[0]
        y = dimension[1]
        self.dimension = dimension
        self.matrix = np.zeros((x, y))

        self.start = (random.randint(0, x - 1), random.randint(0, y - 1))

    def generate(self):
        x = self.start[0]
        y = self.start[1]

        stack = [(x, y)]
        focus = stack[0]
        while len(stack) > 0:
            x = focus[0]
            y = focus[1]
            self.matrix[x][y] = 1
            neighbors = self.get_neighbors(x, y)
            unvisited = []
            for n in neighbors:
                if not self.is_wall(n[0], n[1]):
                    unvisited.append(n)
            if len(unvisited) > 0:
                focus = random.choice(unvisited)
                stack.append(focus)
            else:
                focus = stack.pop()

    def get_neighbors(self, x_pos, y_pos):
        x_bound = len(self.matrix)
        y_bound = len(self.matrix[0])

        neighbors = []
        # left
        if x_pos - 1 >= 0:
            neighbors.append((x_pos - 1, y_pos))
        # right
        if x_pos + 1 < x_bound:
            neighbors.append((x_pos + 1, y_pos))
        # up
        if y_pos - 1 >= 0:
            neighbors.append((x_pos, y_pos - 1))
        # down
        if y_pos + 1 < y_bound:
            neighbors.append((x_pos, y_pos + 1))
        return neighbors

    def is_wall(self, x_pos, y_pos):
        neighbors = self.get_neighbors(x_pos, y_pos)
        paths = 0
        for pos in neighbors:
            if self.matrix[pos[0]][pos[1]] == 1:
                paths += 1
        if paths <= 1:
            return False
        else:
            return True

    def demo(self):
        print(self.get_neighbors(1, 1))
        print(self.is_wall(1, 1))
        self.generate()


if __name__ == "__main__":

    generator = SimpleMazeGenerator((30, 30))
    generator.demo()
    display_matrix(generator.matrix)

    # print(basic_maze(10))

    # display_matrix(np.identity(3))
