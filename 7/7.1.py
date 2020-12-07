from collections import defaultdict

can_hold = defaultdict(list)
for line in open('in').readlines():
    words = line.split(' ')
    color = words[0] + words[1]
    words = words[4:]
    for i in range(len(words) // 4):
        other_color = words[4*i + 1] + words[4*i + 2]
        can_hold[other_color].append(color)

shinies = can_hold['shinygold']
good_colors = set()
idx = 0
while idx < len(shinies):
    if shinies[idx] not in good_colors:
        good_colors.add(shinies[idx])
        shinies += can_hold[shinies[idx]]
    idx += 1
print(len(good_colors))

    