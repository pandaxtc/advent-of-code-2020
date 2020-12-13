dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
deg = 0
x, y = 0, 0

for line in open('in').readlines():
  command = line[0]
  amt = int(line[1:])
  print(command, amt)
  if command == 'N':
    y += amt
  elif command == 'S':
    y -= amt
  elif command == 'E':
    x += amt
  elif command == 'W':
    x -= amt
  elif command == 'L':
    deg = (deg + amt) % 360
  elif command == 'R':
    deg = (deg - amt) % 360
  elif command == 'F':
    delta = dirs[deg // 90]
    x += delta[0] * amt
    y += delta[1] * amt

print(abs(x) + abs(y))

