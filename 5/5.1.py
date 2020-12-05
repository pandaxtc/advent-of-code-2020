max_sid = 0
# a cool dude pointed out to me that you can directly convert BFBFBF... to binary
for line in open('in').readlines():
    row = [0, 127]
    seat = [0, 7]
    for c in line:
        if c == 'F':
            row[1] = row[0] + (row[1] - row[0]) // 2
        if c == 'B':
            row[0] = row[0] + (row[1] - row[0]) // 2 + 1
        if c == 'R':
            seat[0] = seat[0] + (seat[1] - seat[0]) // 2 + 1
        if c == 'L':
            seat[1] = seat[0] + (seat[1] - seat[0]) // 2
        print(f'char {c}, row is now {row}')
    assert row[0] == row[1], f'Row mismatch {row}'
    assert seat[0] == seat[1], f'Seat mismatch {seat}'
    max_sid = max(row[0] * 8 + seat[0], max_sid)
print(max_sid)