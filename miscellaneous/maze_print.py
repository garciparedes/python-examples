import random

U_SYMBOL = '_'
S_SYMBOL = ' '
V_SYMBOL = '|'
B_SYMBOL = '\n'


def generate_random_maze(rows, columns):
    dist = [0] * 3 + [1] * 1
    return [[random.choice(dist) for i in range(columns)] for j in range(rows)]


def stringify_list_2d(list_2d):
    s = ''
    for row in list_2d:
        for column in row:
            s += str(column) + S_SYMBOL
        s += B_SYMBOL
    return s


def stringify_maze(maze):
    s = ''
    for i in range(len(maze)):
        if i == 0:
            s += S_SYMBOL
            for j in range(len(maze[i])):
                s += U_SYMBOL + S_SYMBOL
            s += B_SYMBOL
        s += V_SYMBOL
        for j in range(len(maze[i])):
            if i == len(maze) - 1 or maze[i][j] != maze[i + 1][j]:
                s += U_SYMBOL
            else:
                s += S_SYMBOL
            if j == len(maze[i]) - 1 or maze[i][j] != maze[i][j + 1]:
                s += V_SYMBOL
            else:
                s += S_SYMBOL
        s += B_SYMBOL
    return s


def print_maze(maze):
    print(stringify_maze(maze))


def print_list_2d(list_2d):
    print(stringify_list_2d(list_2d))


if __name__ == '__main__':
    rows = 20
    columns = 30
    maze = generate_random_maze(rows, columns)
    print_list_2d(maze)
    print_maze(maze)
