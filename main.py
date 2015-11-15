# coding=utf-8
from random import shuffle, seed
import argparse

N, S, E, W = 'N', 'S', 'E', 'W'
DX = {E: 1, W: -1, N: 0, S: 0}
DY = {E: 0, W: 0, N: -1, S: 1}
OPPOSITE = {E: W, W: E, N: S, S: N}

WALL_CHAR = "█"


class Maze:
    """
    Representation of the maze
    """
    height = 0
    width = 0
    container = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.container = self.initiate()

    def __str__(self):
        """
        Used for debugging purposes
        :return:
        """
        return "Maze H: {} - W: {}".format(self.height, self.width)

    def print_maze(self):
        """
        Make a text representation of the maze
        :return:
        """
        ascii_maze = "{}".format(WALL_CHAR) * (self.width * 2 + 1) + "\n"
        for row in self.container:
            ascii_maze += "{}".format(WALL_CHAR)
            for cell in row:
                if E in cell.carve_direction:
                    ascii_maze += "  "
                else:
                    ascii_maze += " {}".format(WALL_CHAR)
            ascii_maze += "\n{}".format(WALL_CHAR)
            for cell in row:
                if S in cell.carve_direction:
                    ascii_maze += " {}".format(WALL_CHAR)
                else:
                    ascii_maze += "{}".format(WALL_CHAR) * 2
            ascii_maze += "\n"
        print ascii_maze

    def initiate(self):
        """
        Make a 2D list of empty Cell objects
        :return:
        """
        m = list()
        for y in range(self.height):
            row = list()
            for x in range(self.width):
                row.append(Cell(x, y))
            m.append(row)
        return m

    def carve_passages_from(self, cx, cy):
        """
        Recursively generate maze hallways using Recursive Backtracking
        :param cx:
        :param cy:
        :return:
        """
        directions = [N, S, E, W]
        # Shuffle is affected by the seed if provided
        shuffle(directions)
        for direction in directions:
            nx = cx + DX[direction]
            ny = cy + DY[direction]
            if (0 <= ny < self.height) and (0 <= nx < self.width) and len(self.container[ny][nx].carve_direction) == 0:
                self.container[cy][cx].carve_direction.append(direction)
                self.container[ny][nx].carve_direction.append(OPPOSITE[direction])
                self.carve_passages_from(nx, ny)


class Cell:
    """
    Representation of a Cell
    Connected Cells are the hallways of the Maze
    """
    x = 0
    y = 0
    carve_direction = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.carve_direction = list()

    def __str__(self):
        """
        Used for debugging purposes
        :return:
        """
        return "{}".format(", ".join(self.carve_direction))


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--height', '-hh', dest='height', help='Height of the maze',
                        type=int, required=False, default=18)
    parser.add_argument('--width', '-ww', dest='width', help='Width of the maze',
                        type=int, required=False, default=50)
    parser.add_argument('--seed', '-s', dest='seed', help='String that serves as seed for the Maze',
                        type=str, required=False, default=None)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    if args.seed:
        seed(args.seed)
    maze = Maze(args.height, args.width)
    maze.carve_passages_from(0, 0)
    maze.print_maze()
