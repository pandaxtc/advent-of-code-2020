from collections import defaultdict

has = defaultdict(dict)
for line in open('in').readlines():
    words = line.split(' ')
    color = words[0] + words[1]
    print(f'==========checking {line} with color {color}')
    words = words[4:]
    for i in range(len(words) // 4):
        num = int(words[4*i])
        other_color = words[4*i + 1] + words[4*i + 2]
        print(f'other color {other_color}')
        has[color][other_color] = num
    print(has[color])

def r(color):
    print(f'color {color} with {has[color]} can hold {sum(r(other_color) * has[color][other_color] for other_color in has[color])} bags')
    if len(has[color]) == 0:
        return 0
    return sum((r(other_color) + 1) * has[color][other_color] for other_color in has[color])

print(r('shinygold'))

    