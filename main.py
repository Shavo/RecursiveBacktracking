import argparse


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
        ascii_maze = " " + "_" * (self.width * 2) + "\n"
        for row in self.container:
            ascii_maze += '|'
            for cell in row:
                ascii_maze += ' |'
            ascii_maze += '\n'
        ascii_maze += " " + "_" * (self.width * 2) + "\n"
        return ascii_maze

    def initiate(self):
        maze = list()
        for y in range(self.height):
            row = list()
            for x in range(self.width):
                row.append(Cell(x, y))
            maze.append(row)
        return maze

    def carve_passage_from(self, cx, cy, grid):
        pass


class Cell:
    x = 0
    y = 0
    carve_direction = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


def parse_arguments():
    """
    parse command line arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--height', '-hh', dest='height', help='Height of the maze',
                        type=int, required=False, default=10)
    parser.add_argument('--width', '-ww', dest='width', help='Width of the maze',
                        type=int, required=False, default=10)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    maze = Maze(args.height, args.width)
    print maze