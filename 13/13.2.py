import sys

f = open('in')
mins = int(f.readline())
buses = [int(bus) if bus != 'x' else None for bus in f.readline().strip().split(',')]

for idx, bus in enumerate(buses):
  if bus is None:
    continue
  print(f'{-idx % bus} mod {bus}')

'''
0 mod 13
30 mod 37
448 mod 461
7 mod 17
6 mod 19
16 mod 29
695 mod 739
28 mod 41
2 mod 23
'''

# im giving up and plugging this system into a calculator lol
