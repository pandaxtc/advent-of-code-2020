execed = set()
ops = open('in').readlines()
acc = 0
ptr = 0
while ptr not in execed:
  print(ptr, execed)
  line = ops[ptr]
  op = line[:3] 
  if op == 'jmp':
    ptr += int(line[3:]) - 1
  elif op == 'acc':
    acc += int(line[3:])
  execed.add(ptr)
  ptr += 1
print(acc)
