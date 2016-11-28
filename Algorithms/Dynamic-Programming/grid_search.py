'''
A robot is in a grid and it needs to figure out a way to get from the top left of the grid
to the bottom right of the grid. At any time, it can only take 1 step. It cannot visit some squares because
they are filled with Arts majors and it doesn't like them.
'''


def find_path(matrix, row, column, route, storage):
    if column < 0 or row < 0 or (matrix[row][column] is False):
        return False
    curr = (row, column)

    if curr in storage:
        return storage[curr]

    done_iter = False
    origin = row == 0 and column == 0

    if origin or find_path(matrix, row-1, column, route, storage) or find_path(matrix, row, column-1, route, storage):
        route.append(curr)
        done_iter = True

    storage[curr] = done_iter
    return done_iter


def main():
    matrix = list()
    rows, columns = list(map(int, input().split(' ')))
    for i in range(rows):
        a = list(map(int, input().split(' ')))
        matrix.append(a)
    route = list()
    if find_path(matrix, rows, columns, route, dict()):
        return route
    return None
