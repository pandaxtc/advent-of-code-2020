nums = [int(line) for line in open('in').readlines()]
nums.sort()
print(nums)

onediff = 0
threediff = 0
prev = 0
for num in nums:
  delta = num - prev
  print(delta)
  if delta == 1:
    onediff += 1
  elif delta == 3:
    threediff += 1
  prev = num
print(onediff * (threediff + 1))
