sids = set()
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
    assert row[0] == row[1], f'Row mismatch {row}'
    assert seat[0] == seat[1], f'Seat mismatch {seat}'
    sids.add(row[0] * 8 + seat[0])
print(set(range(min(sids), max(sids))) - sids)