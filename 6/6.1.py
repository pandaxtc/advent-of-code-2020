yes_questions = set()
total_questions = 0
for line in open('in').readlines():
    if line == '\n':
        total_questions += len(yes_questions)
        yes_questions = set()
        continue

    yes_questions |= set(line.strip())

total_questions += len(yes_questions)
print(total_questions)