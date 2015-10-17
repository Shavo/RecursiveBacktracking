from random import shuffle
import argparse

N, S, E, W = 'N', 'S', 'E', 'W'
DX = {E: 1, W: -1, N: 0, S: 0}
DY = {E: 0, W: 0, N: -1, S: 1}
OPPOSITE = {E: W, W: E, N: S, S: N}


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
        return "Maze H: {} - W: {}".format(self.height, self.width)

    def print_maze(self):
        ascii_maze = " " + "_" * (self.width * 2) + "\n"
        for row in self.container:
            ascii_maze += '|'
            for cell in row:
                ascii_maze += " " if ((cell.carve_direction and S) != 0) else "_"
                if cell.carve_direction and E != 0:
                    ascii_maze += " " if ((cell.carve_direction or row[cell.x + 1].carve_direction) and S) != 0 else "_"
                else:
                    ascii_maze += "|"
            ascii_maze += '\n'
        ascii_maze += " " + "_" * (self.width * 2) + "\n"
        print ascii_maze

    def initiate(self):
        m = list()
        for y in range(self.height):
            row = list()
            for x in range(self.width):
                row.append(Cell(x, y))
            m.append(row)
        return m

    def carve_passages_from(self, cx, cy):
        directions = [N, S, E, W]
        shuffle(directions)
        for direction in directions:
            nx = cx + DX[direction]
            ny = cy + DY[direction]
            if (0 <= ny < self.height) and (0 <= nx < self.width) and not self.container[ny][nx].carve_direction:
                self.container[cy][cx].carve_direction.append(direction)
                self.container[ny][nx].carve_direction.append(OPPOSITE[direction])
                self.carve_passages_from(nx, ny)


class Cell:
    x = 0
    y = 0
    carve_direction = list()

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
    maze.carve_passages_from(0, 0)
    maze.print_maze()
