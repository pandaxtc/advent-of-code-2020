ops = open('in').readlines()

for mut_idx in range(len(ops)):
  execed = set()
  acc = 0
  ptr = 0
  while ptr not in execed:
    #print(ptr, execed)
    line = ops[ptr]
    op = line[:3] 

    if ptr == mut_idx:
      if op == 'jmp':
        op = 'nop'
      elif op == 'nop':
        op = 'jmp'
    
    if op == 'jmp':
      ptr += int(line[3:]) - 1
    elif op == 'acc':
      acc += int(line[3:])
    execed.add(ptr)
    ptr += 1
    if ptr == len(ops):
      print(acc)
      exit()
