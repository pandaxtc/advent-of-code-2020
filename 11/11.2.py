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
          chk_row = row + offset_row
          chk_col = col + offset_col
          while not (chk_row < 0 or 
                     chk_col < 0 or
                     chk_row >= len(room) or
                     chk_col >= len(room[0]) or
                     offset_col == offset_row == 0):
              if room[chk_row][chk_col] == 'L':
                break
              if room[chk_row][chk_col] == '#':
                num_adj += 1
                break
              chk_row += offset_row
              chk_col += offset_col
      if num_adj == 0:
        if room[row][col] != '#':
          changes += 1
        next_room[row][col] = '#'
      elif num_adj >= 5:
        if room[row][col] != 'L':
          changes += 1
        next_room[row][col] = 'L'
      else:
        next_room[row][col] = room[row][col]
  room = next_room
  next_room = [[None] * len(room[0]) for _ in range(len(room))]

print(sum(line.count('#') for line in room))
