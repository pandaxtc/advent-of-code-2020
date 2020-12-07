yes_questions = None
total_questions = 0
for line in open('in').readlines():
    if line == '\n':
        total_questions += len(yes_questions)
        yes_questions = None
        continue

    if yes_questions is None:
        yes_questions = set(line.strip())
    else:
        yes_questions &= set(line.strip())

total_questions += len(yes_questions)
print(total_questions)