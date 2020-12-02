import re

num_valid = 0
r = re.compile('^(\d+)-(\d+) ([a-z]): (\w+)$')
for line in open('in').readlines():
    a, b, c, s = re.match(r, line).groups()
    a = int(a)
    b = int(b)
    if (s[a - 1] == c) != (s[b - 1] == c):
        num_valid += 1
print(num_valid)