from itertools import islice

nums = [int(line) for line in open('in').readlines()]
low = nums[0]
prev25 = set(islice(nums, 0, 25))

for idx, num in enumerate(islice(nums, 25, None)):
  canbeformed = False
  for addend in prev25:
    if num - addend in prev25:
      canbeformed = True
      break
  if not canbeformed:
    print(num)
    break
  prev25.add(num)
  prev25.remove(low)
  low = nums[idx + 1]
