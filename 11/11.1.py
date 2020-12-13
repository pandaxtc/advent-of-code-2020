room = [line.strip() for line in open('in').readlines()]
next_room = [[None] * len(room[0]) for _ in range(len(room))]
print('\n'.join(room))

changes = 1
while changes != 0:
  changes = 0
  for row, line in enumerate(room):
    for col, seat in enumerate(line):
      if seat == '.' or seat is None:
        next_room[row][col] = '.'
        continue
      num_adj = 0
      for offset_row in (-1, 0, 1):
        for offset_col in (-1, 0, 1):
          if (row + offset_row < 0 or 
              col + offset_col < 0 or
              row + offset_row >= len(room) or
              col + offset_col >= len(room[0]) or
              offset_col == offset_row == 0):
            continue
          #print(row + offset_row, offset_col + col, len(room), len(room[0]))
          if room[row + offset_row][col + offset_col] == '#':
            num_adj += 1
      if num_adj == 0:
        if room[row][col] != '#':
          changes += 1
        next_room[row][col] = '#'
      elif num_adj >= 4:
        if room[row][col] != 'L':
          changes += 1
        next_room[row][col] = 'L'
      else:
        next_room[row][col] = room[row][col]
  #print(changes)
  room = next_room
  #print('\n'.join(''.join(l) for l in room))
  next_room = [[None] * len(room[0]) for _ in range(len(room))]

print(sum(line.count('#') for line in room))

