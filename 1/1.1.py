
nums = set([int(n) for n in open('in').readlines()])

for num in nums:
    if 2020 - num in nums:
        print(num * (2020 - num))
        break
    