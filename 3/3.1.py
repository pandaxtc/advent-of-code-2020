lines = [l for l in open('in').readlines()]

row = 0
col = 0
num_trees = 0
while row != len(lines):
    print(f'examining row {row} col {col} ll {len(lines[0])}')
    if lines[row][col] == '#':
        num_trees += 1
    col += 3
    if col >= (len(lines[0]) - 1):
        col -= (len(lines[0]) - 1)
    row += 1

print(num_trees)
