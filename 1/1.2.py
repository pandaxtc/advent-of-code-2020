
nums = set([int(n) for n in open('in').readlines()])

for num1 in nums:
    for num2 in nums:
        if num1 == num2:
            continue
        if 2020 - num1 - num2 in nums:
            print(num1 * num2 * (2020 - num1 - num2))
            break
    