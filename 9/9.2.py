from itertools import islice

nums = [int(line) for line in open('in').readlines()]
low = nums[0]
prev25 = set(islice(nums, 0, 25))

ans = None # 466456641
           # 52858841
for idx, num in enumerate(islice(nums, 25, None)):
  canbeformed = False
  for addend in prev25:
    if num - addend in prev25:
      canbeformed = True
      break
  if not canbeformed:
    ans = num
    break
  prev25.add(num)
  prev25.remove(low)
  low = nums[idx + 1]

s = 0
low = 0
high = 0
for idx, num in enumerate(nums):
  s += num
  high = idx
  if s > ans:
    while s > ans:
      s -= nums[low]
      low += 1
  if s == ans:
    print(s, low, high)
    print(min(nums[low:high + 1]) + max(nums[low:high + 1]))
    break
print(sum(nums[low:high + 1]))