def val_byr(n):
	return 1920 <= int(n) <= 2002 and len(n) == 4
def val_iyr(n):
	return 2010 <= int(n) <= 2020 and len(n) == 4
def val_eyr(n):
	return 2020 <= int(n) <= 2030 and len(n) == 4
def val_hgt(n):
	if n.endswith('cm'):
		i = n[0:3]
		try:
			return 150 <= int(i) <= 193 and len(n) == 5
		except ValueError:
			return False
	if n.endswith('in'):
		i = n[0:2]
		try:
			return 59 <= int(i) <= 76 and len(n) == 4
		except ValueError:
			return False
def val_hcl(n):
	try:
		int(n[1:], 16)
		return n.startswith('#') and len(n) == 7
	except ValueError:
		return False
def val_ecl(n):
	return n in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
def val_pid(n):
	return len(n) == 9

valid_passports = 0

fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
validators = (val_byr, val_iyr, val_eyr, val_hgt, val_hcl, val_ecl, val_pid)

has_fields = [False, False, False, False, False, False, False]
for line in open('in').readlines():
	if line == '\n':
		if all(has_fields):
			valid_passports += 1
		has_fields = [False, False, False, False, False, False, False]	
		continue

	for word in line.split():
		if word == '':
			continue
		for idx, field in enumerate(fields):
			if word.startswith(field):
				value = word[4:]
				if validators[idx](value):
					has_fields[idx] = True
				break


if all(has_fields):
	valid_passports += 1

print(valid_passports)

