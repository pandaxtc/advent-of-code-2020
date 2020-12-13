from math import cos, sin, radians

deg = 0
w_x, w_y, x, y = 10, 1, 0, 0

for line in open('in').readlines():
  command = line[0]
  amt = int(line[1:])
  print(command, amt)
  if command == 'N':
    w_y += amt
  elif command == 'S':
    w_y -= amt
  elif command == 'E':
    w_x += amt
  elif command == 'W':
    w_x -= amt
  elif command == 'L':
    amt = radians(amt) # i swear to god, linear algebra feels like black magic sometimes
    w_x, w_y = round(cos(amt) * w_x) - round(sin(amt) * w_y), round(sin(amt) * w_x) + round(cos(amt) * w_y)
    print(f'calculated w_x and w_y to be {w_x, w_y}')
  elif command == 'R':
    amt = radians(amt)
    w_x, w_y = round(cos(-amt) * w_x) - round(sin(-amt) * w_y), round(sin(-amt) * w_x) + round(cos(-amt) * w_y)
    print(f'calculated w_x and w_y to be {w_x, w_y}')
  elif command == 'F':
    x += w_x * amt
    y += w_y * amt

print(abs(x) + abs(y))

