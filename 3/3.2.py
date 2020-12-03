
from functools import reduce

lines = [l for l in open('in').readlines()]

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
num_trees = []
for down, right in slopes:
    row, col, num = 0, 0, 0
    while row < len(lines):
        print(f'examining row {row} col {col} ll {len(lines[0])}')
        if lines[row][col] == '#':
            num += 1
        col += right
        if col >= (len(lines[0]) - 1):
            col -= (len(lines[0]) - 1)
        row += down
    num_trees.append(num)

print(num_trees)
print(reduce(lambda x, y: x*y, num_trees))
