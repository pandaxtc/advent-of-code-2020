nums = [int(line) for line in open('in').readlines()]
nums.sort()
nums.append(nums[-1] + 3)
numsset = set(nums)

dp = [1, 1, 2, 4] #dp[i] is the number of paths to reach i
# this could be more space efficient but fuck it
for idx in range(4, nums[-1] + 1):
  dp.append(0)
  if idx in numsset:
    dp[idx] += sum(dp[idx - delta] for delta in range(1, 4))
  print(f'dp[{idx}] is {dp[idx]}')

print(f'answer is {dp[-1]}')

