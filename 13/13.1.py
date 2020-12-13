f = open('in')
mins = int(f.readline())
buses = [int(bus) for bus in f.readline().strip().split(',') if bus != 'x']

nearest_bus = None
mins_wait = 0
min_del = mins
for bus in buses:
  delta = bus - (mins % bus)
  if delta == bus:
    delta = 0
  if delta < min_del:
    min_del = delta
    nearest_bus = bus
    mins_wait = mins + delta
    assert mins_wait % bus == 0

print((mins_wait - mins) * nearest_bus)
