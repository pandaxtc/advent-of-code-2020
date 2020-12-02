import re

num_valid = 0
r = re.compile('^(\d+)-(\d+) ([a-z]): (\w+)$')
for line in open('in').readlines():
    a, b, c, s = re.match(r, line).groups()
    a = int(a)
    b = int(b)
    num = 0
    for ch in s:
        if ch == c:
            num += 1
    if a <= num <= b:
        num_valid += 1
print(num_valid)
    